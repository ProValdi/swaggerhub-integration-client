# coding: utf-8

"""
    Swagger Balancer

    This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.summ_api import SummApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSummApi(unittest.TestCase):
    """SummApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.summ_api.SummApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_do_action(self):
        """Test case for do_action

        operate 2 numbers  # noqa: E501
        """
        pass

    def test_get_results(self):
        """Test case for get_results

        Get previous results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
