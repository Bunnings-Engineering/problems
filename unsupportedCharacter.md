# Unsupported Character Detected in Request

An unsupported character was detected in the request sent to the server. Supported charsets are Windows-1252 and ISO-8859-1.

## Problem Type

type = https://problem.api.bunnings.com.au?type=unsupportedCharacter

## Specification

The unsupported character problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem, so it uses the base specification.

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

[Specification](./problem.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=unsupportedCharacter",
    "title": "Invalid encoded character detected.",
    "status": 415
}
```
