#!/usr/bin/env python3
from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Initialize calendar
cal = Calendar()

# Start date (ADJUST THIS TO YOUR START DATE)
start_date = datetime(2025, 2, 7, tzinfo=pytz.utc)  # Example: January 1, 2024

# Weekly tasks for each phase (12 weeks per phase)
weekly_tasks = [
    # Phase 1: Core Math & Programming (Weeks 1–12)
    [
        "Week 1: Brownian Motion basics (Shreve Ch1-2) + numpy/pandas basics",
        "Week 2: Itô's Lemma (Shreve Ch3) + Monte Carlo basics",
        "Week 3: Stochastic Differential Equations (Shreve Ch4) + scipy/statsmodels",
        "Week 4: Linear Algebra refresher (PCA) + Portfolio Optimizer Project (Markowitz Setup)",
        "Week 5: Convex Optimization (Boyd Ch1-3) + Portfolio Optimizer Implementation",
        "Week 6: GBM Simulation Project (Code Structure)",
        "Week 7: Advanced GBM (Volatility clustering) + Debugging",
        "Week 8: Numerical Methods for SDEs (Euler-Maruyama)",
        "Week 9: Optimization in Python (CVXPY) + Project Refinement",
        "Week 10: Advanced Pandas (Time Series Manipulation)",
        "Week 11: Review Stochastic Calculus + Project Documentation",
        "Week 12: Phase 1 Wrap-up (Test Projects)"
    ],
    # Phase 2: Financial Theory & Products (Weeks 13–24)
    [
        "Week 13: Forwards/Futures (Hull Ch1-5) + Data Collection",
        "Week 14: Options Basics (Hull Ch6-9) + Black-Scholes Derivation",
        "Week 15: Implement Black-Scholes in Python",
        "Week 16: Binomial Trees (Hull Ch13) + Python Implementation",
        "Week 17: Fixed Income (Yield Curves, Duration) + Bond Pricing",
        "Week 18: Exotic Options (Barrier/Asian) + Monte Carlo Pricing",
        "Week 19: Volatility Models (GARCH) + Time Series Analysis",
        "Week 20: Backtest Volatility Strategy (GARCH + Historical Data)",
        "Week 21: Finite Difference Methods (Heat Equation)",
        "Week 22: Heston Model Basics + Calibration",
        "Week 23: Project: Exotic Option Pricing (Full Pipeline)",
        "Week 24: Phase 2 Wrap-up (Document Results)"
    ],
    # Phase 3: Advanced Quant Techniques (Weeks 25–36)
    [
        "Week 25: ML Basics (Regression/Classification) + sklearn",
        "Week 26: Predict Stock Returns (Feature Engineering)",
        "Week 27: Unsupervised Learning (Clustering for Portfolios)",
        "Week 28: Reinforcement Learning (Q-Learning Basics)",
        "Week 29: Algo-Trading Bot (Data Feed Setup)",
        "Week 30: Backtesting Framework (Vectorized vs Event-Driven)",
        "Week 31: Risk Metrics (VaR, CVaR) + Historical Simulation",
        "Week 32: Heston Model Calibration with MLE",
        "Week 33: Parallel Computing (Python Multiprocessing)",
        "Week 34: GPU Acceleration (CUDA Basics)",
        "Week 35: Project: Full Trading Strategy (Backtest + Report)",
        "Week 36: Phase 3 Wrap-up (Optimize Code)"
    ],
    # Phase 4: Professional Quant (Weeks 37–48)
    [
        "Week 37: Choose Track (Trading/Research/Risk) + Literature Review",
        "Week 38: Trading: Order Book Dynamics | Research: Local Volatility Models",
        "Week 39: Risk: Counterparty Risk (CVA/DVA) | Trading: Execution Algorithms",
        "Week 40: Bloomberg Terminal/Refinitiv Basics",
        "Week 41: Git Workflow (Branches, PRs) + Docker Containers",
        "Week 42: CI/CD Pipelines (GitHub Actions)",
        "Week 43: Mock Interviews (Brain Teasers)",
        "Week 44: Mock Interviews (Coding Challenges)",
        "Week 45: Revise Stochastic Calculus + PDEs",
        "Week 46: Network on LinkedIn/Attend Quant Meetups",
        "Week 47: Final Project: Full Portfolio (GitHub)",
        "Week 48: Job Applications + Final Prep"
    ]
]

# Create events for each week
current_date = start_date
for phase_idx, phase in enumerate(weekly_tasks):
    for week_idx, task in enumerate(phase):
        event = Event(
            name=f"Quant Roadmap: Phase {phase_idx+1}, Week {week_idx+1}",
            begin=current_date.strftime("%Y-%m-%d"),
            end=(current_date + timedelta(days=7)).strftime("%Y-%m-%d"),
            description=task
        )
        cal.events.add(event)
        current_date += timedelta(days=7)

# Save the calendar
with open("quant_weekly_tasks.ics", "w") as f:
    f.writelines(cal)