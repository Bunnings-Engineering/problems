# Checkout API error codes

| Code | Name |
| -------- | -------- |
| E-CHK-0001 | InvalidStreetType |
| E-CHK-0002 | EstimateAndAddressMutuallyExclusive |
| E-CHK-0003 | MarketplaceNotValidForNZ |
| E-CHK-0004 | MarketplaceNotValidForInstore |
| E-CHK-0005 | MarketplaceWithoutDetail |
| E-CHK-0006 | PreferredDeliveryTypeInvalidForContext |
| E-CHK-0007 | PreferredDateInvalidForContext |
| E-CHK-0008 | EstimateAndAddressMutuallyExclusiveInRequest |
| E-CHK-0009 | MarketplaceMustBeDelivery |
| E-CHK-0010 | InvalidAddressRef |
| E-CHK-0011 | DuplicateFulfilmentIds |
| E-CHK-0012 | DuplicateDeliveryAddressIds |
| E-CHK-0013 | InvalidFulfilmentRef |
| E-CHK-0014 | InvalidQuantity |
| E-CHK-0015 | InvalidGiftQuantity |
| E-CHK-0016 | MissingQuantity |
| E-CHK-0017 | InvalidSize |
| E-CHK-0018 | MissingFulfilmentRequirementRef |
| E-CHK-0019 | MissingItemNumber |
| E-CHK-0020 | DuplicateLineIds |
| E-CHK-0021 | CustomerDetailsAlsoHasAsMe |
| E-CHK-0022 | CustomerMemberOrCustomerMustBeSet |
| E-CHK-0023 | CustomerMemberIdMissing |
| E-CHK-0024 | CustomerMemberCantBePowerpass |
| E-CHK-0025 | CustomerSegmentsRequireMemberOrPowerpass |
| E-CHK-0026 | LogisticsApiCantDeliverToSuburb |
| E-CHK-0027 | PricingApiHasNoItemPrice | 
| E-CHK-0029 | LineNumberInvalid |
| E-CHK-0030 | StreetOrLotMustBeProvided |
| E-CHK-0031 | DeliveryAddressRequired |
| E-CHK-0032 | EstimatePostcodeRequired |
| E-CHK-0033 | ItemApiNotFound |
| E-CHK-0034 | MiraklApiNotFound |
| E-CHK-0035 | MiraklApiOfferNotFound |
| E-CHK-0036 | MiraklApiShippingZoneNotAllowed |
| E-CHK-0037 | MiraklApiShippingTypeNotAllowed |
| E-CHK-0038 | MiraklApiShippingZoneNotFound |
| E-CHK-0039 | LocationApiNotFound |
| E-CHK-0040 | LogisticsApiNotFound |
| E-CHK-0041 | PricingApiNotFound |
| E-CHK-0042 | ItemApiDetailNotReturned |
| E-CHK-0043 | LocationCodeNotCached |
| E-CHK-0044 | LocationConfigurationErrorsFound |
| E-CHK-0045 | PreferredDeliveryNotAllowedForDirect |
| E-CHK-0046 | ItemDeliveryOnly |
| E-CHK-0047 | ItemHasSizeButIsWholeUnitOnly |
| E-CHK-0048 | ItemLacksSizeButIsWholeUnitOnly |
| E-CHK-0049 | ItemHasNoValidSupplier |
| E-CHK-0050 | ItemHasNoZoningInformation |
| E-CHK-0051 | CantCheckoutUsingClosedInactiveStore |
| E-CHK-0052 | CantCheckoutRestrictedItem |
| E-CHK-0053 | CantCheckoutExclusiveItem |
| E-CHK-0054 | CantCheckoutItemTooLong |
| E-CHK-0055 | CantCheckoutItemTooMany |
| E-CHK-0056 | LocationNotCached |

### Shipment call:

| Code | Name |
| -------- | -------- |
| E-CHK-0200 | ShipmentsMissing |
| E-CHK-0201 | ShipmentsMissingMismatchCount |
| E-CHK-0202 | ShipmentsJwtInvalid |

### General:

| Code | Name |
| -------- | -------- |
| E-CHK-0300 | InvalidRequest |
