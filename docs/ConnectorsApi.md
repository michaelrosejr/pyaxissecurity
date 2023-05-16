# pyaxissecurity.ConnectorsApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectors_create**](ConnectorsApi.md#connectors_create) | **POST** /api/v1.0/Connectors | Create a New Connector
[**connectors_delete**](ConnectorsApi.md#connectors_delete) | **DELETE** /api/v1.0/Connectors/{id} | Delete Connector by ID
[**connectors_get_by_id**](ConnectorsApi.md#connectors_get_by_id) | **GET** /api/v1.0/Connectors/{id} | Get Connector by ID
[**connectors_query**](ConnectorsApi.md#connectors_query) | **GET** /api/v1.0/Connectors | Get Connectors
[**connectors_regenerate**](ConnectorsApi.md#connectors_regenerate) | **POST** /api/v1.0/Connectors/{id}/regenerate | Regenerate an Installation Command for an Exisitng Connector
[**connectors_status**](ConnectorsApi.md#connectors_status) | **GET** /api/v1.0/Connectors/{id}/status | Get the Status of a Connector
[**connectors_update**](ConnectorsApi.md#connectors_update) | **PUT** /api/v1.0/Connectors/{id} | Update an Existing Connector


# **connectors_create**
> ConnectorCreateResponseModelV1 connectors_create(connector_model)

Create a New Connector

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
connector_model = pyaxissecurity.ConnectorModelV1() # ConnectorModelV1 | 

try:
    # Create a New Connector
    api_response = api_instance.connectors_create(connector_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_model** | [**ConnectorModelV1**](ConnectorModelV1.md)|  | 

### Return type

[**ConnectorCreateResponseModelV1**](ConnectorCreateResponseModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_delete**
> connectors_delete(id)

Delete Connector by ID

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Connector by ID
    api_instance.connectors_delete(id)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_delete: %s\n" % e)
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

# **connectors_get_by_id**
> ConnectorModelV1 connectors_get_by_id(id)

Get Connector by ID

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Connector by ID
    api_response = api_instance.connectors_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConnectorModelV1**](ConnectorModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_query**
> PagedApiResponseOfIEnumerableOfConnectorModelV1 connectors_query(page_number=page_number, page_size=page_size)

Get Connectors

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Connectors
    api_response = api_instance.connectors_query(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PagedApiResponseOfIEnumerableOfConnectorModelV1**](PagedApiResponseOfIEnumerableOfConnectorModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_regenerate**
> ConnectorRegenerateResponseModelV1 connectors_regenerate(id)

Regenerate an Installation Command for an Exisitng Connector

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Regenerate an Installation Command for an Exisitng Connector
    api_response = api_instance.connectors_regenerate(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_regenerate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConnectorRegenerateResponseModelV1**](ConnectorRegenerateResponseModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_status**
> ConnectorStatusResponseModelV1 connectors_status(id)

Get the Status of a Connector

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get the Status of a Connector
    api_response = api_instance.connectors_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConnectorStatusResponseModelV1**](ConnectorStatusResponseModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_update**
> ConnectorModelV1 connectors_update(id, connector_model)

Update an Existing Connector

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
api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
connector_model = pyaxissecurity.ConnectorModelV1() # ConnectorModelV1 | 

try:
    # Update an Existing Connector
    api_response = api_instance.connectors_update(id, connector_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->connectors_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **connector_model** | [**ConnectorModelV1**](ConnectorModelV1.md)|  | 

### Return type

[**ConnectorModelV1**](ConnectorModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

