# Ordering API error codes

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-ORD-0006 | ServiceHttpResponse | Downstream service is unavailabe. Please check the error message or investigate the logs for futher information. |
| E-ORD-0007 | LocationValidation | Location is invalid. Please check the error message or investigate the logs for futher information. |
| E-ORD-0008 | PriceValidation | Pricing in invalid. Please check the error message or investigate the logs for futher information. |
| E-ORD-0009 | CheckoutValidation | Checkout validation failed. Please check the error message or investigate the logs for futher information. |
| E-ORD-2000 | BasketSubmission | Basket processing has failed. Please check the error message or investigate the logs for futher information. |
| E-ORD-1030 | DataStore | Basket processing has failed due to an error in the downstream data store. Please check the error message or investigate the logs for futher information. |
| E-ORD-0025 | FlybuysValidation | Flybuys information is incorrect for order, please reverify and try again. |
| E-ORD-0026 | OnePassValidation | OnePass information is incorrect for order, please reverify and try again. |

# General:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-ORD-0010 | GeneralValidation | A bad request was passed. One or more fields were invalid. |

# Validation Errors:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-ORD-0018 | NoMatchingEnteredLine | Basket doesn't have a matching entered line item for computed line. |
| E-ORD-0027 | InvalidLoyaltyRef | The loyalty type(s): {Types} is/are duplicated, only one type is permitted for an order, please rectify and try again. |
| E-ORD-0030 | InvalidLoyaltyProgram | The loyalty program is not supported by Ordering. Please remove and try again. |
| E-ORD-0101 | CentraPayValidation | When submitting an order for with the payment provider Centrapay, the providerAccount must equal FARMLANDS. |
| E-ORD-0102 | ConversionErrorDecimal | Conversion error from string to decimal |
| E-ORD-0103 | MaxLengthExceeded | string length exceeded, maximum length permitted is {MaxLength}. |
| E-ORD-0104 | EnumerationMismatch | Unsupported string value, valid options include {enumList}. |
| E-ORD-0105 | RegexMismatch | Data entry does not meet Regex |
| E-ORD-0106 | InvalidLength | Invalid Length |

