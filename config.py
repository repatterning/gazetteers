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
        self.series_ = os.path.join(self.warehouse, 'data', 'series')
        self.references_ = os.path.join(self.warehouse, 'references')

        # Template
        self.s3_parameters_key = 's3_parameters.yaml'

        # Care
        self.care_ = ('https://geo.spatialhub.scot/geoserver/sh_chep/wfs?service=WFS&'
                      'authkey={spatial-hub-geoserver}&request=GetFeature&typeName=sh_chep:pub_chep&format_options'
                      '=filename:Care_Homes_for_Older_People_-_Scotland&outputFormat=application/json')
