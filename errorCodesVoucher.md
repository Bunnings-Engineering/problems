# Voucher API error codes

This catalog of error codes is generated exclusively from the Voucher Domain.

## Voucher & Events Errors

The following list of error codes relates to the **Voucher & Events** endpoints and can be used across many endpoints.

| Short&nbsp;error&nbsp;code | Constant Name | Message | Error type |
| -------- | -------- | -------- | -------- |
| E-VCH-0001 | VoucherNotFound | Voucher barcode number does not exist. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0002 | VoucherNonRBGC | Voucher barcode received is a non-balance reducing gift card and cannot be used for this action. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0003 | VoucherIncorrectPin | The PIN is incorrect. Please try again. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0004 | VoucherIncorrectPinExceeded | Incorrect PIN. Your attempts have been exceeded. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0005 | VoucherCurrencyMismatch | The currency of the transaction does not match the currency available on the voucher. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0006 | VoucherLocked | The Voucher is locked. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0007 | VoucherStatusOrdered | The voucher has a status of 'ordered' and cannot be used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0008 | VoucherStatusUnregistered | The voucher has a status of 'unregistered' and cannot be used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0009 | VoucherStatusDisposed | The voucher has a status of 'disposed' and cannot be used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0010 | VoucherStatusSecured | The voucher has a status of 'secured'. Please destroy this card. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0011 | VoucherStatusSoldInactive | The voucher has been sold but not yet activated. Please activate it for use. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0012 | VoucherStatusSold | The voucher is already sold. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0013 | VoucherFundsExhausted | The voucher funds are exhausted. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0014 | VoucherBalanceLow | The requested funds exceed the available balance on the voucher. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0015 | VoucherStatusCancelled | The voucher has a status of 'cancelled' and cannot be used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0016 | VoucherStatusReplaced | The voucher has a status of 'replaced' and cannot be used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0017 | VoucherStatusRedeemed | The voucher has a status of 'redeemed' and cannot be used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0018 | VoucherPreAuthNotFound | The voucher does not have a pre-authorisation. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0019 | VoucherPreAuthCancelled | The voucher has a cancelled pre-authorisation. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0020 | VoucherPreAuthRedeemed | The voucher has a redeemed pre-authorisation. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0021 | VoucherPreAuthExpired | The voucher's pre-authorisation has expired. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0022 | VoucherRedeemeAmountMismatch | The voucher pre-authorisation amount and the redeem amount do not match. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0023 | InvalidCreateVoucherItemNumber | The `itemNumber` provided does not exist within the configuration of voucher details in the item domain. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0101 | IdempotencyCheckFailed | Idempotency error: The key has already been used. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0102 | VoucherAndVoucherEventUpsertFailed | Failed to upsert the voucher and voucher event document. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0201 | MissingVoucherReference | Voucher reference is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0202 | MissingActivityDateTime | Activity date and time are required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0203 | MissingLocationCode | Location code is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0204 | MissingCurrency | Currency is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0205 | MissingRedeemAmount | Redeem amount is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0206 | MissingSourceSystem | Source system is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0207 | MissingPreAuthAmount | Pre-authorisation amount is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0208 | MissingPreAuthToken | Pre-authorisation token is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0209 | MissingVoucherPinCode | Voucher PIN code is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0210 | MissingAmount | Amount is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0211 | MissingTransactionReference | Transaction reference is required. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0212 | InvalidRedeemAmount | Invalid redeem amount. | [voucherValidationError](?type=voucherValidationError) |
| E-VCH-0213 | InvalidPreAuthAmount | Invalid pre-authorisation amount. | [voucherValidationError](?type=voucherValidationError) |

## Voucher Design Errors

The following list of error codes relates to the **Design** endpoints within the Voucher API.

