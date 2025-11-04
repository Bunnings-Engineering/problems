# Input Schema Error Codes

The following error codes are used globally across all domains within Bunnings ecosystem.  

They are designed to be a standard error code for common input schema issues.

Receiving an error with one of these codes will have the same meaning regardless of the domain it is received from.

| Short&nbsp;error&nbsp;code | Name | Description | Error Type|
| -------- | -------- | -------- | -------|
| E-0001 | Invalid Model | The model has an invalid structure. Review the request against the specification. | [requestError](?type=requestError) |
| E-0002 | Over Max Length | The field is over its maximum length. | [requestError](?type=requestError) |
| E-0003 | Under Min Length | The field is under its minimum length. | [requestError](?type=requestError) |
| E-0004 | Out of Range | The value is outside the valid range. | [requestError](?type=requestError) |
| E-0005 | Does not match required pattern | The value is not a match for the required regex for the field. | [requestError](?type=requestError) |
| E-0006 | Missing Required | The required field was not provided. | [requestError](?type=requestError) |
| E-0007 | Invalid String Length | The given string is outside the valid length. | [requestError](?type=requestError) |
