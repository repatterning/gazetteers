"""Module geo.py"""
import logging

import geopandas


class Geo:
    """
    Geo
    """

    def __init__(self):
        pass

    @staticmethod
    def persist(blob: geopandas.GeoDataFrame, filename: str):
        """

        :param blob:
        :param filename:
        :return:
        """

        try:
            blob.to_file(filename=filename, driver='GeoJSON')
            logging.info('%s: Succeeded', filename)
        except RuntimeError as err:
            raise err from err
