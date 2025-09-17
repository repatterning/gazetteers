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

    strings = src.transfer.dictionary.Dictionary().exc(
        path=os.path.join(os.getcwd(), 'warehouse'), extension='*', prefix='')
    strings['metadata'] = strings['vertex'].apply(lambda x: metadata[os.path.basename(x)])
    logger.info(strings)

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

    import src.functions.cache
    import src.transfer.dictionary
    import src.metadata.interface

    metadata = src.metadata.interface.Interface().metadata

    main()
