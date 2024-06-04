"""
Type annotations for kendra-ranking service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra_ranking import KendraRankingClient

    client: KendraRankingClient = boto3.client("kendra-ranking")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CapacityUnitsConfigurationTypeDef,
    CreateRescoreExecutionPlanResponseTypeDef,
    DescribeRescoreExecutionPlanResponseTypeDef,
    DocumentTypeDef,
    ListRescoreExecutionPlansResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RescoreResultTypeDef,
    TagTypeDef,
)

__all__ = ("KendraRankingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class KendraRankingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KendraRankingClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#close)
        """

    def create_rescore_execution_plan(
        self,
        *,
        Name: str,
        Description: str = None,
        CapacityUnits: "CapacityUnitsConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateRescoreExecutionPlanResponseTypeDef:
        """
        Creates a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.create_rescore_execution_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#create_rescore_execution_plan)
        """

    def delete_rescore_execution_plan(self, *, Id: str) -> None:
        """
        Deletes a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.delete_rescore_execution_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#delete_rescore_execution_plan)
        """

    def describe_rescore_execution_plan(
        self, *, Id: str
    ) -> DescribeRescoreExecutionPlanResponseTypeDef:
        """
        Gets information about a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.describe_rescore_execution_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#describe_rescore_execution_plan)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#generate_presigned_url)
        """

    def list_rescore_execution_plans(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListRescoreExecutionPlansResponseTypeDef:
        """
        Lists your rescore execution plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.list_rescore_execution_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#list_rescore_execution_plans)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#list_tags_for_resource)
        """

    def rescore(
        self, *, RescoreExecutionPlanId: str, SearchQuery: str, Documents: List["DocumentTypeDef"]
    ) -> RescoreResultTypeDef:
        """
        Rescores or re-ranks search results from a search service such as OpenSearch
        (self managed).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.rescore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#rescore)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds a specified tag to a specified rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#untag_resource)
        """

    def update_rescore_execution_plan(
        self,
        *,
        Id: str,
        Name: str = None,
        Description: str = None,
        CapacityUnits: "CapacityUnitsConfigurationTypeDef" = None
    ) -> None:
        """
        Updates a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/kendra-ranking.html#KendraRanking.Client.update_rescore_execution_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client.html#update_rescore_execution_plan)
        """
