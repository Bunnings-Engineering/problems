# Request Timeout

The server timed out waiting for the request to be completed.

## Problem Type

type = https://problem.api.bunnings.com.au?type=requestTimeout

[MDN: Request Timeout](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/408)

## Specification

The requestTimeout problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./requestTimeout.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=requestTimeout",
    "title": "Request Timeout",
    "status": 408
}
```
