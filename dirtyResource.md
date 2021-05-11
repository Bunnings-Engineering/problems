# Dirty Resource

This is used to indicate the requested action passed out-of-date information.

## Problem Type

type = https://problem.api.bunnings.com.au?type=dirtyResource

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
[Specification](./problem.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=missingResource",
    "title": "This record has been updated on the server, please perform the request again",
    "detail": "12345 != 23456",
    "status": 422,
    "traceId": "|<id>."
}
```	