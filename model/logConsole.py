__author__ = 'xueyan'
import sys,os,logging,configparser
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
class LogConsole(object):
    log_file = os.path.join(os.getcwd(),'F:/web/pythonAutoYes/log/yesLog.log')
    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
    logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)