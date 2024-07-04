# User

Operations about user

Find out more about our store: [http://swagger.io](http://swagger.io)

```python
user_controller = client.user
```

## Class Name

`UserController`

## Methods

* [Create Users With Array Input](../../doc/controllers/user.md#create-users-with-array-input)
* [Update User](../../doc/controllers/user.md#update-user)
* [Create Users With List Input](../../doc/controllers/user.md#create-users-with-list-input)
* [Logout User](../../doc/controllers/user.md#logout-user)
* [Login User](../../doc/controllers/user.md#login-user)
* [Get User by Name](../../doc/controllers/user.md#get-user-by-name)
* [Create User](../../doc/controllers/user.md#create-user)
* [Delete User](../../doc/controllers/user.md#delete-user)


# Create Users With Array Input

Creates list of users with given input array

:information_source: **Note** This endpoint does not require authentication.

```python
def create_users_with_array_input(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[User]`](../../doc/models/user.md) | Body, Required | List of user object |

## Response Type

`void`

## Example Usage

```python
body = [
    User()
]

result = user_controller.create_users_with_array_input(body)
print(result)
```


# Update User

This can only be done by the logged in user.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_user(self,
               username,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | name that need to be updated |
| `body` | [`UserRequest`](../../doc/models/user-request.md) | Body, Required | Updated user object |

## Response Type

`void`

## Example Usage

```python
username = 'username0'

body = UserRequest()

result = user_controller.update_user(
    username,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid user supplied | `APIException` |
| 404 | User not found | `APIException` |


# Create Users With List Input

Creates list of users with given input array

:information_source: **Note** This endpoint does not require authentication.

```python
def create_users_with_list_input(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List[User]`](../../doc/models/user.md) | Body, Required | List of user object |

## Response Type

`void`

## Example Usage

```python
body = [
    User()
]

result = user_controller.create_users_with_list_input(body)
print(result)
```


# Logout User

Logs out current logged in user session

:information_source: **Note** This endpoint does not require authentication.

```python
def logout_user(self)
```

## Response Type

`void`

## Example Usage

```python
result = user_controller.logout_user()
print(result)
```


# Login User

Logs user into the system

:information_source: **Note** This endpoint does not require authentication.

```python
def login_user(self,
              username,
              password)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Query, Required | The user name for login |
| `password` | `str` | Query, Required | The password for login in clear text |

## Response Type

`str`

## Example Usage

```python
username = 'username0'

password = 'password4'

result = user_controller.login_user(
    username,
    password
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username/password supplied | `APIException` |


# Get User by Name

Get user by user name

:information_source: **Note** This endpoint does not require authentication.

```python
def get_user_by_name(self,
                    username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | The name that needs to be fetched. Use user1 for testing. |

## Response Type

[`User`](../../doc/models/user.md)

## Example Usage

```python
username = 'username0'

result = user_controller.get_user_by_name(username)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username supplied | `APIException` |
| 404 | User not found | `APIException` |


# Create User

This can only be done by the logged in user.

:information_source: **Note** This endpoint does not require authentication.

```python
def create_user(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UserRequest`](../../doc/models/user-request.md) | Body, Required | Created user object |

## Response Type

`void`

## Example Usage

```python
body = UserRequest()

result = user_controller.create_user(body)
print(result)
```


# Delete User

This can only be done by the logged in user.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_user(self,
               username)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `str` | Template, Required | The name that needs to be deleted |

## Response Type

`void`

## Example Usage

```python
username = 'username0'

result = user_controller.delete_user(username)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid username supplied | `APIException` |
| 404 | User not found | `APIException` |

