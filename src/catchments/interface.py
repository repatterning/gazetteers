"""Module"""
import os
import shutil

import config

class Interface:
    """
    Alas, at present a catchments GeoJSON is not available via an application programming
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

    def exc(self):
        """

        :return:
        """

        src = os.path.join(self.__configurations.data, 'cartography', 'SEPA.geojson')
        shutil.copy(src=src, dst=self.__configurations.cartography_)
