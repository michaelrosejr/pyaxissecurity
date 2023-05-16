from __future__ import print_function

import logging

from dotenv import dotenv_values

import pyaxissecurity
from pyaxissecurity.rest import ApiException

logging.basicConfig(level=logging.DEBUG)
config = dotenv_values(".env")

# TODO Delete this...
# print(f"AXIS_API_TOKEN: {config['AXIS_API_TOKEN']}")

# Configure API key authorization: OAuthBearerToken
configuration = pyaxissecurity.Configuration()
configuration.api_key['Authorization'] = config['AXIS_API_TOKEN']
configuration.api_key_prefix['Authorization'] = 'Bearer '


def getGroups():
    api_instance = pyaxissecurity.GroupsApi(pyaxissecurity.ApiClient(configuration))
    page_number = 1  # int |  (optional)
    page_size = 100  # int |  (optional)

    try:
        # Get Group List
        api_response = api_instance.groups_query(page_number=page_number, page_size=page_size)
        logging.debug(api_response)
        return api_response
    except ApiException as e:
        logging.error("Exception when calling GroupsApi->groups_query: %s\n" % e)


def getUsers():
    api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
    page_number = 1  # int |  (optional)
    page_size = 100  # int |  (optional)

    try:
        # Get Users
        api_response = api_instance.users_query(page_number=page_number, page_size=page_size)
        logging.debug(api_response)
        return api_response
    except ApiException as e:
        logging.error("Exception when calling UsersApi->users_create: %s\n" % e)


def getUserById(userId):
    api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))

    try:
        # Get User by ID
        api_response = api_instance.users_get_by_id(userId)
        logging.debug(api_response)
        return api_response
    except ApiException as e:
        logging.error("Exception when calling UsersApi->users_get_by_id: %s\n" % e)


def getUserByEmail(email):
    api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
    page_number = 1  # int |  (optional)
    page_size = 100  # int |  (optional)

    try:
        # Get User by Email
        api_response = api_instance.users_query(page_number=page_number, page_size=page_size)
        users = api_response.data  # type: ignore
        user = next((user for user in users if user.email == email), None)
        logging.debug(user)
        return user
    except ApiException as e:
        logging.error("Exception when calling UsersApi->users_get_by_email: %s\n" % e)


def getConnectors():
    api_instance = pyaxissecurity.ConnectorsApi(pyaxissecurity.ApiClient(configuration))
    page_number = 1  # int |  (optional)
    page_size = 100  # int |  (optional)

    try:
        # Create a New Connector
        api_response = api_instance.connectors_query(page_number=page_number, page_size=page_size)
        logging.debug(api_response)
        return api_response
    except ApiException as e:
        logging.error("Exception when calling ConnectorsApi->connectors_create: %s\n" % e)


def usersCreate(user_data):
    api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))
    print(f"type: {type(user_data)}")
    user_model = pyaxissecurity.UserModelV1(**user_data)
    print(f"USERMODEL: {user_model}")
    try:
        # Create a New User
        api_response = api_instance.users_create(user_model)
        logging.debug(api_response)
        return api_response
    except ApiException as e:
        logging.error("Exception when calling UsersApi->users_create: %s\n" % e)


def userDelete(userId):
    api_instance = pyaxissecurity.UsersApi(pyaxissecurity.ApiClient(configuration))

    try:
        # Delete a User
        api_response = api_instance.users_delete(userId)
        logging.debug(api_response)
        return api_response
    except ApiException as e:
        logging.error("Exception when calling UsersApi->users_delete: %s\n" % e)


if __name__ == "__main__":
    # users = getUsers()
    # users_by_id = getUserById("a-users-id")
    # user = getUserByEmail("some.person@hpe.com")
    # groups = getGroups()
    # connectors = getConnectors()
    # me = getUserByEmail("michael.rose@hpe.com")
    # print(me)
    user_data = {
        'email': 'michael.rose.jr@hpe.com',
        'user_name': 'MichaelRosetest4',
        'first_name': 'MichaelTest3',
        'last_name': 'RoseTest1',
        'enabled': True,
        'expiration': None,
        'groups': [{'id': 'ca3a136c-5add-41da-9f4a-664f5523db1d', 'value': 'ASSET Team'}]
    }

    # print(user_data)
    # print(usersCreate(user_data))
    # print(getUserByEmail("michael.rose.jr@hpe.com"))
    # print(getUserByEmail("mrosejr@hpe.com"))
    print(getUserByEmail("michael.rose@hpe.com"))
