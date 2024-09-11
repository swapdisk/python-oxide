# SledInstance

An operator's view of an instance running on a given sled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_sled_id** | **str** |  | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**memory** | **int** |  | 
**migration_id** | **str** |  | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**ncpus** | **int** |  | 
**project_name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**silo_name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**state** | [**InstanceState**](InstanceState.md) |  | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.sled_instance import SledInstance

# TODO update the JSON string below
json = "{}"
# create an instance of SledInstance from a JSON string
sled_instance_instance = SledInstance.from_json(json)
# print the JSON string representation of the object
print(SledInstance.to_json())

# convert the object into a dict
sled_instance_dict = sled_instance_instance.to_dict()
# create an instance of SledInstance from a dict
sled_instance_from_dict = SledInstance.from_dict(sled_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


