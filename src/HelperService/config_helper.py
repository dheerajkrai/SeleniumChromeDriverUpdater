import sys, getopt
import os
import json

CONFIG_FILE_LOCATION = './config.json'


def parse_args(args):
    global CONFIG_FILE_LOCATION
    try:
      opts, argsv = getopt.getopt(args,"hc:",["config="])
    except getopt.GetoptError:
        print ('Usage : main.py -c </path/to/config/file>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage : main.py -c </path/to/config/file>')
            sys.exit()
        elif opt in ("-c", "--config"):
            CONFIG_FILE_LOCATION = str(arg)
            
    return CONFIG_FILE_LOCATION


def load_config(location):
    config = {}
    #check if location exists
    if not os.path.exists(location) or not os.path.isfile(location):
        print('Unable to find config file at location [' + location + ']')
        exit(-1)
    print('Loading configuration from : ' + location)
    with open(location, 'r') as configfile:
        config = json.load(configfile)
    return config


def setup(args):
    config_location = parse_args(args)
    config = load_config(config_location)
    print('Starting script : Chrome Driver Auto Update')
    if config is None or len(config) == 0:
        print('Application config not set up!')
        exit(1)
    return config