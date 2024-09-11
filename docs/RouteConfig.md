# RouteConfig

Route configuration data associated with a switch port configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routes** | [**List[Route]**](Route.md) | The set of routes assigned to a switch port. | 

## Example

```python
from oxide.models.route_config import RouteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RouteConfig from a JSON string
route_config_instance = RouteConfig.from_json(json)
# print the JSON string representation of the object
print(RouteConfig.to_json())

# convert the object into a dict
route_config_dict = route_config_instance.to_dict()
# create an instance of RouteConfig from a dict
route_config_from_dict = RouteConfig.from_dict(route_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


