import logging

import geopandas

import src.basins.fine


class Interface:

    def __init__(self):
        pass

    @staticmethod
    def exc():

        fine: geopandas.GeoDataFrame = src.basins.fine.Fine().exc()
        logging.info(fine)
