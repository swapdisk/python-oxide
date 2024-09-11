# SiloQuotasCreate

The amount of provisionable resources for a Silo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | The amount of virtual CPUs available for running instances in the Silo | 
**memory** | **int** | The amount of RAM (in bytes) available for running instances in the Silo | 
**storage** | **int** | The amount of storage (in bytes) available for disks or snapshots | 

## Example

```python
from oxide.models.silo_quotas_create import SiloQuotasCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiloQuotasCreate from a JSON string
silo_quotas_create_instance = SiloQuotasCreate.from_json(json)
# print the JSON string representation of the object
print(SiloQuotasCreate.to_json())

# convert the object into a dict
silo_quotas_create_dict = silo_quotas_create_instance.to_dict()
# create an instance of SiloQuotasCreate from a dict
silo_quotas_create_from_dict = SiloQuotasCreate.from_dict(silo_quotas_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


