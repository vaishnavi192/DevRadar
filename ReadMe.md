# DevRadar - GTM for developer-focused companies.

DevRadar triangulates developer demand across search, GitHub, YouTube, trends, and market signals to recommend what developer-focused companies should do next, identify adoption opportunities, GTM strategies, distribution channels, competitive gaps, and content priorities. 

<img width="1905" height="856" alt="Screenshot 2026-10-10 230809" src="https://github.com/user-attachments/assets/deed03c2-6d1a-4b5a-a50d-75725b8ce951" />

1. Developer ecosystem signals
Connect information from web search, GitHub, YouTube, and google trends sources to understand the landscape around a developer-focused product.

2. GTM opportunities
Surface relevant adoption opportunities, competitive gaps, and potential distribution channels from the collected evidence.

3. Content direction
Identify potential content gaps and video opportunities relevant to developers and the product's target audience.

DevRadar collects developer signals through SerpApi (Google Search, Youtube), GitHub, and enriches them with google trend data, and processes the results through normalization, deduplication, filtering, and TF-IDF-based clustering. The resulting evidence is organized into clusters of developer problems and content gaps, then passed to Google Gemini for cross-source synthesis and GTM recommendations covering product positioning, content strategy, and acquisition.
<img width="1389" height="1132" alt="image" src="https://github.com/user-attachments/assets/9ed92213-e5ce-49ea-8390-ac635cda91a7" />

## Demo of the product

https://github.com/user-attachments/assets/18dac604-5424-482a-97d7-43e7d638bbe2

## Techstack
Frontend - React, Vite, Tailwind CSS<br>
Backend	- Python, FastAPI<br>
Search Layer - SerpApi<br>
Language model - Google Gemini API<br>
Analysis- TF-IDF, evidence clustering, scikit learn
