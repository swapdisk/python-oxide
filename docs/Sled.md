# Sled

An operator's view of a Sled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseboard** | [**Baseboard**](Baseboard.md) |  | 
**id** | **str** | unique, immutable, system-controlled identifier for each resource | 
**policy** | [**SledPolicy**](SledPolicy.md) | The operator-defined policy of a sled. | 
**rack_id** | **str** | The rack to which this Sled is currently attached | 
**state** | [**SledState**](SledState.md) | The current state Nexus believes the sled to be in. | 
**time_created** | **datetime** | timestamp when this resource was created | 
**time_modified** | **datetime** | timestamp when this resource was last modified | 
**usable_hardware_threads** | **int** | The number of hardware threads which can execute on this sled | 
**usable_physical_ram** | **int** | Amount of RAM which may be used by the Sled&#39;s OS | 

## Example

```python
from oxide.models.sled import Sled

# TODO update the JSON string below
json = "{}"
# create an instance of Sled from a JSON string
sled_instance = Sled.from_json(json)
# print the JSON string representation of the object
print(Sled.to_json())

# convert the object into a dict
sled_dict = sled_instance.to_dict()
# create an instance of Sled from a dict
sled_from_dict = Sled.from_dict(sled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


