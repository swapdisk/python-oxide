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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from oxide.models.bin_rangeint64_one_of import BinRangeint64OneOf
from oxide.models.bin_rangeint64_one_of1 import BinRangeint64OneOf1
from oxide.models.bin_rangeint64_one_of2 import BinRangeint64OneOf2
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

BINRANGEINT64_ONE_OF_SCHEMAS = ["BinRangeint64OneOf", "BinRangeint64OneOf1", "BinRangeint64OneOf2"]

class BinRangeint64(BaseModel):
    """
    A type storing a range over `T`.  This type supports ranges similar to the `RangeTo`, `Range` and `RangeFrom` types in the standard library. Those cover `(..end)`, `(start..end)`, and `(start..)` respectively.
    """
    # data type: BinRangeint64OneOf
    oneof_schema_1_validator: Optional[BinRangeint64OneOf] = None
    # data type: BinRangeint64OneOf1
    oneof_schema_2_validator: Optional[BinRangeint64OneOf1] = None
    # data type: BinRangeint64OneOf2
    oneof_schema_3_validator: Optional[BinRangeint64OneOf2] = None
    actual_instance: Optional[Union[BinRangeint64OneOf, BinRangeint64OneOf1, BinRangeint64OneOf2]] = None
    one_of_schemas: Set[str] = { "BinRangeint64OneOf", "BinRangeint64OneOf1", "BinRangeint64OneOf2" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = BinRangeint64.model_construct()
        error_messages = []
        match = 0
        # validate data type: BinRangeint64OneOf
        if not isinstance(v, BinRangeint64OneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BinRangeint64OneOf`")
        else:
            match += 1
        # validate data type: BinRangeint64OneOf1
        if not isinstance(v, BinRangeint64OneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BinRangeint64OneOf1`")
        else:
            match += 1
        # validate data type: BinRangeint64OneOf2
        if not isinstance(v, BinRangeint64OneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BinRangeint64OneOf2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BinRangeint64 with oneOf schemas: BinRangeint64OneOf, BinRangeint64OneOf1, BinRangeint64OneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BinRangeint64 with oneOf schemas: BinRangeint64OneOf, BinRangeint64OneOf1, BinRangeint64OneOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BinRangeint64OneOf
        try:
            instance.actual_instance = BinRangeint64OneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BinRangeint64OneOf1
        try:
            instance.actual_instance = BinRangeint64OneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BinRangeint64OneOf2
        try:
            instance.actual_instance = BinRangeint64OneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BinRangeint64 with oneOf schemas: BinRangeint64OneOf, BinRangeint64OneOf1, BinRangeint64OneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BinRangeint64 with oneOf schemas: BinRangeint64OneOf, BinRangeint64OneOf1, BinRangeint64OneOf2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BinRangeint64OneOf, BinRangeint64OneOf1, BinRangeint64OneOf2]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


