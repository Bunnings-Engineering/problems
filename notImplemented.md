# Not Implemented

The server does not support the functionality required to fulfil the request.

## Problem Type

type = https://problem.api.bunnings.com.au?type=notImplemented

[MDN: Not Implemented](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/501)

## Specification

The notImplemented problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./notImplemented.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=notImplemented",
    "title": "Not Implemented",
    "status": 501
}
```
