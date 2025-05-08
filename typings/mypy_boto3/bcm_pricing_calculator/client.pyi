"""
Type annotations for bcm-pricing-calculator service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bcm_pricing_calculator.client import BillingandCostManagementPricingCalculatorClient

    session = Session()
    client: BillingandCostManagementPricingCalculatorClient = session.client("bcm-pricing-calculator")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBillEstimateCommitmentsPaginator,
    ListBillEstimateInputCommitmentModificationsPaginator,
    ListBillEstimateInputUsageModificationsPaginator,
    ListBillEstimateLineItemsPaginator,
    ListBillEstimatesPaginator,
    ListBillScenarioCommitmentModificationsPaginator,
    ListBillScenariosPaginator,
    ListBillScenarioUsageModificationsPaginator,
    ListWorkloadEstimatesPaginator,
    ListWorkloadEstimateUsagePaginator,
)
from .type_defs import (
    BatchCreateBillScenarioCommitmentModificationRequestTypeDef,
    BatchCreateBillScenarioCommitmentModificationResponseTypeDef,
    BatchCreateBillScenarioUsageModificationRequestTypeDef,
    BatchCreateBillScenarioUsageModificationResponseTypeDef,
    BatchCreateWorkloadEstimateUsageRequestTypeDef,
    BatchCreateWorkloadEstimateUsageResponseTypeDef,
    BatchDeleteBillScenarioCommitmentModificationRequestTypeDef,
    BatchDeleteBillScenarioCommitmentModificationResponseTypeDef,
    BatchDeleteBillScenarioUsageModificationRequestTypeDef,
    BatchDeleteBillScenarioUsageModificationResponseTypeDef,
    BatchDeleteWorkloadEstimateUsageRequestTypeDef,
    BatchDeleteWorkloadEstimateUsageResponseTypeDef,
    BatchUpdateBillScenarioCommitmentModificationRequestTypeDef,
    BatchUpdateBillScenarioCommitmentModificationResponseTypeDef,
    BatchUpdateBillScenarioUsageModificationRequestTypeDef,
    BatchUpdateBillScenarioUsageModificationResponseTypeDef,
    BatchUpdateWorkloadEstimateUsageRequestTypeDef,
    BatchUpdateWorkloadEstimateUsageResponseTypeDef,
    CreateBillEstimateRequestTypeDef,
    CreateBillEstimateResponseTypeDef,
    CreateBillScenarioRequestTypeDef,
    CreateBillScenarioResponseTypeDef,
    CreateWorkloadEstimateRequestTypeDef,
    CreateWorkloadEstimateResponseTypeDef,
    DeleteBillEstimateRequestTypeDef,
    DeleteBillScenarioRequestTypeDef,
    DeleteWorkloadEstimateRequestTypeDef,
    GetBillEstimateRequestTypeDef,
    GetBillEstimateResponseTypeDef,
    GetBillScenarioRequestTypeDef,
    GetBillScenarioResponseTypeDef,
    GetPreferencesResponseTypeDef,
    GetWorkloadEstimateRequestTypeDef,
    GetWorkloadEstimateResponseTypeDef,
    ListBillEstimateCommitmentsRequestTypeDef,
    ListBillEstimateCommitmentsResponseTypeDef,
    ListBillEstimateInputCommitmentModificationsRequestTypeDef,
    ListBillEstimateInputCommitmentModificationsResponseTypeDef,
    ListBillEstimateInputUsageModificationsRequestTypeDef,
    ListBillEstimateInputUsageModificationsResponseTypeDef,
    ListBillEstimateLineItemsRequestTypeDef,
    ListBillEstimateLineItemsResponseTypeDef,
    ListBillEstimatesRequestTypeDef,
    ListBillEstimatesResponseTypeDef,
    ListBillScenarioCommitmentModificationsRequestTypeDef,
    ListBillScenarioCommitmentModificationsResponseTypeDef,
    ListBillScenariosRequestTypeDef,
    ListBillScenariosResponseTypeDef,
    ListBillScenarioUsageModificationsRequestTypeDef,
    ListBillScenarioUsageModificationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkloadEstimatesRequestTypeDef,
    ListWorkloadEstimatesResponseTypeDef,
    ListWorkloadEstimateUsageRequestTypeDef,
    ListWorkloadEstimateUsageResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBillEstimateRequestTypeDef,
    UpdateBillEstimateResponseTypeDef,
    UpdateBillScenarioRequestTypeDef,
    UpdateBillScenarioResponseTypeDef,
    UpdatePreferencesRequestTypeDef,
    UpdatePreferencesResponseTypeDef,
    UpdateWorkloadEstimateRequestTypeDef,
    UpdateWorkloadEstimateResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BillingandCostManagementPricingCalculatorClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DataUnavailableException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BillingandCostManagementPricingCalculatorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator.html#BillingandCostManagementPricingCalculator.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BillingandCostManagementPricingCalculatorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator.html#BillingandCostManagementPricingCalculator.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#generate_presigned_url)
        """

    def batch_create_bill_scenario_commitment_modification(
        self, **kwargs: Unpack[BatchCreateBillScenarioCommitmentModificationRequestTypeDef]
    ) -> BatchCreateBillScenarioCommitmentModificationResponseTypeDef:
        """
        Create Compute Savings Plans, EC2 Instance Savings Plans, or EC2 Reserved
        Instances commitments that you want to model in a Bill Scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_create_bill_scenario_commitment_modification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_create_bill_scenario_commitment_modification)
        """

    def batch_create_bill_scenario_usage_modification(
        self, **kwargs: Unpack[BatchCreateBillScenarioUsageModificationRequestTypeDef]
    ) -> BatchCreateBillScenarioUsageModificationResponseTypeDef:
        """
        Create Amazon Web Services service usage that you want to model in a Bill
        Scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_create_bill_scenario_usage_modification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_create_bill_scenario_usage_modification)
        """

    def batch_create_workload_estimate_usage(
        self, **kwargs: Unpack[BatchCreateWorkloadEstimateUsageRequestTypeDef]
    ) -> BatchCreateWorkloadEstimateUsageResponseTypeDef:
        """
        Create Amazon Web Services service usage that you want to model in a Workload
        Estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_create_workload_estimate_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_create_workload_estimate_usage)
        """

    def batch_delete_bill_scenario_commitment_modification(
        self, **kwargs: Unpack[BatchDeleteBillScenarioCommitmentModificationRequestTypeDef]
    ) -> BatchDeleteBillScenarioCommitmentModificationResponseTypeDef:
        """
        Delete commitment that you have created in a Bill Scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_delete_bill_scenario_commitment_modification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_delete_bill_scenario_commitment_modification)
        """

    def batch_delete_bill_scenario_usage_modification(
        self, **kwargs: Unpack[BatchDeleteBillScenarioUsageModificationRequestTypeDef]
    ) -> BatchDeleteBillScenarioUsageModificationResponseTypeDef:
        """
        Delete usage that you have created in a Bill Scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_delete_bill_scenario_usage_modification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_delete_bill_scenario_usage_modification)
        """

    def batch_delete_workload_estimate_usage(
        self, **kwargs: Unpack[BatchDeleteWorkloadEstimateUsageRequestTypeDef]
    ) -> BatchDeleteWorkloadEstimateUsageResponseTypeDef:
        """
        Delete usage that you have created in a Workload estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_delete_workload_estimate_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_delete_workload_estimate_usage)
        """

    def batch_update_bill_scenario_commitment_modification(
        self, **kwargs: Unpack[BatchUpdateBillScenarioCommitmentModificationRequestTypeDef]
    ) -> BatchUpdateBillScenarioCommitmentModificationResponseTypeDef:
        """
        Update a newly added or existing commitment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_update_bill_scenario_commitment_modification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_update_bill_scenario_commitment_modification)
        """

    def batch_update_bill_scenario_usage_modification(
        self, **kwargs: Unpack[BatchUpdateBillScenarioUsageModificationRequestTypeDef]
    ) -> BatchUpdateBillScenarioUsageModificationResponseTypeDef:
        """
        Update a newly added or existing usage lines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_update_bill_scenario_usage_modification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_update_bill_scenario_usage_modification)
        """

    def batch_update_workload_estimate_usage(
        self, **kwargs: Unpack[BatchUpdateWorkloadEstimateUsageRequestTypeDef]
    ) -> BatchUpdateWorkloadEstimateUsageResponseTypeDef:
        """
        Update a newly added or existing usage lines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/batch_update_workload_estimate_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#batch_update_workload_estimate_usage)
        """

    def create_bill_estimate(
        self, **kwargs: Unpack[CreateBillEstimateRequestTypeDef]
    ) -> CreateBillEstimateResponseTypeDef:
        """
        Create a Bill estimate from a Bill scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/create_bill_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#create_bill_estimate)
        """

    def create_bill_scenario(
        self, **kwargs: Unpack[CreateBillScenarioRequestTypeDef]
    ) -> CreateBillScenarioResponseTypeDef:
        """
        Creates a new bill scenario to model potential changes to Amazon Web Services
        usage and costs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/create_bill_scenario.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#create_bill_scenario)
        """

    def create_workload_estimate(
        self, **kwargs: Unpack[CreateWorkloadEstimateRequestTypeDef]
    ) -> CreateWorkloadEstimateResponseTypeDef:
        """
        Creates a new workload estimate to model costs for a specific workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/create_workload_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#create_workload_estimate)
        """

    def delete_bill_estimate(
        self, **kwargs: Unpack[DeleteBillEstimateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/delete_bill_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#delete_bill_estimate)
        """

    def delete_bill_scenario(
        self, **kwargs: Unpack[DeleteBillScenarioRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing bill scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/delete_bill_scenario.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#delete_bill_scenario)
        """

    def delete_workload_estimate(
        self, **kwargs: Unpack[DeleteWorkloadEstimateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing workload estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/delete_workload_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#delete_workload_estimate)
        """

    def get_bill_estimate(
        self, **kwargs: Unpack[GetBillEstimateRequestTypeDef]
    ) -> GetBillEstimateResponseTypeDef:
        """
        Retrieves details of a specific bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_bill_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_bill_estimate)
        """

    def get_bill_scenario(
        self, **kwargs: Unpack[GetBillScenarioRequestTypeDef]
    ) -> GetBillScenarioResponseTypeDef:
        """
        Retrieves details of a specific bill scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_bill_scenario.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_bill_scenario)
        """

    def get_preferences(self) -> GetPreferencesResponseTypeDef:
        """
        Retrieves the current preferences for Pricing Calculator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_preferences)
        """

    def get_workload_estimate(
        self, **kwargs: Unpack[GetWorkloadEstimateRequestTypeDef]
    ) -> GetWorkloadEstimateResponseTypeDef:
        """
        Retrieves details of a specific workload estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_workload_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_workload_estimate)
        """

    def list_bill_estimate_commitments(
        self, **kwargs: Unpack[ListBillEstimateCommitmentsRequestTypeDef]
    ) -> ListBillEstimateCommitmentsResponseTypeDef:
        """
        Lists the commitments associated with a bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_estimate_commitments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_estimate_commitments)
        """

    def list_bill_estimate_input_commitment_modifications(
        self, **kwargs: Unpack[ListBillEstimateInputCommitmentModificationsRequestTypeDef]
    ) -> ListBillEstimateInputCommitmentModificationsResponseTypeDef:
        """
        Lists the input commitment modifications associated with a bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_estimate_input_commitment_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_estimate_input_commitment_modifications)
        """

    def list_bill_estimate_input_usage_modifications(
        self, **kwargs: Unpack[ListBillEstimateInputUsageModificationsRequestTypeDef]
    ) -> ListBillEstimateInputUsageModificationsResponseTypeDef:
        """
        Lists the input usage modifications associated with a bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_estimate_input_usage_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_estimate_input_usage_modifications)
        """

    def list_bill_estimate_line_items(
        self, **kwargs: Unpack[ListBillEstimateLineItemsRequestTypeDef]
    ) -> ListBillEstimateLineItemsResponseTypeDef:
        """
        Lists the line items associated with a bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_estimate_line_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_estimate_line_items)
        """

    def list_bill_estimates(
        self, **kwargs: Unpack[ListBillEstimatesRequestTypeDef]
    ) -> ListBillEstimatesResponseTypeDef:
        """
        Lists all bill estimates for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_estimates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_estimates)
        """

    def list_bill_scenario_commitment_modifications(
        self, **kwargs: Unpack[ListBillScenarioCommitmentModificationsRequestTypeDef]
    ) -> ListBillScenarioCommitmentModificationsResponseTypeDef:
        """
        Lists the commitment modifications associated with a bill scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_scenario_commitment_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_scenario_commitment_modifications)
        """

    def list_bill_scenario_usage_modifications(
        self, **kwargs: Unpack[ListBillScenarioUsageModificationsRequestTypeDef]
    ) -> ListBillScenarioUsageModificationsResponseTypeDef:
        """
        Lists the usage modifications associated with a bill scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_scenario_usage_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_scenario_usage_modifications)
        """

    def list_bill_scenarios(
        self, **kwargs: Unpack[ListBillScenariosRequestTypeDef]
    ) -> ListBillScenariosResponseTypeDef:
        """
        Lists all bill scenarios for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_bill_scenarios.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_bill_scenarios)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_tags_for_resource)
        """

    def list_workload_estimate_usage(
        self, **kwargs: Unpack[ListWorkloadEstimateUsageRequestTypeDef]
    ) -> ListWorkloadEstimateUsageResponseTypeDef:
        """
        Lists the usage associated with a workload estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_workload_estimate_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_workload_estimate_usage)
        """

    def list_workload_estimates(
        self, **kwargs: Unpack[ListWorkloadEstimatesRequestTypeDef]
    ) -> ListWorkloadEstimatesResponseTypeDef:
        """
        Lists all workload estimates for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/list_workload_estimates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#list_workload_estimates)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#untag_resource)
        """

    def update_bill_estimate(
        self, **kwargs: Unpack[UpdateBillEstimateRequestTypeDef]
    ) -> UpdateBillEstimateResponseTypeDef:
        """
        Updates an existing bill estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/update_bill_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#update_bill_estimate)
        """

    def update_bill_scenario(
        self, **kwargs: Unpack[UpdateBillScenarioRequestTypeDef]
    ) -> UpdateBillScenarioResponseTypeDef:
        """
        Updates an existing bill scenario.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/update_bill_scenario.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#update_bill_scenario)
        """

    def update_preferences(
        self, **kwargs: Unpack[UpdatePreferencesRequestTypeDef]
    ) -> UpdatePreferencesResponseTypeDef:
        """
        Updates the preferences for Pricing Calculator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/update_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#update_preferences)
        """

    def update_workload_estimate(
        self, **kwargs: Unpack[UpdateWorkloadEstimateRequestTypeDef]
    ) -> UpdateWorkloadEstimateResponseTypeDef:
        """
        Updates an existing workload estimate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/update_workload_estimate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#update_workload_estimate)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_estimate_commitments"]
    ) -> ListBillEstimateCommitmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_estimate_input_commitment_modifications"]
    ) -> ListBillEstimateInputCommitmentModificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_estimate_input_usage_modifications"]
    ) -> ListBillEstimateInputUsageModificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_estimate_line_items"]
    ) -> ListBillEstimateLineItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_estimates"]
    ) -> ListBillEstimatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_scenario_commitment_modifications"]
    ) -> ListBillScenarioCommitmentModificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_scenario_usage_modifications"]
    ) -> ListBillScenarioUsageModificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bill_scenarios"]
    ) -> ListBillScenariosPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workload_estimate_usage"]
    ) -> ListWorkloadEstimateUsagePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workload_estimates"]
    ) -> ListWorkloadEstimatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/client/#get_paginator)
        """
