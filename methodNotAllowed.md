# Method Not Allowed

The method specified in the request is not supported by the target resource.

## Problem Type

type = https://problem.api.bunnings.com.au?type=methodNotAllowed

[MDN: Method Not Allowed](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/405)

## Specification

The methodNotAllowed problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./methodNotAllowed.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=methodNotAllowed",
    "title": "Method Not Allowed",
    "status": 405
}
```
