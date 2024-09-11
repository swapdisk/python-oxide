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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SshKey(BaseModel):
    """
    View of an SSH Key
    """ # noqa: E501
    description: StrictStr = Field(description="human-readable free-form text about a resource")
    id: StrictStr = Field(description="unique, immutable, system-controlled identifier for each resource")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=63)] = Field(description="unique, mutable, user-controlled identifier for each resource")
    public_key: StrictStr = Field(description="SSH public key, e.g., `\"ssh-ed25519 AAAAC3NzaC...\"`")
    silo_user_id: StrictStr = Field(description="The user to whom this key belongs")
    time_created: datetime = Field(description="timestamp when this resource was created")
    time_modified: datetime = Field(description="timestamp when this resource was last modified")
    __properties: ClassVar[List[str]] = ["description", "id", "name", "public_key", "silo_user_id", "time_created", "time_modified"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
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
        """Create an instance of SshKey from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SshKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "public_key": obj.get("public_key"),
            "silo_user_id": obj.get("silo_user_id"),
            "time_created": obj.get("time_created"),
            "time_modified": obj.get("time_modified")
        })
        return _obj


