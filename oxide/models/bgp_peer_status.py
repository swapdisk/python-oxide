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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from oxide.models.bgp_peer_state import BgpPeerState
from oxide.models.switch_location import SwitchLocation
from typing import Optional, Set
from typing_extensions import Self

class BgpPeerStatus(BaseModel):
    """
    The current status of a BGP peer.
    """ # noqa: E501
    addr: StrictStr = Field(description="IP address of the peer.")
    local_asn: Annotated[int, Field(strict=True, ge=0)] = Field(description="Local autonomous system number.")
    remote_asn: Annotated[int, Field(strict=True, ge=0)] = Field(description="Remote autonomous system number.")
    state: BgpPeerState = Field(description="State of the peer.")
    state_duration_millis: Annotated[int, Field(strict=True, ge=0)] = Field(description="Time of last state change.")
    switch: SwitchLocation = Field(description="Switch with the peer session.")
    __properties: ClassVar[List[str]] = ["addr", "local_asn", "remote_asn", "state", "state_duration_millis", "switch"]

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
        """Create an instance of BgpPeerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of switch
        if self.switch:
            _dict['switch'] = self.switch.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BgpPeerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addr": obj.get("addr"),
            "local_asn": obj.get("local_asn"),
            "remote_asn": obj.get("remote_asn"),
            "state": BgpPeerState.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "state_duration_millis": obj.get("state_duration_millis"),
            "switch": SwitchLocation.from_dict(obj["switch"]) if obj.get("switch") is not None else None
        })
        return _obj


