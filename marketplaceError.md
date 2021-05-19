# Marketplace problems found

An external Marketplace API raised an error. Bunnings integrates with external APIs to manage its Marketplace,
these errors encapsulate problems caused due to deliberate decisions (limits on shipping) or configuration
problems.

## Problem Type

type = https://problem.api.bunnings.com.au?type=marketplaceError

## Specification

The problems response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
This is extended to include code/description collection

```yaml
problem:
    type: object
    description: RFC 7807 superset problem.
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
        errors:
            type: object
            properties:
                <offerId>:
                    type: array
                    properties:
                        code:
                            type: string
                        message:
                            type: string
```
[Problem Specification](./marketplaceError.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=marketplaceError",
    "title": "Bad Request",
    "status": 400,
    "errors": {
        "3010": [
            {
                "message": "Marketplace shipping zone WA_PERTH_METRO not allowed",
                "code": "E-CHK-0036"
            }
        ],
        "3012": [
            {
                "message": "Invalid Marketplace Offer ID",
                "code": "E-CHK-0035"
            }
        ]
    }
}
```