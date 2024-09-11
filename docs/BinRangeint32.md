# BinRangeint32

A type storing a range over `T`.  This type supports ranges similar to the `RangeTo`, `Range` and `RangeFrom` types in the standard library. Those cover `(..end)`, `(start..end)`, and `(start..)` respectively.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | 
**type** | **str** |  | 
**start** | **int** |  | 

## Example

```python
from oxide.models.bin_rangeint32 import BinRangeint32

# TODO update the JSON string below
json = "{}"
# create an instance of BinRangeint32 from a JSON string
bin_rangeint32_instance = BinRangeint32.from_json(json)
# print the JSON string representation of the object
print(BinRangeint32.to_json())

# convert the object into a dict
bin_rangeint32_dict = bin_rangeint32_instance.to_dict()
# create an instance of BinRangeint32 from a dict
bin_rangeint32_from_dict = BinRangeint32.from_dict(bin_rangeint32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


