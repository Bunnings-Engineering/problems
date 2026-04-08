# Invalid Version Number

The `x-version-api` header provided in the request does not contain a valid version number. The version must be a valid semantic version using only major and minor parts.

## Problem Type

type = https://problem.api.bunnings.com.au?type=invalidVersionNumber

## Specification

The invalid version number problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Specification](./invalidVersionNumber.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=invalidVersionNumber",
    "title": "'x-version-api' must be Major.Minor (e.g., 1.0).",
    "status": 400
}
```
