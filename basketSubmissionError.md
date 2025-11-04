# Basket submission problems found

A request failed to successfully process an order submission. Typically, this is after the request is accepted by the API and further
processing is performed. This can include failures like:

* Invalid prices
* Invalid account details
* Invalid items

## Problem Type

type = https://problem.api.bunnings.com.au?type=basketSubmissionError

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
        basketRef:
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
    "type": "https://problem.api.bunnings.com.au?type=basketSubmissionError",
    "title": "Basket submission error",
    "status": 400,
    "detail": "Please refer to the errors for additional details.",
    "basketRef": "B1:0f019b58-9fa4-4800-92d3-b1635d70025f",
    "errors": {        
        "submissionAttempt": [                    
            {
                "message": "Duplicate Order Number",
                "code": "E-ORD-1010"
            }
        ]
    }
}
```

## Links

[E-ORD-*](./?codes=errorCodesOrdering)
[E-CHK-*](./?codes=errorCodesCheckout)
[E-TRA-*](./?codes=errorCodesTransaction)