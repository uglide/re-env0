# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.credential_without_value import CredentialWithoutValue

class TestCredentialWithoutValue(unittest.TestCase):
    """CredentialWithoutValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialWithoutValue:
        """Test CredentialWithoutValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CredentialWithoutValue`
        """
        model = CredentialWithoutValue()
        if include_optional:
            return CredentialWithoutValue(
                id = '0',
                name = '',
                organization_id = '',
                value = None,
                encryption_method = '',
                type = 'GCP_SERVICE_ACCOUNT_FOR_DEPLOYMENT',
                created_by_user = env0_client.models.user.User(
                    email = '', 
                    user_id = '', 
                    created_at = '', 
                    app_metadata = env0_client.models.app_metadata.app_metadata(), 
                    picture = '', 
                    name = '', 
                    last_login = '', 
                    given_name = '', 
                    family_name = '', ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CredentialWithoutValue(
                id = '0',
                name = '',
                organization_id = '',
                value = None,
                type = 'GCP_SERVICE_ACCOUNT_FOR_DEPLOYMENT',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCredentialWithoutValue(self):
        """Test CredentialWithoutValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
