# Item API error codes

| Short&nbsp;error&nbsp;code | Name | Description | Error |
| -------- | -------- | -------- | -------- |
| E-ITM-0003 | MissingIdempotencyKey | The x-idempotency-key header is required. | [validationError](?type=validationError) |
| E-ITM-0004 | MissingCountryCode | The country code is required. | [validationError](?type=validationError) |
| E-ITM-0005 | InvalidCountryCode | The country code is invalid. Valid country codes are AU and NZ. | [validationError](?type=validationError) |
| E-ITM-0006 | MissingItemNumbers | The itemNumbers query parameter is required. | [validationError](?type=validationError) |
| E-ITM-0007 | TooManyItemNumbers | Too many records requested, the total number cannot be more than 100. | [validationError](?type=validationError) |
| E-ITM-0008 | MissingItemNumber | The item number is required. | [validationError](?type=validationError) |
| E-ITM-0009 | InvalidItemNumber | The item number is invalid. It must be a 7 digit numerical value. | [validationError](?type=validationError) |
| E-ITM-0010 | MissingLocationCodes | The locationCodes query parameter is required. | [validationError](?type=validationError) |
| E-ITM-0011 | MissingSearchQuery | The search query is required. | [validationError](?type=validationError) |
