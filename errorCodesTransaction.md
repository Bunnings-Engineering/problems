# Transaction API error codes

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-TRA-0001 | InvalidTransactionRef | Invalid transaction reference. |
| E-TRA-0002 | InvalidPageSize | Invalid page size. |
| E-TRA-0003 | InvalidTransactionSource | Invalid transaction source. |
| E-TRA-0004 | InvalidLocation | Invalid location. |
| E-TRA-0005 | InvalidItemType | Invalid item type. |
| E-TRA-0006 | InvalidItemNumber | Invalid item number. |
| E-TRA-0007 | InvalidItemBarcode | Invalid item barcode. |
| E-TRA-0008 | InvalidCustomerType | Invalid customer type. |
| E-TRA-0009 | InvalidTenderType | Invalid tender type. |
| E-TRA-0010 | InvalidEftAccountType | Invalid EFT account type. |
| E-TRA-0011 | InvalidEftCardType | Invalid EFT card type. |
| Short&nbsp;error&nbsp;code | Name | Description | Error&nbsp;Type |
| -------- | -------- | -------- | -------- |
| E-TRA-0001 | InvalidTransactionRef | Invalid transaction reference - transaction reference must be 20 characters | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0002 | InvalidPageSize | Invalid page size - page size cannot be less than 20 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0003 | InvalidTransactionSource | Invalid transaction source - allowed values are INSTORE, ECOMMERCE | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0004 | InvalidLocation | Location is invalid. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0005 | InvalidItemType | Invalid item type - allowed values are ITEM, BARCODE | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0006 | InvalidItemNumber | Invalid item number - item number must be 7 digits long | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0007 | InvalidItemBarcode | Invalid item barcode - item barcode must be between 8 and 14 digits long | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0008 | InvalidCustomerType | Invalid customer type - allowed values are RETAIL_CUSTOMER, TEAM_MEMBER, POWERPASS, POWERPASSCARDUSER | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0009 | InvalidTenderType | Invalid tender type | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0010 | InvalidEftAccountType | Invalid EFT Account type - allowed values are CHEQUE, CREDIT, SAVINGS | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0011 | InvalidEftCardType | Invalid EFT card type | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0012 | InvalidPowerPassCardHash | Invalid PowerPass card hash | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=validationError">validationError</a> |
| E-TRA-0013 | InvalidTrxNumberForTheBasket | Transaction number is not assigned to basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0014 | InvalidShoppingLocationForTheBasket | Basket doesn't have a valid shopping location. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0015 | NoLinesAddedToTheBasket | Basket doesn't have any lines. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0016 | InvalidItemAddedToTheBasket | Lines don't have valid item assigned for the basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0017 | InvalidItemNumberAddedToTheBasket | Invalid item number used in basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0018 | NoPaymentInfoSetForTheBasket | No payment information provided for the basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0019 | NoCustomerTypeSetForTheBasket | No customer type provided for the basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0020 | NoFulfilmentOptionSelected | Basket doesn't have any fulfilment selected | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0021 | NoCheckoutCalledOnBasket | Basket requires to go through checkout before submitting for transaction | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0022 | NoFulfilmentCalculated | Basket requires to calculate fulfilments through checkout before submitting for transaction | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0023 | UnsupportedBasket | Basket submitted is not supported for basket submission. Error message provides more information on details. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0024 | UnsupportedEnumSetForTheBasket | The submitted value is not valid and cannot be converted to an accepted enum. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0025 | InvalidFlybuys | Incorrect flybuys information provided in basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0026 | InvalidOnePass | Incorrect OnePass information provided in basket. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0500 | MultipleItemsNotFound | No corresponding item details found for all or some of the item numbers: 1234567, 1122334 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0501 | ItemNotFound | No corresponding item details found in item domain for the item number: 1234567 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0502 | ItemArchived | Item is archived. Item number: 1234567 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0503 | InvalidItemBarcode | No corresponding item barcode found in item domain for the item number: 1234567 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0504 | InvalidCountryCode | Location details cannot be retrieved due to an invalid country code on the basket | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0505 | LocationNotFound | Shopping location details cannot be found for the location code | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0506 | InvalidLocationCode | Shopping location is not valid. Please ensure that it is a store, it's trading and not closed. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0507 | UnsupportedLocationCode | For MVP, only following location types and sub types are supported. Types: "SF", "TD", "WA". Sub Types: "TDC", "CAFE", "WA", "SF" | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0508 | MultiplePriceDetailsNotFound | No corresponding price details found for all or some of the items. | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0509 | TaxCodeMappingNotFound | The selling tax id cannot be mapped from the selling tax code provided by Checkout | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0510 | TeamMemberDetailsNotFound | No corresponding team member details found for team member number: 123456 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0511 | TeamMemberCardNotFound | No corresponding active card can be found for the team member: barcode E123456 | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0512 | UnsupportedPaymentProvider | Unsupported payment provider, only supporting BunCredit, BPOINT and Click | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
| E-TRA-0513 | NoPaymentInfoSetForTheBasket | Payments not set for the basket | <a target="_blank" href="https://problem.api.bunnings.com.au/?type=basketSubmissionError">basketSubmissionError</a> |
