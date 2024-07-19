# Input Schema Error codes

The following error codes are used globally across all domains within Bunnings eco-system.  

They are designed to be a standard error code for common input schema issues.

Receiving an error with one of these codes will have the same meaning regardless of the domain it is received from.

| Short&nbsp;error&nbsp;code | Name | Description | Error Type| 
| -------- | -------- | -------- | -------|
| E-0001 | Invalid Model | The model has an invalid structure review the request against the specification | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |
| E-0002 | Over Max Length | The field is over its maximum length | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |
| E-0003 | Under Min Length | The field is under its minimum length | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |
| E-0004 | Out of Range | The value is outside the valid range | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |
| E-0005 | Does not match required pattern | The value is not a match for the required regex for the felid | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |
| E-0006 | Missing Required | The required field was not provided | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |
| E-0007 | Invalid String Length | The given string is outside the valid length | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=requestError">requestError</a> |