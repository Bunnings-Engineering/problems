# Service Unavailable

The requested operation could not be completed because a dependent service is currently unavailable.

## Problem Type

type = https://problem.api.bunnings.com.au?type=serviceUnavailable

## Specification

The problem response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem. This is extended to include service-specific error details and a trace identifier.

```yaml
serviceUnavailable:
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
                message:
                    type: string
                code:
                    type: string
        traceId:
            type: string
```

[Specification](./serviceUnavailable.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=serviceUnavailable",
    "title": "Service Unavailable",
    "status": 503,
    "detail": "The service is currently unavailable.",
    "errors": {
        "message": "Loyalty service is unavailable",
        "code": "E-LOY-2000"
    },
    "traceId": "{Scrubbed}"
}
```

## Links

[E-LOY-*](./?codes=errorCodesLoyalty)