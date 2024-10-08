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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from oxide.models.external_ip_create import ExternalIpCreate
from oxide.models.instance_disk_attachment import InstanceDiskAttachment
from oxide.models.instance_network_interface_attachment import InstanceNetworkInterfaceAttachment
from oxide.models.name_or_id import NameOrId
from typing import Optional, Set
from typing_extensions import Self

class InstanceCreate(BaseModel):
    """
    Create-time parameters for an `Instance`
    """ # noqa: E501
    description: StrictStr
    disks: Optional[List[InstanceDiskAttachment]] = Field(default=None, description="The disks to be created or attached for this instance.")
    external_ips: Optional[List[ExternalIpCreate]] = Field(default=None, description="The external IP addresses provided to this instance.  By default, all instances have outbound connectivity, but no inbound connectivity. These external addresses can be used to provide a fixed, known IP address for making inbound connections to the instance.")
    hostname: Annotated[str, Field(min_length=1, strict=True, max_length=253)] = Field(description="A hostname identifies a host on a network, and is usually a dot-delimited sequence of labels, where each label contains only letters, digits, or the hyphen. See RFCs 1035 and 952 for more details.")
    memory: Annotated[int, Field(strict=True, ge=0)] = Field(description="Byte count to express memory or storage capacity.")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=63)] = Field(description="Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and '-', and may not end with a '-'. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long.")
    ncpus: Annotated[int, Field(strict=True, ge=0)] = Field(description="The number of CPUs in an Instance")
    network_interfaces: Optional[InstanceNetworkInterfaceAttachment] = Field(default=None, description="The network interfaces to be created for this instance.")
    ssh_public_keys: Optional[List[NameOrId]] = Field(default=None, description="An allowlist of SSH public keys to be transferred to the instance via cloud-init during instance creation.  If not provided, all SSH public keys from the user's profile will be sent. If an empty list is provided, no public keys will be transmitted to the instance.")
    start: Optional[StrictBool] = Field(default=True, description="Should this instance be started upon creation; true by default.")
    user_data: Optional[Union[StrictBytes, StrictStr]] = Field(default='[B@1763992e', description="User data for instance initialization systems (such as cloud-init). Must be a Base64-encoded string, as specified in RFC 4648 § 4 (+ and / characters with padding). Maximum 32 KiB unencoded data.")
    __properties: ClassVar[List[str]] = ["description", "disks", "external_ips", "hostname", "memory", "name", "ncpus", "network_interfaces", "ssh_public_keys", "start", "user_data"]

    @field_validator('hostname')
    def hostname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^([a-zA-Z0-9]+[a-zA-Z0-9\-]*(?<!-))(\.[a-zA-Z0-9]+[a-zA-Z0-9\-]*(?<!-))*$", value):
            raise ValueError(r"must validate the regular expression /^([a-zA-Z0-9]+[a-zA-Z0-9\-]*(?<!-))(\.[a-zA-Z0-9]+[a-zA-Z0-9\-]*(?<!-))*$/")
        return value

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
        """Create an instance of InstanceCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in disks (list)
        _items = []
        if self.disks:
            for _item_disks in self.disks:
                if _item_disks:
                    _items.append(_item_disks.to_dict())
            _dict['disks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_ips (list)
        _items = []
        if self.external_ips:
            for _item_external_ips in self.external_ips:
                if _item_external_ips:
                    _items.append(_item_external_ips.to_dict())
            _dict['external_ips'] = _items
        # override the default output from pydantic by calling `to_dict()` of network_interfaces
        if self.network_interfaces:
            _dict['network_interfaces'] = self.network_interfaces.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ssh_public_keys (list)
        _items = []
        if self.ssh_public_keys:
            for _item_ssh_public_keys in self.ssh_public_keys:
                if _item_ssh_public_keys:
                    _items.append(_item_ssh_public_keys.to_dict())
            _dict['ssh_public_keys'] = _items
        # set to None if ssh_public_keys (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_public_keys is None and "ssh_public_keys" in self.model_fields_set:
            _dict['ssh_public_keys'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstanceCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "disks": [InstanceDiskAttachment.from_dict(_item) for _item in obj["disks"]] if obj.get("disks") is not None else None,
            "external_ips": [ExternalIpCreate.from_dict(_item) for _item in obj["external_ips"]] if obj.get("external_ips") is not None else None,
            "hostname": obj.get("hostname"),
            "memory": obj.get("memory"),
            "name": obj.get("name"),
            "ncpus": obj.get("ncpus"),
            "network_interfaces": InstanceNetworkInterfaceAttachment.from_dict(obj["network_interfaces"]) if obj.get("network_interfaces") is not None else None,
            "ssh_public_keys": [NameOrId.from_dict(_item) for _item in obj["ssh_public_keys"]] if obj.get("ssh_public_keys") is not None else None,
            "start": obj.get("start") if obj.get("start") is not None else True,
            "user_data": obj.get("user_data") if obj.get("user_data") is not None else '[B@1763992e'
        })
        return _obj


