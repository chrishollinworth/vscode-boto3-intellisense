# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for savingsplans service client

Usage::

    ```python
    import boto3
    from mypy_boto3_savingsplans import SavingsPlansClient

    client: SavingsPlansClient = boto3.client("savingsplans")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_savingsplans.type_defs import (
    CreateSavingsPlanResponseTypeDef,
    DescribeSavingsPlanRatesResponseTypeDef,
    DescribeSavingsPlansOfferingRatesResponseTypeDef,
    DescribeSavingsPlansOfferingsResponseTypeDef,
    DescribeSavingsPlansResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SavingsPlanFilterTypeDef,
    SavingsPlanOfferingFilterElementTypeDef,
    SavingsPlanOfferingRateFilterElementTypeDef,
    SavingsPlanRateFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SavingsPlansClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SavingsPlansClient:
    """
    [SavingsPlans.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.can_paginate)
        """

    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: str = None,
        purchaseTime: datetime = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateSavingsPlanResponseTypeDef:
        """
        [Client.create_savings_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.create_savings_plan)
        """

    def delete_queued_savings_plan(self, savingsPlanId: str) -> Dict[str, Any]:
        """
        [Client.delete_queued_savings_plan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.delete_queued_savings_plan)
        """

    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: List[SavingsPlanRateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlanRatesResponseTypeDef:
        """
        [Client.describe_savings_plan_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plan_rates)
        """

    def describe_savings_plans(
        self,
        savingsPlanArns: List[str] = None,
        savingsPlanIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        states: List[
            Literal[
                "payment-pending", "payment-failed", "active", "retired", "queued", "queued-deleted"
            ]
        ] = None,
        filters: List[SavingsPlanFilterTypeDef] = None,
    ) -> DescribeSavingsPlansResponseTypeDef:
        """
        [Client.describe_savings_plans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans)
        """

    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: List[str] = None,
        savingsPlanPaymentOptions: List[
            Literal["All Upfront", "Partial Upfront", "No Upfront"]
        ] = None,
        savingsPlanTypes: List[Literal["Compute", "EC2Instance"]] = None,
        products: List[Literal["EC2", "Fargate", "Lambda"]] = None,
        serviceCodes: List[Literal["AmazonEC2", "AmazonECS", "AWSLambda"]] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[SavingsPlanOfferingRateFilterElementTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlansOfferingRatesResponseTypeDef:
        """
        [Client.describe_savings_plans_offering_rates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offering_rates)
        """

    def describe_savings_plans_offerings(
        self,
        offeringIds: List[str] = None,
        paymentOptions: List[Literal["All Upfront", "Partial Upfront", "No Upfront"]] = None,
        productType: Literal["EC2", "Fargate", "Lambda"] = None,
        planTypes: List[Literal["Compute", "EC2Instance"]] = None,
        durations: List[int] = None,
        currencies: List[Literal["CNY", "USD"]] = None,
        descriptions: List[str] = None,
        serviceCodes: List[str] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[SavingsPlanOfferingFilterElementTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlansOfferingsResponseTypeDef:
        """
        [Client.describe_savings_plans_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offerings)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/savingsplans.html#SavingsPlans.Client.untag_resource)
        """
