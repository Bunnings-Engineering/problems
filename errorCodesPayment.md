# Payment API error codes

The Payment API is unlike other domains, the purpose of this domain is to act as a gateway for the various payment providers utilised throughout Bunnings eco-system,  (e.g. PayPal, Click, AfterPay, ZipPay, Voucher etc).  This has resulted in one common schema which is servicing the functions for all the available payment providers.

For this reason, the API has a series of error codes available at the domain level (e.g. all payment providers can potentially return the error) OR a provider specific error message which has been created to enforce a specific provider rule.  

The error codes have been designed to easily identify the difference between the two <b>rule types</b>. <ul><li>A domain level error will have the format <b>E-PAY-XXX</b></li><li>A provider specific error message will have the format <b>E-PAY-XXX-XX</b></li></ul>

The table below outlines the catalogue of error codes being returned in this format, which provider returns these error codes and the error codes template in use for each code.

A current list of the payment providers, including the end points they support within this domain, is available on <b>GET /providers</b>.

## Validation Errors: 

| Short error&nbsp;code | Provider | Constant Name | Business Rule | Message | Error Type | Where Used
| -------- | -------- | ---------- | -------- |-----------|--------- | --------- |
| E-PAY-0001 | Domain | CurrencyNotAcceptable | Input data must be one of “aud” or “nzd”.  This value is not case sensitive e.g. AUD, Aud, aud, all versions are acceptable. | Currency must be either aud or nzd and is not case sensitive. The input provided did not match. |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: currency <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balanceCheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul></details>
| E-PAY-0002 | Domain | BunningsInternalRefMandatory | Data entry for the nominated provider is mandatory | The input data is mandatory |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: internalPaymentRef <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/reserve</li></ul> </details>
| E-PAY-0003 | Domain| ProviderRefMandatory |  Data entry for the nominated provider is mandatory | The input data is mandatory |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerPaymentRef <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul> </details>
| E-PAY-0004 | Domain | ProviderRefUnacceptable |  Data entry for the nominated provider does not meet the input expectations | The input data is not acceptable |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |JSON Path: providerPaymentRef 
| E-PAY-0004-01 | <i>Voucher specific</i> | VoucherReferenceInvalid | Input data must be exactly 25 digits (numerical data only) | The voucher barcode provided in providerPaymentRef must equal exactly 25 digits.  The input provided did not match. |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerPaymentRef <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li></ul></details>
| E-PAY-0004-02 | <i>Voucher specific</i> | VoucherReferenceUnacceptable |  Input data must be either a <ul><li>a valid and active token OR</li><li>voucher barcode which must be exactly 25 digits</li></ul> | The voucher provider expects providerPaymentRef to contain a valid and active PUT&nbsp;/payment/balancecheck token OR a voucher barcode with exactly 25 digits |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerPaymentRef <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/reserve</li></ul> </details>
| E-PAY-0004-03 | <i>Voucher specific</i> |VoucherTokenReferenceInvalid | Input token must be<ul><li>Active</li><li>issued by payment API</li><li>have subject</li><li>have idp</li><li>have barcode number</li></ul> | The voucher token provided is not valid and the transaction cannot be voided. |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerPaymentRef <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/void</li></ul> </details>
| E-PAY-0005 | Domain  | ProviderAuthMandatory | Data entry for the nominated provider is mandatory | The input data is mandatory |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerPaymentAuthorisationCode <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li></ul></details>
| E-PAY-0006 | Domain | ProviderAuthUnacceptable | Data entry for the nominated provider does not meet the input expectations | Input data is not acceptable |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |JSON Path: providerPaymentAuthorisationCode 
| E-PAY-0006-01 | <i>Voucher specific</i>  | VoucherPINMandatory | When <i>providerPaymentRef</i> contains a string with 25 digits (representing a voucher barcode) then providerPaymentAuthorisationCode is <u>mandatory</u> | For voucher provider when the providerPaymentRef contains a voucher barcode, providerPaymentAuthorisationCode is mandatory.  This attribute expects the voucher PIN. |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerPaymentAuthorisationCode <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/reserve</li></ul></details>
| E-PAY-0007 | Domain | LocationCodeMandatory | Data entry for the nominated provider is mandatory | The input data is mandatory |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: locationCode <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul> </details>
| E-PAY-0008 | Domain  | LocationCodeInvalid | Input data is validated to a known list of Bunnings store locations and the input data did not match. | An invalid location code was provided |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: locationCode <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul></details>
| E-PAY-0009 | Domain  | SourceMandatory | Data entry for the nominated provider is mandatory | The input data is mandatory |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: source <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul></details>
| E-PAY-0010 | Domain | ProviderAccountMandatory | Data entry for the nominated provider does not meet the input expectations | Input data is not acceptable |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |JSON Path: providerAccount 
| E-PAY-0010-01 | <i>Voucher specific</i>  | VoucherAccountInvalid | This data input is optional<ul><li>If this input data is omitted, then a default value of “Bunnings” is applied within Payment API.</li><li>If populated, then data must match “Bunnings”. This value is not case sensitive e.g. “Bunnings”, “BUNNINGS”, “bunnings” are acceptable.</li></ul> | For voucher provider the providerAccount expects the static value 'Bunnings' |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerAccount <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul></details>
| E-PAY-0011 | Domain  | ProviderRefInvalid | Data entry for the nominated provider does not meet the input expectations | Input data is not acceptable.  A known provider name is expected. |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | JSON Path: providerRef <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li><li>PUT&nbsp;/payment/void</li></ul></details>
| E-PAY-00012 | Domain  | CustomerTokenExpired | Token supplied has expired | Customer access token has expired |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a>  | JSON Path: customer/token <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li></ul></details>
| E-PAY-00013 | Domain   | CustomerTokenInvalid | Token supplied is invalid  | Customer access token is invalid |<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |JSON Path: customer/token <br><details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/balancecheck</li><li>PUT&nbsp;/payment/reserve</li></ul></details>
| E-PAY-00014-01 | <i>Voucher specific</i>  | VoucherTokenMismatch | When <i>providerPaymentRef</i> contains a token then <i>customer/token</i> is <u>mandatory.</u><br><i>customer/token</i> must have<ul><li>subjectId populated</li><li>token is active</li><li>token is issued by the same idp as auth token (e.g. issued by Bunnings)</li></ul><i>providerPaymentRef</i> token<ul><li>Active</li><li>issued by payment API</li><li>have subject</li><li>have idp</li><li>have card number</li></ul><u>both</u> tokens must have<ul><li>same subject</li><li>same idp</li></ul>| PUT&nbsp;/payment/balancecheck token provided in providerPaymentRef does not match the credentials in customer token.|<a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a>  |<details><summary>End Points:</summary><b>Voucher&nbsp;Provider</b><ul><li>PUT&nbsp;/payment/reserve</li></ul></details>



