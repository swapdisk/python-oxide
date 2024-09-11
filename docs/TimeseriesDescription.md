# TimeseriesDescription

Text descriptions for the target and metric of a timeseries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**target** | **str** |  | 

## Example

```python
from oxide.models.timeseries_description import TimeseriesDescription

# TODO update the JSON string below
json = "{}"
# create an instance of TimeseriesDescription from a JSON string
timeseries_description_instance = TimeseriesDescription.from_json(json)
# print the JSON string representation of the object
print(TimeseriesDescription.to_json())

# convert the object into a dict
timeseries_description_dict = timeseries_description_instance.to_dict()
# create an instance of TimeseriesDescription from a dict
timeseries_description_from_dict = TimeseriesDescription.from_dict(timeseries_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


