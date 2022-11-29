"""
Type annotations for appstream service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appstream import AppStreamClient

    client: AppStreamClient = boto3.client("appstream")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ApplicationAttributeType,
    AppVisibilityType,
    AuthenticationTypeType,
    FleetAttributeType,
    FleetTypeType,
    MessageActionType,
    PlatformTypeType,
    StackAttributeType,
    StreamViewType,
    VisibilityTypeType,
)
from .paginator import (
    DescribeDirectoryConfigsPaginator,
    DescribeFleetsPaginator,
    DescribeImageBuildersPaginator,
    DescribeImagesPaginator,
    DescribeSessionsPaginator,
    DescribeStacksPaginator,
    DescribeUsersPaginator,
    DescribeUserStackAssociationsPaginator,
    ListAssociatedFleetsPaginator,
    ListAssociatedStacksPaginator,
)
from .type_defs import (
    AccessEndpointTypeDef,
    ApplicationSettingsTypeDef,
    AssociateApplicationFleetResultTypeDef,
    BatchAssociateUserStackResultTypeDef,
    BatchDisassociateUserStackResultTypeDef,
    CertificateBasedAuthPropertiesTypeDef,
    ComputeCapacityTypeDef,
    CopyImageResponseTypeDef,
    CreateAppBlockResultTypeDef,
    CreateApplicationResultTypeDef,
    CreateDirectoryConfigResultTypeDef,
    CreateEntitlementResultTypeDef,
    CreateFleetResultTypeDef,
    CreateImageBuilderResultTypeDef,
    CreateImageBuilderStreamingURLResultTypeDef,
    CreateStackResultTypeDef,
    CreateStreamingURLResultTypeDef,
    CreateUpdatedImageResultTypeDef,
    CreateUsageReportSubscriptionResultTypeDef,
    DeleteImageBuilderResultTypeDef,
    DeleteImageResultTypeDef,
    DescribeAppBlocksResultTypeDef,
    DescribeApplicationFleetAssociationsResultTypeDef,
    DescribeApplicationsResultTypeDef,
    DescribeDirectoryConfigsResultTypeDef,
    DescribeEntitlementsResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeImageBuildersResultTypeDef,
    DescribeImagePermissionsResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeSessionsResultTypeDef,
    DescribeStacksResultTypeDef,
    DescribeUsageReportSubscriptionsResultTypeDef,
    DescribeUsersResultTypeDef,
    DescribeUserStackAssociationsResultTypeDef,
    DomainJoinInfoTypeDef,
    EntitlementAttributeTypeDef,
    ImagePermissionsTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksResultTypeDef,
    ListEntitledApplicationsResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    S3LocationTypeDef,
    ScriptDetailsTypeDef,
    ServiceAccountCredentialsTypeDef,
    StartImageBuilderResultTypeDef,
    StopImageBuilderResultTypeDef,
    StorageConnectorTypeDef,
    StreamingExperienceSettingsTypeDef,
    UpdateApplicationResultTypeDef,
    UpdateDirectoryConfigResultTypeDef,
    UpdateEntitlementResultTypeDef,
    UpdateFleetResultTypeDef,
    UpdateStackResultTypeDef,
    UserSettingTypeDef,
    UserStackAssociationTypeDef,
    VpcConfigTypeDef,
)
from .waiter import FleetStartedWaiter, FleetStoppedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppStreamClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    EntitlementAlreadyExistsException: Type[BotocoreClientError]
    EntitlementNotFoundException: Type[BotocoreClientError]
    IncompatibleImageException: Type[BotocoreClientError]
    InvalidAccountStatusException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    RequestLimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotAvailableException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class AppStreamClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppStreamClient exceptions.
        """
    def associate_application_fleet(
        self, *, FleetName: str, ApplicationArn: str
    ) -> AssociateApplicationFleetResultTypeDef:
        """
        Associates the specified application with the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.associate_application_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#associate_application_fleet)
        """
    def associate_application_to_entitlement(
        self, *, StackName: str, EntitlementName: str, ApplicationIdentifier: str
    ) -> Dict[str, Any]:
        """
        Associates an application to entitle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.associate_application_to_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#associate_application_to_entitlement)
        """
    def associate_fleet(self, *, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        Associates the specified fleet with the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.associate_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#associate_fleet)
        """
    def batch_associate_user_stack(
        self, *, UserStackAssociations: List["UserStackAssociationTypeDef"]
    ) -> BatchAssociateUserStackResultTypeDef:
        """
        Associates the specified users with the specified stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.batch_associate_user_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#batch_associate_user_stack)
        """
    def batch_disassociate_user_stack(
        self, *, UserStackAssociations: List["UserStackAssociationTypeDef"]
    ) -> BatchDisassociateUserStackResultTypeDef:
        """
        Disassociates the specified users from the specified stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.batch_disassociate_user_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#batch_disassociate_user_stack)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#close)
        """
    def copy_image(
        self,
        *,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: str = None
    ) -> CopyImageResponseTypeDef:
        """
        Copies the image within the same region or to a new region within the same AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.copy_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#copy_image)
        """
    def create_app_block(
        self,
        *,
        Name: str,
        SourceS3Location: "S3LocationTypeDef",
        SetupScriptDetails: "ScriptDetailsTypeDef",
        Description: str = None,
        DisplayName: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateAppBlockResultTypeDef:
        """
        Creates an app block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_app_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_app_block)
        """
    def create_application(
        self,
        *,
        Name: str,
        IconS3Location: "S3LocationTypeDef",
        LaunchPath: str,
        Platforms: List[PlatformTypeType],
        InstanceFamilies: List[str],
        AppBlockArn: str,
        DisplayName: str = None,
        Description: str = None,
        WorkingDirectory: str = None,
        LaunchParameters: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateApplicationResultTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_application)
        """
    def create_directory_config(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str],
        ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None,
        CertificateBasedAuthProperties: "CertificateBasedAuthPropertiesTypeDef" = None
    ) -> CreateDirectoryConfigResultTypeDef:
        """
        Creates a Directory Config object in AppStream 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_directory_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_directory_config)
        """
    def create_entitlement(
        self,
        *,
        Name: str,
        StackName: str,
        AppVisibility: AppVisibilityType,
        Attributes: List["EntitlementAttributeTypeDef"],
        Description: str = None
    ) -> CreateEntitlementResultTypeDef:
        """
        Creates a new entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_entitlement)
        """
    def create_fleet(
        self,
        *,
        Name: str,
        InstanceType: str,
        ImageName: str = None,
        ImageArn: str = None,
        FleetType: FleetTypeType = None,
        ComputeCapacity: "ComputeCapacityTypeDef" = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        Tags: Dict[str, str] = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        IamRoleArn: str = None,
        StreamView: StreamViewType = None,
        Platform: PlatformTypeType = None,
        MaxConcurrentSessions: int = None,
        UsbDeviceFilterStrings: List[str] = None,
        SessionScriptS3Location: "S3LocationTypeDef" = None
    ) -> CreateFleetResultTypeDef:
        """
        Creates a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_fleet)
        """
    def create_image_builder(
        self,
        *,
        Name: str,
        InstanceType: str,
        ImageName: str = None,
        ImageArn: str = None,
        Description: str = None,
        DisplayName: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        IamRoleArn: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        AppstreamAgentVersion: str = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None
    ) -> CreateImageBuilderResultTypeDef:
        """
        Creates an image builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_image_builder)
        """
    def create_image_builder_streaming_url(
        self, *, Name: str, Validity: int = None
    ) -> CreateImageBuilderStreamingURLResultTypeDef:
        """
        Creates a URL to start an image builder streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_image_builder_streaming_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_image_builder_streaming_url)
        """
    def create_stack(
        self,
        *,
        Name: str,
        Description: str = None,
        DisplayName: str = None,
        StorageConnectors: List["StorageConnectorTypeDef"] = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        UserSettings: List["UserSettingTypeDef"] = None,
        ApplicationSettings: "ApplicationSettingsTypeDef" = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
        EmbedHostDomains: List[str] = None,
        StreamingExperienceSettings: "StreamingExperienceSettingsTypeDef" = None
    ) -> CreateStackResultTypeDef:
        """
        Creates a stack to start streaming applications to users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_stack)
        """
    def create_streaming_url(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: str = None,
        Validity: int = None,
        SessionContext: str = None
    ) -> CreateStreamingURLResultTypeDef:
        """
        Creates a temporary URL to start an AppStream 2.0 streaming session for the
        specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_streaming_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_streaming_url)
        """
    def create_updated_image(
        self,
        *,
        existingImageName: str,
        newImageName: str,
        newImageDescription: str = None,
        newImageDisplayName: str = None,
        newImageTags: Dict[str, str] = None,
        dryRun: bool = None
    ) -> CreateUpdatedImageResultTypeDef:
        """
        Creates a new image with the latest Windows operating system updates, driver
        updates, and AppStream 2.0 agent software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_updated_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_updated_image)
        """
    def create_usage_report_subscription(self) -> CreateUsageReportSubscriptionResultTypeDef:
        """
        Creates a usage report subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_usage_report_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_usage_report_subscription)
        """
    def create_user(
        self,
        *,
        UserName: str,
        AuthenticationType: AuthenticationTypeType,
        MessageAction: MessageActionType = None,
        FirstName: str = None,
        LastName: str = None
    ) -> Dict[str, Any]:
        """
        Creates a new user in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#create_user)
        """
    def delete_app_block(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an app block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_app_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_app_block)
        """
    def delete_application(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_application)
        """
    def delete_directory_config(self, *, DirectoryName: str) -> Dict[str, Any]:
        """
        Deletes the specified Directory Config object from AppStream 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_directory_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_directory_config)
        """
    def delete_entitlement(self, *, Name: str, StackName: str) -> Dict[str, Any]:
        """
        Deletes the specified entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_entitlement)
        """
    def delete_fleet(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_fleet)
        """
    def delete_image(self, *, Name: str) -> DeleteImageResultTypeDef:
        """
        Deletes the specified image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_image)
        """
    def delete_image_builder(self, *, Name: str) -> DeleteImageBuilderResultTypeDef:
        """
        Deletes the specified image builder and releases the capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_image_builder)
        """
    def delete_image_permissions(self, *, Name: str, SharedAccountId: str) -> Dict[str, Any]:
        """
        Deletes permissions for the specified private image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_image_permissions)
        """
    def delete_stack(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_stack)
        """
    def delete_usage_report_subscription(self) -> Dict[str, Any]:
        """
        Disables usage report generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_usage_report_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_usage_report_subscription)
        """
    def delete_user(
        self, *, UserName: str, AuthenticationType: AuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        Deletes a user from the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#delete_user)
        """
    def describe_app_blocks(
        self, *, Arns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeAppBlocksResultTypeDef:
        """
        Retrieves a list that describes one or more app blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_app_blocks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_app_blocks)
        """
    def describe_application_fleet_associations(
        self,
        *,
        FleetName: str = None,
        ApplicationArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeApplicationFleetAssociationsResultTypeDef:
        """
        Retrieves a list that describes one or more application fleet associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_application_fleet_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_application_fleet_associations)
        """
    def describe_applications(
        self, *, Arns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeApplicationsResultTypeDef:
        """
        Retrieves a list that describes one or more applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_applications)
        """
    def describe_directory_configs(
        self, *, DirectoryNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDirectoryConfigsResultTypeDef:
        """
        Retrieves a list that describes one or more specified Directory Config objects
        for AppStream 2.0, if the names for these objects are provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_directory_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_directory_configs)
        """
    def describe_entitlements(
        self, *, StackName: str, Name: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeEntitlementsResultTypeDef:
        """
        Retrieves a list that describes one of more entitlements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_entitlements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_entitlements)
        """
    def describe_fleets(
        self, *, Names: List[str] = None, NextToken: str = None
    ) -> DescribeFleetsResultTypeDef:
        """
        Retrieves a list that describes one or more specified fleets, if the fleet names
        are provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_fleets)
        """
    def describe_image_builders(
        self, *, Names: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeImageBuildersResultTypeDef:
        """
        Retrieves a list that describes one or more specified image builders, if the
        image builder names are provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_image_builders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_image_builders)
        """
    def describe_image_permissions(
        self,
        *,
        Name: str,
        MaxResults: int = None,
        SharedAwsAccountIds: List[str] = None,
        NextToken: str = None
    ) -> DescribeImagePermissionsResultTypeDef:
        """
        Retrieves a list that describes the permissions for shared AWS account IDs on a
        private image that you own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_image_permissions)
        """
    def describe_images(
        self,
        *,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: VisibilityTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeImagesResultTypeDef:
        """
        Retrieves a list that describes one or more specified images, if the image names
        or image ARNs are provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_images)
        """
    def describe_sessions(
        self,
        *,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        NextToken: str = None,
        Limit: int = None,
        AuthenticationType: AuthenticationTypeType = None
    ) -> DescribeSessionsResultTypeDef:
        """
        Retrieves a list that describes the streaming sessions for a specified stack and
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_sessions)
        """
    def describe_stacks(
        self, *, Names: List[str] = None, NextToken: str = None
    ) -> DescribeStacksResultTypeDef:
        """
        Retrieves a list that describes one or more specified stacks, if the stack names
        are provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_stacks)
        """
    def describe_usage_report_subscriptions(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeUsageReportSubscriptionsResultTypeDef:
        """
        Retrieves a list that describes one or more usage report subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_usage_report_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_usage_report_subscriptions)
        """
    def describe_user_stack_associations(
        self,
        *,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: AuthenticationTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeUserStackAssociationsResultTypeDef:
        """
        Retrieves a list that describes the UserStackAssociation objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_user_stack_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_user_stack_associations)
        """
    def describe_users(
        self,
        *,
        AuthenticationType: AuthenticationTypeType,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeUsersResultTypeDef:
        """
        Retrieves a list that describes one or more specified users in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.describe_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#describe_users)
        """
    def disable_user(
        self, *, UserName: str, AuthenticationType: AuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        Disables the specified user in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.disable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#disable_user)
        """
    def disassociate_application_fleet(
        self, *, FleetName: str, ApplicationArn: str
    ) -> Dict[str, Any]:
        """
        Disassociates the specified application from the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.disassociate_application_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#disassociate_application_fleet)
        """
    def disassociate_application_from_entitlement(
        self, *, StackName: str, EntitlementName: str, ApplicationIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified application from the specified entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.disassociate_application_from_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#disassociate_application_from_entitlement)
        """
    def disassociate_fleet(self, *, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        Disassociates the specified fleet from the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.disassociate_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#disassociate_fleet)
        """
    def enable_user(
        self, *, UserName: str, AuthenticationType: AuthenticationTypeType
    ) -> Dict[str, Any]:
        """
        Enables a user in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.enable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#enable_user)
        """
    def expire_session(self, *, SessionId: str) -> Dict[str, Any]:
        """
        Immediately stops the specified streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.expire_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#expire_session)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#generate_presigned_url)
        """
    def list_associated_fleets(
        self, *, StackName: str, NextToken: str = None
    ) -> ListAssociatedFleetsResultTypeDef:
        """
        Retrieves the name of the fleet that is associated with the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.list_associated_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_associated_fleets)
        """
    def list_associated_stacks(
        self, *, FleetName: str, NextToken: str = None
    ) -> ListAssociatedStacksResultTypeDef:
        """
        Retrieves the name of the stack with which the specified fleet is associated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.list_associated_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_associated_stacks)
        """
    def list_entitled_applications(
        self, *, StackName: str, EntitlementName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListEntitledApplicationsResultTypeDef:
        """
        Retrieves a list of entitled applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.list_entitled_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_entitled_applications)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of all tags for the specified AppStream 2.0 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#list_tags_for_resource)
        """
    def start_fleet(self, *, Name: str) -> Dict[str, Any]:
        """
        Starts the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.start_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#start_fleet)
        """
    def start_image_builder(
        self, *, Name: str, AppstreamAgentVersion: str = None
    ) -> StartImageBuilderResultTypeDef:
        """
        Starts the specified image builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.start_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#start_image_builder)
        """
    def stop_fleet(self, *, Name: str) -> Dict[str, Any]:
        """
        Stops the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.stop_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#stop_fleet)
        """
    def stop_image_builder(self, *, Name: str) -> StopImageBuilderResultTypeDef:
        """
        Stops the specified image builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.stop_image_builder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#stop_image_builder)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified AppStream 2.0 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Disassociates one or more specified tags from the specified AppStream 2.0
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        Name: str,
        DisplayName: str = None,
        Description: str = None,
        IconS3Location: "S3LocationTypeDef" = None,
        LaunchPath: str = None,
        WorkingDirectory: str = None,
        LaunchParameters: str = None,
        AppBlockArn: str = None,
        AttributesToDelete: List[ApplicationAttributeType] = None
    ) -> UpdateApplicationResultTypeDef:
        """
        Updates the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_application)
        """
    def update_directory_config(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str] = None,
        ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None,
        CertificateBasedAuthProperties: "CertificateBasedAuthPropertiesTypeDef" = None
    ) -> UpdateDirectoryConfigResultTypeDef:
        """
        Updates the specified Directory Config object in AppStream 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.update_directory_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_directory_config)
        """
    def update_entitlement(
        self,
        *,
        Name: str,
        StackName: str,
        Description: str = None,
        AppVisibility: AppVisibilityType = None,
        Attributes: List["EntitlementAttributeTypeDef"] = None
    ) -> UpdateEntitlementResultTypeDef:
        """
        Updates the specified entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.update_entitlement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_entitlement)
        """
    def update_fleet(
        self,
        *,
        ImageName: str = None,
        ImageArn: str = None,
        Name: str = None,
        InstanceType: str = None,
        ComputeCapacity: "ComputeCapacityTypeDef" = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        DeleteVpcConfig: bool = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        AttributesToDelete: List[FleetAttributeType] = None,
        IamRoleArn: str = None,
        StreamView: StreamViewType = None,
        Platform: PlatformTypeType = None,
        MaxConcurrentSessions: int = None,
        UsbDeviceFilterStrings: List[str] = None,
        SessionScriptS3Location: "S3LocationTypeDef" = None
    ) -> UpdateFleetResultTypeDef:
        """
        Updates the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.update_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_fleet)
        """
    def update_image_permissions(
        self, *, Name: str, SharedAccountId: str, ImagePermissions: "ImagePermissionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Adds or updates permissions for the specified private image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.update_image_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_image_permissions)
        """
    def update_stack(
        self,
        *,
        Name: str,
        DisplayName: str = None,
        Description: str = None,
        StorageConnectors: List["StorageConnectorTypeDef"] = None,
        DeleteStorageConnectors: bool = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        AttributesToDelete: List[StackAttributeType] = None,
        UserSettings: List["UserSettingTypeDef"] = None,
        ApplicationSettings: "ApplicationSettingsTypeDef" = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
        EmbedHostDomains: List[str] = None,
        StreamingExperienceSettings: "StreamingExperienceSettingsTypeDef" = None
    ) -> UpdateStackResultTypeDef:
        """
        Updates the specified fields for the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Client.update_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/client.html#update_stack)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directory_configs"]
    ) -> DescribeDirectoryConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describedirectoryconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describefleetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_builders"]
    ) -> DescribeImageBuildersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagebuilderspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeimagespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describesessionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_stacks"]) -> DescribeStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describestackspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_user_stack_associations"]
    ) -> DescribeUserStackAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserstackassociationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#describeuserspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_fleets"]
    ) -> ListAssociatedFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedfleetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_stacks"]
    ) -> ListAssociatedStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/paginators.html#listassociatedstackspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["fleet_started"]) -> FleetStartedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Waiter.FleetStarted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstartedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["fleet_stopped"]) -> FleetStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/appstream.html#AppStream.Waiter.FleetStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/waiters.html#fleetstoppedwaiter)
        """
