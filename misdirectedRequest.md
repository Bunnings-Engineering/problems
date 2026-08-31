# Misdirected Request

The request was directed at a server that is not able to produce a response.

## Problem Type

type = https://problem.api.bunnings.com.au?type=misdirectedRequest

[MDN: Misdirected Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/421)

## Specification

The misdirectedRequest problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./misdirectedRequest.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=misdirectedRequest",
    "title": "Misdirected Request",
    "status": 421
}
```
