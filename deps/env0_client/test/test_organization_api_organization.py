# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.organization_api_organization import OrganizationApiOrganization

class TestOrganizationApiOrganization(unittest.TestCase):
    """OrganizationApiOrganization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationApiOrganization:
        """Test OrganizationApiOrganization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationApiOrganization`
        """
        model = OrganizationApiOrganization()
        if include_optional:
            return OrganizationApiOrganization(
                id = '',
                name = '',
                max_ttl = '',
                default_ttl = '',
                do_not_report_skipped_status_checks = True,
                do_not_consider_merge_commits_for_pr_plans = True,
                enable_oidc = True,
                description = '',
                photo_url = '',
                created_by = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                mode = 'free',
                trial_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                enforce_pr_commenter_permissions = True,
                project_custom_flows_policy = 'MERGE_WITH_TEMPLATES',
                role = '',
                is_self_hosted_k8s = True
            )
        else:
            return OrganizationApiOrganization(
                id = '',
                name = '',
                created_by = '',
                mode = 'free',
                project_custom_flows_policy = 'MERGE_WITH_TEMPLATES',
                role = '',
        )
        """

    def testOrganizationApiOrganization(self):
        """Test OrganizationApiOrganization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()