# Invalid Authorisation Token

The authorisation token provided with request to access resource is not valid. token string in request Authrorisation bearer header is required to validate the identity of user to whether user has access to asked resource.

## Problem Type

type = https://problem.api.bunnings.com.au?type=invalidAuthorisationToken

## Specification

The invalid authorisation token problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
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
    "type": "https://problem.api.bunnings.com.au?type=invalidAuthorisationToken",
    "title": "Access Token provided by the client was found not valid for this request",
    "status": 401
}
```	