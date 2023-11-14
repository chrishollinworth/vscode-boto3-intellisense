"""
Type annotations for oam service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_oam import CloudWatchObservabilityAccessManagerClient

    client: CloudWatchObservabilityAccessManagerClient = boto3.client("oam")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ResourceTypeType
from .paginator import ListAttachedLinksPaginator, ListLinksPaginator, ListSinksPaginator
from .type_defs import (
    CreateLinkOutputTypeDef,
    CreateSinkOutputTypeDef,
    GetLinkOutputTypeDef,
    GetSinkOutputTypeDef,
    GetSinkPolicyOutputTypeDef,
    ListAttachedLinksOutputTypeDef,
    ListLinksOutputTypeDef,
    ListSinksOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSinkPolicyOutputTypeDef,
    UpdateLinkOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CloudWatchObservabilityAccessManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceFault: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    MissingRequiredParameterException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchObservabilityAccessManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchObservabilityAccessManagerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#close)
        """
    def create_link(
        self,
        *,
        LabelTemplate: str,
        ResourceTypes: List[ResourceTypeType],
        SinkIdentifier: str,
        Tags: Dict[str, str] = None
    ) -> CreateLinkOutputTypeDef:
        """
        Creates a link between a source account and a sink that you have created in a
        monitoring account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.create_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#create_link)
        """
    def create_sink(self, *, Name: str, Tags: Dict[str, str] = None) -> CreateSinkOutputTypeDef:
        """
        Use this to create a *sink* in the current account, so that it can be used as a
        monitoring account in CloudWatch cross-account observability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.create_sink)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#create_sink)
        """
    def delete_link(self, *, Identifier: str) -> Dict[str, Any]:
        """
        Deletes a link between a monitoring account sink and a source account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.delete_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#delete_link)
        """
    def delete_sink(self, *, Identifier: str) -> Dict[str, Any]:
        """
        Deletes a sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.delete_sink)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#delete_sink)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#generate_presigned_url)
        """
    def get_link(self, *, Identifier: str) -> GetLinkOutputTypeDef:
        """
        Returns complete information about one link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#get_link)
        """
    def get_sink(self, *, Identifier: str) -> GetSinkOutputTypeDef:
        """
        Returns complete information about one monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_sink)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#get_sink)
        """
    def get_sink_policy(self, *, SinkIdentifier: str) -> GetSinkPolicyOutputTypeDef:
        """
        Returns the current sink policy attached to this sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.get_sink_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#get_sink_policy)
        """
    def list_attached_links(
        self, *, SinkIdentifier: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAttachedLinksOutputTypeDef:
        """
        Returns a list of source account links that are linked to this monitoring
        account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_attached_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#list_attached_links)
        """
    def list_links(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListLinksOutputTypeDef:
        """
        Use this operation in a source account to return a list of links to monitoring
        account sinks that this source account has.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#list_links)
        """
    def list_sinks(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListSinksOutputTypeDef:
        """
        Use this operation in a monitoring account to return the list of sinks created
        in that account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_sinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#list_sinks)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Displays the tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#list_tags_for_resource)
        """
    def put_sink_policy(self, *, SinkIdentifier: str, Policy: str) -> PutSinkPolicyOutputTypeDef:
        """
        Creates or updates the resource policy that grants permissions to source
        accounts to link to the monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.put_sink_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#put_sink_policy)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#untag_resource)
        """
    def update_link(
        self, *, Identifier: str, ResourceTypes: List[ResourceTypeType]
    ) -> UpdateLinkOutputTypeDef:
        """
        Use this operation to change what types of data are shared from a source account
        to its linked monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client.update_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/client.html#update_link)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_attached_links"]
    ) -> ListAttachedLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListAttachedLinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listattachedlinkspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_links"]) -> ListLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListLinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listlinkspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_sinks"]) -> ListSinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/oam.html#CloudWatchObservabilityAccessManager.Paginator.ListSinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/paginators.html#listsinkspaginator)
        """
