# Payment Required

The request was valid, but requires authentication for payment authorisation.

## Problem Type

type = https://problem.api.bunnings.com.au?type=paymentRequired

[MDN: Payment Required](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/402)

## Specification

The paymentRequired problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./paymentRequired.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=paymentRequired",
    "title": "Payment Required",
    "status": 402
}
```
