#!/usr/bin/env python3
"""
RAG Tutorial 12 — Graph RAG
Minimal example: build a tiny knowledge graph (entities + relations), traverse for context.
Run: pip install -r requirements.txt && python example.py
"""
from collections import defaultdict

# In production: extract entities/relations with an LLM. Here we hand-define a small graph.
ENTITIES = {"Alice", "Bob", "Project_X", "Project_Y"}
RELATIONS = [
    ("Alice", "reports_to", "Bob"),
    ("Bob", "leads", "Project_X"),
    ("Bob", "leads", "Project_Y"),
]


def build_graph():
    """Build adjacency: entity -> [(relation, target), ...]"""
    graph = defaultdict(list)
    for s, r, t in RELATIONS:
        graph[s].append((r, t))
    return graph


def get_subgraph(graph, start: str, depth: int = 2) -> list[str]:
    """BFS from start; return edges as readable facts for LLM context."""
    facts = []
    visited = {start}
    frontier = [start]
    for _ in range(depth):
        next_frontier = []
        for node in frontier:
            for rel, target in graph[node]:
                facts.append(f"{node} --[{rel}]--> {target}")
                if target not in visited:
                    visited.add(target)
                    next_frontier.append(target)
        frontier = next_frontier
    return facts


def main():
    graph = build_graph()
    # Query: "Who does Alice report to, and what projects do they lead?"
    context = get_subgraph(graph, "Alice")
    print("Query: Who does Alice report to, and what projects do they lead?")
    print("Subgraph context (for LLM):")
    for f in context:
        print(" ", f)
    print("\n→ LLM would answer: Alice reports to Bob, who leads Project_X and Project_Y.")


if __name__ == "__main__":
    main()
