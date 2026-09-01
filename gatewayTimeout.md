# Gateway Timeout

The upstream server did not respond in time.

## Problem Type

type = https://problem.api.bunnings.com.au?type=gatewayTimeout

[MDN: Gateway Timeout](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/504)

## Specification

The gatewayTimeout problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./gatewayTimeout.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=gatewayTimeout",
    "title": "Gateway Timeout",
    "status": 504
}
```
