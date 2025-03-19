#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH_DEFAULT = os.path.join(os.path.join(PROJ_DIR, 'logs'), 'console.log')


def logger(
        log_path: str = None,
        log_console: bool = True,
        log_keep_days: int = 30,
) -> logging.Logger:
    if not log_path:
        log_path = LOG_PATH_DEFAULT
    log_handle = logging.getLogger(log_path)

    formatter = logging.Formatter(
        "%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    log_handle.setLevel(logging.DEBUG)

    if log_console:
        log_screen = logging.StreamHandler()
        log_screen.setFormatter(formatter)
        log_handle.addHandler(log_screen)

    try:
        file_handler = TimedRotatingFileHandler(
            filename=log_path,
            when="MIDNIGHT",
            backupCount=log_keep_days,
        )
        file_handler.suffix = "%Y-%m-%d.log"
        file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
        file_handler.setFormatter(formatter)
        log_handle.addHandler(file_handler)
    except FileNotFoundError as e:
        log_handle.error(e)
    return log_handle


log = logger()
