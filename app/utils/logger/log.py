import logging


def configure_logger(business_name: str="default business"):
    """
    The `configure_logger` function sets up a logger named "my_app_logger" with both console and file
    handlers.
    :return: The function `configure_logger` is returning a logger object that has been configured with
    a console handler and a file handler, both using the specified formatter.
    """
    
    logger = logging.getLogger(business_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(f'{business_name}.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = configure_logger()
