# Too Early

The server is unwilling to process the request because it might be repeated.

## Problem Type

type = https://problem.api.bunnings.com.au?type=tooEarly

[MDN: Too Early](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/425)

## Specification

The tooEarly problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./tooEarly.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=tooEarly",
    "title": "Too Early",
    "status": 425
}
```
