# MCP SERVER

## Make queries about any issue using the latest documentation available

With this MCP, you can debug your application by querying any issue using the latest documentation available on the web. We currently support LangChain, LlamaIndex, and OpenAI docs, but you can add any other sources as needed.

## TECH

- Python3.12.9
- beautifulsoup4
- mcp[cli]

## Installation

```
git clone https://github.com/JeanVittory/mcp-server.git
cd mcp-server
python3.12 -m venv ~/venv/mcp-server
source ~/venv/mcp-server/bin/activate
uv pip install -e .
```
## Env variables

Yuu just need a Serper Api Key generated [here](https://serper.dev/)

## Add more documentation sources

Please look for a variable called docs_urls in the constants folder. Add the URLs of the documentation you want to reference to that dictionary.

## MCP Installation
```
{
    "mcpServers": {
        "mcp-server": {
            "command": "uv", # if fail run which uv and paste the absolute route here
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/YOUR/mcp-server-code",
                "run",
                "src/main.py"
            ]
        }
    }
}
```

## Troubleshooting

If you have any issue please contact me vittory.dev@gmail.com or generate an issue!