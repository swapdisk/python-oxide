# BinRangeint8OneOf

A range unbounded below and exclusively above, `..end`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from oxide.models.bin_rangeint8_one_of import BinRangeint8OneOf

# TODO update the JSON string below
json = "{}"
# create an instance of BinRangeint8OneOf from a JSON string
bin_rangeint8_one_of_instance = BinRangeint8OneOf.from_json(json)
# print the JSON string representation of the object
print(BinRangeint8OneOf.to_json())

# convert the object into a dict
bin_rangeint8_one_of_dict = bin_rangeint8_one_of_instance.to_dict()
# create an instance of BinRangeint8OneOf from a dict
bin_rangeint8_one_of_from_dict = BinRangeint8OneOf.from_dict(bin_rangeint8_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