| Short&nbsp;error&nbsp;code | JSON Path | Business Rule | Message | Error Type | Where&nbsp;used |
| -------- | -----------|--------- | --------| --------|  --------|
| E-VCH-0501 | ```rendering/templateParameters``` | Returned when `applicableFilters/medium` is set to **Digital** AND `rendering/templateParameters` is **empty**. | For a digital voucher, the rendering template details are mandatory. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0502 | ```rendering/template``` | Returned when the rendering collection is **populated** AND `rendering/template` is **empty**. | A rendering template name is mandatory. This needs to align with a template name in the Rendering API. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0503 | ```rendering/templateParameters /value``` | Returned when `rendering/templateParameters/type` is set to an **image value** AND `rendering/templateParameters/value` is **empty**. | The `rendering/templateParameters/value` is mandatory when `rendering/templateParameters/type` is an image. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0504 | ```rendering/templateParameters /value``` | Returned when `rendering/templateParameters/type` is set to an **image value** AND the text provided *cannot* be decoded using the base64 algorithm. | The template parameter type specifies an image, but the content provided is not encoded to base64 standards and cannot be accepted. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0505 | ```userParameters/maxLengthInclusive``` | Returned when `userParameters/type` is set to a **text value** AND `userParameters/maxLengthInclusive` is **empty**. | When a text parameter is specified within the design parameters, the maximum length of the user message is mandatory. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0506 | ```exampleImage``` | Returned when `exampleImageType` is **populated** AND `exampleImage` is empty. | A MIME type has been provided for an example image; this value is now mandatory. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0507 | ```exampleImage``` | Returned when `exampleImage` is **populated** AND the text provided cannot be decoded using the base64 algorithm. | The image content provided is not encoded to base64 standards and cannot be accepted. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0508 | ```exampleImageType``` | Returned when `exampleImage` is **populated** AND `exampleImageType` is **empty**. | Example image content has been provided; this value for MIME type is now mandatory. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0509 | ```exampleImageType``` | Returned when the string text does not contain the MIME type `image/svg`. | Unsupported MIME type. The following option is acceptable: `image/svg`. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0510 | ```rendering/templateParameters /type``` | Returned when the string text does not contain one of the MIME types: `text/plain`, `image/svg`. | Unsupported MIME type. The following options are acceptable: `text/plain`, `image/svg`. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0512 | ```rendering``` | Returned when a `rendering/templateParameters/code` or `userParameters/code` is duplicated within a single request. It is acceptable for a code to be reused across separate requests. | **Variation 1:** The code value assigned to `rendering/templateParameters` has been duplicated. This code must be unique within the whole design.<br /><br />**Variation 2:** The code value assigned to `userParameters` has been duplicated. This code must be unique within the whole design.<br /><br />**Variation 3:** The code value assigned to either `rendering/templateParameters` or `userParameters` has been duplicated. This code must be unique within the whole design. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0513 | ```userParameters/type``` | Returned when the string text does not contain the MIME type `text/plain`. | Unsupported MIME type. The following option is acceptable: `text/plain`. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0514 | ```userParameters/isRequired``` | Returned when `audience/target` = **All**, `userParameters/isRequired` = **true**, AND `userParameters/targetAudience` does **not** equal **All**. *Test Cases outlined below*. | When a design audience is set to 'All' and a `userParameter` is marked as required, then the `userParameter` design audience must also be set to 'All'. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0515 | ```userParameters/targetAudience``` | Returned when `audience/target` = **RetailOnly** AND `userParameters/targetAudience` = **CorporateOnly**. *Test Cases outlined below*. | When a design audience is set to 'RetailOnly', `userParameters` cannot be set to 'CorporateOnly'. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0516 | ```userParameters/targetAudience``` | Returned when `audience/target` = **CorporateOnly** AND `userParameters/targetAudience` = **RetailOnly**. *Test Cases outlined below*. | When a design audience is set to 'CorporateOnly', `userParameters` cannot be set to 'RetailOnly'. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0517 | ```audience/target``` | Returned when `audience/target` is not equal to **CorporateOnly** AND `audience/commercialCustomers/accountNumber` is populated. *Test Cases outlined below*. | When a design is configured for specific commercial customers, the audience target must be set to 'CorporateOnly'. | [validationError](?type=validationError)|PUT /design/{serverState}
| E-VCH-0518 | ```rendering/templateParameters /code``` | Returned when a request is received with `rendering/templateParameters/code` set to the value **“exampleImage”**. | The input 'exampleImage' is a restricted word and cannot be used for a template parameter code. Please nominate a different value. | [validationError](?type=validationError)|PUT /design/{serverState}

### Test Cases for **E-VCH-0514**, **E-VCH-0515**, **E-VCH-0516** & **E-VCH-0517**

The following table outlines the accepted and errored patterns for the design audience input data.

