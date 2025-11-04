# Invalid Server State

The server state path parameter passed to the operation is invalid.

Server state is an opaque string returned by the server as part of an object's `_meta` data and should be used to populate a link's `href` template. It should be copied directly into an HTTP resource request. Server state is part of how the API implements the HATEOAS pattern and is used by the server to manage workflow state.

## Problem Type

type = https://problem.api.bunnings.com.au?type=invalidServerState

## Specification

The invalid server state problem includes no additional properties on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem and therefore uses the base specification.

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

[Problem Specification](./invalidServerState.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=invalidServerState",
    "title": "Server state provided by the client is invalid",
    "status": 400
}
```
