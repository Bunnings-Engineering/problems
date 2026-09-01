# Payload Too Large

The request entity is larger than the server is willing or able to process.

## Problem Type

type = https://problem.api.bunnings.com.au?type=payloadTooLarge

[MDN: Payload Too Large](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/413)

## Specification

The payloadTooLarge problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./payloadTooLarge.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=payloadTooLarge",
    "title": "Payload Too Large",
    "status": 413
}
```
