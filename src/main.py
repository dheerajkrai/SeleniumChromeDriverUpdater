import sys
from HelperService import config_helper as cfgHelper
from HelperService import driver_service as drvrHelper
        
    
def main(args):
    config = cfgHelper.setup(args)
    drvrHelper.download_latest_chrome_driver(config)


if __name__ == '__main__':
    main(sys.argv[1:])