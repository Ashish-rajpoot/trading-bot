from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RiskConfig:
    """
    Configuration for risk management.
    """

    risk_percent: float = 1.0

    max_trades_per_day: int = 3

    max_consecutive_losses: int = 3

    daily_loss_limit_percent: float = 3.0