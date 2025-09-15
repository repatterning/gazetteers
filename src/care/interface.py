"""Module algorithms/interface.py"""
import io
import logging
import sys
import xml.etree.ElementTree as et

import boto3
import geopandas
import requests

import src.functions.cache
import src.functions.secret


class Interface:
    """
    The interface to the programs of the algorithms package.
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
