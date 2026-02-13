# 🕸️ RAG Tutorial 12 — Graph RAG

<p align="center">
  <a href="https://github.com/kishore2797/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-12_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/kishore2797/mastering-rag) tutorial series**  
> Previous: [11 — Multi-Modal RAG](https://github.com/kishore2797/rag-11-multi-modal-rag) | Next: [13 — RAG Evaluation](https://github.com/kishore2797/rag-13-evaluation-framework)

---

## 🌍 Real-World Scenario

> A journalist investigating corporate ownership asks: "Which companies does Elon Musk control, and which of those companies have contracts with NASA?" Vector search finds documents mentioning Musk and NASA separately, but can't connect the dots. **Graph RAG** builds a knowledge graph: `Elon Musk → CEO_of → SpaceX`, `Elon Musk → CEO_of → Tesla`, `SpaceX → has_contract_with → NASA`. It traverses these relationships to answer: "SpaceX (CEO: Elon Musk) has active contracts with NASA for Crew Dragon and Starship." Multi-hop reasoning that no vector search can do.

---

## 🏗️ What You'll Build

A RAG system that **extracts entities and relationships** from documents to build a knowledge graph, then **traverses the graph** to answer complex, multi-hop queries that vector search alone can't handle.

```
Document ──→ LLM extracts entities + relations ──→ Knowledge Graph
                                                        ↓
"Who does Alice report to, and what                Traverse: Alice → reports_to → Bob
 projects is that person leading?"                          Bob → leads → [Project X, Y]
                                                        ↓
                                              Subgraph context ──→ LLM ──→ Answer
```

## 🔑 Key Concepts

- **Entity extraction**: LLM identifies people, organizations, concepts from text
- **Relation linking**: LLM identifies relationships between entities
- **Knowledge graph**: nodes (entities) + edges (relations) stored as a graph
- **Graph traversal**: follow edges to gather multi-hop context
- **Subgraph as context**: send the relevant portion of the graph to the LLM

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · NetworkX · OpenAI · Sentence-Transformers |
| Frontend | React 19 · Vite · Tailwind CSS · D3.js (graph visualization) |

## 🚀 Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8006
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — ingest text, view the knowledge graph, run graph-powered queries.

## 📦 Example

A minimal runnable example is in the `example/` folder:

```bash
cd example
python example.py
```

It builds a tiny knowledge graph and traverses it to gather context for a multi-hop query.

## 📖 What You'll Learn

1. How to extract entities and relations from unstructured text
2. Building and storing a knowledge graph
3. Graph traversal strategies for multi-hop questions
4. When Graph RAG outperforms vector-only RAG
5. Combining graph context with vector context for richer answers

## 📋 Prerequisites

- Python 3.11+ and Node.js 18+
- Concepts from [Tutorial 05](https://github.com/kishore2797/rag-05-basic-rag-pipeline) (basic RAG pipeline)
- OpenAI API key (for entity extraction)

## ✏️ Exercises

1. **Your own data**: Ingest a Wikipedia article about a complex topic (e.g., "European Union"). Inspect the extracted graph — are the entities and relations correct?
2. **Multi-hop query depth**: Try queries requiring 1-hop, 2-hop, and 3-hop traversal. At what depth does accuracy start to degrade?
3. **Entity disambiguation**: Ingest text where "Apple" refers to both the company and the fruit. Does the graph distinguish them?
4. **Graph + Vector hybrid**: For the same queries, compare graph-only, vector-only, and combined retrieval. When does each approach win?
5. **Graph visualization**: Use the D3.js visualization to explore the graph interactively. Can you spot extraction errors (wrong relations) by visual inspection?

## ⚠️ Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Too many entities extracted | LLM extracts every noun as an entity | Add entity type constraints: only extract PERSON, ORG, CONCEPT, LOCATION |
| Duplicate entities ("Elon Musk" vs "Musk" vs "Mr. Musk") | No entity resolution/normalization | Add an entity resolution step to merge aliases |
| Relations are too generic ("related_to" for everything) | LLM defaults to vague relationships | Provide example relation types in the extraction prompt |
| Graph traversal is slow on large graphs | Traversing all paths from an entity | Limit traversal depth to 2–3 hops; use indexed lookups for starting nodes |

## 📚 Further Reading

- [Graph Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2408.08921) — Comprehensive survey (2024)
- [Microsoft GraphRAG](https://github.com/microsoft/graphrag) — Microsoft's production Graph RAG implementation
- [NetworkX Documentation](https://networkx.org/documentation/stable/) — Python graph library used in this tutorial
- [Knowledge Graphs: Opportunities and Challenges](https://arxiv.org/abs/2211.05994) — Foundation paper on knowledge graph construction

## ➡️ Next Steps

You've built advanced retrieval systems. Now learn to **measure** them — head to **[Tutorial 13 — RAG Evaluation Framework](https://github.com/kishore2797/rag-13-evaluation-framework)**.

---

<p align="center">
  <sub>Part of <a href="https://github.com/kishore2797/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>
