# coding: utf-8

"""
    Attribution Service

    A set of API endpoints that allow you to get information about attribution  # noqa: E501

    The version of the OpenAPI document: 1.00
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ApplicationCourseCalendar(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'title': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'authorized_target_year': 'int',
        'is_open': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'authorized_target_year': 'authorized_target_year',
        'is_open': 'is_open'
    }

    def __init__(self, title=None, start_date=None, end_date=None, authorized_target_year=None, is_open=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationCourseCalendar - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._start_date = None
        self._end_date = None
        self._authorized_target_year = None
        self._is_open = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if authorized_target_year is not None:
            self.authorized_target_year = authorized_target_year
        if is_open is not None:
            self.is_open = is_open

    @property
    def title(self):
        """Gets the title of this ApplicationCourseCalendar.  # noqa: E501


        :return: The title of this ApplicationCourseCalendar.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ApplicationCourseCalendar.


        :param title: The title of this ApplicationCourseCalendar.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def start_date(self):
        """Gets the start_date of this ApplicationCourseCalendar.  # noqa: E501


        :return: The start_date of this ApplicationCourseCalendar.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ApplicationCourseCalendar.


        :param start_date: The start_date of this ApplicationCourseCalendar.  # noqa: E501
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ApplicationCourseCalendar.  # noqa: E501


        :return: The end_date of this ApplicationCourseCalendar.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ApplicationCourseCalendar.


        :param end_date: The end_date of this ApplicationCourseCalendar.  # noqa: E501
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def authorized_target_year(self):
        """Gets the authorized_target_year of this ApplicationCourseCalendar.  # noqa: E501


        :return: The authorized_target_year of this ApplicationCourseCalendar.  # noqa: E501
        :rtype: int
        """
        return self._authorized_target_year

    @authorized_target_year.setter
    def authorized_target_year(self, authorized_target_year):
        """Sets the authorized_target_year of this ApplicationCourseCalendar.


        :param authorized_target_year: The authorized_target_year of this ApplicationCourseCalendar.  # noqa: E501
        :type authorized_target_year: int
        """

        self._authorized_target_year = authorized_target_year

    @property
    def is_open(self):
        """Gets the is_open of this ApplicationCourseCalendar.  # noqa: E501


        :return: The is_open of this ApplicationCourseCalendar.  # noqa: E501
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        """Sets the is_open of this ApplicationCourseCalendar.


        :param is_open: The is_open of this ApplicationCourseCalendar.  # noqa: E501
        :type is_open: bool
        """

        self._is_open = is_open

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApplicationCourseCalendar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationCourseCalendar):
            return True

        return self.to_dict() != other.to_dict()
