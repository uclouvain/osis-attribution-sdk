# openapi_client.ApplicationApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/attribution*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationcoursescalendars_list**](ApplicationApi.md#applicationcoursescalendars_list) | **GET** /application/calendars | 


# **applicationcoursescalendars_list**
> list[ApplicationCourseCalendar] applicationcoursescalendars_list()



Return all calendars related to application courses.

### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/attribution
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/attribution"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApplicationApi(api_client)
    
    try:
        api_response = api_instance.applicationcoursescalendars_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi->applicationcoursescalendars_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApplicationCourseCalendar]**](ApplicationCourseCalendar.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

