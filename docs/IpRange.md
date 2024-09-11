# IpRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | 
**last** | **str** |  | 

## Example

```python
from oxide.models.ip_range import IpRange

# TODO update the JSON string below
json = "{}"
# create an instance of IpRange from a JSON string
ip_range_instance = IpRange.from_json(json)
# print the JSON string representation of the object
print(IpRange.to_json())

# convert the object into a dict
ip_range_dict = ip_range_instance.to_dict()
# create an instance of IpRange from a dict
ip_range_from_dict = IpRange.from_dict(ip_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


