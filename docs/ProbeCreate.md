# ProbeCreate

Create time parameters for probes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**ip_pool** | [**NameOrId**](NameOrId.md) |  | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**sled** | **str** |  | 

## Example

```python
from oxide.models.probe_create import ProbeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeCreate from a JSON string
probe_create_instance = ProbeCreate.from_json(json)
# print the JSON string representation of the object
print(ProbeCreate.to_json())

# convert the object into a dict
probe_create_dict = probe_create_instance.to_dict()
# create an instance of ProbeCreate from a dict
probe_create_from_dict = ProbeCreate.from_dict(probe_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


