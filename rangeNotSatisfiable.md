# Range Not Satisfiable

The range specified in the request cannot be fulfilled by the server.

## Problem Type

type = https://problem.api.bunnings.com.au?type=rangeNotSatisfiable

[MDN: Range Not Satisfiable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/416)

## Specification

The rangeNotSatisfiable problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./rangeNotSatisfiable.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=rangeNotSatisfiable",
    "title": "Range Not Satisfiable",
    "status": 416
}
```
