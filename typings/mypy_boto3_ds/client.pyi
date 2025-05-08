"""
Type annotations for ds service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ds.client import DirectoryServiceClient

    session = Session()
    client: DirectoryServiceClient = session.client("ds")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    AcceptSharedDirectoryRequestTypeDef,
    AcceptSharedDirectoryResultTypeDef,
    AddIpRoutesRequestTypeDef,
    AddRegionRequestTypeDef,
    AddTagsToResourceRequestTypeDef,
    CancelSchemaExtensionRequestTypeDef,
    ConnectDirectoryRequestTypeDef,
    ConnectDirectoryResultTypeDef,
    CreateAliasRequestTypeDef,
    CreateAliasResultTypeDef,
    CreateComputerRequestTypeDef,
    CreateComputerResultTypeDef,
    CreateConditionalForwarderRequestTypeDef,
    CreateDirectoryRequestTypeDef,
    CreateDirectoryResultTypeDef,
    CreateLogSubscriptionRequestTypeDef,
    CreateMicrosoftADRequestTypeDef,
    CreateMicrosoftADResultTypeDef,
    CreateSnapshotRequestTypeDef,
    CreateSnapshotResultTypeDef,
    CreateTrustRequestTypeDef,
    CreateTrustResultTypeDef,
    DeleteConditionalForwarderRequestTypeDef,
    DeleteDirectoryRequestTypeDef,
    DeleteDirectoryResultTypeDef,
    DeleteLogSubscriptionRequestTypeDef,
    DeleteSnapshotRequestTypeDef,
    DeleteSnapshotResultTypeDef,
    DeleteTrustRequestTypeDef,
    DeleteTrustResultTypeDef,
    DeregisterCertificateRequestTypeDef,
    DeregisterEventTopicRequestTypeDef,
    DescribeCertificateRequestTypeDef,
    DescribeCertificateResultTypeDef,
    DescribeClientAuthenticationSettingsRequestTypeDef,
    DescribeClientAuthenticationSettingsResultTypeDef,
    DescribeConditionalForwardersRequestTypeDef,
    DescribeConditionalForwardersResultTypeDef,
    DescribeDirectoriesRequestTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDirectoryDataAccessRequestTypeDef,
    DescribeDirectoryDataAccessResultTypeDef,
    DescribeDomainControllersRequestTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeEventTopicsRequestTypeDef,
    DescribeEventTopicsResultTypeDef,
    DescribeLDAPSSettingsRequestTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeRegionsRequestTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeSettingsRequestTypeDef,
    DescribeSettingsResultTypeDef,
    DescribeSharedDirectoriesRequestTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsRequestTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsRequestTypeDef,
    DescribeTrustsResultTypeDef,
    DescribeUpdateDirectoryRequestTypeDef,
    DescribeUpdateDirectoryResultTypeDef,
    DisableClientAuthenticationRequestTypeDef,
    DisableDirectoryDataAccessRequestTypeDef,
    DisableLDAPSRequestTypeDef,
    DisableRadiusRequestTypeDef,
    DisableSsoRequestTypeDef,
    EnableClientAuthenticationRequestTypeDef,
    EnableDirectoryDataAccessRequestTypeDef,
    EnableLDAPSRequestTypeDef,
    EnableRadiusRequestTypeDef,
    EnableSsoRequestTypeDef,
    GetDirectoryLimitsResultTypeDef,
    GetSnapshotLimitsRequestTypeDef,
    GetSnapshotLimitsResultTypeDef,
    ListCertificatesRequestTypeDef,
    ListCertificatesResultTypeDef,
    ListIpRoutesRequestTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsRequestTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsRequestTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    RegisterCertificateRequestTypeDef,
    RegisterCertificateResultTypeDef,
    RegisterEventTopicRequestTypeDef,
    RejectSharedDirectoryRequestTypeDef,
    RejectSharedDirectoryResultTypeDef,
    RemoveIpRoutesRequestTypeDef,
    RemoveRegionRequestTypeDef,
    RemoveTagsFromResourceRequestTypeDef,
    ResetUserPasswordRequestTypeDef,
    RestoreFromSnapshotRequestTypeDef,
    ShareDirectoryRequestTypeDef,
    ShareDirectoryResultTypeDef,
    StartSchemaExtensionRequestTypeDef,
    StartSchemaExtensionResultTypeDef,
    UnshareDirectoryRequestTypeDef,
    UnshareDirectoryResultTypeDef,
    UpdateConditionalForwarderRequestTypeDef,
    UpdateDirectorySetupRequestTypeDef,
    UpdateNumberOfDomainControllersRequestTypeDef,
    UpdateRadiusRequestTypeDef,
    UpdateSettingsRequestTypeDef,
    UpdateSettingsResultTypeDef,
    UpdateTrustRequestTypeDef,
    UpdateTrustResultTypeDef,
    VerifyTrustRequestTypeDef,
    VerifyTrustResultTypeDef,
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

__all__ = ("DirectoryServiceClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DirectoryServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds.html#DirectoryService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#generate_presigned_url)
        """

    def accept_shared_directory(
        self, **kwargs: Unpack[AcceptSharedDirectoryRequestTypeDef]
    ) -> AcceptSharedDirectoryResultTypeDef:
        """
        Accepts a directory sharing request that was sent from the directory owner
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/accept_shared_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#accept_shared_directory)
        """

    def add_ip_routes(self, **kwargs: Unpack[AddIpRoutesRequestTypeDef]) -> Dict[str, Any]:
        """
        If the DNS server for your self-managed domain uses a publicly addressable IP
        address, you must add a CIDR address block to correctly route traffic to and
        from your Microsoft AD on Amazon Web Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/add_ip_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#add_ip_routes)
        """

    def add_region(self, **kwargs: Unpack[AddRegionRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds two domain controllers in the specified Region for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/add_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#add_region)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#add_tags_to_resource)
        """

    def cancel_schema_extension(
        self, **kwargs: Unpack[CancelSchemaExtensionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels an in-progress schema extension to a Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/cancel_schema_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#cancel_schema_extension)
        """

    def connect_directory(
        self, **kwargs: Unpack[ConnectDirectoryRequestTypeDef]
    ) -> ConnectDirectoryResultTypeDef:
        """
        Creates an AD Connector to connect to a self-managed directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/connect_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#connect_directory)
        """

    def create_alias(self, **kwargs: Unpack[CreateAliasRequestTypeDef]) -> CreateAliasResultTypeDef:
        """
        Creates an alias for a directory and assigns the alias to the directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_alias.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_alias)
        """

    def create_computer(
        self, **kwargs: Unpack[CreateComputerRequestTypeDef]
    ) -> CreateComputerResultTypeDef:
        """
        Creates an Active Directory computer object in the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_computer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_computer)
        """

    def create_conditional_forwarder(
        self, **kwargs: Unpack[CreateConditionalForwarderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a conditional forwarder associated with your Amazon Web Services
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_conditional_forwarder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_conditional_forwarder)
        """

    def create_directory(
        self, **kwargs: Unpack[CreateDirectoryRequestTypeDef]
    ) -> CreateDirectoryResultTypeDef:
        """
        Creates a Simple AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_directory)
        """

    def create_log_subscription(
        self, **kwargs: Unpack[CreateLogSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a subscription to forward real-time Directory Service domain controller
        security logs to the specified Amazon CloudWatch log group in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_log_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_log_subscription)
        """

    def create_microsoft_ad(
        self, **kwargs: Unpack[CreateMicrosoftADRequestTypeDef]
    ) -> CreateMicrosoftADResultTypeDef:
        """
        Creates a Microsoft AD directory in the Amazon Web Services Cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_microsoft_ad.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_microsoft_ad)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestTypeDef]
    ) -> CreateSnapshotResultTypeDef:
        """
        Creates a snapshot of a Simple AD or Microsoft AD directory in the Amazon Web
        Services cloud.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_snapshot)
        """

    def create_trust(self, **kwargs: Unpack[CreateTrustRequestTypeDef]) -> CreateTrustResultTypeDef:
        """
        Directory Service for Microsoft Active Directory allows you to configure trust
        relationships.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/create_trust.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#create_trust)
        """

    def delete_conditional_forwarder(
        self, **kwargs: Unpack[DeleteConditionalForwarderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a conditional forwarder that has been set up for your Amazon Web
        Services directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/delete_conditional_forwarder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#delete_conditional_forwarder)
        """

    def delete_directory(
        self, **kwargs: Unpack[DeleteDirectoryRequestTypeDef]
    ) -> DeleteDirectoryResultTypeDef:
        """
        Deletes an Directory Service directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/delete_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#delete_directory)
        """

    def delete_log_subscription(
        self, **kwargs: Unpack[DeleteLogSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified log subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/delete_log_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#delete_log_subscription)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotRequestTypeDef]
    ) -> DeleteSnapshotResultTypeDef:
        """
        Deletes a directory snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/delete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#delete_snapshot)
        """

    def delete_trust(self, **kwargs: Unpack[DeleteTrustRequestTypeDef]) -> DeleteTrustResultTypeDef:
        """
        Deletes an existing trust relationship between your Managed Microsoft AD
        directory and an external domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/delete_trust.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#delete_trust)
        """

    def deregister_certificate(
        self, **kwargs: Unpack[DeregisterCertificateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes from the system the certificate that was registered for secure LDAP or
        client certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/deregister_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#deregister_certificate)
        """

    def deregister_event_topic(
        self, **kwargs: Unpack[DeregisterEventTopicRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified directory as a publisher to the specified Amazon SNS
        topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/deregister_event_topic.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#deregister_event_topic)
        """

    def describe_certificate(
        self, **kwargs: Unpack[DescribeCertificateRequestTypeDef]
    ) -> DescribeCertificateResultTypeDef:
        """
        Displays information about the certificate registered for secure LDAP or client
        certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_certificate)
        """

    def describe_client_authentication_settings(
        self, **kwargs: Unpack[DescribeClientAuthenticationSettingsRequestTypeDef]
    ) -> DescribeClientAuthenticationSettingsResultTypeDef:
        """
        Retrieves information about the type of client authentication for the specified
        directory, if the type is specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_client_authentication_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_client_authentication_settings)
        """

    def describe_conditional_forwarders(
        self, **kwargs: Unpack[DescribeConditionalForwardersRequestTypeDef]
    ) -> DescribeConditionalForwardersResultTypeDef:
        """
        Obtains information about the conditional forwarders for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_conditional_forwarders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_conditional_forwarders)
        """

    def describe_directories(
        self, **kwargs: Unpack[DescribeDirectoriesRequestTypeDef]
    ) -> DescribeDirectoriesResultTypeDef:
        """
        Obtains information about the directories that belong to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_directories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_directories)
        """

    def describe_directory_data_access(
        self, **kwargs: Unpack[DescribeDirectoryDataAccessRequestTypeDef]
    ) -> DescribeDirectoryDataAccessResultTypeDef:
        """
        Obtains status of directory data access enablement through the Directory
        Service Data API for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_directory_data_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_directory_data_access)
        """

    def describe_domain_controllers(
        self, **kwargs: Unpack[DescribeDomainControllersRequestTypeDef]
    ) -> DescribeDomainControllersResultTypeDef:
        """
        Provides information about any domain controllers in your directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_domain_controllers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_domain_controllers)
        """

    def describe_event_topics(
        self, **kwargs: Unpack[DescribeEventTopicsRequestTypeDef]
    ) -> DescribeEventTopicsResultTypeDef:
        """
        Obtains information about which Amazon SNS topics receive status messages from
        the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_event_topics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_event_topics)
        """

    def describe_ldaps_settings(
        self, **kwargs: Unpack[DescribeLDAPSSettingsRequestTypeDef]
    ) -> DescribeLDAPSSettingsResultTypeDef:
        """
        Describes the status of LDAP security for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_ldaps_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_ldaps_settings)
        """

    def describe_regions(
        self, **kwargs: Unpack[DescribeRegionsRequestTypeDef]
    ) -> DescribeRegionsResultTypeDef:
        """
        Provides information about the Regions that are configured for multi-Region
        replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_regions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_regions)
        """

    def describe_settings(
        self, **kwargs: Unpack[DescribeSettingsRequestTypeDef]
    ) -> DescribeSettingsResultTypeDef:
        """
        Retrieves information about the configurable settings for the specified
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_settings)
        """

    def describe_shared_directories(
        self, **kwargs: Unpack[DescribeSharedDirectoriesRequestTypeDef]
    ) -> DescribeSharedDirectoriesResultTypeDef:
        """
        Returns the shared directories in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_shared_directories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_shared_directories)
        """

    def describe_snapshots(
        self, **kwargs: Unpack[DescribeSnapshotsRequestTypeDef]
    ) -> DescribeSnapshotsResultTypeDef:
        """
        Obtains information about the directory snapshots that belong to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_snapshots)
        """

    def describe_trusts(
        self, **kwargs: Unpack[DescribeTrustsRequestTypeDef]
    ) -> DescribeTrustsResultTypeDef:
        """
        Obtains information about the trust relationships for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_trusts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_trusts)
        """

    def describe_update_directory(
        self, **kwargs: Unpack[DescribeUpdateDirectoryRequestTypeDef]
    ) -> DescribeUpdateDirectoryResultTypeDef:
        """
        Describes the updates of a directory for a particular update type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/describe_update_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#describe_update_directory)
        """

    def disable_client_authentication(
        self, **kwargs: Unpack[DisableClientAuthenticationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disables alternative client authentication methods for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/disable_client_authentication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#disable_client_authentication)
        """

    def disable_directory_data_access(
        self, **kwargs: Unpack[DisableDirectoryDataAccessRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deactivates access to directory data via the Directory Service Data API for the
        specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/disable_directory_data_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#disable_directory_data_access)
        """

    def disable_ldaps(self, **kwargs: Unpack[DisableLDAPSRequestTypeDef]) -> Dict[str, Any]:
        """
        Deactivates LDAP secure calls for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/disable_ldaps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#disable_ldaps)
        """

    def disable_radius(self, **kwargs: Unpack[DisableRadiusRequestTypeDef]) -> Dict[str, Any]:
        """
        Disables multi-factor authentication (MFA) with the Remote Authentication Dial
        In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/disable_radius.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#disable_radius)
        """

    def disable_sso(self, **kwargs: Unpack[DisableSsoRequestTypeDef]) -> Dict[str, Any]:
        """
        Disables single-sign on for a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/disable_sso.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#disable_sso)
        """

    def enable_client_authentication(
        self, **kwargs: Unpack[EnableClientAuthenticationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables alternative client authentication methods for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/enable_client_authentication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#enable_client_authentication)
        """

    def enable_directory_data_access(
        self, **kwargs: Unpack[EnableDirectoryDataAccessRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables access to directory data via the Directory Service Data API for the
        specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/enable_directory_data_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#enable_directory_data_access)
        """

    def enable_ldaps(self, **kwargs: Unpack[EnableLDAPSRequestTypeDef]) -> Dict[str, Any]:
        """
        Activates the switch for the specific directory to always use LDAP secure calls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/enable_ldaps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#enable_ldaps)
        """

    def enable_radius(self, **kwargs: Unpack[EnableRadiusRequestTypeDef]) -> Dict[str, Any]:
        """
        Enables multi-factor authentication (MFA) with the Remote Authentication Dial
        In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/enable_radius.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#enable_radius)
        """

    def enable_sso(self, **kwargs: Unpack[EnableSsoRequestTypeDef]) -> Dict[str, Any]:
        """
        Enables single sign-on for a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/enable_sso.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#enable_sso)
        """

    def get_directory_limits(self) -> GetDirectoryLimitsResultTypeDef:
        """
        Obtains directory limit information for the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_directory_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_directory_limits)
        """

    def get_snapshot_limits(
        self, **kwargs: Unpack[GetSnapshotLimitsRequestTypeDef]
    ) -> GetSnapshotLimitsResultTypeDef:
        """
        Obtains the manual snapshot limits for a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_snapshot_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_snapshot_limits)
        """

    def list_certificates(
        self, **kwargs: Unpack[ListCertificatesRequestTypeDef]
    ) -> ListCertificatesResultTypeDef:
        """
        For the specified directory, lists all the certificates registered for a secure
        LDAP or client certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/list_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#list_certificates)
        """

    def list_ip_routes(
        self, **kwargs: Unpack[ListIpRoutesRequestTypeDef]
    ) -> ListIpRoutesResultTypeDef:
        """
        Lists the address blocks that you have added to a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/list_ip_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#list_ip_routes)
        """

    def list_log_subscriptions(
        self, **kwargs: Unpack[ListLogSubscriptionsRequestTypeDef]
    ) -> ListLogSubscriptionsResultTypeDef:
        """
        Lists the active log subscriptions for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/list_log_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#list_log_subscriptions)
        """

    def list_schema_extensions(
        self, **kwargs: Unpack[ListSchemaExtensionsRequestTypeDef]
    ) -> ListSchemaExtensionsResultTypeDef:
        """
        Lists all schema extensions applied to a Microsoft AD Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/list_schema_extensions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#list_schema_extensions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Lists all tags on a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#list_tags_for_resource)
        """

    def register_certificate(
        self, **kwargs: Unpack[RegisterCertificateRequestTypeDef]
    ) -> RegisterCertificateResultTypeDef:
        """
        Registers a certificate for a secure LDAP or client certificate authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/register_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#register_certificate)
        """

    def register_event_topic(
        self, **kwargs: Unpack[RegisterEventTopicRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates a directory with an Amazon SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/register_event_topic.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#register_event_topic)
        """

    def reject_shared_directory(
        self, **kwargs: Unpack[RejectSharedDirectoryRequestTypeDef]
    ) -> RejectSharedDirectoryResultTypeDef:
        """
        Rejects a directory sharing request that was sent from the directory owner
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/reject_shared_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#reject_shared_directory)
        """

    def remove_ip_routes(self, **kwargs: Unpack[RemoveIpRoutesRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes IP address blocks from a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/remove_ip_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#remove_ip_routes)
        """

    def remove_region(self, **kwargs: Unpack[RemoveRegionRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops all replication and removes the domain controllers from the specified
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/remove_region.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#remove_region)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes tags from a directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#remove_tags_from_resource)
        """

    def reset_user_password(
        self, **kwargs: Unpack[ResetUserPasswordRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets the password for any user in your Managed Microsoft AD or Simple AD
        directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/reset_user_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#reset_user_password)
        """

    def restore_from_snapshot(
        self, **kwargs: Unpack[RestoreFromSnapshotRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Restores a directory using an existing directory snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/restore_from_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#restore_from_snapshot)
        """

    def share_directory(
        self, **kwargs: Unpack[ShareDirectoryRequestTypeDef]
    ) -> ShareDirectoryResultTypeDef:
        """
        Shares a specified directory (<code>DirectoryId</code>) in your Amazon Web
        Services account (directory owner) with another Amazon Web Services account
        (directory consumer).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/share_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#share_directory)
        """

    def start_schema_extension(
        self, **kwargs: Unpack[StartSchemaExtensionRequestTypeDef]
    ) -> StartSchemaExtensionResultTypeDef:
        """
        Applies a schema extension to a Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/start_schema_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#start_schema_extension)
        """

    def unshare_directory(
        self, **kwargs: Unpack[UnshareDirectoryRequestTypeDef]
    ) -> UnshareDirectoryResultTypeDef:
        """
        Stops the directory sharing between the directory owner and consumer accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/unshare_directory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#unshare_directory)
        """

    def update_conditional_forwarder(
        self, **kwargs: Unpack[UpdateConditionalForwarderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a conditional forwarder that has been set up for your Amazon Web
        Services directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/update_conditional_forwarder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#update_conditional_forwarder)
        """

    def update_directory_setup(
        self, **kwargs: Unpack[UpdateDirectorySetupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the directory for a particular update type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/update_directory_setup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#update_directory_setup)
        """

    def update_number_of_domain_controllers(
        self, **kwargs: Unpack[UpdateNumberOfDomainControllersRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds or removes domain controllers to or from the directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/update_number_of_domain_controllers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#update_number_of_domain_controllers)
        """

    def update_radius(self, **kwargs: Unpack[UpdateRadiusRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the Remote Authentication Dial In User Service (RADIUS) server
        information for an AD Connector or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/update_radius.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#update_radius)
        """

    def update_settings(
        self, **kwargs: Unpack[UpdateSettingsRequestTypeDef]
    ) -> UpdateSettingsResultTypeDef:
        """
        Updates the configurable settings for the specified directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/update_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#update_settings)
        """

    def update_trust(self, **kwargs: Unpack[UpdateTrustRequestTypeDef]) -> UpdateTrustResultTypeDef:
        """
        Updates the trust that has been set up between your Managed Microsoft AD
        directory and an self-managed Active Directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/update_trust.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#update_trust)
        """

    def verify_trust(self, **kwargs: Unpack[VerifyTrustRequestTypeDef]) -> VerifyTrustResultTypeDef:
        """
        Directory Service for Microsoft Active Directory allows you to configure and
        verify trust relationships.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/verify_trust.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#verify_trust)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_client_authentication_settings"]
    ) -> DescribeClientAuthenticationSettingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_directories"]
    ) -> DescribeDirectoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_domain_controllers"]
    ) -> DescribeDomainControllersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ldaps_settings"]
    ) -> DescribeLDAPSSettingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_regions"]
    ) -> DescribeRegionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_shared_directories"]
    ) -> DescribeSharedDirectoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_trusts"]
    ) -> DescribeTrustsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_update_directory"]
    ) -> DescribeUpdateDirectoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ip_routes"]
    ) -> ListIpRoutesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_log_subscriptions"]
    ) -> ListLogSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schema_extensions"]
    ) -> ListSchemaExtensionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ds/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds/client/#get_paginator)
        """
