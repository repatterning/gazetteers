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
    state = src.data.interface.Interface(attributes=attributes).exc()
    if state:
        src.transfer.interface.Interface(service=service, s3_parameters=s3_parameters).exc()
    else:
        logger.info('Beware, reacquire is false and excerpt is null, therefore no data acquisition activity.')

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
    import src.data.interface
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
    attributes: dict
    connector, s3_parameters, service, attributes = src.preface.interface.Interface().exc()

    main()
