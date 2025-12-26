"""Module stations.py"""

import boto3
import pandas as pd

import src.elements.text_attributes as txa
import src.functions.streams
import src.gauges.special


class Stations:
    """
    <b>Notes</b><br>
    ------<br>

    The stations.<br>
    """

    def __init__(self, connector: boto3.session.Session):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        """

        self.__connector = connector

        # Instances
        self.__streams = src.functions.streams.Streams()

        # The uniform resource locator for the stations vis-à-vis <Level>
        self.__uri = (
            'https://timeseries.sepa.org.uk/KiWIS/KiWIS?service=kisters&type=queryServices&datasource=0'
            '&request=getstationlist&stationparameter_name=Level&returnfields=station_id,station_no,station_name,'
            'catchment_id,catchment_no,catchment_name,station_latitude,station_longitude,'
            'station_carteasting,station_cartnorthing,river_id,river_name,ca_sta&'
            'ca_sta_returnfields=CATCHMENT_SIZE,GAUGE_DATUM,GROUND_DATUM,GWREF_DATUM&object_type=General&format=csv')

    def exc(self) -> pd.DataFrame:
        """
        logging.info(data[['catchment_id', 'catchment_no', 'catchment_name']].drop_duplicates())

        :return:
        """

        buffer = src.gauges.special.Special(connector=self.__connector).get_text(url=self.__uri)
        text = txa.TextAttributes(uri=buffer, header=0, sep=';')
        data = self.__streams.read(text=text)

        return data
