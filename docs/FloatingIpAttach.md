# FloatingIpAttach

Parameters for attaching a floating IP address to another resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**FloatingIpParentKind**](FloatingIpParentKind.md) | The type of &#x60;parent&#x60;&#39;s resource | 
**parent** | [**NameOrId**](NameOrId.md) | Name or ID of the resource that this IP address should be attached to | 

## Example

```python
from oxide.models.floating_ip_attach import FloatingIpAttach

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIpAttach from a JSON string
floating_ip_attach_instance = FloatingIpAttach.from_json(json)
# print the JSON string representation of the object
print(FloatingIpAttach.to_json())

# convert the object into a dict
floating_ip_attach_dict = floating_ip_attach_instance.to_dict()
# create an instance of FloatingIpAttach from a dict
floating_ip_attach_from_dict = FloatingIpAttach.from_dict(floating_ip_attach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


