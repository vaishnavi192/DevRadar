# DevRadar

## Product Promise

DevRadar turns developer behavior into actionable GTM decisions.

It helps developer-focused companies answer:

> What are developers trying to do, what are they struggling with, and what should our team do next?

---

## Problem

Developer-focused companies have fragmented signals about what their audience needs.

Useful information exists across:

- Search results
- Search suggestions
- YouTube
- Forums
- Trends
- News
- Job listings
- Competitor content
- Product documentation
- GitHub and other developer ecosystems

The problem is not a lack of information.

The problem is turning fragmented signals into:

1. Developer problems
2. Opportunities
3. Concrete GTM actions

---

## Target Users

Primary users:

- DevRel teams
- Developer marketing teams
- Product marketing teams
- Developer-tool founders
- API/SDK/infra companies
- Open-source companies

---

# Product Inputs

```text
Product name: required
Product website: required
Documentation URL: optional
GitHub repository: optional
Target audience: required
Competitors: optional
Primary goal: optional

Example:

Product:
SerpApi

Website:
https://serpapi.com

Target audience:
Developers

Documentation:
https://serpapi.com/docs

SerpApi is a demonstration product, not a hardcoded dependency.

DevRadar must work with other developer-focused products.

Signal Model

DevRadar does not treat external APIs as separate dashboards.

Instead, external sources provide different types of developer signals.

External Sources
       ↓
Raw Evidence
       ↓
Normalized Signals
       ↓
Signal Clusters
       ↓
Developer Problems
       ↓
Opportunities
       ↓
GTM Actions

A signal is an observation derived from an external source.

Signal Categories
1. Developer Demand

Question:

What are developers trying to find or accomplish?

Primary sources:

Google Search
Google Autocomplete
Google Trends

Examples:

[product] python
[product] nextjs
[product] integration
[product] alternative
[product] error
2. Developer Education

Question:

What are developers trying to learn?

Primary sources:

YouTube Search
YouTube Videos
YouTube Transcripts

Examples:

[product] tutorial
[product] example
[product] how to
[product] integration tutorial
3. Developer Conversations

Question:

What problems are developers discussing?

Potential sources:

Google Forums
Search results
Future community sources

This can surface:

Questions
Troubleshooting
Implementation problems
Product complaints
Workarounds
4. Market Trends

Question:

What is changing around the developer ecosystem?

Sources:

Google Trends
Google News
Google Jobs

Examples:

Rising technology interest
Framework changes
Competitor announcements
New product launches
Hiring trends
5. Competitor Positioning

Question:

What alternatives are developers considering and what do competitors emphasize?

Sources:

Google Search
YouTube
News
Competitor websites
Competitor documentation

Example queries:

[product] alternative
[product] vs
[product] comparison
[product] pricing
[competitor] vs [product]
6. Content Gaps

Question:

Where does developer demand exist but useful coverage appear weak?

Signals can come from:

Search results
YouTube results
Related searches
Forums
Documentation

Example:

Developer demand exists
        +
Existing content is weak/outdated
        ↓
Potential content opportunity
7. Distribution Opportunities

Question:

Where are developers already looking for answers?

Potential sources:

Search
YouTube
Forums
Developer communities
Social profiles

The goal is not simply to identify platforms.

The goal is to identify where a specific developer problem is already being discussed.

8. Adoption Opportunities

Question:

What could make developers more likely to try or adopt the product?

Potential evidence:

Integration searches
Alternative searches
Troubleshooting searches
Documentation gaps
Job/technology signals
Competitor positioning
SerpApi Sources

DevRadar should initially focus on sources that directly contribute to developer intelligence.

Core Sources
Google Search

Provides:

Organic results
Related searches
People Also Ask
Search-result metadata
Relevant web pages

Primary use:

Developer demand
Competitor research
Content gaps
Implementation problems
YouTube Search

Provides:

Developer videos
Channels
Video metadata
Search results

Primary use:

Developer education demand
Tutorial research
Content gaps
Secondary Sources

These should be added after the core Google + YouTube workflow works.

Google Autocomplete

Use for discovering how developers phrase searches and generating additional search hypotheses.

Google Trends

Use for trend direction and related queries/topics.

Google News

Use for product, competitor, technology, and ecosystem developments.

Google Forums

Use for developer conversations and troubleshooting signals.

Google Jobs

Use selectively to identify technologies and skills appearing in relevant hiring demand.

YouTube Transcript

Use to analyze what existing tutorials actually teach and identify coverage gaps.

YouTube Channel

Use for creator/channel-level analysis.

Yandex

Use selectively for regional or non-Google search behavior.

Low-Priority Sources

These are not part of the MVP:

Facebook Profile
Instagram Profile
Image search
Shopping
Maps
Travel
Hotels
Flights

They may be useful for specific future use cases but are not central to developer intelligence.

Evidence Philosophy

DevRadar distinguishes:

Observation

What the source directly shows.

Example:

Search results contain several queries related to
using the product with n8n.
Inference

What DevRadar concludes from multiple observations.

Example:

There may be meaningful developer interest in an n8n integration.
Recommendation

What DevRadar suggests the company should do.

Example:

Create an n8n integration guide and example workflow.

Never present an inference as a directly observed fact.

Core Workflow
Product Input
      ↓
Product Understanding
      ↓
Search Hypotheses
      ↓
Signal Collection
      ↓
Evidence Normalization
      ↓
Signal Clustering
      ↓
Developer Problems
      ↓
Opportunity Analysis
      ↓
GTM Actions
      ↓
Evidence-backed Opportunities
Opportunity Example

Product:

SerpApi

Signal:

Search and YouTube results indicate interest in
using search APIs with n8n.

Developer problem:

Developers want to use search data inside n8n
workflows without building the integration themselves.

Opportunity:

Create an n8n integration/template and supporting
technical documentation.

Recommended actions:

- Integration
- Documentation
- Tutorial
- Example workflow
Opportunity Object
{
  "title": "...",
  "developer_problem": "...",
  "intent": "integration",
  "signals": [],
  "evidence": [],
  "serp_gap": "...",
  "content_gap": "...",
  "docs_gap": "...",
  "integration_opportunity": "...",
  "recommended_actions": [],
  "confidence": "medium"
}
MVP

The MVP should:

Accept a developer-focused product.
Understand basic product context.
Generate search hypotheses.
Collect Google Search evidence using SerpApi.
Collect YouTube evidence using SerpApi.
Normalize results into DevRadar signals.
Group related signals.
Identify developer problems.
Generate opportunities.
Recommend GTM actions.
Show evidence behind recommendations.
Return structured results through the API.
Post-MVP Roadmap
Phase 2

Add:

Google Autocomplete
Google Trends
Google News
Google Forums
Phase 3

Add selectively:

YouTube Transcripts
YouTube Channels
Google Jobs
Yandex
Phase 4

Add:

Historical signal tracking
Recurring analysis
Opportunity changes over time
Action tracking
Outcome measurement

The long-term product should connect:

Signal
 ↓
Opportunity
 ↓
Action
 ↓
Outcome