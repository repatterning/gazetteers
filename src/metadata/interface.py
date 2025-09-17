"""Module metadata/interface.py"""


# pylint: disable=R0903
class Interface:
    """
    The metadata of the gazetteers.
    """

    def __init__(self):
        """
        Constructor
        """

        self.metadata = {
            "care.geojson": {
                "desc": "A geospatial data file that encodes known care home locations across Scotland."},
            "coarse.geojson": {
                "desc": "Scotland's hydrometric river catchments.  At present, derived.  Direct acquisition in future."},
            "SEPA.geojson": {
                "desc": ("This geospatial data file encodes the segments, i.e., hydrometric area divisions, of Scotland's "
                         "river catchments.  The coarse.geojson file encodes the river catchment boundaries.")},
            "rating.csv": {
                "key": "The quality code of a measure.",
                "code": "The letter code of a measure.",
                "description": "The description of the key and code."
            },
            "assets.csv": {
                "station_id": "The measuring station identification code.",
                "station_name": "The station name.",
                "catchment_id": "The identification code of the catchment wherein the measuring station resides.",
                "catchment_name": "The name of the catchment wherein the measuring station resides.",
                "ts_id": "The water level time series identification code.",
                "ts_name": "The name of the time series with respect to its granularity.",
                "from": "The date of the earliest record, yyyy-mm-dd.",
                "to": "The date of the latest record, at retrieval time, yyyy-mm-dd.",
                "station_latitude": "Latitude, degree decimal.",
                "station_longitude": "Longitude, degree decimal.",
                "river_id": "If the station resides on a river, the identification code of the river.",
                "river_name": "The river name.",
                "catchment_size": "In square kilometres.",
                "gauge_datum": "The reference point of a gauge site, in metres.",
                "on_river": "If the measuring station is on a river True, otherwise False."
            }
        }
