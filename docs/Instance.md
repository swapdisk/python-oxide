# Instance

View of an Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**hostname** | **str** | RFC1035-compliant hostname for the Instance. | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**memory** | **int** | memory allocated for this Instance | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**ncpus** | **int** | number of CPUs allocated for this Instance | 
**project_id** | **str** | id for the project containing this Instance | 
**run_state** | [**InstanceState**](InstanceState.md) |  | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**time_run_state_updated** | **datetime** |  | 

## Example

```python
from oxide.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


