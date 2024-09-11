# Binuint32

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeuint32**](BinRangeuint32.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binuint32 import Binuint32

# TODO update the JSON string below
json = "{}"
# create an instance of Binuint32 from a JSON string
binuint32_instance = Binuint32.from_json(json)
# print the JSON string representation of the object
print(Binuint32.to_json())

# convert the object into a dict
binuint32_dict = binuint32_instance.to_dict()
# create an instance of Binuint32 from a dict
binuint32_from_dict = Binuint32.from_dict(binuint32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


