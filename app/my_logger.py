#!/usr/bin/python
# -*- coding:utf-8 -*-
import os, stat
import logging


def init_logger(level, log_name=None):
    FLASK_LOG_DIR = os.path.join(os.path.abspath('.'), 'log')

    if not os.path.exists(FLASK_LOG_DIR):
        os.makedirs(FLASK_LOG_DIR)
        os.chmod(FLASK_LOG_DIR, stat.S_IWOTH)

    logger = logging.getLogger(log_name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(FLASK_LOG_DIR, encoding='utf-8')
    formatter = logging.Formatter('[%(asctime)s %(filename)s:%(lineno)s] - %(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger


logger = init_logger(logging.DEBUG, log_name="flask")
