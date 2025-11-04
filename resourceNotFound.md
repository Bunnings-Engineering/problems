# Resource Not Found

Requested resource not found.

## Problem Type

type = https://problem.api.bunnings.com.au?type=resourceNotFound

## Specification

The resource not found problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem, so it uses the base specification.

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

[Specification](./problem.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=resourceNotFound",
    "title": "Requested resource not found.",
    "status": 404
}
```
