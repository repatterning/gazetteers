"""Module basins/fine.py"""
import os
import shutil
import geopandas

import config


class Fine:
    """
    Alas, at present a catchments/river-basins GeoJSON is not available via an application programming
    interface.  Download a GeoJSON from https://data.cefas.co.uk/view/21970, save
    as SEPA.geojson<br><br>

    root:<br>
      &nbsp;&nbsp;data:<br>
      &nbsp;&nbsp;&nbsp;&nbsp;cartography: SEPA.geojson<br>
      &nbsp;&nbsp;src:<br>
      &nbsp;&nbsp;warehouse:<br>
      <br>
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()
        self.__src = os.path.join(self.__configurations.data, 'cartography', 'SEPA.geojson')

    def __persist(self):
        """
        Ascertaining a copy of the fine-grained basins exists within the cloud-upload area

        :return:
        """

        try:
            shutil.copy(src=self.__src, dst=self.__configurations.cartography_)
        except FileNotFoundError as err:
            raise err from err

    def exc(self) -> geopandas.GeoDataFrame:
        """

        :return:
        """

        self.__persist()

        try:
            return geopandas.read_file(filename=self.__src)
        except FileNotFoundError as err:
            raise err from err
