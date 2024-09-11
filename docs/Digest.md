# Digest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from oxide.models.digest import Digest

# TODO update the JSON string below
json = "{}"
# create an instance of Digest from a JSON string
digest_instance = Digest.from_json(json)
# print the JSON string representation of the object
print(Digest.to_json())

# convert the object into a dict
digest_dict = digest_instance.to_dict()
# create an instance of Digest from a dict
digest_from_dict = Digest.from_dict(digest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


