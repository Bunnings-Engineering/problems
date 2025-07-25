# Payment Provider Errors

The requested operation returned errors by the payment provider.  It is possible more than one errors can be triggered from the provider, if this occurs an array of results is returned

## Problem Type

type = https://problem.api.bunnings.com.au?type=paymentProviderErrors

## Specification

The problems response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem. 
This is extended to include payment provider errors code and details using an array layout:

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
        traceid:
            type: string
            format: uri
        providerErrors:
            type: array
            properties:
                ref:
                    type: string
                statusCode:
                    type: int
                errorCode:
                    type: string
                errorDetail:
                    type: string
                paymentNumber:
                    type: integer
        outcomes:
            type: array
            properties:
                outcome:
                    type: string
                paymentNumber:
                    type: integer 

```
[Specification](./paymentProviderErrors.yaml)


## JSON Example - Payment Provider Errors
```json
{
    "type": "https://problem.api.bunnings.com.au?type=paymentProviderErrors",
    "title": "Bad Request",
    "status": 400,
    "detail": "Voucher API returned errors",
    "traceid": "00-758a2ee6af6029a4af86afb1e8b802a7-f3e03c7e8d1e1fa1-00",
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

## JSON Example - Payment Provider Errors - '/captures' endpoint (batch processing)
```json  
{
    "type": "https://problem.api.bunnings.com.au?type=paymentProviderErrors",
    "title": "Bad Request",
    "status": 400,
    "detail": "Captures API Error",
    "traceid": "00-758a2ee6af6029a4af86afb1e8b802a7-f3e03c7e8d1e1fa1-00",
    "providerErrors": [
        {
            "ref": "BPoint",
            "statusCode": 400,
            "errorCode": "CapturesFailed",
            "errorDetail": "Exception of type 'HttpException' was thrown.",
            "paymentNumber": 2
        }
    ],
    "outcomes": [
        {
            "paymentNumber": 1,
            "outcome": "Refunded",
        },
        {
            "paymentNumber": 2,
            "outcome": "Voided",
        }
    ]
}
```

## Links

[E-PAY-*](./?codes=errorCodesPayment)