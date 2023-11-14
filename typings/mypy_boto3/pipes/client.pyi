"""
Type annotations for pipes service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pipes import EventBridgePipesClient

    client: EventBridgePipesClient = boto3.client("pipes")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import PipeStateType, RequestedPipeStateType
from .paginator import ListPipesPaginator
from .type_defs import (
    CreatePipeResponseTypeDef,
    DeletePipeResponseTypeDef,
    DescribePipeResponseTypeDef,
    ListPipesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PipeEnrichmentParametersTypeDef,
    PipeSourceParametersTypeDef,
    PipeTargetParametersTypeDef,
    StartPipeResponseTypeDef,
    StopPipeResponseTypeDef,
    UpdatePipeResponseTypeDef,
    UpdatePipeSourceParametersTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EventBridgePipesClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EventBridgePipesClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EventBridgePipesClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#close)
        """
    def create_pipe(
        self,
        *,
        Name: str,
        RoleArn: str,
        Source: str,
        Target: str,
        Description: str = None,
        DesiredState: RequestedPipeStateType = None,
        Enrichment: str = None,
        EnrichmentParameters: "PipeEnrichmentParametersTypeDef" = None,
        SourceParameters: "PipeSourceParametersTypeDef" = None,
        Tags: Dict[str, str] = None,
        TargetParameters: "PipeTargetParametersTypeDef" = None
    ) -> CreatePipeResponseTypeDef:
        """
        Create a pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.create_pipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#create_pipe)
        """
    def delete_pipe(self, *, Name: str) -> DeletePipeResponseTypeDef:
        """
        Delete an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.delete_pipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#delete_pipe)
        """
    def describe_pipe(self, *, Name: str) -> DescribePipeResponseTypeDef:
        """
        Get the information about an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.describe_pipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#describe_pipe)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#generate_presigned_url)
        """
    def list_pipes(
        self,
        *,
        CurrentState: PipeStateType = None,
        DesiredState: RequestedPipeStateType = None,
        Limit: int = None,
        NamePrefix: str = None,
        NextToken: str = None,
        SourcePrefix: str = None,
        TargetPrefix: str = None
    ) -> ListPipesResponseTypeDef:
        """
        Get the pipes associated with this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.list_pipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#list_pipes)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#list_tags_for_resource)
        """
    def start_pipe(self, *, Name: str) -> StartPipeResponseTypeDef:
        """
        Start an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.start_pipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#start_pipe)
        """
    def stop_pipe(self, *, Name: str) -> StopPipeResponseTypeDef:
        """
        Stop an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.stop_pipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#stop_pipe)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified pipes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#untag_resource)
        """
    def update_pipe(
        self,
        *,
        Name: str,
        RoleArn: str,
        Description: str = None,
        DesiredState: RequestedPipeStateType = None,
        Enrichment: str = None,
        EnrichmentParameters: "PipeEnrichmentParametersTypeDef" = None,
        SourceParameters: "UpdatePipeSourceParametersTypeDef" = None,
        Target: str = None,
        TargetParameters: "PipeTargetParametersTypeDef" = None
    ) -> UpdatePipeResponseTypeDef:
        """
        Update an existing pipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Client.update_pipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/client.html#update_pipe)
        """
    def get_paginator(self, operation_name: Literal["list_pipes"]) -> ListPipesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Paginator.ListPipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/paginators.html#listpipespaginator)
        """
