# Failed Dependency

The request failed due to the failure of a previous request.

## Problem Type

type = https://problem.api.bunnings.com.au?type=failedDependency

[MDN: Failed Dependency](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/424)

## Specification

The failedDependency problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./failedDependency.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=failedDependency",
    "title": "Failed Dependency",
    "status": 424
}
```
