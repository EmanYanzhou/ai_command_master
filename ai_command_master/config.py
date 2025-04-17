import os
import yaml
from typing import Dict, Any

class Config:
    """配置管理类，用于处理应用程序的配置文件。

    该类负责管理默认配置和用户配置文件，支持配置的加载和保存操作。
    配置文件使用YAML格式，存储在'config'目录下：
    - default.yaml: 默认配置文件，包含基础配置项
    - config.yaml: 用户配置文件，用于覆盖默认配置
    """

    def __init__(self):
        """初始化配置管理器，设置配置文件路径。"""
        self.config_dir = os.path.join(os.path.dirname(__file__), 'config')  # 配置文件目录
        self.default_config = os.path.join(self.config_dir, 'default.yaml')  # 默认配置文件路径
        self.user_config = os.path.join(self.config_dir, 'config.yaml')      # 用户配置文件路径
        self.config_data = {}  # 存储合并后的配置数据

    def load_config(self) -> Dict[str, Any]:
        """加载并合并配置文件。

        首先加载默认配置文件，然后如果存在用户配置文件，
        则使用用户配置覆盖默认配置中的相应项。

        Returns:
            Dict[str, Any]: 合并后的配置数据字典
        """
        # 加载默认配置
        with open(self.default_config, 'r', encoding='utf-8') as f:
            self.config_data = yaml.safe_load(f)

        # 如果存在用户配置，则覆盖默认配置
        if os.path.exists(self.user_config):
            with open(self.user_config, 'r', encoding='utf-8') as f:
                user_config = yaml.safe_load(f)
                if user_config:
                    self.config_data.update(user_config)

        return self.config_data

    def save_config(self, config: Dict[str, Any]) -> None:
        """保存配置到用户配置文件。

        Args:
            config (Dict[str, Any]): 要保存的配置数据字典
        """
        # 保存配置到用户配置文件
        with open(self.user_config, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True)