# Application problems found

Application problems have been found that are unlikely to be resolved by immediately repeating the request. They can represent
issues such as misconfigured prices or store settings.

## Problem Type

type = https://problem.api.bunnings.com.au?type=problems

## Specification

The problems response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
This is extended to include code/description collection

```yaml
problem:
    type: object
    description: RFC 7807 superset problem.
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
        errors:
            type: object
            properties:
                problems:
                    type: array
                    properties:
                        code:
                            type: string
                        message:
                            type: string
```
[Problem Specification](./problems.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=problems",
    "title": "Bad Request",
    "status": 400
    "errors": {
        "problems": [
            {
                "message": "Pricing API did not find a price for item: 3314001",
                "code": "E-CHK-0027"
            }
        ]
    }
  }
}
```