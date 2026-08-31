# Request Header Fields Too Large

One or more request headers are larger than the server is willing to process.

## Problem Type

type = https://problem.api.bunnings.com.au?type=requestHeaderFieldsTooLarge

[MDN: Request Header Fields Too Large](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/431)

## Specification

The requestHeaderFieldsTooLarge problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./requestHeaderFieldsTooLarge.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=requestHeaderFieldsTooLarge",
    "title": "Request Header Fields Too Large",
    "status": 431
}
```
