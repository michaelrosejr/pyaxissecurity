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


class PagedApiResponseOfIEnumerableOfSwgCategoryModelV1(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'first_page': 'str',
        'last_page': 'str',
        'total_pages': 'int',
        'total_records': 'int',
        'next_page': 'str',
        'previous_page': 'str',
        'data': 'list[SwgCategoryModelV1]'
    }

    attribute_map = {
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'first_page': 'firstPage',
        'last_page': 'lastPage',
        'total_pages': 'totalPages',
        'total_records': 'totalRecords',
        'next_page': 'nextPage',
        'previous_page': 'previousPage',
        'data': 'data'
    }

    def __init__(self, page_number=None, page_size=None, first_page=None, last_page=None, total_pages=None, total_records=None, next_page=None, previous_page=None, data=None, _configuration=None):  # noqa: E501
        """PagedApiResponseOfIEnumerableOfSwgCategoryModelV1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._first_page = None
        self._last_page = None
        self._total_pages = None
        self._total_records = None
        self._next_page = None
        self._previous_page = None
        self._data = None
        self.discriminator = None

        self.page_number = page_number
        self.page_size = page_size
        if first_page is not None:
            self.first_page = first_page
        if last_page is not None:
            self.last_page = last_page
        self.total_pages = total_pages
        self.total_records = total_records
        if next_page is not None:
            self.next_page = next_page
        if previous_page is not None:
            self.previous_page = previous_page
        if data is not None:
            self.data = data

    @property
    def page_number(self):
        """Gets the page_number of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The page_number of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param page_number: The page_number of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The page_size of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param page_size: The page_size of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

    @property
    def first_page(self):
        """Gets the first_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The first_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: str
        """
        return self._first_page

    @first_page.setter
    def first_page(self, first_page):
        """Sets the first_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param first_page: The first_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: str
        """

        self._first_page = first_page

    @property
    def last_page(self):
        """Gets the last_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The last_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: str
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param last_page: The last_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: str
        """

        self._last_page = last_page

    @property
    def total_pages(self):
        """Gets the total_pages of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The total_pages of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param total_pages: The total_pages of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_pages is None:
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def total_records(self):
        """Gets the total_records of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The total_records of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param total_records: The total_records of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_records is None:
            raise ValueError("Invalid value for `total_records`, must not be `None`")  # noqa: E501

        self._total_records = total_records

    @property
    def next_page(self):
        """Gets the next_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The next_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param next_page: The next_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def previous_page(self):
        """Gets the previous_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The previous_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page):
        """Sets the previous_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param previous_page: The previous_page of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: str
        """

        self._previous_page = previous_page

    @property
    def data(self):
        """Gets the data of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501


        :return: The data of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :rtype: list[SwgCategoryModelV1]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.


        :param data: The data of this PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.  # noqa: E501
        :type: list[SwgCategoryModelV1]
        """

        self._data = data

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
        if issubclass(PagedApiResponseOfIEnumerableOfSwgCategoryModelV1, dict):
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
        if not isinstance(other, PagedApiResponseOfIEnumerableOfSwgCategoryModelV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagedApiResponseOfIEnumerableOfSwgCategoryModelV1):
            return True

        return self.to_dict() != other.to_dict()
