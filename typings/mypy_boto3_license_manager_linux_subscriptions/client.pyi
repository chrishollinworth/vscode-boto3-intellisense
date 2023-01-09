"""
Type annotations for license-manager-linux-subscriptions service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_license_manager_linux_subscriptions import LicenseManagerLinuxSubscriptionsClient

    client: LicenseManagerLinuxSubscriptionsClient = boto3.client("license-manager-linux-subscriptions")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import LinuxSubscriptionsDiscoveryType
from .paginator import ListLinuxSubscriptionInstancesPaginator, ListLinuxSubscriptionsPaginator
from .type_defs import (
    FilterTypeDef,
    GetServiceSettingsResponseTypeDef,
    LinuxSubscriptionsDiscoverySettingsTypeDef,
    ListLinuxSubscriptionInstancesResponseTypeDef,
    ListLinuxSubscriptionsResponseTypeDef,
    UpdateServiceSettingsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LicenseManagerLinuxSubscriptionsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class LicenseManagerLinuxSubscriptionsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LicenseManagerLinuxSubscriptionsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#generate_presigned_url)
        """
    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        Lists the Linux subscriptions service settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.get_service_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#get_service_settings)
        """
    def list_linux_subscription_instances(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListLinuxSubscriptionInstancesResponseTypeDef:
        """
        Lists the running Amazon EC2 instances that were discovered with commercial
        Linux subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.list_linux_subscription_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#list_linux_subscription_instances)
        """
    def list_linux_subscriptions(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListLinuxSubscriptionsResponseTypeDef:
        """
        Lists the Linux subscriptions that have been discovered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.list_linux_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#list_linux_subscriptions)
        """
    def update_service_settings(
        self,
        *,
        LinuxSubscriptionsDiscovery: LinuxSubscriptionsDiscoveryType,
        LinuxSubscriptionsDiscoverySettings: "LinuxSubscriptionsDiscoverySettingsTypeDef",
        AllowUpdate: bool = None
    ) -> UpdateServiceSettingsResponseTypeDef:
        """
        Updates the service settings for Linux subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Client.update_service_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/client.html#update_service_settings)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_linux_subscription_instances"]
    ) -> ListLinuxSubscriptionInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptionInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html#listlinuxsubscriptioninstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_linux_subscriptions"]
    ) -> ListLinuxSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/license-manager-linux-subscriptions.html#LicenseManagerLinuxSubscriptions.Paginator.ListLinuxSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/paginators.html#listlinuxsubscriptionspaginator)
        """
