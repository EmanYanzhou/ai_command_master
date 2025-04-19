"""安全输出类
    接收到格式化处理后的字典，安全的选择处理方式
"""
import click
import pyperclip


class Execution:
    def __init__(self, model: str, response_dict: dict):
        self.model = model
        self.response_dict = response_dict
        self.execution_type = response_dict['conversation_type']

    def execute(self):
        if self.execution_type == "Command":
            self.execute_command()
        elif self.execution_type == "Text":
            self.execute_text()

    def execute_command(self):
        """Command 模式"""
        pyperclip.copy(self.response_dict['content'])
        click.echo(f"{self.model}: ")
        click.echo(f"可能执行的命令为[ {self.response_dict['content']} ]")
        click.echo(f"Warning: {self.response_dict['warning']}")
        if not self.response_dict['tip'] is None:
            click.echo(f"Tip: {self.response_dict['tip']}")
        click.echo("[ 命令已复制到剪贴板，右键鼠标粘贴 ]")

    def execute_text(self):
        """Text 模式"""
        click.echo(f"{self.model}: ")
        click.echo(f"{self.response_dict['content']}")
        click.echo(f"Warning: {self.response_dict['warning']}")
        if not self.response_dict['tip'] is None:
            click.echo(f"Tip: {self.response_dict['tip']}")