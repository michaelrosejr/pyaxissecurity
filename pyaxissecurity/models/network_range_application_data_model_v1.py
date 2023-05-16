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


class NetworkRangeApplicationDataModelV1(object):
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
        'dns_searches': 'list[str]',
        'ip_ranges_or_cidrs': 'list[str]',
        'excluded_dns_searches': 'list[str]',
        'ports_and_protocols': 'list[str]',
        'enable_icmp': 'bool',
        'server_initiated_ports': 'list[str]',
        'enforce_resolved_dns_to_ip': 'bool'
    }

    attribute_map = {
        'dns_searches': 'dnsSearches',
        'ip_ranges_or_cidrs': 'ipRangesOrCIDRs',
        'excluded_dns_searches': 'excludedDnsSearches',
        'ports_and_protocols': 'portsAndProtocols',
        'enable_icmp': 'enableIcmp',
        'server_initiated_ports': 'serverInitiatedPorts',
        'enforce_resolved_dns_to_ip': 'enforceResolvedDnsToIp'
    }

    def __init__(self, dns_searches=None, ip_ranges_or_cidrs=None, excluded_dns_searches=None, ports_and_protocols=None, enable_icmp=True, server_initiated_ports=None, enforce_resolved_dns_to_ip=False, _configuration=None):  # noqa: E501
        """NetworkRangeApplicationDataModelV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dns_searches = None
        self._ip_ranges_or_cidrs = None
        self._excluded_dns_searches = None
        self._ports_and_protocols = None
        self._enable_icmp = None
        self._server_initiated_ports = None
        self._enforce_resolved_dns_to_ip = None
        self.discriminator = None

        if dns_searches is not None:
            self.dns_searches = dns_searches
        if ip_ranges_or_cidrs is not None:
            self.ip_ranges_or_cidrs = ip_ranges_or_cidrs
        if excluded_dns_searches is not None:
            self.excluded_dns_searches = excluded_dns_searches
        if ports_and_protocols is not None:
            self.ports_and_protocols = ports_and_protocols
        self.enable_icmp = enable_icmp
        if server_initiated_ports is not None:
            self.server_initiated_ports = server_initiated_ports
        self.enforce_resolved_dns_to_ip = enforce_resolved_dns_to_ip

    @property
    def dns_searches(self):
        """Gets the dns_searches of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The dns_searches of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_searches

    @dns_searches.setter
    def dns_searches(self, dns_searches):
        """Sets the dns_searches of this NetworkRangeApplicationDataModelV1.


        :param dns_searches: The dns_searches of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: list[str]
        """

        self._dns_searches = dns_searches

    @property
    def ip_ranges_or_cidrs(self):
        """Gets the ip_ranges_or_cidrs of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The ip_ranges_or_cidrs of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_ranges_or_cidrs

    @ip_ranges_or_cidrs.setter
    def ip_ranges_or_cidrs(self, ip_ranges_or_cidrs):
        """Sets the ip_ranges_or_cidrs of this NetworkRangeApplicationDataModelV1.


        :param ip_ranges_or_cidrs: The ip_ranges_or_cidrs of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: list[str]
        """

        self._ip_ranges_or_cidrs = ip_ranges_or_cidrs

    @property
    def excluded_dns_searches(self):
        """Gets the excluded_dns_searches of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The excluded_dns_searches of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._excluded_dns_searches

    @excluded_dns_searches.setter
    def excluded_dns_searches(self, excluded_dns_searches):
        """Sets the excluded_dns_searches of this NetworkRangeApplicationDataModelV1.


        :param excluded_dns_searches: The excluded_dns_searches of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: list[str]
        """

        self._excluded_dns_searches = excluded_dns_searches

    @property
    def ports_and_protocols(self):
        """Gets the ports_and_protocols of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The ports_and_protocols of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._ports_and_protocols

    @ports_and_protocols.setter
    def ports_and_protocols(self, ports_and_protocols):
        """Sets the ports_and_protocols of this NetworkRangeApplicationDataModelV1.


        :param ports_and_protocols: The ports_and_protocols of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: list[str]
        """

        self._ports_and_protocols = ports_and_protocols

    @property
    def enable_icmp(self):
        """Gets the enable_icmp of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The enable_icmp of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: bool
        """
        return self._enable_icmp

    @enable_icmp.setter
    def enable_icmp(self, enable_icmp):
        """Sets the enable_icmp of this NetworkRangeApplicationDataModelV1.


        :param enable_icmp: The enable_icmp of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enable_icmp is None:
            raise ValueError("Invalid value for `enable_icmp`, must not be `None`")  # noqa: E501

        self._enable_icmp = enable_icmp

    @property
    def server_initiated_ports(self):
        """Gets the server_initiated_ports of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The server_initiated_ports of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_initiated_ports

    @server_initiated_ports.setter
    def server_initiated_ports(self, server_initiated_ports):
        """Sets the server_initiated_ports of this NetworkRangeApplicationDataModelV1.


        :param server_initiated_ports: The server_initiated_ports of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: list[str]
        """

        self._server_initiated_ports = server_initiated_ports

    @property
    def enforce_resolved_dns_to_ip(self):
        """Gets the enforce_resolved_dns_to_ip of this NetworkRangeApplicationDataModelV1.  # noqa: E501


        :return: The enforce_resolved_dns_to_ip of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_resolved_dns_to_ip

    @enforce_resolved_dns_to_ip.setter
    def enforce_resolved_dns_to_ip(self, enforce_resolved_dns_to_ip):
        """Sets the enforce_resolved_dns_to_ip of this NetworkRangeApplicationDataModelV1.


        :param enforce_resolved_dns_to_ip: The enforce_resolved_dns_to_ip of this NetworkRangeApplicationDataModelV1.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enforce_resolved_dns_to_ip is None:
            raise ValueError("Invalid value for `enforce_resolved_dns_to_ip`, must not be `None`")  # noqa: E501

        self._enforce_resolved_dns_to_ip = enforce_resolved_dns_to_ip

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
        if issubclass(NetworkRangeApplicationDataModelV1, dict):
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
        if not isinstance(other, NetworkRangeApplicationDataModelV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkRangeApplicationDataModelV1):
            return True

        return self.to_dict() != other.to_dict()