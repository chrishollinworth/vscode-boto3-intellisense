"""
Type annotations for servicecatalog service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_servicecatalog.client import ServiceCatalogClient
    from mypy_boto3_servicecatalog.paginator import (
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

    session = Session()
    client: ServiceCatalogClient = session.client("servicecatalog")

    list_accepted_portfolio_shares_paginator: ListAcceptedPortfolioSharesPaginator = client.get_paginator("list_accepted_portfolio_shares")
    list_constraints_for_portfolio_paginator: ListConstraintsForPortfolioPaginator = client.get_paginator("list_constraints_for_portfolio")
    list_launch_paths_paginator: ListLaunchPathsPaginator = client.get_paginator("list_launch_paths")
    list_organization_portfolio_access_paginator: ListOrganizationPortfolioAccessPaginator = client.get_paginator("list_organization_portfolio_access")
    list_portfolios_for_product_paginator: ListPortfoliosForProductPaginator = client.get_paginator("list_portfolios_for_product")
    list_portfolios_paginator: ListPortfoliosPaginator = client.get_paginator("list_portfolios")
    list_principals_for_portfolio_paginator: ListPrincipalsForPortfolioPaginator = client.get_paginator("list_principals_for_portfolio")
    list_provisioned_product_plans_paginator: ListProvisionedProductPlansPaginator = client.get_paginator("list_provisioned_product_plans")
    list_provisioning_artifacts_for_service_action_paginator: ListProvisioningArtifactsForServiceActionPaginator = client.get_paginator("list_provisioning_artifacts_for_service_action")
    list_record_history_paginator: ListRecordHistoryPaginator = client.get_paginator("list_record_history")
    list_resources_for_tag_option_paginator: ListResourcesForTagOptionPaginator = client.get_paginator("list_resources_for_tag_option")
    list_service_actions_for_provisioning_artifact_paginator: ListServiceActionsForProvisioningArtifactPaginator = client.get_paginator("list_service_actions_for_provisioning_artifact")
    list_service_actions_paginator: ListServiceActionsPaginator = client.get_paginator("list_service_actions")
    list_tag_options_paginator: ListTagOptionsPaginator = client.get_paginator("list_tag_options")
    scan_provisioned_products_paginator: ScanProvisionedProductsPaginator = client.get_paginator("scan_provisioned_products")
    search_products_as_admin_paginator: SearchProductsAsAdminPaginator = client.get_paginator("search_products_as_admin")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAcceptedPortfolioSharesInputPaginateTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListConstraintsForPortfolioInputPaginateTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsInputPaginateTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessInputPaginateTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductInputPaginateTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosInputPaginateTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioInputPaginateTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansInputPaginateTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionInputPaginateTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListRecordHistoryInputPaginateTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListResourcesForTagOptionInputPaginateTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactInputPaginateTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsInputPaginateTypeDef,
    ListServiceActionsOutputTypeDef,
    ListTagOptionsInputPaginateTypeDef,
    ListTagOptionsOutputTypeDef,
    ScanProvisionedProductsInputPaginateTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminInputPaginateTypeDef,
    SearchProductsAsAdminOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAcceptedPortfolioSharesPaginator",
    "ListConstraintsForPortfolioPaginator",
    "ListLaunchPathsPaginator",
    "ListOrganizationPortfolioAccessPaginator",
    "ListPortfoliosForProductPaginator",
    "ListPortfoliosPaginator",
    "ListPrincipalsForPortfolioPaginator",
    "ListProvisionedProductPlansPaginator",
    "ListProvisioningArtifactsForServiceActionPaginator",
    "ListRecordHistoryPaginator",
    "ListResourcesForTagOptionPaginator",
    "ListServiceActionsForProvisioningArtifactPaginator",
    "ListServiceActionsPaginator",
    "ListTagOptionsPaginator",
    "ScanProvisionedProductsPaginator",
    "SearchProductsAsAdminPaginator",
)

if TYPE_CHECKING:
    _ListAcceptedPortfolioSharesPaginatorBase = Paginator[ListAcceptedPortfolioSharesOutputTypeDef]
else:
    _ListAcceptedPortfolioSharesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAcceptedPortfolioSharesPaginator(_ListAcceptedPortfolioSharesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListAcceptedPortfolioShares.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listacceptedportfoliosharespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAcceptedPortfolioSharesInputPaginateTypeDef]
    ) -> PageIterator[ListAcceptedPortfolioSharesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListAcceptedPortfolioShares.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listacceptedportfoliosharespaginator)
        """

if TYPE_CHECKING:
    _ListConstraintsForPortfolioPaginatorBase = Paginator[ListConstraintsForPortfolioOutputTypeDef]
