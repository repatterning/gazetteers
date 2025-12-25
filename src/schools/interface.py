"""Module interface.py"""
import logging
import os

import boto3
import geopandas

import config
import src.cuttings
import src.membership
import src.schools.data


class Interface:
    """
    An interface to the `src.schools` package's programs
    """

    def __init__(self, connector: boto3.session.Session, coarse: geopandas.GeoDataFrame, arguments: dict):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        :param coarse: The coarse level river basins
        :param arguments: A set of arguments vis-à-vis computation & data operations objectives.
        """

        self.__connector = connector
        self.__coarse = coarse
        self.__arguments = arguments

        # Instances
        self.__configurations = config.Config()

    def exc(self):
        """

        :return:
        """

        data: geopandas.GeoDataFrame = src.schools.data.Data(
            connector=self.__connector, arguments=self.__arguments).exc()

        # Intersects, Persist
        filename = os.path.join(self.__configurations.cartography_, 'sch-catchments.geojson')
        src.membership.Membership(coarse=self.__coarse).exc(frame=data, filename=filename)
