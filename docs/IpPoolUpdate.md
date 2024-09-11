# IpPoolUpdate

Parameters for updating an IP Pool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | [optional] 

## Example

```python
from oxide.models.ip_pool_update import IpPoolUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolUpdate from a JSON string
ip_pool_update_instance = IpPoolUpdate.from_json(json)
# print the JSON string representation of the object
print(IpPoolUpdate.to_json())

# convert the object into a dict
ip_pool_update_dict = ip_pool_update_instance.to_dict()
# create an instance of IpPoolUpdate from a dict
ip_pool_update_from_dict = IpPoolUpdate.from_dict(ip_pool_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


