import logging


logger = logging.getLogger('')

logger.setLevel(logging.INFO)

file_log = logging.FileHandler('app.log')
console_log = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)s %(message)s",
    "%d-%m-%Y %H:%M:%S"
)

file_log.setFormatter(formatter)
console_log.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_log)
    logger.addHandler(console_log)