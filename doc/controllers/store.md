# Store

Access to Petstore orders

```python
store_controller = client.store
```

## Class Name

`StoreController`

## Methods

* [Get Order by Id](../../doc/controllers/store.md#get-order-by-id)
* [Place Order](../../doc/controllers/store.md#place-order)
* [Get Inventory](../../doc/controllers/store.md#get-inventory)
* [Delete Order](../../doc/controllers/store.md#delete-order)


# Get Order by Id

For valid response try integer IDs with value >= 1 and <= 10. Other values will generated exceptions

:information_source: **Note** This endpoint does not require authentication.

```python
def get_order_by_id(self,
                   order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `long\|int` | Template, Required | ID of pet that needs to be fetched |

## Response Type

[`Order`](../../doc/models/order.md)

## Example Usage

```python
order_id = 62

result = store_controller.get_order_by_id(order_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `APIException` |
| 404 | Order not found | `APIException` |


# Place Order

Place an order for a pet

:information_source: **Note** This endpoint does not require authentication.

```python
def place_order(self,
               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoreOrderRequest`](../../doc/models/store-order-request.md) | Body, Required | order placed for purchasing the pet |

## Response Type

[`Order`](../../doc/models/order.md)

## Example Usage

```python
body = StoreOrderRequest()

result = store_controller.place_order(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Order | `APIException` |


# Get Inventory

Returns a map of status codes to quantities

```python
def get_inventory(self)
```

## Response Type

`Dict[str, int]`

## Example Usage

```python
result = store_controller.get_inventory()
print(result)
```


# Delete Order

For valid response try integer IDs with positive integer value. Negative or non-integer values will generate API errors

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_order(self,
                order_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `long\|int` | Template, Required | ID of the order that needs to be deleted |

## Response Type

`void`

## Example Usage

```python
order_id = 62

result = store_controller.delete_order(order_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid ID supplied | `APIException` |
| 404 | Order not found | `APIException` |

