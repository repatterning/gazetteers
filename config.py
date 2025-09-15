"""
Module config
"""
import os
import datetime
import time


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.references_ = os.path.join(self.warehouse, 'references')
        self.cartography_ = os.path.join(self.warehouse, 'cartography')

        # Keys
        self.s3_parameters_key = 's3_parameters.yaml'
        self.arguments_key = 'gazetteers/arguments.json'

        # Care
        self.care_ = ('https://geo.spatialhub.scot/geoserver/sh_chep/wfs?service=WFS&'
                      'authkey={authkey}&request=GetFeature&typeName=sh_chep:pub_chep&format_options'
                      '=filename:Care_Homes_for_Older_People_-_Scotland&outputFormat=application/json')
