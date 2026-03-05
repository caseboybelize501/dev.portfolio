# Dev.Portfolio

**Autonomous Developer Portfolio & Reputation Engine**

A system that monitors a developer's GitHub activity, synthesizes their technical identity from commit patterns, open-source contributions, and project quality signals — generates a living portfolio site, a recruiter-facing technical brief, and a self-updating skills graph that learns which contribution patterns correlate with job offers, consulting leads, and open-source reputation growth.

## The Space That Doesn't Exist

A developer's GitHub profile is the most honest resume that exists — and almost nobody presents it well. The actual signal is buried: commit frequency patterns that show sustained deep work, PR quality that shows collaborative judgment, issue responses that show domain authority, the specific combination of technologies that reveals genuine expertise versus tutorial completion.

Recruiters and clients look at pinned repos and star counts, missing 90% of the actual signal.

## System Architecture


STARTUP BOOTSTRAP (HARD PARAMS — ABSOLUTE FIRST):
┌─────┬──────────────────────────────────────────────────────────────────────┐
│ PHASE 1 — LOCAL ASSET INVENTORY                                     │
│ → Walk C:\ D:\ → sha256 all model files                            │
│ → Probe inference servers                                           │
│ → which node / python3 / git → version + path                      │
│ → npm list next astro / which hugo → version + path                │
│ → netstat → active LISTEN ports                                     │
│ → Write SystemProfile.json. Block until validated.                 │
│                                                                     │
│ PHASE 2 — GITHUB ACTIVITY DEEP PULL                                │
│ → REST: /users/caseboybelize501/repos + events + starred           │
│ → GraphQL: contributionsCollection (52-week contribution graph)    │
│ → Cache raw data locally (dedup by event_id + date)               │
│                                                                     │
│ PHASE 3 — PERMISSION GATE A                                         │
│ → Show: activity summary (repos, commits, PRs, contribution streak) │
│ → Show: site generator to be used from SystemProfile               │
│ → APPROVE → TechIdentityAgent | SKIP → mark known                 │
│                                                                     │
│ PHASE 4 — INCREMENTAL UPDATE                                        │
│ → On subsequent runs: only process new events since last sync      │
│ → Portfolio rebuilds only when identity delta > threshold          │
└─────┴──────────────────────────────────────────────────────────────────────┘

10-STAGE VALIDATION CYCLE:
┌─────┬──────────────────────────────────────────────────────────────────────┐
│ Stage 01 — Activity Sync    : all repos + events fetched           │
│ Stage 02 — Tech Identity    : identity profile extracted           │
│ Stage 03 — Skills Graph     : dynamic skills graph builds clean    │
│ Stage 04 — Project Select   : top projects auto-selected           │
│ Stage 05 — Portfolio Build  : static site builds without error     │
│ Stage 06 — Recruiter Brief  : 1-page brief generates correctly    │
│ Stage 07 — Deploy           : live on GitHub Pages                 │
│ Stage 08 — Analytics        : Plausible tracking fires             │
│ Stage 09 — Auto-Update      : new commit → portfolio updates       │
│                              in <5 min (webhook → rebuild)        │
│ Stage 10 — Regression       : prior deployed portfolios stable     │
│                                                                     │
│ REPUTATION MUTATION TESTING:                                       │
│ → Add high-quality repo → skills graph must update                │
│ → Simulate inbound follow spike → reputation tracker records      │
│ → Change top language → portfolio hero section must update        │
│                                                                     │
│ STABLE GATE: 7 consecutive passing cycles across all 10 stages     │
└─────┴──────────────────────────────────────────────────────────────────────┘

## Stack

- Orchestrator      → Python (FastAPI + asyncio)
- GitHub data       → httpx (REST + GraphQL, rate-limit aware)
- Tech identity     → LLM via SystemProfile.inference_config
- Skills graph      → NetworkX (dynamic graph) → D3.js (render)
- Portfolio site    → Next.js/Astro/Hugo (best available from SystemProfile)
- Analytics         → Plausible Community (self-hosted, no paid plan)
- Recruiter brief   → LLM (structured PDF via weasyprint)
- Auto-update       → GitHub webhook → rebuild trigger
- RAG memory        → ChromaDB (identity patterns + opportunity signals)
- Reputation graph  → Neo4j (contribution_pattern → opportunity_type)
- Meta-learner      → sklearn (portfolio_style → opportunity_signal_rate)
- Payment           → Stripe (free: GitHub Pages | paid: custom domain+analytics)
- Free hosting      → GitHub Pages (always default, no fallback needed)
- Paid hosting      → Vercel (custom domain on Stripe upgrade)
- Queue             → Celery + Redis
- Interface         → React (identity dashboard + skills graph + brief preview)

## Features

1. **System Scan & Bootstrap**
   - Local asset inventory
   - Model deduplication
   - Tool detection
   - Static site generator detection

2. **GitHub Activity Monitoring**
   - Full activity graph pull
   - Commit patterns analysis
   - PR quality assessment
   - Contribution streak tracking

3. **Technical Identity Synthesis**
   - Language expertise mapping
   - Domain specialization identification
   - Collaboration style analysis
   - Depth vs breadth index calculation

4. **Skills Graph Generation**
   - Dynamic skills network
   - Weighted by recency and impact
   - Real-time updates from code usage

5. **Portfolio Generation**
   - Static site generation
   - Auto-selected top projects
   - Self-updating content
   - GitHub Pages deployment

6. **Recruiter Brief Creation**
   - 1-page technical summary
   - Achievement highlighting
   - Availability signals
   - Contact information

7. **Reputation Tracking**
   - Portfolio view analytics
   - Inbound opportunity tracking
   - Star velocity monitoring
   - Follow spike detection

8. **Learning Engine**
   - Pattern correlation learning
   - Opportunity signal prediction
   - Portfolio style optimization
   - Meta-learning for developers

## Installation

bash
# Clone the repository
git clone https://github.com/caseboybelize501/dev.portfolio.git

cd dev.portfolio

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py


## Usage

### API Endpoints

- `GET /health` - Health check
- `POST /api/portfolio/sync` - Sync portfolio for a user
- `GET /api/system/profile` - Get system profile
- `GET /api/portfolio/{username}/identity` - Get tech identity
- `GET /api/portfolio/{username}/skills` - Get skills graph
- `GET /api/portfolio/{username}/brief` - Get recruiter brief
- `GET /api/reputation/{username}/signals` - Get reputation signals
- `GET /api/memory/patterns` - Get identity patterns
- `GET /api/memory/reputation` - Get reputation correlations
- `POST /api/payments/subscribe` - Subscribe to payment tier

### Docker Usage

bash
docker-compose up


## License

MIT