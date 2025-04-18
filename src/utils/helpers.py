import json
import os
import httpx
from bs4 import BeautifulSoup

async def search_web(query:str, url:str) -> dict | None:
    payload = json.dumps({"q": query, "num": 2})
    headers= {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "Application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                url, 
                data=payload, 
                headers=headers, 
                timeout=30.0
            )
            response.raise_for_status()
            return response.json
        except httpx.TimeoutException():
            return {"error": "Timeout error searching web"}
        except httpx.HTTPStatusError as e:
            return {"error": f"Error: {e.response.status_code}"} 
            
    

async def fetch_url(url:str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url, timeout=30.0)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text 
    except httpx.TimeoutException():
        return {"error": "Timeout Error fetching url"}