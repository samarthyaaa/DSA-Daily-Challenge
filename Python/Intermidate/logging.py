import logging#- how to lock different lock handlers, modules, capture traces in the log
import logging.config
logging.config.dictConfig('logging.conf')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
# we can also make our own logger to log any info , or debug in the module

logger = logging.getLogger(__name__)
logger = logging.getLogger("simpleExample")
logger.debug('debug message')
#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
