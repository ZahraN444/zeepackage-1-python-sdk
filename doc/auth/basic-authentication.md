
# Basic Authentication



Documentation for accessing and setting credentials for httpBasic.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| username | `str` | - | `username` |
| passwprd | `str` | - | `passwprd` |



**Note:** Auth credentials can be set using `HttpBasicCredentials` object, passed in as named parameter `http_basic_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = SwaggerpetstoreClient(
    http_basic_credentials=HttpBasicCredentials(
        username='username',
        passwprd='passwprd'
    )
)
```


