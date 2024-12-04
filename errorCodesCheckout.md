# Checkout API error codes

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-CHK-0001 | InvalidStreetType | The address' street type is not one of the standard values. Note that both full and abbreviated names can be used, for example: "st" or "street." |
| E-CHK-0002 | EstimateAndAddressMutuallyExclusive | The request received specified both a delivery address as well an requested an estimate for a postcode. These are mutually exclusive. |
| E-CHK-0003 | MarketplaceNotValidForNZ | Marketplace purchases are not supported in New Zealand. |
| E-CHK-0004 | MarketplaceNotValidForInstore | Marketplace purchases can only be made on-line and not in-store. |
| E-CHK-0005 | MarketplaceWithoutDetail | Marketplace orders must include the details of the specified offer. |
| E-CHK-0006 | PreferredDeliveryTypeInvalidForContext | It is not possile to specify this preffered delivery type for this context, for example: courier delivery with on-line orders. |
| E-CHK-0009 | MarketplaceMustBeDelivery | Marketplace items must have a delivery fulfilment type. |
| E-CHK-0010 | InvalidAddressRef | A fulfilment requirements has an invalid address references. |
| E-CHK-0011 | DuplicateFulfilmentIds | Multiple fulfilment requirements share the same ID. |
| E-CHK-0012 | DuplicateDeliveryAddressIds | Multiple addresses share the same ID. |
| E-CHK-0013 | InvalidFulfilmentRef | A line has an invalid fulfilment requirements references. |
| E-CHK-0014 | InvalidQuantity | The line's quantity was less than 1. | 
| E-CHK-0015 | InvalidGiftQuantity | The line's quantity must be 1 for gifts. | 
| E-CHK-0016 | MissingQuantity | The quantity field is required for the line type. |
| E-CHK-0017 | InvalidSize | The size value is less than 0. |
| E-CHK-0018 | MissingFulfilmentRequirementRef | The line requires a fulfilment requirement reference. |
| E-CHK-0019 | MissingItemNumber | The line requires an item number. |
| E-CHK-0020 | DuplicateLineIds | Multiple lines share the same ID. |
| E-CHK-0021 | CustomerDetailsAlsoHasAsMe | The customer details have AsMe set but also include a PowerPassAccountNumber or TeamMemberId. Furthermore, it is not valid to pass TeamMemberCustomer or segments. |
| E-CHK-0022 | CustomerMemberOrCustomerMustBeSet | The call must include a TeamMemberId or TeamMemberCustomer. |
| E-CHK-0023 | CustomerMemberIdMissing | If a TeamMemberCustomer is passed then a TeamMemberId is required. |
| E-CHK-0024 | CustomerMemberCantBePowerpass | If a TeamMemberID is passed it cannot have a PowerPassAccountNumber. |
| E-CHK-0025 | CustomerSegmentsRequireMemberOrPowerpass | If segments are passed then either a TeamMemberID or PowerPassAccountNumber must be passed. |
| E-CHK-0026 | BunningsDoesNotDeliverToSuburb | Bunnings does not delivery to the requested suburb. |
| E-CHK-0027 | ItemHasNoItemPrice | No price can be found for the item. |
| E-CHK-0029 | LineNumberInvalid | The line number is must be greater than 0. |
| E-CHK-0030 | StreetOrLotMustBeProvided | A street or lot number must be included with an address. |
| E-CHK-0031 | DeliveryAddressRequired | An address is required for delivery fulfilments unless they are an estimate. |
| E-CHK-0032 | EstimatePostcodeRequired | If an estimate is requested then a EstimatePostcodeRequired must be provided. | 
| E-CHK-0033 | ItemNotFound | The item was not found. |
| E-CHK-0035 | MarketplaceOfferNotFound | The Offer passed was not found in the Marketplace. |
| E-CHK-0036 | MarketplaceShippingZoneNotAllowed | The Offer cannot be delivered to the requested address. |
| E-CHK-0037 | MarketplaceShippingTypeNotAllowed | The Offer cannot be delivered using the shipping type. |
| E-CHK-0038 | MarketplaceShippingZoneNotFound | A shipping zone has not been set up for the postcode. |
| E-CHK-0039 | LocationNotFound | The location could not be found. |
| E-CHK-0040 | LogisticsApiNotFound | Delivery response could not be found. |
| E-CHK-0041 | ItemPriceNotFound | A price could not found for the item. |
| E-CHK-0042 | ItemDetailsNotFound | An item could be found with an item location but details were not available for it. |
| E-CHK-0043 | LocationCodeNotCached | The locationCode could not be found. |
| E-CHK-0044 | LocationConfigurationErrorsFound | The location was found but has configuration errors. |
| E-CHK-0045 | PreferredDeliveryNotAllowedForDirect | The item has a preferred delivery type of direct delivery however the item is not set for direct delivery. |
| E-CHK-0046 | ItemDeliveryOnly | The item is marked as delivery only at the location. |
| E-CHK-0047 | ItemHasSizeButIsWholeUnitOnly | The item has specified a size, but the item is whole unit only. |
| E-CHK-0048 | ItemLacksSizeButIsWholeUnitOnly | The item requires a size since the item is not whole unit only. |
| E-CHK-0049 | ItemHasNoValidSupplier | The item has no Suppliers for the location. |
| E-CHK-0050 | ItemHasNoZoningInformation | Zoning information could not be found for the item. |
| E-CHK-0051 | CantCheckoutUsingClosedInactiveStore | A checkout was attempted on a closed or inactive store. |
| E-CHK-0052 | CantCheckoutRestrictedItem | A checkout was attempted for a restricted item. |
| E-CHK-0053 | CantCheckoutExclusiveItem | A checkout was attempted for an exclusive item. |
| E-CHK-0054 | CantCheckoutItemTooLong | The item exceeds the maximum length. |
| E-CHK-0055 | CantCheckoutItemTooMany | The item order exceeds the maximum quantity. |
| E-CHK-0056 | LocationNotCached | Location has not been set up for country |
| E-CHK-0057 | MarketplaceMustGoToSameAddress | Marketplace items must be delivered to the same address |
| E-CHK-0058 | TimberTallySizeMismatch | TimberTally failed match sizes |
| E-CHK-0059 | LocationDoesntHandleCollection | Location does not handle 'Click&Collect' or 'Drive&Collect' for item(s) |
| E-CHK-0060 | LocationDoesntHandleDelivery | Location does not handle 'Click&Deliver' for item(s) |
| E-CHK-0061 | ItemLessThanMinSize | Item is less than the minimum allowed size |
| E-CHK-0062 | ItemMoreThanMaxSize | Item is more than the maximum allowed size |
| E-CHK-0063 | ItemInvalidSizeIncrement | Item does not match the allowed size increment |
| E-CHK-0064 | FulfilmentDataNotNeeded | A line includes a FulfilmentRef which is not needed for the checkoutFulfilmentRulesSet value |
| E-CHK-0065 | ContextNotValidForRoles | The sales context is not valid for the security roles provided |
| E-CHK-0066 | MarketplaceNotSupportedByContext | Marketplace items are not supported for this context |
| E-CHK-0067 | CustomerCantTransactInThisState | The customer account cannot transact in this state |
| E-CHK-0068 | StateNotAllowedForCountry | The state cannot be supplied for this country |
| E-CHK-0069 | StateMandatoryForCountry | The state must be supplied for this country |
| E-CHK-0070 | AddressCountryMandatory | The country is mandatory for address |
| E-CHK-0071 | AddressLocalityMandatory | The locality/suburb is mandatory for address |
| E-CHK-0072 | MarketplaceNotSupportedByUser | Marketplace items are not supported for this type of user |
| E-CHK-0073 | InvalidStateForCountry | The state is invalid for the country |
| E-CHK-0074 | SpecifiedItemNotSellable | The item is not sellable |
| E-CHK-0075 | ActualItemNotSellable | The item mapped is not sellable |
| E-CHK-0076 | DeliveryAddressNotSupportedByUser | Delivery addresses are not supported for this user |
| E-CHK-0077 | ItemNotFoundAtLocation | The item is not found at Location |
| E-CHK-0078 | ItemNotFoundForCountry | The item is not found in the country |
| E-CHK-0079 | StoresNotFoundForCountry | Stores not found for Country |
| E-CHK-0080 | ServerStateNotFoundForLocation | Exceptional Trading Hours details cannot be fetched |
| E-CHK-0081 | MiraklOrdersNotFoundForMarketLine | Mirakl order not found for market line |

