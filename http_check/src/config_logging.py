#!/env_3.7/bin/python3.7
# import logging
from formatting import basic

B = basic().BOLD
U = basic().UNDERLINE
E = basic().END
R = basic().RED
G = basic().GREEN
Y = basic().YELLOW


class Logging(object):

    """Class for logging"""

    def __init__(self):
        """
        TODO : good, warning, and critical

        For the moment we need to make some custom logging

        logging.basicConfig(filename='http_check.log',
            filemode='w')
        """
        self.count_good = 0
        self.count_warn = 0
        self.count_critical = 0
        self.good_list = []
        self.warn_list = []
        self.critical_list = []


    def GOOD(self, error_info):
        self.count_good += 1
        self.good_list.append(error_info)


    def WARN(self, error_info):
        self.count_warn += 1
        self.warn_list.append(error_info)


    def CRIT(self, error_info):
        self.count_critical += 1
        self.critical_list.append(error_info)


    def report(self):
        """Prints out a report of the information"""
        print(f"{G}GOOD : {self.count_good}{E}")
        for err in self.good_list:
            print(f"{G} - Good{E} - {err}")

        print(f"{Y}WARN: {self.count_warn}{E}")

        print(f"{R}CRITCAL : {self.count_critical}{E}")

        for err in self.critical_list:
            print(f"{R} - Error: {err}")

