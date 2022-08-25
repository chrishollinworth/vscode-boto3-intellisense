"""
Type annotations for macie service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_macie import MacieClient

    client: MacieClient = boto3.client("macie")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListMemberAccountsPaginator, ListS3ResourcesPaginator
from .type_defs import (
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

class MacieClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MacieClient exceptions.
        """
    def associate_member_account(self, *, memberAccountId: str) -> None:
        """
        (Discontinued) Associates a specified Amazon Web Services account with Amazon
        Macie Classic as a member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.associate_member_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#associate_member_account)
        """
    def associate_s3_resources(
        self, *, s3Resources: List["S3ResourceClassificationTypeDef"], memberAccountId: str = None
    ) -> AssociateS3ResourcesResultTypeDef:
        """
        (Discontinued) Associates specified S3 resources with Amazon Macie Classic for
        monitoring and data classification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.associate_s3_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#associate_s3_resources)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#close)
        """
    def disassociate_member_account(self, *, memberAccountId: str) -> None:
        """
        (Discontinued) Removes the specified member account from Amazon Macie Classic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.disassociate_member_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#disassociate_member_account)
        """
    def disassociate_s3_resources(
        self, *, associatedS3Resources: List["S3ResourceTypeDef"], memberAccountId: str = None
    ) -> DisassociateS3ResourcesResultTypeDef:
        """
        (Discontinued) Removes specified S3 resources from being monitored by Amazon
        Macie Classic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.disassociate_s3_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#disassociate_s3_resources)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#generate_presigned_url)
        """
    def list_member_accounts(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListMemberAccountsResultTypeDef:
        """
        (Discontinued) Lists all Amazon Macie Classic member accounts for the current
        Macie Classic administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.list_member_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#list_member_accounts)
        """
    def list_s3_resources(
        self, *, memberAccountId: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListS3ResourcesResultTypeDef:
        """
        (Discontinued) Lists all the S3 resources associated with Amazon Macie Classic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.list_s3_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#list_s3_resources)
        """
    def update_s3_resources(
        self,
        *,
        s3ResourcesUpdate: List["S3ResourceClassificationUpdateTypeDef"],
        memberAccountId: str = None
    ) -> UpdateS3ResourcesResultTypeDef:
        """
        (Discontinued) Updates the classification types for the specified S3 resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Client.update_s3_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/client.html#update_s3_resources)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> ListMemberAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html#listmemberaccountspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_s3_resources"]
    ) -> ListS3ResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/macie.html#Macie.Paginator.ListS3Resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/paginators.html#lists3resourcespaginator)
        """
