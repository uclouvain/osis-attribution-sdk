# osis_attribution_sdk.ApplicationApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/attribution*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_create**](ApplicationApi.md#application_create) | **POST** /application/ | 
[**application_delete**](ApplicationApi.md#application_delete) | **DELETE** /application/{application_uuid}/ | 
[**application_list**](ApplicationApi.md#application_list) | **GET** /application/ | 
[**application_update**](ApplicationApi.md#application_update) | **PUT** /application/{application_uuid}/ | 
[**applicationcoursescalendars_list**](ApplicationApi.md#applicationcoursescalendars_list) | **GET** /application/calendars | 
[**applications_summary_send**](ApplicationApi.md#applications_summary_send) | **POST** /application/send_summary | 
[**attributionsabouttoexpire_list**](ApplicationApi.md#attributionsabouttoexpire_list) | **GET** /application/renewal | 
[**attributionsabouttoexpire_renew**](ApplicationApi.md#attributionsabouttoexpire_renew) | **POST** /application/renewal | 
[**my_charge_summary**](ApplicationApi.md#my_charge_summary) | **GET** /application/my_charges | 
[**vacantcourses_list**](ApplicationApi.md#vacantcourses_list) | **GET** /application/vacant_courses | 


# **application_create**
> ApplicationCreateCommand application_create(application_create_command)



Create an application on the current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.application_create_command import ApplicationCreateCommand
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
    api_instance = application_api.ApplicationApi(api_client)
    application_create_command = ApplicationCreateCommand(
        code="Candidature aux cours vacants",
        lecturing_volume="10.0",
        practical_volume="15.0",
        remark="remark_example",
        course_summary="course_summary_example",
    ) # ApplicationCreateCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.application_create(application_create_command)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.application_create(application_create_command, accept_language=accept_language)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_create_command** | [**ApplicationCreateCommand**](ApplicationCreateCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**ApplicationCreateCommand**](ApplicationCreateCommand.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_delete**
> application_delete(application_uuid)



Delete an application on the current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
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
    api_instance = application_api.ApplicationApi(api_client)
    application_uuid = "application_uuid_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.application_delete(application_uuid)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.application_delete(application_uuid, accept_language=accept_language)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_list**
> ApplicationList application_list()



Return all applications of connected user of the current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.application_list import ApplicationList
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
    api_instance = application_api.ApplicationApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.application_list(accept_language=accept_language)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**ApplicationList**](ApplicationList.md)

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

# **application_update**
> ApplicationUpdateCommand application_update(application_uuid, application_update_command)



Update an application on the current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.application_update_command import ApplicationUpdateCommand
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
    api_instance = application_api.ApplicationApi(api_client)
    application_uuid = "application_uuid_example" # str | 
    application_update_command = ApplicationUpdateCommand(
        lecturing_volume="10.0",
        practical_volume="15.0",
        remark="remark_example",
        course_summary="course_summary_example",
    ) # ApplicationUpdateCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.application_update(application_uuid, application_update_command)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.application_update(application_uuid, application_update_command, accept_language=accept_language)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->application_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_uuid** | **str**|  |
 **application_update_command** | [**ApplicationUpdateCommand**](ApplicationUpdateCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**ApplicationUpdateCommand**](ApplicationUpdateCommand.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applicationcoursescalendars_list**
> [ApplicationCourseCalendar] applicationcoursescalendars_list()



Return all calendars related to application courses.

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.application_course_calendar import ApplicationCourseCalendar
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
    api_instance = application_api.ApplicationApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.applicationcoursescalendars_list(accept_language=accept_language)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->applicationcoursescalendars_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**[ApplicationCourseCalendar]**](ApplicationCourseCalendar.md)

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

# **applications_summary_send**
> applications_summary_send()



Send an applications summary on the current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
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
    api_instance = application_api.ApplicationApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.applications_summary_send(accept_language=accept_language)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->applications_summary_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The summary email has been sent |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attributionsabouttoexpire_list**
> AttributionAboutToExpireList attributionsabouttoexpire_list()



Get all attributions about to expire during current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.attribution_about_to_expire_list import AttributionAboutToExpireList
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
    api_instance = application_api.ApplicationApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attributionsabouttoexpire_list(accept_language=accept_language)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->attributionsabouttoexpire_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**AttributionAboutToExpireList**](AttributionAboutToExpireList.md)

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

# **attributionsabouttoexpire_renew**
> attributionsabouttoexpire_renew(renew_attribution_about_to_expire_command)



 Renew multiple attributions about to expire application during current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.renew_attribution_about_to_expire_command import RenewAttributionAboutToExpireCommand
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
    api_instance = application_api.ApplicationApi(api_client)
    renew_attribution_about_to_expire_command = RenewAttributionAboutToExpireCommand(
        codes=[
            "codes_example",
        ],
    ) # RenewAttributionAboutToExpireCommand | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.attributionsabouttoexpire_renew(renew_attribution_about_to_expire_command)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->attributionsabouttoexpire_renew: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.attributionsabouttoexpire_renew(renew_attribution_about_to_expire_command, accept_language=accept_language)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->attributionsabouttoexpire_renew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **renew_attribution_about_to_expire_command** | [**RenewAttributionAboutToExpireCommand**](RenewAttributionAboutToExpireCommand.md)|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_charge_summary**
> MyChargeSummaryList my_charge_summary()



Return charge summary of connected user of the current application period

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.my_charge_summary_list import MyChargeSummaryList
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
    api_instance = application_api.ApplicationApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.my_charge_summary(accept_language=accept_language)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->my_charge_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]

### Return type

[**MyChargeSummaryList**](MyChargeSummaryList.md)

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

# **vacantcourses_list**
> VacantCourseList vacantcourses_list()



Return vacant courses available filtered by criteria

### Example

* Api Key Authentication (Token):
```python
import time
import osis_attribution_sdk
from osis_attribution_sdk.api import application_api
from osis_attribution_sdk.model.error import Error
from osis_attribution_sdk.model.vacant_course_list import VacantCourseList
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
    api_instance = application_api.ApplicationApi(api_client)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    code = "code_example" # str |  (optional)
    allocation_faculty = "allocation_faculty_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.vacantcourses_list(accept_language=accept_language, code=code, allocation_faculty=allocation_faculty)
        pprint(api_response)
    except osis_attribution_sdk.ApiException as e:
        print("Exception when calling ApplicationApi->vacantcourses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **code** | **str**|  | [optional]
 **allocation_faculty** | **str**|  | [optional]

### Return type

[**VacantCourseList**](VacantCourseList.md)

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