# Basket Processing Errors:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-ORD-0200 | ComputedMandatory | Basket has not passed Checkout validation, please reverify and try again. |
| E-ORD-0201 | UnknownFulfilmentType | The basket includes a fulfilment type of Unknown. This is an invalid option. |
| E-ORD-0202 | InvalidFulfilmentType | This end point only supports fulfilments for DeliveryToCustomer & DigitalDeliveryToCustomer. Please process this request through POST /basketRef/{basketRef}/order. |
| E-ORD-0203 | InvalidDigitalFulfilmentType | The basket includes a fulfilment type of DigitalDeliveryToCustomer. A dispatch email address has not been provided. |
| E-ORD-0204 | InvalidDeliveryFulfilmentType | The basket includes a fulfilment type of DeliveryToCustomer. A delivery address has not been provided. |
| E-ORD-0205 | InvalidGiftCardOrder | The basket includes a fulfilment type of DigitalDeliveryToCustomer. The lineType must be set to GIFTCARDORDER. |
| E-ORD-0206 | DesignTokenMandatory | The basket includes a fulfilment type of DigitalDeliveryToCustomer. A gift card digital design token has not been provided. |
| E-ORD-0207 | FulfilmentOptionsNotResolved | The basket has not nominated a computed fulfilment option, this is mandatory for submission to ordering. Please nominate and try again. |
| E-ORD-0208 | ItemNumberInvalid | itemNumber must equal a length of 7 numeric characters. |
| E-ORD-0210 | ConsiderationPaymentMandatory | Payment details have not been provided. Please update and try again. |
| E-ORD-0211 | UnsupportedPaymentProvider | Payment provider is unsupported by the ordering domain. Please nominate a different provider and try again. Valid options include: [{enumList}] |
| E-ORD-0212 | CustomerTypeConsumer | A consumer customer has been nominated, person details are mandatory. |
| E-ORD-0213 | CustomerTypeCommercial | A commercial customer has been nominated, account details are mandatory. |
| E-ORD-0214 | EnteredMandatory | This basket cannot be processed by Ordering domain as entered lines are missing. Please nominate and try again. |
| E-ORD-0215 | EnteredFulfilmentMandatory | This basket cannot be processed by Ordering domain without a fulfilment option nominated. Please nominate and try again. |
| E-ORD-0216 | EnteredLinesItemMandatory | Items details are missing. Please nominate and try again. |
| E-ORD-0217 | OrderNumMandatory | Order number is mandatory for all ecommerce requests. Please nominate and try again. |
| E-ORD-0218 | GiftcardDesignTokenMandatory | A line type of GIFTCARDORDER must have a design token populated. Please nominate and try again. |
| E-ORD-0219 | GiftcardCardNumberMandatory | A line type of GIFTCARD must have a card number populated. Please nominate and try again. |
| E-ORD-0220 | UnsupportedLineType | This end point currently only supports lineType of GIFTCARDORDER. Please process this request through PUT /basket/{serverState}/order. |
| E-ORD-0221 | GiftcardCustomerToCollectUnsupported | The basket includes a fulfilment type of CustomerToCollect. This option does not support the lineType of GIFTCARDORDER. |
| E-ORD-0222 | InvalidGiftcardFulfilment | A GIFTCARDORDER must be on an independent fulfilment. It cannot be mixed with other lineTypes due to dispatch occurring from a central location. |
| E-ORD-0223 | GiftcardDetailsMandatory | A line type of GIFTCARD/GIFTCARDORDER must have gift card details populated. Please nominate and try again. |
| E-ORD-0224 | InvalidConcatenatedAddress | For compatibility the address input data for "premise", "lotNumber", "streetNumber" and "streetName" has been concatenated. This joined data either exceeds the allowed length of 100 characters or is empty. Please provide valid address information. |
| E-ORD-0225 | InvalidStreetType | Basket doesn't have a valid address street type. |
| E-ORD-0226 | InvalidOrderNumberFormat | Order number is in invalid format. It needs to start with W and follow by 9 digits. |
| E-ORD-0228 | InvalidCountryCode | Country code is invalid. It needs to be either AU or NZ |
| E-ORD-0229 | InvalidPaymentDetails | Person and Account details can not be defined together. |
| E-ORD-0230 | InvalidStateCode | Invalid Australian State, allowed values: {States}. |
| E-ORD-0231 | InvalidIdentityProvider | Invalid identity provider. the value must be: {Providers} |
| E-ORD-0232 | InvalidIdentityId | Invalid identity id. the value must be a GUID |
| E-ORD-0233 | InvalidContactEmail | The contact email is invalid |
| E-ORD-0234 | InvalidCommercialAccount | A commercial customer has been nominated, commercial account number is mandatory. |
| E-ORD-0235 | InvalidGiftCardSize | Invalid GC size. |
| E-ORD-0236 | InvalidPaymentProvider | Payment provider is unsupported by the ordering domain. Please nominate a different provider and try again. Valid options include: [ BPOINT, BRAINTREE, PAYPAL, ZIPPAY, CLICK, AFTERPAY, CENTRAPAY, VOUCHER ] |
| E-ORD-0237 | InvalidPaymentAmount | Invalid payment amount for {paymentType}. |
| E-ORD-0238 | MissingCustomerAccForBasketCredit | Customer Account is required for Basket Credit. |
| E-ORD-0239 | InvalidBalanceOnCredit | When balance on credit is set, amount of credit cannot be 0. |
| E-ORD-0240 | InvalidAmountOfCredit | Credit. Amount of credit cannot be empty when no balance on credit specified. |
| E-ORD-0241 | InvalidIpAddress | Invalid IP address. |
| E-ORD-0242 | InvalidVoucherPaymentDetails | When submitting an order with the payment provider VOUCHER, the providerAccount must equal Bunnings and the referenceType must equal PREAUTH. |
| E-ORD-0250 | MissingMandatoryData | Mandatory field and not present. |

# Marketplace Specific Errors:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-ORD-0243 | MissingContactEmailForTradeMarketPlace | Contact email is required for marketplace orders. |
| E-ORD-0244 | ProvideContactFirstAndLastNameForTradeMarketPlace | Please provide both first and last name for marketplace orders. |
| E-ORD-0245 | AllTradeMarketPlaceFulfilmentsShareContactInfo | All fulfilments must use the same contact information. |
| E-ORD-0246 | InvalidContactInfo | Provide either contact name or first and last name, but not both. |
| E-ORD-0247 | MarketPlaceNotSupportedForPowerPassCredit | PowerPass credit cannot be used for Marketplace items. |
| E-ORD-0251 | OnlyMarketplaceLinesInMarketplaceFulfilments | Marketplace fulfilments can only contain marketplace lines. |
| E-ORD-0252 | MarketplaceFulfilmentsMustHaveDeliveryTypeDirect | Marketplace fulfilments must have a delivery type of Direct. |
