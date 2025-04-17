"""
核心逻辑：处理用户输入、加载配置、调用API、确认、执行等等
"""

from .config import Config
from .api_clients.factory import APIClientFactory
from .system import SystemInfo


# 配置参数
user_message = None
config_args = {}
system_args = {}


# 2.调用 config.py 加载配置
def load_config():
    global config_args
    config = Config()
    config_args = config.load_config()
    # return config_args



# 加载系统信息
def load_system_info():
    global system_args
    system_info = SystemInfo()  # 创建实例
    system_args = system_info.get_system_info()  # 通过实例调用方法


# 调用合适的接口
def call_api(messages: list) -> str:
    provider = config_args['model_provider'].lower()
    client = APIClientFactory.get_api_client(provider, config_args)
    response = client.chat_completion(messages)
    client.close()  # 清理资源
    return response


# 核心处理逻辑
def start_request(full_description: str) -> list:
    # 1. 获取用户信息
    global user_message
    user_message = full_description
    
    # 2. 加载配置
    load_config()

    # 3. 加载系统信息
    load_system_info()
    
    # 3. 准备消息
    messages = [
        {"role": "system", "content": f"{config_args['prompt']['system']['content']}，计算机系统参数：{system_args}"},
        {"role": "user", "content": f"用户提问：{user_message}"}
    ]
    
    # 4. 调用API获取结果
    response = call_api(messages)
    
    # 5. 处理响应
    return [response, config_args['model']]




if __name__ == '__main__':
    load_config()
    print('配置加载完成')
    print(config_args)