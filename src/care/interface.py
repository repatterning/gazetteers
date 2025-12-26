"""Module algorithms/interface.py"""

import os

import boto3
import geopandas

import config
import src.care.data
import src.membership


class Interface:
    """
    The interface to the programs of the care package.
    """

    def __init__(self, connector: boto3.session.Session, arguments: dict):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        :param arguments: A set of arguments vis-à-vis computation & data operations objectives.
        """

        self.__connector = connector
        self.__arguments = arguments

        # Instances
        self.__configurations = config.Config()

    def exc(self, coarse: geopandas.GeoDataFrame):
        """

        :param coarse:
        :return:
        """

        data: geopandas.GeoDataFrame = src.care.data.Data(
            connector=self.__connector, arguments=self.__arguments).exc()

        # membership, etc.
        filename = os.path.join(self.__configurations.cartography_, 'care_and_coarse_catchments.geojson')
        src.membership.Membership(coarse=coarse).exc(frame=data, filename=filename)
