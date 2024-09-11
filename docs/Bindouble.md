# Bindouble

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangedouble**](BinRangedouble.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.bindouble import Bindouble

# TODO update the JSON string below
json = "{}"
# create an instance of Bindouble from a JSON string
bindouble_instance = Bindouble.from_json(json)
# print the JSON string representation of the object
print(Bindouble.to_json())

# convert the object into a dict
bindouble_dict = bindouble_instance.to_dict()
# create an instance of Bindouble from a dict
bindouble_from_dict = Bindouble.from_dict(bindouble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


