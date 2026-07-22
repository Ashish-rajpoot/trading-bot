from __future__ import annotations

from datetime import UTC, date, datetime

from app.risk.risk_config import RiskConfig


class RiskManager:
    """
    Responsible for enforcing portfolio level risk rules.
    """

    def __init__(self, config: RiskConfig) -> None:

        self._config = config

        self._trades_today = 0
        self._consecutive_losses = 0
        self._daily_loss_percent = 0.0
        self._current_day = datetime.now(UTC).date()

    def _reset_daily_stats(self) -> None:
        """
        Reset counters when a new UTC day starts.
        """
        today = datetime.now(UTC).date()

        if today != self._current_day:
            self._current_day = today
            self._trades_today = 0
            self._consecutive_losses = 0
            self._daily_loss_percent = 0.0

    def can_trade(self) -> tuple[bool, str]:
        """
        Check whether a new trade is allowed.
        """

        self._reset_daily_stats()

        if self._trades_today >= self._config.max_trades_per_day:
            return False, "Maximum trades reached."

        if (
            self._consecutive_losses
            >= self._config.max_consecutive_losses
        ):
            return False, "Maximum consecutive losses reached."

        if (
            self._daily_loss_percent
            >= self._config.daily_loss_limit_percent
        ):
            return False, "Daily loss limit reached."

        return True, "Trading allowed."

    def record_trade(
        self,
        pnl_percent: float,
    ) -> None:
        """
        Record the result of a completed trade.

        Parameters
        ----------
        pnl_percent
            Profit/loss expressed as a percentage of account equity.
            Positive = profit
            Negative = loss
        """

        self._reset_daily_stats()

        self._trades_today += 1

        if pnl_percent < 0:
            self._consecutive_losses += 1
            self._daily_loss_percent += abs(pnl_percent)
        else:
            self._consecutive_losses = 0