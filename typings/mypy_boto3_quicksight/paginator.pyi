"""
Type annotations for quicksight service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_quicksight import QuickSightClient
    from mypy_boto3_quicksight.paginator import (
        ListAnalysesPaginator,
        ListDashboardVersionsPaginator,
        ListDashboardsPaginator,
        ListDataSetsPaginator,
        ListDataSourcesPaginator,
        ListIngestionsPaginator,
        ListNamespacesPaginator,
        ListTemplateAliasesPaginator,
        ListTemplateVersionsPaginator,
        ListTemplatesPaginator,
        ListThemeVersionsPaginator,
        ListThemesPaginator,
        SearchAnalysesPaginator,
        SearchDashboardsPaginator,
        SearchDataSetsPaginator,
        SearchDataSourcesPaginator,
    )

    client: QuickSightClient = boto3.client("quicksight")

    list_analyses_paginator: ListAnalysesPaginator = client.get_paginator("list_analyses")
    list_dashboard_versions_paginator: ListDashboardVersionsPaginator = client.get_paginator("list_dashboard_versions")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_ingestions_paginator: ListIngestionsPaginator = client.get_paginator("list_ingestions")
    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_template_aliases_paginator: ListTemplateAliasesPaginator = client.get_paginator("list_template_aliases")
    list_template_versions_paginator: ListTemplateVersionsPaginator = client.get_paginator("list_template_versions")
    list_templates_paginator: ListTemplatesPaginator = client.get_paginator("list_templates")
    list_theme_versions_paginator: ListThemeVersionsPaginator = client.get_paginator("list_theme_versions")
    list_themes_paginator: ListThemesPaginator = client.get_paginator("list_themes")
    search_analyses_paginator: SearchAnalysesPaginator = client.get_paginator("search_analyses")
    search_dashboards_paginator: SearchDashboardsPaginator = client.get_paginator("search_dashboards")
    search_data_sets_paginator: SearchDataSetsPaginator = client.get_paginator("search_data_sets")
    search_data_sources_paginator: SearchDataSourcesPaginator = client.get_paginator("search_data_sources")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ThemeTypeType
from .type_defs import (
    AnalysisSearchFilterTypeDef,
    DashboardSearchFilterTypeDef,
    DataSetSearchFilterTypeDef,
    DataSourceSearchFilterTypeDef,
    ListAnalysesResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListDashboardVersionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListNamespacesResponseTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListThemesResponseTypeDef,
    ListThemeVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchAnalysesResponseTypeDef,
    SearchDashboardsResponseTypeDef,
    SearchDataSetsResponseTypeDef,
    SearchDataSourcesResponseTypeDef,
)

__all__ = (
    "ListAnalysesPaginator",
    "ListDashboardVersionsPaginator",
    "ListDashboardsPaginator",
    "ListDataSetsPaginator",
    "ListDataSourcesPaginator",
    "ListIngestionsPaginator",
    "ListNamespacesPaginator",
    "ListTemplateAliasesPaginator",
    "ListTemplateVersionsPaginator",
    "ListTemplatesPaginator",
    "ListThemeVersionsPaginator",
    "ListThemesPaginator",
    "SearchAnalysesPaginator",
    "SearchDashboardsPaginator",
    "SearchDataSetsPaginator",
    "SearchDataSourcesPaginator",
)

class ListAnalysesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalysesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listanalysespaginator)
        """

class ListDashboardVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        DashboardId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardversionspaginator)
        """

class ListDashboardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdashboardspaginator)
        """

class ListDataSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasetspaginator)
        """

class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listdatasourcespaginator)
        """

class ListIngestionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
    """

    def paginate(
        self, *, DataSetId: str, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listingestionspaginator)
        """

class ListNamespacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listnamespacespaginator)
        """

class ListTemplateAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, TemplateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatealiasespaginator)
        """

class ListTemplateVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, TemplateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplateversionspaginator)
        """

class ListTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listtemplatespaginator)
        """

class ListThemeVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
    """

    def paginate(
        self, *, AwsAccountId: str, ThemeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemeversionspaginator)
        """

class ListThemesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Type: ThemeTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.ListThemes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#listthemespaginator)
        """

class SearchAnalysesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["AnalysisSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchAnalysesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchanalysespaginator)
        """

class SearchDashboardsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DashboardSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdashboardspaginator)
        """

class SearchDataSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasetspaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DataSetSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasetspaginator)
        """

class SearchDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasourcespaginator)
    """

    def paginate(
        self,
        *,
        AwsAccountId: str,
        Filters: List["DataSourceSearchFilterTypeDef"],
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/quicksight.html#QuickSight.Paginator.SearchDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/paginators.html#searchdatasourcespaginator)
        """
