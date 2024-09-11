# Quantile

Structure for estimating the p-quantile of a population.  This is based on the P² algorithm for estimating quantiles using constant space.  The algorithm consists of maintaining five markers: the minimum, the p/2-, p-, and (1 + p)/2 quantiles, and the maximum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_marker_positions** | **List[float]** | The desired marker positions. | 
**marker_heights** | **List[float]** | The heights of the markers. | 
**marker_positions** | **List[int]** | The positions of the markers.  We track sample size in the 5th position, as useful observations won&#39;t start until we&#39;ve filled the heights at the 6th sample anyway This does deviate from the paper, but it&#39;s a more useful representation that works according to the paper&#39;s algorithm. | 
**p** | **float** | The p value for the quantile. | 

## Example

```python
from oxide.models.quantile import Quantile

# TODO update the JSON string below
json = "{}"
# create an instance of Quantile from a JSON string
quantile_instance = Quantile.from_json(json)
# print the JSON string representation of the object
print(Quantile.to_json())

# convert the object into a dict
quantile_dict = quantile_instance.to_dict()
# create an instance of Quantile from a dict
quantile_from_dict = Quantile.from_dict(quantile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


