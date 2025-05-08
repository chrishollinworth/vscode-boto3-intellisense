"""
Type annotations for kendra-ranking service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kendra_ranking.client import KendraRankingClient

    session = Session()
    client: KendraRankingClient = session.client("kendra-ranking")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateRescoreExecutionPlanRequestTypeDef,
    CreateRescoreExecutionPlanResponseTypeDef,
    DeleteRescoreExecutionPlanRequestTypeDef,
    DescribeRescoreExecutionPlanRequestTypeDef,
    DescribeRescoreExecutionPlanResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ListRescoreExecutionPlansRequestTypeDef,
    ListRescoreExecutionPlansResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RescoreRequestTypeDef,
    RescoreResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateRescoreExecutionPlanRequestTypeDef,
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

__all__ = ("KendraRankingClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KendraRankingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking.html#KendraRanking.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#generate_presigned_url)
        """

    def create_rescore_execution_plan(
        self, **kwargs: Unpack[CreateRescoreExecutionPlanRequestTypeDef]
    ) -> CreateRescoreExecutionPlanResponseTypeDef:
        """
        Creates a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/create_rescore_execution_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#create_rescore_execution_plan)
        """

    def delete_rescore_execution_plan(
        self, **kwargs: Unpack[DeleteRescoreExecutionPlanRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/delete_rescore_execution_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#delete_rescore_execution_plan)
        """

    def describe_rescore_execution_plan(
        self, **kwargs: Unpack[DescribeRescoreExecutionPlanRequestTypeDef]
    ) -> DescribeRescoreExecutionPlanResponseTypeDef:
        """
        Gets information about a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/describe_rescore_execution_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#describe_rescore_execution_plan)
        """

    def list_rescore_execution_plans(
        self, **kwargs: Unpack[ListRescoreExecutionPlansRequestTypeDef]
    ) -> ListRescoreExecutionPlansResponseTypeDef:
        """
        Lists your rescore execution plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/list_rescore_execution_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#list_rescore_execution_plans)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#list_tags_for_resource)
        """

    def rescore(self, **kwargs: Unpack[RescoreRequestTypeDef]) -> RescoreResultTypeDef:
        """
        Rescores or re-ranks search results from a search service such as OpenSearch
        (self managed).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/rescore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#rescore)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a specified tag to a specified rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#untag_resource)
        """

    def update_rescore_execution_plan(
        self, **kwargs: Unpack[UpdateRescoreExecutionPlanRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a rescore execution plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra-ranking/client/update_rescore_execution_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/client/#update_rescore_execution_plan)
        """
