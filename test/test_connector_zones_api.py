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
from pyaxissecurity.api.connector_zones_api import ConnectorZonesApi  # noqa: E501
from pyaxissecurity.rest import ApiException


class TestConnectorZonesApi(unittest.TestCase):
    """ConnectorZonesApi unit test stubs"""

    def setUp(self):
        self.api = pyaxissecurity.api.connector_zones_api.ConnectorZonesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_connector_zones_create(self):
        """Test case for connector_zones_create

        Create a New Connector Zone  # noqa: E501
        """
        pass

    def test_connector_zones_delete(self):
        """Test case for connector_zones_delete

        Delete Connector Zone by ID  # noqa: E501
        """
        pass

    def test_connector_zones_get_by_id(self):
        """Test case for connector_zones_get_by_id

        Get Connector Zone by ID  # noqa: E501
        """
        pass

    def test_connector_zones_query(self):
        """Test case for connector_zones_query

        Get Connector Zones  # noqa: E501
        """
        pass

    def test_connector_zones_update(self):
        """Test case for connector_zones_update

        Update an Existing Connector Zone  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()