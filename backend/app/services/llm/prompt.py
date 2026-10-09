from app.models.evidence_cluster import EvidenceCluster
from app.models.product import Product
from app.models.trend_signal import TrendSignal


def build_research_synthesis_prompt(
    product: Product,
    clusters: list[EvidenceCluster],
    trends: list[TrendSignal],
) -> str:

    cluster_blocks = []

    for cluster in clusters:
        evidence_blocks = []

        for evidence_index, item in enumerate(
            cluster.evidence,
            start=1,
        ):
            evidence_blocks.append(
                f"""
Evidence {evidence_index}
Source: {item.source}
Source role: {item.source_role}
Title: {item.title}
URL: {item.url}
Query: {item.query or ""}
Text: {item.text or ""}
Relevance score: {item.relevance_score}
""".strip()
            )

        cluster_blocks.append(
    f"""
CLUSTER: {cluster.key}

{"\n\n".join(evidence_blocks)}
""".strip()
)

    evidence_block = "\n\n---\n\n".join(cluster_blocks)

    trend_blocks = []

    for trend in trends:
        trend_blocks.append(
            f"""
Trend query: {trend.query}
Trend direction: {trend.trend_direction}
Related topics: {", ".join(trend.related_topics)}
Related queries: {", ".join(trend.related_queries)}
Interest over time: {trend.interest_over_time}
""".strip()
        )

    trend_block = "\n\n---\n\n".join(trend_blocks)

    return f"""
You are analyzing developer research for a developer-focused company.

PRODUCT

Name: {product.name}
Website: {product.website}
Target audience: {product.targetAudience}
Primary goal: {product.primary_goal}

You have been given two types of research:

1. Evidence clusters from Google Search, GitHub, and YouTube.
2. Google Trends signals derived from research topics.

Your job is to synthesize the research into evidence-based developer
and GTM insights.

IMPORTANT RULES:

1. Use only the supplied evidence and trend signals.
2. Do not invent developer experiences, market demand, competitors,
   or trends.
3. Do not treat the number of evidence items as the number of developers.
4. Do not claim that a problem is widespread unless the evidence
   supports that conclusion.
5. Educational content is not automatically evidence of a problem.
6. Implementation content is not automatically evidence of a problem.
7. Integration content is not automatically evidence of a problem.
8. GitHub issues are evidence of reported technical problems, but a
   single issue does not prove widespread demand.
9. YouTube content is useful for understanding the content landscape
   and developer/community interests. It is not automatically proof
   of a developer problem.
10. Google Trends indicates search interest, not confirmed product usage
    or developer pain.
11. A rising trend does not by itself prove a valuable market opportunity.
12. A declining trend does not automatically mean the underlying problem
    is unimportant.
13. Distinguish evidence from inference.
14. Keep uncertainty explicit.
15. Do not use general knowledge to fill evidence gaps.
16. Every developer problem must reference the cluster that supports it.
17. Every conclusion must be traceable to supplied evidence or trends.
18. Return valid JSON only.

DEVELOPER PROBLEMS

Identify genuine developer problems demonstrated by the evidence.

A problem should represent something developers are actually struggling
to accomplish, understand, integrate, debug, or use.
- Never use words such as "frequently", "widely", "common",
  "many developers", "most developers", "often", or "prevalent"
  unless the supplied evidence explicitly supports the frequency claim.
- The number of supplied evidence items is not evidence of the number
  of developers experiencing a problem.
- Prefer "the supplied evidence shows", "the research identified",
  or "some reported cases" when scope is uncertain.
Do not create a problem merely because evidence contains words such as
"error", "issue", "tutorial", "integration", or "failure".

CONTENT GAPS

Identify potential content opportunities where the research indicates
developer interest or demand but the available content appears weak,
missing, fragmented, outdated, or insufficient.

Do not claim a content gap merely because there are few videos.

DEMAND SIGNALS

Use Google Trends and the supplied evidence to identify meaningful
signals of developer interest.

Clearly distinguish:

- search interest
- reported technical problems
- educational interest
- implementation activity

Do not equate them.

GTM RECOMMENDATIONS

Recommend concrete actions that follow from the evidence.

Recommendations may include:

- documentation improvements
- integration work
- developer onboarding
- technical content
- tutorials
- comparison content
- examples
- community engagement
- developer acquisition
- activation improvements


Do not recommend something merely because it is generally good GTM practice.

Every recommendation should have a clear connection to the supplied
research.

OUTPUT

Return exactly this JSON structure:

{{
  "developer_problems": [
    {{
      "cluster_id": "cluster_1",
      "title": "short problem title",
      "conclusion": "short evidence-based conclusion",
      "evidence_count": 0,
      "source_breakdown": {{}},
      "confidence": "low",
      "supporting_evidence": [],
      "limitations": [],
      "is_problem": true
    }}
  ],
  "conclusions": [
    "evidence-based conclusion"
  ],
  "demand_signals": [
    {{
      "query": "trend query",
      "direction": "rising",
      "interpretation": "what the signal actually indicates",
      "limitations": []
    }}
  ],
  "content_gaps": [
    {{
      "topic": "content topic",
      "reason": "why the research suggests a gap",
      "evidence": []
    }}
  ],
  "gtm_recommendations": [
    {{
      "recommendation": "specific action",
      "reason": "evidence-based reason",
      "priority": "high"
    }}
  ]
}}

FIELD RULES:

Developer problems:

- cluster_id must exactly match a supplied cluster key.
- title maximum 12 words.
- conclusion maximum 30 words.
- confidence must be "low", "medium", or "high".
- supporting_evidence maximum 3 titles.
- limitations maximum 2 items.
- evidence_count counts supporting evidence items only.
- source_breakdown counts supporting evidence items by source.
- is_problem is true only when an actual developer problem is demonstrated.

Conclusions:

- Maximum 5.
- Keep them specific and evidence-based.

Demand signals:

- Only include meaningful trend signals.
- Do not describe Google Trends as user counts.
- If a trend is unknown or unreliable, say so.

Content gaps:

- Maximum 5.
- Do not manufacture gaps.
- A content gap requires evidence of interest plus an apparent weakness
  in available content.

GTM recommendations:

- Maximum 5.
- Each recommendation must follow from the research.
- priority must be "high", "medium", or "low".

RESEARCH EVIDENCE

{evidence_block}

GOOGLE TRENDS

{trend_block if trend_block else "No Google Trends signals were successfully retrieved."}
""".strip()