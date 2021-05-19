# coding: utf-8

# flake8: noqa

"""
    Attribution Service

    A set of API endpoints that allow you to get information about attribution  # noqa: E501

    The version of the OpenAPI document: 1.00
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.application_api import ApplicationApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.application_course_calendar import ApplicationCourseCalendar
from openapi_client.models.error import Error
