import click

from ai_command_master import core

# 定义主命令组 'ai'
# 该命令组实现了一个CLI工具，是aicmd的核心功能
# 支持直接执行命令或通过子命令执行特定功能
@click.group(invoke_without_command=True, context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('description_or_command', nargs=-1)  # 接收任意数量的参数作为命令描述
@click.pass_context  # 注入click上下文，用于访问命令运行时的状态信息
def cli(ctx, description_or_command):   # ctx是Click的上下文对象,类型为click.Content
    """
    ai-command-master: 通过自然语言生成并执行终端命令.

    默认行为是 'ask' 命令.
    例如:
    'ai list all python files' 等同于 'ai ask list all python files'.
    """
    # 检查是否有子命令被调用
    if ctx.invoked_subcommand is None:
        if description_or_command:
            # 如果提供了参数但没有指定子命令,将参数作为ask命令的输入.
            # 合并多个参数为一个完整的描述
            full_description: str = ' '.join(description_or_command)
            # 调用ask命令处理自然语言描述;invoke是上下文对象的一个方法,作用是显示调用命令
            ctx.invoke(ask, full_description=full_description)
        else:
            # 没有参数也没有子命令时，显示帮助信息
            click.echo(ctx.get_help())
            ctx.exit()


# ask子命令：将自然语言描述转换为终端命令
@cli.command()
@click.argument('full_description', nargs=-1, required=True)  # 必须提供至少一个参数作为命令描述
def ask(full_description: str):

    """
    (默认) 根据自然语言描述生成命令。
    参数:
        full_description: 自然语言描述的命令需求，支持多个参数，将被合并为一个描述字符串
    示例:
        ai 列出所有java文件
        ai ask list all python files
        ai ask create a new directory named test
    """

    # 调用核心处理函数生成命令
    # resp_command =
    core.start_request(full_description)
    
    # 将生成的命令复制到剪贴板并显示给用户
    # try:
    #     pyperclip.copy(resp_command[0])  # resp_command[0]为生成的命令
    #     click.echo(f"{resp_command[1]}: {resp_command[0]}")  # resp_command[1]为命令说明
    #     click.echo("【命令已复制到剪贴板，右键鼠标粘贴】")
    # except Exception as e:
    #     click.echo(f"复制命令时出错: {str(e)}", err=True)

# 3. 定义 'config' 命令组 - TODO: 实现配置管理功能


# 4. 定义 'log' 命令 - TODO: 实现日志查看功能