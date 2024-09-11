# Binint16

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeint16**](BinRangeint16.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binint16 import Binint16

# TODO update the JSON string below
json = "{}"
# create an instance of Binint16 from a JSON string
binint16_instance = Binint16.from_json(json)
# print the JSON string representation of the object
print(Binint16.to_json())

# convert the object into a dict
binint16_dict = binint16_instance.to_dict()
# create an instance of Binint16 from a dict
binint16_from_dict = Binint16.from_dict(binint16_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


