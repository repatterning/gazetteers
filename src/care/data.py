"""Module data.py"""
import os

import boto3
import geopandas

import config
import src.functions.cache
import src.functions.geo
import src.functions.secret


class Data:
    """
    Data
    """

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



    def __get_data(self) -> geopandas.GeoDataFrame:
        """
        Retrieves a gazetteer of Scotland's care homes.

        :return:
        """

        authkey = self.__secret.exc(secret_id=self.__arguments.get('project_key_name'), node='spatial-hub-geoserver')
        filename = self.__configurations.url_spatial_hub_care.format(authkey=authkey)

        try:
            return geopandas.read_file(filename=filename)
        except FileNotFoundError as err:
            raise err from err

    def exc(self) -> geopandas.GeoDataFrame:
        """

        :return:
        """

        data = self.__get_data()

        # persist
        filename = os.path.join(self.__configurations.cartography_, 'care.geojson')
        src.functions.geo.Geo().persist(blob=data, filename=filename)

        return data
