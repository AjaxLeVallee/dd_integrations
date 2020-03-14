#!/bin/usr/python3
import click
from datadog_checks.base import AgentCheck


class Config(object):

    """Some config options to carry along the program"""

    def __init__(self):
        """Defining initialized variables"""
        self.verbose = False
        self.log_file = False
        self.http_yaml_file = False


# Creating the decorator for the config vars
pass_config = click.make_pass_decorator(Config, ensure=True)


class validation_class(object):

    """All Validation related Objects"""

    def __init__(self):
        pass



class montoring_class(object):

    """All Monitoring related Objects"""

    def __init__(self):
        pass



"""
Creating the inital group for the program
"""
@click.group()
@click.option('--verbose', '-v',
    is_flag=True)
@click.argument("http_yaml",
    required=False)
@click.argument("log_file",
    required=False)
@pass_config
def cli(config, verbose, log_file, http_yaml):
    config.verbose = verbose
    config.log_file = log_file
    config.http_yaml_file = http_yaml



"""
When I thought about the goal, the check command really had one part with
another that could be toggled. so I made it one command with a toggle flag.
"""
@cli.command()
@click.option('-g', '--generate_checks', is_flag=True, help="Will generate checks to the file")
@pass_config
def validate(config, generate_checks):
    """Will validate and/or generate the checks for the yaml file given"""
    click.echo(bool(config.log_file))
    click.echo("CLI Checker")




"""
Monitor config has a slightly different function so it was broken out
"""
@cli.command()
@pass_config
def monitor(config):
    """Will validate or raise errors in datadog yaml file"""
    if config.verbose:
        click.echo("Increasing Verbosity")
    click.echo("Monitoring")


