# Binuint16

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeuint16**](BinRangeuint16.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binuint16 import Binuint16

# TODO update the JSON string below
json = "{}"
# create an instance of Binuint16 from a JSON string
binuint16_instance = Binuint16.from_json(json)
# print the JSON string representation of the object
print(Binuint16.to_json())

# convert the object into a dict
binuint16_dict = binuint16_instance.to_dict()
# create an instance of Binuint16 from a dict
binuint16_from_dict = Binuint16.from_dict(binuint16_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


