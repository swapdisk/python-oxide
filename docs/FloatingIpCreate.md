# FloatingIpCreate

Parameters for creating a new floating IP address for instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**ip** | **str** | An IP address to reserve for use as a floating IP. This field is optional: when not set, an address will be automatically chosen from &#x60;pool&#x60;. If set, then the IP must be available in the resolved &#x60;pool&#x60;. | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**pool** | [**NameOrId**](NameOrId.md) | The parent IP pool that a floating IP is pulled from. If unset, the default pool is selected. | [optional] 

## Example

```python
from oxide.models.floating_ip_create import FloatingIpCreate

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIpCreate from a JSON string
floating_ip_create_instance = FloatingIpCreate.from_json(json)
# print the JSON string representation of the object
print(FloatingIpCreate.to_json())

# convert the object into a dict
floating_ip_create_dict = floating_ip_create_instance.to_dict()
# create an instance of FloatingIpCreate from a dict
floating_ip_create_from_dict = FloatingIpCreate.from_dict(floating_ip_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


