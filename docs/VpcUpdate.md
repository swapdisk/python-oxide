# VpcUpdate

Updateable properties of a `Vpc`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**dns_name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | [optional] 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | [optional] 

## Example

```python
from oxide.models.vpc_update import VpcUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VpcUpdate from a JSON string
vpc_update_instance = VpcUpdate.from_json(json)
# print the JSON string representation of the object
print(VpcUpdate.to_json())

# convert the object into a dict
vpc_update_dict = vpc_update_instance.to_dict()
# create an instance of VpcUpdate from a dict
vpc_update_from_dict = VpcUpdate.from_dict(vpc_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


