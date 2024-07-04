
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `test_header` | `str` | This is a test header<br>*Default*: `'TestHeaderDefaultValue'` |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `api_key_credentials` | [`ApiKeyCredentials`]($a/custom-header-signature.md) | The credential object for Custom Header Signature |
| `http_basic_credentials` | [`HttpBasicCredentials`]($a/basic-authentication.md) | The credential object for Basic Authentication |
| `petstore_auth_credentials` | [`PetstoreAuthCredentials`]($a/oauth-2-implicit-grant.md) | The credential object for OAuth 2 Implicit Grant |

The API client can be initialized as follows:

```python
client = SwaggerpetstoreClient(
    test_header='TestHeaderDefaultValue',
    api_key_credentials=ApiKeyCredentials(
        api_key='api_key'
    ),
    http_basic_credentials=HttpBasicCredentials(
        username='username',
        passwprd='passwprd'
    ),
    petstore_auth_credentials=PetstoreAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_redirect_uri='OAuthRedirectUri',
        o_auth_scopes=[
            OAuthScopePetstoreAuthEnum.READPETS,
            OAuthScopePetstoreAuthEnum.WRITEPETS
        ]
    )
)
```

## Swagger Petstore Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| pet | Gets PetController |
| store | Gets StoreController |
| user | Gets UserController |

