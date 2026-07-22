from __future__ import annotations


class PositionSizer:
    """
    Calculates position size based on account risk.
    """

    @staticmethod
    def calculate(
        account_balance: float,
        risk_percent: float,
        entry_price: float,
        stop_loss_price: float,
    ) -> float:
        """
        Calculate position size.

        Formula

        Risk Amount = Balance × Risk %

        Position Size =
            Risk Amount /
            abs(entry - stoploss)
        """

        if account_balance <= 0:
            raise ValueError("Account balance must be positive.")

        if entry_price == stop_loss_price:
            raise ValueError(
                "Entry price and stop loss cannot be equal."
            )

        risk_amount = (
            account_balance
            * risk_percent
            / 100
        )

        position_size = (
            risk_amount
            / abs(entry_price - stop_loss_price)
        )

        return round(position_size, 6)