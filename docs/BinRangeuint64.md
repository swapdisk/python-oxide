# BinRangeuint64

A type storing a range over `T`.  This type supports ranges similar to the `RangeTo`, `Range` and `RangeFrom` types in the standard library. Those cover `(..end)`, `(start..end)`, and `(start..)` respectively.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | 
**type** | **str** |  | 
**start** | **int** |  | 

## Example

```python
from oxide.models.bin_rangeuint64 import BinRangeuint64

# TODO update the JSON string below
json = "{}"
# create an instance of BinRangeuint64 from a JSON string
bin_rangeuint64_instance = BinRangeuint64.from_json(json)
# print the JSON string representation of the object
print(BinRangeuint64.to_json())

# convert the object into a dict
bin_rangeuint64_dict = bin_rangeuint64_instance.to_dict()
# create an instance of BinRangeuint64 from a dict
bin_rangeuint64_from_dict = BinRangeuint64.from_dict(bin_rangeuint64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


