import os
import sys
import time
import os

from sources.build import execute_build
from sources.build.args import parse_args
from sources.build.logger import logger

if __name__ == "__main__":
    git_root = os.path.dirname(os.path.realpath(__file__))
    args = parse_args()

    try:
        start = time.time()
        execute_build(git_root, args)
        end = time.time() - start

        logger.info("")
        logger.info(f"Built in {round(end, 3)}s")
    except Exception as e:
        logger.error("Something went wrong when building the theme:", exc_info=e)
