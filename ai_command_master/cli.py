import click

from . import core

# 1. 定义主命令组 'ai'
# invoke_without_command=True 允许在没有指定子命令时执行 cli 函数本身
@click.group(invoke_without_command=True, context_settings=dict(help_option_names=['-h', '--help']))
# 捕获所有未被识别为选项的参数
@click.argument('description_or_command', nargs=-1)
# 允许访问上下文信息，比如是否调用了子命令
@click.pass_context
def cli(ctx, description_or_command):
    """
    ai-command-master: 通过自然语言生成并执行终端命令。

    默认行为是 'ask' 命令。例如：
    'ai list all python files' 等同于 'ai ask list all python files'.
    """
    # 检查是否有子命令被调用
    if ctx.invoked_subcommand is None:
        # 如果没有子命令被调用
        if description_or_command:
            # 并且提供了参数，则认为这些参数是 'ask' 命令的描述
            description = ' '.join(description_or_command)
            ctx.invoke(ask, description=description_or_command)
            # click.echo(f"默认行为: 执行 'ask' 命令...") # 也可以这样调用
            # 直接调用 ask 命令的处理逻辑 (或者其背后的核心函数)
            # core.handle_ask_request(description)
        else:
            # 如果没有子命令，也没有提供参数，则显示帮助信息
            click.echo(ctx.get_help())
            ctx.exit()


# 2. 定义 'ask' 子命令
@cli.command()
@click.argument('description', nargs=-1, required=True) # nargs=-1 允许多个词作为描述
def ask(description):
    """(默认) 根据自然语言描述生成命令。"""
    full_description = ' '.join(description)
    # 调用核心处理函数
    core.handle_ask_request(full_description)


# 3. 定义 'config' 命令组


# 4. 定义 'log' 命令