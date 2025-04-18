import os
import yaml
from typing import Dict, Any

class ConfigManager:

    """配置管理类，用于处理应用程序的配置文件。

    该类负责管理默认配置和用户配置文件，支持配置的加载和保存操作。
    配置文件使用YAML格式，存储在'./ai_command_master/config/'目录下：
    - default.yaml: 默认配置文件，包含基础配置项
    - config.yaml: 用户配置文件，用于覆盖默认配置
    """

    _instance: 'Config | None' = None    # 私有化_instance用来储存唯一实例

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """初始化配置管理器，设置配置文件路径"""
        # hasattr(self, 'config_dir') 检查 self 对象是否已经具有 config_dir 属性
        if not hasattr(self, 'config_dir'):
            self.config_dir: str = os.path.join(os.path.dirname(__file__), 'config')     # 配置文件目录
            self.default_config: str = os.path.join(self.config_dir, 'default.yaml')     # 默认配置文件路径
            self.user_config: str = os.path.join(self.config_dir, 'config.yaml')         # 用户配置文件路径
            self.config_data: dict = {}                                                  # 存储合并后的配置数据

    def load_config(self) -> Dict[str, Any]:

        """加载并合并配置文件。

        首先加载默认配置文件，然后如果存在用户配置文件，
        则使用用户配置覆盖默认配置中的相应项。

        Returns:
            self.config_data
            Dict[str, Any]: 合并后的配置数据字典
        """

        try:
            # 检查用户配置文件是否存在,存在就加载用户配置,不存在就加载默认配置
            if os.path.exists(self.user_config):
                # 加载用户配置
                with open(self.user_config, 'r', encoding='utf-8') as f:
                    self.config_data = yaml.safe_load(f)
            else:
                # 加载默认配置
                with open(self.default_config, 'r', encoding='utf-8') as f:
                    self.config_data = yaml.safe_load(f)
            return self.config_data
        except FileNotFoundError as e:
            # 配置文件都未找到
            print(f"错误: 配置文件 {self.user_config} 或 {self.default_config} 不存在，请检查路径。")
            return {}    # 返回空字典


    # 保存配置文件 - TODO：计划实现保存配置功能
    # def save_config(self, config: Dict[str, Any]) -> None:
    #     """保存配置到用户配置文件。
    #
    #     Args:
    #         config (Dict[str, Any]): 要保存的配置数据字典
    #     """
    #     # 保存配置到用户配置文件
    #     with open(self.user_config, 'w', encoding='utf-8') as f:
    #         yaml.dump(config, f, allow_unicode=True)