"""
Type annotations for partnercentral-channel service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_channel.client import PartnerCentralChannelAPIClient

    session = Session()
    client: PartnerCentralChannelAPIClient = session.client("partnercentral-channel")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListChannelHandshakesPaginator,
    ListProgramManagementAccountsPaginator,
    ListRelationshipsPaginator,
)
from .type_defs import (
    AcceptChannelHandshakeRequestTypeDef,
    AcceptChannelHandshakeResponseTypeDef,
    CancelChannelHandshakeRequestTypeDef,
    CancelChannelHandshakeResponseTypeDef,
    CreateChannelHandshakeRequestTypeDef,
    CreateChannelHandshakeResponseTypeDef,
    CreateProgramManagementAccountRequestTypeDef,
    CreateProgramManagementAccountResponseTypeDef,
    CreateRelationshipRequestTypeDef,
    CreateRelationshipResponseTypeDef,
    DeleteProgramManagementAccountRequestTypeDef,
    DeleteRelationshipRequestTypeDef,
    GetRelationshipRequestTypeDef,
    GetRelationshipResponseTypeDef,
    ListChannelHandshakesRequestTypeDef,
    ListChannelHandshakesResponseTypeDef,
    ListProgramManagementAccountsRequestTypeDef,
    ListProgramManagementAccountsResponseTypeDef,
    ListRelationshipsRequestTypeDef,
    ListRelationshipsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RejectChannelHandshakeRequestTypeDef,
    RejectChannelHandshakeResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateProgramManagementAccountRequestTypeDef,
    UpdateProgramManagementAccountResponseTypeDef,
    UpdateRelationshipRequestTypeDef,
    UpdateRelationshipResponseTypeDef,
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

__all__ = ("PartnerCentralChannelAPIClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PartnerCentralChannelAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel.html#PartnerCentralChannelAPI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PartnerCentralChannelAPIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel.html#PartnerCentralChannelAPI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#generate_presigned_url)
        """

    def accept_channel_handshake(
        self, **kwargs: Unpack[AcceptChannelHandshakeRequestTypeDef]
    ) -> AcceptChannelHandshakeResponseTypeDef:
        """
        Accepts a pending channel handshake request from another AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/accept_channel_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#accept_channel_handshake)
        """

    def cancel_channel_handshake(
        self, **kwargs: Unpack[CancelChannelHandshakeRequestTypeDef]
    ) -> CancelChannelHandshakeResponseTypeDef:
        """
        Cancels a pending channel handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/cancel_channel_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#cancel_channel_handshake)
        """

    def create_channel_handshake(
        self, **kwargs: Unpack[CreateChannelHandshakeRequestTypeDef]
    ) -> CreateChannelHandshakeResponseTypeDef:
        """
        Creates a new channel handshake request to establish a partnership with another
        AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/create_channel_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#create_channel_handshake)
        """

    def create_program_management_account(
        self, **kwargs: Unpack[CreateProgramManagementAccountRequestTypeDef]
    ) -> CreateProgramManagementAccountResponseTypeDef:
        """
        Creates a new program management account for managing partner relationships.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/create_program_management_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#create_program_management_account)
        """

    def create_relationship(
        self, **kwargs: Unpack[CreateRelationshipRequestTypeDef]
    ) -> CreateRelationshipResponseTypeDef:
        """
        Creates a new partner relationship between accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/create_relationship.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#create_relationship)
        """

    def delete_program_management_account(
        self, **kwargs: Unpack[DeleteProgramManagementAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a program management account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/delete_program_management_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#delete_program_management_account)
        """

    def delete_relationship(
        self, **kwargs: Unpack[DeleteRelationshipRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a partner relationship.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/delete_relationship.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#delete_relationship)
        """

    def get_relationship(
        self, **kwargs: Unpack[GetRelationshipRequestTypeDef]
    ) -> GetRelationshipResponseTypeDef:
        """
        Retrieves details of a specific partner relationship.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/get_relationship.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#get_relationship)
        """

    def list_channel_handshakes(
        self, **kwargs: Unpack[ListChannelHandshakesRequestTypeDef]
    ) -> ListChannelHandshakesResponseTypeDef:
        """
        Lists channel handshakes based on specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/list_channel_handshakes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#list_channel_handshakes)
        """

    def list_program_management_accounts(
        self, **kwargs: Unpack[ListProgramManagementAccountsRequestTypeDef]
    ) -> ListProgramManagementAccountsResponseTypeDef:
        """
        Lists program management accounts based on specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/list_program_management_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#list_program_management_accounts)
        """

    def list_relationships(
        self, **kwargs: Unpack[ListRelationshipsRequestTypeDef]
    ) -> ListRelationshipsResponseTypeDef:
        """
        Lists partner relationships based on specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/list_relationships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#list_relationships)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags associated with a specific resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#list_tags_for_resource)
        """

    def reject_channel_handshake(
        self, **kwargs: Unpack[RejectChannelHandshakeRequestTypeDef]
    ) -> RejectChannelHandshakeResponseTypeDef:
        """
        Rejects a pending channel handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/reject_channel_handshake.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#reject_channel_handshake)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#untag_resource)
        """

    def update_program_management_account(
        self, **kwargs: Unpack[UpdateProgramManagementAccountRequestTypeDef]
    ) -> UpdateProgramManagementAccountResponseTypeDef:
        """
        Updates the properties of a program management account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/update_program_management_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#update_program_management_account)
        """

    def update_relationship(
        self, **kwargs: Unpack[UpdateRelationshipRequestTypeDef]
    ) -> UpdateRelationshipResponseTypeDef:
        """
        Updates the properties of a partner relationship.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/update_relationship.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#update_relationship)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channel_handshakes"]
    ) -> ListChannelHandshakesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_program_management_accounts"]
    ) -> ListProgramManagementAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_relationships"]
    ) -> ListRelationshipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-channel/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_channel/client/#get_paginator)
        """
