"""
Type annotations for repostspace service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_repostspace import rePostPrivateClient

    client: rePostPrivateClient = boto3.client("repostspace")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import TierLevelType
from .paginator import ListSpacesPaginator
from .type_defs import (
    CreateSpaceOutputTypeDef,
    GetSpaceOutputTypeDef,
    ListSpacesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("rePostPrivateClient",)

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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class rePostPrivateClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        rePostPrivateClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#close)
        """
    def create_space(
        self,
        *,
        name: str,
        subdomain: str,
        tier: TierLevelType,
        description: str = None,
        roleArn: str = None,
        tags: Dict[str, str] = None,
        userKMSKey: str = None
    ) -> CreateSpaceOutputTypeDef:
        """
        Creates an AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.create_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#create_space)
        """
    def delete_space(self, *, spaceId: str) -> None:
        """
        Deletes an AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.delete_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#delete_space)
        """
    def deregister_admin(self, *, adminId: str, spaceId: str) -> None:
        """
        Removes the user or group from the list of administrators of the private
        re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.deregister_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#deregister_admin)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#generate_presigned_url)
        """
    def get_space(self, *, spaceId: str) -> GetSpaceOutputTypeDef:
        """
        Displays information about the AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.get_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#get_space)
        """
    def list_spaces(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSpacesOutputTypeDef:
        """
        Returns a list of AWS re:Post Private private re:Posts in the account with some
        information about each private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.list_spaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#list_spaces)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tags that are associated with the AWS re:Post Private resource
        specified by the resourceArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#list_tags_for_resource)
        """
    def register_admin(self, *, adminId: str, spaceId: str) -> None:
        """
        Adds a user or group to the list of administrators of the private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.register_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#register_admin)
        """
    def send_invites(self, *, accessorIds: List[str], body: str, spaceId: str, title: str) -> None:
        """
        Sends an invitation email to selected users and groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.send_invites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#send_invites)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates tags with an AWS re:Post Private resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the association of the tag with the AWS re:Post Private resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#untag_resource)
        """
    def update_space(
        self,
        *,
        spaceId: str,
        description: str = None,
        roleArn: str = None,
        tier: TierLevelType = None
    ) -> None:
        """
        Modifies an existing AWS re:Post Private private re:Post.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Client.update_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/client.html#update_space)
        """
    def get_paginator(self, operation_name: Literal["list_spaces"]) -> ListSpacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Paginator.ListSpaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators.html#listspacespaginator)
        """
