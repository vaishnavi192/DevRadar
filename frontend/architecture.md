# DevRadar Architecture

Now replace the relevant source/pipeline sections with this:

```md
# DevRadar Architecture

## 1. Architecture Goal

Build the smallest system that can:

1. Accept a developer-focused product.
2. Generate relevant search hypotheses.
3. Collect external evidence through SerpApi.
4. Normalize evidence into DevRadar signals.
5. Group related signals.
6. Identify developer problems.
7. Generate actionable opportunities.
8. Return evidence-backed recommendations.

The architecture must remain understandable and modifiable by one developer.

---

# 2. Technology Stack

## Frontend

- React
- JavaScript
- Vite
- Tailwind CSS

## Backend

- Python
- FastAPI

## Database

- SQLite

## External Services

- SerpApi
- LLM provider, added after the deterministic pipeline works

---

# 3. High-Level Architecture

```text
                    React
                      │
                      │ HTTP
                      ↓
                  FastAPI
                      │
        ┌─────────────┼──────────────┐
        ↓             ↓              ↓
    Services      Connectors       Models
        │             │
        │             ↓
        │          SerpApi
        │
        ↓
    SQLite
4. Signal Pipeline
Product
   ↓
Search Hypotheses
   ↓
SerpApi Connectors
   ↓
Raw External Results
   ↓
Normalization
   ↓
Signals
   ↓
Clustering
   ↓
Developer Problems
   ↓
Opportunities
   ↓
GTM Actions

The core architectural unit is the normalized Signal.

5. Source → Signal Mapping
Source	Primary Signal
Google Search	Developer demand
Google Autocomplete	Search phrasing / demand discovery
YouTube Search	Developer education
YouTube Transcript	Tutorial coverage
Google Trends	Trend direction
Google News	Market/ecosystem changes
Google Forums	Developer conversations
Google Jobs	Technology/hiring signals
YouTube Channel	Creator/channel ecosystem
Yandex	Regional search behavior

External sources are evidence providers.

They should not define DevRadar's internal data model.

6. Connector Architecture

External APIs live under:

backend/
└── app/
    └── connectors/
        └── serpapi/

Initial connectors:

serpapi/
├── google_search.py
└── youtube.py

Later:

serpapi/
├── google_search.py
├── youtube.py
├── google_trends.py
├── google_news.py
├── google_forums.py
├── google_jobs.py
└── youtube_transcript.py

Do not create all these files now.

Create a connector only when that source is implemented.

7. Connector Responsibility

A connector should:

Accept the parameters required for a search.
Call SerpApi.
Handle provider-specific response details.
Return a predictable result to the application.

A connector should not:

Identify opportunities
Generate GTM recommendations
Contain product strategy
Call the frontend
Decide how signals are clustered
8. Normalization Boundary

SerpApi response:

Provider-specific JSON

should become:

DevRadar Signal

before reaching the rest of the application.

This prevents the application from becoming coupled to SerpApi's response structure.

9. Signal Model

A Signal represents an observation.

Potential fields:

source
source_type
title
url
snippet
query
metadata

Example:

{
  "source": "serpapi",
  "source_type": "google_search",
  "title": "How to use SerpApi with n8n",
  "url": "...",
  "snippet": "...",
  "query": "SerpApi n8n",
  "metadata": {}
}

The Signal must not contain AI-generated conclusions.

10. Product Model
name
website
targetAudience
docs_url
github_url
competitors
primary_goal
11. Search Query Generator

Location:

backend/app/services/query_generator.py

Responsibility:

Product
 ↓
Search hypotheses

It must not know about SerpApi.

Initial deterministic queries include:

[product] api
[product] python
[product] javascript
[product] tutorial
[product] example
[product] integration
[product] alternative
[product] vs

Later, product understanding and LLM reasoning may generate additional domain-specific hypotheses.

12. Services

Services contain application/business logic.

Potential structure:

backend/app/services/
├── query_generator.py
├── signal_normalizer.py
├── signal_clusterer.py
└── opportunity_engine.py

Do not create these files until their functionality is implemented.

13. AI Boundary

The deterministic pipeline must work without an LLM.

Initial:

Product
 ↓
Queries
 ↓
SerpApi
 ↓
Signals

Then introduce an LLM for:

Signals
 ↓
Problem interpretation
 ↓
Opportunity synthesis
 ↓
Recommendations

The LLM should receive structured evidence rather than arbitrary raw API responses.

Do not build a multi-agent system.

Do not create an LLM provider abstraction until multiple providers are actually required.

14. API

Initial endpoint:

POST /api/analyze

Input:

{
  "name": "...",
  "website": "...",
  "targetAudience": "...",
  "docs_url": null,
  "github_url": null,
  "competitors": [],
  "primary_goal": "Developer acquisition"
}

The endpoint eventually executes:

Product
 ↓
Query Generator
 ↓
Signal Collection
 ↓
Normalization
 ↓
Clustering
 ↓
Opportunity Engine
 ↓
Response
15. MVP Source Scope

Implement first:

Google Search
YouTube Search

Do not implement all SerpApi APIs simultaneously.

The purpose of the MVP is to prove that combining two complementary sources can generate useful developer opportunities.

After that works, expand the signal graph.

16. Expansion Order

Recommended sequence:

Stage 1
Google Search
YouTube Search
Stage 2
Google Autocomplete
Google Trends
Google News
Google Forums
Stage 3
YouTube Transcript
YouTube Channel
Google Jobs
Yandex

The order may change based on evidence from the MVP.

17. Architecture Rules
Keep source-specific logic inside connectors.
Normalize external responses before business logic.
Keep query generation independent from search providers.
Keep deterministic logic outside the LLM.
Do not create abstractions for hypothetical future providers.
Do not create unused connectors.
Do not create unused services.
Do not introduce a database layer before persistence is required.
Keep the API contract explicit.
Prefer simple functions over unnecessary classes.
Every feature must have a clear input → process → output contract.
Avoid unrelated refactoring.
Delete unnecessary code instead of layering workarounds.

---

## One more thing: don't implement all those APIs today

The temptation now will be:

> "We discovered 15 SerpApi APIs, let's build 15 connectors."

**Don't.**

That would turn this into an API wrapper, not DevRadar.

Our immediate technical milestone is:

```text
Product
 ↓
8–15 search hypotheses
 ↓
Google Search
 ↓
YouTube Search
 ↓
normalized Signal objects
 ↓
API returns signals