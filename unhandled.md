# Unhandled error

This is usually used to return status information after an unhandled exception is caught. The trace ID returned should be
sufficient to find the internal details that caused the problem.

## Problem Type

type = https://problem.api.bunnings.com.au?type=unhandled

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
[Specification](./unhandled.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=unhandled",
    "title": "Error",
    "detail": "An error occured while processing a request.",
    "status": 500,
    "traceId": "|<id>."
}
```	