"""
Type annotations for marketplace-agreement service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_agreement.type_defs import AcceptedTermTypeDef

    data: AcceptedTermTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import AgreementStatusType, SortOrderType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptedTermTypeDef",
    "AcceptorTypeDef",
    "AgreementViewSummaryTypeDef",
    "ByolPricingTermTypeDef",
    "ConfigurableUpfrontPricingTermConfigurationTypeDef",
    "ConfigurableUpfrontPricingTermTypeDef",
    "ConfigurableUpfrontRateCardItemTypeDef",
    "ConstraintsTypeDef",
    "DescribeAgreementInputRequestTypeDef",
    "DescribeAgreementOutputTypeDef",
    "DimensionTypeDef",
    "DocumentItemTypeDef",
    "EstimatedChargesTypeDef",
    "FilterTypeDef",
    "FixedUpfrontPricingTermTypeDef",
    "FreeTrialPricingTermTypeDef",
    "GetAgreementTermsInputRequestTypeDef",
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
    "SearchAgreementsInputRequestTypeDef",
    "SearchAgreementsOutputTypeDef",
    "SelectorTypeDef",
    "SortTypeDef",
    "SupportTermTypeDef",
    "UsageBasedPricingTermTypeDef",
    "UsageBasedRateCardItemTypeDef",
    "ValidityTermTypeDef",
)

AcceptedTermTypeDef = TypedDict(
    "AcceptedTermTypeDef",
    {
        "byolPricingTerm": "ByolPricingTermTypeDef",
        "configurableUpfrontPricingTerm": "ConfigurableUpfrontPricingTermTypeDef",
        "fixedUpfrontPricingTerm": "FixedUpfrontPricingTermTypeDef",
        "freeTrialPricingTerm": "FreeTrialPricingTermTypeDef",
        "legalTerm": "LegalTermTypeDef",
        "paymentScheduleTerm": "PaymentScheduleTermTypeDef",
        "recurringPaymentTerm": "RecurringPaymentTermTypeDef",
        "renewalTerm": "RenewalTermTypeDef",
        "supportTerm": "SupportTermTypeDef",
        "usageBasedPricingTerm": "UsageBasedPricingTermTypeDef",
        "validityTerm": "ValidityTermTypeDef",
    },
    total=False,
)

AcceptorTypeDef = TypedDict(
    "AcceptorTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

AgreementViewSummaryTypeDef = TypedDict(
    "AgreementViewSummaryTypeDef",
    {
        "acceptanceTime": datetime,
        "acceptor": "AcceptorTypeDef",
        "agreementId": str,
        "agreementType": str,
        "endTime": datetime,
        "proposalSummary": "ProposalSummaryTypeDef",
        "proposer": "ProposerTypeDef",
        "startTime": datetime,
        "status": AgreementStatusType,
    },
    total=False,
)

ByolPricingTermTypeDef = TypedDict(
    "ByolPricingTermTypeDef",
    {
        "type": str,
    },
    total=False,
)

ConfigurableUpfrontPricingTermConfigurationTypeDef = TypedDict(
    "ConfigurableUpfrontPricingTermConfigurationTypeDef",
    {
        "dimensions": List["DimensionTypeDef"],
        "selectorValue": str,
    },
)

ConfigurableUpfrontPricingTermTypeDef = TypedDict(
    "ConfigurableUpfrontPricingTermTypeDef",
    {
        "configuration": "ConfigurableUpfrontPricingTermConfigurationTypeDef",
        "currencyCode": str,
        "rateCards": List["ConfigurableUpfrontRateCardItemTypeDef"],
        "type": str,
    },
    total=False,
)

ConfigurableUpfrontRateCardItemTypeDef = TypedDict(
    "ConfigurableUpfrontRateCardItemTypeDef",
    {
        "constraints": "ConstraintsTypeDef",
        "rateCard": List["RateCardItemTypeDef"],
        "selector": "SelectorTypeDef",
    },
    total=False,
)

ConstraintsTypeDef = TypedDict(
    "ConstraintsTypeDef",
    {
        "multipleDimensionSelection": str,
        "quantityConfiguration": str,
    },
    total=False,
)

DescribeAgreementInputRequestTypeDef = TypedDict(
    "DescribeAgreementInputRequestTypeDef",
    {
        "agreementId": str,
    },
)

DescribeAgreementOutputTypeDef = TypedDict(
    "DescribeAgreementOutputTypeDef",
    {
        "acceptanceTime": datetime,
        "acceptor": "AcceptorTypeDef",
        "agreementId": str,
        "agreementType": str,
        "endTime": datetime,
        "estimatedCharges": "EstimatedChargesTypeDef",
        "proposalSummary": "ProposalSummaryTypeDef",
        "proposer": "ProposerTypeDef",
        "startTime": datetime,
        "status": AgreementStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "dimensionKey": str,
        "dimensionValue": int,
    },
)

DocumentItemTypeDef = TypedDict(
    "DocumentItemTypeDef",
    {
        "type": str,
        "url": str,
        "version": str,
    },
    total=False,
)

EstimatedChargesTypeDef = TypedDict(
    "EstimatedChargesTypeDef",
    {
        "agreementValue": str,
        "currencyCode": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

FixedUpfrontPricingTermTypeDef = TypedDict(
    "FixedUpfrontPricingTermTypeDef",
    {
        "currencyCode": str,
        "duration": str,
        "grants": List["GrantItemTypeDef"],
        "price": str,
        "type": str,
    },
    total=False,
)

FreeTrialPricingTermTypeDef = TypedDict(
    "FreeTrialPricingTermTypeDef",
    {
        "duration": str,
        "grants": List["GrantItemTypeDef"],
        "type": str,
    },
    total=False,
)

_RequiredGetAgreementTermsInputRequestTypeDef = TypedDict(
    "_RequiredGetAgreementTermsInputRequestTypeDef",
    {
        "agreementId": str,
    },
)
_OptionalGetAgreementTermsInputRequestTypeDef = TypedDict(
    "_OptionalGetAgreementTermsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class GetAgreementTermsInputRequestTypeDef(
    _RequiredGetAgreementTermsInputRequestTypeDef, _OptionalGetAgreementTermsInputRequestTypeDef
):
    pass

GetAgreementTermsOutputTypeDef = TypedDict(
    "GetAgreementTermsOutputTypeDef",
    {
        "acceptedTerms": List["AcceptedTermTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantItemTypeDef = TypedDict(
    "GrantItemTypeDef",
    {
        "dimensionKey": str,
        "maxQuantity": int,
    },
    total=False,
)

LegalTermTypeDef = TypedDict(
    "LegalTermTypeDef",
    {
        "documents": List["DocumentItemTypeDef"],
        "type": str,
    },
    total=False,
)

PaymentScheduleTermTypeDef = TypedDict(
    "PaymentScheduleTermTypeDef",
    {
        "currencyCode": str,
        "schedule": List["ScheduleItemTypeDef"],
        "type": str,
    },
    total=False,
)

ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "offerId": str,
        "resources": List["ResourceTypeDef"],
    },
    total=False,
)

ProposerTypeDef = TypedDict(
    "ProposerTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

RateCardItemTypeDef = TypedDict(
    "RateCardItemTypeDef",
    {
        "dimensionKey": str,
        "price": str,
    },
    total=False,
)

RecurringPaymentTermTypeDef = TypedDict(
    "RecurringPaymentTermTypeDef",
    {
        "billingPeriod": str,
        "currencyCode": str,
        "price": str,
        "type": str,
    },
    total=False,
)

RenewalTermConfigurationTypeDef = TypedDict(
    "RenewalTermConfigurationTypeDef",
    {
        "enableAutoRenew": bool,
    },
)

RenewalTermTypeDef = TypedDict(
    "RenewalTermTypeDef",
    {
        "configuration": "RenewalTermConfigurationTypeDef",
        "type": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "type": str,
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

ScheduleItemTypeDef = TypedDict(
    "ScheduleItemTypeDef",
    {
        "chargeAmount": str,
        "chargeDate": datetime,
    },
    total=False,
)

SearchAgreementsInputRequestTypeDef = TypedDict(
    "SearchAgreementsInputRequestTypeDef",
    {
        "catalog": str,
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sort": "SortTypeDef",
    },
    total=False,
)

SearchAgreementsOutputTypeDef = TypedDict(
    "SearchAgreementsOutputTypeDef",
    {
        "agreementViewSummaries": List["AgreementViewSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SelectorTypeDef = TypedDict(
    "SelectorTypeDef",
    {
        "type": str,
        "value": str,
    },
    total=False,
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "sortBy": str,
        "sortOrder": SortOrderType,
    },
    total=False,
)

SupportTermTypeDef = TypedDict(
    "SupportTermTypeDef",
    {
        "refundPolicy": str,
        "type": str,
    },
    total=False,
)

UsageBasedPricingTermTypeDef = TypedDict(
    "UsageBasedPricingTermTypeDef",
    {
        "currencyCode": str,
        "rateCards": List["UsageBasedRateCardItemTypeDef"],
        "type": str,
    },
    total=False,
)

UsageBasedRateCardItemTypeDef = TypedDict(
    "UsageBasedRateCardItemTypeDef",
    {
        "rateCard": List["RateCardItemTypeDef"],
    },
    total=False,
)

ValidityTermTypeDef = TypedDict(
    "ValidityTermTypeDef",
    {
        "agreementDuration": str,
        "agreementEndDate": datetime,
        "agreementStartDate": datetime,
        "type": str,
    },
    total=False,
)
