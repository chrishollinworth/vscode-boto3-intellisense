# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for macie service client

Usage::

    ```python
    import boto3
    from mypy_boto3_macie import MacieClient

    client: MacieClient = boto3.client("macie")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_macie.paginator import ListMemberAccountsPaginator, ListS3ResourcesPaginator
from mypy_boto3_macie.type_defs import (
    AssociateS3ResourcesResultTypeDef,
    DisassociateS3ResourcesResultTypeDef,
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    S3ResourceClassificationTypeDef,
    S3ResourceClassificationUpdateTypeDef,
    S3ResourceTypeDef,
    UpdateS3ResourcesResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MacieClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]


class MacieClient:
    """
    [Macie.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_member_account(self, memberAccountId: str) -> None:
        """
        [Client.associate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.associate_member_account)
        """

    def associate_s3_resources(
        self, s3Resources: List["S3ResourceClassificationTypeDef"], memberAccountId: str = None
    ) -> AssociateS3ResourcesResultTypeDef:
        """
        [Client.associate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.associate_s3_resources)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.can_paginate)
        """

    def disassociate_member_account(self, memberAccountId: str) -> None:
        """
        [Client.disassociate_member_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.disassociate_member_account)
        """

    def disassociate_s3_resources(
        self, associatedS3Resources: List["S3ResourceTypeDef"], memberAccountId: str = None
    ) -> DisassociateS3ResourcesResultTypeDef:
        """
        [Client.disassociate_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.disassociate_s3_resources)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.generate_presigned_url)
        """

    def list_member_accounts(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListMemberAccountsResultTypeDef:
        """
        [Client.list_member_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.list_member_accounts)
        """

    def list_s3_resources(
        self, memberAccountId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListS3ResourcesResultTypeDef:
        """
        [Client.list_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.list_s3_resources)
        """

    def update_s3_resources(
        self,
        s3ResourcesUpdate: List[S3ResourceClassificationUpdateTypeDef],
        memberAccountId: str = None,
    ) -> UpdateS3ResourcesResultTypeDef:
        """
        [Client.update_s3_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Client.update_s3_resources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> ListMemberAccountsPaginator:
        """
        [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_s3_resources"]
    ) -> ListS3ResourcesPaginator:
        """
        [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/macie.html#Macie.Paginator.ListS3Resources)
        """
