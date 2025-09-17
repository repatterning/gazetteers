"""Module config.py"""
import os


# pylint: disable=R0903
class Config:
    """
    Project settings
    """

    def __init__(self):
        """
        Constructor
        """

        self.data = os.path.join(os.getcwd(), 'data')

        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.references_ = os.path.join(self.warehouse, 'references')
        self.cartography_ = os.path.join(self.warehouse, 'cartography')

        # Keys
        self.s3_parameters_key = 's3_parameters.yaml'
        self.arguments_key = 'gazetteers/arguments.json'

        # Care
        self.url_spatial_hub_care = ('https://geo.spatialhub.scot/geoserver/sh_chep/wfs?service=WFS&'
                                     'authkey={authkey}&request=GetFeature&typeName=sh_chep:pub_chep&format_options'
                                     '=filename:Care_Homes_for_Older_People_-_Scotland&outputFormat=application/json')
