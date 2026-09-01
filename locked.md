# Locked

The resource has been locked by another process.

## Problem Type

type = https://problem.api.bunnings.com.au?type=locked

[MDN: Locked](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/423)

## Specification

The locked problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./locked.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=locked",
    "title": "Locked",
    "status": 423
}
```
