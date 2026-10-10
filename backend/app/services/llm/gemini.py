import json

from google import genai

from app.models.evidence_cluster import EvidenceCluster
from app.models.product import Product
from app.models.research_synthesis import ResearchSynthesis
from app.models.trend_signal import TrendSignal
from app.services.llm.prompt import build_research_synthesis_prompt


MODEL_NAME = "gemini-3.5-flash-lite"


def synthesize_research(
    product: Product,
    clusters: list[EvidenceCluster],
    trends: list[TrendSignal],
) -> ResearchSynthesis:

    if not clusters:
        return ResearchSynthesis()

    client = genai.Client()

    prompt = build_research_synthesis_prompt(
        product=product,
        clusters=clusters,
        trends=trends,
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.removeprefix("```json").strip()
        raw_text = raw_text.removesuffix("```").strip()

    data = json.loads(raw_text)

    return ResearchSynthesis.model_validate(data)