# osis_attribution_sdk.AttributionApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/attribution*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributions_list**](AttributionApi.md#attributions_list) | **GET** /{year}/{global_id}/ | 
[**myattributions_list**](AttributionApi.md#myattributions_list) | **GET** /{year}/me | 


# **attributions_list**
> [Attribution] attributions_list(year, global_id)



Return all attributions of specific user in a specific year.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import attribution_api
from osis_attribution_sdk.model.attribution import Attribution
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/attribution
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_attribution_sdk.Configuration(
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
with osis_attribution_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attribution_api.AttributionApi(api_client)
    year = "year_example" # str | 
    global_id = "global_id_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    with_classes = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attributions_list(year, global_id)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling AttributionApi->attributions_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attributions_list(year, global_id, accept_language=accept_language, with_classes=with_classes)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling AttributionApi->attributions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **global_id** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **with_classes** | **bool**|  | [optional]

### Return type

[**[Attribution]**](Attribution.md)

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

# **myattributions_list**
> [Attribution] myattributions_list(year)



Return all attributions of connected user in a specific year.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import attribution_api
from osis_attribution_sdk.model.attribution import Attribution
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/attribution
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_attribution_sdk.Configuration(
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
with osis_attribution_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attribution_api.AttributionApi(api_client)
    year = "year_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    with_classes = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.myattributions_list(year)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling AttributionApi->myattributions_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.myattributions_list(year, accept_language=accept_language, with_classes=with_classes)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling AttributionApi->myattributions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **with_classes** | **bool**|  | [optional]

### Return type

[**[Attribution]**](Attribution.md)

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

