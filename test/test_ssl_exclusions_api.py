# coding: utf-8

"""
    PublicAdminApi

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pyaxissecurity
from pyaxissecurity.api.ssl_exclusions_api import SslExclusionsApi  # noqa: E501
from pyaxissecurity.rest import ApiException


class TestSslExclusionsApi(unittest.TestCase):
    """SslExclusionsApi unit test stubs"""

    def setUp(self):
        self.api = pyaxissecurity.api.ssl_exclusions_api.SslExclusionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ssl_exclusions_create(self):
        """Test case for ssl_exclusions_create

        Create a New SSL Exclusion  # noqa: E501
        """
        pass

    def test_ssl_exclusions_delete(self):
        """Test case for ssl_exclusions_delete

        Delete SSL Exclusion by ID  # noqa: E501
        """
        pass

    def test_ssl_exclusions_get_by_id(self):
        """Test case for ssl_exclusions_get_by_id

        Get SSL Exclusion by ID  # noqa: E501
        """
        pass

    def test_ssl_exclusions_query(self):
        """Test case for ssl_exclusions_query

        Get SSL Exclusions  # noqa: E501
        """
        pass

    def test_ssl_exclusions_update(self):
        """Test case for ssl_exclusions_update

        Update an Existing SSL Exclusion  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()