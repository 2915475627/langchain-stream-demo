# langchain-stream-demo

> 对比了 langchain stream 同步异步实现

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📝 项目简介
stream_demo.py 是同步实现，直接定义在主函数中

astream_demo.py 是异步实现，需要定义一个异步函数，并使用 asyncio.run() 运行该函数


同步输出可以直接输出到控制台。

在前后端项目中一般自定义异步输出，以此实现 SSE 流式传输。


stream_model 参数可传 "messages" ,"updates","values"
"messages" 以 tokens 级别响应，响应快，消息多。
"updates" 每次代理进度后响应，每次执行完一个功能，比如一次模型调用，或者一次工具调用，响应一条消息。



## 🚀 快速开始

### 环境要求
- Python 3.12+
- **包管理器**: [uv](https://github.com/astral-sh/uv)（推荐）或 pip
- MiniMax APIKey

### 安装步骤
1. **克隆项目**

````
git clone https://github.com/2915475627/langchain-stream-demo.git
````

2. **配置环境**

a. 设置 Python 解释器
````
# 使用 uv
uv venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows
````

b. 安装依赖
````
uv pip install -r requirements.txt
````

c. 配置 LLM API Key

复制环境变量模板
````
cp .env.example .env
````
在 .env文件中填入你的 API Key
````
MINIMAX_BASE_URL=https://api.minimaxi.com/anthropic
MINIMAX_API_KEY=sk-xxxxxx
````

3. **运行文件**
````
python stream_demo.py

python astream_demo.py
````