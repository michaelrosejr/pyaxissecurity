# pyaxissecurity.GroupsApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_create**](GroupsApi.md#groups_create) | **POST** /api/v1.0/Groups | Create a New Group
[**groups_delete**](GroupsApi.md#groups_delete) | **DELETE** /api/v1.0/Groups/{id} | Delete Group by ID
[**groups_get_by_id**](GroupsApi.md#groups_get_by_id) | **GET** /api/v1.0/Groups/{id} | Get Group by ID
[**groups_query**](GroupsApi.md#groups_query) | **GET** /api/v1.0/Groups | Get Groups
[**groups_update**](GroupsApi.md#groups_update) | **PUT** /api/v1.0/Groups/{id} | Update an Existing Group


# **groups_create**
> GroupModelV1 groups_create(group_model)

Create a New Group

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.GroupsApi(pyaxissecurity.ApiClient(configuration))
group_model = pyaxissecurity.GroupModelV1() # GroupModelV1 | 

try:
    # Create a New Group
    api_response = api_instance.groups_create(group_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_model** | [**GroupModelV1**](GroupModelV1.md)|  | 

### Return type

[**GroupModelV1**](GroupModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_delete**
> groups_delete(id)

Delete Group by ID

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.GroupsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Group by ID
    api_instance.groups_delete(id)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_by_id**
> GroupModelV1 groups_get_by_id(id)

Get Group by ID

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.GroupsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Group by ID
    api_response = api_instance.groups_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupModelV1**](GroupModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_query**
> PagedApiResponseOfIEnumerableOfGroupModelV1 groups_query(page_number=page_number, page_size=page_size)

Get Groups

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.GroupsApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Groups
    api_response = api_instance.groups_query(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PagedApiResponseOfIEnumerableOfGroupModelV1**](PagedApiResponseOfIEnumerableOfGroupModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_update**
> GroupModelV1 groups_update(id, group_model)

Update an Existing Group

### Example
```python
from __future__ import print_function
import time
import pyaxissecurity
from pyaxissecurity.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = pyaxissecurity.GroupsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
group_model = pyaxissecurity.GroupModelV1() # GroupModelV1 | 

try:
    # Update an Existing Group
    api_response = api_instance.groups_update(id, group_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group_model** | [**GroupModelV1**](GroupModelV1.md)|  | 

### Return type

[**GroupModelV1**](GroupModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

