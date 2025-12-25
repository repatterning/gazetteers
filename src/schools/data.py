
import logging
import os

import boto3
import geopandas
import pandas as pd

import config
import src.functions.cache
import src.functions.secret

class Data:

    def __init__(self, connector: boto3.session.Session, arguments: dict):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        :param arguments: A set of arguments vis-à-vis computation & data operations objectives.
        """

        self.__connector = connector
        self.__arguments = arguments

        self.__secret = src.functions.secret.Secret(connector=self.__connector)
        self.__configurations = config.Config()

    @staticmethod
    def __get_data(filename: str) -> geopandas.GeoDataFrame:

        try:
            return geopandas.read_file(filename=filename)
        except FileNotFoundError as err:
            raise err from err

    def exc(self):

        authkey = self.__secret.exc(secret_id=self.__arguments.get('project_key_name'), node='spatial-hub-geoserver')

        doublet = self.__configurations.spatial_hub_schools
        for part, label in zip(doublet.keys(), doublet.values()):

            logging.info(part)

            filename = self.__configurations.url_spatial_hub_schools.format(authkey=authkey, part=part)
            data = self.__get_data(filename=filename)
            data.loc[:, 'label'] = label
            data.info()
    