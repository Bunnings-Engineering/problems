# Proxy Authentication Required

The request must be authenticated by a proxy before it can be processed.

## Problem Type

type = https://problem.api.bunnings.com.au?type=proxyAuthenticationRequired

[MDN: Proxy Authentication Required](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/407)

## Specification

The proxyAuthenticationRequired problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./proxyAuthenticationRequired.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=proxyAuthenticationRequired",
    "title": "Proxy Authentication Required",
    "status": 407
}
```
