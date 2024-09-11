# BfdStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detection_threshold** | **int** |  | 
**local** | **str** |  | [optional] 
**mode** | [**BfdMode**](BfdMode.md) |  | 
**peer** | **str** |  | 
**required_rx** | **int** |  | 
**state** | [**BfdState**](BfdState.md) |  | 
**switch** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.bfd_status import BfdStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BfdStatus from a JSON string
bfd_status_instance = BfdStatus.from_json(json)
# print the JSON string representation of the object
print(BfdStatus.to_json())

# convert the object into a dict
bfd_status_dict = bfd_status_instance.to_dict()
# create an instance of BfdStatus from a dict
bfd_status_from_dict = BfdStatus.from_dict(bfd_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


