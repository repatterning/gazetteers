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

        # Schools
        self.spatial_hub_schools = {'sh_schl:pub_schlpd': 'primary denominational',
                                    'sh_schl:pub_schlpn': 'primary non-denominational',
                                    'sh_schl:pub_schlsd': 'secondary denominational',
                                    'sh_schl:pub_schlsn': 'secondary non-denominational'}
        self.parts_spatial_hub_schools = ['sh_schl:pub_schlpd', 'sh_schl:pub_schlpn', 'sh_schl:pub_schlsd', 'sh_schl:pub_schlsn']
        self.url_spatial_hub_schools = ('https://geo.spatialhub.scot/geoserver/sh_schl/wfs?service=WFS&'
                                        'authkey={authkey}&request=GetFeature&typeName={part}&format_options'
                                        '=filename:School_Catchments_-_Scotland&outputFormat=application/json')

        # From https://data.cefas.co.uk/view/21970
        self.cefas = 'https://raw.githubusercontent.com/repatterning/.github/refs/heads/master/profile/SEPA.zip'
