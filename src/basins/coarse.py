"""Module coarse.py"""
import logging

import dask
import geopandas
import pandas as pd
import shapely

import src.cuttings


class Coarse:
    """
    Coarse
    """

    def __init__(self, assets: pd.DataFrame, fine: geopandas.GeoDataFrame):
        """

        :param assets: Each instance represents a distinct gauge station, alongside its details.
        :param fine: The low level, most granular, catchment-segments fine.
        """

        self.__assets = assets
        self.__fine = fine

    def __get_attributes(self) -> geopandas.GeoDataFrame:
        """

        :return:
        """

        attributes = geopandas.GeoDataFrame(
            self.__assets,
            geometry=geopandas.points_from_xy(self.__assets['station_longitude'], self.__assets['station_latitude'])
        )
        attributes.crs = 'epsg:4326'

        return attributes

    @dask.delayed
    def __intersections(self, places: geopandas.GeoDataFrame, code: int, name: str) -> geopandas.GeoDataFrame:
        """

        :param places:
        :param code:
        :param name:
        :return:
        """

        # Which [child] polygons are associated with the catchment in focus?
        identifiers = self.__fine.geometry.map(src.cuttings.Cuttings(places=places).inside)
        applicable = self.__fine.copy().loc[identifiers > 0, :]

        # Convert the polygons into a single polygon.
        frame = geopandas.GeoDataFrame({'catchment_id': [code], 'catchment_name': [name]})

        frame.set_geometry([shapely.unary_union(applicable.geometry)], inplace=True)

        return frame

    def exc(self) -> geopandas.GeoDataFrame:
        """

        :return:
        """

        attributes = self.__get_attributes()
        catchments = self.__assets[['catchment_id', 'catchment_name']].drop_duplicates()

        computations = []
        for code, name in zip(catchments.catchment_id.values, catchments.catchment_name.values):
            places = attributes.copy().loc[attributes['catchment_id'] == code, :]
            intersections = self.__intersections(places=places, code=code, name=name)
            computations.append(intersections)
        _coarse = dask.compute(computations, scheduler='threads')[0]

        coarse: geopandas.GeoDataFrame = pd.concat(_coarse, ignore_index=True, axis=0)
        coarse.crs = self.__fine.crs.srs
        logging.info('Coördinate Reference System:\n%s', coarse.crs)

        return coarse
