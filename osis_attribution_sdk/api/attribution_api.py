"""
    Attribution Service

    A set of API endpoints that allow you to get information about attribution  # noqa: E501

    The version of the OpenAPI document: 1.12
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_attribution_sdk.api_client import ApiClient, Endpoint as _Endpoint
from osis_attribution_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from osis_attribution_sdk.model.attribution import Attribution
from osis_attribution_sdk.model.error import Error


class AttributionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __attributions_list(
            self,
            year,
            global_id,
            **kwargs
        ):
            """attributions_list  # noqa: E501

            Return all attributions of specific user in a specific year.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.attributions_list(year, global_id, async_req=True)
            >>> result = thread.get()

            Args:
                year (str):
                global_id (str):

            Keyword Args:
                with_classes (bool): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Attribution]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['year'] = \
                year
            kwargs['global_id'] = \
                global_id
            return self.call_with_http_info(**kwargs)

        self.attributions_list = _Endpoint(
            settings={
                'response_type': ([Attribution],),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/{year}/{global_id}/',
                'operation_id': 'attributions_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'year',
                    'global_id',
                    'with_classes',
                ],
                'required': [
                    'year',
                    'global_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'year':
                        (str,),
                    'global_id':
                        (str,),
                    'with_classes':
                        (bool,),
                },
                'attribute_map': {
                    'year': 'year',
                    'global_id': 'global_id',
                    'with_classes': 'with_classes',
                },
                'location_map': {
                    'year': 'path',
                    'global_id': 'path',
                    'with_classes': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__attributions_list
        )

        def __myattributions_list(
            self,
            year,
            **kwargs
        ):
            """myattributions_list  # noqa: E501

            Return all attributions of connected user in a specific year.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.myattributions_list(year, async_req=True)
            >>> result = thread.get()

            Args:
                year (str):

            Keyword Args:
                with_classes (bool): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Attribution]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['year'] = \
                year
            return self.call_with_http_info(**kwargs)

        self.myattributions_list = _Endpoint(
            settings={
                'response_type': ([Attribution],),
                'auth': [
                    'Token'
                ],
                'endpoint_path': '/{year}/me',
                'operation_id': 'myattributions_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'year',
                    'with_classes',
                ],
                'required': [
                    'year',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'year':
                        (str,),
                    'with_classes':
                        (bool,),
                },
                'attribute_map': {
                    'year': 'year',
                    'with_classes': 'with_classes',
                },
                'location_map': {
                    'year': 'path',
                    'with_classes': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__myattributions_list
        )
