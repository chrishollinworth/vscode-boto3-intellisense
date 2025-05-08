"""
Type annotations for savingsplans service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_savingsplans.client import SavingsPlansClient

    session = Session()
    client: SavingsPlansClient = session.client("savingsplans")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateSavingsPlanRequestTypeDef,
    CreateSavingsPlanResponseTypeDef,
    DeleteQueuedSavingsPlanRequestTypeDef,
    DescribeSavingsPlanRatesRequestTypeDef,
    DescribeSavingsPlanRatesResponseTypeDef,
    DescribeSavingsPlansOfferingRatesRequestTypeDef,
    DescribeSavingsPlansOfferingRatesResponseTypeDef,
    DescribeSavingsPlansOfferingsRequestTypeDef,
    DescribeSavingsPlansOfferingsResponseTypeDef,
    DescribeSavingsPlansRequestTypeDef,
    DescribeSavingsPlansResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ReturnSavingsPlanRequestTypeDef,
    ReturnSavingsPlanResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("SavingsPlansClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SavingsPlansClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SavingsPlansClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans.html#SavingsPlans.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#generate_presigned_url)
        """

    def create_savings_plan(
        self, **kwargs: Unpack[CreateSavingsPlanRequestTypeDef]
    ) -> CreateSavingsPlanResponseTypeDef:
        """
        Creates a Savings Plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/create_savings_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#create_savings_plan)
        """

    def delete_queued_savings_plan(
        self, **kwargs: Unpack[DeleteQueuedSavingsPlanRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the queued purchase for the specified Savings Plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/delete_queued_savings_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#delete_queued_savings_plan)
        """

    def describe_savings_plan_rates(
        self, **kwargs: Unpack[DescribeSavingsPlanRatesRequestTypeDef]
    ) -> DescribeSavingsPlanRatesResponseTypeDef:
        """
        Describes the rates for the specified Savings Plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/describe_savings_plan_rates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#describe_savings_plan_rates)
        """

    def describe_savings_plans(
        self, **kwargs: Unpack[DescribeSavingsPlansRequestTypeDef]
    ) -> DescribeSavingsPlansResponseTypeDef:
        """
        Describes the specified Savings Plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/describe_savings_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#describe_savings_plans)
        """

    def describe_savings_plans_offering_rates(
        self, **kwargs: Unpack[DescribeSavingsPlansOfferingRatesRequestTypeDef]
    ) -> DescribeSavingsPlansOfferingRatesResponseTypeDef:
        """
        Describes the offering rates for the specified Savings Plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/describe_savings_plans_offering_rates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#describe_savings_plans_offering_rates)
        """

    def describe_savings_plans_offerings(
        self, **kwargs: Unpack[DescribeSavingsPlansOfferingsRequestTypeDef]
    ) -> DescribeSavingsPlansOfferingsResponseTypeDef:
        """
        Describes the offerings for the specified Savings Plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/describe_savings_plans_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#describe_savings_plans_offerings)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#list_tags_for_resource)
        """

    def return_savings_plan(
        self, **kwargs: Unpack[ReturnSavingsPlanRequestTypeDef]
    ) -> ReturnSavingsPlanResponseTypeDef:
        """
        Returns the specified Savings Plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/return_savings_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#return_savings_plan)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/savingsplans/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client/#untag_resource)
        """
