#!/bin/usr/python3
import click
from datadog_checks.base import AgentCheck


class Config(object):

    """Some config options to carry along the program"""

    def __init__(self):
        """Defining initialized variables"""
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', '-v', is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose

@cli.command()
@click.option('-l','--validate',
    help="Will only validate file")
@click.argument("log_file", required=False)
@pass_config
def check(config, validate):
    """Will validate then create a corresponding Datadog Synthetic check for \
each check in the file"""
    click.echo("CLI Checker")


@cli.command()
@pass_config
def monitor(config):
    """Will validate or raise errors in datadog yaml file"""
    if config.verbose:
        click.echo("Increasing Verbosity")
    click.echo("Monitoring")


#class http_check(AgentCheck):
#    def check(self, instance):
#        self.count(
#            "example_metric.count",
#            2,
#            tags=["env:dev","metric_submission_type:count"],
#        )
#
#        # Calling the functions below twice simulates
#        # several metrics submissions during one Agent run.
#        self.histogram(
#            "example_metric.histogram",
#            random.randint(0, 10),
#            tags=["env:dev","metric_submission_type:histogram"],
#        )
#        self.count(
#            "plex_worker.histogram",
#            random.randint(0, 10),
#            tags=["env:dev","metric_submission_type:histogram"],
#        )

