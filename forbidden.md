# Forbidden

The server understood the request but refuses to authorize it because the user lacks the necessary permissions.

## Problem Type

type = https://problem.api.bunnings.com.au?type=forbidden

## Specification

The forbidden problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./forbidden.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=forbidden",
    "title": "This request is not authorized to perform this operation using current permissions.",
    "status": 403
}
```
