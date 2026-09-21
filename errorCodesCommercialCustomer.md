# Commercial Customer API error codes

| Short&nbsp;error&nbsp;code | Name | Description |
| -------- | -------- | -------- |
| E-CUC-0004 | UsernameNotAvailable | Username is not available. |
| E-CUC-0005 | PasswordStrength | Password strength is not strong enough. |
| E-CUC-0006 | InvalidStreetNumber | Either a Lot Number or a Street Number is required. |
| E-CUC-0008 | InvalidCountry | Country is not supported. |
| E-CUC-0011 | EmailAlreadyRegistered | This email address is already registered in the system. |
| E-CUC-0012 | InvalidCardNumber | Card number is invalid. |
| E-CUC-0013 | InvalidAccountNumber | Account number is invalid. |
| E-CUC-0014 | InvalidCardOrAccountNumber | Card number or account number is invalid. |
| E-CUC-0015 | InvalidSecurityAnswer | The answer to a security question cannot be the user's password or user name, and cannot contain part of the question. |
| E-CUC-0016 | InvalidAssociationAccountNotSame | Invalid association. The card and the user do not belong to the same account. |
| E-CUC-0017 | AssociationExists | Association already exists. |
| E-CUC-0018 | AccessTokenExpired| Access token has expired. |
| E-CUC-0019 | InvalidAccessToken| Invalid access token. |
| E-CUC-0020 | AssociationDoesntExist | Association does not exist. |
| E-CUC-0021 | IneligibleAccount | account number entered is not eligible for online access request. |
| E-CUC-0022 | InvalidCardLinking | cannot change card link on conformance level 2. |
| E-CUC-0023 | InvalidPin | pin provided is not valid. |
| E-CUC-0024 | InvalidTeamMemberId | teamMemberId provided is not valid. |
| E-CUC-0025 | InvalidLocationCode | locationCode provided is not a valid Bunnings code. |
| E-CUC-0026 | InvalidRegisterId | regsiterId provided is not valid. |
| E-CUC-0027 | IdSightedMissing | idSighted is missing. Please provide the type of the ID that you are verifying customer's identity with. |
| E-CUC-0028 | CardNumberMissing | cardNumber is missing. This is mandatory for physical cards. |
| E-CUC-0029 | CardNumberNotMatching | cardNumber is not matching. Please review and provide the cardNumber matching to the card that you are trying to activate. |
| E-CUC-0030 | InvalidIpAddress | ipAddress is not valid. |
| E-CUC-0031 | InvalidAddressStructure | The provided address does not comply with the requirements for the account. Customers on accounts with Conformance level greater than 1 are required to provide a detailed address with streetNumber, streetName, and streetType. |
| E-CUC-0032 | InvalidMarketingFlag | The provided marketing flag is not valid as isReceiveMarketing is a boolean. The expected values are "true" or "false". |
| E-CUC-0033 | InvalidContextInfo | The value should be provided as a string based key–value dictionary. |
| E-CUC-0034 | MissingDeviceName | deviceName must be provided. |
| E-CUC-0035 | MaximumDevicesReached | Maximum of 2 devices can be linked to this card. maximum number is reached. |
| E-CUC-0036 | InvalidCardReference | The provided cardReference is not valid. Use a valid cardBId or hashedCardNumber. |
| E-CUC-0037 | InvalidCardBId | The provided cardBId is not valid. Use a valid cardBId. |
| E-CUC-0038 | AccountContactDoesntExist | Account Contact does not exist. |
| E-CUC-0039 | IneligibleForContactUpdate | Account Contact does not exist. |
| E-CUC-0040 | IneligibleForSecurityQuestionsUpdate | Security Questions cannot be updated for the selected account. |
| E-CUC-0041 | IneligibleForPricingDetailUpdate | Pricing details cannot be updated for the selected account. |
| E-CUC-0042 | InvalidSalesRepId | SalesRepId must contain only numbers. |
| E-CUC-0043 | IneligibleForUsernameUpdate | Username cannot be updated for the selected user. |
| E-CUC-0044 | IneligibleForSegmentUpdate | secondarySegment cannot be updated for the selected account. |
| E-CUC-0045 | MissingIncludeCurrentCardDetailsFlag | includeReplacedCards must be used with includeCurrentCardDetails set to true. |
