from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("docs")

USER_AGENT="docs-app/1.0"
SERPER_URL="google.serper.dev"

docs_urls={
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs"
}

def search_web():
    return

def fetch_url():
    return

@mcp.tool()
def get_docs():
    return

def main():
    print("Hello from mcp-server!")


if __name__ == "__main__":
    main()
