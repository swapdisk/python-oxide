# Binint8

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeint8**](BinRangeint8.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binint8 import Binint8

# TODO update the JSON string below
json = "{}"
# create an instance of Binint8 from a JSON string
binint8_instance = Binint8.from_json(json)
# print the JSON string representation of the object
print(Binint8.to_json())

# convert the object into a dict
binint8_dict = binint8_instance.to_dict()
# create an instance of Binint8 from a dict
binint8_from_dict = Binint8.from_dict(binint8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


