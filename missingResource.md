# Missing Resource

This problem type is used to indicate that the requested resource was not found.

## Problem Type

type = https://problem.api.bunnings.com.au?type=missingResource

## Specification

This problem type includes no additional properties beyond the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

```yaml
problem:
    type: object
    description: RFC 7807 compliant problem.
    required:
    - type
    properties:
        type:
            type: string
            format: uri
        title:
            type: string
        status:
            type: integer
        detail:
            type: string
        instance:
            type: string
            format: uri
```

[Specification](./missingResource.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=missingResource",
    "title": "Order not found",
    "detail": "order id:12345",
    "status": 404,
    "traceId": "|<id>."
}
```
