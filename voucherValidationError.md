# Voucher Validation problems found

This indicates that voucher error(s) were found in the incoming request, they can be issues such as 
- invalid values or missing mandatory data OR 
- after the request was accepted by the API and further validation was performed. 

An error code is used to describe the request problem, with a link to this library below

## Problem Type

type = https://problem.api.bunnings.com.au?type=voucherValidationError

## Specification

The response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem.
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
            type: array
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
    "title": "Bad request",
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