"""
Module setup.py
"""
import sys

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.functions.directories
import src.s3.bucket


class Setup:
    """

    Notes
    -----

    This class prepares the Amazon S3 (Simple Storage Service) and local data environments.
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """
        
        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this project, e.g., region code
                              name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()

    def __s3(self) -> bool:
        """
        Prepares an Amazon S3 (Simple Storage Service) bucket.

        :return:
        """

        # An instance for interacting with Amazon S3 buckets.
        bucket = src.s3.bucket.Bucket(service=self.__service, location_constraint=self.__s3_parameters.location_constraint,
                                      bucket_name=self.__s3_parameters.internal)

        if bucket.exists():
            return True

        return bucket.create()

    def __local(self) -> bool:
        """

        :return:
        """

        # An instance for interacting with local directories
        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__configurations.warehouse)

        # The warehouse
        states = []
        for path in [self.__configurations.references_, self.__configurations.cartography_]:
            states.append(directories.create(path=path))

        return all(states)

    def exc(self) -> bool:
        """

        :return:
        """

        if self.__local() & self.__s3():
            return True

        sys.exit('Error: Set up failure.')
