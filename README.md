# pyaxissecurity

## Requirements.

certifi >= 14.05.14
six >= 1.10
python_dateutil >= 2.5.3
setuptools >= 21.0.0
urllib3 >= 1.15.1

## Installation & Usage

### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:

```python
import swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: OAuthBearerToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApplicationGroupsApi(swagger_client.ApiClient(configuration))
application_group_model = swagger_client.ApplicationGroupModelV1() # ApplicationGroupModelV1 |

try:
    # Create a New Application Group
    api_instance.application_groups_create(application_group_model)
except ApiException as e:
    print("Exception when calling ApplicationGroupsApi->application_groups_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://admin-api.axissecurity.com*

| Class                  | Method                                                                                        | HTTP request                                  | Description                                                  |
| ---------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| _ApplicationGroupsApi_ | [**application_groups_create**](docs/ApplicationGroupsApi.md#application_groups_create)       | **POST** /api/v1.0/tags                       | Create a New Application Group                               |
| _ApplicationGroupsApi_ | [**application_groups_delete**](docs/ApplicationGroupsApi.md#application_groups_delete)       | **DELETE** /api/v1.0/tags/{id}                | Delete Application Group by ID                               |
| _ApplicationGroupsApi_ | [**application_groups_get_by_id**](docs/ApplicationGroupsApi.md#application_groups_get_by_id) | **GET** /api/v1.0/tags/{id}                   | Get Application Group by ID                                  |
| _ApplicationGroupsApi_ | [**application_groups_query**](docs/ApplicationGroupsApi.md#application_groups_query)         | **GET** /api/v1.0/tags                        | Get Application Groups                                       |
| _ApplicationGroupsApi_ | [**application_groups_update**](docs/ApplicationGroupsApi.md#application_groups_update)       | **PUT** /api/v1.0/tags/{id}                   | Update an Existing Application Group                         |
| _ApplicationsApi_      | [**applications_create**](docs/ApplicationsApi.md#applications_create)                        | **POST** /api/v1.0/Applications               | Create a New Application                                     |
| _ApplicationsApi_      | [**applications_delete**](docs/ApplicationsApi.md#applications_delete)                        | **DELETE** /api/v1.0/Applications/{id}        | Delete Application by ID                                     |
| _ApplicationsApi_      | [**applications_get_by_id**](docs/ApplicationsApi.md#applications_get_by_id)                  | **GET** /api/v1.0/Applications/{id}           | Get Application by ID                                        |
| _ApplicationsApi_      | [**applications_query**](docs/ApplicationsApi.md#applications_query)                          | **GET** /api/v1.0/Applications                | Get Applications                                             |
| _ApplicationsApi_      | [**applications_update**](docs/ApplicationsApi.md#applications_update)                        | **PUT** /api/v1.0/Applications/{id}           | Update an Existing Application                               |
| _CommitApi_            | [**commit_commit_changes**](docs/CommitApi.md#commit_commit_changes)                          | **POST** /api/v1.0/Commit                     | Commit Changes                                               |
| _ConnectorZonesApi_    | [**connector_zones_create**](docs/ConnectorZonesApi.md#connector_zones_create)                | **POST** /api/v1.0/ConnectorZones             | Create a New Connector Zone                                  |
| _ConnectorZonesApi_    | [**connector_zones_delete**](docs/ConnectorZonesApi.md#connector_zones_delete)                | **DELETE** /api/v1.0/ConnectorZones/{id}      | Delete Connector Zone by ID                                  |
| _ConnectorZonesApi_    | [**connector_zones_get_by_id**](docs/ConnectorZonesApi.md#connector_zones_get_by_id)          | **GET** /api/v1.0/ConnectorZones/{id}         | Get Connector Zone by ID                                     |
| _ConnectorZonesApi_    | [**connector_zones_query**](docs/ConnectorZonesApi.md#connector_zones_query)                  | **GET** /api/v1.0/ConnectorZones              | Get Connector Zones                                          |
| _ConnectorZonesApi_    | [**connector_zones_update**](docs/ConnectorZonesApi.md#connector_zones_update)                | **PUT** /api/v1.0/ConnectorZones/{id}         | Update an Existing Connector Zone                            |
| _ConnectorsApi_        | [**connectors_create**](docs/ConnectorsApi.md#connectors_create)                              | **POST** /api/v1.0/Connectors                 | Create a New Connector                                       |
| _ConnectorsApi_        | [**connectors_delete**](docs/ConnectorsApi.md#connectors_delete)                              | **DELETE** /api/v1.0/Connectors/{id}          | Delete Connector by ID                                       |
| _ConnectorsApi_        | [**connectors_get_by_id**](docs/ConnectorsApi.md#connectors_get_by_id)                        | **GET** /api/v1.0/Connectors/{id}             | Get Connector by ID                                          |
| _ConnectorsApi_        | [**connectors_query**](docs/ConnectorsApi.md#connectors_query)                                | **GET** /api/v1.0/Connectors                  | Get Connectors                                               |
| _ConnectorsApi_        | [**connectors_regenerate**](docs/ConnectorsApi.md#connectors_regenerate)                      | **POST** /api/v1.0/Connectors/{id}/regenerate | Regenerate an Installation Command for an Exisitng Connector |
| _ConnectorsApi_        | [**connectors_status**](docs/ConnectorsApi.md#connectors_status)                              | **GET** /api/v1.0/Connectors/{id}/status      | Get the Status of a Connector                                |
| _ConnectorsApi_        | [**connectors_update**](docs/ConnectorsApi.md#connectors_update)                              | **PUT** /api/v1.0/Connectors/{id}             | Update an Existing Connector                                 |
| _GroupsApi_            | [**groups_create**](docs/GroupsApi.md#groups_create)                                          | **POST** /api/v1.0/Groups                     | Create a New Group                                           |
| _GroupsApi_            | [**groups_delete**](docs/GroupsApi.md#groups_delete)                                          | **DELETE** /api/v1.0/Groups/{id}              | Delete Group by ID                                           |
| _GroupsApi_            | [**groups_get_by_id**](docs/GroupsApi.md#groups_get_by_id)                                    | **GET** /api/v1.0/Groups/{id}                 | Get Group by ID                                              |
| _GroupsApi_            | [**groups_query**](docs/GroupsApi.md#groups_query)                                            | **GET** /api/v1.0/Groups                      | Get Groups                                                   |
| _GroupsApi_            | [**groups_update**](docs/GroupsApi.md#groups_update)                                          | **PUT** /api/v1.0/Groups/{id}                 | Update an Existing Group                                     |
| _SslExclusionsApi_     | [**ssl_exclusions_create**](docs/SslExclusionsApi.md#ssl_exclusions_create)                   | **POST** /api/v1.0/SslExclusions              | Create a New SSL Exclusion                                   |
| _SslExclusionsApi_     | [**ssl_exclusions_delete**](docs/SslExclusionsApi.md#ssl_exclusions_delete)                   | **DELETE** /api/v1.0/SslExclusions/{id}       | Delete SSL Exclusion by ID                                   |
| _SslExclusionsApi_     | [**ssl_exclusions_get_by_id**](docs/SslExclusionsApi.md#ssl_exclusions_get_by_id)             | **GET** /api/v1.0/SslExclusions/{id}          | Get SSL Exclusion by ID                                      |
| _SslExclusionsApi_     | [**ssl_exclusions_query**](docs/SslExclusionsApi.md#ssl_exclusions_query)                     | **GET** /api/v1.0/SslExclusions               | Get SSL Exclusions                                           |
| _SslExclusionsApi_     | [**ssl_exclusions_update**](docs/SslExclusionsApi.md#ssl_exclusions_update)                   | **PUT** /api/v1.0/SslExclusions/{id}          | Update an Existing SSL Exclusion                             |
| _SwgCategoryApi_       | [**swg_category_create**](docs/SwgCategoryApi.md#swg_category_create)                         | **POST** /api/v1.0/webcategories              | Create a New Web Category                                    |
| _SwgCategoryApi_       | [**swg_category_delete**](docs/SwgCategoryApi.md#swg_category_delete)                         | **DELETE** /api/v1.0/webcategories/{id}       | Delete Web Category by ID                                    |
| _SwgCategoryApi_       | [**swg_category_get_by_id**](docs/SwgCategoryApi.md#swg_category_get_by_id)                   | **GET** /api/v1.0/webcategories/{id}          | Get Web Category by ID                                       |
| _SwgCategoryApi_       | [**swg_category_query**](docs/SwgCategoryApi.md#swg_category_query)                           | **GET** /api/v1.0/webcategories               | Get Web Categories                                           |
| _SwgCategoryApi_       | [**swg_category_update**](docs/SwgCategoryApi.md#swg_category_update)                         | **PUT** /api/v1.0/webcategories/{id}          | Update an Existing Web Category                              |
| _UsersApi_             | [**users_create**](docs/UsersApi.md#users_create)                                             | **POST** /api/v1.0/Users                      | Create a New User                                            |
| _UsersApi_             | [**users_delete**](docs/UsersApi.md#users_delete)                                             | **DELETE** /api/v1.0/Users/{id}               | Delete User by ID                                            |
| _UsersApi_             | [**users_get_by_id**](docs/UsersApi.md#users_get_by_id)                                       | **GET** /api/v1.0/Users/{id}                  | Get User by ID                                               |
| _UsersApi_             | [**users_query**](docs/UsersApi.md#users_query)                                               | **GET** /api/v1.0/Users                       | Get Users                                                    |
| _UsersApi_             | [**users_update**](docs/UsersApi.md#users_update)                                             | **PUT** /api/v1.0/Users/{id}                  | Update an Existing User                                      |

## Documentation For Models

- [ApplicationGroupModelV1](docs/ApplicationGroupModelV1.md)
- [ApplicationModelType](docs/ApplicationModelType.md)
- [ApplicationModelV1](docs/ApplicationModelV1.md)
- [ApplicationModelV1Type](docs/ApplicationModelV1Type.md)
- [ConnectorCreateResponseModelV1](docs/ConnectorCreateResponseModelV1.md)
- [ConnectorModelV1](docs/ConnectorModelV1.md)
- [ConnectorRegenerateResponseModelV1](docs/ConnectorRegenerateResponseModelV1.md)
- [ConnectorStatus](docs/ConnectorStatus.md)
- [ConnectorStatusResponseModelV1](docs/ConnectorStatusResponseModelV1.md)
- [ConnectorZoneModelV1](docs/ConnectorZoneModelV1.md)
- [ConnectorZonePurpose](docs/ConnectorZonePurpose.md)
- [ConnectorZoneType](docs/ConnectorZoneType.md)
- [DescriptionNamedModelBase](docs/DescriptionNamedModelBase.md)
- [GroupModelV1](docs/GroupModelV1.md)
- [HttpStatusCode](docs/HttpStatusCode.md)
- [ModelBase](docs/ModelBase.md)
- [NamedModelBase](docs/NamedModelBase.md)
- [NetworkRangeApplicationDataModelV1](docs/NetworkRangeApplicationDataModelV1.md)
- [PagedApiResponseOfIEnumerableOfConnectorModelV1](docs/PagedApiResponseOfIEnumerableOfConnectorModelV1.md)
- [PagedApiResponseOfIEnumerableOfConnectorZoneModelV1](docs/PagedApiResponseOfIEnumerableOfConnectorZoneModelV1.md)
- [PagedApiResponseOfIEnumerableOfGroupModelV1](docs/PagedApiResponseOfIEnumerableOfGroupModelV1.md)
- [PagedApiResponseOfIEnumerableOfSslExclusionModelV1](docs/PagedApiResponseOfIEnumerableOfSslExclusionModelV1.md)
- [PagedApiResponseOfIEnumerableOfSwgCategoryModelV1](docs/PagedApiResponseOfIEnumerableOfSwgCategoryModelV1.md)
- [PagedApiResponseOfIEnumerableOfUserModelV1](docs/PagedApiResponseOfIEnumerableOfUserModelV1.md)
- [PublicAdminApiError](docs/PublicAdminApiError.md)
- [SlimModelV1](docs/SlimModelV1.md)
- [SslExclusionModelV1](docs/SslExclusionModelV1.md)
- [SslExclusionType](docs/SslExclusionType.md)
- [SwgCategoryModelV1](docs/SwgCategoryModelV1.md)
- [SwgCategoryType](docs/SwgCategoryType.md)
- [UserModelV1](docs/UserModelV1.md)

## Documentation For Authorization

## OAuthBearerToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## Author

# pyaxissecurity
