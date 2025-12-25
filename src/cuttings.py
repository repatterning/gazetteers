"""Module care/cuttings.py"""
import geopandas
import pandas as pd
import shapely


class Cuttings:
    """
    Herein, the aim is to determine the hydrometric catchment that a point belongs to.  The catchments 
    are contiguous, non-overlapping, catchments.  Each point should be a member of a single catchment only.
    """

    def __init__(self, places: geopandas.GeoDataFrame):
        """

        :param places: Each instance encodes the details of a place.
        """

        self.__places = places

    def __is_member(self, _polygon: shapely.geometry.polygon.Polygon) -> pd.Series:
        """
        Determines whether each place lies within the input polygon.

        :param _polygon: The polygon of a catchment area
        :return:
        """

        return self.__places.geometry.apply(lambda y: y.within(_polygon))

    def inside(self, _polygon: shapely.geometry.polygon.Polygon) -> int:
        """
        Determines the # of places that are located within the input polygon

        :param _polygon:
        :return:
        """

        return sum(self.__is_member(_polygon=_polygon))

    def members(self, _elements) -> geopandas.GeoDataFrame:
        """
        .geometry: shapely.geometry.polygon.Polygon -> A catchment area polygon

        :param _elements: The details of a catchment area; the .geometry entity encodes a catchment area polygon
        :return:
        """

        is_member_of: pd.Series = self.__is_member(_polygon=_elements.geometry)

        frame = self.__places.copy().loc[is_member_of, :]
        frame['catchment_id'] = _elements.catchment_id
        frame['catchment_name'] = _elements.catchment_name

        return frame
