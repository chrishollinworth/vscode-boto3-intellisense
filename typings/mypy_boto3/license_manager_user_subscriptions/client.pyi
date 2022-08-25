"""
Type annotations for license-manager-user-subscriptions service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_license_manager_user_subscriptions import LicenseManagerUserSubscriptionsClient

    client: LicenseManagerUserSubscriptionsClient = boto3.client("license-manager-user-subscriptions")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListIdentityProvidersPaginator,
    ListInstancesPaginator,
    ListProductSubscriptionsPaginator,
    ListUserAssociationsPaginator,
)
from .type_defs import (
    AssociateUserResponseTypeDef,
    DeregisterIdentityProviderResponseTypeDef,
    DisassociateUserResponseTypeDef,
    FilterTypeDef,
    IdentityProviderTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListProductSubscriptionsResponseTypeDef,
    ListUserAssociationsResponseTypeDef,
    RegisterIdentityProviderResponseTypeDef,
    StartProductSubscriptionResponseTypeDef,
    StopProductSubscriptionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LicenseManagerUserSubscriptionsClient",)

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

class LicenseManagerUserSubscriptionsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LicenseManagerUserSubscriptionsClient exceptions.
        """
    def associate_user(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        InstanceId: str,
        Username: str,
        Domain: str = None
    ) -> AssociateUserResponseTypeDef:
        """
        Associates the user to an EC2 instance to utilize user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.associate_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#associate_user)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#close)
        """
    def deregister_identity_provider(
        self, *, IdentityProvider: "IdentityProviderTypeDef", Product: str
    ) -> DeregisterIdentityProviderResponseTypeDef:
        """
        Deregisters the identity provider from providing user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.deregister_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#deregister_identity_provider)
        """
    def disassociate_user(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        InstanceId: str,
        Username: str,
        Domain: str = None
    ) -> DisassociateUserResponseTypeDef:
        """
        Disassociates the user from an EC2 instance providing user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.disassociate_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#disassociate_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#generate_presigned_url)
        """
    def list_identity_providers(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Lists the identity providers for user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_identity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#list_identity_providers)
        """
    def list_instances(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListInstancesResponseTypeDef:
        """
        Lists the EC2 instances providing user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#list_instances)
        """
    def list_product_subscriptions(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        Product: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListProductSubscriptionsResponseTypeDef:
        """
        Lists the user-based subscription products available from an identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_product_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#list_product_subscriptions)
        """
    def list_user_associations(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        InstanceId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListUserAssociationsResponseTypeDef:
        """
        Lists user associations for an identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.list_user_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#list_user_associations)
        """
    def register_identity_provider(
        self, *, IdentityProvider: "IdentityProviderTypeDef", Product: str
    ) -> RegisterIdentityProviderResponseTypeDef:
        """
        Registers an identity provider for user-based subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.register_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#register_identity_provider)
        """
    def start_product_subscription(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        Product: str,
        Username: str,
        Domain: str = None
    ) -> StartProductSubscriptionResponseTypeDef:
        """
        Starts a product subscription for a user with the specified identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.start_product_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#start_product_subscription)
        """
    def stop_product_subscription(
        self,
        *,
        IdentityProvider: "IdentityProviderTypeDef",
        Product: str,
        Username: str,
        Domain: str = None
    ) -> StopProductSubscriptionResponseTypeDef:
        """
        Stops a product subscription for a user with the specified identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Client.stop_product_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/client.html#stop_product_subscription)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListIdentityProviders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listidentityproviderspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_product_subscriptions"]
    ) -> ListProductSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListProductSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listproductsubscriptionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_associations"]
    ) -> ListUserAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/license-manager-user-subscriptions.html#LicenseManagerUserSubscriptions.Paginator.ListUserAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/paginators.html#listuserassociationspaginator)
        """
