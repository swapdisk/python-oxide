# BinRangedouble

A type storing a range over `T`.  This type supports ranges similar to the `RangeTo`, `Range` and `RangeFrom` types in the standard library. Those cover `(..end)`, `(start..end)`, and `(start..)` respectively.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **float** |  | 
**type** | **str** |  | 
**start** | **float** |  | 

## Example

```python
from oxide.models.bin_rangedouble import BinRangedouble

# TODO update the JSON string below
json = "{}"
# create an instance of BinRangedouble from a JSON string
bin_rangedouble_instance = BinRangedouble.from_json(json)
# print the JSON string representation of the object
print(BinRangedouble.to_json())

# convert the object into a dict
bin_rangedouble_dict = bin_rangedouble_instance.to_dict()
# create an instance of BinRangedouble from a dict
bin_rangedouble_from_dict = BinRangedouble.from_dict(bin_rangedouble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


