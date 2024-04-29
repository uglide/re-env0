# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.infracost_total_output_projects_inner import InfracostTotalOutputProjectsInner

class TestInfracostTotalOutputProjectsInner(unittest.TestCase):
    """InfracostTotalOutputProjectsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InfracostTotalOutputProjectsInner:
        """Test InfracostTotalOutputProjectsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InfracostTotalOutputProjectsInner`
        """
        model = InfracostTotalOutputProjectsInner()
        if include_optional:
            return InfracostTotalOutputProjectsInner(
                path = '',
                metadata = None,
                past_breakdown = env0_client.models.infracost/output.Infracost.Output(
                    resources = [
                        null
                        ], 
                    total_hourly_cost = '', 
                    total_monthly_cost = '', ),
                breakdown = env0_client.models.infracost/output.Infracost.Output(
                    resources = [
                        null
                        ], 
                    total_hourly_cost = '', 
                    total_monthly_cost = '', ),
                diff = env0_client.models.infracost/output.Infracost.Output(
                    resources = [
                        null
                        ], 
                    total_hourly_cost = '', 
                    total_monthly_cost = '', )
            )
        else:
            return InfracostTotalOutputProjectsInner(
        )
        """

    def testInfracostTotalOutputProjectsInner(self):
        """Test InfracostTotalOutputProjectsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()