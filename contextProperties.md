# Context Property Registry

The `validationError`, `requestError` and `problems` schemas each support an optional `context` object on every error
item. The `context` object carries additional metadata about the failure, allowing generic error codes to be reused
across multiple use cases without creating domain-specific variations.

This page is the registry of approved `context` property names. Domains should reuse the names below before introducing
new ones, so that consumers can interpret metadata consistently across all Bunnings APIs.

## Rules

1. `context` is always optional. It is omitted from the response when there is no metadata to report, so existing
   consumers are unaffected.
2. `context` is a map of simple JSON key-value pairs. Nested objects and arrays are not supported.
3. Property names are lowercase and reuse the registry entries below wherever they apply.
4. `context` is supplementary. The `code` and `message` must remain meaningful on their own, and consumers must be able
   to ignore `context` entirely.
5. Never place personally identifiable information, credentials or other sensitive data in `context`.
6. New properties should be added to this registry before being used in production.

## Approved properties

| Property | Type | Description |
| --- | --- | --- |
| `length` | number | The length of the supplied value. |
| `max` | number | The maximum permitted value or length, inclusive. |
| `min` | number | The minimum permitted value or length, inclusive. |

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=validationError",
    "title": "Bad Request",
    "status": 400,
    "detail": "Please refer to the errors for additional details.",
    "errors": {
        "Consumer.FirstName": [
            {
                "message": "The field is under its minimum length",
                "code": "E-0003",
                "context": {
                    "min": 2,
                    "max": 50,
                    "length": 1
                }
            }
        ]
    }
}
```

## Links

[Problems](./?type=problems)
[Request Error](./?type=requestError)
[Validation Error](./?type=validationError)
