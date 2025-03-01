# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import unittest
from tests.http_response_catcher import HttpResponseCatcher
from swaggerpetstore.configuration import Configuration
from swaggerpetstore.swaggerpetstore_client import SwaggerpetstoreClient
from swaggerpetstore.http.auth.http_basic import HttpBasicCredentials


class ControllerTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    client = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = ControllerTestBase.create_configuration()
        cls.client = SwaggerpetstoreClient(config=cls.config)

        petstore_auth_token = cls.client.petstore_auth.fetch_token()
        petstore_auth_credentials = cls.config.petstore_auth_credentials\
            .clone_with(o_auth_token=petstore_auth_token)
        cls.config = cls.config.clone_with(petstore_auth_credentials=petstore_auth_credentials)

        cls.client = SwaggerpetstoreClient(config=cls.config)

    @staticmethod
    def create_configuration():
        return Configuration(
            http_basic_credentials=HttpBasicCredentials(username='test',
                                                        passwprd='testPassword'),
            http_call_back=HttpResponseCatcher())
