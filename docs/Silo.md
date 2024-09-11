# Silo

View of a Silo  A Silo is the highest level unit of isolation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | human-readable free-form text about a resource | 
**discoverable** | **bool** | A silo where discoverable is false can be retrieved only by its id - it will not be part of the \&quot;list all silos\&quot; output. | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**identity_mode** | [**SiloIdentityMode**](SiloIdentityMode.md) | How users and groups are managed in this Silo | 
**mapped_fleet_roles** | **Dict[str, List[FleetRole]]** | Mapping of which Fleet roles are conferred by each Silo role  The default is that no Fleet roles are conferred by any Silo roles unless there&#39;s a corresponding entry in this map. | 
**name** | **str** | unique, mutable, user-controlled identifier for each resource | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 

## Example

```python
from oxide.models.silo import Silo

# TODO update the JSON string below
json = "{}"
# create an instance of Silo from a JSON string
silo_instance = Silo.from_json(json)
# print the JSON string representation of the object
print(Silo.to_json())

# convert the object into a dict
silo_dict = silo_instance.to_dict()
# create an instance of Silo from a dict
silo_from_dict = Silo.from_dict(silo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


