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
import json
from enum import Enum
from typing_extensions import Self


class SystemMetricName(str, Enum):
    """
    SystemMetricName
    """

    """
    allowed enum values
    """
    VIRTUAL_DISK_SPACE_PROVISIONED = 'virtual_disk_space_provisioned'
    CPUS_PROVISIONED = 'cpus_provisioned'
    RAM_PROVISIONED = 'ram_provisioned'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SystemMetricName from a JSON string"""
        return cls(json.loads(json_str))


