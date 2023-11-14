"""
Type annotations for savingsplans service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/type_defs.html)

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import CreateSavingsPlanRequestRequestTypeDef

    data: CreateSavingsPlanRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    CurrencyCodeType,
    SavingsPlanOfferingFilterAttributeType,
    SavingsPlanOfferingPropertyKeyType,
    SavingsPlanPaymentOptionType,
    SavingsPlanProductTypeType,
    SavingsPlanRateFilterAttributeType,
    SavingsPlanRateFilterNameType,
    SavingsPlanRatePropertyKeyType,
    SavingsPlanRateServiceCodeType,
    SavingsPlanRateUnitType,
    SavingsPlansFilterNameType,
    SavingsPlanStateType,
    SavingsPlanTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateSavingsPlanRequestRequestTypeDef",
    "CreateSavingsPlanResponseTypeDef",
    "DeleteQueuedSavingsPlanRequestRequestTypeDef",
    "DescribeSavingsPlanRatesRequestRequestTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesRequestRequestTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingsRequestRequestTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansRequestRequestTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParentSavingsPlanOfferingTypeDef",
    "ResponseMetadataTypeDef",
    "SavingsPlanFilterTypeDef",
    "SavingsPlanOfferingFilterElementTypeDef",
    "SavingsPlanOfferingPropertyTypeDef",
    "SavingsPlanOfferingRateFilterElementTypeDef",
    "SavingsPlanOfferingRatePropertyTypeDef",
    "SavingsPlanOfferingRateTypeDef",
    "SavingsPlanOfferingTypeDef",
    "SavingsPlanRateFilterTypeDef",
    "SavingsPlanRatePropertyTypeDef",
    "SavingsPlanRateTypeDef",
    "SavingsPlanTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

_RequiredCreateSavingsPlanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSavingsPlanRequestRequestTypeDef",
    {
        "savingsPlanOfferingId": str,
        "commitment": str,
    },
)
_OptionalCreateSavingsPlanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSavingsPlanRequestRequestTypeDef",
    {
        "upfrontPaymentAmount": str,
        "purchaseTime": Union[datetime, str],
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSavingsPlanRequestRequestTypeDef(
    _RequiredCreateSavingsPlanRequestRequestTypeDef, _OptionalCreateSavingsPlanRequestRequestTypeDef
):
    pass

CreateSavingsPlanResponseTypeDef = TypedDict(
    "CreateSavingsPlanResponseTypeDef",
    {
        "savingsPlanId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteQueuedSavingsPlanRequestRequestTypeDef = TypedDict(
    "DeleteQueuedSavingsPlanRequestRequestTypeDef",
    {
        "savingsPlanId": str,
    },
)

_RequiredDescribeSavingsPlanRatesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSavingsPlanRatesRequestRequestTypeDef",
    {
        "savingsPlanId": str,
    },
)
_OptionalDescribeSavingsPlanRatesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSavingsPlanRatesRequestRequestTypeDef",
    {
        "filters": List["SavingsPlanRateFilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeSavingsPlanRatesRequestRequestTypeDef(
    _RequiredDescribeSavingsPlanRatesRequestRequestTypeDef,
    _OptionalDescribeSavingsPlanRatesRequestRequestTypeDef,
):
    pass

DescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlanRatesResponseTypeDef",
    {
        "savingsPlanId": str,
        "searchResults": List["SavingsPlanRateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSavingsPlansOfferingRatesRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesRequestRequestTypeDef",
    {
        "savingsPlanOfferingIds": List[str],
        "savingsPlanPaymentOptions": List[SavingsPlanPaymentOptionType],
        "savingsPlanTypes": List[SavingsPlanTypeType],
        "products": List[SavingsPlanProductTypeType],
        "serviceCodes": List[SavingsPlanRateServiceCodeType],
        "usageTypes": List[str],
        "operations": List[str],
        "filters": List["SavingsPlanOfferingRateFilterElementTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    {
        "searchResults": List["SavingsPlanOfferingRateTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSavingsPlansOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsRequestRequestTypeDef",
    {
        "offeringIds": List[str],
        "paymentOptions": List[SavingsPlanPaymentOptionType],
        "productType": SavingsPlanProductTypeType,
        "planTypes": List[SavingsPlanTypeType],
        "durations": List[int],
        "currencies": List[CurrencyCodeType],
        "descriptions": List[str],
        "serviceCodes": List[str],
        "usageTypes": List[str],
        "operations": List[str],
        "filters": List["SavingsPlanOfferingFilterElementTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    {
        "searchResults": List["SavingsPlanOfferingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSavingsPlansRequestRequestTypeDef = TypedDict(
    "DescribeSavingsPlansRequestRequestTypeDef",
    {
        "savingsPlanArns": List[str],
        "savingsPlanIds": List[str],
        "nextToken": str,
        "maxResults": int,
        "states": List[SavingsPlanStateType],
        "filters": List["SavingsPlanFilterTypeDef"],
    },
    total=False,
)

DescribeSavingsPlansResponseTypeDef = TypedDict(
    "DescribeSavingsPlansResponseTypeDef",
    {
        "savingsPlans": List["SavingsPlanTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ParentSavingsPlanOfferingTypeDef = TypedDict(
    "ParentSavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": SavingsPlanPaymentOptionType,
        "planType": SavingsPlanTypeType,
        "durationSeconds": int,
        "currency": CurrencyCodeType,
        "planDescription": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SavingsPlanFilterTypeDef = TypedDict(
    "SavingsPlanFilterTypeDef",
    {
        "name": SavingsPlansFilterNameType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingFilterElementTypeDef",
    {
        "name": SavingsPlanOfferingFilterAttributeType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingPropertyTypeDef = TypedDict(
    "SavingsPlanOfferingPropertyTypeDef",
    {
        "name": SavingsPlanOfferingPropertyKeyType,
        "value": str,
    },
    total=False,
)

SavingsPlanOfferingRateFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingRateFilterElementTypeDef",
    {
        "name": SavingsPlanRateFilterAttributeType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingRatePropertyTypeDef = TypedDict(
    "SavingsPlanOfferingRatePropertyTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

SavingsPlanOfferingRateTypeDef = TypedDict(
    "SavingsPlanOfferingRateTypeDef",
    {
        "savingsPlanOffering": "ParentSavingsPlanOfferingTypeDef",
        "rate": str,
        "unit": SavingsPlanRateUnitType,
        "productType": SavingsPlanProductTypeType,
        "serviceCode": SavingsPlanRateServiceCodeType,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingRatePropertyTypeDef"],
    },
    total=False,
)

SavingsPlanOfferingTypeDef = TypedDict(
    "SavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "productTypes": List[SavingsPlanProductTypeType],
        "planType": SavingsPlanTypeType,
        "description": str,
        "paymentOption": SavingsPlanPaymentOptionType,
        "durationSeconds": int,
        "currency": CurrencyCodeType,
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingPropertyTypeDef"],
    },
    total=False,
)

SavingsPlanRateFilterTypeDef = TypedDict(
    "SavingsPlanRateFilterTypeDef",
    {
        "name": SavingsPlanRateFilterNameType,
        "values": List[str],
    },
    total=False,
)

SavingsPlanRatePropertyTypeDef = TypedDict(
    "SavingsPlanRatePropertyTypeDef",
    {
        "name": SavingsPlanRatePropertyKeyType,
        "value": str,
    },
    total=False,
)

SavingsPlanRateTypeDef = TypedDict(
    "SavingsPlanRateTypeDef",
    {
        "rate": str,
        "currency": CurrencyCodeType,
        "unit": SavingsPlanRateUnitType,
        "productType": SavingsPlanProductTypeType,
        "serviceCode": SavingsPlanRateServiceCodeType,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanRatePropertyTypeDef"],
    },
    total=False,
)

SavingsPlanTypeDef = TypedDict(
    "SavingsPlanTypeDef",
    {
        "offeringId": str,
        "savingsPlanId": str,
        "savingsPlanArn": str,
        "description": str,
        "start": str,
        "end": str,
        "state": SavingsPlanStateType,
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": SavingsPlanTypeType,
        "paymentOption": SavingsPlanPaymentOptionType,
        "productTypes": List[SavingsPlanProductTypeType],
        "currency": CurrencyCodeType,
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