else:
    _ListConstraintsForPortfolioPaginatorBase = Paginator  # type: ignore[assignment]

class ListConstraintsForPortfolioPaginator(_ListConstraintsForPortfolioPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListConstraintsForPortfolio.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listconstraintsforportfoliopaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConstraintsForPortfolioInputPaginateTypeDef]
    ) -> PageIterator[ListConstraintsForPortfolioOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListConstraintsForPortfolio.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listconstraintsforportfoliopaginator)
        """

if TYPE_CHECKING:
    _ListLaunchPathsPaginatorBase = Paginator[ListLaunchPathsOutputTypeDef]
else:
    _ListLaunchPathsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLaunchPathsPaginator(_ListLaunchPathsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListLaunchPaths.html#ServiceCatalog.Paginator.ListLaunchPaths)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listlaunchpathspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLaunchPathsInputPaginateTypeDef]
    ) -> PageIterator[ListLaunchPathsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListLaunchPaths.html#ServiceCatalog.Paginator.ListLaunchPaths.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listlaunchpathspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationPortfolioAccessPaginatorBase = Paginator[
        ListOrganizationPortfolioAccessOutputTypeDef
    ]
else:
    _ListOrganizationPortfolioAccessPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationPortfolioAccessPaginator(_ListOrganizationPortfolioAccessPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListOrganizationPortfolioAccess.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listorganizationportfolioaccesspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationPortfolioAccessInputPaginateTypeDef]
    ) -> PageIterator[ListOrganizationPortfolioAccessOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListOrganizationPortfolioAccess.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listorganizationportfolioaccesspaginator)
        """

if TYPE_CHECKING:
    _ListPortfoliosForProductPaginatorBase = Paginator[ListPortfoliosForProductOutputTypeDef]
else:
    _ListPortfoliosForProductPaginatorBase = Paginator  # type: ignore[assignment]

class ListPortfoliosForProductPaginator(_ListPortfoliosForProductPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListPortfoliosForProduct.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listportfoliosforproductpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPortfoliosForProductInputPaginateTypeDef]
    ) -> PageIterator[ListPortfoliosForProductOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListPortfoliosForProduct.html#ServiceCatalog.Paginator.ListPortfoliosForProduct.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listportfoliosforproductpaginator)
        """

if TYPE_CHECKING:
    _ListPortfoliosPaginatorBase = Paginator[ListPortfoliosOutputTypeDef]
else:
    _ListPortfoliosPaginatorBase = Paginator  # type: ignore[assignment]

class ListPortfoliosPaginator(_ListPortfoliosPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListPortfolios.html#ServiceCatalog.Paginator.ListPortfolios)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listportfoliospaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPortfoliosInputPaginateTypeDef]
    ) -> PageIterator[ListPortfoliosOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListPortfolios.html#ServiceCatalog.Paginator.ListPortfolios.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listportfoliospaginator)
        """

if TYPE_CHECKING:
    _ListPrincipalsForPortfolioPaginatorBase = Paginator[ListPrincipalsForPortfolioOutputTypeDef]
else:
    _ListPrincipalsForPortfolioPaginatorBase = Paginator  # type: ignore[assignment]

class ListPrincipalsForPortfolioPaginator(_ListPrincipalsForPortfolioPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListPrincipalsForPortfolio.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listprincipalsforportfoliopaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPrincipalsForPortfolioInputPaginateTypeDef]
    ) -> PageIterator[ListPrincipalsForPortfolioOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListPrincipalsForPortfolio.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listprincipalsforportfoliopaginator)
        """

if TYPE_CHECKING:
    _ListProvisionedProductPlansPaginatorBase = Paginator[ListProvisionedProductPlansOutputTypeDef]
else:
    _ListProvisionedProductPlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListProvisionedProductPlansPaginator(_ListProvisionedProductPlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListProvisionedProductPlans.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listprovisionedproductplanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProvisionedProductPlansInputPaginateTypeDef]
    ) -> PageIterator[ListProvisionedProductPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListProvisionedProductPlans.html#ServiceCatalog.Paginator.ListProvisionedProductPlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listprovisionedproductplanspaginator)
        """

if TYPE_CHECKING:
    _ListProvisioningArtifactsForServiceActionPaginatorBase = Paginator[
        ListProvisioningArtifactsForServiceActionOutputTypeDef
    ]
else:
    _ListProvisioningArtifactsForServiceActionPaginatorBase = Paginator  # type: ignore[assignment]

