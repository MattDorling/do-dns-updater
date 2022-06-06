import os
import yaml

DO_API_TOKEN = os.environ['DO_API_TOKEN']


with open('config.yml', 'r') as config_file:
    data = yaml.safe_load(config_file)

    DOMAIN_NAME = data['domain']
    PUBLIC_IP_CHECK_INTERVAL = data['public_ip_check_interval']
    NAME = data['records'][0]['name']
    TYPE = data['records'][0]['type']
