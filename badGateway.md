# Bad Gateway

The server received an invalid response from an upstream server.

## Problem Type

type = https://problem.api.bunnings.com.au?type=badGateway

[MDN: Bad Gateway](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/502)

## Specification

The badGateway problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./badGateway.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=badGateway",
    "title": "Bad Gateway",
    "status": 502
}
```
