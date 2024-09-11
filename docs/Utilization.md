# Utilization

View of the current silo's resource utilization and capacity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**VirtualResourceCounts**](VirtualResourceCounts.md) | The total amount of resources that can be provisioned in this silo Actions that would exceed this limit will fail | 
**provisioned** | [**VirtualResourceCounts**](VirtualResourceCounts.md) | Accounts for resources allocated to running instances or storage allocated via disks or snapshots Note that CPU and memory resources associated with a stopped instances are not counted here whereas associated disks will still be counted | 

## Example

```python
from oxide.models.utilization import Utilization

# TODO update the JSON string below
json = "{}"
# create an instance of Utilization from a JSON string
utilization_instance = Utilization.from_json(json)
# print the JSON string representation of the object
print(Utilization.to_json())

# convert the object into a dict
utilization_dict = utilization_instance.to_dict()
# create an instance of Utilization from a dict
utilization_from_dict = Utilization.from_dict(utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


