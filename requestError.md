# Request problems found

This indicates that error(s) were found in the incoming request, they are likely to be a low-level issues such as invalid values 
for the type or missing fields. A generic high-level error code is used to describe all request problems as the problem represents 
an issue with the caller.

## Problem Type

type = https://problem.api.bunnings.com.au?type=requestError

## Specification

The response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
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
                <field>:
                    type: array
                    properties:
                        code:
                            type: string
                        message:
                            type: string
```
[Specification](./requestError.yaml)

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



## Links

[E-PAY-*](./?codes=errorCodesInputSchemaErrors)