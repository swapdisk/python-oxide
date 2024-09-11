# BgpImportedRouteIpv4

A route imported from a BGP peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | BGP identifier of the originating router. | 
**nexthop** | **str** | The nexthop the prefix is reachable through. | 
**prefix** | **str** | The destination network prefix. | 
**switch** | [**SwitchLocation**](SwitchLocation.md) | Switch the route is imported into. | 

## Example

```python
from oxide.models.bgp_imported_route_ipv4 import BgpImportedRouteIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpImportedRouteIpv4 from a JSON string
bgp_imported_route_ipv4_instance = BgpImportedRouteIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpImportedRouteIpv4.to_json())

# convert the object into a dict
bgp_imported_route_ipv4_dict = bgp_imported_route_ipv4_instance.to_dict()
# create an instance of BgpImportedRouteIpv4 from a dict
bgp_imported_route_ipv4_from_dict = BgpImportedRouteIpv4.from_dict(bgp_imported_route_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


