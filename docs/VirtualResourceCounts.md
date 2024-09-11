# VirtualResourceCounts

A collection of resource counts used to describe capacity and utilization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | Number of virtual CPUs | 
**memory** | **int** | Amount of memory in bytes | 
**storage** | **int** | Amount of disk storage in bytes | 

## Example

```python
from oxide.models.virtual_resource_counts import VirtualResourceCounts

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualResourceCounts from a JSON string
virtual_resource_counts_instance = VirtualResourceCounts.from_json(json)
# print the JSON string representation of the object
print(VirtualResourceCounts.to_json())

# convert the object into a dict
virtual_resource_counts_dict = virtual_resource_counts_instance.to_dict()
# create an instance of VirtualResourceCounts from a dict
virtual_resource_counts_from_dict = VirtualResourceCounts.from_dict(virtual_resource_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


