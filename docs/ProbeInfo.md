# ProbeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ips** | [**List[ProbeExternalIp]**](ProbeExternalIp.md) |  | 
**id** | **str** |  | 
**interface** | [**NetworkInterface**](NetworkInterface.md) |  | 
**name** | **str** | Names must begin with a lower case ASCII letter, be composed exclusively of lowercase ASCII, uppercase ASCII, numbers, and &#39;-&#39;, and may not end with a &#39;-&#39;. Names cannot be a UUID, but they may contain a UUID. They can be at most 63 characters long. | 
**sled** | **str** |  | 

## Example

```python
from oxide.models.probe_info import ProbeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeInfo from a JSON string
probe_info_instance = ProbeInfo.from_json(json)
# print the JSON string representation of the object
print(ProbeInfo.to_json())

# convert the object into a dict
probe_info_dict = probe_info_instance.to_dict()
# create an instance of ProbeInfo from a dict
probe_info_from_dict = ProbeInfo.from_dict(probe_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


