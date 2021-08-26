import logging


# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logger = logging.getLogger()
# logger.setLevel('DEBUG')


# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='[%(levelname)s] [%(asctime)s ] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.basicConfig(filename='example.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='[%(levelname)s] [%(asctime)s ] %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too')
