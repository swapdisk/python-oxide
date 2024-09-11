# Route

A route to a destination network through a gateway address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst** | [**IpNet**](IpNet.md) | The route destination. | 
**gw** | **str** | The route gateway. | 
**local_pref** | **int** | Local preference for route. Higher preference indictes precedence within and across protocols. | [optional] 
**vid** | **int** | VLAN id the gateway is reachable over. | [optional] 

## Example

```python
from oxide.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print(Route.to_json())

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_from_dict = Route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


