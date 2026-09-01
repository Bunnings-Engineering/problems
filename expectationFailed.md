# Expectation Failed

A precondition given in one of the request headers is not met by the server.

## Problem Type

type = https://problem.api.bunnings.com.au?type=expectationFailed

[MDN: Expectation Failed](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/417)

## Specification

The expectationFailed problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./expectationFailed.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=expectationFailed",
    "title": "Expectation Failed",
    "status": 417
}
```
