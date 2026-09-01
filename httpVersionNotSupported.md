# HTTP Version Not Supported

The server does not support the HTTP protocol version used in the request.

## Problem Type

type = https://problem.api.bunnings.com.au?type=httpVersionNotSupported

[MDN: HTTP Version Not Supported](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/505)

## Specification

The httpVersionNotSupported problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./httpVersionNotSupported.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=httpVersionNotSupported",
    "title": "HTTP Version Not Supported",
    "status": 505
}
```
