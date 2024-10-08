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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from oxide.models.quantile import Quantile
from typing import Optional, Set
from typing_extensions import Self

class Distributiondouble(BaseModel):
    """
    A distribution is a sequence of bins and counts in those bins, and some statistical information tracked to compute the mean, standard deviation, and quantile estimates.  Min, max, and the p-* quantiles are treated as optional due to the possibility of distribution operations, like subtraction.
    """ # noqa: E501
    bins: List[Union[StrictFloat, StrictInt]]
    counts: List[Annotated[int, Field(strict=True, ge=0)]]
    max: Optional[Union[StrictFloat, StrictInt]] = None
    min: Optional[Union[StrictFloat, StrictInt]] = None
    p50: Optional[Quantile] = None
    p90: Optional[Quantile] = None
    p99: Optional[Quantile] = None
    squared_mean: Union[StrictFloat, StrictInt]
    sum_of_samples: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["bins", "counts", "max", "min", "p50", "p90", "p99", "squared_mean", "sum_of_samples"]

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
        """Create an instance of Distributiondouble from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of p50
        if self.p50:
            _dict['p50'] = self.p50.to_dict()
        # override the default output from pydantic by calling `to_dict()` of p90
        if self.p90:
            _dict['p90'] = self.p90.to_dict()
        # override the default output from pydantic by calling `to_dict()` of p99
        if self.p99:
            _dict['p99'] = self.p99.to_dict()
        # set to None if max (nullable) is None
        # and model_fields_set contains the field
        if self.max is None and "max" in self.model_fields_set:
            _dict['max'] = None

        # set to None if min (nullable) is None
        # and model_fields_set contains the field
        if self.min is None and "min" in self.model_fields_set:
            _dict['min'] = None

        # set to None if p50 (nullable) is None
        # and model_fields_set contains the field
        if self.p50 is None and "p50" in self.model_fields_set:
            _dict['p50'] = None

        # set to None if p90 (nullable) is None
        # and model_fields_set contains the field
        if self.p90 is None and "p90" in self.model_fields_set:
            _dict['p90'] = None

        # set to None if p99 (nullable) is None
        # and model_fields_set contains the field
        if self.p99 is None and "p99" in self.model_fields_set:
            _dict['p99'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Distributiondouble from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bins": obj.get("bins"),
            "counts": obj.get("counts"),
            "max": obj.get("max"),
            "min": obj.get("min"),
            "p50": Quantile.from_dict(obj["p50"]) if obj.get("p50") is not None else None,
            "p90": Quantile.from_dict(obj["p90"]) if obj.get("p90") is not None else None,
            "p99": Quantile.from_dict(obj["p99"]) if obj.get("p99") is not None else None,
            "squared_mean": obj.get("squared_mean"),
            "sum_of_samples": obj.get("sum_of_samples")
        })
        return _obj


