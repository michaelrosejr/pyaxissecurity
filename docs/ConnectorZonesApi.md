# pyaxissecurity.ConnectorZonesApi

All URIs are relative to *https://admin-api.axissecurity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connector_zones_create**](ConnectorZonesApi.md#connector_zones_create) | **POST** /api/v1.0/ConnectorZones | Create a New Connector Zone
[**connector_zones_delete**](ConnectorZonesApi.md#connector_zones_delete) | **DELETE** /api/v1.0/ConnectorZones/{id} | Delete Connector Zone by ID
[**connector_zones_get_by_id**](ConnectorZonesApi.md#connector_zones_get_by_id) | **GET** /api/v1.0/ConnectorZones/{id} | Get Connector Zone by ID
[**connector_zones_query**](ConnectorZonesApi.md#connector_zones_query) | **GET** /api/v1.0/ConnectorZones | Get Connector Zones
[**connector_zones_update**](ConnectorZonesApi.md#connector_zones_update) | **PUT** /api/v1.0/ConnectorZones/{id} | Update an Existing Connector Zone


# **connector_zones_create**
> ConnectorZoneModelV1 connector_zones_create(connector_zone_model)

Create a New Connector Zone

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
api_instance = pyaxissecurity.ConnectorZonesApi(pyaxissecurity.ApiClient(configuration))
connector_zone_model = pyaxissecurity.ConnectorZoneModelV1() # ConnectorZoneModelV1 | 

try:
    # Create a New Connector Zone
    api_response = api_instance.connector_zones_create(connector_zone_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorZonesApi->connector_zones_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_zone_model** | [**ConnectorZoneModelV1**](ConnectorZoneModelV1.md)|  | 

### Return type

[**ConnectorZoneModelV1**](ConnectorZoneModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_zones_delete**
> connector_zones_delete(id)

Delete Connector Zone by ID

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
api_instance = pyaxissecurity.ConnectorZonesApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Connector Zone by ID
    api_instance.connector_zones_delete(id)
except ApiException as e:
    print("Exception when calling ConnectorZonesApi->connector_zones_delete: %s\n" % e)
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

# **connector_zones_get_by_id**
> ConnectorZoneModelV1 connector_zones_get_by_id(id)

Get Connector Zone by ID

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
api_instance = pyaxissecurity.ConnectorZonesApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Connector Zone by ID
    api_response = api_instance.connector_zones_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorZonesApi->connector_zones_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConnectorZoneModelV1**](ConnectorZoneModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_zones_query**
> PagedApiResponseOfIEnumerableOfConnectorZoneModelV1 connector_zones_query(page_number=page_number, page_size=page_size)

Get Connector Zones

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
api_instance = pyaxissecurity.ConnectorZonesApi(pyaxissecurity.ApiClient(configuration))
page_number = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try:
    # Get Connector Zones
    api_response = api_instance.connector_zones_query(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorZonesApi->connector_zones_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**PagedApiResponseOfIEnumerableOfConnectorZoneModelV1**](PagedApiResponseOfIEnumerableOfConnectorZoneModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_zones_update**
> ConnectorZoneModelV1 connector_zones_update(id, connector_zone_model)

Update an Existing Connector Zone

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
api_instance = pyaxissecurity.ConnectorZonesApi(pyaxissecurity.ApiClient(configuration))
id = 'id_example' # str | 
connector_zone_model = pyaxissecurity.ConnectorZoneModelV1() # ConnectorZoneModelV1 | 

try:
    # Update an Existing Connector Zone
    api_response = api_instance.connector_zones_update(id, connector_zone_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorZonesApi->connector_zones_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **connector_zone_model** | [**ConnectorZoneModelV1**](ConnectorZoneModelV1.md)|  | 

### Return type

[**ConnectorZoneModelV1**](ConnectorZoneModelV1.md)

### Authorization

[OAuthBearerToken](../README.md#OAuthBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

