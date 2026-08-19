import os
from openai import OpenAI
from ds_func import *

# 初始化客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),   # 从环境变量读取 Key
    base_url="https://api.deepseek.com"
)

# 初始化消息历史，第一条是 system
messages = [
    {"role": "system", "content": "你是用户的聊天/查询助手"},
]

print("=== deepseek-v4-flash started ===")
print("please enter content, enter 'quit' or 'exit' to quit\n")

while True:
    # 获取用户输入
    user_input = input("<user input> ")
    if user_input.lower() in ["exit", "quit"]:
        print("对话结束。")
        break

    # 将用户消息加入历史
    messages.append({"role": "user", "content": user_input})

    try:
        # 调用 API
        response = client.chat.completions.create(
            model="deepseek-reasoner",   # 或 "deepseek-chat"
            messages=messages,
            stream=False,               # 此处设为 False，若想流式输出可改为 True
            max_tokens=8192
        )

        # 获取助手回复
        assistant_reply = response.choices[0].message.content

        # 将助手回复加入历史
        messages.append({"role": "assistant", "content": assistant_reply})

        # 打印回复
        ds_single_output(response)

        # 可选：打印 token 消耗统计
        # print(f"[Token 消耗: {response.usage.total_tokens}]\n")

    except Exception as e:
        print(f"发生错误: {e}")
        # 如果出错，可以选择移除刚才添加的用户消息以避免历史污染
        messages.pop()