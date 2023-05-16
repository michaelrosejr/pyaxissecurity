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
from pyaxissecurity.api.users_api import UsersApi  # noqa: E501
from pyaxissecurity.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = pyaxissecurity.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_create(self):
        """Test case for users_create

        Create a New User  # noqa: E501
        """
        pass

    def test_users_delete(self):
        """Test case for users_delete

        Delete User by ID  # noqa: E501
        """
        pass

    def test_users_get_by_id(self):
        """Test case for users_get_by_id

        Get User by ID  # noqa: E501
        """
        pass

    def test_users_query(self):
        """Test case for users_query

        Get Users  # noqa: E501
        """
        pass

    def test_users_update(self):
        """Test case for users_update

        Update an Existing User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
