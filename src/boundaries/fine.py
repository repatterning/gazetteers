
import os

import geopandas

import config


class Fine:

    def __init__(self):

        self.__configurations = config.Config()

    def exc(self) -> geopandas.GeoDataFrame:

        filename = os.path.join(self.__configurations.data, 'cartography', 'SEPA.geojson')

        try:
            return geopandas.read_file(filename=filename)
        except FileNotFoundError as err:
            raise err from err
