#!/bin/usr/python3
import click
from datadog_checks.base import AgentCheck


@click.group()
def cli():
    print("Checked")
    pass


@cli.command()
@click.option('-l','--validate',
    help="Will only validate file")
@click.argument("log_file", required=False)
def check(validate):
    """Will validate then create a corresponding Datadog Synthetic \
check for each check in the file"""
    click.echo("CLI Checker")


@cli.command()
def monitor():
    """Will validate or raise errors in datadog yaml file"""
    pass


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

