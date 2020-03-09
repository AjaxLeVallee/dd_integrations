#!/bin/usr/python3
import argparse
from datadog_checks.base import AgentCheck

__version__ = "0.1.0"

class http_check(AgentCheck):
    def check(self, instance):
        self.count(
            "example_metric.count",
            2,
            tags=["env:dev","metric_submission_type:count"],
        )

        # Calling the functions below twice simulates
        # several metrics submissions during one Agent run.
        self.histogram(
            "example_metric.histogram",
            random.randint(0, 10),
            tags=["env:dev","metric_submission_type:histogram"],
        )
        self.count(
            "plex_worker.histogram",
            random.randint(0, 10),
            tags=["env:dev","metric_submission_type:histogram"],
        )


if __name__ == "__main__":

    """
NAME
    http_check -- check yaml

SYNOPSIS
    http_check [-l --validate] | [-c --checks] | [-m --monitor] teamname

DESCRIPTION


    The options are as follows:

    No Args        Return Help content.

    -h --help      Run help dialog

    -l --validate  Print out a summary of good, warning, and critical checks
                   (count); print out critical checks with their error noted.

    -c --checks    Run validation and create a corresponding Datadog Synthetic
                   check.

    -m --monitor   create or update a monitor which is tagged with the team
                   name, such that the synthetic checks are associated with the
                   monitor.

    """

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
