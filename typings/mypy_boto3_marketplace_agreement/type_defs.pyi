"""
Type annotations for marketplace-agreement service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_marketplace_agreement.type_defs import ByolPricingTermTypeDef

    data: ByolPricingTermTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import AgreementStatusType, SortOrderType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptedTermTypeDef",
    "AcceptorTypeDef",
    "AgreementViewSummaryTypeDef",
    "ByolPricingTermTypeDef",
    "ConfigurableUpfrontPricingTermConfigurationTypeDef",
    "ConfigurableUpfrontPricingTermTypeDef",
    "ConfigurableUpfrontRateCardItemTypeDef",
    "ConstraintsTypeDef",
    "DescribeAgreementInputTypeDef",
    "DescribeAgreementOutputTypeDef",
    "DimensionTypeDef",
    "DocumentItemTypeDef",
    "EstimatedChargesTypeDef",
    "FilterTypeDef",
    "FixedUpfrontPricingTermTypeDef",
    "FreeTrialPricingTermTypeDef",
    "GetAgreementTermsInputTypeDef",
    "GetAgreementTermsOutputTypeDef",
    "GrantItemTypeDef",
    "LegalTermTypeDef",
    "PaymentScheduleTermTypeDef",
    "ProposalSummaryTypeDef",
    "ProposerTypeDef",
    "RateCardItemTypeDef",
    "RecurringPaymentTermTypeDef",
    "RenewalTermConfigurationTypeDef",
    "RenewalTermTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ScheduleItemTypeDef",
    "SearchAgreementsInputTypeDef",
    "SearchAgreementsOutputTypeDef",
    "SelectorTypeDef",
    "SortTypeDef",
    "SupportTermTypeDef",
    "UsageBasedPricingTermTypeDef",
    "UsageBasedRateCardItemTypeDef",
    "ValidityTermTypeDef",
)

ByolPricingTermTypeDef = TypedDict(
    "ByolPricingTermTypeDef",
    {
        "type": NotRequired[str],
    },
)
RecurringPaymentTermTypeDef = TypedDict(
    "RecurringPaymentTermTypeDef",
    {
        "billingPeriod": NotRequired[str],
        "currencyCode": NotRequired[str],
        "price": NotRequired[str],
        "type": NotRequired[str],
    },
)
SupportTermTypeDef = TypedDict(
    "SupportTermTypeDef",
    {
        "refundPolicy": NotRequired[str],
        "type": NotRequired[str],
    },
)
ValidityTermTypeDef = TypedDict(
    "ValidityTermTypeDef",
    {
        "agreementDuration": NotRequired[str],
        "agreementEndDate": NotRequired[datetime],
        "agreementStartDate": NotRequired[datetime],
        "type": NotRequired[str],
    },
)

class AcceptorTypeDef(TypedDict):
    accountId: NotRequired[str]

class ProposerTypeDef(TypedDict):
    accountId: NotRequired[str]

class DimensionTypeDef(TypedDict):
    dimensionKey: str
    dimensionValue: int

class ConstraintsTypeDef(TypedDict):
    multipleDimensionSelection: NotRequired[str]
    quantityConfiguration: NotRequired[str]

class RateCardItemTypeDef(TypedDict):
    dimensionKey: NotRequired[str]
    price: NotRequired[str]

SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "type": NotRequired[str],
        "value": NotRequired[str],
    },
)

class DescribeAgreementInputTypeDef(TypedDict):
    agreementId: str

class EstimatedChargesTypeDef(TypedDict):
    agreementValue: NotRequired[str]
    currencyCode: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DocumentItemTypeDef = TypedDict(
    "DocumentItemTypeDef",
    {
        "type": NotRequired[str],
        "url": NotRequired[str],
        "version": NotRequired[str],
    },
)

class FilterTypeDef(TypedDict):
    name: NotRequired[str]
    values: NotRequired[Sequence[str]]

class GrantItemTypeDef(TypedDict):
    dimensionKey: NotRequired[str]
    maxQuantity: NotRequired[int]

class GetAgreementTermsInputTypeDef(TypedDict):
    agreementId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ScheduleItemTypeDef(TypedDict):
    chargeAmount: NotRequired[str]
    chargeDate: NotRequired[datetime]

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[str],
    },
)

class RenewalTermConfigurationTypeDef(TypedDict):
    enableAutoRenew: bool

class SortTypeDef(TypedDict):
    sortBy: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]

class ConfigurableUpfrontPricingTermConfigurationTypeDef(TypedDict):
    dimensions: List[DimensionTypeDef]
    selectorValue: str

class UsageBasedRateCardItemTypeDef(TypedDict):
    rateCard: NotRequired[List[RateCardItemTypeDef]]

class ConfigurableUpfrontRateCardItemTypeDef(TypedDict):
    constraints: NotRequired[ConstraintsTypeDef]
    rateCard: NotRequired[List[RateCardItemTypeDef]]
    selector: NotRequired[SelectorTypeDef]

LegalTermTypeDef = TypedDict(
    "LegalTermTypeDef",
    {
        "documents": NotRequired[List[DocumentItemTypeDef]],
        "type": NotRequired[str],
    },
)
FixedUpfrontPricingTermTypeDef = TypedDict(
    "FixedUpfrontPricingTermTypeDef",
    {
        "currencyCode": NotRequired[str],
        "duration": NotRequired[str],
        "grants": NotRequired[List[GrantItemTypeDef]],
        "price": NotRequired[str],
        "type": NotRequired[str],
    },
)
FreeTrialPricingTermTypeDef = TypedDict(
    "FreeTrialPricingTermTypeDef",
    {
        "duration": NotRequired[str],
        "grants": NotRequired[List[GrantItemTypeDef]],
        "type": NotRequired[str],
    },
)
PaymentScheduleTermTypeDef = TypedDict(
    "PaymentScheduleTermTypeDef",
    {
        "currencyCode": NotRequired[str],
        "schedule": NotRequired[List[ScheduleItemTypeDef]],
        "type": NotRequired[str],
    },
)

class ProposalSummaryTypeDef(TypedDict):
    offerId: NotRequired[str]
    resources: NotRequired[List[ResourceTypeDef]]

RenewalTermTypeDef = TypedDict(
    "RenewalTermTypeDef",
    {
        "configuration": NotRequired[RenewalTermConfigurationTypeDef],
        "type": NotRequired[str],
    },
)

class SearchAgreementsInputTypeDef(TypedDict):
    catalog: NotRequired[str]
    filters: NotRequired[Sequence[FilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sort: NotRequired[SortTypeDef]

UsageBasedPricingTermTypeDef = TypedDict(
    "UsageBasedPricingTermTypeDef",
    {
        "currencyCode": NotRequired[str],
        "rateCards": NotRequired[List[UsageBasedRateCardItemTypeDef]],
        "type": NotRequired[str],
    },
)
ConfigurableUpfrontPricingTermTypeDef = TypedDict(
    "ConfigurableUpfrontPricingTermTypeDef",
    {
        "configuration": NotRequired[ConfigurableUpfrontPricingTermConfigurationTypeDef],
        "currencyCode": NotRequired[str],
        "rateCards": NotRequired[List[ConfigurableUpfrontRateCardItemTypeDef]],
        "type": NotRequired[str],
    },
)

class AgreementViewSummaryTypeDef(TypedDict):
    acceptanceTime: NotRequired[datetime]
    acceptor: NotRequired[AcceptorTypeDef]
    agreementId: NotRequired[str]
    agreementType: NotRequired[str]
    endTime: NotRequired[datetime]
    proposalSummary: NotRequired[ProposalSummaryTypeDef]
    proposer: NotRequired[ProposerTypeDef]
    startTime: NotRequired[datetime]
    status: NotRequired[AgreementStatusType]

class DescribeAgreementOutputTypeDef(TypedDict):
    acceptanceTime: datetime
    acceptor: AcceptorTypeDef
    agreementId: str
    agreementType: str
    endTime: datetime
    estimatedCharges: EstimatedChargesTypeDef
    proposalSummary: ProposalSummaryTypeDef
    proposer: ProposerTypeDef
    startTime: datetime
    status: AgreementStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptedTermTypeDef(TypedDict):
    byolPricingTerm: NotRequired[ByolPricingTermTypeDef]
    configurableUpfrontPricingTerm: NotRequired[ConfigurableUpfrontPricingTermTypeDef]
    fixedUpfrontPricingTerm: NotRequired[FixedUpfrontPricingTermTypeDef]
    freeTrialPricingTerm: NotRequired[FreeTrialPricingTermTypeDef]
    legalTerm: NotRequired[LegalTermTypeDef]
    paymentScheduleTerm: NotRequired[PaymentScheduleTermTypeDef]
    recurringPaymentTerm: NotRequired[RecurringPaymentTermTypeDef]
    renewalTerm: NotRequired[RenewalTermTypeDef]
    supportTerm: NotRequired[SupportTermTypeDef]
    usageBasedPricingTerm: NotRequired[UsageBasedPricingTermTypeDef]
    validityTerm: NotRequired[ValidityTermTypeDef]

class SearchAgreementsOutputTypeDef(TypedDict):
    agreementViewSummaries: List[AgreementViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetAgreementTermsOutputTypeDef(TypedDict):
    acceptedTerms: List[AcceptedTermTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
