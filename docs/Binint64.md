# Binint64

Type storing bin edges and a count of samples within it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total count of samples in this bin. | 
**range** | [**BinRangeint64**](BinRangeint64.md) | The range of the support covered by this bin. | 

## Example

```python
from oxide.models.binint64 import Binint64

# TODO update the JSON string below
json = "{}"
# create an instance of Binint64 from a JSON string
binint64_instance = Binint64.from_json(json)
# print the JSON string representation of the object
print(Binint64.to_json())

# convert the object into a dict
binint64_dict = binint64_instance.to_dict()
# create an instance of Binint64 from a dict
binint64_from_dict = Binint64.from_dict(binint64_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


