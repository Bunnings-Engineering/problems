# Unsupported Character detected in request

Unsupported character detected in request sent to server. Supported charset are Windows-1252 and ISO8859-1

## Problem Type

type = https://problem.api.bunnings.com.au?type=unsupportedCharacter

## Specification

The Unsupported character problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
so uses the base specification

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
[Problem Specification](./problem.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=unsupportedCharacter",
    "title": "Invalid encoded character detected.",
    "status": 415
}
```