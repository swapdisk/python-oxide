# Binuint64

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeuint64**](BinRangeuint64.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binuint64 import Binuint64

# TODO update the JSON string below
json = "{}"
# create an instance of Binuint64 from a JSON string
binuint64_instance = Binuint64.from_json(json)
# print the JSON string representation of the object
print(Binuint64.to_json())

# convert the object into a dict
binuint64_dict = binuint64_instance.to_dict()
# create an instance of Binuint64 from a dict
binuint64_from_dict = Binuint64.from_dict(binuint64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


