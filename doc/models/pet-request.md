
# Pet Request

## Structure

`PetRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `category` | [`Category2`](../../doc/models/category-2.md) | Optional | - |
| `name` | `str` | Required | - |
| `photo_urls` | `List[str]` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Optional | - |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": 198,
  "category": {
    "id": 232,
    "name": "name2"
  },
  "name": "name4",
  "photoUrls": [
    "photoUrls9"
  ],
  "tags": [
    {
      "id": 26,
      "name": "name0"
    },
    {
      "id": 26,
      "name": "name0"
    },
    {
      "id": 26,
      "name": "name0"
    }
  ],
  "status": "pending"
}
```

