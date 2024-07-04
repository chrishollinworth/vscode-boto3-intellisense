"""
Type annotations for osis service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_osis import OpenSearchIngestionClient

    client: OpenSearchIngestionClient = boto3.client("osis")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    BufferOptionsTypeDef,
    CreatePipelineResponseTypeDef,
    EncryptionAtRestOptionsTypeDef,
    GetPipelineBlueprintResponseTypeDef,
    GetPipelineChangeProgressResponseTypeDef,
    GetPipelineResponseTypeDef,
    ListPipelineBlueprintsResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LogPublishingOptionsTypeDef,
    StartPipelineResponseTypeDef,
    StopPipelineResponseTypeDef,
    TagTypeDef,
    UpdatePipelineResponseTypeDef,
    ValidatePipelineResponseTypeDef,
    VpcOptionsTypeDef,
)

__all__ = ("OpenSearchIngestionClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OpenSearchIngestionClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#close)
        """

    def create_pipeline(
        self,
        *,
        PipelineName: str,
        MinUnits: int,
        MaxUnits: int,
        PipelineConfigurationBody: str,
        LogPublishingOptions: "LogPublishingOptionsTypeDef" = None,
        VpcOptions: "VpcOptionsTypeDef" = None,
        BufferOptions: "BufferOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#create_pipeline)
        """

    def delete_pipeline(self, *, PipelineName: str) -> Dict[str, Any]:
        """
        Deletes an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#delete_pipeline)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#generate_presigned_url)
        """

    def get_pipeline(self, *, PipelineName: str) -> GetPipelineResponseTypeDef:
        """
        Retrieves information about an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.get_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#get_pipeline)
        """

    def get_pipeline_blueprint(
        self, *, BlueprintName: str, Format: str = None
    ) -> GetPipelineBlueprintResponseTypeDef:
        """
        Retrieves information about a specific blueprint for OpenSearch Ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.get_pipeline_blueprint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#get_pipeline_blueprint)
        """

    def get_pipeline_change_progress(
        self, *, PipelineName: str
    ) -> GetPipelineChangeProgressResponseTypeDef:
        """
        Returns progress information for the current change happening on an OpenSearch
        Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.get_pipeline_change_progress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#get_pipeline_change_progress)
        """

    def list_pipeline_blueprints(self) -> ListPipelineBlueprintsResponseTypeDef:
        """
        Retrieves a list of all available blueprints for Data Prepper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.list_pipeline_blueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#list_pipeline_blueprints)
        """

    def list_pipelines(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListPipelinesResponseTypeDef:
        """
        Lists all OpenSearch Ingestion pipelines in the current Amazon Web Services
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#list_pipelines)
        """

    def list_tags_for_resource(self, *, Arn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all resource tags associated with an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#list_tags_for_resource)
        """

    def start_pipeline(self, *, PipelineName: str) -> StartPipelineResponseTypeDef:
        """
        Starts an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.start_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#start_pipeline)
        """

    def stop_pipeline(self, *, PipelineName: str) -> StopPipelineResponseTypeDef:
        """
        Stops an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.stop_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#stop_pipeline)
        """

    def tag_resource(self, *, Arn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#tag_resource)
        """

    def untag_resource(self, *, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#untag_resource)
        """

    def update_pipeline(
        self,
        *,
        PipelineName: str,
        MinUnits: int = None,
        MaxUnits: int = None,
        PipelineConfigurationBody: str = None,
        LogPublishingOptions: "LogPublishingOptionsTypeDef" = None,
        BufferOptions: "BufferOptionsTypeDef" = None,
        EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef" = None
    ) -> UpdatePipelineResponseTypeDef:
        """
        Updates an OpenSearch Ingestion pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#update_pipeline)
        """

    def validate_pipeline(
        self, *, PipelineConfigurationBody: str
    ) -> ValidatePipelineResponseTypeDef:
        """
        Checks whether an OpenSearch Ingestion pipeline configuration is valid prior to
        creation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/osis.html#OpenSearchIngestion.Client.validate_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_osis/client.html#validate_pipeline)
        """
