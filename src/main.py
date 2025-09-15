"""Module main.py"""
import logging
import os
import sys

import boto3


def main():
    """
    Entry point
    """

    # Logging
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info(__name__)

    # Steps
    src.gauges.interface.Interface().exc()
    src.care.interface.Interface(connector=connector, arguments=arguments).exc()

    # Transfer
    # src.transfer.interface.Interface(service=service, s3_parameters=s3_parameters).exc()

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Setting-up
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import src.care.interface
    import src.gauges.interface
    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.functions.service
    import src.s3.s3_parameters
    import src.preface.setup
    import src.transfer.interface
    import src.preface.interface

    connector: boto3.session.Session
    s3_parameters: s3p.S3Parameters
    service: sr.Service
    arguments: dict
    connector, s3_parameters, service, arguments = src.preface.interface.Interface().exc()

    main()
