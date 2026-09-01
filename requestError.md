# Request problems found

This indicates that error(s) were found in the incoming request, they are likely to be low-level issues such as invalid values
for the type or missing fields. A generic, high-level error code is used to describe all request problems. These problems indicate
an issue with the caller.

## Problem Type

type = https://problem.api.bunnings.com.au?type=requestError

## Specification

The response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
This is extended to include a collection of codes and descriptions.

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
                <field>:
                    type: array
                    properties:
                        code:
                            type: string
                        message:
                            type: string
                        context:
                            type: object
                            description: Optional metadata describing the error. Scalar values are supported; arrays are reserved for allowedValues.
                            properties:
                                allowedValues:
                                    type: array
                                disallowedValues:
                                    type: array
                            additionalProperties:
                                oneOf:
                                - type: string
                                - type: number
                                - type: boolean
```

[Specification](./requestError.yaml)

## Context

Each error may include an optional `context` object. It carries additional metadata about the failure, such as the
minimum and maximum lengths that were expected, so that generic error codes can be reused across use cases without
creating domain-specific variations.

`context` is optional and holds simple JSON key-value pairs. Scalar values are supported, and arrays are reserved for
`allowedValues`. Nested objects are not supported. It is omitted entirely when there is no metadata to report, so
existing consumers are unaffected, and consumers that do not understand `context` can safely ignore it.

Refer to the [context property registry](./?type=contextProperties) for the approved property names.

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=requestError",
    "title": "One or more validation errors occurred",
    "status": 400,
    "errors": {
        "code": [
            {
                "message": "The required field was not provided",
                "code": "E-0006"
            }
        ],
        "name": [
            {
                "message": "The field is under its minimum length",
                "code": "E-0003"
            }
        ]
    }
}
```

An example including the optional `context` metadata:

```json
{
    "type": "https://problem.api.bunnings.com.au?type=requestError",
    "title": "One or more validation errors occurred",
    "status": 400,
    "errors": {
        "name": [
            {
                "message": "The field is under its minimum length",
                "code": "E-0003",
                "context": {
                    "min": 3,
                    "max": 50,
                    "length": 1
                }
            }
        ]
    }
}
```

## Links

[E-PAY-*](./?codes=errorCodesInputSchemaErrors)
