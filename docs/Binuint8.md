# Binuint8

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeuint8**](BinRangeuint8.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binuint8 import Binuint8

# TODO update the JSON string below
json = "{}"
# create an instance of Binuint8 from a JSON string
binuint8_instance = Binuint8.from_json(json)
# print the JSON string representation of the object
print(Binuint8.to_json())

# convert the object into a dict
binuint8_dict = binuint8_instance.to_dict()
# create an instance of Binuint8 from a dict
binuint8_from_dict = Binuint8.from_dict(binuint8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


