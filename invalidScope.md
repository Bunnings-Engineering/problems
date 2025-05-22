# Invalid Scope

The scope present in the token does not match the API scope.

## Problem Type

type = https://problem.api.bunnings.com.au?type=invalidScope

## Specification

The invalid scope problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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
    "type": "https://problem.api.bunnings.com.au?type=invalidScope",
    "title": "Scope present in token does not match to API scope.",
    "status": 400
}
```
