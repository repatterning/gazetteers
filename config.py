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
