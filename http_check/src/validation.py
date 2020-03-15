#!/env_3.7/bin/python3.7
import yaml
import os
import re

from formatting import basic


B = basic().BOLD
U = basic().UNDERLINE
E = basic().END
R = basic().RED


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
        def regex_check(regex, element, data):
            if data.get(element):
                for t in data[element]:
                    try:
                        if self.verbose:
                            print(f"Testing tag: {t}. for data[element]: {data[element]}")
                        if re.search(regex, t):
                            if self.verbose:
                                print(f"{data['name']} check is all set with {t} as the tag")
                        break
                    except Exception as e:
                        raise e
                        print(f"{U + data['name'] + E} check does not have a valid tag")
            else:
                print(f"{R}Error No {element} for check: {U + data['name'] + E}")


        def content_check(element, data):
            if data.get(element):
                if self.verbose:
                    print(f"Content in value {U + element + E} of {B + data[element] + E}")
            else:
                print(f"{R}Error no {U + element + E + R} in {B + str(data) + E}")




        def process(self, data):
            """This is going to do some flattening and do some checks on the elements
            along the way. This should also take some params.

            :data: TODO
            :returns: TODO

            """
            with open(self.validation_specs) as vs:
               vs = yaml.load_all(vs, Loader=yaml.FullLoader)
               for spec in vs:
                   # I'll build this out more, but just to obtain these checks for the moment
                   for check in spec:
                       if check['checktype'] == 'regex':
                           regex = check['regex']
                           regex_check(regex, check['check'], data)

                           if self.verbose:
                               print(f"{check['check']} check {B}Finished{E}")

                       if check['checktype'] == 'content':
                           content_check(check['check'], data)
                           if self.verbose:
                               print(f"{check['check']} check {B}Finished{E}")



        if self.verbose:
            print(f"Performing Validation of yaml at {self.http_yaml.name}")
#            __import__('pdb').set_trace()


        with open(self.http_yaml.name) as f:
            yamls = yaml.load_all(f, Loader=yaml.FullLoader)

            for yaml_f in yamls:
                if type(yaml_f) is list:
                    for key in yaml_f:
                        process(self, key)



