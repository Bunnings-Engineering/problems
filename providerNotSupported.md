# Provider Not Supported

This is used to indicate the requested operation was not supported by the provider.

## Problem Type

type = https://problem.api.bunnings.com.au?type=providerNotSupported

```yaml
problem:
    type: object
    description: >|
This problem is used to describe the error received when a user
did an invalid operation against an API. The instance will provide
the url, the title the error and specific details around the invalid
operation that occurred.
This problem is based off the RFC 7807 compliant problem type.
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