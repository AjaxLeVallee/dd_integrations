# yamlCheck tool

It's at about this point that I've put in about 8-10hrs of work, f95a7a6e7b5e242d4e4f1de94938097e6bb2678e

## Basic usage
```

Usage: yamlCheck [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --verbose
  --help         Show this message and exit.

Commands:
  monitor   Will validate or raise errors in datadog yaml file
  validate  Will validate and/or generate the checks for the yaml file given
```

## Installation

```
Clone repo
make build
source ./env_3.7/bin/activate
```

## Light reading

The main command yamlCheck, has two sub commands, validate and monitor.

Thinking about the check generation I was thinking this should be a flag used as
it was running the validation step anyway, so it's off by default but if you
would like it to generate a synthetic check add the flag to the command.
From a usability standpoint the flag could be longer, to be more descriptive
like: `--generate-checks` (which is why the shorthand is `-g`) this could be
changed down the road though.

