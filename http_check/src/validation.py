#!/env_3.7/bin/python3.7
import yaml
import os

class validation_class(object):

    """All Validation related Objects"""

    def __init__(self, verbose, http_yaml=False, out_log=False, validation_spec=False):
        self.verbose = (verbose or False)
        self.http_yaml = (http_yaml or False)
        self.out_log = (out_log or False)
        self.validation_specs = (validation_spec or False)


    def validate(self):
        """Check File syntax

        :file: It should inherit this from the main.py
        :returns: It should return lines that are incorrect or return a "OK!"

        """
        def process(self, data):
            """This is going to do some flattening and do some checks on the elements
            along the way. This should also take some params.

            :data: TODO
            :returns: TODO

            """
            pass
        if self.verbose:
            print(f"Performing Validation of yaml at {self.http_yaml.name}")
            __import__('pdb').set_trace()

#        with open(self.http_yaml.name) as f:
#            yamls = yaml.load_all(f, Loader=yaml.FullLoader)
#
#            for yaml_f in yamls:
#                if type(yaml_f) is list:
#                    for key in yaml_f:



