# BgpExported

The current status of a BGP peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exports** | **Dict[str, List[str]]** | Exported routes indexed by peer address. | 

## Example

```python
from oxide.models.bgp_exported import BgpExported

# TODO update the JSON string below
json = "{}"
# create an instance of BgpExported from a JSON string
bgp_exported_instance = BgpExported.from_json(json)
# print the JSON string representation of the object
print(BgpExported.to_json())

# convert the object into a dict
bgp_exported_dict = bgp_exported_instance.to_dict()
# create an instance of BgpExported from a dict
bgp_exported_from_dict = BgpExported.from_dict(bgp_exported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


