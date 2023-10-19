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



from pydantic import BaseModel, Field, StrictStr
from petstore_api.models.creature_info import CreatureInfo

class Creature(BaseModel):
    """
    Creature
    """
    info: CreatureInfo = Field(...)
    type: StrictStr = Field(...)
    __properties = ["info", "type"]

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
    def from_json(cls, json_str: str) -> Creature:
        """Create an instance of Creature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Creature:
        """Create an instance of Creature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Creature.parse_obj(obj)

        _obj = Creature.parse_obj({
            "info": CreatureInfo.from_dict(obj.get("info")) if obj.get("info") is not None else None,
            "type": obj.get("type")
        })
        return _obj