| | |  |
| -------- | -----------|----------
|`audience/target` = All `userParameters/isRequired` = true `userParameters/targetAudience` = RetailOnly **RETURN** error **E-VCH-0514**|`audience/target` = All `userParameters/isRequired` = true `userParameters/targetAudience` = CorporateOnly **RETURN** error **E-VCH-0514**|`audience/target` = All `userParameters/isRequired` = true `userParameters/targetAudience` = All **RETURN SUCCESS**
|`audience/target` = All `userParameters/isRequired` = false `userParameters/targetAudience` = RetailOnly **RETURN SUCCESS** | `audience/target` = All `userParameters/isRequired` = false `userParameters/targetAudience` = CorporateOnly **RETURN SUCCESS** |`audience/target` = All `userParameters/isRequired` = false `userParameters/targetAudience` = All **RETURN SUCCESS** |
|`audience/target` = RetailOnly `userParameters/isRequired` = true `userParameters/targetAudience` = RetailOnly **RETURN SUCCESS** |`audience/target` = RetailOnly `userParameters/isRequired` = true `userParameters/targetAudience` = CorporateOnly **RETURN** error **E-VCH-0515** | `audience/target` = RetailOnly `userParameters/isRequired` = true `userParameters/targetAudience` = All **RETURN SUCCESS**|
|`audience/target` = RetailOnly `userParameters/isRequired` = false `userParameters/targetAudience` = RetailOnly **RETURN SUCCESS** |`audience/target` = RetailOnly `userParameters/isRequired` = false `userParameters/targetAudience` = CorporateOnly **RETURN** error **E-VCH-0515**|`audience/target` = RetailOnly `userParameters/isRequired` = false `userParameters/targetAudience` = All **RETURN SUCCESS** |
|`audience/target` = CorporateOnly `userParameters/isRequired` = true `userParameters/targetAudience` = RetailOnly **RETURN** error **E-VCH-0516** | `audience/target` = CorporateOnly `userParameters/isRequired` = true `userParameters/targetAudience` = CorporateOnly **RETURN SUCCESS** |`audience/target` = CorporateOnly `userParameters/isRequired` = true `userParameters/targetAudience` = All **RETURN SUCCESS** |
| `audience/target` = CorporateOnly `userParameters/isRequired` = false `userParameters/targetAudience` = RetailOnly **RETURN** error **E-VCH-0516** | `audience/target` = CorporateOnly `userParameters/isRequired` = false `userParameters/targetAudience` = CorporateOnly **RETURN SUCCESS** |`audience/target` = CorporateOnly `userParameters/isRequired` = false `userParameters/targetAudience` = All **RETURN SUCCESS** |
|`audience/target` = All `audience/commercialCustomers/accountNumber` is populated **RETURN** error **E-VCH-0517** | `audience/target` = RetailOnly `audience/commercialCustomers/accountNumber` is populated **RETURN** error **E-VCH-0517** | `audience/target` = CorporateOnly `audience/commercialCustomers/accountNumber` is populated **RETURN SUCCESS** |

## Voucher Design Encode & Decode Errors

The following list of error codes relates to encoding and decoding a Voucher Design for use within the Bunnings ecosystem.

| Short&nbsp;error&nbsp;code | JSON Path | Business Rule | Message | Error Type | Where&nbsp;used |
| -------- | -----------|--------- | --------| --------|  --------|
| E-VCH-0601 | ```countryCode``` | Returned when data entry is not one of: **AU**, **NZ**. Note: This data is not case-sensitive; however, all data entry for this attribute is set to uppercase to align with ISO standards. | `countryCode` must be either 'AU' or 'NZ'. The input provided did not match. | [validationError](?type=validationError)|POST /encode
| E-VCH-0602 | ```itemNumber``` | Returned when data entry is not a seven digit integer. | The `itemNumber` provided must be exactly seven digits to allow for validation by the item domain. The data entry did not meet this criterion. | [validationError](?type=validationError)|POST /encode
| E-VCH-0603 | ```itemNumber``` | Returned when a request is received with an `itemNumber` not specified to a voucher. | The `itemNumber` provided is not supported by the voucher domain. | [validationError](?type=validationError)|POST /encode
| E-VCH-0604 | ```design/code``` | Returned when a request is received with a **voucher design** “design/code” which does *not* match **exactly** to a record with `isActive`=*true*. |The voucher design code provided does not match an active record. | [validationError](?type=validationError)|POST /encode
| E-VCH-0605 | ```design/code``` | Returned when the **voucher design** `countryCode` and the *encode input data* `countryCode` do not match. | The `countryCode` for the selected voucher design and the `itemNumber` do not match. | [validationError](?type=validationError)|POST /encode
| E-VCH-0606 | ```design/code``` | Returned when the **voucher design** has `isCustomerOrderable` = **false** AND the caller’s privileges do not allow `isCustomerOrderable` = **false**. | The voucher design is not available for use. | [validationError](?type=validationError)|POST /encode
| E-VCH-0607 | ```design/code``` | Returned when the **voucher design** has `audience/target` = **RetailOnly** AND the caller’s privileges do not allow `audience/target` = **RetailOnly**. | The voucher design is not available for use. | [validationError](?type=validationError)|POST /encode
| E-VCH-0608 | ```design/code``` | Returned when the **voucher design** has `audience/target` = **CorporateOnly** AND the caller’s privileges do not allow `audience/target` = **CorporateOnly**. | The voucher design is not available for use. | [validationError](?type=validationError)|POST /encode
| E-VCH-0609 | ```designHangsell/code``` | Returned when a request is received with a **voucher hangsell** “design/code” which does *not* match **exactly** to an `isActive`=**true** hangsell record. | The voucher hangsell code provided does not match an active record. | [validationError](?type=validationError)|POST /encode
| E-VCH-0620 | ```voucherToken``` | The `b-id` & `b-type` within the JWT token do **not** match the identified customer `b-id` & `b-type` on the request. Note: If this data is not provided on input, this error check is skipped. | The `voucherToken` was not issued to this customer. | [validationError](?type=validationError)|POST /decode
