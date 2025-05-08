"""
Type annotations for oam service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_oam.client import CloudWatchObservabilityAccessManagerClient

    session = Session()
    client: CloudWatchObservabilityAccessManagerClient = session.client("oam")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListAttachedLinksPaginator, ListLinksPaginator, ListSinksPaginator
from .type_defs import (
    CreateLinkInputTypeDef,
    CreateLinkOutputTypeDef,
    CreateSinkInputTypeDef,
    CreateSinkOutputTypeDef,
    DeleteLinkInputTypeDef,
    DeleteSinkInputTypeDef,
    GetLinkInputTypeDef,
    GetLinkOutputTypeDef,
    GetSinkInputTypeDef,
    GetSinkOutputTypeDef,
    GetSinkPolicyInputTypeDef,
    GetSinkPolicyOutputTypeDef,
    ListAttachedLinksInputTypeDef,
    ListAttachedLinksOutputTypeDef,
    ListLinksInputTypeDef,
    ListLinksOutputTypeDef,
    ListSinksInputTypeDef,
    ListSinksOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSinkPolicyInputTypeDef,
    PutSinkPolicyOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateLinkInputTypeDef,
    UpdateLinkOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CloudWatchObservabilityAccessManagerClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchObservabilityAccessManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam.html#CloudWatchObservabilityAccessManager.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#generate_presigned_url)
        """

    def create_link(self, **kwargs: Unpack[CreateLinkInputTypeDef]) -> CreateLinkOutputTypeDef:
        """
        Creates a link between a source account and a sink that you have created in a
        monitoring account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/create_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#create_link)
        """

    def create_sink(self, **kwargs: Unpack[CreateSinkInputTypeDef]) -> CreateSinkOutputTypeDef:
        """
        Use this to create a <i>sink</i> in the current account, so that it can be used
        as a monitoring account in CloudWatch cross-account observability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/create_sink.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#create_sink)
        """

    def delete_link(self, **kwargs: Unpack[DeleteLinkInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a link between a monitoring account sink and a source account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/delete_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#delete_link)
        """

    def delete_sink(self, **kwargs: Unpack[DeleteSinkInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/delete_sink.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#delete_sink)
        """

    def get_link(self, **kwargs: Unpack[GetLinkInputTypeDef]) -> GetLinkOutputTypeDef:
        """
        Returns complete information about one link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/get_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#get_link)
        """

    def get_sink(self, **kwargs: Unpack[GetSinkInputTypeDef]) -> GetSinkOutputTypeDef:
        """
        Returns complete information about one monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/get_sink.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#get_sink)
        """

    def get_sink_policy(
        self, **kwargs: Unpack[GetSinkPolicyInputTypeDef]
    ) -> GetSinkPolicyOutputTypeDef:
        """
        Returns the current sink policy attached to this sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/get_sink_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#get_sink_policy)
        """

    def list_attached_links(
        self, **kwargs: Unpack[ListAttachedLinksInputTypeDef]
    ) -> ListAttachedLinksOutputTypeDef:
        """
        Returns a list of source account links that are linked to this monitoring
        account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/list_attached_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#list_attached_links)
        """

    def list_links(self, **kwargs: Unpack[ListLinksInputTypeDef]) -> ListLinksOutputTypeDef:
        """
        Use this operation in a source account to return a list of links to monitoring
        account sinks that this source account has.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/list_links.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#list_links)
        """

    def list_sinks(self, **kwargs: Unpack[ListSinksInputTypeDef]) -> ListSinksOutputTypeDef:
        """
        Use this operation in a monitoring account to return the list of sinks created
        in that account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/list_sinks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#list_sinks)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Displays the tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#list_tags_for_resource)
        """

    def put_sink_policy(
        self, **kwargs: Unpack[PutSinkPolicyInputTypeDef]
    ) -> PutSinkPolicyOutputTypeDef:
        """
        Creates or updates the resource policy that grants permissions to source
        accounts to link to the monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/put_sink_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#put_sink_policy)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#untag_resource)
        """

    def update_link(self, **kwargs: Unpack[UpdateLinkInputTypeDef]) -> UpdateLinkOutputTypeDef:
        """
        Use this operation to change what types of data are shared from a source
        account to its linked monitoring account sink.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/update_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#update_link)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attached_links"]
    ) -> ListAttachedLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_links"]
    ) -> ListLinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sinks"]
    ) -> ListSinksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/oam/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/client/#get_paginator)
        """
