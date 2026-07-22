from app.api.client import DeltaRestClient
from app.bot.trading_bot import TradingBot
from app.config.settings import settings
from app.exchange.market_data import MarketData
from app.exchange.orders import Orders
from app.exchange.products import Products
from app.indicators.ema_indicator import EMAIndicator
from app.risk.risk_config import RiskConfig
from app.risk.risk_manager import RiskManager
from app.services.order_service import OrderService
from app.strategies.ema_strategy import EMAStrategy


client = DeltaRestClient(settings.base_url)

market = MarketData(client)

orders = Orders(client)

products = Products(client)

service = OrderService(
    orders=orders,
    products=products,
)

risk = RiskManager(
    RiskConfig(),
)

bot = TradingBot(
    market_data=market,
    indicator=EMAIndicator(),
    strategy=EMAStrategy(),
    risk_manager=risk,
    order_service=service,
)

bot.run()