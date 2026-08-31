# Gone

The requested resource is no longer available and will not be available again.

## Problem Type

type = https://problem.api.bunnings.com.au?type=gone

[MDN: Gone](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/410)

## Specification

The gone problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./gone.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=gone",
    "title": "Gone",
    "status": 410
}
```
