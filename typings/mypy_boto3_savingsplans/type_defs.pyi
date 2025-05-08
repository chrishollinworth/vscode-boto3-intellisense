"""
Type annotations for savingsplans service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateSavingsPlanRequestTypeDef",
    "CreateSavingsPlanResponseTypeDef",
    "DeleteQueuedSavingsPlanRequestTypeDef",
    "DescribeSavingsPlanRatesRequestTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesRequestTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingsRequestTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansRequestTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParentSavingsPlanOfferingTypeDef",
    "ResponseMetadataTypeDef",
    "ReturnSavingsPlanRequestTypeDef",
    "ReturnSavingsPlanResponseTypeDef",
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
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
)

TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteQueuedSavingsPlanRequestTypeDef(TypedDict):
    savingsPlanId: str

class SavingsPlanRateFilterTypeDef(TypedDict):
    name: NotRequired[SavingsPlanRateFilterNameType]
    values: NotRequired[Sequence[str]]

class SavingsPlanOfferingRateFilterElementTypeDef(TypedDict):
    name: NotRequired[SavingsPlanRateFilterAttributeType]
    values: NotRequired[Sequence[str]]

class SavingsPlanOfferingFilterElementTypeDef(TypedDict):
    name: NotRequired[SavingsPlanOfferingFilterAttributeType]
    values: NotRequired[Sequence[str]]

class SavingsPlanFilterTypeDef(TypedDict):
    name: NotRequired[SavingsPlansFilterNameType]
    values: NotRequired[Sequence[str]]

class SavingsPlanTypeDef(TypedDict):
    offeringId: NotRequired[str]
    savingsPlanId: NotRequired[str]
    savingsPlanArn: NotRequired[str]
    description: NotRequired[str]
    start: NotRequired[str]
    end: NotRequired[str]
    state: NotRequired[SavingsPlanStateType]
    region: NotRequired[str]
    ec2InstanceFamily: NotRequired[str]
    savingsPlanType: NotRequired[SavingsPlanTypeType]
    paymentOption: NotRequired[SavingsPlanPaymentOptionType]
    productTypes: NotRequired[List[SavingsPlanProductTypeType]]
    currency: NotRequired[CurrencyCodeType]
    commitment: NotRequired[str]
    upfrontPaymentAmount: NotRequired[str]
    recurringPaymentAmount: NotRequired[str]
    termDurationInSeconds: NotRequired[int]
    tags: NotRequired[Dict[str, str]]
    returnableUntil: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ParentSavingsPlanOfferingTypeDef(TypedDict):
    offeringId: NotRequired[str]
    paymentOption: NotRequired[SavingsPlanPaymentOptionType]
    planType: NotRequired[SavingsPlanTypeType]
    durationSeconds: NotRequired[int]
    currency: NotRequired[CurrencyCodeType]
    planDescription: NotRequired[str]

class ReturnSavingsPlanRequestTypeDef(TypedDict):
    savingsPlanId: str
    clientToken: NotRequired[str]

class SavingsPlanOfferingPropertyTypeDef(TypedDict):
    name: NotRequired[SavingsPlanOfferingPropertyKeyType]
    value: NotRequired[str]

class SavingsPlanOfferingRatePropertyTypeDef(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]

class SavingsPlanRatePropertyTypeDef(TypedDict):
    name: NotRequired[SavingsPlanRatePropertyKeyType]
    value: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class CreateSavingsPlanRequestTypeDef(TypedDict):
    savingsPlanOfferingId: str
    commitment: str
    upfrontPaymentAmount: NotRequired[str]
    purchaseTime: NotRequired[TimestampTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateSavingsPlanResponseTypeDef(TypedDict):
    savingsPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ReturnSavingsPlanResponseTypeDef(TypedDict):
    savingsPlanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSavingsPlanRatesRequestTypeDef(TypedDict):
    savingsPlanId: str
    filters: NotRequired[Sequence[SavingsPlanRateFilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeSavingsPlansOfferingRatesRequestTypeDef(TypedDict):
    savingsPlanOfferingIds: NotRequired[Sequence[str]]
    savingsPlanPaymentOptions: NotRequired[Sequence[SavingsPlanPaymentOptionType]]
    savingsPlanTypes: NotRequired[Sequence[SavingsPlanTypeType]]
    products: NotRequired[Sequence[SavingsPlanProductTypeType]]
    serviceCodes: NotRequired[Sequence[SavingsPlanRateServiceCodeType]]
    usageTypes: NotRequired[Sequence[str]]
    operations: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[SavingsPlanOfferingRateFilterElementTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeSavingsPlansOfferingsRequestTypeDef(TypedDict):
    offeringIds: NotRequired[Sequence[str]]
    paymentOptions: NotRequired[Sequence[SavingsPlanPaymentOptionType]]
    productType: NotRequired[SavingsPlanProductTypeType]
    planTypes: NotRequired[Sequence[SavingsPlanTypeType]]
    durations: NotRequired[Sequence[int]]
    currencies: NotRequired[Sequence[CurrencyCodeType]]
    descriptions: NotRequired[Sequence[str]]
    serviceCodes: NotRequired[Sequence[str]]
    usageTypes: NotRequired[Sequence[str]]
    operations: NotRequired[Sequence[str]]
    filters: NotRequired[Sequence[SavingsPlanOfferingFilterElementTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class DescribeSavingsPlansRequestTypeDef(TypedDict):
    savingsPlanArns: NotRequired[Sequence[str]]
    savingsPlanIds: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    states: NotRequired[Sequence[SavingsPlanStateType]]
    filters: NotRequired[Sequence[SavingsPlanFilterTypeDef]]

class DescribeSavingsPlansResponseTypeDef(TypedDict):
    savingsPlans: List[SavingsPlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SavingsPlanOfferingTypeDef(TypedDict):
    offeringId: NotRequired[str]
    productTypes: NotRequired[List[SavingsPlanProductTypeType]]
    planType: NotRequired[SavingsPlanTypeType]
    description: NotRequired[str]
    paymentOption: NotRequired[SavingsPlanPaymentOptionType]
    durationSeconds: NotRequired[int]
    currency: NotRequired[CurrencyCodeType]
    serviceCode: NotRequired[str]
    usageType: NotRequired[str]
    operation: NotRequired[str]
    properties: NotRequired[List[SavingsPlanOfferingPropertyTypeDef]]

class SavingsPlanOfferingRateTypeDef(TypedDict):
    savingsPlanOffering: NotRequired[ParentSavingsPlanOfferingTypeDef]
    rate: NotRequired[str]
    unit: NotRequired[SavingsPlanRateUnitType]
    productType: NotRequired[SavingsPlanProductTypeType]
    serviceCode: NotRequired[SavingsPlanRateServiceCodeType]
    usageType: NotRequired[str]
    operation: NotRequired[str]
    properties: NotRequired[List[SavingsPlanOfferingRatePropertyTypeDef]]

class SavingsPlanRateTypeDef(TypedDict):
    rate: NotRequired[str]
    currency: NotRequired[CurrencyCodeType]
    unit: NotRequired[SavingsPlanRateUnitType]
    productType: NotRequired[SavingsPlanProductTypeType]
    serviceCode: NotRequired[SavingsPlanRateServiceCodeType]
    usageType: NotRequired[str]
    operation: NotRequired[str]
    properties: NotRequired[List[SavingsPlanRatePropertyTypeDef]]

class DescribeSavingsPlansOfferingsResponseTypeDef(TypedDict):
    searchResults: List[SavingsPlanOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeSavingsPlansOfferingRatesResponseTypeDef(TypedDict):
    searchResults: List[SavingsPlanOfferingRateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeSavingsPlanRatesResponseTypeDef(TypedDict):
    savingsPlanId: str
    searchResults: List[SavingsPlanRateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
