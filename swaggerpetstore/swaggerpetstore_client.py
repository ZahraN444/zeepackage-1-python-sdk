# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from swaggerpetstore.configuration import Configuration
from swaggerpetstore.controllers.base_controller import BaseController
from swaggerpetstore.configuration import Environment
from swaggerpetstore.http.auth.api_key import ApiKey
from swaggerpetstore.http.auth.http_basic import HttpBasic
from swaggerpetstore.http.auth.petstore_auth import PetstoreAuth
from swaggerpetstore.controllers.pet_controller import PetController
from swaggerpetstore.controllers.store_controller import StoreController
from swaggerpetstore.controllers.user_controller import UserController


class SwaggerpetstoreClient(object):
    @LazyProperty
    def pet(self):
        return PetController(self.global_configuration)

    @LazyProperty
    def store(self):
        return StoreController(self.global_configuration)

    @LazyProperty
    def user(self):
        return UserController(self.global_configuration)

    @property
    def petstore_auth(self):
        return self.auth_managers['petstore_auth']

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, api_key_credentials=None,
                 http_basic_credentials=None, petstore_auth_credentials=None,
                 test_header='TestHeaderDefaultValue', config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, api_key_credentials=api_key_credentials,
            http_basic_credentials=http_basic_credentials,
            petstore_auth_credentials=petstore_auth_credentials,
            test_header=test_header)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())\
            .global_header('TestHeader', self.config.test_header)

        self.auth_managers = {key: None for key in ['api_key', 'httpBasic',
                                                    'petstore_auth']}
        self.auth_managers['api_key'] = ApiKey(self.config.api_key_credentials)
        self.auth_managers['httpBasic'] = HttpBasic(
            self.config.http_basic_credentials)
        self.auth_managers['petstore_auth'] = PetstoreAuth(
            self.config.petstore_auth_credentials, self.global_configuration)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

