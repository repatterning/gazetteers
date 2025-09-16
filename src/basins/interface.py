"""Module rivers/interface.py"""
import logging

import geopandas
import pandas as pd

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

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, assets: pd.DataFrame):
        """

        :param assets:
        :return:
        """

        fine: geopandas.GeoDataFrame = src.basins.fine.Fine().exc()
        self.__logger.info(fine)

        coarse = src.basins.coarse.Coarse(assets=assets, fine=fine).exc()
        self.__logger.info(coarse)
