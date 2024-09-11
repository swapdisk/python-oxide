# ProbeExternalIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_port** | **int** |  | 
**ip** | **str** |  | 
**kind** | [**ProbeExternalIpKind**](ProbeExternalIpKind.md) |  | 
**last_port** | **int** |  | 

## Example

```python
from oxide.models.probe_external_ip import ProbeExternalIp

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeExternalIp from a JSON string
probe_external_ip_instance = ProbeExternalIp.from_json(json)
# print the JSON string representation of the object
print(ProbeExternalIp.to_json())

# convert the object into a dict
probe_external_ip_dict = probe_external_ip_instance.to_dict()
# create an instance of ProbeExternalIp from a dict
probe_external_ip_from_dict = ProbeExternalIp.from_dict(probe_external_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


