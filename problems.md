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
                            context:
                                type: object
                                description: Optional metadata describing the error. Simple key-value pairs only.
                                nullable: true
                                additionalProperties: true
```

[Problem Specification](./problems.yaml)

## Context

Each problem may include an optional `context` object. It carries additional metadata about the failure, such as the
minimum and maximum lengths that were expected, so that generic error codes can be reused across use cases without
creating domain-specific variations.

`context` is optional and holds simple JSON key-value pairs. It is omitted entirely when there is no metadata to
report, so existing consumers are unaffected, and consumers that do not understand `context` can safely ignore it.

Refer to the [context property registry](./?type=contextProperties) for the approved property names.

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

An example including the optional `context` metadata:

```json
{
    "type": "https://problem.api.bunnings.com.au?type=problems",
    "title": "Bad Request",
    "status": 400,
    "errors": {
        "problems": [
            {
                "message": "The requested quantity was outside the allowed range.",
                "code": "E-CHK-0014",
                "context": {
                    "min": 1,
                    "max": 999
                }
            }
        ]
    }
}
```
