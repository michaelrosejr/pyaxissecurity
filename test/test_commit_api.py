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
from pyaxissecurity.api.commit_api import CommitApi  # noqa: E501
from pyaxissecurity.rest import ApiException


class TestCommitApi(unittest.TestCase):
    """CommitApi unit test stubs"""

    def setUp(self):
        self.api = pyaxissecurity.api.commit_api.CommitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_commit_commit_changes(self):
        """Test case for commit_commit_changes

        Commit Changes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
