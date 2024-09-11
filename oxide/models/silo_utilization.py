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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from oxide.models.virtual_resource_counts import VirtualResourceCounts
from typing import Optional, Set
from typing_extensions import Self

class SiloUtilization(BaseModel):
    """
    View of a silo's resource utilization and capacity
    """ # noqa: E501
    allocated: VirtualResourceCounts = Field(description="Accounts for the total amount of resources reserved for silos via their quotas")
    provisioned: VirtualResourceCounts = Field(description="Accounts for resources allocated by in silos like CPU or memory for running instances and storage for disks and snapshots Note that CPU and memory resources associated with a stopped instances are not counted here")
    silo_id: StrictStr
    silo_name: Annotated[str, Field(min_length=1, strict=True, max_length=63)] = Field(description="Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and '-', and may not end with a '-'. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long.")
    __properties: ClassVar[List[str]] = ["allocated", "provisioned", "silo_id", "silo_name"]

    @field_validator('silo_name')
    def silo_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of SiloUtilization from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of allocated
        if self.allocated:
            _dict['allocated'] = self.allocated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provisioned
        if self.provisioned:
            _dict['provisioned'] = self.provisioned.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SiloUtilization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allocated": VirtualResourceCounts.from_dict(obj["allocated"]) if obj.get("allocated") is not None else None,
            "provisioned": VirtualResourceCounts.from_dict(obj["provisioned"]) if obj.get("provisioned") is not None else None,
            "silo_id": obj.get("silo_id"),
            "silo_name": obj.get("silo_name")
        })
        return _obj