## Payment Provider Errors:

When an error code is returned from a payment provider (e.g. PayPal, Click, AfterPay, ZipPay, Voucher etc), the Payment API wraps this content into a <a target="_blank" href="https://problem.api.bunnings.com.au/?type=paymentProviderError">paymentProviderError</a>

Generic mapping rules for this type of error response are outlined below

| JSON&nbsp;Path&nbsp;for paymentProviderError | Required | Transformation Rule | Sample Data |
| -------- | -------- | -------- |-----------|
| type | Mandatory |Specifies the error code template <br>https://problem.api.bunnings.com.au?type=paymentProviderError| `https://problem.api.bunnings.com.au?type=paymentProviderError`
| title | Mandatory |Set to a constant value for each payment provider (e.g. PayPal, Click, AfterPay, ZipPay, Voucher etc)| Voucher API returned an error
| status | Mandatory |Hard code to 400| 400
| detail | Mandatory |</i>Represents human readable version of the response received from the provider.  <br><br>Note:  This may be constructed using the data received from the provider| Voucher Status Code: 400, Voucher Error Code: E-VCH-001, Voucher Error Message: Voucher barcode number does not exist
| traceId | Optional |Capture the traceId returned in the error transaction (if available)| 00-758a2ee6af6029a4af86afb1e8b802a7-f3e03c7e8d1e1fa1-00
| provider/ref | Mandatory |Hard code to the payment provider name (e.g. PayPal, Click, AfterPay, ZipPay, Voucher etc)| Voucher
| provider/statusCode | Mandatory |map to the http status code received from the provider (e.g. 400, 404)| 400
| provider/errorCode | Mandatory |map to the error code received from the provider (e.g. refund_timelimit_exceeded, E-VCH-0001)| E-VCH-0001
| provider/errorDetail | Mandatory |map to the error description received from the provider| Voucher barcode number does not exist
<br>

### JSON Example
```json  
{
    "type": "https://problem.api.bunnings.com.au?type=paymentProviderError",
    "title": "Voucher API returned an error",
    "status": 400,
    "detail": "Voucher Status Code: 400, Voucher Error Code: E-VCH-0001, Voucher Error Message: Voucher barcode number does not exist",
    "traceid": "00-758a2ee6af6029a4af86afb1e8b802a7-f3e03c7e8d1e1fa1-00",
    "provider": {
        "ref": "Voucher",
        "statusCode": "400",
        "errorCode": "E-VCH-0001",
        "errorDetail": "Voucher barcode number does not exist"
    }
}
```