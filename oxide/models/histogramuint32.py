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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from oxide.models.binuint32 import Binuint32
from oxide.models.quantile import Quantile
from typing import Optional, Set
from typing_extensions import Self

class Histogramuint32(BaseModel):
    """
    Histogram metric  A histogram maintains the count of any number of samples, over a set of bins. Bins are specified on construction via their _left_ edges, inclusive. There can't be any \"gaps\" in the bins, and an additional bin may be added to the left, right, or both so that the bins extend to the entire range of the support.  Note that any gaps, unsorted bins, or non-finite values will result in an error.
    """ # noqa: E501
    bins: List[Binuint32] = Field(description="The bins of the histogram.")
    max: Annotated[int, Field(strict=True, ge=0)] = Field(description="The maximum value of all samples in the histogram.")
    min: Annotated[int, Field(strict=True, ge=0)] = Field(description="The minimum value of all samples in the histogram.")
    n_samples: Annotated[int, Field(strict=True, ge=0)] = Field(description="The total number of samples in the histogram.")
    p50: Quantile = Field(description="p50 Quantile")
    p90: Quantile = Field(description="p95 Quantile")
    p99: Quantile = Field(description="p99 Quantile")
    squared_mean: Union[StrictFloat, StrictInt] = Field(description="M2 for Welford's algorithm for variance calculation.  Read about [Welford's algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm) for more information on the algorithm.")
    start_time: datetime = Field(description="The start time of the histogram.")
    sum_of_samples: StrictInt = Field(description="The sum of all samples in the histogram.")
    __properties: ClassVar[List[str]] = ["bins", "max", "min", "n_samples", "p50", "p90", "p99", "squared_mean", "start_time", "sum_of_samples"]

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
        """Create an instance of Histogramuint32 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bins (list)
        _items = []
        if self.bins:
            for _item_bins in self.bins:
                if _item_bins:
                    _items.append(_item_bins.to_dict())
            _dict['bins'] = _items
        # override the default output from pydantic by calling `to_dict()` of p50
        if self.p50:
            _dict['p50'] = self.p50.to_dict()
        # override the default output from pydantic by calling `to_dict()` of p90
        if self.p90:
            _dict['p90'] = self.p90.to_dict()
        # override the default output from pydantic by calling `to_dict()` of p99
        if self.p99:
            _dict['p99'] = self.p99.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Histogramuint32 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bins": [Binuint32.from_dict(_item) for _item in obj["bins"]] if obj.get("bins") is not None else None,
            "max": obj.get("max"),
            "min": obj.get("min"),
            "n_samples": obj.get("n_samples"),
            "p50": Quantile.from_dict(obj["p50"]) if obj.get("p50") is not None else None,
            "p90": Quantile.from_dict(obj["p90"]) if obj.get("p90") is not None else None,
            "p99": Quantile.from_dict(obj["p99"]) if obj.get("p99") is not None else None,
            "squared_mean": obj.get("squared_mean"),
            "start_time": obj.get("start_time"),
            "sum_of_samples": obj.get("sum_of_samples")
        })
        return _obj


