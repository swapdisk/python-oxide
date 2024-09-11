# ExternalIpOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | 
**kind** | **str** |  | 

## Example

```python
from oxide.models.external_ip_one_of import ExternalIpOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalIpOneOf from a JSON string
external_ip_one_of_instance = ExternalIpOneOf.from_json(json)
# print the JSON string representation of the object
print(ExternalIpOneOf.to_json())

# convert the object into a dict
external_ip_one_of_dict = external_ip_one_of_instance.to_dict()
# create an instance of ExternalIpOneOf from a dict
external_ip_one_of_from_dict = ExternalIpOneOf.from_dict(external_ip_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


