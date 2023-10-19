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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from petstore_api.models.category import Category
from petstore_api.models.tag import Tag

class Pet(BaseModel):
    """
    Pet
    """
    id: Optional[StrictInt] = None
    category: Optional[Category] = None
    name: StrictStr = Field(...)
    photo_urls: conlist(StrictStr, min_items=0, unique_items=True) = Field(..., alias="photoUrls")
    tags: Optional[conlist(Tag)] = None
    status: Optional[StrictStr] = Field(None, description="pet status in the store")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "category", "name", "photoUrls", "tags", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('available', 'pending', 'sold'):
            raise ValueError("must be one of enum values ('available', 'pending', 'sold')")
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
    def from_json(cls, json_str: str) -> Pet:
        """Create an instance of Pet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Pet:
        """Create an instance of Pet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Pet.parse_obj(obj)

        _obj = Pet.parse_obj({
            "id": obj.get("id"),
            "category": Category.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "name": obj.get("name"),
            "photo_urls": obj.get("photoUrls"),
            "tags": [Tag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


