# Loyalty API error codes

This catalog of error codes is generated exclusively from the Loyalty API domain.

## Loyalty Errors

The following list of error codes relates to Loyalty endpoints.

| Short&nbsp;error&nbsp;code | HTTP Status | Error Type | Type & Endpoint | Operator Message | Description |
| -------- | -------- | -------- | -------- | -------- | -------- |
| E-LOY-2000 | 503 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=serviceUnavailable">serviceUnavailable</a> | Transport/platform - ALL | Loyalty service is unavailable. | Can't connect to the Loyalty service |
| E-LOY-2001 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Request validity/idempotency - ALL but Void | Not authorised to access loyalty service. | Loyalty Membership has changed. The Loyalty member is not authorised to action this redemption. |
| E-LOY-2002 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Request validity/idempotency - ALL but Void | Forbidden. | The token provided is not valid. |
| E-LOY-2003 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Request validity/idempotency - ALL but Void | Duplicate attempt/transaction sequence. | Two active requests share the same saleActionId + attemptSequence, or same pair used with a different idempotency key — must error. |
| E-LOY-2004 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Request validity/idempotency - ALL but Void | Transaction sequence not provided | saleActionId + attemptSequence not provided |
| E-LOY-2005 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Request validity/idempotency - ALL but Void | Invalid customer/request identifiers. | The IDs passed in don’t match |
| E-LOY-2006 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Request validity/idempotency - ALL but Void | Sale Transaction ID is missing | A valid transaction number not provided |
| E-LOY-2007 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Account/Funds availability - Balance | Requested amount not available to redeem. | Rewards Dollars amount POS trying to process redemption for is not available. |
| E-LOY-2008 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Account/Funds availability - Balance and Refund | Selected source of funds is no longer available. | Membership/account closed or currency removed between Balance and Redeem (effectively “not available”). |
| E-LOY-2009 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Account/Funds availability - Balance and Refund | The amount you are trying to redeem is not valid | Incorrect value. Must be greater than 0 and only 2 decimal places |
| E-LOY-2010 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Account/Funds availability - Refund | Wallet balance currently at max limit | Wallet balance currently at max limit and can't go above 4999. If a refund, provide exchange voucher instead of rewards currency |
| E-LOY-2011 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Secure-code / PIN evidence - Process or refund (future-ready for MVP) | Secure PIN authorisation not provided. | Secure-PIN required, but not supplied. |
| E-LOY-2012 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Secure-code / PIN evidence - Process or refund (future-ready for MVP) | Secure authorisation evidence invalid. | Evidence fails validation; must include Balance token in context so backend can correlate. |
| E-LOY-2013 | 400 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> | Secure-code / PIN evidence - Process or refund (future-ready for MVP) | Secure authorisation evidence expiered. | Evidence fails validation; Secure authorisation evidence expiered as PIN wasn't received in the required timeframe of 1 hour. |