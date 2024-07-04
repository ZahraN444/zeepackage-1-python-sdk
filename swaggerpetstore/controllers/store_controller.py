# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from swaggerpetstore.api_helper import APIHelper
from swaggerpetstore.configuration import Server
from swaggerpetstore.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from swaggerpetstore.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from swaggerpetstore.models.order import Order
from swaggerpetstore.exceptions.api_exception import APIException


class StoreController(BaseController):

    """A Controller to access Endpoints in the swaggerpetstore API."""
    def __init__(self, config):
        super(StoreController, self).__init__(config)

    def get_order_by_id(self,
                        order_id):
        """Does a GET request to /store/order/{orderId}.

        For valid response try integer IDs with value >= 1 and <= 10. Other
        values will generated exceptions

        Args:
            order_id (long|int): ID of pet that needs to be fetched

        Returns:
            Order: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/order/{orderId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('orderId')
                            .value(order_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .local_error('400', 'Invalid ID supplied', APIException)
            .local_error('404', 'Order not found', APIException)
        ).execute()

    def place_order(self,
                    body):
        """Does a POST request to /store/order.

        Place an order for a pet

        Args:
            body (StoreOrderRequest): order placed for purchasing the pet

        Returns:
            Order: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/order')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Order.from_dictionary)
            .local_error('400', 'Invalid Order', APIException)
        ).execute()

    def get_inventory(self):
        """Does a GET request to /store/inventory.

        Returns a map of status codes to quantities

        Returns:
            Dict[str, int]: Response from the API. successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/inventory')
            .http_method(HttpMethodEnum.GET)
            .auth(Single('api_key'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def delete_order(self,
                     order_id):
        """Does a DELETE request to /store/order/{orderId}.

        For valid response try integer IDs with positive integer value.
        Negative or non-integer values will generate API errors

        Args:
            order_id (long|int): ID of the order that needs to be deleted

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/store/order/{orderId}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('orderId')
                            .value(order_id)
                            .should_encode(True))
        ).execute()
