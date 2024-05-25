import logging

logger = logging.getLogger("catppuccin-gtk")

logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("[%(name)s] [%(levelname)s] - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
