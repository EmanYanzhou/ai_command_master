"""核心逻辑
    处理用户输入、加载配置、调用API、确认、执行等等操作
"""

from .config import ConfigManager
from .system import SystemInfo
from .api_clients.factory import APIClientFactory


# 相关参数
config_instance: ConfigManager = ConfigManager()    # 单例模式: 配置文件管理对象


# 2.调用 config.py 加载配置
def load_config() -> dict:
    config = config_instance.load_config()
    return config


# 加载系统信息
def load_system_info() -> dict:
    system_info = SystemInfo()    # 创建SystemInfo实例
    return system_info.get_system_info()    # 返回字典


# 准备消息
def prepare_message(user_message: str, config_args: dict, system_args: dict) -> list:
    messages: list = []

    # 提示词
    prompt: str = config_args['prompt']['base']

    system_content: str = f"""
    {prompt}
    --------------提示词分割线---------------
    系统信息:
    系统:{system_args['系统']};
    系统版本:{system_args['系统版本']};
    用户名:{system_args['用户名']};
    用户家目录:{system_args['用户家目录']};
    当前工作目录:{system_args['当前工作目录']};
    """
    user_content: str = f"{user_message}"

    messages.append({
        "role": "system",
        "content": f"{system_content}"
    })
    messages.append({
        "role": "user",
        "content": f"{user_content}"
    })

    return messages


# 调用合适的接口
def call_api(config_args: dict, messages: list) -> str:
    provider = config_args['model_provider']
    client = APIClientFactory.get_api_client(provider, config_args)
    response = client.chat_completion(messages)
    client.close()
    return response


# 核心处理逻辑
def start_request(full_description: str) -> list:

    # 1. 获取用户输入
    user_message: str = full_description    # 用户输入
    
    # 2. 加载配置
    config_args: dict = load_config()    # 配置参数

    # 3. 加载系统信息
    system_args: dict = load_system_info()    # 系统信息
    
    # 3. 准备消息
    messages: list = prepare_message(user_message, config_args, system_args)
    
    # 4. 调用API获取结果
    response = call_api(config_args, messages)
    
    # 5. 处理响应
    return [response, config_args['model']]




if __name__ == '__main__':
    pass