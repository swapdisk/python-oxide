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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from oxide.models.ip_net import IpNet
from typing import Optional, Set
from typing_extensions import Self

class InstanceNetworkInterfaceUpdate(BaseModel):
    """
    Parameters for updating an `InstanceNetworkInterface`  Note that modifying IP addresses for an interface is not yet supported, a new interface must be created instead.
    """ # noqa: E501
    description: Optional[StrictStr] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=63)]] = Field(default=None, description="Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and '-', and may not end with a '-'. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long.")
    primary: Optional[StrictBool] = Field(default=False, description="Make a secondary interface the instance's primary interface.  If applied to a secondary interface, that interface will become the primary on the next reboot of the instance. Note that this may have implications for routing between instances, as the new primary interface will be on a distinct subnet from the previous primary interface.  Note that this can only be used to select a new primary interface for an instance. Requests to change the primary interface into a secondary will return an error.")
    transit_ips: Optional[List[IpNet]] = Field(default=None, description="A set of additional networks that this interface may send and receive traffic on.")
    __properties: ClassVar[List[str]] = ["description", "name", "primary", "transit_ips"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
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
        """Create an instance of InstanceNetworkInterfaceUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transit_ips (list)
        _items = []
        if self.transit_ips:
            for _item_transit_ips in self.transit_ips:
                if _item_transit_ips:
                    _items.append(_item_transit_ips.to_dict())
            _dict['transit_ips'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstanceNetworkInterfaceUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "name": obj.get("name"),
            "primary": obj.get("primary") if obj.get("primary") is not None else False,
            "transit_ips": [IpNet.from_dict(_item) for _item in obj["transit_ips"]] if obj.get("transit_ips") is not None else None
        })
        return _obj


