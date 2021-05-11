# Problems

These are the shared problems for the Bunnings APIs. These problems are all compliant with [RFC 7807](https://tools.ietf.org/html/rfc7807) though some include extensions to the base application/problem+json type. Refer to the individual pages for schema definitions.

A complete description of Bunnings' Error Code design can be found [here](https://bunnings.atlassian.net/wiki/spaces/BAT/pages/5703997776/Problem+Details+Error+Handling). 

Problems returned in this format include a Problem Type URL that can be used to decide how to intepret the rest of the response. The URL is of the format  `https://problem.api.bunnings.com.au?type=<problemName>`, for example: https://problem.api.bunnings.com.au?type=invalidServerState.

## Problem types
Refer to the links below for details: