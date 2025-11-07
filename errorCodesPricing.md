# Pricing Domain error messages

This catalogue of error codes are generated from the Pricing Domain which is comprised of the below components.  

## General Pricing Validation

The below can be found across any endpoint which uses a price id as an input.

| Short&nbsp;error&nbsp;code | Name                                                     | Description                                                                 |
| -------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------- |
| E-PRI-GEN-0001             | InvalidPriceId                                           | Price Id is invalid.                                                        |


## Markdown Pricing Error Codes

| Short&nbsp;error&nbsp;code | Name                                                     | Description                                                                 |
| -------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------- |
| E-PRI-MD-0001              | ItemNumberRequired                                       | ItemNumber is required.                                                     |
| E-PRI-MD-0002              | LocationCodeRequired                                     | LocationCode is required.                                                   |
| E-PRI-MD-0003              | ReasonCodeRequired                                       | ReasonCode is required.                                                     |
| E-PRI-MD-0004              | QtyMustBeGreaterThanZero                                 | Qty must be greater than 0.                                                 |
| E-PRI-MD-0005              | SizeMustBeGreaterThanZero                                | Size must be greater than 0.                                                |
| E-PRI-MD-0006              | TeamMemberNumberRequired                                 | TeamMemberNumber is required.                                               |
| E-PRI-MD-0007              | TeamMemberNumberMustBeExactlySixCharacters               | TeamMemberNumber must be exactly 6 characters.                              |
| E-PRI-MD-0008              | HostnameRequiredWhenPOSRequest                           | Hostname is required when it's a POS request.                               |
| E-PRI-MD-0009              | ServerStateRequired                                      | ServerState is required.                                                    |
| E-PRI-MD-0010              | PriceMustBeGreaterThanZero                               | Price must be greater than 0.                                               |
| E-PRI-MD-0011              | PriceCannotBeNegative                                    | Price cannot be negative.                                                   |
| E-PRI-MD-0012              | PriceMustExist                                           | Price cannot be null.                                                       |


