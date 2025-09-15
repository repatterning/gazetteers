"""Module interface.py"""
import datetime
import logging
import os.path

import pandas as pd

import config
import src.gauges.assets
import src.gauges.codes
import src.gauges.rating
import src.gauges.stations
import src.functions.directories
import src.functions.streams


class Interface:
    """
    Interface
    """

    def __init__(self, attributes: dict):
        """

        :param attributes: A set of data acquisition attributes.
        """

        self.__attributes = attributes

        # An instance for reading & writing CSV (comma separated values) data files.
        self.__streams = src.functions.streams.Streams()

        # the references directory
        self.__references_ = config.Config().references_
        directories = src.functions.directories.Directories()
        directories.create(path=self.__references_)

    def __persist(self, blob: pd.DataFrame, name: str) -> None:
        """

        :param blob:
        :param name:
        :return:
        """

        message = self.__streams.write(blob=blob, path=os.path.join(self.__references_, f'{name}.csv'))
        logging.info(message)

    def exc(self):
        """

        :return:
        """

        # Retrieving the codes of <level> sequences, and the details of stations that record <level> sequences.
        codes = src.gauges.codes.Codes().exc()
        stations = src.gauges.stations.Stations().exc()

        # Hence, assets; joining codes & stations, subsequently limiting by stations
        # that were recording measures from a starting point of interest.
        assets = src.gauges.assets.Assets(codes=codes, stations=stations).exc()
        self.__persist(blob=assets, name='assets')

        # Rating
        rating = src.gauges.rating.Rating().exc()
        self.__persist(blob=rating, name='rating')
