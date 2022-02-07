# Invalid Audience 

Json is invalid and one or more potential threats were detected.

## Problem Type

type = https://problem.api.bunnings.com.au?type=protectionError

## Specification

One or more potential threats were detected, problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
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
    "type": "https://problem.api.bunnings.com.au?type=protectionError",
    "title": "One or more potential threats were detected.",
    "status": 500
}
```