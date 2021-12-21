# Not Supported

This is used to indicate the requested operation was not supported.

## Problem Type

type = https://problem.api.bunnings.com.au?type=notSupported

## Specification

The problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
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
[Specification](./notSupported.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=notSupported",
    "title": "Not Supported",
    "detail": "Provider type is not supported for this operation",
    "status": 400,
    "traceId": "|<id>."
}
```	