```
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
```
