import geopandas
import pandas as pd
import shapely


class Cuttings:
    """
    Herein, the aim is to determine the catchment that each care home belongs to.
    """

    def __init__(self, reference: geopandas.GeoDataFrame):
        """

        :param reference: Each instance encodes the details of a care home.
        """

        self.__reference = reference

    def __is_member(self, _polygon: shapely.geometry.polygon.Polygon) -> pd.Series:
        """
        Determines whether a home lies within a polygon; per home.

        :param _polygon: The polygon of a catchment area
        :return:
        """

        return self.__reference.geometry.apply(lambda y: y.within(_polygon))

    def members(self, _elements) -> geopandas.GeoDataFrame:
        """
        .geometry: shapely.geometry.polygon.Polygon -> A catchment area polygon

        :param _elements: The details of a catchment area; the .geometry entity encodes a catchment area polygon
        :return:
        """

        states = self.__is_member(_polygon=_elements.geometry)

        frame = self.__reference.copy().loc[states, :]
        frame['catchment_id'] = _elements.catchment_id
        frame['catchment_name'] = _elements.catchment_name

        return frame
