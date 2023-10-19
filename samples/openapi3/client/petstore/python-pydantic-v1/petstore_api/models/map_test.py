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


from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictBool, StrictStr, validator

class MapTest(BaseModel):
    """
    MapTest
    """
    map_map_of_string: Optional[Dict[str, Dict[str, StrictStr]]] = None
    map_of_enum_string: Optional[Dict[str, StrictStr]] = None
    direct_map: Optional[Dict[str, StrictBool]] = None
    indirect_map: Optional[Dict[str, StrictBool]] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["map_map_of_string", "map_of_enum_string", "direct_map", "indirect_map"]

    @validator('map_of_enum_string')
    def map_of_enum_string_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('UPPER', 'lower'):
            raise ValueError("must be one of enum values ('UPPER', 'lower')")
        return value

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
    def from_json(cls, json_str: str) -> MapTest:
        """Create an instance of MapTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MapTest:
        """Create an instance of MapTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapTest.parse_obj(obj)

        _obj = MapTest.parse_obj({
            "map_map_of_string": obj.get("map_map_of_string"),
            "map_of_enum_string": obj.get("map_of_enum_string"),
            "direct_map": obj.get("direct_map"),
            "indirect_map": obj.get("indirect_map")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


