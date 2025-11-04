# Resource error

This error indicates a problem with a dependent resource. It is safe to retry after a short delay.

## Problem Type

type = https://problem.api.bunnings.com.au?type=resourceError

## Specification

The resource error is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem. This is extended to include a collection of codes and descriptions.

```yaml
resourceError:
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

[Specification](./resourceError.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=resourceError",
    "title": "Error",
    "detail": "An error occured while processing a request.",
    "status": 500,
    "traceId": "|<id>.",
    "errors": {
        "problems": [
            {
                "message": "Preauth Cancel for bulk release was incomplete.  It is safe to retry after a short delay.",
                "code": "E-VCH-0103"
            }
        ]
    }    
}
```
