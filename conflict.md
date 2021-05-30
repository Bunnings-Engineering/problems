# Conflict

This is used to indicate a request conflict with current state of the target resource.
Conflicts are most likely to occur when target resource has changed since the last load.

## Problem Type

type = https://problem.api.bunnings.com.au?type=conflict

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
[Specification](./conflict.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=conflict",
    "title": "Request conflicts with current state of the target resource",
    "status": 409,
    "traceId": "|<id>."
}
```	