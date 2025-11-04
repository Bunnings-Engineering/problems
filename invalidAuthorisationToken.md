# Invalid Authorisation Token

The authorisation token provided with the request to access a resource is invalid. The token string in the `Authorisation` bearer header is required to validate the user's identity and determine if they have access to the requested resource.

## Problem Type

type = https://problem.api.bunnings.com.au?type=invalidAuthorisationToken

## Specification

The invalid authorisation token problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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
    "type": "https://problem.api.bunnings.com.au?type=invalidAuthorisationToken",
    "title": "Access Token provided by the client was found not valid for this request",
    "status": 401
}
```
