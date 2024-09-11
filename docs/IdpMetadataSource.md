# IdpMetadataSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from oxide.models.idp_metadata_source import IdpMetadataSource

# TODO update the JSON string below
json = "{}"
# create an instance of IdpMetadataSource from a JSON string
idp_metadata_source_instance = IdpMetadataSource.from_json(json)
# print the JSON string representation of the object
print(IdpMetadataSource.to_json())

# convert the object into a dict
idp_metadata_source_dict = idp_metadata_source_instance.to_dict()
# create an instance of IdpMetadataSource from a dict
idp_metadata_source_from_dict = IdpMetadataSource.from_dict(idp_metadata_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


