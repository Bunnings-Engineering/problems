# Validation problems found

A request failed to pass validation stage of processing. Typically, this is after the request is accepted by the API and further
validation is performed. This can include checks like:
- Mutually exclusive fields
- Conditionally mandatory fields
- Field value range checks


## Problem Type

type = https://problem.api.bunnings.com.au?type=validationError

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
                <field name>:
                    type: array
                    properties:
                        code:
                            type: string
                        message:
                            type: string
```
[Specification](./problems.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=validationError",
    "title": "Bad Request",
    "status": 400,
    "errors": {
        "errors": {
            "CheckoutAttempt.Basket.FulfilmentRequirements[0].EstimateForPostCode": [
                {
                    "message": "EstimateForPostCode and DeliveryAddressRef are mutually exclusive",
                    "code": "E-CHK-0002"
                }
            ],
            "Line": [
                {
                    "message": "EstimateForPostCode and DeliveryAddressRef cannot be mixed in one request",
                    "code": "E-CHK-0008"
                }
            ]
        }
    }
}
```