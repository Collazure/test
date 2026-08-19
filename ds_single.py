import os
from openai import OpenAI
from ds_func import *

# 初始化客户端
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),  # 从环境变量读取 Key
    base_url="https://api.deepseek.com"          # DeepSeek API 地址
)

text_content = multi_text_reader(r"E:\texts\Arknights\0_肉鸽\黑流树海-黑流数据库.txt", r"E:\texts\Arknights\0_肉鸽\黑流树海-实践随行录.txt")

# 发送请求
response = client.chat.completions.create(
    model="deepseek-reasoner",  # 指定使用 R1 模型
    messages=[
        {"role": "system", "content": "你是一个阅读助手, 需要客观, 理性地分析用户提供的文本。"},
        {"role": "user", "content": f"请分析以下文本的剧情脉络:\n{text_content}"}
    ],
    stream=False  # 是否启用流式输出
)

# 打印结果
ds_single_output(response)