import os
import sys
import time
import os

from scripts import build
from scripts.args import parse_args
from scripts.logger import logger

if __name__ == "__main__":
    git_root = os.path.dirname(os.path.realpath(__file__))
    args = parse_args()

    try:
        start = time.time()
        build(git_root, args)
        end = time.time() - start

        logger.info('')
        logger.info(f'Built in {round(end, 3)}s')
    except Exception as e:
        logger.error("Something went wrong when building the theme:", exc_info=e)
