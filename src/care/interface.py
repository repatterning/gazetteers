"""Module algorithms/interface.py"""
import logging
import os

import boto3
import geopandas
import pandas as pd

import config
import src.functions.cache
import src.functions.secret
import src.care.cuttings


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

    def __persist(self, blob: geopandas.GeoDataFrame, name: str):
        """

        :param blob:
        :param name:
        :return:
        """

        filename = os.path.join(self.__configurations.cartography_, name)

        try:
            blob.to_file(filename=filename, driver='GeoJSON')
            logging.info('%s: Succeeded', filename)
        except RuntimeError as err:
            raise err from err

    def exc(self, coarse: geopandas.GeoDataFrame):
        """

        :param coarse:
        :return:
        """

        frame = self.__get_data()

        # Determining the catchment area of each care home
        cuttings = src.care.cuttings.Cuttings(reference=frame.to_crs(epsg=coarse.crs.to_epsg()))
        initial: list[geopandas.GeoDataFrame] = [
            cuttings.members(_elements=_elements) for _elements in coarse.itertuples()]
        pockets: geopandas.GeoDataFrame = pd.concat(initial, axis=0, ignore_index=True)

        # Persist
        self.__persist(blob=frame, name='care.geojson')
        self.__persist(blob=pockets, name='care_and_coarse_catchments.geojson')
