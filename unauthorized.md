# Unauthorized

The server understood the request but refuses to authorise it because the user has not provided valid credentials.

## Problem Type

type = https://problem.api.bunnings.com.au?type=unauthorized

[MDN: Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/401)

## Specification

The unauthorized problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./unauthorized.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=unauthorized",
    "title": "Unauthorized",
    "status": 401
}
```
