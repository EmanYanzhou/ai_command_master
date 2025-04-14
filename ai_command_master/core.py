"""
核心逻辑：处理用户输入、加载配置、调用API、确认、执行等等
"""

from openai import OpenAI


# 配置参数
config_args = {
    'model_provider': '',       # 模型提供商
    'model': '',                # 模型
    'base_url': '',             # 模型url
    'max_tocken': '',           # 最大tocken
    'temperature': '',          # 模型温度
}


# 1.接受 ai <description> 的传递参数
def handle_ask_request(full_description: str):
    client = OpenAI(api_key="", base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "正常聊天"},
            {"role": "user", "content": f"{full_description}"},
        ],
        stream=False
    )
    print('deepseek: ' + response.choices[0].message.content)


# 2.调用 config.py 加载配置

if __name__ == '__main__':
    test()