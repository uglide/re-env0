# coding: utf-8

"""
    env0 API

    This document describes the resources that make up the official env0 REST API  ### BaseURL https://api.env0.com/  ### Content Types All requests should be in JSON format, and include the `accept: application/json` header 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class EnvironmentApiUpdatePoliciesRequestBody(BaseModel):
    """
    EnvironmentApiUpdatePoliciesRequestBody
    """ # noqa: E501
    project_id: StrictStr = Field(alias="projectId")
    number_of_environments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="numberOfEnvironments")
    number_of_environments_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="numberOfEnvironmentsTotal")
    max_ttl: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The maximum allowed TTL. Must be 6-h, 12-h, 1-d, 3-d, 1-w, 2-w, 1-M, inherit or explicit null which means infinite", alias="maxTtl")
    default_ttl: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The default TTL set when creating environments. Must be 6-h, 12-h, 1-d, 3-d, 1-w, 2-w, 1-M, inherit or explicit null which means infinite", alias="defaultTtl")
    requires_approval_default: Optional[StrictBool] = Field(default=None, alias="requiresApprovalDefault")
    include_cost_estimation: Optional[StrictBool] = Field(default=None, alias="includeCostEstimation")
    skip_apply_when_plan_is_empty: Optional[StrictBool] = Field(default=None, alias="skipApplyWhenPlanIsEmpty")
    disable_destroy_environments: Optional[StrictBool] = Field(default=None, alias="disableDestroyEnvironments")
    skip_redundant_deployments: Optional[StrictBool] = Field(default=None, alias="skipRedundantDeployments")
    run_pull_request_plan_default: Optional[StrictBool] = Field(default=None, alias="runPullRequestPlanDefault")
    continuous_deployment_default: Optional[StrictBool] = Field(default=None, alias="continuousDeploymentDefault")
    force_remote_backend: Optional[StrictBool] = Field(default=None, alias="forceRemoteBackend")
    drift_detection_enabled: Optional[StrictBool] = Field(default=None, alias="driftDetectionEnabled")
    drift_detection_cron: Optional[StrictStr] = Field(default=None, alias="driftDetectionCron")
    outputs_as_inputs_enabled: Optional[StrictBool] = Field(default=None, alias="outputsAsInputsEnabled")
    __properties: ClassVar[List[str]] = ["projectId", "numberOfEnvironments", "numberOfEnvironmentsTotal", "maxTtl", "defaultTtl", "requiresApprovalDefault", "includeCostEstimation", "skipApplyWhenPlanIsEmpty", "disableDestroyEnvironments", "skipRedundantDeployments", "runPullRequestPlanDefault", "continuousDeploymentDefault", "forceRemoteBackend", "driftDetectionEnabled", "driftDetectionCron", "outputsAsInputsEnabled"]

    @field_validator('max_ttl')
    def max_ttl_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+-[h|d|w|M]|inherit", value):
            raise ValueError(r"must validate the regular expression /^\d+-[h|d|w|M]|inherit/")
        return value

    @field_validator('default_ttl')
    def default_ttl_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+-[h|d|w|M]|inherit", value):
            raise ValueError(r"must validate the regular expression /^\d+-[h|d|w|M]|inherit/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EnvironmentApiUpdatePoliciesRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if number_of_environments (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_environments is None and "number_of_environments" in self.model_fields_set:
            _dict['numberOfEnvironments'] = None

        # set to None if number_of_environments_total (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_environments_total is None and "number_of_environments_total" in self.model_fields_set:
            _dict['numberOfEnvironmentsTotal'] = None

        # set to None if max_ttl (nullable) is None
        # and model_fields_set contains the field
        if self.max_ttl is None and "max_ttl" in self.model_fields_set:
            _dict['maxTtl'] = None

        # set to None if default_ttl (nullable) is None
        # and model_fields_set contains the field
        if self.default_ttl is None and "default_ttl" in self.model_fields_set:
            _dict['defaultTtl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnvironmentApiUpdatePoliciesRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projectId": obj.get("projectId"),
            "numberOfEnvironments": obj.get("numberOfEnvironments"),
            "numberOfEnvironmentsTotal": obj.get("numberOfEnvironmentsTotal"),
            "maxTtl": obj.get("maxTtl"),
            "defaultTtl": obj.get("defaultTtl"),
            "requiresApprovalDefault": obj.get("requiresApprovalDefault"),
            "includeCostEstimation": obj.get("includeCostEstimation"),
            "skipApplyWhenPlanIsEmpty": obj.get("skipApplyWhenPlanIsEmpty"),
            "disableDestroyEnvironments": obj.get("disableDestroyEnvironments"),
            "skipRedundantDeployments": obj.get("skipRedundantDeployments"),
            "runPullRequestPlanDefault": obj.get("runPullRequestPlanDefault"),
            "continuousDeploymentDefault": obj.get("continuousDeploymentDefault"),
            "forceRemoteBackend": obj.get("forceRemoteBackend"),
            "driftDetectionEnabled": obj.get("driftDetectionEnabled"),
            "driftDetectionCron": obj.get("driftDetectionCron"),
            "outputsAsInputsEnabled": obj.get("outputsAsInputsEnabled")
        })
        return _obj

