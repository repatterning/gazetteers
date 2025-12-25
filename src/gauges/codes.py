"""Module codes.py"""

import logging

import pandas as pd
import boto3

import src.elements.text_attributes as txa
import src.functions.streams
import src.gauges.special


class Codes:
    """
    <b>Notes</b><br>
    ------<br>

    Extracts time series codes.<br>
    """

    def __init__(self, connector: boto3.session.Session):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        """

        self.__connector = connector

        self.__streams = src.functions.streams.Streams()

        # # The uniform resource locator for the time series codes list vis-à-vis <Level>
        self.__uri = ('https://timeseries.sepa.org.uk/KiWIS/KiWIS?service=kisters&type=queryServices&datasource=0'
                      '&request=getTimeseriesList&catchment_no=*&stationparameter_name=Level&ts_name=15minute'
                      '&returnfields=catchment_id,catchment_no,catchment_name,station_id,station_no,station_name,'
                      'ts_name,ts_id,ts_path,coverage'
                      '&dateformat=yyyy-MM-dd&format=csv')

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        buffer = src.gauges.special.Special(connector=self.__connector).get_text(url=self.__uri)

        text = txa.TextAttributes(uri=buffer, header=0, sep=';')
        frame = self.__streams.read(text=text)
        frame.info()
        logging.info(frame)

        return frame




















