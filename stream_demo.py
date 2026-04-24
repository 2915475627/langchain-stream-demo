from langchain.agents import create_agent
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import AIMessage, HumanMessage

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

# stream_mode="messages" 使得推理过程也能流式响应
for chunk in agent.stream(
    {"messages": [("user", "你好,今天天气怎么样")]},
    stream_mode="messages",
    version="v2"
):
        print(chunk)