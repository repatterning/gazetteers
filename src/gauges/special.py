"""Module special.py"""
import io
import json
import sys

import boto3
import requests

import src.functions.secret


class Special:
    """
    Special
    """

    def __init__(self, connector: boto3.session.Session):
        """

        :param connector: A boto3 session instance, it retrieves the developer's <default> Amazon
                          Web Services (AWS) profile details, which allows for programmatic interaction with AWS.
        """

        # Hence
        self.__secret = src.functions.secret.Secret(connector=connector)

        # Headers
        self.__headers = self.__get_headers()

    def __get_headers(self) -> dict:
        """
        This function sets up an ephemeral data retrieval token dict via a client's key.

        :return:
        """

        token_url = 'https://timeseries.sepa.org.uk/KiWebPortal/rest/auth/oidcServer/token'
        access_key = self.__secret.exc(secret_id='HydrographyProject', node='sepa')
        headers =  {'Authorization':'Basic ' + access_key}
        response_token= requests.post(token_url, headers = headers, data = 'grant_type=client_credentials', timeout=600)
        access_token = response_token.json()['access_token']

        return {'Authorization':'Bearer ' + access_token}

    def __get_response(self, url: str) -> requests.Response:
        """

        :param url: A data set's uniform resource locator
        :return:
        """

        try:
            response: requests.Response = requests.get(url=url, headers=self.__headers, timeout=600)
            response.raise_for_status()
        except requests.exceptions.Timeout as err:
            raise err from err
        except Exception as err:
            raise err from err

        if response.status_code == 200:
            return response

        sys.exit(response.status_code)

    def get_json(self, url: str) -> dict | list[dict]:
        """

        :param url: A data set's uniform resource locator
        :return:
        """

        response = self.__get_response(url=url)
        content = response.content.decode(encoding='utf-8')

        return json.loads(content)

    def get_text(self, url: str) -> io.StringIO:
        """

        :param url: A data set's uniform resource locator
        :return:
        """

        response = self.__get_response(url=url)
        buffer = io.StringIO(response.text)

        return buffer
