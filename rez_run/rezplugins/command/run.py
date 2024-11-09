"""
Execute the given command inside the package resolved env.
"""

import argparse
import os
from rez.cli.build import get_current_developer_package
from rez.command import Command
from rez.resolved_context import ResolvedContext

# This attribute is optional, default behavior will be applied if not present.
command_behavior = {
    "hidden": False,  # (bool): default False
    "arg_mode": None,  # (str): "passthrough", "grouped", default None
}

_package = None


def get_current_developer_package():
    from rez.packages import get_developer_package

    global _package

    if _package is None:
        _package = get_developer_package(os.getcwd())

    return _package


def setup_parser(parser, completions=False):
    parser.add_argument("cmd",help="Command to run")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Command arguments")


def command(opts, parser=None, extra_arg_groups=None):
    package = get_current_developer_package()
    c = ResolvedContext(package_requests=[package.qualified_name])

    available_tool = set()
    for _, tools in c.get_tools().values():
        available_tool.update(set(tools))

    if opts.cmd not in tools:
        print(f"No tool is matching with name '{opts.cmd}'")
        return

    c.execute_shell(command=[opts.cmd, *opts.args], detached=True)


class RunCommand(Command):
    @classmethod
    def name(cls):
        return "run"


def register_plugin():
    return RunCommand
