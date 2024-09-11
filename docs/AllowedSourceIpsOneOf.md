# AllowedSourceIpsOneOf

Allow traffic from any external IP address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **str** |  | 

## Example

```python
from oxide.models.allowed_source_ips_one_of import AllowedSourceIpsOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedSourceIpsOneOf from a JSON string
allowed_source_ips_one_of_instance = AllowedSourceIpsOneOf.from_json(json)
# print the JSON string representation of the object
print(AllowedSourceIpsOneOf.to_json())

# convert the object into a dict
allowed_source_ips_one_of_dict = allowed_source_ips_one_of_instance.to_dict()
# create an instance of AllowedSourceIpsOneOf from a dict
allowed_source_ips_one_of_from_dict = AllowedSourceIpsOneOf.from_dict(allowed_source_ips_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


