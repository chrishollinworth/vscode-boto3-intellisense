"""
Type annotations for servicecatalog service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_servicecatalog.client import ServiceCatalogClient

    session = Session()
    client: ServiceCatalogClient = session.client("servicecatalog")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAcceptedPortfolioSharesPaginator,
    ListConstraintsForPortfolioPaginator,
    ListLaunchPathsPaginator,
    ListOrganizationPortfolioAccessPaginator,
    ListPortfoliosForProductPaginator,
    ListPortfoliosPaginator,
    ListPrincipalsForPortfolioPaginator,
    ListProvisionedProductPlansPaginator,
    ListProvisioningArtifactsForServiceActionPaginator,
    ListRecordHistoryPaginator,
    ListResourcesForTagOptionPaginator,
    ListServiceActionsForProvisioningArtifactPaginator,
    ListServiceActionsPaginator,
    ListTagOptionsPaginator,
    ScanProvisionedProductsPaginator,
    SearchProductsAsAdminPaginator,
)
from .type_defs import (
    AcceptPortfolioShareInputTypeDef,
    AssociateBudgetWithResourceInputTypeDef,
    AssociatePrincipalWithPortfolioInputTypeDef,
    AssociateProductWithPortfolioInputTypeDef,
    AssociateServiceActionWithProvisioningArtifactInputTypeDef,
    AssociateTagOptionWithResourceInputTypeDef,
    BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef,
    BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef,
    BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef,
    BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef,
    CopyProductInputTypeDef,
    CopyProductOutputTypeDef,
    CreateConstraintInputTypeDef,
    CreateConstraintOutputTypeDef,
    CreatePortfolioInputTypeDef,
    CreatePortfolioOutputTypeDef,
    CreatePortfolioShareInputTypeDef,
    CreatePortfolioShareOutputTypeDef,
    CreateProductInputTypeDef,
    CreateProductOutputTypeDef,
    CreateProvisionedProductPlanInputTypeDef,
    CreateProvisionedProductPlanOutputTypeDef,
    CreateProvisioningArtifactInputTypeDef,
    CreateProvisioningArtifactOutputTypeDef,
    CreateServiceActionInputTypeDef,
    CreateServiceActionOutputTypeDef,
    CreateTagOptionInputTypeDef,
    CreateTagOptionOutputTypeDef,
    DeleteConstraintInputTypeDef,
    DeletePortfolioInputTypeDef,
    DeletePortfolioShareInputTypeDef,
    DeletePortfolioShareOutputTypeDef,
    DeleteProductInputTypeDef,
    DeleteProvisionedProductPlanInputTypeDef,
    DeleteProvisioningArtifactInputTypeDef,
    DeleteServiceActionInputTypeDef,
    DeleteTagOptionInputTypeDef,
    DescribeConstraintInputTypeDef,
    DescribeConstraintOutputTypeDef,
    DescribeCopyProductStatusInputTypeDef,
    DescribeCopyProductStatusOutputTypeDef,
    DescribePortfolioInputTypeDef,
    DescribePortfolioOutputTypeDef,
    DescribePortfolioSharesInputTypeDef,
    DescribePortfolioSharesOutputTypeDef,
    DescribePortfolioShareStatusInputTypeDef,
    DescribePortfolioShareStatusOutputTypeDef,
    DescribeProductAsAdminInputTypeDef,
    DescribeProductAsAdminOutputTypeDef,
    DescribeProductInputTypeDef,
    DescribeProductOutputTypeDef,
    DescribeProductViewInputTypeDef,
    DescribeProductViewOutputTypeDef,
    DescribeProvisionedProductInputTypeDef,
    DescribeProvisionedProductOutputTypeDef,
    DescribeProvisionedProductPlanInputTypeDef,
    DescribeProvisionedProductPlanOutputTypeDef,
    DescribeProvisioningArtifactInputTypeDef,
    DescribeProvisioningArtifactOutputTypeDef,
    DescribeProvisioningParametersInputTypeDef,
    DescribeProvisioningParametersOutputTypeDef,
    DescribeRecordInputTypeDef,
    DescribeRecordOutputTypeDef,
    DescribeServiceActionExecutionParametersInputTypeDef,
    DescribeServiceActionExecutionParametersOutputTypeDef,
    DescribeServiceActionInputTypeDef,
    DescribeServiceActionOutputTypeDef,
    DescribeTagOptionInputTypeDef,
    DescribeTagOptionOutputTypeDef,
    DisassociateBudgetFromResourceInputTypeDef,
    DisassociatePrincipalFromPortfolioInputTypeDef,
    DisassociateProductFromPortfolioInputTypeDef,
    DisassociateServiceActionFromProvisioningArtifactInputTypeDef,
    DisassociateTagOptionFromResourceInputTypeDef,
    ExecuteProvisionedProductPlanInputTypeDef,
    ExecuteProvisionedProductPlanOutputTypeDef,
    ExecuteProvisionedProductServiceActionInputTypeDef,
    ExecuteProvisionedProductServiceActionOutputTypeDef,
    GetAWSOrganizationsAccessStatusOutputTypeDef,
    GetProvisionedProductOutputsInputTypeDef,
    GetProvisionedProductOutputsOutputTypeDef,
    ImportAsProvisionedProductInputTypeDef,
    ImportAsProvisionedProductOutputTypeDef,
    ListAcceptedPortfolioSharesInputTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListBudgetsForResourceInputTypeDef,
    ListBudgetsForResourceOutputTypeDef,
    ListConstraintsForPortfolioInputTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsInputTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessInputTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfolioAccessInputTypeDef,
    ListPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductInputTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosInputTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioInputTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansInputTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionInputTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListProvisioningArtifactsInputTypeDef,
    ListProvisioningArtifactsOutputTypeDef,
    ListRecordHistoryInputTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListResourcesForTagOptionInputTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactInputTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsInputTypeDef,
    ListServiceActionsOutputTypeDef,
    ListStackInstancesForProvisionedProductInputTypeDef,
    ListStackInstancesForProvisionedProductOutputTypeDef,
    ListTagOptionsInputTypeDef,
    ListTagOptionsOutputTypeDef,
    NotifyProvisionProductEngineWorkflowResultInputTypeDef,
    NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef,
    NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef,
    ProvisionProductInputTypeDef,
    ProvisionProductOutputTypeDef,
    RejectPortfolioShareInputTypeDef,
    ScanProvisionedProductsInputTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminInputTypeDef,
    SearchProductsAsAdminOutputTypeDef,
    SearchProductsInputTypeDef,
    SearchProductsOutputTypeDef,
    SearchProvisionedProductsInputTypeDef,
    SearchProvisionedProductsOutputTypeDef,
    TerminateProvisionedProductInputTypeDef,
    TerminateProvisionedProductOutputTypeDef,
    UpdateConstraintInputTypeDef,
    UpdateConstraintOutputTypeDef,
    UpdatePortfolioInputTypeDef,
    UpdatePortfolioOutputTypeDef,
    UpdatePortfolioShareInputTypeDef,
    UpdatePortfolioShareOutputTypeDef,
    UpdateProductInputTypeDef,
    UpdateProductOutputTypeDef,
    UpdateProvisionedProductInputTypeDef,
    UpdateProvisionedProductOutputTypeDef,
    UpdateProvisionedProductPropertiesInputTypeDef,
    UpdateProvisionedProductPropertiesOutputTypeDef,
    UpdateProvisioningArtifactInputTypeDef,
    UpdateProvisioningArtifactOutputTypeDef,
    UpdateServiceActionInputTypeDef,
    UpdateServiceActionOutputTypeDef,
    UpdateTagOptionInputTypeDef,
    UpdateTagOptionOutputTypeDef,
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

__all__ = ("ServiceCatalogClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InvalidParametersException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagOptionNotMigratedException: Type[BotocoreClientError]

class ServiceCatalogClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog.html#ServiceCatalog.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ServiceCatalogClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog.html#ServiceCatalog.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#generate_presigned_url)
        """

    def accept_portfolio_share(
        self, **kwargs: Unpack[AcceptPortfolioShareInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Accepts an offer to share the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/accept_portfolio_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#accept_portfolio_share)
        """

    def associate_budget_with_resource(
        self, **kwargs: Unpack[AssociateBudgetWithResourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the specified budget with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/associate_budget_with_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#associate_budget_with_resource)
        """

    def associate_principal_with_portfolio(
        self, **kwargs: Unpack[AssociatePrincipalWithPortfolioInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the specified principal ARN with the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/associate_principal_with_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#associate_principal_with_portfolio)
        """

    def associate_product_with_portfolio(
        self, **kwargs: Unpack[AssociateProductWithPortfolioInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the specified product with the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/associate_product_with_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#associate_product_with_portfolio)
        """

    def associate_service_action_with_provisioning_artifact(
        self, **kwargs: Unpack[AssociateServiceActionWithProvisioningArtifactInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a self-service action with a provisioning artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/associate_service_action_with_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#associate_service_action_with_provisioning_artifact)
        """

    def associate_tag_option_with_resource(
        self, **kwargs: Unpack[AssociateTagOptionWithResourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Associate the specified TagOption with the specified portfolio or product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/associate_tag_option_with_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#associate_tag_option_with_resource)
        """

    def batch_associate_service_action_with_provisioning_artifact(
        self, **kwargs: Unpack[BatchAssociateServiceActionWithProvisioningArtifactInputTypeDef]
    ) -> BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef:
        """
        Associates multiple self-service actions with provisioning artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/batch_associate_service_action_with_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#batch_associate_service_action_with_provisioning_artifact)
        """

    def batch_disassociate_service_action_from_provisioning_artifact(
        self, **kwargs: Unpack[BatchDisassociateServiceActionFromProvisioningArtifactInputTypeDef]
    ) -> BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef:
        """
        Disassociates a batch of self-service actions from the specified provisioning
        artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/batch_disassociate_service_action_from_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#batch_disassociate_service_action_from_provisioning_artifact)
        """

    def copy_product(self, **kwargs: Unpack[CopyProductInputTypeDef]) -> CopyProductOutputTypeDef:
        """
        Copies the specified source product to the specified target product or a new
        product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/copy_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#copy_product)
        """

    def create_constraint(
        self, **kwargs: Unpack[CreateConstraintInputTypeDef]
    ) -> CreateConstraintOutputTypeDef:
        """
        Creates a constraint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_constraint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_constraint)
        """

    def create_portfolio(
        self, **kwargs: Unpack[CreatePortfolioInputTypeDef]
    ) -> CreatePortfolioOutputTypeDef:
        """
        Creates a portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_portfolio)
        """

    def create_portfolio_share(
        self, **kwargs: Unpack[CreatePortfolioShareInputTypeDef]
    ) -> CreatePortfolioShareOutputTypeDef:
        """
        Shares the specified portfolio with the specified account or organization node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_portfolio_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_portfolio_share)
        """

    def create_product(
        self, **kwargs: Unpack[CreateProductInputTypeDef]
    ) -> CreateProductOutputTypeDef:
        """
        Creates a product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_product)
        """

    def create_provisioned_product_plan(
        self, **kwargs: Unpack[CreateProvisionedProductPlanInputTypeDef]
    ) -> CreateProvisionedProductPlanOutputTypeDef:
        """
        Creates a plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_provisioned_product_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_provisioned_product_plan)
        """

    def create_provisioning_artifact(
        self, **kwargs: Unpack[CreateProvisioningArtifactInputTypeDef]
    ) -> CreateProvisioningArtifactOutputTypeDef:
        """
        Creates a provisioning artifact (also known as a version) for the specified
        product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_provisioning_artifact)
        """

    def create_service_action(
        self, **kwargs: Unpack[CreateServiceActionInputTypeDef]
    ) -> CreateServiceActionOutputTypeDef:
        """
        Creates a self-service action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_service_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_service_action)
        """

    def create_tag_option(
        self, **kwargs: Unpack[CreateTagOptionInputTypeDef]
    ) -> CreateTagOptionOutputTypeDef:
        """
        Creates a TagOption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/create_tag_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#create_tag_option)
        """

    def delete_constraint(self, **kwargs: Unpack[DeleteConstraintInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified constraint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_constraint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_constraint)
        """

    def delete_portfolio(self, **kwargs: Unpack[DeletePortfolioInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_portfolio)
        """

    def delete_portfolio_share(
        self, **kwargs: Unpack[DeletePortfolioShareInputTypeDef]
    ) -> DeletePortfolioShareOutputTypeDef:
        """
        Stops sharing the specified portfolio with the specified account or
        organization node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_portfolio_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_portfolio_share)
        """

    def delete_product(self, **kwargs: Unpack[DeleteProductInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_product)
        """

    def delete_provisioned_product_plan(
        self, **kwargs: Unpack[DeleteProvisionedProductPlanInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_provisioned_product_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_provisioned_product_plan)
        """

    def delete_provisioning_artifact(
        self, **kwargs: Unpack[DeleteProvisioningArtifactInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified provisioning artifact (also known as a version) for the
        specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_provisioning_artifact)
        """

    def delete_service_action(
        self, **kwargs: Unpack[DeleteServiceActionInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a self-service action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_service_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_service_action)
        """

    def delete_tag_option(self, **kwargs: Unpack[DeleteTagOptionInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified TagOption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/delete_tag_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#delete_tag_option)
        """

    def describe_constraint(
        self, **kwargs: Unpack[DescribeConstraintInputTypeDef]
    ) -> DescribeConstraintOutputTypeDef:
        """
        Gets information about the specified constraint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_constraint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_constraint)
        """

    def describe_copy_product_status(
        self, **kwargs: Unpack[DescribeCopyProductStatusInputTypeDef]
    ) -> DescribeCopyProductStatusOutputTypeDef:
        """
        Gets the status of the specified copy product operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_copy_product_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_copy_product_status)
        """

    def describe_portfolio(
        self, **kwargs: Unpack[DescribePortfolioInputTypeDef]
    ) -> DescribePortfolioOutputTypeDef:
        """
        Gets information about the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_portfolio)
        """

    def describe_portfolio_share_status(
        self, **kwargs: Unpack[DescribePortfolioShareStatusInputTypeDef]
    ) -> DescribePortfolioShareStatusOutputTypeDef:
        """
        Gets the status of the specified portfolio share operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_portfolio_share_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_portfolio_share_status)
        """

    def describe_portfolio_shares(
        self, **kwargs: Unpack[DescribePortfolioSharesInputTypeDef]
    ) -> DescribePortfolioSharesOutputTypeDef:
        """
        Returns a summary of each of the portfolio shares that were created for the
        specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_portfolio_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_portfolio_shares)
        """

    def describe_product(
        self, **kwargs: Unpack[DescribeProductInputTypeDef]
    ) -> DescribeProductOutputTypeDef:
        """
        Gets information about the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_product)
        """

    def describe_product_as_admin(
        self, **kwargs: Unpack[DescribeProductAsAdminInputTypeDef]
    ) -> DescribeProductAsAdminOutputTypeDef:
        """
        Gets information about the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_product_as_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_product_as_admin)
        """

    def describe_product_view(
        self, **kwargs: Unpack[DescribeProductViewInputTypeDef]
    ) -> DescribeProductViewOutputTypeDef:
        """
        Gets information about the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_product_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_product_view)
        """

    def describe_provisioned_product(
        self, **kwargs: Unpack[DescribeProvisionedProductInputTypeDef]
    ) -> DescribeProvisionedProductOutputTypeDef:
        """
        Gets information about the specified provisioned product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_provisioned_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_provisioned_product)
        """

    def describe_provisioned_product_plan(
        self, **kwargs: Unpack[DescribeProvisionedProductPlanInputTypeDef]
    ) -> DescribeProvisionedProductPlanOutputTypeDef:
        """
        Gets information about the resource changes for the specified plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_provisioned_product_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_provisioned_product_plan)
        """

    def describe_provisioning_artifact(
        self, **kwargs: Unpack[DescribeProvisioningArtifactInputTypeDef]
    ) -> DescribeProvisioningArtifactOutputTypeDef:
        """
        Gets information about the specified provisioning artifact (also known as a
        version) for the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_provisioning_artifact)
        """

    def describe_provisioning_parameters(
        self, **kwargs: Unpack[DescribeProvisioningParametersInputTypeDef]
    ) -> DescribeProvisioningParametersOutputTypeDef:
        """
        Gets information about the configuration required to provision the specified
        product using the specified provisioning artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_provisioning_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_provisioning_parameters)
        """

    def describe_record(
        self, **kwargs: Unpack[DescribeRecordInputTypeDef]
    ) -> DescribeRecordOutputTypeDef:
        """
        Gets information about the specified request operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_record)
        """

    def describe_service_action(
        self, **kwargs: Unpack[DescribeServiceActionInputTypeDef]
    ) -> DescribeServiceActionOutputTypeDef:
        """
        Describes a self-service action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_service_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_service_action)
        """

    def describe_service_action_execution_parameters(
        self, **kwargs: Unpack[DescribeServiceActionExecutionParametersInputTypeDef]
    ) -> DescribeServiceActionExecutionParametersOutputTypeDef:
        """
        Finds the default parameters for a specific self-service action on a specific
        provisioned product and returns a map of the results to the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_service_action_execution_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_service_action_execution_parameters)
        """

    def describe_tag_option(
        self, **kwargs: Unpack[DescribeTagOptionInputTypeDef]
    ) -> DescribeTagOptionOutputTypeDef:
        """
        Gets information about the specified TagOption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/describe_tag_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#describe_tag_option)
        """

    def disable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        Disable portfolio sharing through the Organizations service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/disable_aws_organizations_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#disable_aws_organizations_access)
        """

    def disassociate_budget_from_resource(
        self, **kwargs: Unpack[DisassociateBudgetFromResourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified budget from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/disassociate_budget_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#disassociate_budget_from_resource)
        """

    def disassociate_principal_from_portfolio(
        self, **kwargs: Unpack[DisassociatePrincipalFromPortfolioInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a previously associated principal ARN from a specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/disassociate_principal_from_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#disassociate_principal_from_portfolio)
        """

    def disassociate_product_from_portfolio(
        self, **kwargs: Unpack[DisassociateProductFromPortfolioInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified product from the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/disassociate_product_from_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#disassociate_product_from_portfolio)
        """

    def disassociate_service_action_from_provisioning_artifact(
        self, **kwargs: Unpack[DisassociateServiceActionFromProvisioningArtifactInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified self-service action association from the specified
        provisioning artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/disassociate_service_action_from_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#disassociate_service_action_from_provisioning_artifact)
        """

    def disassociate_tag_option_from_resource(
        self, **kwargs: Unpack[DisassociateTagOptionFromResourceInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified TagOption from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/disassociate_tag_option_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#disassociate_tag_option_from_resource)
        """

    def enable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        Enable portfolio sharing feature through Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/enable_aws_organizations_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#enable_aws_organizations_access)
        """

    def execute_provisioned_product_plan(
        self, **kwargs: Unpack[ExecuteProvisionedProductPlanInputTypeDef]
    ) -> ExecuteProvisionedProductPlanOutputTypeDef:
        """
        Provisions or modifies a product based on the resource changes for the
        specified plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/execute_provisioned_product_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#execute_provisioned_product_plan)
        """

    def execute_provisioned_product_service_action(
        self, **kwargs: Unpack[ExecuteProvisionedProductServiceActionInputTypeDef]
    ) -> ExecuteProvisionedProductServiceActionOutputTypeDef:
        """
        Executes a self-service action against a provisioned product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/execute_provisioned_product_service_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#execute_provisioned_product_service_action)
        """

    def get_aws_organizations_access_status(self) -> GetAWSOrganizationsAccessStatusOutputTypeDef:
        """
        Get the Access Status for Organizations portfolio share feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_aws_organizations_access_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_aws_organizations_access_status)
        """

    def get_provisioned_product_outputs(
        self, **kwargs: Unpack[GetProvisionedProductOutputsInputTypeDef]
    ) -> GetProvisionedProductOutputsOutputTypeDef:
        """
        This API takes either a <code>ProvisonedProductId</code> or a
        <code>ProvisionedProductName</code>, along with a list of one or more output
        keys, and responds with the key/value pairs of those outputs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_provisioned_product_outputs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_provisioned_product_outputs)
        """

    def import_as_provisioned_product(
        self, **kwargs: Unpack[ImportAsProvisionedProductInputTypeDef]
    ) -> ImportAsProvisionedProductOutputTypeDef:
        """
        Requests the import of a resource as an Service Catalog provisioned product
        that is associated to an Service Catalog product and provisioning artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/import_as_provisioned_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#import_as_provisioned_product)
        """

    def list_accepted_portfolio_shares(
        self, **kwargs: Unpack[ListAcceptedPortfolioSharesInputTypeDef]
    ) -> ListAcceptedPortfolioSharesOutputTypeDef:
        """
        Lists all imported portfolios for which account-to-account shares were accepted
        by this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_accepted_portfolio_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_accepted_portfolio_shares)
        """

    def list_budgets_for_resource(
        self, **kwargs: Unpack[ListBudgetsForResourceInputTypeDef]
    ) -> ListBudgetsForResourceOutputTypeDef:
        """
        Lists all the budgets associated to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_budgets_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_budgets_for_resource)
        """

    def list_constraints_for_portfolio(
        self, **kwargs: Unpack[ListConstraintsForPortfolioInputTypeDef]
    ) -> ListConstraintsForPortfolioOutputTypeDef:
        """
        Lists the constraints for the specified portfolio and product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_constraints_for_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_constraints_for_portfolio)
        """

    def list_launch_paths(
        self, **kwargs: Unpack[ListLaunchPathsInputTypeDef]
    ) -> ListLaunchPathsOutputTypeDef:
        """
        Lists the paths to the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_launch_paths.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_launch_paths)
        """

    def list_organization_portfolio_access(
        self, **kwargs: Unpack[ListOrganizationPortfolioAccessInputTypeDef]
    ) -> ListOrganizationPortfolioAccessOutputTypeDef:
        """
        Lists the organization nodes that have access to the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_organization_portfolio_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_organization_portfolio_access)
        """

    def list_portfolio_access(
        self, **kwargs: Unpack[ListPortfolioAccessInputTypeDef]
    ) -> ListPortfolioAccessOutputTypeDef:
        """
        Lists the account IDs that have access to the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_portfolio_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_portfolio_access)
        """

    def list_portfolios(
        self, **kwargs: Unpack[ListPortfoliosInputTypeDef]
    ) -> ListPortfoliosOutputTypeDef:
        """
        Lists all portfolios in the catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_portfolios.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_portfolios)
        """

    def list_portfolios_for_product(
        self, **kwargs: Unpack[ListPortfoliosForProductInputTypeDef]
    ) -> ListPortfoliosForProductOutputTypeDef:
        """
        Lists all portfolios that the specified product is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_portfolios_for_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_portfolios_for_product)
        """

    def list_principals_for_portfolio(
        self, **kwargs: Unpack[ListPrincipalsForPortfolioInputTypeDef]
    ) -> ListPrincipalsForPortfolioOutputTypeDef:
        """
        Lists all <code>PrincipalARN</code>s and corresponding
        <code>PrincipalType</code>s associated with the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_principals_for_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_principals_for_portfolio)
        """

    def list_provisioned_product_plans(
        self, **kwargs: Unpack[ListProvisionedProductPlansInputTypeDef]
    ) -> ListProvisionedProductPlansOutputTypeDef:
        """
        Lists the plans for the specified provisioned product or all plans to which the
        user has access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_provisioned_product_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_provisioned_product_plans)
        """

    def list_provisioning_artifacts(
        self, **kwargs: Unpack[ListProvisioningArtifactsInputTypeDef]
    ) -> ListProvisioningArtifactsOutputTypeDef:
        """
        Lists all provisioning artifacts (also known as versions) for the specified
        product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_provisioning_artifacts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_provisioning_artifacts)
        """

    def list_provisioning_artifacts_for_service_action(
        self, **kwargs: Unpack[ListProvisioningArtifactsForServiceActionInputTypeDef]
    ) -> ListProvisioningArtifactsForServiceActionOutputTypeDef:
        """
        Lists all provisioning artifacts (also known as versions) for the specified
        self-service action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_provisioning_artifacts_for_service_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_provisioning_artifacts_for_service_action)
        """

    def list_record_history(
        self, **kwargs: Unpack[ListRecordHistoryInputTypeDef]
    ) -> ListRecordHistoryOutputTypeDef:
        """
        Lists the specified requests or all performed requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_record_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_record_history)
        """

    def list_resources_for_tag_option(
        self, **kwargs: Unpack[ListResourcesForTagOptionInputTypeDef]
    ) -> ListResourcesForTagOptionOutputTypeDef:
        """
        Lists the resources associated with the specified TagOption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_resources_for_tag_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_resources_for_tag_option)
        """

    def list_service_actions(
        self, **kwargs: Unpack[ListServiceActionsInputTypeDef]
    ) -> ListServiceActionsOutputTypeDef:
        """
        Lists all self-service actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_service_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_service_actions)
        """

    def list_service_actions_for_provisioning_artifact(
        self, **kwargs: Unpack[ListServiceActionsForProvisioningArtifactInputTypeDef]
    ) -> ListServiceActionsForProvisioningArtifactOutputTypeDef:
        """
        Returns a paginated list of self-service actions associated with the specified
        Product ID and Provisioning Artifact ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_service_actions_for_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_service_actions_for_provisioning_artifact)
        """

    def list_stack_instances_for_provisioned_product(
        self, **kwargs: Unpack[ListStackInstancesForProvisionedProductInputTypeDef]
    ) -> ListStackInstancesForProvisionedProductOutputTypeDef:
        """
        Returns summary information about stack instances that are associated with the
        specified <code>CFN_STACKSET</code> type provisioned product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_stack_instances_for_provisioned_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_stack_instances_for_provisioned_product)
        """

    def list_tag_options(
        self, **kwargs: Unpack[ListTagOptionsInputTypeDef]
    ) -> ListTagOptionsOutputTypeDef:
        """
        Lists the specified TagOptions or all TagOptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/list_tag_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#list_tag_options)
        """

    def notify_provision_product_engine_workflow_result(
        self, **kwargs: Unpack[NotifyProvisionProductEngineWorkflowResultInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Notifies the result of the provisioning engine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/notify_provision_product_engine_workflow_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#notify_provision_product_engine_workflow_result)
        """

    def notify_terminate_provisioned_product_engine_workflow_result(
        self, **kwargs: Unpack[NotifyTerminateProvisionedProductEngineWorkflowResultInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Notifies the result of the terminate engine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/notify_terminate_provisioned_product_engine_workflow_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#notify_terminate_provisioned_product_engine_workflow_result)
        """

    def notify_update_provisioned_product_engine_workflow_result(
        self, **kwargs: Unpack[NotifyUpdateProvisionedProductEngineWorkflowResultInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Notifies the result of the update engine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/notify_update_provisioned_product_engine_workflow_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#notify_update_provisioned_product_engine_workflow_result)
        """

    def provision_product(
        self, **kwargs: Unpack[ProvisionProductInputTypeDef]
    ) -> ProvisionProductOutputTypeDef:
        """
        Provisions the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/provision_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#provision_product)
        """

    def reject_portfolio_share(
        self, **kwargs: Unpack[RejectPortfolioShareInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Rejects an offer to share the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/reject_portfolio_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#reject_portfolio_share)
        """

    def scan_provisioned_products(
        self, **kwargs: Unpack[ScanProvisionedProductsInputTypeDef]
    ) -> ScanProvisionedProductsOutputTypeDef:
        """
        Lists the provisioned products that are available (not terminated).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/scan_provisioned_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#scan_provisioned_products)
        """

    def search_products(
        self, **kwargs: Unpack[SearchProductsInputTypeDef]
    ) -> SearchProductsOutputTypeDef:
        """
        Gets information about the products to which the caller has access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/search_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#search_products)
        """

    def search_products_as_admin(
        self, **kwargs: Unpack[SearchProductsAsAdminInputTypeDef]
    ) -> SearchProductsAsAdminOutputTypeDef:
        """
        Gets information about the products for the specified portfolio or all products.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/search_products_as_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#search_products_as_admin)
        """

    def search_provisioned_products(
        self, **kwargs: Unpack[SearchProvisionedProductsInputTypeDef]
    ) -> SearchProvisionedProductsOutputTypeDef:
        """
        Gets information about the provisioned products that meet the specified
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/search_provisioned_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#search_provisioned_products)
        """

    def terminate_provisioned_product(
        self, **kwargs: Unpack[TerminateProvisionedProductInputTypeDef]
    ) -> TerminateProvisionedProductOutputTypeDef:
        """
        Terminates the specified provisioned product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/terminate_provisioned_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#terminate_provisioned_product)
        """

    def update_constraint(
        self, **kwargs: Unpack[UpdateConstraintInputTypeDef]
    ) -> UpdateConstraintOutputTypeDef:
        """
        Updates the specified constraint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_constraint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_constraint)
        """

    def update_portfolio(
        self, **kwargs: Unpack[UpdatePortfolioInputTypeDef]
    ) -> UpdatePortfolioOutputTypeDef:
        """
        Updates the specified portfolio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_portfolio.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_portfolio)
        """

    def update_portfolio_share(
        self, **kwargs: Unpack[UpdatePortfolioShareInputTypeDef]
    ) -> UpdatePortfolioShareOutputTypeDef:
        """
        Updates the specified portfolio share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_portfolio_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_portfolio_share)
        """

    def update_product(
        self, **kwargs: Unpack[UpdateProductInputTypeDef]
    ) -> UpdateProductOutputTypeDef:
        """
        Updates the specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_product)
        """

    def update_provisioned_product(
        self, **kwargs: Unpack[UpdateProvisionedProductInputTypeDef]
    ) -> UpdateProvisionedProductOutputTypeDef:
        """
        Requests updates to the configuration of the specified provisioned product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_provisioned_product.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_provisioned_product)
        """

    def update_provisioned_product_properties(
        self, **kwargs: Unpack[UpdateProvisionedProductPropertiesInputTypeDef]
    ) -> UpdateProvisionedProductPropertiesOutputTypeDef:
        """
        Requests updates to the properties of the specified provisioned product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_provisioned_product_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_provisioned_product_properties)
        """

    def update_provisioning_artifact(
        self, **kwargs: Unpack[UpdateProvisioningArtifactInputTypeDef]
    ) -> UpdateProvisioningArtifactOutputTypeDef:
        """
        Updates the specified provisioning artifact (also known as a version) for the
        specified product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_provisioning_artifact.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_provisioning_artifact)
        """

    def update_service_action(
        self, **kwargs: Unpack[UpdateServiceActionInputTypeDef]
    ) -> UpdateServiceActionOutputTypeDef:
        """
        Updates a self-service action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_service_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_service_action)
        """

    def update_tag_option(
        self, **kwargs: Unpack[UpdateTagOptionInputTypeDef]
    ) -> UpdateTagOptionOutputTypeDef:
        """
        Updates the specified TagOption.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/update_tag_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#update_tag_option)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_accepted_portfolio_shares"]
    ) -> ListAcceptedPortfolioSharesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_constraints_for_portfolio"]
    ) -> ListConstraintsForPortfolioPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_launch_paths"]
    ) -> ListLaunchPathsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organization_portfolio_access"]
    ) -> ListOrganizationPortfolioAccessPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_portfolios_for_product"]
    ) -> ListPortfoliosForProductPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_portfolios"]
    ) -> ListPortfoliosPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_principals_for_portfolio"]
    ) -> ListPrincipalsForPortfolioPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_provisioned_product_plans"]
    ) -> ListProvisionedProductPlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_provisioning_artifacts_for_service_action"]
    ) -> ListProvisioningArtifactsForServiceActionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_record_history"]
    ) -> ListRecordHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resources_for_tag_option"]
    ) -> ListResourcesForTagOptionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_actions_for_provisioning_artifact"]
    ) -> ListServiceActionsForProvisioningArtifactPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_service_actions"]
    ) -> ListServiceActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tag_options"]
    ) -> ListTagOptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["scan_provisioned_products"]
    ) -> ScanProvisionedProductsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_products_as_admin"]
    ) -> SearchProductsAsAdminPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client/#get_paginator)
        """
