"""Module membership.py"""
import geopandas
import pandas as pd

import src.cuttings
import src.functions.geo


class Membership:
    """
    Per dataframe, this class determines the catchment membership of each place/point, and subsequently saves the data.
    """

    def __init__(self, coarse: geopandas.GeoDataFrame):
        """

        :param coarse: The coarse level catchments
        """

        self.__coarse = coarse

        # Instances
        self.__geo = src.functions.geo.Geo()

    def __pockets(self, frame: geopandas.GeoDataFrame) -> geopandas.GeoDataFrame:
        """

        :param frame:
        :return:
        """

        cuttings = src.cuttings.Cuttings(places=frame.to_crs(epsg=self.__coarse.crs.to_epsg()))
        initial: list[geopandas.GeoDataFrame] = [
            cuttings.members(_elements=_elements) for _elements in self.__coarse.itertuples()]

        return pd.concat(initial, axis=0, ignore_index=True)

    def exc(self, frame: geopandas.GeoDataFrame, filename: str):
        """

        :param frame:
        :param filename:
        :return:
        """

        pockets = self.__pockets(frame=frame)
        self.__geo.persist(blob=pockets, filename=filename)
