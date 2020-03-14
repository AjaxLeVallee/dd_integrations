#!/env_3.7/bin/python3.7
import click
from datadog_checks.base import AgentCheck
from monitoring import monitoring_class
from validation import validation_class


class Config(object):

    """Some config options to carry along the program"""

    def __init__(self):
        """Defining initialized variables"""
        self.verbose = False
        self.log_file = False
        self.http_yaml_file = False


# Creating the decorator for the config vars
pass_config = click.make_pass_decorator(Config, ensure=True)



"""
Creating the inital group for the program
"""
@click.group()
@click.option('--verbose', '-v',
    is_flag=True)
@pass_config
def cli(config, verbose):# logfile):
    config.verbose = verbose
    pass
    # config.log_file = log_file
    # config.http_yaml_file = http_yaml


"""
When I thought about the goal, the check command really had one part with
another that could be toggled off or on.
"""
@cli.command()
@click.option('-g', '--generate-checks',
    is_flag=True,
    help="Will generate checks to the file")
# This will need to be changed to True once we get closer to ingesting it.
@click.argument("http_yaml",
    required=False)
@click.argument("log_file",
     required=False)
@pass_config
def validate(config, generate_checks, http_yaml, log_file):
    """Will validate and/or generate the checks for the yaml file given"""
    __import__('pdb').set_trace()
    click.echo("Validate Checker")


"""
Monitor config has a slightly different function so it was broken out
"""
@cli.command()
# This will need to be changed to True once we get closer to ingesting it.
@click.argument("http_yaml",
    required=False,
    type=click.Path(exists=True))
@click.argument("log_file",
     required=False)
@pass_config
def monitor(config, http_yaml, log_file):
    """Will validate or raise errors in datadog yaml file"""
    #__import__('pdb').set_trace()
    #if config.verbose:
    #    click.echo("Increasing Verbosity")
    click.echo("Monitoring")


