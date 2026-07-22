from datetime import UTC, datetime, timedelta

from app.api.client import DeltaRestClient
from app.config.settings import settings
from app.exchange.market_data import MarketData
from app.indicators.ema_indicator import EMAIndicator


def test() -> None:

    client = DeltaRestClient(settings.base_url)

    market = MarketData(client)

    end = datetime.now(UTC)
    start = end - timedelta(hours=2)

    candles = market.get_candles(
        symbol=settings.symbol,
        resolution="1m",
        start=int(start.timestamp()),
        end=int(end.timestamp()),
    )

    indicator = EMAIndicator()

    df = indicator.calculate(candles)

    print(df.tail(10))


if __name__ == "__test__":
    test()