from app.connectors.serpapi.google_search import search_google
from app.models.product import Product
from app.models.research_packet import ResearchPacket
from app.services.github_research import research_github
from app.services.query_generator import generate_queries
from app.services.youtube_research import research_youtube


def build_research_packet(product: Product) -> ResearchPacket:
    hypotheses = generate_queries(product)

    google_signals = []

    for hypothesis in hypotheses:
        signals = search_google(hypothesis)
        google_signals.extend(signals)

    youtube_signals = []

    youtube_queries = [
        f"{product.name} Python",
        f"{product.name} tutorial",
    ]

    for query in youtube_queries:
        youtube_signals.extend(
            research_youtube(
                query=query,
                product_name=product.name,
            )
        )

    github_signals = research_github(product)

    return ResearchPacket(
        product=product,
        google_search=google_signals,
        youtube=youtube_signals,
        google_trends=[],
        github=github_signals,
    )