# Histogramuint32

Histogram metric  A histogram maintains the count of any number of samples, over a set of bins. Bins are specified on construction via their _left_ edges, inclusive. There can't be any \"gaps\" in the bins, and an additional bin may be added to the left, right, or both so that the bins extend to the entire range of the support.  Note that any gaps, unsorted bins, or non-finite values will result in an error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bins** | [**List[Binuint32]**](Binuint32.md) | The bins of the histogram. | 
**max** | **int** | The maximum value of all samples in the histogram. | 
**min** | **int** | The minimum value of all samples in the histogram. | 
**n_samples** | **int** | The total number of samples in the histogram. | 
**p50** | [**Quantile**](Quantile.md) | p50 Quantile | 
**p90** | [**Quantile**](Quantile.md) | p95 Quantile | 
**p99** | [**Quantile**](Quantile.md) | p99 Quantile | 
**squared_mean** | **float** | M2 for Welford&#39;s algorithm for variance calculation.  Read about [Welford&#39;s algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford&#39;s_online_algorithm) for more information on the algorithm. | 
**start_time** | **datetime** | The start time of the histogram. | 
**sum_of_samples** | **int** | The sum of all samples in the histogram. | 

## Example

```python
from oxide.models.histogramuint32 import Histogramuint32

# TODO update the JSON string below
json = "{}"
# create an instance of Histogramuint32 from a JSON string
histogramuint32_instance = Histogramuint32.from_json(json)
# print the JSON string representation of the object
print(Histogramuint32.to_json())

# convert the object into a dict
histogramuint32_dict = histogramuint32_instance.to_dict()
# create an instance of Histogramuint32 from a dict
histogramuint32_from_dict = Histogramuint32.from_dict(histogramuint32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


