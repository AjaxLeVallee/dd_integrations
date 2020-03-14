from setuptools import setup


setup(
      name = "Datadog HTTP Checker",
      version = "0.1.0",

      py_modules =['src/main'],
      install_requires=[
          'Click',
          'datadog-checks-base',
      ],
      entry_points='''
          [console_scripts]
          yamlCheck=main:cli
          ''',
        )
