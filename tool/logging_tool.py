#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import logging
import os
from logging.handlers import TimedRotatingFileHandler

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(PROJ_DIR, 'logs')
LOG_NAME = 'console.log'

LOG_FORMATTER = """
{
    "timestamp":"%(asctime)s", 
    "process":"%(process)d", 
    "processName":"%(processName)s", 
    "thread":"%(thread)d", 
    "threadName":"%(threadName)s", 
    "level":"%(levelname)s", 
    "filename":"%(filename)s", 
    "funcName":"%(funcName)s", 
    "lineno":"%(lineno)d",
    "message":"%(message)s", 
}
"""


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'process': record.process,
            'processName': record.processName,
            'thread': record.thread,
            'threadName': record.threadName,
            'level': record.levelname,
            'filename': record.filename,
            'funcName': record.funcName,
            'lineno': record.lineno,
            'message': record.getMessage(),
        }
        return json.dumps(log_record)


def logger(
        log_name: str = LOG_NAME,
        log_dir: str = LOG_DIR,
        log_console: bool = True,
        log_keep_days: int = 30,
        log_level: int = logging.INFO,
) -> logging.Logger:
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_name)

    log_handle = logging.getLogger(log_path)
    log_handle.setLevel(log_level)

    formatter = JsonFormatter(LOG_FORMATTER)

    # log_console
    if log_console:
        log_screen = logging.StreamHandler()
        log_screen.setFormatter(formatter)
        log_handle.addHandler(log_screen)

    # time_handler
    time_handler = TimedRotatingFileHandler(
        filename=log_path,
        when="MIDNIGHT",
        backupCount=log_keep_days,
    )
    time_handler.suffix = "%Y-%m-%d.log"
    time_handler.extMatch = r"^\d{4}-\d{2}-\d{2}.log$"
    time_handler.setFormatter(formatter)
    time_handler.setLevel(log_level)
    log_handle.addHandler(time_handler)

    return log_handle


log = logger()
