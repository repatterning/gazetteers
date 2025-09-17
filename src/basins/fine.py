"""Module basins/fine.py"""
import os

import geopandas

import config


class Fine:
    """
    Alas, a catchments/river-basins GeoJSON is not available via an application programming
    interface.  A zipped version of SEPA.geojson, retrieved from https://data.cefas.co.uk/view/21970, is
    available via
    <a href="https://github.com/repatterning/gazetteers/blob/792f47e25208c259e6a68f7ca8a80a83aacdbd2c/config.py#L32"
    target="_blank">self.cefas in config.py</a><br><br>
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

    def __persist(self, frame: geopandas.GeoDataFrame):
        """
        Ascertaining a copy of the fine-grained basins exists within the cloud-upload area

        :return:
        """

        filename = os.path.join(self.__configurations.cartography_, 'SEPA.geojson')

        try:
            frame.to_file(filename=filename, driver='GeoJSON')
        except RuntimeError as err:
            raise err from err

    def exc(self) -> geopandas.GeoDataFrame:
        """
        if local &rarr; <br>
        &nbsp; &nbsp; filename = f'zip:{os.sep}{os.sep}{os.path.join(...)}' <br><br>

        :return:
        """

        try:
            frame = geopandas.read_file(filename=self.__configurations.cefas)
            self.__persist(frame=frame)
            return frame
        except FileNotFoundError as err:
            raise err from err
