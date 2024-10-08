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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from oxide.models.ip_net import IpNet
from typing import Optional, Set
from typing_extensions import Self

class SwitchPortAddressConfig(BaseModel):
    """
    An IP address configuration for a port settings object.
    """ # noqa: E501
    address: IpNet = Field(description="The IP address and prefix.")
    address_lot_block_id: StrictStr = Field(description="The id of the address lot block this address is drawn from.")
    interface_name: StrictStr = Field(description="The interface name this address belongs to.")
    port_settings_id: StrictStr = Field(description="The port settings object this address configuration belongs to.")
    vlan_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="An optional VLAN ID")
    __properties: ClassVar[List[str]] = ["address", "address_lot_block_id", "interface_name", "port_settings_id", "vlan_id"]

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
        """Create an instance of SwitchPortAddressConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # set to None if vlan_id (nullable) is None
        # and model_fields_set contains the field
        if self.vlan_id is None and "vlan_id" in self.model_fields_set:
            _dict['vlan_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwitchPortAddressConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": IpNet.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "address_lot_block_id": obj.get("address_lot_block_id"),
            "interface_name": obj.get("interface_name"),
            "port_settings_id": obj.get("port_settings_id"),
            "vlan_id": obj.get("vlan_id")
        })
        return _obj


