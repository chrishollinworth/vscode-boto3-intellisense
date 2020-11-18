# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for accessanalyzer service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_accessanalyzer import AccessAnalyzerClient
    from mypy_boto3_accessanalyzer.paginator import (
        ListAnalyzedResourcesPaginator,
        ListAnalyzersPaginator,
        ListArchiveRulesPaginator,
        ListFindingsPaginator,
    )

    client: AccessAnalyzerClient = boto3.client("accessanalyzer")

    list_analyzed_resources_paginator: ListAnalyzedResourcesPaginator = client.get_paginator("list_analyzed_resources")
    list_analyzers_paginator: ListAnalyzersPaginator = client.get_paginator("list_analyzers")
    list_archive_rules_paginator: ListArchiveRulesPaginator = client.get_paginator("list_archive_rules")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    ```
"""
import sys
from typing import Dict, Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_accessanalyzer.type_defs import (
    CriterionTypeDef,
    ListAnalyzedResourcesResponseTypeDef,
    ListAnalyzersResponseTypeDef,
    ListArchiveRulesResponseTypeDef,
    ListFindingsResponseTypeDef,
    PaginatorConfigTypeDef,
    SortCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAnalyzedResourcesPaginator",
    "ListAnalyzersPaginator",
    "ListArchiveRulesPaginator",
    "ListFindingsPaginator",
)


class ListAnalyzedResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListAnalyzedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzedResources)
    """

    def paginate(
        self,
        analyzerArn: str,
        resourceType: Literal[
            "AWS::S3::Bucket",
            "AWS::IAM::Role",
            "AWS::SQS::Queue",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::KMS::Key",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAnalyzedResourcesResponseTypeDef]:
        """
        [ListAnalyzedResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzedResources.paginate)
        """


class ListAnalyzersPaginator(Boto3Paginator):
    """
    [Paginator.ListAnalyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzers)
    """

    def paginate(
        self,
        type: Literal["ACCOUNT", "ORGANIZATION"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAnalyzersResponseTypeDef]:
        """
        [ListAnalyzers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzers.paginate)
        """


class ListArchiveRulesPaginator(Boto3Paginator):
    """
    [Paginator.ListArchiveRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListArchiveRules)
    """

    def paginate(
        self, analyzerName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListArchiveRulesResponseTypeDef]:
        """
        [ListArchiveRules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListArchiveRules.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListFindings)
    """

    def paginate(
        self,
        analyzerArn: str,
        filter: Dict[str, "CriterionTypeDef"] = None,
        sort: SortCriteriaTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFindingsResponseTypeDef]:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListFindings.paginate)
        """
