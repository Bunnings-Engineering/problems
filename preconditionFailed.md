# Precondition Failed

One or more conditions given in the request headers evaluated to false when tested on the server.

## Problem Type

type = https://problem.api.bunnings.com.au?type=preconditionFailed

[MDN: Precondition Failed](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/412)

## Specification

The preconditionFailed problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./preconditionFailed.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=preconditionFailed",
    "title": "Precondition Failed",
    "status": 412
}
```
