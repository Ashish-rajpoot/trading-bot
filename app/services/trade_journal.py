from __future__ import annotations

import csv
from pathlib import Path
from datetime import datetime

from app.models.trade import Trade


class TradeJournal:
    """
    Stores all trades in a CSV file.
    """

    HEADER = [
        "Timestamp",
        "Symbol",
        "Signal",
        "Quantity",
        "Entry Price",
        "Stop Loss",
        "Take Profit",
        "Leverage",
        "Mode",
        "Status",
        "Order ID",
    ]

    def __init__(self, file_path: str = "logs/trades.csv") -> None:
        self._path = Path(file_path)

        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self._path.exists():
            with self._path.open(
                "w",
                newline="",
                encoding="utf-8",
            ) as file:
                writer = csv.writer(file)
                writer.writerow(self.HEADER)

    def log(self, trade: Trade) -> None:
        """
        Append a trade to the journal.
        """

        with self._path.open(
            "a",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    trade.symbol,
                    trade.signal.name,
                    trade.quantity,
                    trade.entry_price,
                    trade.stop_loss,
                    trade.take_profit,
                    trade.leverage,
                    trade.trading_mode,
                    trade.status,
                    trade.order_id,
                ]
            )