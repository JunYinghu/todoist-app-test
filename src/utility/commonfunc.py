import string
import random


class CommonFunc(object):
    def __init__(self, config):
        self.config = config

    def get_random_project_name(self, size):
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    def get_api_token(self, section, flag):
        return self.config.get(section, flag)

    def get_api_endpoint(self, section, flag):
        return self.config.get(section, flag)
