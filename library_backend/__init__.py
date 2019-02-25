import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(module)s::%(funcName)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("LibraryBackend")
