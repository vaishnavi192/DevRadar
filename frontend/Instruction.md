# DevRadar

## Problem

Developer-focused companies have access to large amounts of information about their market, users, competitors, and ecosystem, but that information is fragmented across search engines, YouTube, communities, competitor websites, documentation, and other sources.

DevRel, developer marketing, and product teams have difficulty turning these signals into clear decisions:

- What are developers actually searching for?
- What problems are developers discussing?
- What are competitors emphasizing?
- Which developer questions are poorly answered?
- Where are developers already gathering?
- What could increase product adoption?
- What should the team build, document, publish, integrate, or promote next?

Existing tools can provide individual pieces of this information, while general-purpose AI can research and summarize it. DevRadar focuses on connecting these signals into actionable developer-focused GTM opportunities.

---

## Target User

Primary users:

- Developer Advocates
- Developer Relations teams
- Developer Marketing teams
- Product Marketing teams at developer-focused companies
- Founders of developer-tool companies
- Open-source companies trying to increase developer adoption

The product is designed for companies that sell or maintain:

- APIs
- SDKs
- developer tools
- infrastructure
- AI developer products
- open-source projects
- technical platforms

The MVP should work for any developer-focused company rather than being specific to SerpApi.

SerpApi will be used as the initial demonstration product.

---

## Core Promise

> **DevRadar turns developer behavior into actionable GTM decisions.**

Instead of simply showing search results, mentions, or trends, DevRadar connects developer signals to concrete actions a team can take.

The central question is:

> **What should our developer team do next?**

Possible actions include:

- Create content
- Improve documentation
- Build an example
- Create an integration
- Engage with a community
- Improve product adoption
- Investigate a product gap
- Explore a partnership

---

## Inputs

The user provides information about the developer-focused product.

Required:

- Product name
- Product website
- Target audience

Optional:

- Documentation URL
- GitHub repository
- Competitors
- Product description
- Primary GTM goal

Example:

Product:
SerpApi

Website:
https://serpapi.com

Audience:
Developers

The application must not contain SerpApi-specific logic.

SerpApi is only the default example/demo product.

---

## External Signals

DevRadar gathers signals from multiple sources.

### Google Search

Used to understand:

- What developers are searching for
- Search intent
- Related searches
- People Also Ask
- Competitor visibility
- Existing content
- Developer implementation questions

### YouTube

Used to understand:

- What developers are learning
- Which technical topics receive attention
- Existing tutorials
- Competitor educational content
- Potential video opportunities

### Google Jobs

Used selectively to understand:

- Technologies companies are hiring for
- Emerging developer skills
- Technology adoption signals

### Google News

Used to understand:

- Industry developments
- Product launches
- Technology trends
- Competitor developments

### Additional sources

The architecture should allow future integrations with sources such as:

- Reddit
- LinkedIn
- GitHub
- Stack Overflow
- Hacker News
- developer communities

These sources are not required for the initial MVP.

---

## Core Intelligence Areas

DevRadar organizes intelligence into seven areas.

### 01 — Developer Demand

**What are developers searching for?**

Identify search queries and clusters representing developer intent.

Examples:

- Implementation questions
- Integration searches
- Comparison searches
- Troubleshooting searches
- Framework-specific searches
- Technology adoption searches

---

### 02 — Developer Conversations

**What are developers discussing?**

Identify recurring developer problems, questions, complaints, and discussions.

The system should distinguish between:

- Search intent
- Developer conversation
- Developer experience

---

### 03 — Competitor Positioning

**What are competitors emphasizing?**

Analyze competitor websites, search results, educational content, and other available signals.

Identify themes such as:

- Features
- Integrations
- Pricing
- Ease of use
- Developer experience
- Framework support
- Use cases
- Positioning

The goal is not merely to list competitors.

The goal is to understand how competitors are presenting themselves to developers.

---

### 04 — Content Gaps

**What developer questions aren't being answered well?**

Identify situations where:

- Developer demand is strong
- Existing content is weak or incomplete
- Documentation does not adequately address the problem
- Competitors have stronger coverage
- Developers repeatedly encounter the same problem

Possible recommendations:

- Blog post
- Technical tutorial
- Documentation page
- Video
- FAQ
- GitHub example

---

### 05 — Distribution Opportunities

**Where are developers already gathering?**

Identify channels and communities associated with relevant developer problems.

Potential channels include:

- YouTube
- Reddit
- GitHub
- LinkedIn
- Hacker News
- Stack Overflow
- Developer communities

The objective is to connect an opportunity with an appropriate distribution channel.

Example:

Developer problem:
"How to use X with n8n"

Possible distribution:

- n8n integration/template
- YouTube tutorial
- GitHub example
- Community discussion

---

### 06 — Adoption Opportunities

**What could make more developers try the product?**

Identify potential adoption friction such as:

- Difficult setup
- Poor documentation
- Missing examples
- Missing integrations
- Unclear positioning
- Missing framework support
- Repeated implementation problems

Recommendations should focus on reducing friction between:

