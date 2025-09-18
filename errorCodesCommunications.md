# Communications API error codes

The Communications domain provides functionality to send messages via **Email** or **SMS**. The delivery of these messages is handled by third-party providers such as SendGrid, Sfmc, and FoneDynamics. This domain uses a standard API contract structure to integrate with any of these providers.

Messages can be sent using one of two approaches:
<ul><li><b>Immediate Release:</b> The message content is received and dispatched immediately according to the provided instructions.</li>
<li><b>Hold & Release:</b> The message content is received and held until a secondary process calls the Communications API to release the message for dispatch according to the provided instructions.</li></ul> 

The Communications domain uses an internal outbox to manage the dispatch of messages. The progress of a message can be tracked by calling the **GET /logs** endpoint.

This page catalogues a list of error codes generated exclusively from the Communications Domain from V2.0 and above.

Communications V1.0 is scheduled for retirement and should no longer be used.

## Message Creation Errors
The following is a list of error codes related to these API endpoints that **create** a message, including (but not limited to):
<ul><li><b>PUT /email/{context}/{businessKey}</b></li>
<li><b>PUT /sms/{context}/{businessKey}</b></li></ul>
<br>
All error codes listed return using a <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">https://problem.api.bunnings.com.au/?type=validationError</a> format.

<br>

| Short&nbsp;error&nbsp;code | Constant Name | JSON Path | Business Rule | Message | Where used |
| -------- | -------- | -------- | -------- |  -------- |  -------- |
| E-COM-0001 | SendDefinitionIdNotActive | ```sendDefinitionId``` | When input payload is received, check whether the ```sendDefinitionId``` is valid for use | The template provided either doesn’t exist or is not in a valid state for use | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/email/{context}/{businessKey}</li><li>PUT&nbsp;/sms/{context}/{businessKey}</li></ul></details> |
| E-COM-0002 | DelaySecondsInvalid | ```sendDelaySeconds``` | The value in ```SendDelaySeconds``` cannot exceed the value in ```DiscardAfterSeconds```| SendDelaySeconds cannot exceed the value in DiscardAfterSeconds.  Please revise input | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/email/{context}/{businessKey}</li><li>PUT&nbsp;/sms/{context}/{businessKey}</li></ul></details> |
| E-COM-0003 | recipientEmailAddressInvalid | ```recipientEmailAddress``` | Returned when ```recipientEmailAddress``` is provided but is not a valid email address <br> Assess the data entry to ensure there is a character before and after an @ symbol.<br><br>RegEx: <b>^.+@.+$</b> | Invalid recipient email address | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/email/{context}/{businessKey}</li></ul></details> |
| E-COM-0004 | fromEmailAddressInvalid | ```fromEmailAddress``` | Returned when ```fromEmailAddress``` is provided but is not a valid email address <br> Assess the data entry to ensure there is a character before and after an @ symbol.<br><br>RegEx: <b>^.+@.+$</b> | Invalid from email address | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/email/{context}/{businessKey}</li></ul></details> |
| E-COM-0005 | recipientMobileNbrInvalid | ```recipientMobileNumber``` | Returned when ```recipientMobileNumber``` is not matching E.164 format | Invalid recipient mobile number.  This must be formatted to E.164 standard e.g. +61412345678 | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/sms/{context}/{businessKey}</li></ul></details> |
| E-COM-0006 | fromMobileNbrInvalid | ```fromMobileNumber``` | Returned when ```fromMobileNumber``` is not matching E.164 format | Invalid from mobile number.  This must be formatted to E.164 standard e.g. +61412345678 | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/sms/{context}/{businessKey}</li></ul></details> |
| E-COM-0007 | TemplateValidationFail | ```sendOnTemplateValidationFailure``` | Each message request is validated to the ```sendDefinitionId``` nominated, this is done by binding the input data to the template contents.  If this process results in a failure, then this error message is returned. <br><br>To assist troubleshooting this error, a template preview is available on <b>POST /definitions/preview</b> end point.<br><br>This error can be skipped, forcing the input request to be sent to 3rd party.  This is achieved by setting ```sendOnTemplateValidationFailure``` to true.<br><br>When not specified, by default this be set to false. | This request has failed when binding the input data to the sendDefinitionId template contents.  Please preview the data on the link provided and try again. | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/email/{context}/{businessKey}</li><li>PUT&nbsp;/sms/{context}/{businessKey}</li></ul></details> |
| E-COM-0008 | contextBusinessKeyExists | ```#businessKey``` |When ```x-idempotency-key``` has not been provided and a request is received which matches to an existing <b>{context} & {businessKey}</b> | A message matching the context and businessKey already exists.  Use an idempotency key to handle transient retries to avoid returning this error. If this is a discrete communication, then you need to provide a different businessKey.| <details><summary>End Points:</summary><ul><li>PUT&nbsp;/email/{context}/{businessKey}</li><li>PUT&nbsp;/sms/{context}/{businessKey}</li></ul></details> |
 

<br><br>


## Message Release Errors
The following is a list of error codes related to these API endpoints that **release** a message, including (but not limited to):
<ul><li><b>PUT /release/{serverState}</b></li></ul>
<br>
All error codes listed return using a <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">https://problem.api.bunnings.com.au/?type=validationError</a> format.

<br>

| Short&nbsp;error&nbsp;code | Constant Name | JSON Path | Business Rule | Message | Where used |
| -------- | -------- | -------- | -------- |  -------- |  -------- |
| E-COM-0009 | messageNotFound | ```sourceSystemReference``` | Returned when a matching message record cannot be found | Message does not exist | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/release/{serverState}</li></ul></details> |
| E-COM-0010 | messageInvalid | ```sourceSystemReference``` |Returned when a message is found but the message ```schedule.discardDateTimeUtc``` is less than the current system UTC date time.<br><br>This means the data has expired and will be discarded. | Message exists but it has reached the discard date time and cannot be released.  | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/release/{serverState}</li></ul></details> |
| E-COM-0011 | serverStateInvalid | ```#serverState``` | Returned when the matching message has progressed from the <b>Hold</b> status.<br><br>This signifies the release has already occured.  This action can only be performed once. | Message has already been released.  This action can only be performed once.  Use <b>GET /logs</b> end point to review the current status. | <details><summary>End Points:</summary><ul><li>PUT&nbsp;/release/{serverState}</li></ul></details> |