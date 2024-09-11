# ProjectCreate

Create-time parameters for a `Project`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 

## Example

```python
from oxide.models.project_create import ProjectCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreate from a JSON string
project_create_instance = ProjectCreate.from_json(json)
# print the JSON string representation of the object
print(ProjectCreate.to_json())

# convert the object into a dict
project_create_dict = project_create_instance.to_dict()
# create an instance of ProjectCreate from a dict
project_create_from_dict = ProjectCreate.from_dict(project_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


