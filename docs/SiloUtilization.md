# SiloUtilization

View of a silo's resource utilization and capacity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**VirtualResourceCounts**](VirtualResourceCounts.md) | Accounts for the total amount of resources reserved for silos via their quotas | 
**provisioned** | [**VirtualResourceCounts**](VirtualResourceCounts.md) | Accounts for resources allocated by in silos like CPU or memory for running instances and storage for disks and snapshots Note that CPU and memory resources associated with a stopped instances are not counted here | 
**silo_id** | **str** |  | 
**silo_name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.silo_utilization import SiloUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of SiloUtilization from a JSON string
silo_utilization_instance = SiloUtilization.from_json(json)
# print the JSON string representation of the object
print(SiloUtilization.to_json())

# convert the object into a dict
silo_utilization_dict = silo_utilization_instance.to_dict()
# create an instance of SiloUtilization from a dict
silo_utilization_from_dict = SiloUtilization.from_dict(silo_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


