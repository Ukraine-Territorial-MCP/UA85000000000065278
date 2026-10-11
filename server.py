import json
from pathlib import Path
from mcp.server.mcpserver import MCPServer

DATA = json.loads(
    (Path(__file__).parent / "data.json").read_text(encoding="utf-8")
)

server = MCPServer(name=DATA["code"].lower())

@server.tool()
def get_identity() -> dict:
    """Офіційна назва, код і тип території."""
    return DATA

@server.tool()
def get_basic_profile() -> dict:
    """Адміністративний профіль території."""
    return {
        "name": DATA["name"],
        "code": DATA["code"],
        "category": DATA["category"],
        "level": DATA["level"],
        "region_code": DATA["region_code"],
        "district_code": DATA["district_code"],
        "community_code": DATA["community_code"],
        "settlement_code": DATA["settlement_code"],
    }

@server.tool()
def get_sources() -> dict:
    """Джерело адміністративних даних."""
    return {
        "source": "КАТОТТГ",
        "code": DATA["code"],
    }


if __name__ == "__main__":
    server.run(transport="stdio")
