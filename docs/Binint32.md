# Binint32

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeint32**](BinRangeint32.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binint32 import Binint32

# TODO update the JSON string below
json = "{}"
# create an instance of Binint32 from a JSON string
binint32_instance = Binint32.from_json(json)
# print the JSON string representation of the object
print(Binint32.to_json())

# convert the object into a dict
binint32_dict = binint32_instance.to_dict()
# create an instance of Binint32 from a dict
binint32_from_dict = Binint32.from_dict(binint32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


