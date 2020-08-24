"""
Main interface for savingsplans service type definitions.

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import ParentSavingsPlanOfferingTypeDef

    data: ParentSavingsPlanOfferingTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ParentSavingsPlanOfferingTypeDef",
    "SavingsPlanOfferingPropertyTypeDef",
    "SavingsPlanOfferingRatePropertyTypeDef",
    "SavingsPlanOfferingRateTypeDef",
    "SavingsPlanOfferingTypeDef",
    "SavingsPlanRatePropertyTypeDef",
    "SavingsPlanRateTypeDef",
    "SavingsPlanTypeDef",
    "CreateSavingsPlanResponseTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SavingsPlanFilterTypeDef",
    "SavingsPlanOfferingFilterElementTypeDef",
    "SavingsPlanOfferingRateFilterElementTypeDef",
    "SavingsPlanRateFilterTypeDef",
)

ParentSavingsPlanOfferingTypeDef = TypedDict(
    "ParentSavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "planType": Literal["Compute", "EC2Instance"],
        "durationSeconds": int,
        "currency": Literal["CNY", "USD"],
        "planDescription": str,
    },
    total=False,
)

SavingsPlanOfferingPropertyTypeDef = TypedDict(
    "SavingsPlanOfferingPropertyTypeDef",
    {"name": Literal["region", "instanceFamily"], "value": str},
    total=False,
)

SavingsPlanOfferingRatePropertyTypeDef = TypedDict(
    "SavingsPlanOfferingRatePropertyTypeDef", {"name": str, "value": str}, total=False
)

SavingsPlanOfferingRateTypeDef = TypedDict(
    "SavingsPlanOfferingRateTypeDef",
    {
        "savingsPlanOffering": "ParentSavingsPlanOfferingTypeDef",
        "rate": str,
        "unit": Literal["Hrs", "Lambda-GB-Second", "Request"],
        "productType": Literal["EC2", "Fargate", "Lambda"],
        "serviceCode": Literal["AmazonEC2", "AmazonECS", "AmazonEKS", "AWSLambda"],
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
        "productTypes": List[Literal["EC2", "Fargate", "Lambda"]],
        "planType": Literal["Compute", "EC2Instance"],
        "description": str,
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "durationSeconds": int,
        "currency": Literal["CNY", "USD"],
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingPropertyTypeDef"],
    },
    total=False,
)

SavingsPlanRatePropertyTypeDef = TypedDict(
    "SavingsPlanRatePropertyTypeDef",
    {
        "name": Literal[
            "region", "instanceType", "instanceFamily", "productDescription", "tenancy"
        ],
        "value": str,
    },
    total=False,
)

SavingsPlanRateTypeDef = TypedDict(
    "SavingsPlanRateTypeDef",
    {
        "rate": str,
        "currency": Literal["CNY", "USD"],
        "unit": Literal["Hrs", "Lambda-GB-Second", "Request"],
        "productType": Literal["EC2", "Fargate", "Lambda"],
        "serviceCode": Literal["AmazonEC2", "AmazonECS", "AmazonEKS", "AWSLambda"],
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
        "state": Literal["payment-pending", "payment-failed", "active", "retired"],
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": Literal["Compute", "EC2Instance"],
        "paymentOption": Literal["All Upfront", "Partial Upfront", "No Upfront"],
        "productTypes": List[Literal["EC2", "Fargate", "Lambda"]],
        "currency": Literal["CNY", "USD"],
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSavingsPlanResponseTypeDef = TypedDict(
    "CreateSavingsPlanResponseTypeDef", {"savingsPlanId": str}, total=False
)

DescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlanRatesResponseTypeDef",
    {"savingsPlanId": str, "searchResults": List["SavingsPlanRateTypeDef"], "nextToken": str},
    total=False,
)

DescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    {"searchResults": List["SavingsPlanOfferingRateTypeDef"], "nextToken": str},
    total=False,
)

DescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    {"searchResults": List["SavingsPlanOfferingTypeDef"], "nextToken": str},
    total=False,
)

DescribeSavingsPlansResponseTypeDef = TypedDict(
    "DescribeSavingsPlansResponseTypeDef",
    {"savingsPlans": List["SavingsPlanTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

SavingsPlanFilterTypeDef = TypedDict(
    "SavingsPlanFilterTypeDef",
    {
        "name": Literal[
            "region",
            "ec2-instance-family",
            "commitment",
            "upfront",
            "term",
            "savings-plan-type",
            "payment-option",
            "start",
            "end",
        ],
        "values": List[str],
    },
    total=False,
)

SavingsPlanOfferingFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingFilterElementTypeDef",
    {"name": Literal["region", "instanceFamily"], "values": List[str]},
    total=False,
)

SavingsPlanOfferingRateFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingRateFilterElementTypeDef",
    {
        "name": Literal[
            "region", "instanceFamily", "instanceType", "productDescription", "tenancy", "productId"
        ],
        "values": List[str],
    },
    total=False,
)

SavingsPlanRateFilterTypeDef = TypedDict(
    "SavingsPlanRateFilterTypeDef",
    {
        "name": Literal[
            "region",
            "instanceType",
            "productDescription",
            "tenancy",
            "productType",
            "serviceCode",
            "usageType",
            "operation",
        ],
        "values": List[str],
    },
    total=False,
)
