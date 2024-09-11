# SiloQuotas

A collection of resource counts used to set the virtual capacity of a silo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus** | **int** | Number of virtual CPUs | 
**memory** | **int** | Amount of memory in bytes | 
**silo_id** | **str** |  | 
**storage** | **int** | Amount of disk storage in bytes | 

## Example

```python
from oxide.models.silo_quotas import SiloQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of SiloQuotas from a JSON string
silo_quotas_instance = SiloQuotas.from_json(json)
# print the JSON string representation of the object
print(SiloQuotas.to_json())

# convert the object into a dict
silo_quotas_dict = silo_quotas_instance.to_dict()
# create an instance of SiloQuotas from a dict
silo_quotas_from_dict = SiloQuotas.from_dict(silo_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


