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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from oxide.models.bgp_peer import BgpPeer
from oxide.models.lldp_link_config import LldpLinkConfig
from oxide.models.switch_interface_config import SwitchInterfaceConfig
from oxide.models.switch_port_address_config import SwitchPortAddressConfig
from oxide.models.switch_port_config import SwitchPortConfig
from oxide.models.switch_port_link_config import SwitchPortLinkConfig
from oxide.models.switch_port_route_config import SwitchPortRouteConfig
from oxide.models.switch_port_settings import SwitchPortSettings
from oxide.models.switch_port_settings_groups import SwitchPortSettingsGroups
from oxide.models.switch_vlan_interface_config import SwitchVlanInterfaceConfig
from typing import Optional, Set
from typing_extensions import Self

class SwitchPortSettingsView(BaseModel):
    """
    This structure contains all port settings information in one place. It's a convenience data structure for getting a complete view of a particular port's settings.
    """ # noqa: E501
    addresses: List[SwitchPortAddressConfig] = Field(description="Layer 3 IP address settings.")
    bgp_peers: List[BgpPeer] = Field(description="BGP peer settings.")
    groups: List[SwitchPortSettingsGroups] = Field(description="Switch port settings included from other switch port settings groups.")
    interfaces: List[SwitchInterfaceConfig] = Field(description="Layer 3 interface settings.")
    link_lldp: List[LldpLinkConfig] = Field(description="Link-layer discovery protocol (LLDP) settings.")
    links: List[SwitchPortLinkConfig] = Field(description="Layer 2 link settings.")
    port: SwitchPortConfig = Field(description="Layer 1 physical port settings.")
    routes: List[SwitchPortRouteConfig] = Field(description="IP route settings.")
    settings: SwitchPortSettings = Field(description="The primary switch port settings handle.")
    vlan_interfaces: List[SwitchVlanInterfaceConfig] = Field(description="Vlan interface settings.")
    __properties: ClassVar[List[str]] = ["addresses", "bgp_peers", "groups", "interfaces", "link_lldp", "links", "port", "routes", "settings", "vlan_interfaces"]

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
        """Create an instance of SwitchPortSettingsView from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item_addresses in self.addresses:
                if _item_addresses:
                    _items.append(_item_addresses.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bgp_peers (list)
        _items = []
        if self.bgp_peers:
            for _item_bgp_peers in self.bgp_peers:
                if _item_bgp_peers:
                    _items.append(_item_bgp_peers.to_dict())
            _dict['bgp_peers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in interfaces (list)
        _items = []
        if self.interfaces:
            for _item_interfaces in self.interfaces:
                if _item_interfaces:
                    _items.append(_item_interfaces.to_dict())
            _dict['interfaces'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in link_lldp (list)
        _items = []
        if self.link_lldp:
            for _item_link_lldp in self.link_lldp:
                if _item_link_lldp:
                    _items.append(_item_link_lldp.to_dict())
            _dict['link_lldp'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict['port'] = self.port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in routes (list)
        _items = []
        if self.routes:
            for _item_routes in self.routes:
                if _item_routes:
                    _items.append(_item_routes.to_dict())
            _dict['routes'] = _items
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vlan_interfaces (list)
        _items = []
        if self.vlan_interfaces:
            for _item_vlan_interfaces in self.vlan_interfaces:
                if _item_vlan_interfaces:
                    _items.append(_item_vlan_interfaces.to_dict())
            _dict['vlan_interfaces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwitchPortSettingsView from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addresses": [SwitchPortAddressConfig.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "bgp_peers": [BgpPeer.from_dict(_item) for _item in obj["bgp_peers"]] if obj.get("bgp_peers") is not None else None,
            "groups": [SwitchPortSettingsGroups.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "interfaces": [SwitchInterfaceConfig.from_dict(_item) for _item in obj["interfaces"]] if obj.get("interfaces") is not None else None,
            "link_lldp": [LldpLinkConfig.from_dict(_item) for _item in obj["link_lldp"]] if obj.get("link_lldp") is not None else None,
            "links": [SwitchPortLinkConfig.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "port": SwitchPortConfig.from_dict(obj["port"]) if obj.get("port") is not None else None,
            "routes": [SwitchPortRouteConfig.from_dict(_item) for _item in obj["routes"]] if obj.get("routes") is not None else None,
            "settings": SwitchPortSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "vlan_interfaces": [SwitchVlanInterfaceConfig.from_dict(_item) for _item in obj["vlan_interfaces"]] if obj.get("vlan_interfaces") is not None else None
        })
        return _obj


