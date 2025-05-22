# Payment Provider Error

**This error definition type has been deprecated and replaced by [paymentProviderErrors](./paymentProviderErrors.md)**

The requested operation returned an error from the payment provider.

## Problem Type

type = https://problem.api.bunnings.com.au?type=paymentProviderError

## Specification

The problem response is based on the base [RFC 7807](https://tools.ietf.org/html/rfc7807) problem. This is extended to include payment provider error codes and details:

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
        provider:
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

[Specification](./providerValidationError.yaml)

## JSON with Definition

```json
{
    "type": "https://problem.api.bunnings.com.au?type=paymentProviderError",
    "title": "AfterPay API returned an error.",
    "status": 400,
    "detail": "AfterPay Error Code: invalid_amount, AfterPay Status Code: 422, AfterPay Error Message: Refund amount exceeded open to refund amount.",
    "traceId": "00-e277b5db14c2b1c559679b7b67217694-27364b14ec835d69-00",
    "provider": {
        "ref": "AfterPay",
        "statusCode": 422,
        "errorCode": "Unmapped original error code from the provider, for example invalid_amount",
        "errorDetail": "Unmapped Original error detail from the provider, example Refund amount exceeded open to refund amount"
    }
}
```

## Example

```json
{
    "type": "https://problem.api.bunnings.com.au?type=paymentProviderError",
    "title": "Afterpay API returned an error.",
    "status": 400,
    "detail": "Afterpay Error Code: refund_timelimit_exceeded, Afterpay Status Code: 422, Afterpay Error Message: The refund exceeds the time limit of 120 days.",
    "traceid": "00-758a2ee6af6029a4af86afb1e8b802a7-f3e03c7e8d1e1fa1-00",
    "provider": {
        "ref": "Afterpay",
        "statusCode": "422",
        "errorCode": "refund_timelimit_exceeded",
        "errorDetail": "The refund exceeds the time limit of 120 days"
    }
}
```

## Links

[E-PAY-*](./?codes=errorCodesPayment)