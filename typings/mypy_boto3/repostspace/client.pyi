"""
Type annotations for repostspace service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_repostspace.client import RePostPrivateClient

    session = Session()
    client: RePostPrivateClient = session.client("repostspace")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListSpacesPaginator
from .type_defs import (
    BatchAddRoleInputTypeDef,
    BatchAddRoleOutputTypeDef,
    BatchRemoveRoleInputTypeDef,
    BatchRemoveRoleOutputTypeDef,
    CreateSpaceInputTypeDef,
    CreateSpaceOutputTypeDef,
    DeleteSpaceInputTypeDef,
    DeregisterAdminInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetSpaceInputTypeDef,
    GetSpaceOutputTypeDef,
    ListSpacesInputTypeDef,
    ListSpacesOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterAdminInputTypeDef,
    SendInvitesInputTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateSpaceInputTypeDef,
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

__all__ = ("RePostPrivateClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RePostPrivateClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace.html#RePostPrivate.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RePostPrivateClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace.html#RePostPrivate.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#generate_presigned_url)
        """

    def batch_add_role(
        self, **kwargs: Unpack[BatchAddRoleInputTypeDef]
    ) -> BatchAddRoleOutputTypeDef:
        """
        Add role to multiple users or groups in a private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/batch_add_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#batch_add_role)
        """

    def batch_remove_role(
        self, **kwargs: Unpack[BatchRemoveRoleInputTypeDef]
    ) -> BatchRemoveRoleOutputTypeDef:
        """
        Remove role from multiple users or groups in a private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/batch_remove_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#batch_remove_role)
        """

    def create_space(self, **kwargs: Unpack[CreateSpaceInputTypeDef]) -> CreateSpaceOutputTypeDef:
        """
        Creates an AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/create_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#create_space)
        """

    def delete_space(
        self, **kwargs: Unpack[DeleteSpaceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/delete_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#delete_space)
        """

    def deregister_admin(
        self, **kwargs: Unpack[DeregisterAdminInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the user or group from the list of administrators of the private
        re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/deregister_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#deregister_admin)
        """

    def get_space(self, **kwargs: Unpack[GetSpaceInputTypeDef]) -> GetSpaceOutputTypeDef:
        """
        Displays information about the AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/get_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#get_space)
        """

    def list_spaces(self, **kwargs: Unpack[ListSpacesInputTypeDef]) -> ListSpacesOutputTypeDef:
        """
        Returns a list of AWS re:Post Private private re:Posts in the account with some
        information about each private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/list_spaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#list_spaces)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tags that are associated with the AWS re:Post Private resource
        specified by the resourceArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#list_tags_for_resource)
        """

    def register_admin(
        self, **kwargs: Unpack[RegisterAdminInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a user or group to the list of administrators of the private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/register_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#register_admin)
        """

    def send_invites(
        self, **kwargs: Unpack[SendInvitesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sends an invitation email to selected users and groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/send_invites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#send_invites)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates tags with an AWS re:Post Private resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the association of the tag with the AWS re:Post Private resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#untag_resource)
        """

    def update_space(
        self, **kwargs: Unpack[UpdateSpaceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies an existing AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/update_space.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#update_space)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_spaces"]
    ) -> ListSpacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client/#get_paginator)
        """
