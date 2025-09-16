"""Module script.py"""
import datetime
import logging
import os
import sys


def main():
    """

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Starting: %s', datetime.datetime.now().isoformat(timespec='microseconds'))

    # Basins
    src.basins.interface.Interface().exc()

    # Deleting __pycache__
    src.functions.cache.Cache().exc()

if __name__ == '__main__':

    # Setting-up
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    import src.basins.interface
    import src.functions.cache

    main()
