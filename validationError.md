# Validation problems found

A request didn't pass validation stage of processing. Typically, this is after the request was accepted by the API and further
validation was performed. This can include checks like:
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
[Specification](./validationError.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=validationError",
    "title": "Bad Request",
    "status": 400,
    "errors": {
        "Basket.FulfilmentRequirements[0].EstimateForPostCode": [
            {
                "message": "EstimateForPostCode and DeliveryAddressRef are mutually exclusive",
                "code": "E-CHK-0002"
            }
        ],
        "Basket.Lines[4].Quantity": [
            {
                "message": "The line's quantity was less than 1.",
                "code": "E-CHK-0014"
            }
        ]
    }
}
```

```json
{
    "type": "https://problem.api.bunnings.com.au?type=validationError",
    "title": "Bad Request",
    "status": 400,
    "detail": "Please refer to the errors for additional details.",
    "errors": {
        "Currency": [
            {
                "message": "Currency must be either aud or nzd and is not case sensitive. The input provided did not match.",
                "code": "E-PAY-0001"
            }
        ]
    }
}
```

## Links

[E-CHK-*](./?codes=errorCodesCheckout)
[E-ORD-*](./?codes=errorCodesOrdering)
[E-PAY-*](./?codes=errorCodesPayment)
[E-VCH-*](./?codes=errorCodesVoucher)
[E-BSK-*](./?codes=errorCodesBasket)