# Provider Not Supported

This is used to indicate the requested operation was not supported by the provider.

## Problem Type

type = https://problem.api.bunnings.com.au?type=providerNotSupported

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
        traceId:
            type: string
```
[Specification](./providerNotSupported.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=providerNotSupported",
    "title": "Provider Not Supported",
    "detail": "Provider type is not supported for this operation",
    "status": 400,
    "traceId": "|<id>."
}
```	