#!/env_3.7/bin/python3.7
import click
import os
from datadog_checks.base import AgentCheck
from monitoring import monitoring_class
from validation import validation_class


class Config(object):

    """Some config options to carry along the program"""

    def __init__(self):
        """Defining initialized variables"""
        def_config = '/config'
        self.verbose = False
        self.log_file = False
        self.http_yaml_file = False
        self.config_specs = False
        try:
            spec_file = '/default_validation_specs.yaml'
            os.path.isfile(os.getcwd() + def_config + spec_file)
            self.config_specs = os.path.join(os.getcwd() + def_config + spec_file)
        except Exception as e:
            raise e


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


"""
When I thought about the goal, the check command really had one part with
another that could be toggled off or on.
"""
@cli.command()
@click.option('-g', '--checks',
    is_flag=True,
    help="Will generate checks")
# This will need to be changed to True once we get closer to ingesting it.
@click.argument("http_yaml",
    type=click.File('rb'),
    required=True)
@click.argument("out_log",
    required=False)
@click.argument("validation_config",
    type=click.File('rb'),
    required=False)
@pass_config
def validate(config, checks, http_yaml, out_log, validation_config):
    """Will validate and/or generate the checks for the yaml file given"""
    validation_spec = (validation_config or config.config_specs)
    validation = validation_class(config.verbose, http_yaml, out_log, validation_spec)

    validation.validate()
    if checks and validation.validate:
        return validation.checks



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
def monitor(config, http_yaml, out_log):
    """Will validate or raise errors in datadog yaml file"""
    return monitoring_class()


