# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt

class SelfReferenceModel(BaseModel):
    """
    SelfReferenceModel
    """
    size: Optional[StrictInt] = None
    nested: Optional[DummyModel] = None
    __properties = ["size", "nested"]

    class Config:
        """Pydantic configuration"""
        populate_by_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SelfReferenceModel:
        """Create an instance of SelfReferenceModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of nested
        if self.nested:
            _dict['nested'] = self.nested.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SelfReferenceModel:
        """Create an instance of SelfReferenceModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SelfReferenceModel.parse_obj(obj)

        _obj = SelfReferenceModel.parse_obj({
            "size": obj.get("size"),
            "nested": DummyModel.from_dict(obj.get("nested")) if obj.get("nested") is not None else None
        })
        return _obj

from petstore_api.models.dummy_model import DummyModel
SelfReferenceModel.update_forward_refs()

