# Precondition Required

The request requires precondition headers to be present and valid.

## Problem Type

type = https://problem.api.bunnings.com.au?type=preconditionRequired

[MDN: Precondition Required](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/428)

## Specification

The preconditionRequired problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./preconditionRequired.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=preconditionRequired",
    "title": "Precondition Required",
    "status": 428
}
```