Developer discovers product
→ Developer understands product
→ Developer implements product
→ Developer successfully uses product

---

### 07 — GTM Actions

**What should the company actually do?**

The previous six intelligence areas should converge into concrete recommendations.

Possible actions:

- Create documentation
- Publish a technical article
- Create a video
- Build a GitHub example
- Build an integration
- Respond to community questions
- Improve onboarding
- Improve product documentation
- Investigate a product limitation
- Explore a partnership

Each recommendation should include evidence explaining why it was generated.

---

## Core Workflow

```text
Product Input
     ↓
Product Understanding
     ↓
Search / Signal Generation
     ↓
SerpApi
     ↓
Raw Signals
     ↓
Signal Normalization
     ↓
Signal Clustering
     ↓
Developer Problems
     ↓
Opportunity Analysis
     ↓
┌─────────────────────────────┐
│ Developer Demand            │
│ Developer Conversations     │
│ Competitor Positioning      │
│ Content Gaps                │
│ Distribution Opportunities  │
│ Adoption Opportunities      │
└─────────────────────────────┘
     ↓
GTM Actions
     ↓
Evidence-backed Opportunity

Opportunity

The primary object displayed to the user is a Developer Opportunity.

An opportunity should contain:

Title
Developer problem
Problem type
Evidence
Supporting search queries
Relevant sources
Competitor information
Content gap
Distribution opportunity
Adoption opportunity
Recommended action
Confidence

Example:

Opportunity

SerpApi + n8n

Developer problem

Developers are looking for ways to use Google Search data inside n8n workflows.

Evidence

Related Google searches
People Also Ask questions
YouTube tutorials
Existing competitor content

Opportunity

There appears to be an integration/content opportunity around n8n.

Recommended actions

Create an n8n integration/template
Publish an implementation guide
Create a runnable example
Publish a technical tutorial
Evidence

DevRadar should show the evidence behind its conclusions.

The system should distinguish:

Observation

What the source directly shows.

Inference

What DevRadar concludes from multiple observations.

Recommendation

What the company could do based on the evidence.

The product should avoid presenting AI-generated conclusions as facts.

UI
Do not create giant, duplicated Tailwind class strings. Extract a React component when a UI pattern genuinely repeats. Do not create abstractions merely to shorten class names.

AI Usage

AI is used primarily for:

Understanding product context
Generating search hypotheses
Clustering related signals
Identifying underlying developer problems
Synthesizing evidence
Classifying opportunities
Recommending GTM actions
Generating content/action briefs

AI should not replace deterministic application logic where normal code is sufficient.

SerpApi provides the primary search intelligence.

Application code handles:

Data collection
Normalization
Deduplication
Storage
Clustering infrastructure
Historical data
Application logic

The AI reasoning layer operates on structured evidence rather than raw unfiltered web data.

MVP

The MVP should support:

Enter a developer-focused product
Generate developer-oriented search queries
Collect Google Search signals through SerpApi
Collect YouTube signals through SerpApi
Optionally collect Jobs/News signals
Normalize results
Cluster related signals
Identify developer problems
Generate developer opportunities
Recommend GTM actions
Display supporting evidence
Generate a content/action brief

The MVP should demonstrate the complete flow using SerpApi as the example product while remaining generic enough to analyze another developer-focused company.

MVP Output

The main interface should answer:

What should your developer team do next?

Display a small number of high-quality opportunities rather than a large analytics dashboard.

Each opportunity should show:

Developer problem
Signal strength
Evidence
Competitor context
Recommended action
Action type
Confidence
Out of Scope for MVP

Do not build:

Authentication
Billing
Multi-user teams
Enterprise permissions
Full CRM
Automatic publishing
Automatic outreach
Slack integration
Linear integration
CMS integrations
Full social-media ingestion
Large-scale historical analytics
Autonomous browser agents
Complex multi-agent architecture
Dozens of external APIs
Automated product changes

These may be considered later only if validated.

Future Direction

The long-term product can evolve from:

Developer signals
       ↓
Developer problems
       ↓
Opportunities
       ↓
GTM actions

into:

Developer signals
       ↓
Developer problems
       ↓
GTM intervention
       ↓
Content / Docs / Code / Integration
       ↓
Developer engagement
       ↓
Adoption
       ↓
Outcome

The long-term goal is to learn which GTM interventions actually work for different developer problems.

Success Criteria

The MVP succeeds if a developer-focused company can enter its product information and receive opportunities that are:

Relevant to its developer audience
Supported by observable evidence
More useful than a generic list of content ideas
Connected to concrete GTM actions
Understandable without trusting an opaque AI conclusion

The primary product test is:

Does DevRadar help a developer-focused team decide what to do next?


### One thing I deliberately changed

I made **“Developer Opportunity” the central object** instead of making the seven sections seven separate dashboards.

That's important for keeping the codebase clean:

```text
Signals
   ↓
Problems
   ↓
Opportunities
   ↓
Actions

The seven categories are views/analysis dimensions, not seven independent systems.

