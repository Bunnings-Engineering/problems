# Reused Idempotency Key

The `x-idempotency-key` has already been used on a previous request. Please generate a new key and try again.

## Problem Type

type = https://problem.api.bunnings.com.au?type=reusedIdempotencyKey

## Specification

The reused idempotency key problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
It uses the base specification:

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
    "type": "https://problem.api.bunnings.com.au?type=reusedIdempotencyKey",
    "title": "The x-idempotency-key has already been used on a previous request. Please generate a new key and try again.",
    "status": 400
}
```
