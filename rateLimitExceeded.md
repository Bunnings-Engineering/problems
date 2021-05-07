# Spike Arrest Limit excedded 

The number of request sent to server have exceeded the permitted rate limit. 

## Problem Type

type = https://problem.api.bunnings.com.au?type=rateLimitExceeded

## Specification

The rate limit exceeded problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
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
```
[Problem Specification](./problem.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=rateLimitExceeded",
    "title": "Too Many messages from the client",
    "status": 429
}
```
