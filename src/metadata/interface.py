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
            "care_and_coarse_catchments.geojson": {
                "desc": ("Similar to care.geojson.  Its extra fields indicate the hydrometric catchment "
                         "area within which each home lies.")},
            "coarse.geojson": {
                "desc": "Scotland's hydrometric river catchments.  At present, derived.  Direct acquisition in future."},
            "SEPA.zip": {
                "desc": ("The zip version of SEPA.geojson. Its geospatial data file encodes the segments, i.e., hydrometric "
                         "area divisions, of Scotland's river catchments.  Each hydrometric river catchment of "
                         "coarse.geojson is a distinct combination of one or more divisions.")},
            "SEPA.geojson": {
                "desc": ("This geospatial data file encodes the segments, i.e., hydrometric area divisions, of Scotland's "
                         "river catchments.  Each hydrometric river catchment of coarse.geojson is a distinct combination "
                         "of one or more divisions.")},
            "rating.csv": {
                "key": "The quality code of a measure.",
                "code": "The letter code of a measure.",
                "description": "The description of the key and code."
            },
            "sch-catchments.geojson": {
                "desc": "The union of the four schools data.  Additionally, the data set includes a field indicating the catchment within which each school lies."
            },
            "sch-primary-denominational.geojson": {
                "desc": "The denominational primary schools."
            },
            "sch-primary-non-denominational.geojson": {
                "desc": "The non-denominational primary schools."
            },
            "sch-secondary-denominational.geojson": {
                "desc": "The denominational secondary schools."
            },
            "sch-secondary-non-denominational.geojson": {
                "desc": "The non-denominational secondary schools."
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
