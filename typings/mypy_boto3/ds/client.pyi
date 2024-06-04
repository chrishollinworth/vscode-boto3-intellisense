"""
Type annotations for ds service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ds import DirectoryServiceClient

    client: DirectoryServiceClient = boto3.client("ds")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CertificateTypeType,
    ClientAuthenticationTypeType,
    DirectoryConfigurationStatusType,
    DirectoryEditionType,
    DirectorySizeType,
    SelectiveAuthType,
    ShareMethodType,
    TrustDirectionType,
    TrustTypeType,
)
from .paginator import (
    DescribeClientAuthenticationSettingsPaginator,
    DescribeDirectoriesPaginator,
    DescribeDomainControllersPaginator,
    DescribeLDAPSSettingsPaginator,
    DescribeRegionsPaginator,
    DescribeSharedDirectoriesPaginator,
    DescribeSnapshotsPaginator,
    DescribeTrustsPaginator,
    DescribeUpdateDirectoryPaginator,
    ListCertificatesPaginator,
    ListIpRoutesPaginator,
    ListLogSubscriptionsPaginator,
    ListSchemaExtensionsPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AcceptSharedDirectoryResultTypeDef,
    AttributeTypeDef,
    ClientCertAuthSettingsTypeDef,
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
    DescribeClientAuthenticationSettingsResultTypeDef,
    DescribeConditionalForwardersResultTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeEventTopicsResultTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeSettingsResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    DescribeUpdateDirectoryResultTypeDef,
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
    OSUpdateSettingsTypeDef,
    RadiusSettingsTypeDef,
    RegisterCertificateResultTypeDef,
    RejectSharedDirectoryResultTypeDef,
    SettingTypeDef,
    ShareDirectoryResultTypeDef,
    ShareTargetTypeDef,
    StartSchemaExtensionResultTypeDef,
    TagTypeDef,
    UnshareDirectoryResultTypeDef,
    UnshareTargetTypeDef,
    UpdateSettingsResultTypeDef,
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
    DirectoryAlreadyInRegionException: Type[BotocoreClientError]
    DirectoryAlreadySharedException: Type[BotocoreClientError]
    DirectoryDoesNotExistException: Type[BotocoreClientError]
    DirectoryInDesiredStateException: Type[BotocoreClientError]
    DirectoryLimitExceededException: Type[BotocoreClientError]
    DirectoryNotSharedException: Type[BotocoreClientError]
    DirectoryUnavailableException: Type[BotocoreClientError]
    DomainControllerLimitExceededException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityDoesNotExistException: Type[BotocoreClientError]
    IncompatibleSettingsException: Type[BotocoreClientError]
    InsufficientPermissionsException: Type[BotocoreClientError]
    InvalidCertificateException: Type[BotocoreClientError]
    InvalidClientAuthStatusException: Type[BotocoreClientError]
    InvalidLDAPSStatusException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    IpRouteLimitExceededException: Type[BotocoreClientError]
    NoAvailableCertificateException: Type[BotocoreClientError]
    OrganizationsException: Type[BotocoreClientError]
    RegionLimitExceededException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ShareLimitExceededException: Type[BotocoreClientError]
    SnapshotLimitExceededException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedSettingsException: Type[BotocoreClientError]
    UserDoesNotExistException: Type[BotocoreClientError]

class DirectoryServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DirectoryServiceClient exceptions.
        """

    def accept_shared_directory(
        self, *, SharedDirectoryId: str
    ) -> AcceptSharedDirectoryResultTypeDef:
        """
        Accepts a directory sharing request that was sent from the directory owner
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.accept_shared_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#accept_shared_directory)
        """

    def add_ip_routes(
        self,
        *,
        DirectoryId: str,
        IpRoutes: List["IpRouteTypeDef"],
        UpdateSecurityGroupForDirectoryControllers: bool = None
    ) -> Dict[str, Any]:
        """
        If the DNS server for your self-managed domain uses a publicly addressable IP
        address, you must add a CIDR address block to correctly route traffic to and
        from your Microsoft AD on Amazon Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.add_ip_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#add_ip_routes)
        """

    def add_region(
        self, *, DirectoryId: str, RegionName: str, VPCSettings: "DirectoryVpcSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        Adds two domain controllers in the specified Region for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.add_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#add_region)
        """

    def add_tags_to_resource(self, *, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#can_paginate)
        """

    def cancel_schema_extension(
        self, *, DirectoryId: str, SchemaExtensionId: str
    ) -> Dict[str, Any]:
        """
        Cancels an in-progress schema extension to a Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.cancel_schema_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#cancel_schema_extension)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#close)
        """

    def connect_directory(
        self,
        *,
        Name: str,
        Password: str,
        Size: DirectorySizeType,
        ConnectSettings: "DirectoryConnectSettingsTypeDef",
        ShortName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ConnectDirectoryResultTypeDef:
        """
        Creates an AD Connector to connect to a self-managed directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.connect_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#connect_directory)
        """

    def create_alias(self, *, DirectoryId: str, Alias: str) -> CreateAliasResultTypeDef:
        """
        Creates an alias for a directory and assigns the alias to the directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_alias)
        """

    def create_computer(
        self,
        *,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str = None,
        ComputerAttributes: List["AttributeTypeDef"] = None
    ) -> CreateComputerResultTypeDef:
        """
        Creates an Active Directory computer object in the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_computer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_computer)
        """

    def create_conditional_forwarder(
        self, *, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        Creates a conditional forwarder associated with your Amazon Web Services
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_conditional_forwarder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_conditional_forwarder)
        """

    def create_directory(
        self,
        *,
        Name: str,
        Password: str,
        Size: DirectorySizeType,
        ShortName: str = None,
        Description: str = None,
        VpcSettings: "DirectoryVpcSettingsTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDirectoryResultTypeDef:
        """
        Creates a Simple AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_directory)
        """

    def create_log_subscription(self, *, DirectoryId: str, LogGroupName: str) -> Dict[str, Any]:
        """
        Creates a subscription to forward real-time Directory Service domain controller
        security logs to the specified Amazon CloudWatch log group in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_log_subscription)
        """

    def create_microsoft_ad(
        self,
        *,
        Name: str,
        Password: str,
        VpcSettings: "DirectoryVpcSettingsTypeDef",
        ShortName: str = None,
        Description: str = None,
        Edition: DirectoryEditionType = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateMicrosoftADResultTypeDef:
        """
        Creates a Microsoft AD directory in the Amazon Web Services Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_microsoft_ad)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_microsoft_ad)
        """

    def create_snapshot(self, *, DirectoryId: str, Name: str = None) -> CreateSnapshotResultTypeDef:
        """
        Creates a snapshot of a Simple AD or Microsoft AD directory in the Amazon Web
        Services cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_snapshot)
        """

    def create_trust(
        self,
        *,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: TrustDirectionType,
        TrustType: TrustTypeType = None,
        ConditionalForwarderIpAddrs: List[str] = None,
        SelectiveAuth: SelectiveAuthType = None
    ) -> CreateTrustResultTypeDef:
        """
        Directory Service for Microsoft Active Directory allows you to configure trust
        relationships.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.create_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create_trust)
        """

    def delete_conditional_forwarder(
        self, *, DirectoryId: str, RemoteDomainName: str
    ) -> Dict[str, Any]:
        """
        Deletes a conditional forwarder that has been set up for your Amazon Web
        Services directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.delete_conditional_forwarder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete_conditional_forwarder)
        """

    def delete_directory(self, *, DirectoryId: str) -> DeleteDirectoryResultTypeDef:
        """
        Deletes an Directory Service directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.delete_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete_directory)
        """

    def delete_log_subscription(self, *, DirectoryId: str) -> Dict[str, Any]:
        """
        Deletes the specified log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.delete_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete_log_subscription)
        """

    def delete_snapshot(self, *, SnapshotId: str) -> DeleteSnapshotResultTypeDef:
        """
        Deletes a directory snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete_snapshot)
        """

    def delete_trust(
        self, *, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None
    ) -> DeleteTrustResultTypeDef:
        """
        Deletes an existing trust relationship between your Managed Microsoft AD
        directory and an external domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.delete_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete_trust)
        """

    def deregister_certificate(self, *, DirectoryId: str, CertificateId: str) -> Dict[str, Any]:
        """
        Deletes from the system the certificate that was registered for secure LDAP or
        client certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.deregister_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#deregister_certificate)
        """

    def deregister_event_topic(self, *, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        Removes the specified directory as a publisher to the specified Amazon SNS
        topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.deregister_event_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#deregister_event_topic)
        """

    def describe_certificate(
        self, *, DirectoryId: str, CertificateId: str
    ) -> DescribeCertificateResultTypeDef:
        """
        Displays information about the certificate registered for secure LDAP or client
        certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_certificate)
        """

    def describe_client_authentication_settings(
        self,
        *,
        DirectoryId: str,
        Type: ClientAuthenticationTypeType = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeClientAuthenticationSettingsResultTypeDef:
        """
        Retrieves information about the type of client authentication for the specified
        directory, if the type is specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_client_authentication_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_client_authentication_settings)
        """

    def describe_conditional_forwarders(
        self, *, DirectoryId: str, RemoteDomainNames: List[str] = None
    ) -> DescribeConditionalForwardersResultTypeDef:
        """
        Obtains information about the conditional forwarders for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_conditional_forwarders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_conditional_forwarders)
        """

    def describe_directories(
        self, *, DirectoryIds: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> DescribeDirectoriesResultTypeDef:
        """
        Obtains information about the directories that belong to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_directories)
        """

    def describe_domain_controllers(
        self,
        *,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeDomainControllersResultTypeDef:
        """
        Provides information about any domain controllers in your directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_domain_controllers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_domain_controllers)
        """

    def describe_event_topics(
        self, *, DirectoryId: str = None, TopicNames: List[str] = None
    ) -> DescribeEventTopicsResultTypeDef:
        """
        Obtains information about which Amazon SNS topics receive status messages from
        the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_event_topics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_event_topics)
        """

    def describe_ldaps_settings(
        self,
        *,
        DirectoryId: str,
        Type: Literal["Client"] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeLDAPSSettingsResultTypeDef:
        """
        Describes the status of LDAP security for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_ldaps_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_ldaps_settings)
        """

    def describe_regions(
        self, *, DirectoryId: str, RegionName: str = None, NextToken: str = None
    ) -> DescribeRegionsResultTypeDef:
        """
        Provides information about the Regions that are configured for multi-Region
        replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_regions)
        """

    def describe_settings(
        self,
        *,
        DirectoryId: str,
        Status: DirectoryConfigurationStatusType = None,
        NextToken: str = None
    ) -> DescribeSettingsResultTypeDef:
        """
        Retrieves information about the configurable settings for the specified
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_settings)
        """

    def describe_shared_directories(
        self,
        *,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeSharedDirectoriesResultTypeDef:
        """
        Returns the shared directories in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_shared_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_shared_directories)
        """

    def describe_snapshots(
        self,
        *,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeSnapshotsResultTypeDef:
        """
        Obtains information about the directory snapshots that belong to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_snapshots)
        """

    def describe_trusts(
        self,
        *,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeTrustsResultTypeDef:
        """
        Obtains information about the trust relationships for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_trusts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_trusts)
        """

    def describe_update_directory(
        self,
        *,
        DirectoryId: str,
        UpdateType: Literal["OS"],
        RegionName: str = None,
        NextToken: str = None
    ) -> DescribeUpdateDirectoryResultTypeDef:
        """
        Describes the updates of a directory for a particular update type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.describe_update_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe_update_directory)
        """

    def disable_client_authentication(
        self, *, DirectoryId: str, Type: ClientAuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        Disables alternative client authentication methods for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.disable_client_authentication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable_client_authentication)
        """

    def disable_ldaps(self, *, DirectoryId: str, Type: Literal["Client"]) -> Dict[str, Any]:
        """
        Deactivates LDAP secure calls for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.disable_ldaps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable_ldaps)
        """

    def disable_radius(self, *, DirectoryId: str) -> Dict[str, Any]:
        """
        Disables multi-factor authentication (MFA) with the Remote Authentication Dial
        In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.disable_radius)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable_radius)
        """

    def disable_sso(
        self, *, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        Disables single-sign on for a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.disable_sso)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable_sso)
        """

    def enable_client_authentication(
        self, *, DirectoryId: str, Type: ClientAuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        Enables alternative client authentication methods for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.enable_client_authentication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable_client_authentication)
        """

    def enable_ldaps(self, *, DirectoryId: str, Type: Literal["Client"]) -> Dict[str, Any]:
        """
        Activates the switch for the specific directory to always use LDAP secure calls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.enable_ldaps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable_ldaps)
        """

    def enable_radius(
        self, *, DirectoryId: str, RadiusSettings: "RadiusSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        Enables multi-factor authentication (MFA) with the Remote Authentication Dial In
        User Service (RADIUS) server for an AD Connector or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.enable_radius)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable_radius)
        """

    def enable_sso(
        self, *, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        Enables single sign-on for a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.enable_sso)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable_sso)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#generate_presigned_url)
        """

    def get_directory_limits(self) -> GetDirectoryLimitsResultTypeDef:
        """
        Obtains directory limit information for the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.get_directory_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#get_directory_limits)
        """

    def get_snapshot_limits(self, *, DirectoryId: str) -> GetSnapshotLimitsResultTypeDef:
        """
        Obtains the manual snapshot limits for a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.get_snapshot_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#get_snapshot_limits)
        """

    def list_certificates(
        self, *, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListCertificatesResultTypeDef:
        """
        For the specified directory, lists all the certificates registered for a secure
        LDAP or client certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.list_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list_certificates)
        """

    def list_ip_routes(
        self, *, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListIpRoutesResultTypeDef:
        """
        Lists the address blocks that you have added to a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.list_ip_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list_ip_routes)
        """

    def list_log_subscriptions(
        self, *, DirectoryId: str = None, NextToken: str = None, Limit: int = None
    ) -> ListLogSubscriptionsResultTypeDef:
        """
        Lists the active log subscriptions for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.list_log_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list_log_subscriptions)
        """

    def list_schema_extensions(
        self, *, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListSchemaExtensionsResultTypeDef:
        """
        Lists all schema extensions applied to a Microsoft AD Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.list_schema_extensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list_schema_extensions)
        """

    def list_tags_for_resource(
        self, *, ResourceId: str, NextToken: str = None, Limit: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        Lists all tags on a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list_tags_for_resource)
        """

    def register_certificate(
        self,
        *,
        DirectoryId: str,
        CertificateData: str,
        Type: CertificateTypeType = None,
        ClientCertAuthSettings: "ClientCertAuthSettingsTypeDef" = None
    ) -> RegisterCertificateResultTypeDef:
        """
        Registers a certificate for a secure LDAP or client certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.register_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#register_certificate)
        """

    def register_event_topic(self, *, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        Associates a directory with an Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.register_event_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#register_event_topic)
        """

    def reject_shared_directory(
        self, *, SharedDirectoryId: str
    ) -> RejectSharedDirectoryResultTypeDef:
        """
        Rejects a directory sharing request that was sent from the directory owner
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.reject_shared_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#reject_shared_directory)
        """

    def remove_ip_routes(self, *, DirectoryId: str, CidrIps: List[str]) -> Dict[str, Any]:
        """
        Removes IP address blocks from a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.remove_ip_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#remove_ip_routes)
        """

    def remove_region(self, *, DirectoryId: str) -> Dict[str, Any]:
        """
        Stops all replication and removes the domain controllers from the specified
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.remove_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#remove_region)
        """

    def remove_tags_from_resource(self, *, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#remove_tags_from_resource)
        """

    def reset_user_password(
        self, *, DirectoryId: str, UserName: str, NewPassword: str
    ) -> Dict[str, Any]:
        """
        Resets the password for any user in your Managed Microsoft AD or Simple AD
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.reset_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#reset_user_password)
        """

    def restore_from_snapshot(self, *, SnapshotId: str) -> Dict[str, Any]:
        """
        Restores a directory using an existing directory snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.restore_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#restore_from_snapshot)
        """

    def share_directory(
        self,
        *,
        DirectoryId: str,
        ShareTarget: "ShareTargetTypeDef",
        ShareMethod: ShareMethodType,
        ShareNotes: str = None
    ) -> ShareDirectoryResultTypeDef:
        """
        Shares a specified directory ( `DirectoryId`) in your Amazon Web Services
        account (directory owner) with another Amazon Web Services account (directory
        consumer).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.share_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#share_directory)
        """

    def start_schema_extension(
        self,
        *,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str
    ) -> StartSchemaExtensionResultTypeDef:
        """
        Applies a schema extension to a Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.start_schema_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#start_schema_extension)
        """

    def unshare_directory(
        self, *, DirectoryId: str, UnshareTarget: "UnshareTargetTypeDef"
    ) -> UnshareDirectoryResultTypeDef:
        """
        Stops the directory sharing between the directory owner and consumer accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.unshare_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#unshare_directory)
        """

    def update_conditional_forwarder(
        self, *, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        Updates a conditional forwarder that has been set up for your Amazon Web
        Services directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.update_conditional_forwarder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update_conditional_forwarder)
        """

    def update_directory_setup(
        self,
        *,
        DirectoryId: str,
        UpdateType: Literal["OS"],
        OSUpdateSettings: "OSUpdateSettingsTypeDef" = None,
        CreateSnapshotBeforeUpdate: bool = None
    ) -> Dict[str, Any]:
        """
        Updates the directory for a particular update type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.update_directory_setup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update_directory_setup)
        """

    def update_number_of_domain_controllers(
        self, *, DirectoryId: str, DesiredNumber: int
    ) -> Dict[str, Any]:
        """
        Adds or removes domain controllers to or from the directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.update_number_of_domain_controllers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update_number_of_domain_controllers)
        """

    def update_radius(
        self, *, DirectoryId: str, RadiusSettings: "RadiusSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the Remote Authentication Dial In User Service (RADIUS) server
        information for an AD Connector or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.update_radius)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update_radius)
        """

    def update_settings(
        self, *, DirectoryId: str, Settings: List["SettingTypeDef"]
    ) -> UpdateSettingsResultTypeDef:
        """
        Updates the configurable settings for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.update_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update_settings)
        """

    def update_trust(
        self, *, TrustId: str, SelectiveAuth: SelectiveAuthType = None
    ) -> UpdateTrustResultTypeDef:
        """
        Updates the trust that has been set up between your Managed Microsoft AD
        directory and an self-managed Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.update_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update_trust)
        """

    def verify_trust(self, *, TrustId: str) -> VerifyTrustResultTypeDef:
        """
        Directory Service for Microsoft Active Directory allows you to configure and
        verify trust relationships.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Client.verify_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#verify_trust)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_authentication_settings"]
    ) -> DescribeClientAuthenticationSettingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeClientAuthenticationSettings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeclientauthenticationsettingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directories"]
    ) -> DescribeDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedirectoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_domain_controllers"]
    ) -> DescribeDomainControllersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedomaincontrollerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ldaps_settings"]
    ) -> DescribeLDAPSSettingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeLDAPSSettings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeldapssettingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_regions"]
    ) -> DescribeRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeRegions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeregionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_shared_directories"]
    ) -> DescribeSharedDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeshareddirectoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describesnapshotspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_trusts"]) -> DescribeTrustsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describetrustspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_update_directory"]
    ) -> DescribeUpdateDirectoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.DescribeUpdateDirectory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeupdatedirectorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.ListCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listcertificatespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_routes"]) -> ListIpRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listiproutespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_log_subscriptions"]
    ) -> ListLogSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listlogsubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_extensions"]
    ) -> ListSchemaExtensionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listschemaextensionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listtagsforresourcepaginator)
        """
