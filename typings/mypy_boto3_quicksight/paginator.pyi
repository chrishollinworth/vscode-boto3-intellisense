"""
Main interface for quicksight service client paginators.

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
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_quicksight.type_defs import (
    AnalysisSearchFilterTypeDef,
    DashboardSearchFilterTypeDef,
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
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
)


class ListAnalysesPaginator(Boto3Paginator):
    """
    [Paginator.ListAnalyses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses)
    """

    def paginate(
        self, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnalysesResponseTypeDef]:
        """
        [ListAnalyses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListAnalyses.paginate)
        """


class ListDashboardVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDashboardVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions)
    """

    def paginate(
        self, AwsAccountId: str, DashboardId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardVersionsResponseTypeDef]:
        """
        [ListDashboardVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDashboardVersions.paginate)
        """


class ListDashboardsPaginator(Boto3Paginator):
    """
    [Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards)
    """

    def paginate(
        self, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsResponseTypeDef]:
        """
        [ListDashboards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDashboards.paginate)
        """


class ListDataSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets)
    """

    def paginate(
        self, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSetsResponseTypeDef]:
        """
        [ListDataSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDataSets.paginate)
        """


class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources)
    """

    def paginate(
        self, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        """
        [ListDataSources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListDataSources.paginate)
        """


class ListIngestionsPaginator(Boto3Paginator):
    """
    [Paginator.ListIngestions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions)
    """

    def paginate(
        self, DataSetId: str, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionsResponseTypeDef]:
        """
        [ListIngestions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListIngestions.paginate)
        """


class ListNamespacesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamespaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces)
    """

    def paginate(
        self, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamespacesResponseTypeDef]:
        """
        [ListNamespaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListNamespaces.paginate)
        """


class ListTemplateAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListTemplateAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases)
    """

    def paginate(
        self, AwsAccountId: str, TemplateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateAliasesResponseTypeDef]:
        """
        [ListTemplateAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateAliases.paginate)
        """


class ListTemplateVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTemplateVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions)
    """

    def paginate(
        self, AwsAccountId: str, TemplateId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplateVersionsResponseTypeDef]:
        """
        [ListTemplateVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListTemplateVersions.paginate)
        """


class ListTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates)
    """

    def paginate(
        self, AwsAccountId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTemplatesResponseTypeDef]:
        """
        [ListTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListTemplates.paginate)
        """


class ListThemeVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListThemeVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions)
    """

    def paginate(
        self, AwsAccountId: str, ThemeId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListThemeVersionsResponseTypeDef]:
        """
        [ListThemeVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListThemeVersions.paginate)
        """


class ListThemesPaginator(Boto3Paginator):
    """
    [Paginator.ListThemes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListThemes)
    """

    def paginate(
        self,
        AwsAccountId: str,
        Type: Literal["QUICKSIGHT", "CUSTOM", "ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListThemesResponseTypeDef]:
        """
        [ListThemes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.ListThemes.paginate)
        """


class SearchAnalysesPaginator(Boto3Paginator):
    """
    [Paginator.SearchAnalyses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses)
    """

    def paginate(
        self,
        AwsAccountId: str,
        Filters: List[AnalysisSearchFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchAnalysesResponseTypeDef]:
        """
        [SearchAnalyses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.SearchAnalyses.paginate)
        """


class SearchDashboardsPaginator(Boto3Paginator):
    """
    [Paginator.SearchDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards)
    """

    def paginate(
        self,
        AwsAccountId: str,
        Filters: List[DashboardSearchFilterTypeDef],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchDashboardsResponseTypeDef]:
        """
        [SearchDashboards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/quicksight.html#QuickSight.Paginator.SearchDashboards.paginate)
        """
