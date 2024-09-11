# FloatingIpUpdate

Updateable identity-related parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | [optional] 

## Example

```python
from oxide.models.floating_ip_update import FloatingIpUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIpUpdate from a JSON string
floating_ip_update_instance = FloatingIpUpdate.from_json(json)
# print the JSON string representation of the object
print(FloatingIpUpdate.to_json())

# convert the object into a dict
floating_ip_update_dict = floating_ip_update_instance.to_dict()
# create an instance of FloatingIpUpdate from a dict
floating_ip_update_from_dict = FloatingIpUpdate.from_dict(floating_ip_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


