"""Module rivers/interface.py"""
import logging
import os

import geopandas
import pandas as pd

import config
import src.basins.coarse
import src.basins.fine


class Interface:
    """
    The interface to the programs of the basins package
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __persist(self, coarse: geopandas.GeoDataFrame):
        """

        :param coarse:
        :return:
        """

        filename = os.path.join(self.__configurations.cartography_, 'coarse.geojson')

        try:
            coarse.to_file(filename=filename, driver='GeoJSON')
            logging.info('%s: Succeeded', filename)
        except RuntimeError as err:
            raise err from err

    def exc(self, assets: pd.DataFrame):
        """

        :param assets:
        :return:
        """

        fine: geopandas.GeoDataFrame = src.basins.fine.Fine().exc()
        self.__logger.info(fine)

        coarse = src.basins.coarse.Coarse(assets=assets, fine=fine).exc()
        self.__logger.info(coarse)

        self.__persist(coarse=coarse)
