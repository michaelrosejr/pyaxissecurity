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


class UserModelV1(object):
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
        'user_name': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'enabled': 'bool',
        'expiration': 'datetime',
        'groups': 'list[SlimModelV1]',
        'ssh_private_key': 'str',
        'has_ssh_private_key': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'user_name': 'userName',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'enabled': 'enabled',
        'expiration': 'expiration',
        'groups': 'groups',
        'ssh_private_key': 'sshPrivateKey',
        'has_ssh_private_key': 'hasSshPrivateKey',
        'id': 'id'
    }

    def __init__(self, user_name=None, email=None, first_name=None, last_name=None, enabled=True, expiration=None, groups=None, ssh_private_key=None, has_ssh_private_key=None, _configuration=None, id=None):  # noqa: E501
        """UserModelV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_name = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._enabled = None
        self._expiration = None
        self._groups = None
        self._ssh_private_key = None
        self._has_ssh_private_key = None
        self.discriminator = None

        self.user_name = user_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.enabled = enabled
        self.id = id
        if expiration is not None:
            self.expiration = expiration
        if groups is not None:
            self.groups = groups
        if ssh_private_key is not None:
            self.ssh_private_key = ssh_private_key
        if has_ssh_private_key is not None:
            self.has_ssh_private_key = has_ssh_private_key

    @property
    def user_name(self):
        """Gets the user_name of this UserModelV1.  # noqa: E501


        :return: The user_name of this UserModelV1.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserModelV1.


        :param user_name: The user_name of this UserModelV1.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user_name is not None and len(user_name) < 3):
            raise ValueError("Invalid value for `user_name`, length must be greater than or equal to `3`")  # noqa: E501

        self._user_name = user_name

    @property
    def email(self):
        """Gets the email of this UserModelV1.  # noqa: E501


        :return: The email of this UserModelV1.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserModelV1.


        :param email: The email of this UserModelV1.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                email is not None and len(email) < 1):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this UserModelV1.  # noqa: E501


        :return: The first_name of this UserModelV1.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserModelV1.


        :param first_name: The first_name of this UserModelV1.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                first_name is not None and len(first_name) < 1):
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserModelV1.  # noqa: E501


        :return: The last_name of this UserModelV1.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserModelV1.


        :param last_name: The last_name of this UserModelV1.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                last_name is not None and len(last_name) < 1):
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_name = last_name

    @property
    def enabled(self):
        """Gets the enabled of this UserModelV1.  # noqa: E501


        :return: The enabled of this UserModelV1.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserModelV1.


        :param enabled: The enabled of this UserModelV1.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def expiration(self):
        """Gets the expiration of this UserModelV1.  # noqa: E501


        :return: The expiration of this UserModelV1.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this UserModelV1.


        :param expiration: The expiration of this UserModelV1.  # noqa: E501
        :type: datetime
        """

        self._expiration = expiration

    @property
    def groups(self):
        """Gets the groups of this UserModelV1.  # noqa: E501


        :return: The groups of this UserModelV1.  # noqa: E501
        :rtype: list[SlimModelV1]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserModelV1.


        :param groups: The groups of this UserModelV1.  # noqa: E501
        :type: list[SlimModelV1]
        """

        self._groups = groups

    @property
    def ssh_private_key(self):
        """Gets the ssh_private_key of this UserModelV1.  # noqa: E501


        :return: The ssh_private_key of this UserModelV1.  # noqa: E501
        :rtype: str
        """
        return self._ssh_private_key

    @ssh_private_key.setter
    def ssh_private_key(self, ssh_private_key):
        """Sets the ssh_private_key of this UserModelV1.


        :param ssh_private_key: The ssh_private_key of this UserModelV1.  # noqa: E501
        :type: str
        """

        self._ssh_private_key = ssh_private_key

    @property
    def has_ssh_private_key(self):
        """Gets the has_ssh_private_key of this UserModelV1.  # noqa: E501


        :return: The has_ssh_private_key of this UserModelV1.  # noqa: E501
        :rtype: bool
        """
        return self._has_ssh_private_key

    @has_ssh_private_key.setter
    def has_ssh_private_key(self, has_ssh_private_key):
        """Sets the has_ssh_private_key of this UserModelV1.


        :param has_ssh_private_key: The has_ssh_private_key of this UserModelV1.  # noqa: E501
        :type: bool
        """

        self._has_ssh_private_key = has_ssh_private_key

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
        if issubclass(UserModelV1, dict):
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
        if not isinstance(other, UserModelV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserModelV1):
            return True

        return self.to_dict() != other.to_dict()
