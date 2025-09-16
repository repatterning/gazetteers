import logging

import geopandas

import src.boundaries.fine


class Interface:

    def __init__(self):
        pass

    @staticmethod
    def exc():

        fine: geopandas.GeoDataFrame = src.boundaries.fine.Fine().exc()
        logging.info(fine)
