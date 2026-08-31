# Not Acceptable

The server cannot produce a response matching the list of acceptable values provided in the request's preemptive headers.

## Problem Type

type = https://problem.api.bunnings.com.au?type=notAcceptable

[MDN: Not Acceptable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/406)

## Specification

The notAcceptable problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./notAcceptable.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=notAcceptable",
    "title": "Not Acceptable",
    "status": 406
}
```
