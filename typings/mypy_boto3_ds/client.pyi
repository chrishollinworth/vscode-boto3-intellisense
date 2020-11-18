# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for ds service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ds import DirectoryServiceClient

    client: DirectoryServiceClient = boto3.client("ds")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ds.paginator import (
    DescribeDirectoriesPaginator,
    DescribeDomainControllersPaginator,
    DescribeSharedDirectoriesPaginator,
    DescribeSnapshotsPaginator,
    DescribeTrustsPaginator,
    ListIpRoutesPaginator,
    ListLogSubscriptionsPaginator,
    ListSchemaExtensionsPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_ds.type_defs import (
    AcceptSharedDirectoryResultTypeDef,
    AttributeTypeDef,
    ConnectDirectoryResultTypeDef,
    CreateAliasResultTypeDef,
    CreateComputerResultTypeDef,
    CreateDirectoryResultTypeDef,
    CreateMicrosoftADResultTypeDef,
    CreateSnapshotResultTypeDef,
    CreateTrustResultTypeDef,
    DeleteDirectoryResultTypeDef,
    DeleteSnapshotResultTypeDef,
    DeleteTrustResultTypeDef,
    DescribeCertificateResultTypeDef,
    DescribeConditionalForwardersResultTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeEventTopicsResultTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    DirectoryConnectSettingsTypeDef,
    DirectoryVpcSettingsTypeDef,
    GetDirectoryLimitsResultTypeDef,
    GetSnapshotLimitsResultTypeDef,
    IpRouteTypeDef,
    ListCertificatesResultTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    RadiusSettingsTypeDef,
    RegisterCertificateResultTypeDef,
    RejectSharedDirectoryResultTypeDef,
    ShareDirectoryResultTypeDef,
    ShareTargetTypeDef,
    StartSchemaExtensionResultTypeDef,
    TagTypeDef,
    UnshareDirectoryResultTypeDef,
    UnshareTargetTypeDef,
    UpdateTrustResultTypeDef,
    VerifyTrustResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectoryServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AuthenticationFailedException: Type[BotocoreClientError]
    CertificateAlreadyExistsException: Type[BotocoreClientError]
    CertificateDoesNotExistException: Type[BotocoreClientError]
    CertificateInUseException: Type[BotocoreClientError]
    CertificateLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    DirectoryAlreadySharedException: Type[BotocoreClientError]
    DirectoryDoesNotExistException: Type[BotocoreClientError]
    DirectoryLimitExceededException: Type[BotocoreClientError]
    DirectoryNotSharedException: Type[BotocoreClientError]
    DirectoryUnavailableException: Type[BotocoreClientError]
    DomainControllerLimitExceededException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityDoesNotExistException: Type[BotocoreClientError]
    InsufficientPermissionsException: Type[BotocoreClientError]
    InvalidCertificateException: Type[BotocoreClientError]
    InvalidLDAPSStatusException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    IpRouteLimitExceededException: Type[BotocoreClientError]
    NoAvailableCertificateException: Type[BotocoreClientError]
    OrganizationsException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ShareLimitExceededException: Type[BotocoreClientError]
    SnapshotLimitExceededException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UserDoesNotExistException: Type[BotocoreClientError]


class DirectoryServiceClient:
    """
    [DirectoryService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_shared_directory(self, SharedDirectoryId: str) -> AcceptSharedDirectoryResultTypeDef:
        """
        [Client.accept_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.accept_shared_directory)
        """

    def add_ip_routes(
        self,
        DirectoryId: str,
        IpRoutes: List[IpRouteTypeDef],
        UpdateSecurityGroupForDirectoryControllers: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.add_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.add_ip_routes)
        """

    def add_tags_to_resource(self, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.can_paginate)
        """

    def cancel_schema_extension(self, DirectoryId: str, SchemaExtensionId: str) -> Dict[str, Any]:
        """
        [Client.cancel_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.cancel_schema_extension)
        """

    def connect_directory(
        self,
        Name: str,
        Password: str,
        Size: Literal["Small", "Large"],
        ConnectSettings: DirectoryConnectSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ConnectDirectoryResultTypeDef:
        """
        [Client.connect_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.connect_directory)
        """

    def create_alias(self, DirectoryId: str, Alias: str) -> CreateAliasResultTypeDef:
        """
        [Client.create_alias documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_alias)
        """

    def create_computer(
        self,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str = None,
        ComputerAttributes: List["AttributeTypeDef"] = None,
    ) -> CreateComputerResultTypeDef:
        """
        [Client.create_computer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_computer)
        """

    def create_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.create_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_conditional_forwarder)
        """

    def create_directory(
        self,
        Name: str,
        Password: str,
        Size: Literal["Small", "Large"],
        ShortName: str = None,
        Description: str = None,
        VpcSettings: DirectoryVpcSettingsTypeDef = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDirectoryResultTypeDef:
        """
        [Client.create_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_directory)
        """

    def create_log_subscription(self, DirectoryId: str, LogGroupName: str) -> Dict[str, Any]:
        """
        [Client.create_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_log_subscription)
        """

    def create_microsoft_ad(
        self,
        Name: str,
        Password: str,
        VpcSettings: DirectoryVpcSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Edition: Literal["Enterprise", "Standard"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateMicrosoftADResultTypeDef:
        """
        [Client.create_microsoft_ad documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_microsoft_ad)
        """

    def create_snapshot(self, DirectoryId: str, Name: str = None) -> CreateSnapshotResultTypeDef:
        """
        [Client.create_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_snapshot)
        """

    def create_trust(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: Literal["One-Way: Outgoing", "One-Way: Incoming", "Two-Way"],
        TrustType: Literal["Forest", "External"] = None,
        ConditionalForwarderIpAddrs: List[str] = None,
        SelectiveAuth: Literal["Enabled", "Disabled"] = None,
    ) -> CreateTrustResultTypeDef:
        """
        [Client.create_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.create_trust)
        """

    def delete_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.delete_conditional_forwarder)
        """

    def delete_directory(self, DirectoryId: str) -> DeleteDirectoryResultTypeDef:
        """
        [Client.delete_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.delete_directory)
        """

    def delete_log_subscription(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.delete_log_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.delete_log_subscription)
        """

    def delete_snapshot(self, SnapshotId: str) -> DeleteSnapshotResultTypeDef:
        """
        [Client.delete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.delete_snapshot)
        """

    def delete_trust(
        self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None
    ) -> DeleteTrustResultTypeDef:
        """
        [Client.delete_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.delete_trust)
        """

    def deregister_certificate(self, DirectoryId: str, CertificateId: str) -> Dict[str, Any]:
        """
        [Client.deregister_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.deregister_certificate)
        """

    def deregister_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Client.deregister_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.deregister_event_topic)
        """

    def describe_certificate(
        self, DirectoryId: str, CertificateId: str
    ) -> DescribeCertificateResultTypeDef:
        """
        [Client.describe_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_certificate)
        """

    def describe_conditional_forwarders(
        self, DirectoryId: str, RemoteDomainNames: List[str] = None
    ) -> DescribeConditionalForwardersResultTypeDef:
        """
        [Client.describe_conditional_forwarders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_conditional_forwarders)
        """

    def describe_directories(
        self, DirectoryIds: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> DescribeDirectoriesResultTypeDef:
        """
        [Client.describe_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_directories)
        """

    def describe_domain_controllers(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeDomainControllersResultTypeDef:
        """
        [Client.describe_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_domain_controllers)
        """

    def describe_event_topics(
        self, DirectoryId: str = None, TopicNames: List[str] = None
    ) -> DescribeEventTopicsResultTypeDef:
        """
        [Client.describe_event_topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_event_topics)
        """

    def describe_ldaps_settings(
        self,
        DirectoryId: str,
        Type: Literal["Client"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeLDAPSSettingsResultTypeDef:
        """
        [Client.describe_ldaps_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_ldaps_settings)
        """

    def describe_shared_directories(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeSharedDirectoriesResultTypeDef:
        """
        [Client.describe_shared_directories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_shared_directories)
        """

    def describe_snapshots(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeSnapshotsResultTypeDef:
        """
        [Client.describe_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_snapshots)
        """

    def describe_trusts(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeTrustsResultTypeDef:
        """
        [Client.describe_trusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.describe_trusts)
        """

    def disable_ldaps(self, DirectoryId: str, Type: Literal["Client"]) -> Dict[str, Any]:
        """
        [Client.disable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.disable_ldaps)
        """

    def disable_radius(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Client.disable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.disable_radius)
        """

    def disable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Client.disable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.disable_sso)
        """

    def enable_ldaps(self, DirectoryId: str, Type: Literal["Client"]) -> Dict[str, Any]:
        """
        [Client.enable_ldaps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.enable_ldaps)
        """

    def enable_radius(
        self, DirectoryId: str, RadiusSettings: "RadiusSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.enable_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.enable_radius)
        """

    def enable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Client.enable_sso documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.enable_sso)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.generate_presigned_url)
        """

    def get_directory_limits(self) -> GetDirectoryLimitsResultTypeDef:
        """
        [Client.get_directory_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.get_directory_limits)
        """

    def get_snapshot_limits(self, DirectoryId: str) -> GetSnapshotLimitsResultTypeDef:
        """
        [Client.get_snapshot_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.get_snapshot_limits)
        """

    def list_certificates(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListCertificatesResultTypeDef:
        """
        [Client.list_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.list_certificates)
        """

    def list_ip_routes(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListIpRoutesResultTypeDef:
        """
        [Client.list_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.list_ip_routes)
        """

    def list_log_subscriptions(
        self, DirectoryId: str = None, NextToken: str = None, Limit: int = None
    ) -> ListLogSubscriptionsResultTypeDef:
        """
        [Client.list_log_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.list_log_subscriptions)
        """

    def list_schema_extensions(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListSchemaExtensionsResultTypeDef:
        """
        [Client.list_schema_extensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.list_schema_extensions)
        """

    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None, Limit: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.list_tags_for_resource)
        """

    def register_certificate(
        self, DirectoryId: str, CertificateData: str
    ) -> RegisterCertificateResultTypeDef:
        """
        [Client.register_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.register_certificate)
        """

    def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Client.register_event_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.register_event_topic)
        """

    def reject_shared_directory(self, SharedDirectoryId: str) -> RejectSharedDirectoryResultTypeDef:
        """
        [Client.reject_shared_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.reject_shared_directory)
        """

    def remove_ip_routes(self, DirectoryId: str, CidrIps: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_ip_routes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.remove_ip_routes)
        """

    def remove_tags_from_resource(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.remove_tags_from_resource)
        """

    def reset_user_password(
        self, DirectoryId: str, UserName: str, NewPassword: str
    ) -> Dict[str, Any]:
        """
        [Client.reset_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.reset_user_password)
        """

    def restore_from_snapshot(self, SnapshotId: str) -> Dict[str, Any]:
        """
        [Client.restore_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.restore_from_snapshot)
        """

    def share_directory(
        self,
        DirectoryId: str,
        ShareTarget: ShareTargetTypeDef,
        ShareMethod: Literal["ORGANIZATIONS", "HANDSHAKE"],
        ShareNotes: str = None,
    ) -> ShareDirectoryResultTypeDef:
        """
        [Client.share_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.share_directory)
        """

    def start_schema_extension(
        self,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> StartSchemaExtensionResultTypeDef:
        """
        [Client.start_schema_extension documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.start_schema_extension)
        """

    def unshare_directory(
        self, DirectoryId: str, UnshareTarget: UnshareTargetTypeDef
    ) -> UnshareDirectoryResultTypeDef:
        """
        [Client.unshare_directory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.unshare_directory)
        """

    def update_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.update_conditional_forwarder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.update_conditional_forwarder)
        """

    def update_number_of_domain_controllers(
        self, DirectoryId: str, DesiredNumber: int
    ) -> Dict[str, Any]:
        """
        [Client.update_number_of_domain_controllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.update_number_of_domain_controllers)
        """

    def update_radius(
        self, DirectoryId: str, RadiusSettings: "RadiusSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.update_radius documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.update_radius)
        """

    def update_trust(
        self, TrustId: str, SelectiveAuth: Literal["Enabled", "Disabled"] = None
    ) -> UpdateTrustResultTypeDef:
        """
        [Client.update_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.update_trust)
        """

    def verify_trust(self, TrustId: str) -> VerifyTrustResultTypeDef:
        """
        [Client.verify_trust documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Client.verify_trust)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directories"]
    ) -> DescribeDirectoriesPaginator:
        """
        [Paginator.DescribeDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_domain_controllers"]
    ) -> DescribeDomainControllersPaginator:
        """
        [Paginator.DescribeDomainControllers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_shared_directories"]
    ) -> DescribeSharedDirectoriesPaginator:
        """
        [Paginator.DescribeSharedDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Paginator.DescribeSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_trusts"]) -> DescribeTrustsPaginator:
        """
        [Paginator.DescribeTrusts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_routes"]) -> ListIpRoutesPaginator:
        """
        [Paginator.ListIpRoutes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_log_subscriptions"]
    ) -> ListLogSubscriptionsPaginator:
        """
        [Paginator.ListLogSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_extensions"]
    ) -> ListSchemaExtensionsPaginator:
        """
        [Paginator.ListSchemaExtensions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
        """
