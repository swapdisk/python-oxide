# SiloQuotasUpdate

Updateable properties of a Silo's resource limits. If a value is omitted it will not be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | The amount of virtual CPUs available for running instances in the Silo | [optional] 
**memory** | **int** | The amount of RAM (in bytes) available for running instances in the Silo | [optional] 
**storage** | **int** | The amount of storage (in bytes) available for disks or snapshots | [optional] 

## Example

```python
from oxide.models.silo_quotas_update import SiloQuotasUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SiloQuotasUpdate from a JSON string
silo_quotas_update_instance = SiloQuotasUpdate.from_json(json)
# print the JSON string representation of the object
print(SiloQuotasUpdate.to_json())

# convert the object into a dict
silo_quotas_update_dict = silo_quotas_update_instance.to_dict()
# create an instance of SiloQuotasUpdate from a dict
silo_quotas_update_from_dict = SiloQuotasUpdate.from_dict(silo_quotas_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


