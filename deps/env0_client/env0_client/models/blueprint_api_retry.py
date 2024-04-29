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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from env0_client.models.blueprint_api_retry_on_destroy import BlueprintApiRetryOnDestroy
from typing import Optional, Set
from typing_extensions import Self

class BlueprintApiRetry(BaseModel):
    """
    BlueprintApiRetry
    """ # noqa: E501
    on_destroy: Optional[BlueprintApiRetryOnDestroy] = Field(default=None, alias="onDestroy")
    on_deploy: Optional[BlueprintApiRetryOnDestroy] = Field(default=None, alias="onDeploy")
    __properties: ClassVar[List[str]] = ["onDestroy", "onDeploy"]

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
        """Create an instance of BlueprintApiRetry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of on_destroy
        if self.on_destroy:
            _dict['onDestroy'] = self.on_destroy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of on_deploy
        if self.on_deploy:
            _dict['onDeploy'] = self.on_deploy.to_dict()
        # set to None if on_destroy (nullable) is None
        # and model_fields_set contains the field
        if self.on_destroy is None and "on_destroy" in self.model_fields_set:
            _dict['onDestroy'] = None

        # set to None if on_deploy (nullable) is None
        # and model_fields_set contains the field
        if self.on_deploy is None and "on_deploy" in self.model_fields_set:
            _dict['onDeploy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlueprintApiRetry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "onDestroy": BlueprintApiRetryOnDestroy.from_dict(obj["onDestroy"]) if obj.get("onDestroy") is not None else None,
            "onDeploy": BlueprintApiRetryOnDestroy.from_dict(obj["onDeploy"]) if obj.get("onDeploy") is not None else None
        })
        return _obj

