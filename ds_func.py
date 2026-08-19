from openai.types.chat import ChatCompletion
from typing import Union

def ds_single_output(response:ChatCompletion) -> None: 
    print(f"model = {response.model}, request_id = {response.id}, token_usage = {response.usage.total_tokens}.") #使用模型、请求序号、token用量
    print(f"end_reason = {response.choices[0].finish_reason}")  #结束原因
    print("===answer===") #分隔符
    print(f"<{response.choices[0].message.role} output>\n{response.choices[0].message.content}") #打印回答内容

def text_reader(file_path:str) -> str:
    try:
        with open(file_path, "r", encoding= "UTF-8") as f:
            return f.read()
    except FileNotFoundError:
        print("文件路径无效")
        return "文件无效"

def multi_text_reader(*args) -> str:
    count = 0
    output = ""
    for file_path in args:
        update = f"文本文件{count}: "+ text_reader(file_path) + "\n"
        output += update
        count += 1
    return output