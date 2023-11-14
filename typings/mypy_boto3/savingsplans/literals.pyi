"""
Type annotations for savingsplans service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/literals.html)

Usage::

    ```python
    from mypy_boto3_savingsplans.literals import CurrencyCodeType

    data: CurrencyCodeType = "CNY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CurrencyCodeType",
    "SavingsPlanOfferingFilterAttributeType",
    "SavingsPlanOfferingPropertyKeyType",
    "SavingsPlanPaymentOptionType",
    "SavingsPlanProductTypeType",
    "SavingsPlanRateFilterAttributeType",
    "SavingsPlanRateFilterNameType",
    "SavingsPlanRatePropertyKeyType",
    "SavingsPlanRateServiceCodeType",
    "SavingsPlanRateUnitType",
    "SavingsPlanStateType",
    "SavingsPlanTypeType",
    "SavingsPlansFilterNameType",
)

CurrencyCodeType = Literal["CNY", "USD"]
SavingsPlanOfferingFilterAttributeType = Literal["instanceFamily", "region"]
SavingsPlanOfferingPropertyKeyType = Literal["instanceFamily", "region"]
SavingsPlanPaymentOptionType = Literal["All Upfront", "No Upfront", "Partial Upfront"]
SavingsPlanProductTypeType = Literal["EC2", "Fargate", "Lambda", "SageMaker"]
SavingsPlanRateFilterAttributeType = Literal[
    "instanceFamily", "instanceType", "productDescription", "productId", "region", "tenancy"
]
SavingsPlanRateFilterNameType = Literal[
    "instanceType",
    "operation",
    "productDescription",
    "productType",
    "region",
    "serviceCode",
    "tenancy",
    "usageType",
]
SavingsPlanRatePropertyKeyType = Literal[
    "instanceFamily", "instanceType", "productDescription", "region", "tenancy"
]
SavingsPlanRateServiceCodeType = Literal[
    "AWSLambda", "AmazonEC2", "AmazonECS", "AmazonEKS", "AmazonSageMaker"
]
SavingsPlanRateUnitType = Literal["Hrs", "Lambda-GB-Second", "Request"]
SavingsPlanStateType = Literal[
    "active", "payment-failed", "payment-pending", "queued", "queued-deleted", "retired"
]
SavingsPlanTypeType = Literal["Compute", "EC2Instance", "SageMaker"]
SavingsPlansFilterNameType = Literal[
    "commitment",
    "ec2-instance-family",
    "end",
    "payment-option",
    "region",
    "savings-plan-type",
    "start",
    "term",
    "upfront",
]
