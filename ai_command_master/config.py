import os
import yaml
from typing import Dict, Any

class Config:
    def __init__(self):
        self.config_dir = os.path.join(os.path.dirname(__file__), 'config')
        self.default_config = os.path.join(self.config_dir, 'default.yaml')
        self.user_config = os.path.join(self.config_dir, 'config.yaml')
        self.config_data = {}

    def load_config(self) -> Dict[str, Any]:
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
        # 保存配置到用户配置文件
        with open(self.user_config, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, allow_unicode=True)