from pydantic import BaseModel

from app.models.github_signal import GitHubSignal
from app.models.product import Product
from app.models.signal import Signal
from app.models.trend_signal import TrendSignal
from app.models.youtube_signal import YouTubeSignal


class ResearchPacket(BaseModel):
    product: Product
    google_search: list[Signal]
    youtube: list[YouTubeSignal]
    google_trends: list[TrendSignal]
    github: list[GitHubSignal]