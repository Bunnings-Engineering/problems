# Voucher Validation Problems Found

This error indicates that voucher-related problems were found in the incoming request. These errors can occur due to invalid values, missing mandatory data, or issues found during further validation after the API initially accepted the request.

An error code describes the specific request problem, with further details available in the linked error code documentation.

## Problem Type

type = https://problem.api.bunnings.com.au?type=voucherValidationError

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
            type: array
            items:
                type: object
                properties:
                    code:
                        type: string
                    message:
                        type: string        
```

[Specification](./voucherValidationError.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=voucherValidationError",
    "title": "Bad Request",
    "status": 400,
    "detail": "Voucher 9318757000053236902083568 not found.",
    "traceId": "00-2dd0cda44d2b7df0b0ca6b545cacad7b-1c49459d7805780b-00",
    "errors": [
        {
            "message": "Voucher barcode number does not exist",
            "code": "E-VCH-0001"
        }
    ]
}
```

## Links

[E-VCH-*](./?codes=errorCodesVoucher)
