"""
Type annotations for osis service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_osis.client import OpenSearchIngestionClient

    session = Session()
    client: OpenSearchIngestionClient = session.client("osis")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreatePipelineRequestTypeDef,
    CreatePipelineResponseTypeDef,
    DeletePipelineRequestTypeDef,
    GetPipelineBlueprintRequestTypeDef,
    GetPipelineBlueprintResponseTypeDef,
    GetPipelineChangeProgressRequestTypeDef,
    GetPipelineChangeProgressResponseTypeDef,
    GetPipelineRequestTypeDef,
    GetPipelineResponseTypeDef,
    ListPipelineBlueprintsResponseTypeDef,
    ListPipelinesRequestTypeDef,
    ListPipelinesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartPipelineRequestTypeDef,
    StartPipelineResponseTypeDef,
    StopPipelineRequestTypeDef,
    StopPipelineResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdatePipelineRequestTypeDef,
    UpdatePipelineResponseTypeDef,
    ValidatePipelineRequestTypeDef,
    ValidatePipelineResponseTypeDef,
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

__all__ = ("OpenSearchIngestionClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class OpenSearchIngestionClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis.html#OpenSearchIngestion.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchIngestionClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis.html#OpenSearchIngestion.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#generate_presigned_url)
        """

    def create_pipeline(
        self, **kwargs: Unpack[CreatePipelineRequestTypeDef]
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/create_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#create_pipeline)
        """

    def delete_pipeline(self, **kwargs: Unpack[DeletePipelineRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/delete_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#delete_pipeline)
        """

    def get_pipeline(
        self, **kwargs: Unpack[GetPipelineRequestTypeDef]
    ) -> GetPipelineResponseTypeDef:
        """
        Retrieves information about an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/get_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#get_pipeline)
        """

    def get_pipeline_blueprint(
        self, **kwargs: Unpack[GetPipelineBlueprintRequestTypeDef]
    ) -> GetPipelineBlueprintResponseTypeDef:
        """
        Retrieves information about a specific blueprint for OpenSearch Ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/get_pipeline_blueprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#get_pipeline_blueprint)
        """

    def get_pipeline_change_progress(
        self, **kwargs: Unpack[GetPipelineChangeProgressRequestTypeDef]
    ) -> GetPipelineChangeProgressResponseTypeDef:
        """
        Returns progress information for the current change happening on an OpenSearch
        Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/get_pipeline_change_progress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#get_pipeline_change_progress)
        """

    def list_pipeline_blueprints(self) -> ListPipelineBlueprintsResponseTypeDef:
        """
        Retrieves a list of all available blueprints for Data Prepper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/list_pipeline_blueprints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#list_pipeline_blueprints)
        """

    def list_pipelines(
        self, **kwargs: Unpack[ListPipelinesRequestTypeDef]
    ) -> ListPipelinesResponseTypeDef:
        """
        Lists all OpenSearch Ingestion pipelines in the current Amazon Web Services
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/list_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#list_pipelines)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all resource tags associated with an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#list_tags_for_resource)
        """

    def start_pipeline(
        self, **kwargs: Unpack[StartPipelineRequestTypeDef]
    ) -> StartPipelineResponseTypeDef:
        """
        Starts an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/start_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#start_pipeline)
        """

    def stop_pipeline(
        self, **kwargs: Unpack[StopPipelineRequestTypeDef]
    ) -> StopPipelineResponseTypeDef:
        """
        Stops an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/stop_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#stop_pipeline)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#untag_resource)
        """

    def update_pipeline(
        self, **kwargs: Unpack[UpdatePipelineRequestTypeDef]
    ) -> UpdatePipelineResponseTypeDef:
        """
        Updates an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/update_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#update_pipeline)
        """

    def validate_pipeline(
        self, **kwargs: Unpack[ValidatePipelineRequestTypeDef]
    ) -> ValidatePipelineResponseTypeDef:
        """
        Checks whether an OpenSearch Ingestion pipeline configuration is valid prior to
        creation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/client/validate_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/client/#validate_pipeline)
        """