# Shipment call:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-CHK-0200 | ShipmentsMissing | Shipments must be passed to the API. |
| E-CHK-0201 | ShipmentsMissingMismatchCount | Mismatch between the number of shipments and tokens. |
| E-CHK-0202 | ShipmentsJwtInvalid | Something was wrong with the token. Refer to logs for more details. |
| E-CHK-0203 | ShipmentsTokensMixLocations | Shipment request's tokens mix shopping locations. |

# Validation call:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-CHK-0250 | ValidationFulfilmentsMissing | Fulfilments must be passed to the API. |
| E-CHK-0251 | ValidationFulfilmentMissingMismatchCount | Fulfilment counts mismatch. |
| E-CHK-0252 | ValidationFulfilmentsJwtInvalid | There was an error with the fulfilment token. |
| E-CHK-0253 | ValidationFulfilmentLinesMissing | Fulfilment lines must be passed to the API. |
| E-CHK-0254 | PriceNotFound | Price was not found for a specified PriceId |
| E-CHK-0255 | ValidationFulfilmentLinesDuplicated | Duplicate line numbers have been provided for fulfilfment lines. |

# General:

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-CHK-0300 | InvalidRequest | A bad request was passed. One or more fields wre invalid. |
| E-CHK-0301 | SystemError | External API resonded with Problem details |
