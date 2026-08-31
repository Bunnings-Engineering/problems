# Length Required

The request did not specify the length of its body using a Content-Length header.

## Problem Type

type = https://problem.api.bunnings.com.au?type=lengthRequired

[MDN: Length Required](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/411)

## Specification

The lengthRequired problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./lengthRequired.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=lengthRequired",
    "title": "Length Required",
    "status": 411
}
```
