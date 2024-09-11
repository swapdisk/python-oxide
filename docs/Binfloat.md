# Binfloat

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangefloat**](BinRangefloat.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binfloat import Binfloat

# TODO update the JSON string below
json = "{}"
# create an instance of Binfloat from a JSON string
binfloat_instance = Binfloat.from_json(json)
# print the JSON string representation of the object
print(Binfloat.to_json())

# convert the object into a dict
binfloat_dict = binfloat_instance.to_dict()
# create an instance of Binfloat from a dict
binfloat_from_dict = Binfloat.from_dict(binfloat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


