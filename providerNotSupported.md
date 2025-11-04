# Provider Not Supported

This problem indicates that the requested operation is not supported by the specified provider.

## Problem Type

type = https://problem.api.bunnings.com.au?type=providerNotSupported

## Specification

The problem response is based on the [RFC 7807](https://tools.ietf.org/html/rfc7807) problem type. It includes the following structure:

```yaml
problem:
    type: object
    description: >|
        Indicates that the requested operation is not supported by the provider.
        The `instance` field may provide a URL to the specific resource or operation,
        and `detail` can offer more specific information about why the provider
        does not support the operation.
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
