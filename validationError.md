# Validation problems found

A request did not pass the validation stage of processing. Typically, this is after the request was accepted by the API and further
validation was performed. This can include checks like:

- Mutually exclusive fields
- Conditionally mandatory fields
- Field value range checks

## Problem Type

type = <https://problem.api.bunnings.com.au?type=validationError>

## Specification

The problem response is based on the [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
This is extended to include a collection of codes and descriptions.

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
                <field>:
                    type: array
                    properties:
                        code:
                            type: string
                        message:
                            type: string
                        context:
                            type: object
                            description: Optional metadata describing the error. Simple key-value pairs only.
                            nullable: true
                            additionalProperties: true
```

[Specification](./validationError.yaml)

## Context

Each error may include an optional `context` object. It carries additional metadata about the failure, such as the
minimum and maximum lengths that were expected, so that generic error codes can be reused across use cases without
creating domain-specific variations.

`context` is optional and holds simple JSON key-value pairs. It is omitted entirely when there is no metadata to
report, so existing consumers are unaffected, and consumers that do not understand `context` can safely ignore it.

Refer to the [context property registry](./?type=contextProperties) for the approved property names.

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
                "message": "Currency must be 'aud' or 'nzd' (case-insensitive). The provided input did not match.",
                "code": "E-PAY-0001"
            }
        ]
    }
}
```

An example including the optional `context` metadata:

```json
{
    "type": "https://problem.api.bunnings.com.au?type=validationError",
    "title": "Bad Request",
    "status": 400,
    "detail": "Please refer to the errors for additional details.",
    "errors": {
        "Basket.Lines[4].Quantity": [
            {
                "message": "The value was outside the allowed range.",
                "code": "E-CHK-0014",
                "context": {
                    "min": 1,
                    "max": 999
                }
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
[E-COM-*](./?codes=errorCodesCommunications)
[E-CON-*](./?codes=errorCodesConsumer)
[E-LOY-*](./?codes=errorCodesLoyalty)
