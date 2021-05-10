# Unsupported Media Type detected in request

Unsupported media type detected in request sent to server. 

## Problem Type

type = https://problem.api.bunnings.com.au?type=unsupportedMediaType

## Specification

The Unsupported media type problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
so uses the base specification

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
[Problem Specification](./problem.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=unsupportedMediaType",
     "title": "Content type not supported by server.",
    "status": 415
}
```