
import logging
import boto3
import geopandas

import src.schools.data


class Interface:

    def __init__(self, connector: boto3.session.Session, arguments: dict):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        :param arguments: A set of arguments vis-à-vis computation & data operations objectives.
        """

        self.__connector = connector
        self.__arguments = arguments

    def exc(self):

        data: geopandas.GeoDataFrame = src.schools.data.Data(connector=self.__connector, arguments=self.__arguments).exc()
        logging.info(data)
