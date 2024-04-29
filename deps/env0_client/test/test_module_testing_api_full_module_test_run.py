# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from env0_client.models.module_testing_api_full_module_test_run import ModuleTestingApiFullModuleTestRun

class TestModuleTestingApiFullModuleTestRun(unittest.TestCase):
    """ModuleTestingApiFullModuleTestRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModuleTestingApiFullModuleTestRun:
        """Test ModuleTestingApiFullModuleTestRun
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModuleTestingApiFullModuleTestRun`
        """
        model = ModuleTestingApiFullModuleTestRun()
        if include_optional:
            return ModuleTestingApiFullModuleTestRun(
                status = 'QUEUED',
                blueprint_revision = '',
                pr_number = '',
                started_by = '',
                started_by_user = env0_client.models.user.User(
                    email = '', 
                    user_id = '', 
                    created_at = '', 
                    app_metadata = env0_client.models.app_metadata.app_metadata(), 
                    picture = '', 
                    name = '', 
                    last_login = '', 
                    given_name = '', 
                    family_name = '', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                queued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                error = None,
                custom_env0_environment_variables = env0_client.models.custom_env0_environment_variables.CustomEnv0EnvironmentVariables(
                    environment_id = '', 
                    project_id = '', 
                    project_name = '', 
                    deployment_log_id = '', 
                    deployment_type = 'prPlan', 
                    deployment_revision = '', 
                    workspace_name = '', 
                    root_dir = '', 
                    organization_id = '', 
                    template_id = '', 
                    template_dir = '', 
                    template_name = '', 
                    environment_name = '', 
                    environment_creator_name = '', 
                    environment_creator_email = '', 
                    deployer_name = '', 
                    deployer_email = '', 
                    reviewer_name = '', 
                    reviewer_email = '', 
                    pr_author = '', 
                    pr_source_branch = '', 
                    pr_target_branch = '', 
                    commit_hash = '', 
                    commit_url = '', 
                    oidc_token = '', 
                    vcs_access_token = '', 
                    tf_plan_json = '', 
                    cli_args_plan = '', 
                    cli_args_apply = '', ),
                git_avatar_url = '',
                git_user = '',
                blueprint_repository = '',
                id = '',
                deployment_log_id = '',
                environment_id = '',
                organization_id = '',
                trigger_name = 'scheduled',
                test_summary = env0_client.models.module_testing_api/test_file_summary.ModuleTestingApi.TestFileSummary(
                    passed = 1.337, 
                    failed = 1.337, 
                    skipped = 1.337, 
                    errored = 1.337, ),
                test_files_results = {
                    'key' : env0_client.models.module_testing_api/test_file_result.ModuleTestingApi.TestFileResult(
                        test_file = '', 
                        summary = env0_client.models.module_testing_api/test_file_summary.ModuleTestingApi.TestFileSummary(
                            passed = 1.337, 
                            failed = 1.337, 
                            skipped = 1.337, 
                            errored = 1.337, ), 
                        tests = [
                            env0_client.models.module_testing_api/test_result.ModuleTestingApi.TestResult(
                                name = '', 
                                status = 'skipped', )
                            ], )
                    },
                module_id = ''
            )
        else:
            return ModuleTestingApiFullModuleTestRun(
                deployment_log_id = '',
                environment_id = '',
                organization_id = '',
        )
        """

    def testModuleTestingApiFullModuleTestRun(self):
        """Test ModuleTestingApiFullModuleTestRun"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()