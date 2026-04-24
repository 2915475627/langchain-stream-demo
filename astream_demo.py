from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import os
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model="MiniMax-M2.7",
    api_key=os.getenv("MINIMAX_API_KEY"),
    base_url=os.getenv("MINIMAX_BASE_URL"),
    model_provider="anthropic",
    temperature=0.5,
    max_tokens=1000
)

agent = create_agent(model=model)

print("=" * 60)
print("开始流式响应...")
print("=" * 60)

async def run():
    async for event in agent.astream_events(
        {"messages": [("human", "今天天气怎么样")]},
        version="v2"
    ):
        if event["event"] == "on_chat_model_stream":
            chunk = event["data"]["chunk"]
            for item in chunk.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    print(item.get("text", ""), end="", flush=True)
                elif isinstance(item, str):
                    print(item, end="", flush=True)

import asyncio
asyncio.run(run())
