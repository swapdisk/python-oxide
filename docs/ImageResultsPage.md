# ImageResultsPage

A single page of results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Image]**](Image.md) | list of items on this page of results | 
**next_page** | **str** | token used to fetch the next page of results (if any) | [optional] 

## Example

```python
from oxide.models.image_results_page import ImageResultsPage

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResultsPage from a JSON string
image_results_page_instance = ImageResultsPage.from_json(json)
# print the JSON string representation of the object
print(ImageResultsPage.to_json())

# convert the object into a dict
image_results_page_dict = image_results_page_instance.to_dict()
# create an instance of ImageResultsPage from a dict
image_results_page_from_dict = ImageResultsPage.from_dict(image_results_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


