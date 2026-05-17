"""
Real-Time Social Media Event Detection and Misinformation Filtering
Using Streaming Analytics

Main Entry Point - Run this file to start the entire pipeline.
Group 1 | Section 41 | SOA University 2026

Usage:
    python main.py --mode simulate      # Run with simulated data (no Kafka needed)
    python main.py --mode kafka         # Run with real Kafka stream
    python main.py --mode dashboard     # Launch Streamlit dashboard only
    python main.py --mode evaluate      # Run full evaluation with metrics
"""

import argparse
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(
        description="Real-Time Social Media Event Detection & Misinformation Filtering"
    )
    parser.add_argument(
        "--mode",
        choices=["simulate", "kafka", "dashboard", "evaluate"],
        default="simulate",
        help="Execution mode"
    )
    parser.add_argument("--tweets", type=int, default=200, help="Number of simulated tweets")
    parser.add_argument("--batch-size", type=int, default=20, help="Streaming batch size")
    args = parser.parse_args()

    print("=" * 70)
    print("  Real-Time Social Media Event Detection & Misinformation Filtering")
    print("  Group 1 | Section 41 | SOA University 2026")
    print("=" * 70)

    if args.mode == "simulate":
        from src.pipeline import run_simulation_pipeline
        run_simulation_pipeline(num_tweets=args.tweets, batch_size=args.batch_size)

    elif args.mode == "kafka":
        from src.kafka_pipeline import run_kafka_pipeline
        run_kafka_pipeline()

    elif args.mode == "dashboard":
        print("Launching Streamlit Dashboard...")
        os.system("streamlit run dashboard/app.py")

    elif args.mode == "evaluate":
        from src.pipeline import run_simulation_pipeline
        from src.evaluator import Evaluator
        results = run_simulation_pipeline(num_tweets=500, batch_size=50)
        evaluator = Evaluator()
        evaluator.full_evaluation_report(results)


if __name__ == "__main__":
    main()
