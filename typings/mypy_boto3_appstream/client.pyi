# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for appstream service client

Usage::

    ```python
    import boto3
    from mypy_boto3_appstream import AppStreamClient

    client: AppStreamClient = boto3.client("appstream")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_appstream.paginator import (
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
from mypy_boto3_appstream.type_defs import (
    AccessEndpointTypeDef,
    ApplicationSettingsTypeDef,
    BatchAssociateUserStackResultTypeDef,
    BatchDisassociateUserStackResultTypeDef,
    ComputeCapacityTypeDef,
    CopyImageResponseTypeDef,
    CreateDirectoryConfigResultTypeDef,
    CreateFleetResultTypeDef,
    CreateImageBuilderResultTypeDef,
    CreateImageBuilderStreamingURLResultTypeDef,
    CreateStackResultTypeDef,
    CreateStreamingURLResultTypeDef,
    CreateUsageReportSubscriptionResultTypeDef,
    DeleteImageBuilderResultTypeDef,
    DeleteImageResultTypeDef,
    DescribeDirectoryConfigsResultTypeDef,
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
    ImagePermissionsTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    ServiceAccountCredentialsTypeDef,
    StartImageBuilderResultTypeDef,
    StopImageBuilderResultTypeDef,
    StorageConnectorTypeDef,
    UpdateDirectoryConfigResultTypeDef,
    UpdateFleetResultTypeDef,
    UpdateStackResultTypeDef,
    UserSettingTypeDef,
    UserStackAssociationTypeDef,
    VpcConfigTypeDef,
)
from mypy_boto3_appstream.waiter import FleetStartedWaiter, FleetStoppedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AppStreamClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    IncompatibleImageException: Type[Boto3ClientError]
    InvalidAccountStatusException: Type[Boto3ClientError]
    InvalidParameterCombinationException: Type[Boto3ClientError]
    InvalidRoleException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    OperationNotPermittedException: Type[Boto3ClientError]
    RequestLimitExceededException: Type[Boto3ClientError]
    ResourceAlreadyExistsException: Type[Boto3ClientError]
    ResourceInUseException: Type[Boto3ClientError]
    ResourceNotAvailableException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class AppStreamClient:
    """
    [AppStream.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client)
    """

    exceptions: Exceptions

    def associate_fleet(self, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        [Client.associate_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.associate_fleet)
        """

    def batch_associate_user_stack(
        self, UserStackAssociations: List["UserStackAssociationTypeDef"]
    ) -> BatchAssociateUserStackResultTypeDef:
        """
        [Client.batch_associate_user_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.batch_associate_user_stack)
        """

    def batch_disassociate_user_stack(
        self, UserStackAssociations: List["UserStackAssociationTypeDef"]
    ) -> BatchDisassociateUserStackResultTypeDef:
        """
        [Client.batch_disassociate_user_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.batch_disassociate_user_stack)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.can_paginate)
        """

    def copy_image(
        self,
        SourceImageName: str,
        DestinationImageName: str,
        DestinationRegion: str,
        DestinationImageDescription: str = None,
    ) -> CopyImageResponseTypeDef:
        """
        [Client.copy_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.copy_image)
        """

    def create_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str],
        ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None,
    ) -> CreateDirectoryConfigResultTypeDef:
        """
        [Client.create_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_directory_config)
        """

    def create_fleet(
        self,
        Name: str,
        InstanceType: str,
        ComputeCapacity: ComputeCapacityTypeDef,
        ImageName: str = None,
        ImageArn: str = None,
        FleetType: Literal["ALWAYS_ON", "ON_DEMAND"] = None,
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
        StreamView: Literal["APP", "DESKTOP"] = None,
    ) -> CreateFleetResultTypeDef:
        """
        [Client.create_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_fleet)
        """

    def create_image_builder(
        self,
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
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
    ) -> CreateImageBuilderResultTypeDef:
        """
        [Client.create_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_image_builder)
        """

    def create_image_builder_streaming_url(
        self, Name: str, Validity: int = None
    ) -> CreateImageBuilderStreamingURLResultTypeDef:
        """
        [Client.create_image_builder_streaming_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_image_builder_streaming_url)
        """

    def create_stack(
        self,
        Name: str,
        Description: str = None,
        DisplayName: str = None,
        StorageConnectors: List["StorageConnectorTypeDef"] = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        UserSettings: List["UserSettingTypeDef"] = None,
        ApplicationSettings: ApplicationSettingsTypeDef = None,
        Tags: Dict[str, str] = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
        EmbedHostDomains: List[str] = None,
    ) -> CreateStackResultTypeDef:
        """
        [Client.create_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_stack)
        """

    def create_streaming_url(
        self,
        StackName: str,
        FleetName: str,
        UserId: str,
        ApplicationId: str = None,
        Validity: int = None,
        SessionContext: str = None,
    ) -> CreateStreamingURLResultTypeDef:
        """
        [Client.create_streaming_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_streaming_url)
        """

    def create_usage_report_subscription(self) -> CreateUsageReportSubscriptionResultTypeDef:
        """
        [Client.create_usage_report_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_usage_report_subscription)
        """

    def create_user(
        self,
        UserName: str,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        MessageAction: Literal["SUPPRESS", "RESEND"] = None,
        FirstName: str = None,
        LastName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.create_user)
        """

    def delete_directory_config(self, DirectoryName: str) -> Dict[str, Any]:
        """
        [Client.delete_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_directory_config)
        """

    def delete_fleet(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_fleet)
        """

    def delete_image(self, Name: str) -> DeleteImageResultTypeDef:
        """
        [Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_image)
        """

    def delete_image_builder(self, Name: str) -> DeleteImageBuilderResultTypeDef:
        """
        [Client.delete_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_image_builder)
        """

    def delete_image_permissions(self, Name: str, SharedAccountId: str) -> Dict[str, Any]:
        """
        [Client.delete_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_image_permissions)
        """

    def delete_stack(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_stack)
        """

    def delete_usage_report_subscription(self) -> Dict[str, Any]:
        """
        [Client.delete_usage_report_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_usage_report_subscription)
        """

    def delete_user(
        self, UserName: str, AuthenticationType: Literal["API", "SAML", "USERPOOL"]
    ) -> Dict[str, Any]:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.delete_user)
        """

    def describe_directory_configs(
        self, DirectoryNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDirectoryConfigsResultTypeDef:
        """
        [Client.describe_directory_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_directory_configs)
        """

    def describe_fleets(
        self, Names: List[str] = None, NextToken: str = None
    ) -> DescribeFleetsResultTypeDef:
        """
        [Client.describe_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_fleets)
        """

    def describe_image_builders(
        self, Names: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeImageBuildersResultTypeDef:
        """
        [Client.describe_image_builders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_image_builders)
        """

    def describe_image_permissions(
        self,
        Name: str,
        MaxResults: int = None,
        SharedAwsAccountIds: List[str] = None,
        NextToken: str = None,
    ) -> DescribeImagePermissionsResultTypeDef:
        """
        [Client.describe_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_image_permissions)
        """

    def describe_images(
        self,
        Names: List[str] = None,
        Arns: List[str] = None,
        Type: Literal["PUBLIC", "PRIVATE", "SHARED"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeImagesResultTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_images)
        """

    def describe_sessions(
        self,
        StackName: str,
        FleetName: str,
        UserId: str = None,
        NextToken: str = None,
        Limit: int = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
    ) -> DescribeSessionsResultTypeDef:
        """
        [Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_sessions)
        """

    def describe_stacks(
        self, Names: List[str] = None, NextToken: str = None
    ) -> DescribeStacksResultTypeDef:
        """
        [Client.describe_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_stacks)
        """

    def describe_usage_report_subscriptions(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DescribeUsageReportSubscriptionsResultTypeDef:
        """
        [Client.describe_usage_report_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_usage_report_subscriptions)
        """

    def describe_user_stack_associations(
        self,
        StackName: str = None,
        UserName: str = None,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeUserStackAssociationsResultTypeDef:
        """
        [Client.describe_user_stack_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_user_stack_associations)
        """

    def describe_users(
        self,
        AuthenticationType: Literal["API", "SAML", "USERPOOL"],
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeUsersResultTypeDef:
        """
        [Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.describe_users)
        """

    def disable_user(
        self, UserName: str, AuthenticationType: Literal["API", "SAML", "USERPOOL"]
    ) -> Dict[str, Any]:
        """
        [Client.disable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.disable_user)
        """

    def disassociate_fleet(self, FleetName: str, StackName: str) -> Dict[str, Any]:
        """
        [Client.disassociate_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.disassociate_fleet)
        """

    def enable_user(
        self, UserName: str, AuthenticationType: Literal["API", "SAML", "USERPOOL"]
    ) -> Dict[str, Any]:
        """
        [Client.enable_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.enable_user)
        """

    def expire_session(self, SessionId: str) -> Dict[str, Any]:
        """
        [Client.expire_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.expire_session)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.generate_presigned_url)
        """

    def list_associated_fleets(
        self, StackName: str, NextToken: str = None
    ) -> ListAssociatedFleetsResultTypeDef:
        """
        [Client.list_associated_fleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.list_associated_fleets)
        """

    def list_associated_stacks(
        self, FleetName: str, NextToken: str = None
    ) -> ListAssociatedStacksResultTypeDef:
        """
        [Client.list_associated_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.list_associated_stacks)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.list_tags_for_resource)
        """

    def start_fleet(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.start_fleet)
        """

    def start_image_builder(
        self, Name: str, AppstreamAgentVersion: str = None
    ) -> StartImageBuilderResultTypeDef:
        """
        [Client.start_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.start_image_builder)
        """

    def stop_fleet(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.stop_fleet)
        """

    def stop_image_builder(self, Name: str) -> StopImageBuilderResultTypeDef:
        """
        [Client.stop_image_builder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.stop_image_builder)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.untag_resource)
        """

    def update_directory_config(
        self,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str] = None,
        ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef" = None,
    ) -> UpdateDirectoryConfigResultTypeDef:
        """
        [Client.update_directory_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.update_directory_config)
        """

    def update_fleet(
        self,
        ImageName: str = None,
        ImageArn: str = None,
        Name: str = None,
        InstanceType: str = None,
        ComputeCapacity: ComputeCapacityTypeDef = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        MaxUserDurationInSeconds: int = None,
        DisconnectTimeoutInSeconds: int = None,
        DeleteVpcConfig: bool = None,
        Description: str = None,
        DisplayName: str = None,
        EnableDefaultInternetAccess: bool = None,
        DomainJoinInfo: "DomainJoinInfoTypeDef" = None,
        IdleDisconnectTimeoutInSeconds: int = None,
        AttributesToDelete: List[
            Literal[
                "VPC_CONFIGURATION",
                "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
                "DOMAIN_JOIN_INFO",
                "IAM_ROLE_ARN",
            ]
        ] = None,
        IamRoleArn: str = None,
        StreamView: Literal["APP", "DESKTOP"] = None,
    ) -> UpdateFleetResultTypeDef:
        """
        [Client.update_fleet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.update_fleet)
        """

    def update_image_permissions(
        self, Name: str, SharedAccountId: str, ImagePermissions: "ImagePermissionsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.update_image_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.update_image_permissions)
        """

    def update_stack(
        self,
        Name: str,
        DisplayName: str = None,
        Description: str = None,
        StorageConnectors: List["StorageConnectorTypeDef"] = None,
        DeleteStorageConnectors: bool = None,
        RedirectURL: str = None,
        FeedbackURL: str = None,
        AttributesToDelete: List[
            Literal[
                "STORAGE_CONNECTORS",
                "STORAGE_CONNECTOR_HOMEFOLDERS",
                "STORAGE_CONNECTOR_GOOGLE_DRIVE",
                "STORAGE_CONNECTOR_ONE_DRIVE",
                "REDIRECT_URL",
                "FEEDBACK_URL",
                "THEME_NAME",
                "USER_SETTINGS",
                "EMBED_HOST_DOMAINS",
                "IAM_ROLE_ARN",
                "ACCESS_ENDPOINTS",
            ]
        ] = None,
        UserSettings: List["UserSettingTypeDef"] = None,
        ApplicationSettings: ApplicationSettingsTypeDef = None,
        AccessEndpoints: List["AccessEndpointTypeDef"] = None,
        EmbedHostDomains: List[str] = None,
    ) -> UpdateStackResultTypeDef:
        """
        [Client.update_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Client.update_stack)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directory_configs"]
    ) -> DescribeDirectoryConfigsPaginator:
        """
        [Paginator.DescribeDirectoryConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeDirectoryConfigs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Paginator.DescribeFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeFleets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_builders"]
    ) -> DescribeImageBuildersPaginator:
        """
        [Paginator.DescribeImageBuilders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeImageBuilders)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeSessions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_stacks"]) -> DescribeStacksPaginator:
        """
        [Paginator.DescribeStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeStacks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_user_stack_associations"]
    ) -> DescribeUserStackAssociationsPaginator:
        """
        [Paginator.DescribeUserStackAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeUserStackAssociations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.DescribeUsers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_fleets"]
    ) -> ListAssociatedFleetsPaginator:
        """
        [Paginator.ListAssociatedFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.ListAssociatedFleets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_stacks"]
    ) -> ListAssociatedStacksPaginator:
        """
        [Paginator.ListAssociatedStacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Paginator.ListAssociatedStacks)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_started"]) -> FleetStartedWaiter:
        """
        [Waiter.FleetStarted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Waiter.FleetStarted)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_stopped"]) -> FleetStoppedWaiter:
        """
        [Waiter.FleetStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/appstream.html#AppStream.Waiter.FleetStopped)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
