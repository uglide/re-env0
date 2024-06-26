# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.deployment_api_plan_plan_resource_change import DeploymentApiPlanPlanResourceChange

class TestDeploymentApiPlanPlanResourceChange(unittest.TestCase):
    """DeploymentApiPlanPlanResourceChange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentApiPlanPlanResourceChange:
        """Test DeploymentApiPlanPlanResourceChange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentApiPlanPlanResourceChange`
        """
        model = DeploymentApiPlanPlanResourceChange()
        if include_optional:
            return DeploymentApiPlanPlanResourceChange(
                name = '',
                provider_name = '',
                type = '',
                path = '',
                action = 'create',
                attributes = [
                    env0_client.models.deployment_api/plan/attribute_change.DeploymentApi.Plan.AttributeChange(
                        name = '', 
                        before = null, 
                        after = null, )
                    ],
                importing = env0_client.models.deployment_api/plan/resource_import_data.DeploymentApi.Plan.ResourceImportData(
                    id = '', ),
                previous_address = ''
            )
        else:
            return DeploymentApiPlanPlanResourceChange(
                name = '',
                provider_name = '',
                type = '',
                path = '',
                action = 'create',
                attributes = [
                    env0_client.models.deployment_api/plan/attribute_change.DeploymentApi.Plan.AttributeChange(
                        name = '', 
                        before = null, 
                        after = null, )
                    ],
        )
        """

    def testDeploymentApiPlanPlanResourceChange(self):
        """Test DeploymentApiPlanPlanResourceChange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
