
import logging
import shapely
import os

import boto3
import geopandas
import pandas as pd
import dask

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

    @dask.delayed
    def __get_data(self, filename: str, label: str) -> geopandas.GeoDataFrame:

        try:
            data = geopandas.read_file(filename=filename)
        except FileNotFoundError as err:
            raise err from err

        self.__persist(blob=data, name='sch-' + label.replace(' ', '-') + '.geojson')

        data.loc[:, 'label'] = label
        data.info()

        return data

    @dask.delayed
    def __get_centroid(self, data: geopandas.GeoDataFrame):

        # centroid of each school's multipolygon
        data.geometry = data.geometry.centroid

        return data

    def exc(self):

        authkey = self.__secret.exc(secret_id=self.__arguments.get('project_key_name'), node='spatial-hub-geoserver')

        computations = []
        doublet = self.__configurations.spatial_hub_schools

        for part, label in zip(doublet.keys(), doublet.values()):

            filename = self.__configurations.url_spatial_hub_schools.format(authkey=authkey, part=part)

            # the data of a set of schools
            data = self.__get_data(filename=filename, label=label)

            # centroids instead of multi-polygons
            data = self.__get_centroid(data=data.copy())

            computations.append(data)

        calculations = dask.compute(computations, scheduler='threads')[0]

        structure = pd.concat(calculations, axis=0, ignore_index=True)

        logging.info(structure)
