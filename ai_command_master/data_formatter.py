"""格式处理类
    处理返回的格式为各种类型
"""

class DataFormatter:
    def __init__(self, input_string):
        self.input_string = input_string


    def parse(self):
        # 初始化结果字典
        result = {
            'conversation_type': '',
            'risk_level': '',
            'warning': '',
            'tip': '',
            'content': ''
        }

        # 按照 "|/|" 分割字符串，假设原字符串是"[Text][Low(正常交流,无风险)][]|/|请提供具体指令需求"
        parts = self.input_string.split('|/|')

        # 第一部分是 [Text][Low(正常交流,无风险)][]
        first_part = parts[0]

        # 提取 conversation_type
        conversation_type = first_part.split('[')[1].split(']')[0]
        result['conversation_type'] = conversation_type

        # 提取 risk_level 和 warning
        risk_level_part = first_part.split('[')[2].split(']')[0]
        risk_level = risk_level_part.split('(')[0]
        warning = risk_level_part.split('(')[1].split(')')[0]
        result['risk_level'] = risk_level
        result['warning'] = warning

        # 提取 tip
        tip_part = first_part.split('[')[3].split(']')[0]
        result['tip'] = tip_part

        # 第二部分是内容
        result['content'] = parts[1].strip()

        return result