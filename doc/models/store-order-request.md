
# Store Order Request

## Structure

`StoreOrderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `pet_id` | `long\|int` | Optional | - |
| `quantity` | `int` | Optional | - |
| `ship_date` | `datetime` | Optional | - |
| `status` | [`Status1Enum`](../../doc/models/status-1-enum.md) | Optional | - |
| `complete` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "id": 240,
  "petId": 24,
  "quantity": 196,
  "shipDate": "2016-03-13T12:52:32.123Z",
  "status": "placed"
}
```