class ListProvisioningArtifactsForServiceActionPaginator(
    _ListProvisioningArtifactsForServiceActionPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListProvisioningArtifactsForServiceAction.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listprovisioningartifactsforserviceactionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProvisioningArtifactsForServiceActionInputPaginateTypeDef]
    ) -> PageIterator[ListProvisioningArtifactsForServiceActionOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListProvisioningArtifactsForServiceAction.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listprovisioningartifactsforserviceactionpaginator)
        """

if TYPE_CHECKING:
    _ListRecordHistoryPaginatorBase = Paginator[ListRecordHistoryOutputTypeDef]
else:
    _ListRecordHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecordHistoryPaginator(_ListRecordHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListRecordHistory.html#ServiceCatalog.Paginator.ListRecordHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listrecordhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecordHistoryInputPaginateTypeDef]
    ) -> PageIterator[ListRecordHistoryOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListRecordHistory.html#ServiceCatalog.Paginator.ListRecordHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listrecordhistorypaginator)
        """

if TYPE_CHECKING:
    _ListResourcesForTagOptionPaginatorBase = Paginator[ListResourcesForTagOptionOutputTypeDef]
else:
    _ListResourcesForTagOptionPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcesForTagOptionPaginator(_ListResourcesForTagOptionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListResourcesForTagOption.html#ServiceCatalog.Paginator.ListResourcesForTagOption)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listresourcesfortagoptionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcesForTagOptionInputPaginateTypeDef]
    ) -> PageIterator[ListResourcesForTagOptionOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListResourcesForTagOption.html#ServiceCatalog.Paginator.ListResourcesForTagOption.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listresourcesfortagoptionpaginator)
        """

if TYPE_CHECKING:
    _ListServiceActionsForProvisioningArtifactPaginatorBase = Paginator[
        ListServiceActionsForProvisioningArtifactOutputTypeDef
    ]
else:
    _ListServiceActionsForProvisioningArtifactPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceActionsForProvisioningArtifactPaginator(
    _ListServiceActionsForProvisioningArtifactPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListServiceActionsForProvisioningArtifact.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listserviceactionsforprovisioningartifactpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceActionsForProvisioningArtifactInputPaginateTypeDef]
    ) -> PageIterator[ListServiceActionsForProvisioningArtifactOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListServiceActionsForProvisioningArtifact.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listserviceactionsforprovisioningartifactpaginator)
        """

if TYPE_CHECKING:
    _ListServiceActionsPaginatorBase = Paginator[ListServiceActionsOutputTypeDef]
else:
    _ListServiceActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceActionsPaginator(_ListServiceActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListServiceActions.html#ServiceCatalog.Paginator.ListServiceActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listserviceactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceActionsInputPaginateTypeDef]
    ) -> PageIterator[ListServiceActionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListServiceActions.html#ServiceCatalog.Paginator.ListServiceActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listserviceactionspaginator)
        """

if TYPE_CHECKING:
    _ListTagOptionsPaginatorBase = Paginator[ListTagOptionsOutputTypeDef]
else:
    _ListTagOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTagOptionsPaginator(_ListTagOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListTagOptions.html#ServiceCatalog.Paginator.ListTagOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listtagoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagOptionsInputPaginateTypeDef]
    ) -> PageIterator[ListTagOptionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ListTagOptions.html#ServiceCatalog.Paginator.ListTagOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#listtagoptionspaginator)
        """

if TYPE_CHECKING:
    _ScanProvisionedProductsPaginatorBase = Paginator[ScanProvisionedProductsOutputTypeDef]
else:
    _ScanProvisionedProductsPaginatorBase = Paginator  # type: ignore[assignment]

class ScanProvisionedProductsPaginator(_ScanProvisionedProductsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ScanProvisionedProducts.html#ServiceCatalog.Paginator.ScanProvisionedProducts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#scanprovisionedproductspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ScanProvisionedProductsInputPaginateTypeDef]
    ) -> PageIterator[ScanProvisionedProductsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/ScanProvisionedProducts.html#ServiceCatalog.Paginator.ScanProvisionedProducts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#scanprovisionedproductspaginator)
        """

if TYPE_CHECKING:
    _SearchProductsAsAdminPaginatorBase = Paginator[SearchProductsAsAdminOutputTypeDef]
else:
    _SearchProductsAsAdminPaginatorBase = Paginator  # type: ignore[assignment]

class SearchProductsAsAdminPaginator(_SearchProductsAsAdminPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/SearchProductsAsAdmin.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#searchproductsasadminpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchProductsAsAdminInputPaginateTypeDef]
    ) -> PageIterator[SearchProductsAsAdminOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog/paginator/SearchProductsAsAdmin.html#ServiceCatalog.Paginator.SearchProductsAsAdmin.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators/#searchproductsasadminpaginator)
        """
