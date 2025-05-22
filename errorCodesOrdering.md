# Ordering API error codes

| Short&nbsp;error&nbsp;code | Name                | Description                                                                                                                                                    |
| --------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E-ORD-0006                  | ServiceHttpResponse | Downstream service is unavailable. Please check the error message or investigate the logs for further information.                                               |
| E-ORD-0007                  | LocationValidation  | Location is invalid. Please check the error message or investigate the logs for further information.                                                           |
| E-ORD-0008                  | PriceValidation     | Pricing is invalid. Please check the error message or investigate the logs for further information.                                                            |
| E-ORD-0009                  | CheckoutValidation  | Checkout validation failed. Please check the error message or investigate the logs for further information.                                                    |
| E-ORD-2000                  | BasketSubmission    | Basket processing has failed. Please check the error message or investigate the logs for further information.                                                  |
| E-ORD-1030                  | DataStore           | Basket processing has failed due to an error in the downstream data store. Please check the error message or investigate the logs for further information. |
| E-ORD-0025                  | FlybuysValidation   | Flybuys information is incorrect for the order, please re-verify and try again.                                                                                |
| E-ORD-0026                  | OnePassValidation   | OnePass information is incorrect for the order, please re-verify and try again.                                                                                |

## General

| Short&nbsp;error&nbsp;code | Name              | Description                                                        |
| --------------------------- | ----------------- | ------------------------------------------------------------------ |
| E-ORD-0010                  | GeneralValidation | A bad request was passed. One or more fields were invalid.         |
