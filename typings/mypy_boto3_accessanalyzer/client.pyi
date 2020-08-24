# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for accessanalyzer service client

Usage::

    ```python
    import boto3
    from mypy_boto3_accessanalyzer import AccessAnalyzerClient

    client: AccessAnalyzerClient = boto3.client("accessanalyzer")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_accessanalyzer.paginator import (
    ListAnalyzedResourcesPaginator,
    ListAnalyzersPaginator,
    ListArchiveRulesPaginator,
    ListFindingsPaginator,
)
from mypy_boto3_accessanalyzer.type_defs import (
    CreateAnalyzerResponseTypeDef,
    CriterionTypeDef,
    GetAnalyzedResourceResponseTypeDef,
    GetAnalyzerResponseTypeDef,
    GetArchiveRuleResponseTypeDef,
    GetFindingResponseTypeDef,
    InlineArchiveRuleTypeDef,
    ListAnalyzedResourcesResponseTypeDef,
    ListAnalyzersResponseTypeDef,
    ListArchiveRulesResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SortCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AccessAnalyzerClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceQuotaExceededException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class AccessAnalyzerClient:
    """
    [AccessAnalyzer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.can_paginate)
        """

    def create_analyzer(
        self,
        analyzerName: str,
        type: Literal["ACCOUNT", "ORGANIZATION"],
        archiveRules: List[InlineArchiveRuleTypeDef] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAnalyzerResponseTypeDef:
        """
        [Client.create_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_analyzer)
        """

    def create_archive_rule(
        self,
        analyzerName: str,
        filter: Dict[str, "CriterionTypeDef"],
        ruleName: str,
        clientToken: str = None,
    ) -> None:
        """
        [Client.create_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.create_archive_rule)
        """

    def delete_analyzer(self, analyzerName: str, clientToken: str = None) -> None:
        """
        [Client.delete_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_analyzer)
        """

    def delete_archive_rule(
        self, analyzerName: str, ruleName: str, clientToken: str = None
    ) -> None:
        """
        [Client.delete_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.delete_archive_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.generate_presigned_url)
        """

    def get_analyzed_resource(
        self, analyzerArn: str, resourceArn: str
    ) -> GetAnalyzedResourceResponseTypeDef:
        """
        [Client.get_analyzed_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzed_resource)
        """

    def get_analyzer(self, analyzerName: str) -> GetAnalyzerResponseTypeDef:
        """
        [Client.get_analyzer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_analyzer)
        """

    def get_archive_rule(self, analyzerName: str, ruleName: str) -> GetArchiveRuleResponseTypeDef:
        """
        [Client.get_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_archive_rule)
        """

    def get_finding(self, analyzerArn: str, id: str) -> GetFindingResponseTypeDef:
        """
        [Client.get_finding documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.get_finding)
        """

    def list_analyzed_resources(
        self,
        analyzerArn: str,
        maxResults: int = None,
        nextToken: str = None,
        resourceType: Literal[
            "AWS::IAM::Role",
            "AWS::KMS::Key",
            "AWS::Lambda::Function",
            "AWS::Lambda::LayerVersion",
            "AWS::S3::Bucket",
            "AWS::SQS::Queue",
        ] = None,
    ) -> ListAnalyzedResourcesResponseTypeDef:
        """
        [Client.list_analyzed_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzed_resources)
        """

    def list_analyzers(
        self,
        maxResults: int = None,
        nextToken: str = None,
        type: Literal["ACCOUNT", "ORGANIZATION"] = None,
    ) -> ListAnalyzersResponseTypeDef:
        """
        [Client.list_analyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_analyzers)
        """

    def list_archive_rules(
        self, analyzerName: str, maxResults: int = None, nextToken: str = None
    ) -> ListArchiveRulesResponseTypeDef:
        """
        [Client.list_archive_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_archive_rules)
        """

    def list_findings(
        self,
        analyzerArn: str,
        filter: Dict[str, "CriterionTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        sort: SortCriteriaTypeDef = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_findings)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.list_tags_for_resource)
        """

    def start_resource_scan(self, analyzerArn: str, resourceArn: str) -> None:
        """
        [Client.start_resource_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.start_resource_scan)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.untag_resource)
        """

    def update_archive_rule(
        self,
        analyzerName: str,
        filter: Dict[str, "CriterionTypeDef"],
        ruleName: str,
        clientToken: str = None,
    ) -> None:
        """
        [Client.update_archive_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_archive_rule)
        """

    def update_findings(
        self,
        analyzerArn: str,
        status: Literal["ACTIVE", "ARCHIVED"],
        clientToken: str = None,
        ids: List[str] = None,
        resourceArn: str = None,
    ) -> None:
        """
        [Client.update_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Client.update_findings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_analyzed_resources"]
    ) -> ListAnalyzedResourcesPaginator:
        """
        [Paginator.ListAnalyzedResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzedResources)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_analyzers"]) -> ListAnalyzersPaginator:
        """
        [Paginator.ListAnalyzers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListAnalyzers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_archive_rules"]
    ) -> ListArchiveRulesPaginator:
        """
        [Paginator.ListArchiveRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListArchiveRules)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/accessanalyzer.html#AccessAnalyzer.Paginator.ListFindings)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
