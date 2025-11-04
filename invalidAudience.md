# Invalid Audience

The audience present in the token does not match the API audience.

## Problem Type

type = https://problem.api.bunnings.com.au?type=invalidAudience

## Specification

This problem type includes no additional properties beyond the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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
    "type": "https://problem.api.bunnings.com.au?type=invalidAudience",
    "title": "Audience present in token does not match to API audience.",
    "status": 400
}
```
