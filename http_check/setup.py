from setuptools import setup


setup(
      name = "Datadog HTTP Checker",
      version = "0.1.0",
      package_dir={'': 'src'},
      py_modules =[''],
      install_requires=[
          'Click',
          'datadog-checks-base',
          'pyyaml',
      ],
      entry_points='''
          [console_scripts]
          yamlCheck=main:cli
          ''',
        )
