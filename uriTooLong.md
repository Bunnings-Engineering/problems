# URI Too Long

The request URI is longer than the server is willing to interpret.

## Problem Type

type = https://problem.api.bunnings.com.au?type=uriTooLong

[MDN: URI Too Long](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/414)

## Specification

The uriTooLong problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./uriTooLong.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=uriTooLong",
    "title": "URI Too Long",
    "status": 414
}
```
