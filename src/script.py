"""Module script.py"""
import datetime
import logging
import os
import sys
import geopandas


def main():
    """

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Starting: %s', datetime.datetime.now().isoformat(timespec='microseconds'))

    # Paths
    strings = src.transfer.dictionary.Dictionary().exc(
        path=os.path.join(os.getcwd(), 'warehouse'), extension='*', prefix='')
    strings['metadata'] = strings['vertex'].apply(lambda x: metadata[os.path.basename(x)])
    logger.info(strings)

    # Exploring geopandas & zip
    path = os.path.join(configurations.data, 'cartography', 'SEPA.zip')
    frame = geopandas.read_file(f'zip:{os.sep}{os.sep}{path}')
    logger.info(frame)

    frame.to_file(
        filename=os.path.join(configurations.cartography_, 'SEPA.geojson'),
        driver='GeoJSON')

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

    import config
    import src.functions.cache
    import src.transfer.dictionary
    import src.metadata.interface

    configurations = config.Config()
    metadata = src.metadata.interface.Interface().metadata

    main()
