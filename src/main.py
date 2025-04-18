from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from utils.helpers import fetch_url, search_web
from constants import  SERPER_URL, docs_urls

load_dotenv()

mcp = FastMCP("docs")

@mcp.tool()
async def get_docs(query:str, library:str):
    """
    Search the documentation for a given query and library,
    Supports Langchain, Openai, llama-index.
    
    Args:
        query: The query to search (e.g: Chroma DB)
        library: The library search in (e.g: Langchain)
    
    Returns:
        The information from the documentation.
    """
    
    if library not in docs_urls:
        raise ValueError(f"The library {library} is not supported.")

    query = f"site:{docs_urls[library]} {query}"
    search_web_results = await search_web(query=query, url=SERPER_URL)
    
    if "error" in search_web_results:
        raise ValueError(f"Something went wrong: {search_web_results["error"]}")
    
    text = ""
    for result in search_web_results["organic"]:
        text += await fetch_url(result["link"])
    return text 

def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
