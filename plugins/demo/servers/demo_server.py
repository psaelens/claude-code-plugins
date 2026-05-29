#!/usr/bin/env python3
"""Demo MCP server — fetches real Wikipedia intros and suggests tech terms."""
import json
import random
import urllib.parse
import urllib.request
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")

TECH_TERMS = [
    "microservices",
    "continuous integration",
    "technical debt",
    "containerization",
    "application programming interface",
    "DevOps",
    "Agile software development",
    "load balancing",
    "cache (computing)",
    "refactoring",
    "cloud computing",
    "encryption",
]


@mcp.tool()
def get_random_tech_term() -> str:
    """Return a random tech term to explain in plain language."""
    return random.choice(TECH_TERMS)


@mcp.tool()
def fetch_wikipedia_intro(term: str) -> str:
    """Fetch the Wikipedia summary paragraph for a tech term.

    Args:
        term: The tech concept to look up (e.g. "microservices", "DevOps").
    """
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(term)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "demo-plugin/0.1"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read())
            extract = data.get("extract", "")
            title = data.get("title", term)
            return f"{title}: {extract}" if extract else f"No Wikipedia summary found for '{term}'."
    except Exception as e:
        return f"Could not fetch Wikipedia definition for '{term}': {e}"


if __name__ == "__main__":
    mcp.run()
