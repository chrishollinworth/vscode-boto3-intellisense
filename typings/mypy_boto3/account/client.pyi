"""
Type annotations for account service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_account import AccountClient

    client: AccountClient = boto3.client("account")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import AlternateContactTypeType, RegionOptStatusType
from .paginator import ListRegionsPaginator
from .type_defs import (
    ContactInformationTypeDef,
    GetAlternateContactResponseTypeDef,
    GetContactInformationResponseTypeDef,
    GetRegionOptStatusResponseTypeDef,
    ListRegionsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AccountClient",)

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
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AccountClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AccountClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#close)
        """
    def delete_alternate_contact(
        self, *, AlternateContactType: AlternateContactTypeType, AccountId: str = None
    ) -> None:
        """
        Deletes the specified alternate contact from an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.delete_alternate_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#delete_alternate_contact)
        """
    def disable_region(self, *, RegionName: str, AccountId: str = None) -> None:
        """
        Disables (opts-out) a particular Region for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.disable_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#disable_region)
        """
    def enable_region(self, *, RegionName: str, AccountId: str = None) -> None:
        """
        Enables (opts-in) a particular Region for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.enable_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#enable_region)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#generate_presigned_url)
        """
    def get_alternate_contact(
        self, *, AlternateContactType: AlternateContactTypeType, AccountId: str = None
    ) -> GetAlternateContactResponseTypeDef:
        """
        Retrieves the specified alternate contact attached to an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.get_alternate_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#get_alternate_contact)
        """
    def get_contact_information(
        self, *, AccountId: str = None
    ) -> GetContactInformationResponseTypeDef:
        """
        Retrieves the primary contact information of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.get_contact_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#get_contact_information)
        """
    def get_region_opt_status(
        self, *, RegionName: str, AccountId: str = None
    ) -> GetRegionOptStatusResponseTypeDef:
        """
        Retrieves the opt-in status of a particular Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.get_region_opt_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#get_region_opt_status)
        """
    def list_regions(
        self,
        *,
        AccountId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        RegionOptStatusContains: List[RegionOptStatusType] = None
    ) -> ListRegionsResponseTypeDef:
        """
        Lists all the Regions for a given account and their respective opt-in statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.list_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#list_regions)
        """
    def put_alternate_contact(
        self,
        *,
        AlternateContactType: AlternateContactTypeType,
        EmailAddress: str,
        Name: str,
        PhoneNumber: str,
        Title: str,
        AccountId: str = None
    ) -> None:
        """
        Modifies the specified alternate contact attached to an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.put_alternate_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#put_alternate_contact)
        """
    def put_contact_information(
        self, *, ContactInformation: "ContactInformationTypeDef", AccountId: str = None
    ) -> None:
        """
        Updates the primary contact information of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Client.put_contact_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/client.html#put_contact_information)
        """
    def get_paginator(self, operation_name: Literal["list_regions"]) -> ListRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Paginator.ListRegions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/paginators.html#listregionspaginator)
        """
