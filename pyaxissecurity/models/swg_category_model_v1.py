# coding: utf-8

"""
    PublicAdminApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pyaxissecurity.configuration import Configuration


class SwgCategoryModelV1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'included_domains_or_urls': 'list[str]',
        'excluded_domains_or_urls': 'list[str]',
        'connector_zone_id': 'str',
        'type': 'SwgCategoryType'
    }

    attribute_map = {
        'included_domains_or_urls': 'includedDomainsOrUrls',
        'excluded_domains_or_urls': 'excludedDomainsOrUrls',
        'connector_zone_id': 'connectorZoneId',
        'type': 'type'
    }

    def __init__(self, included_domains_or_urls=None, excluded_domains_or_urls=None, connector_zone_id=None, type=None, _configuration=None):  # noqa: E501
        """SwgCategoryModelV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._included_domains_or_urls = None
        self._excluded_domains_or_urls = None
        self._connector_zone_id = None
        self._type = None
        self.discriminator = None

        if included_domains_or_urls is not None:
            self.included_domains_or_urls = included_domains_or_urls
        if excluded_domains_or_urls is not None:
            self.excluded_domains_or_urls = excluded_domains_or_urls
        if connector_zone_id is not None:
            self.connector_zone_id = connector_zone_id
        self.type = type

    @property
    def included_domains_or_urls(self):
        """Gets the included_domains_or_urls of this SwgCategoryModelV1.  # noqa: E501


        :return: The included_domains_or_urls of this SwgCategoryModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._included_domains_or_urls

    @included_domains_or_urls.setter
    def included_domains_or_urls(self, included_domains_or_urls):
        """Sets the included_domains_or_urls of this SwgCategoryModelV1.


        :param included_domains_or_urls: The included_domains_or_urls of this SwgCategoryModelV1.  # noqa: E501
        :type: list[str]
        """

        self._included_domains_or_urls = included_domains_or_urls

    @property
    def excluded_domains_or_urls(self):
        """Gets the excluded_domains_or_urls of this SwgCategoryModelV1.  # noqa: E501


        :return: The excluded_domains_or_urls of this SwgCategoryModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_domains_or_urls

    @excluded_domains_or_urls.setter
    def excluded_domains_or_urls(self, excluded_domains_or_urls):
        """Sets the excluded_domains_or_urls of this SwgCategoryModelV1.


        :param excluded_domains_or_urls: The excluded_domains_or_urls of this SwgCategoryModelV1.  # noqa: E501
        :type: list[str]
        """

        self._excluded_domains_or_urls = excluded_domains_or_urls

    @property
    def connector_zone_id(self):
        """Gets the connector_zone_id of this SwgCategoryModelV1.  # noqa: E501


        :return: The connector_zone_id of this SwgCategoryModelV1.  # noqa: E501
        :rtype: str
        """
        return self._connector_zone_id

    @connector_zone_id.setter
    def connector_zone_id(self, connector_zone_id):
        """Sets the connector_zone_id of this SwgCategoryModelV1.


        :param connector_zone_id: The connector_zone_id of this SwgCategoryModelV1.  # noqa: E501
        :type: str
        """

        self._connector_zone_id = connector_zone_id

    @property
    def type(self):
        """Gets the type of this SwgCategoryModelV1.  # noqa: E501


        :return: The type of this SwgCategoryModelV1.  # noqa: E501
        :rtype: SwgCategoryType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SwgCategoryModelV1.


        :param type: The type of this SwgCategoryModelV1.  # noqa: E501
        :type: SwgCategoryType
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SwgCategoryModelV1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SwgCategoryModelV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SwgCategoryModelV1):
            return True

        return self.to_dict() != other.to_dict()