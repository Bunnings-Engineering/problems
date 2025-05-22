# Payment Provider Errors

The requested operation returned errors from the payment provider. If the provider triggers more than one error, an array of results is returned.

## Problem Type

type = https://problem.api.bunnings.com.au?type=paymentProviderErrors

## Specification

The problem response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem. This is extended to include payment provider error codes and details using an array layout:

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
        traceId:
            type: string
            format: uri
        providerErrors:
            type: array
            items:
                type: object
                properties:
                    ref:
                        type: string
                    statusCode:
                        type: integer
                    errorCode:
                        type: string
                    errorDetail:
                        type: string
```

[Specification](./paymentProviderErrors.yaml)

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=paymentProviderErrors",
    "title": "Bad Request",
    "status": 400,
    "detail": "Voucher API returned errors",
    "traceId": "00-758a2ee6af6029a4af86afb1e8b802a7-f3e03c7e8d1e1fa1-00",
    "providerErrors": [
        {
            "ref": "Voucher",
            "statusCode": 400,
            "errorCode": "E-VCH-0039",
            "errorDetail": "activityDateTime must be in datetime format using offset"
        },
        {
            "ref": "Voucher",
            "statusCode": 400,
            "errorCode": "E-VCH-0216",
            "errorDetail": "posTerminalNumber is required"
        }        
    ]  
}
```

## Links

[E-PAY-*](./?codes=errorCodesPayment)