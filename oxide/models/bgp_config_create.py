# coding: utf-8

"""
    Oxide Region API

    API for interacting with the Oxide control plane

    The version of the OpenAPI document: 20240821.0
    Contact: api@oxide.computer
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from oxide.models.name_or_id import NameOrId
from typing import Optional, Set
from typing_extensions import Self

class BgpConfigCreate(BaseModel):
    """
    Parameters for creating a BGP configuration. This includes and autonomous system number (ASN) and a virtual routing and forwarding (VRF) identifier.
    """ # noqa: E501
    asn: Annotated[int, Field(strict=True, ge=0)] = Field(description="The autonomous system number of this BGP configuration.")
    bgp_announce_set_id: NameOrId
    description: StrictStr
    name: Annotated[str, Field(min_length=1, strict=True, max_length=63)] = Field(description="Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and '-', and may not end with a '-'. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long.")
    vrf: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=63)]] = Field(default=None, description="Optional virtual routing and forwarding identifier for this BGP configuration.")
    __properties: ClassVar[List[str]] = ["asn", "bgp_announce_set_id", "description", "name", "vrf"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?![0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$)^[a-z]([a-zA-Z0-9-]*[a-zA-Z0-9]+)?$", value):
            raise ValueError(r"must validate the regular expression /^(?![0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$)^[a-z]([a-zA-Z0-9-]*[a-zA-Z0-9]+)?$/")
        return value

    @field_validator('vrf')
    def vrf_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?![0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$)^[a-z]([a-zA-Z0-9-]*[a-zA-Z0-9]+)?$", value):
            raise ValueError(r"must validate the regular expression /^(?![0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$)^[a-z]([a-zA-Z0-9-]*[a-zA-Z0-9]+)?$/")
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
        """Create an instance of BgpConfigCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bgp_announce_set_id
        if self.bgp_announce_set_id:
            _dict['bgp_announce_set_id'] = self.bgp_announce_set_id.to_dict()
        # set to None if vrf (nullable) is None
        # and model_fields_set contains the field
        if self.vrf is None and "vrf" in self.model_fields_set:
            _dict['vrf'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BgpConfigCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asn": obj.get("asn"),
            "bgp_announce_set_id": NameOrId.from_dict(obj["bgp_announce_set_id"]) if obj.get("bgp_announce_set_id") is not None else None,
            "description": obj.get("description"),
            "name": obj.get("name"),
            "vrf": obj.get("vrf")
        })
        return _obj


