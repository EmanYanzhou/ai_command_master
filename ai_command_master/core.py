"""核心逻辑
    处理用户输入、加载配置、调用API、确认、执行等等操作
"""
from .execution import Execution
from .system import SystemInfo
from .config import ConfigManager
from .data_formatter import DataFormatter
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


# 格式化返回结果
def format_response(response: str) -> dict:
    # 创建 DataFormatter 类的对象
    response_formatter = DataFormatter(response)
    response_dict = response_formatter.parse()

    return response_dict


# 安全执行
def saft_execution(model: str, response_dict: dict):
    # 创建 Execution 类对象
    # exe =
    # print("开始执行")
    # print(model)
    # print(response_dict)
    exe = Execution(model, response_dict)
    exe.execute()


# 核心处理逻辑
def start_request(full_description: str):

    # 1. 获取用户输入
    user_message: str = full_description    # 用户输入
    # print(f"User message: {user_message}")
    
    # 2. 加载配置
    config_args: dict = load_config()    # 配置参数
    # print(f"Config args: {config_args}")
    
    # 3. 加载系统信息
    system_args: dict = load_system_info()    # 系统信息
    # print(f"System args: {system_args}")
    
    # 3. 准备消息
    messages: list = prepare_message(user_message, config_args, system_args)
    # print(f"Prepared messages: {messages}")
    
    # 4. 调用API获取结果
    response: str = call_api(config_args, messages)
    # print(f"API response: {response}")

    # 5. 格式化返回结果
    response_dict: dict = format_response(response)
    # print(f"Formatted response: {response_dict}")

    # 6. 安全执行
    saft_execution(config_args['model'], response_dict)


if __name__ == '__main__':
    start_request("怎么查看网络配置")