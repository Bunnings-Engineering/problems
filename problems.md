# Application Problems

Application problems have been identified that are unlikely to be resolved by immediately retrying the request. These can represent issues such as misconfigured prices or store settings.

## Problem Type

type = https://problem.api.bunnings.com.au?type=problems

## Specification

The problem response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem. This is extended to include a collection of specific error details.

```yaml
problems:
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
                    items:
                        type: object
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
    "status": 400,
    "errors": {
        "problems": [
            {
                "message": "Pricing API did not find a price for item: 3314001",
                "code": "E-CHK-0027"
            }
        ]
    }
}
```
