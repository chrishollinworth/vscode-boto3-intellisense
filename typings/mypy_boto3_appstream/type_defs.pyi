"""
Type annotations for appstream service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef

    data: AccessEndpointTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionType,
    AppBlockBuilderAttributeType,
    AppBlockBuilderStateType,
    AppBlockStateType,
    ApplicationAttributeType,
    AppVisibilityType,
    AuthenticationTypeType,
    CertificateBasedAuthStatusType,
    DynamicAppProvidersEnabledType,
    FleetAttributeType,
    FleetErrorCodeType,
    FleetStateType,
    FleetTypeType,
    ImageBuilderStateChangeReasonCodeType,
    ImageBuilderStateType,
    ImageSharedWithOthersType,
    ImageStateChangeReasonCodeType,
    ImageStateType,
    LatestAppstreamAgentVersionType,
    MessageActionType,
    PackagingTypeType,
    PermissionType,
    PlatformTypeType,
    PreferredProtocolType,
    SessionConnectionStateType,
    SessionStateType,
    StackAttributeType,
    StackErrorCodeType,
    StorageConnectorTypeType,
    StreamViewType,
    ThemeStateType,
    ThemeStylingType,
    UsageReportExecutionErrorCodeType,
    UserStackAssociationErrorCodeType,
    VisibilityTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessEndpointTypeDef",
    "AppBlockBuilderAppBlockAssociationTypeDef",
    "AppBlockBuilderStateChangeReasonTypeDef",
    "AppBlockBuilderTypeDef",
    "AppBlockTypeDef",
    "ApplicationFleetAssociationTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "ApplicationSettingsTypeDef",
    "ApplicationTypeDef",
    "AssociateAppBlockBuilderAppBlockRequestTypeDef",
    "AssociateAppBlockBuilderAppBlockResultTypeDef",
    "AssociateApplicationFleetRequestTypeDef",
    "AssociateApplicationFleetResultTypeDef",
    "AssociateApplicationToEntitlementRequestTypeDef",
    "AssociateFleetRequestTypeDef",
    "BatchAssociateUserStackRequestTypeDef",
    "BatchAssociateUserStackResultTypeDef",
    "BatchDisassociateUserStackRequestTypeDef",
    "BatchDisassociateUserStackResultTypeDef",
    "CertificateBasedAuthPropertiesTypeDef",
    "ComputeCapacityStatusTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageRequestTypeDef",
    "CopyImageResponseTypeDef",
    "CreateAppBlockBuilderRequestTypeDef",
    "CreateAppBlockBuilderResultTypeDef",
    "CreateAppBlockBuilderStreamingURLRequestTypeDef",
    "CreateAppBlockBuilderStreamingURLResultTypeDef",
    "CreateAppBlockRequestTypeDef",
    "CreateAppBlockResultTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateApplicationResultTypeDef",
    "CreateDirectoryConfigRequestTypeDef",
    "CreateDirectoryConfigResultTypeDef",
    "CreateEntitlementRequestTypeDef",
    "CreateEntitlementResultTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResultTypeDef",
    "CreateImageBuilderRequestTypeDef",
    "CreateImageBuilderResultTypeDef",
    "CreateImageBuilderStreamingURLRequestTypeDef",
    "CreateImageBuilderStreamingURLResultTypeDef",
    "CreateStackRequestTypeDef",
    "CreateStackResultTypeDef",
    "CreateStreamingURLRequestTypeDef",
    "CreateStreamingURLResultTypeDef",
    "CreateThemeForStackRequestTypeDef",
    "CreateThemeForStackResultTypeDef",
    "CreateUpdatedImageRequestTypeDef",
    "CreateUpdatedImageResultTypeDef",
    "CreateUsageReportSubscriptionResultTypeDef",
    "CreateUserRequestTypeDef",
    "DeleteAppBlockBuilderRequestTypeDef",
    "DeleteAppBlockRequestTypeDef",
    "DeleteApplicationRequestTypeDef",
    "DeleteDirectoryConfigRequestTypeDef",
    "DeleteEntitlementRequestTypeDef",
    "DeleteFleetRequestTypeDef",
    "DeleteImageBuilderRequestTypeDef",
    "DeleteImageBuilderResultTypeDef",
    "DeleteImagePermissionsRequestTypeDef",
    "DeleteImageRequestTypeDef",
    "DeleteImageResultTypeDef",
    "DeleteStackRequestTypeDef",
    "DeleteThemeForStackRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeAppBlockBuilderAppBlockAssociationsRequestTypeDef",
    "DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef",
    "DescribeAppBlockBuildersRequestTypeDef",
    "DescribeAppBlockBuildersResultTypeDef",
    "DescribeAppBlocksRequestTypeDef",
    "DescribeAppBlocksResultTypeDef",
    "DescribeApplicationFleetAssociationsRequestTypeDef",
    "DescribeApplicationFleetAssociationsResultTypeDef",
    "DescribeApplicationsRequestTypeDef",
    "DescribeApplicationsResultTypeDef",
    "DescribeDirectoryConfigsRequestPaginateTypeDef",
    "DescribeDirectoryConfigsRequestTypeDef",
    "DescribeDirectoryConfigsResultTypeDef",
    "DescribeEntitlementsRequestTypeDef",
    "DescribeEntitlementsResultTypeDef",
    "DescribeFleetsRequestPaginateTypeDef",
    "DescribeFleetsRequestTypeDef",
    "DescribeFleetsRequestWaitExtraTypeDef",
    "DescribeFleetsRequestWaitTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeImageBuildersRequestPaginateTypeDef",
    "DescribeImageBuildersRequestTypeDef",
    "DescribeImageBuildersResultTypeDef",
    "DescribeImagePermissionsRequestTypeDef",
    "DescribeImagePermissionsResultTypeDef",
    "DescribeImagesRequestPaginateTypeDef",
    "DescribeImagesRequestTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeSessionsRequestPaginateTypeDef",
    "DescribeSessionsRequestTypeDef",
    "DescribeSessionsResultTypeDef",
    "DescribeStacksRequestPaginateTypeDef",
    "DescribeStacksRequestTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeThemeForStackRequestTypeDef",
    "DescribeThemeForStackResultTypeDef",
    "DescribeUsageReportSubscriptionsRequestTypeDef",
    "DescribeUsageReportSubscriptionsResultTypeDef",
    "DescribeUserStackAssociationsRequestPaginateTypeDef",
    "DescribeUserStackAssociationsRequestTypeDef",
    "DescribeUserStackAssociationsResultTypeDef",
    "DescribeUsersRequestPaginateTypeDef",
    "DescribeUsersRequestTypeDef",
    "DescribeUsersResultTypeDef",
    "DirectoryConfigTypeDef",
    "DisableUserRequestTypeDef",
    "DisassociateAppBlockBuilderAppBlockRequestTypeDef",
    "DisassociateApplicationFleetRequestTypeDef",
    "DisassociateApplicationFromEntitlementRequestTypeDef",
    "DisassociateFleetRequestTypeDef",
    "DomainJoinInfoTypeDef",
    "EnableUserRequestTypeDef",
    "EntitledApplicationTypeDef",
    "EntitlementAttributeTypeDef",
    "EntitlementTypeDef",
    "ErrorDetailsTypeDef",
    "ExpireSessionRequestTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "ListAssociatedFleetsRequestPaginateTypeDef",
    "ListAssociatedFleetsRequestTypeDef",
    "ListAssociatedFleetsResultTypeDef",
    "ListAssociatedStacksRequestPaginateTypeDef",
    "ListAssociatedStacksRequestTypeDef",
    "ListAssociatedStacksResultTypeDef",
    "ListEntitledApplicationsRequestTypeDef",
    "ListEntitledApplicationsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceErrorTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "ScriptDetailsTypeDef",
    "ServiceAccountCredentialsTypeDef",
    "SessionTypeDef",
    "SharedImagePermissionsTypeDef",
    "StackErrorTypeDef",
    "StackTypeDef",
    "StartAppBlockBuilderRequestTypeDef",
    "StartAppBlockBuilderResultTypeDef",
    "StartFleetRequestTypeDef",
    "StartImageBuilderRequestTypeDef",
    "StartImageBuilderResultTypeDef",
    "StopAppBlockBuilderRequestTypeDef",
    "StopAppBlockBuilderResultTypeDef",
    "StopFleetRequestTypeDef",
    "StopImageBuilderRequestTypeDef",
    "StopImageBuilderResultTypeDef",
    "StorageConnectorOutputTypeDef",
    "StorageConnectorTypeDef",
    "StorageConnectorUnionTypeDef",
    "StreamingExperienceSettingsTypeDef",
    "TagResourceRequestTypeDef",
    "ThemeFooterLinkTypeDef",
    "ThemeTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppBlockBuilderRequestTypeDef",
    "UpdateAppBlockBuilderResultTypeDef",
    "UpdateApplicationRequestTypeDef",
    "UpdateApplicationResultTypeDef",
    "UpdateDirectoryConfigRequestTypeDef",
    "UpdateDirectoryConfigResultTypeDef",
    "UpdateEntitlementRequestTypeDef",
    "UpdateEntitlementResultTypeDef",
    "UpdateFleetRequestTypeDef",
    "UpdateFleetResultTypeDef",
    "UpdateImagePermissionsRequestTypeDef",
    "UpdateStackRequestTypeDef",
    "UpdateStackResultTypeDef",
    "UpdateThemeForStackRequestTypeDef",
    "UpdateThemeForStackResultTypeDef",
    "UsageReportSubscriptionTypeDef",
    "UserSettingTypeDef",
    "UserStackAssociationErrorTypeDef",
    "UserStackAssociationTypeDef",
    "UserTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigTypeDef",
    "VpcConfigUnionTypeDef",
    "WaiterConfigTypeDef",
)

class AccessEndpointTypeDef(TypedDict):
    EndpointType: Literal["STREAMING"]
    VpceId: NotRequired[str]

class AppBlockBuilderAppBlockAssociationTypeDef(TypedDict):
    AppBlockArn: str
    AppBlockBuilderName: str

class AppBlockBuilderStateChangeReasonTypeDef(TypedDict):
    Code: NotRequired[Literal["INTERNAL_ERROR"]]
    Message: NotRequired[str]

class ResourceErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[FleetErrorCodeType]
    ErrorMessage: NotRequired[str]
    ErrorTimestamp: NotRequired[datetime]

class VpcConfigOutputTypeDef(TypedDict):
    SubnetIds: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]

class ErrorDetailsTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class S3LocationTypeDef(TypedDict):
    S3Bucket: str
    S3Key: NotRequired[str]

class ApplicationFleetAssociationTypeDef(TypedDict):
    FleetName: str
    ApplicationArn: str

class ApplicationSettingsResponseTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    SettingsGroup: NotRequired[str]
    S3BucketName: NotRequired[str]

class ApplicationSettingsTypeDef(TypedDict):
    Enabled: bool
    SettingsGroup: NotRequired[str]

class AssociateAppBlockBuilderAppBlockRequestTypeDef(TypedDict):
    AppBlockArn: str
    AppBlockBuilderName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateApplicationFleetRequestTypeDef(TypedDict):
    FleetName: str
    ApplicationArn: str

class AssociateApplicationToEntitlementRequestTypeDef(TypedDict):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str

class AssociateFleetRequestTypeDef(TypedDict):
    FleetName: str
    StackName: str

class UserStackAssociationTypeDef(TypedDict):
    StackName: str
    UserName: str
    AuthenticationType: AuthenticationTypeType
    SendEmailNotification: NotRequired[bool]

class CertificateBasedAuthPropertiesTypeDef(TypedDict):
    Status: NotRequired[CertificateBasedAuthStatusType]
    CertificateAuthorityArn: NotRequired[str]

class ComputeCapacityStatusTypeDef(TypedDict):
    Desired: int
    Running: NotRequired[int]
    InUse: NotRequired[int]
    Available: NotRequired[int]
    DesiredUserSessions: NotRequired[int]
    AvailableUserSessions: NotRequired[int]
    ActiveUserSessions: NotRequired[int]
    ActualUserSessions: NotRequired[int]

class ComputeCapacityTypeDef(TypedDict):
    DesiredInstances: NotRequired[int]
    DesiredSessions: NotRequired[int]

class CopyImageRequestTypeDef(TypedDict):
    SourceImageName: str
    DestinationImageName: str
    DestinationRegion: str
    DestinationImageDescription: NotRequired[str]

class CreateAppBlockBuilderStreamingURLRequestTypeDef(TypedDict):
    AppBlockBuilderName: str
    Validity: NotRequired[int]

class ServiceAccountCredentialsTypeDef(TypedDict):
    AccountName: str
    AccountPassword: str

class EntitlementAttributeTypeDef(TypedDict):
    Name: str
    Value: str

class DomainJoinInfoTypeDef(TypedDict):
    DirectoryName: NotRequired[str]
    OrganizationalUnitDistinguishedName: NotRequired[str]

class CreateImageBuilderStreamingURLRequestTypeDef(TypedDict):
    Name: str
    Validity: NotRequired[int]

class StreamingExperienceSettingsTypeDef(TypedDict):
    PreferredProtocol: NotRequired[PreferredProtocolType]

class UserSettingTypeDef(TypedDict):
    Action: ActionType
    Permission: PermissionType
    MaximumLength: NotRequired[int]

class CreateStreamingURLRequestTypeDef(TypedDict):
    StackName: str
    FleetName: str
    UserId: str
    ApplicationId: NotRequired[str]
    Validity: NotRequired[int]
    SessionContext: NotRequired[str]

class ThemeFooterLinkTypeDef(TypedDict):
    DisplayName: NotRequired[str]
    FooterLinkURL: NotRequired[str]

class CreateUpdatedImageRequestTypeDef(TypedDict):
    existingImageName: str
    newImageName: str
    newImageDescription: NotRequired[str]
    newImageDisplayName: NotRequired[str]
    newImageTags: NotRequired[Mapping[str, str]]
    dryRun: NotRequired[bool]

class CreateUserRequestTypeDef(TypedDict):
    UserName: str
    AuthenticationType: AuthenticationTypeType
    MessageAction: NotRequired[MessageActionType]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]

class DeleteAppBlockBuilderRequestTypeDef(TypedDict):
    Name: str

class DeleteAppBlockRequestTypeDef(TypedDict):
    Name: str

class DeleteApplicationRequestTypeDef(TypedDict):
    Name: str

class DeleteDirectoryConfigRequestTypeDef(TypedDict):
    DirectoryName: str

class DeleteEntitlementRequestTypeDef(TypedDict):
    Name: str
    StackName: str

class DeleteFleetRequestTypeDef(TypedDict):
    Name: str

class DeleteImageBuilderRequestTypeDef(TypedDict):
    Name: str

class DeleteImagePermissionsRequestTypeDef(TypedDict):
    Name: str
    SharedAccountId: str

class DeleteImageRequestTypeDef(TypedDict):
    Name: str

class DeleteStackRequestTypeDef(TypedDict):
    Name: str

class DeleteThemeForStackRequestTypeDef(TypedDict):
    StackName: str

class DeleteUserRequestTypeDef(TypedDict):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class DescribeAppBlockBuilderAppBlockAssociationsRequestTypeDef(TypedDict):
    AppBlockArn: NotRequired[str]
    AppBlockBuilderName: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeAppBlockBuildersRequestTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeAppBlocksRequestTypeDef(TypedDict):
    Arns: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeApplicationFleetAssociationsRequestTypeDef(TypedDict):
    FleetName: NotRequired[str]
    ApplicationArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeApplicationsRequestTypeDef(TypedDict):
    Arns: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeDirectoryConfigsRequestTypeDef(TypedDict):
    DirectoryNames: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeEntitlementsRequestTypeDef(TypedDict):
    StackName: str
    Name: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeFleetsRequestTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeImageBuildersRequestTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeImagePermissionsRequestTypeDef(TypedDict):
    Name: str
    MaxResults: NotRequired[int]
    SharedAwsAccountIds: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]

DescribeImagesRequestTypeDef = TypedDict(
    "DescribeImagesRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Arns": NotRequired[Sequence[str]],
        "Type": NotRequired[VisibilityTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

class DescribeSessionsRequestTypeDef(TypedDict):
    StackName: str
    FleetName: str
    UserId: NotRequired[str]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]
    AuthenticationType: NotRequired[AuthenticationTypeType]
    InstanceId: NotRequired[str]

class DescribeStacksRequestTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]

class DescribeThemeForStackRequestTypeDef(TypedDict):
    StackName: str

class DescribeUsageReportSubscriptionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeUserStackAssociationsRequestTypeDef(TypedDict):
    StackName: NotRequired[str]
    UserName: NotRequired[str]
    AuthenticationType: NotRequired[AuthenticationTypeType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeUsersRequestTypeDef(TypedDict):
    AuthenticationType: AuthenticationTypeType
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class UserTypeDef(TypedDict):
    AuthenticationType: AuthenticationTypeType
    Arn: NotRequired[str]
    UserName: NotRequired[str]
    Enabled: NotRequired[bool]
    Status: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    CreatedTime: NotRequired[datetime]

class DisableUserRequestTypeDef(TypedDict):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class DisassociateAppBlockBuilderAppBlockRequestTypeDef(TypedDict):
    AppBlockArn: str
    AppBlockBuilderName: str

class DisassociateApplicationFleetRequestTypeDef(TypedDict):
    FleetName: str
    ApplicationArn: str

class DisassociateApplicationFromEntitlementRequestTypeDef(TypedDict):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str

class DisassociateFleetRequestTypeDef(TypedDict):
    FleetName: str
    StackName: str

class EnableUserRequestTypeDef(TypedDict):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class EntitledApplicationTypeDef(TypedDict):
    ApplicationIdentifier: str

class ExpireSessionRequestTypeDef(TypedDict):
    SessionId: str

class FleetErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[FleetErrorCodeType]
    ErrorMessage: NotRequired[str]

class ImageBuilderStateChangeReasonTypeDef(TypedDict):
    Code: NotRequired[ImageBuilderStateChangeReasonCodeType]
    Message: NotRequired[str]

class NetworkAccessConfigurationTypeDef(TypedDict):
    EniPrivateIpAddress: NotRequired[str]
    EniId: NotRequired[str]

class ImagePermissionsTypeDef(TypedDict):
    allowFleet: NotRequired[bool]
    allowImageBuilder: NotRequired[bool]

class ImageStateChangeReasonTypeDef(TypedDict):
    Code: NotRequired[ImageStateChangeReasonCodeType]
    Message: NotRequired[str]

class LastReportGenerationExecutionErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[UsageReportExecutionErrorCodeType]
    ErrorMessage: NotRequired[str]

class ListAssociatedFleetsRequestTypeDef(TypedDict):
    StackName: str
    NextToken: NotRequired[str]

class ListAssociatedStacksRequestTypeDef(TypedDict):
    FleetName: str
    NextToken: NotRequired[str]

class ListEntitledApplicationsRequestTypeDef(TypedDict):
    StackName: str
    EntitlementName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class StackErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[StackErrorCodeType]
    ErrorMessage: NotRequired[str]

class StorageConnectorOutputTypeDef(TypedDict):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: NotRequired[str]
    Domains: NotRequired[List[str]]
    DomainsRequireAdminConsent: NotRequired[List[str]]

class StartAppBlockBuilderRequestTypeDef(TypedDict):
    Name: str

class StartFleetRequestTypeDef(TypedDict):
    Name: str

class StartImageBuilderRequestTypeDef(TypedDict):
    Name: str
    AppstreamAgentVersion: NotRequired[str]

class StopAppBlockBuilderRequestTypeDef(TypedDict):
    Name: str

class StopFleetRequestTypeDef(TypedDict):
    Name: str

class StopImageBuilderRequestTypeDef(TypedDict):
    Name: str

class StorageConnectorTypeDef(TypedDict):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: NotRequired[str]
    Domains: NotRequired[Sequence[str]]
    DomainsRequireAdminConsent: NotRequired[Sequence[str]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class VpcConfigTypeDef(TypedDict):
    SubnetIds: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]

class AppBlockBuilderTypeDef(TypedDict):
    Arn: str
    Name: str
    Platform: Literal["WINDOWS_SERVER_2019"]
    InstanceType: str
    VpcConfig: VpcConfigOutputTypeDef
    State: AppBlockBuilderStateType
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    EnableDefaultInternetAccess: NotRequired[bool]
    IamRoleArn: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    AppBlockBuilderErrors: NotRequired[List[ResourceErrorTypeDef]]
    StateChangeReason: NotRequired[AppBlockBuilderStateChangeReasonTypeDef]
    AccessEndpoints: NotRequired[List[AccessEndpointTypeDef]]

class ApplicationTypeDef(TypedDict):
    Name: NotRequired[str]
    DisplayName: NotRequired[str]
    IconURL: NotRequired[str]
    LaunchPath: NotRequired[str]
    LaunchParameters: NotRequired[str]
    Enabled: NotRequired[bool]
    Metadata: NotRequired[Dict[str, str]]
    WorkingDirectory: NotRequired[str]
    Description: NotRequired[str]
    Arn: NotRequired[str]
    AppBlockArn: NotRequired[str]
    IconS3Location: NotRequired[S3LocationTypeDef]
    Platforms: NotRequired[List[PlatformTypeType]]
    InstanceFamilies: NotRequired[List[str]]
    CreatedTime: NotRequired[datetime]

class CreateApplicationRequestTypeDef(TypedDict):
    Name: str
    IconS3Location: S3LocationTypeDef
    LaunchPath: str
    Platforms: Sequence[PlatformTypeType]
    InstanceFamilies: Sequence[str]
    AppBlockArn: str
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    WorkingDirectory: NotRequired[str]
    LaunchParameters: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ScriptDetailsTypeDef(TypedDict):
    ScriptS3Location: S3LocationTypeDef
    ExecutablePath: str
    TimeoutInSeconds: int
    ExecutableParameters: NotRequired[str]

class UpdateApplicationRequestTypeDef(TypedDict):
    Name: str
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    IconS3Location: NotRequired[S3LocationTypeDef]
    LaunchPath: NotRequired[str]
    WorkingDirectory: NotRequired[str]
    LaunchParameters: NotRequired[str]
    AppBlockArn: NotRequired[str]
    AttributesToDelete: NotRequired[Sequence[ApplicationAttributeType]]

class AssociateAppBlockBuilderAppBlockResultTypeDef(TypedDict):
    AppBlockBuilderAppBlockAssociation: AppBlockBuilderAppBlockAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateApplicationFleetResultTypeDef(TypedDict):
    ApplicationFleetAssociation: ApplicationFleetAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyImageResponseTypeDef(TypedDict):
    DestinationImageName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppBlockBuilderStreamingURLResultTypeDef(TypedDict):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageBuilderStreamingURLResultTypeDef(TypedDict):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingURLResultTypeDef(TypedDict):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageReportSubscriptionResultTypeDef(TypedDict):
    S3BucketName: str
    Schedule: Literal["DAILY"]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef(TypedDict):
    AppBlockBuilderAppBlockAssociations: List[AppBlockBuilderAppBlockAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeApplicationFleetAssociationsResultTypeDef(TypedDict):
    ApplicationFleetAssociations: List[ApplicationFleetAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAssociatedFleetsResultTypeDef(TypedDict):
    Names: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAssociatedStacksResultTypeDef(TypedDict):
    Names: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateUserStackRequestTypeDef(TypedDict):
    UserStackAssociations: Sequence[UserStackAssociationTypeDef]

class BatchDisassociateUserStackRequestTypeDef(TypedDict):
    UserStackAssociations: Sequence[UserStackAssociationTypeDef]

class DescribeUserStackAssociationsResultTypeDef(TypedDict):
    UserStackAssociations: List[UserStackAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UserStackAssociationErrorTypeDef(TypedDict):
    UserStackAssociation: NotRequired[UserStackAssociationTypeDef]
    ErrorCode: NotRequired[UserStackAssociationErrorCodeType]
    ErrorMessage: NotRequired[str]

class CreateDirectoryConfigRequestTypeDef(TypedDict):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Sequence[str]
    ServiceAccountCredentials: NotRequired[ServiceAccountCredentialsTypeDef]
    CertificateBasedAuthProperties: NotRequired[CertificateBasedAuthPropertiesTypeDef]

class DirectoryConfigTypeDef(TypedDict):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: NotRequired[List[str]]
    ServiceAccountCredentials: NotRequired[ServiceAccountCredentialsTypeDef]
    CreatedTime: NotRequired[datetime]
    CertificateBasedAuthProperties: NotRequired[CertificateBasedAuthPropertiesTypeDef]

class UpdateDirectoryConfigRequestTypeDef(TypedDict):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: NotRequired[Sequence[str]]
    ServiceAccountCredentials: NotRequired[ServiceAccountCredentialsTypeDef]
    CertificateBasedAuthProperties: NotRequired[CertificateBasedAuthPropertiesTypeDef]

class CreateEntitlementRequestTypeDef(TypedDict):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: Sequence[EntitlementAttributeTypeDef]
    Description: NotRequired[str]

class EntitlementTypeDef(TypedDict):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: List[EntitlementAttributeTypeDef]
    Description: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]

class UpdateEntitlementRequestTypeDef(TypedDict):
    Name: str
    StackName: str
    Description: NotRequired[str]
    AppVisibility: NotRequired[AppVisibilityType]
    Attributes: NotRequired[Sequence[EntitlementAttributeTypeDef]]

class CreateThemeForStackRequestTypeDef(TypedDict):
    StackName: str
    TitleText: str
    ThemeStyling: ThemeStylingType
    OrganizationLogoS3Location: S3LocationTypeDef
    FaviconS3Location: S3LocationTypeDef
    FooterLinks: NotRequired[Sequence[ThemeFooterLinkTypeDef]]

class ThemeTypeDef(TypedDict):
    StackName: NotRequired[str]
    State: NotRequired[ThemeStateType]
    ThemeTitleText: NotRequired[str]
    ThemeStyling: NotRequired[ThemeStylingType]
    ThemeFooterLinks: NotRequired[List[ThemeFooterLinkTypeDef]]
    ThemeOrganizationLogoURL: NotRequired[str]
    ThemeFaviconURL: NotRequired[str]
    CreatedTime: NotRequired[datetime]

class UpdateThemeForStackRequestTypeDef(TypedDict):
    StackName: str
    FooterLinks: NotRequired[Sequence[ThemeFooterLinkTypeDef]]
    TitleText: NotRequired[str]
    ThemeStyling: NotRequired[ThemeStylingType]
    OrganizationLogoS3Location: NotRequired[S3LocationTypeDef]
    FaviconS3Location: NotRequired[S3LocationTypeDef]
    State: NotRequired[ThemeStateType]
    AttributesToDelete: NotRequired[Sequence[Literal["FOOTER_LINKS"]]]

class DescribeDirectoryConfigsRequestPaginateTypeDef(TypedDict):
    DirectoryNames: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeFleetsRequestPaginateTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeImageBuildersRequestPaginateTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

DescribeImagesRequestPaginateTypeDef = TypedDict(
    "DescribeImagesRequestPaginateTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Arns": NotRequired[Sequence[str]],
        "Type": NotRequired[VisibilityTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class DescribeSessionsRequestPaginateTypeDef(TypedDict):
    StackName: str
    FleetName: str
    UserId: NotRequired[str]
    AuthenticationType: NotRequired[AuthenticationTypeType]
    InstanceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeStacksRequestPaginateTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUserStackAssociationsRequestPaginateTypeDef(TypedDict):
    StackName: NotRequired[str]
    UserName: NotRequired[str]
    AuthenticationType: NotRequired[AuthenticationTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUsersRequestPaginateTypeDef(TypedDict):
    AuthenticationType: AuthenticationTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssociatedFleetsRequestPaginateTypeDef(TypedDict):
    StackName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssociatedStacksRequestPaginateTypeDef(TypedDict):
    FleetName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeFleetsRequestWaitExtraTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeFleetsRequestWaitTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeUsersResultTypeDef(TypedDict):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEntitledApplicationsResultTypeDef(TypedDict):
    EntitledApplications: List[EntitledApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FleetTypeDef(TypedDict):
    Arn: str
    Name: str
    InstanceType: str
    ComputeCapacityStatus: ComputeCapacityStatusTypeDef
    State: FleetStateType
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    ImageName: NotRequired[str]
    ImageArn: NotRequired[str]
    FleetType: NotRequired[FleetTypeType]
    MaxUserDurationInSeconds: NotRequired[int]
    DisconnectTimeoutInSeconds: NotRequired[int]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    CreatedTime: NotRequired[datetime]
    FleetErrors: NotRequired[List[FleetErrorTypeDef]]
    EnableDefaultInternetAccess: NotRequired[bool]
    DomainJoinInfo: NotRequired[DomainJoinInfoTypeDef]
    IdleDisconnectTimeoutInSeconds: NotRequired[int]
    IamRoleArn: NotRequired[str]
    StreamView: NotRequired[StreamViewType]
    Platform: NotRequired[PlatformTypeType]
    MaxConcurrentSessions: NotRequired[int]
    UsbDeviceFilterStrings: NotRequired[List[str]]
    SessionScriptS3Location: NotRequired[S3LocationTypeDef]
    MaxSessionsPerInstance: NotRequired[int]

class ImageBuilderTypeDef(TypedDict):
    Name: str
    Arn: NotRequired[str]
    ImageArn: NotRequired[str]
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    InstanceType: NotRequired[str]
    Platform: NotRequired[PlatformTypeType]
    IamRoleArn: NotRequired[str]
    State: NotRequired[ImageBuilderStateType]
    StateChangeReason: NotRequired[ImageBuilderStateChangeReasonTypeDef]
    CreatedTime: NotRequired[datetime]
    EnableDefaultInternetAccess: NotRequired[bool]
    DomainJoinInfo: NotRequired[DomainJoinInfoTypeDef]
    NetworkAccessConfiguration: NotRequired[NetworkAccessConfigurationTypeDef]
    ImageBuilderErrors: NotRequired[List[ResourceErrorTypeDef]]
    AppstreamAgentVersion: NotRequired[str]
    AccessEndpoints: NotRequired[List[AccessEndpointTypeDef]]
    LatestAppstreamAgentVersion: NotRequired[LatestAppstreamAgentVersionType]

class SessionTypeDef(TypedDict):
    Id: str
    UserId: str
    StackName: str
    FleetName: str
    State: SessionStateType
    ConnectionState: NotRequired[SessionConnectionStateType]
    StartTime: NotRequired[datetime]
    MaxExpirationTime: NotRequired[datetime]
    AuthenticationType: NotRequired[AuthenticationTypeType]
    NetworkAccessConfiguration: NotRequired[NetworkAccessConfigurationTypeDef]
    InstanceId: NotRequired[str]

class SharedImagePermissionsTypeDef(TypedDict):
    sharedAccountId: str
    imagePermissions: ImagePermissionsTypeDef

class UpdateImagePermissionsRequestTypeDef(TypedDict):
    Name: str
    SharedAccountId: str
    ImagePermissions: ImagePermissionsTypeDef

class UsageReportSubscriptionTypeDef(TypedDict):
    S3BucketName: NotRequired[str]
    Schedule: NotRequired[Literal["DAILY"]]
    LastGeneratedReportDate: NotRequired[datetime]
    SubscriptionErrors: NotRequired[List[LastReportGenerationExecutionErrorTypeDef]]

class StackTypeDef(TypedDict):
    Name: str
    Arn: NotRequired[str]
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    CreatedTime: NotRequired[datetime]
    StorageConnectors: NotRequired[List[StorageConnectorOutputTypeDef]]
    RedirectURL: NotRequired[str]
    FeedbackURL: NotRequired[str]
    StackErrors: NotRequired[List[StackErrorTypeDef]]
    UserSettings: NotRequired[List[UserSettingTypeDef]]
    ApplicationSettings: NotRequired[ApplicationSettingsResponseTypeDef]
    AccessEndpoints: NotRequired[List[AccessEndpointTypeDef]]
    EmbedHostDomains: NotRequired[List[str]]
    StreamingExperienceSettings: NotRequired[StreamingExperienceSettingsTypeDef]

StorageConnectorUnionTypeDef = Union[StorageConnectorTypeDef, StorageConnectorOutputTypeDef]
VpcConfigUnionTypeDef = Union[VpcConfigTypeDef, VpcConfigOutputTypeDef]

class CreateAppBlockBuilderResultTypeDef(TypedDict):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlockBuildersResultTypeDef(TypedDict):
    AppBlockBuilders: List[AppBlockBuilderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartAppBlockBuilderResultTypeDef(TypedDict):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopAppBlockBuilderResultTypeDef(TypedDict):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppBlockBuilderResultTypeDef(TypedDict):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResultTypeDef(TypedDict):
    Application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationsResultTypeDef(TypedDict):
    Applications: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ImageTypeDef(TypedDict):
    Name: str
    Arn: NotRequired[str]
    BaseImageArn: NotRequired[str]
    DisplayName: NotRequired[str]
    State: NotRequired[ImageStateType]
    Visibility: NotRequired[VisibilityTypeType]
    ImageBuilderSupported: NotRequired[bool]
    ImageBuilderName: NotRequired[str]
    Platform: NotRequired[PlatformTypeType]
    Description: NotRequired[str]
    StateChangeReason: NotRequired[ImageStateChangeReasonTypeDef]
    Applications: NotRequired[List[ApplicationTypeDef]]
    CreatedTime: NotRequired[datetime]
    PublicBaseImageReleasedDate: NotRequired[datetime]
    AppstreamAgentVersion: NotRequired[str]
    ImagePermissions: NotRequired[ImagePermissionsTypeDef]
    ImageErrors: NotRequired[List[ResourceErrorTypeDef]]
    LatestAppstreamAgentVersion: NotRequired[LatestAppstreamAgentVersionType]
    SupportedInstanceFamilies: NotRequired[List[str]]
    DynamicAppProvidersEnabled: NotRequired[DynamicAppProvidersEnabledType]
    ImageSharedWithOthers: NotRequired[ImageSharedWithOthersType]

class UpdateApplicationResultTypeDef(TypedDict):
    Application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AppBlockTypeDef(TypedDict):
    Name: str
    Arn: str
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    SourceS3Location: NotRequired[S3LocationTypeDef]
    SetupScriptDetails: NotRequired[ScriptDetailsTypeDef]
    CreatedTime: NotRequired[datetime]
    PostSetupScriptDetails: NotRequired[ScriptDetailsTypeDef]
    PackagingType: NotRequired[PackagingTypeType]
    State: NotRequired[AppBlockStateType]
    AppBlockErrors: NotRequired[List[ErrorDetailsTypeDef]]

class CreateAppBlockRequestTypeDef(TypedDict):
    Name: str
    SourceS3Location: S3LocationTypeDef
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    SetupScriptDetails: NotRequired[ScriptDetailsTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    PostSetupScriptDetails: NotRequired[ScriptDetailsTypeDef]
    PackagingType: NotRequired[PackagingTypeType]

class BatchAssociateUserStackResultTypeDef(TypedDict):
    errors: List[UserStackAssociationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateUserStackResultTypeDef(TypedDict):
    errors: List[UserStackAssociationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryConfigResultTypeDef(TypedDict):
    DirectoryConfig: DirectoryConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectoryConfigsResultTypeDef(TypedDict):
    DirectoryConfigs: List[DirectoryConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateDirectoryConfigResultTypeDef(TypedDict):
    DirectoryConfig: DirectoryConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntitlementResultTypeDef(TypedDict):
    Entitlement: EntitlementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntitlementsResultTypeDef(TypedDict):
    Entitlements: List[EntitlementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateEntitlementResultTypeDef(TypedDict):
    Entitlement: EntitlementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThemeForStackResultTypeDef(TypedDict):
    Theme: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThemeForStackResultTypeDef(TypedDict):
    Theme: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemeForStackResultTypeDef(TypedDict):
    Theme: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResultTypeDef(TypedDict):
    Fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetsResultTypeDef(TypedDict):
    Fleets: List[FleetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateFleetResultTypeDef(TypedDict):
    Fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageBuilderResultTypeDef(TypedDict):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageBuilderResultTypeDef(TypedDict):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageBuildersResultTypeDef(TypedDict):
    ImageBuilders: List[ImageBuilderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartImageBuilderResultTypeDef(TypedDict):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopImageBuilderResultTypeDef(TypedDict):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSessionsResultTypeDef(TypedDict):
    Sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeImagePermissionsResultTypeDef(TypedDict):
    Name: str
    SharedImagePermissionsList: List[SharedImagePermissionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeUsageReportSubscriptionsResultTypeDef(TypedDict):
    UsageReportSubscriptions: List[UsageReportSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateStackResultTypeDef(TypedDict):
    Stack: StackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStacksResultTypeDef(TypedDict):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateStackResultTypeDef(TypedDict):
    Stack: StackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    StorageConnectors: NotRequired[Sequence[StorageConnectorUnionTypeDef]]
    RedirectURL: NotRequired[str]
    FeedbackURL: NotRequired[str]
    UserSettings: NotRequired[Sequence[UserSettingTypeDef]]
    ApplicationSettings: NotRequired[ApplicationSettingsTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    AccessEndpoints: NotRequired[Sequence[AccessEndpointTypeDef]]
    EmbedHostDomains: NotRequired[Sequence[str]]
    StreamingExperienceSettings: NotRequired[StreamingExperienceSettingsTypeDef]

class UpdateStackRequestTypeDef(TypedDict):
    Name: str
    DisplayName: NotRequired[str]
    Description: NotRequired[str]
    StorageConnectors: NotRequired[Sequence[StorageConnectorUnionTypeDef]]
    DeleteStorageConnectors: NotRequired[bool]
    RedirectURL: NotRequired[str]
    FeedbackURL: NotRequired[str]
    AttributesToDelete: NotRequired[Sequence[StackAttributeType]]
    UserSettings: NotRequired[Sequence[UserSettingTypeDef]]
    ApplicationSettings: NotRequired[ApplicationSettingsTypeDef]
    AccessEndpoints: NotRequired[Sequence[AccessEndpointTypeDef]]
    EmbedHostDomains: NotRequired[Sequence[str]]
    StreamingExperienceSettings: NotRequired[StreamingExperienceSettingsTypeDef]

class CreateAppBlockBuilderRequestTypeDef(TypedDict):
    Name: str
    Platform: Literal["WINDOWS_SERVER_2019"]
    InstanceType: str
    VpcConfig: VpcConfigUnionTypeDef
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    EnableDefaultInternetAccess: NotRequired[bool]
    IamRoleArn: NotRequired[str]
    AccessEndpoints: NotRequired[Sequence[AccessEndpointTypeDef]]

class CreateFleetRequestTypeDef(TypedDict):
    Name: str
    InstanceType: str
    ImageName: NotRequired[str]
    ImageArn: NotRequired[str]
    FleetType: NotRequired[FleetTypeType]
    ComputeCapacity: NotRequired[ComputeCapacityTypeDef]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    MaxUserDurationInSeconds: NotRequired[int]
    DisconnectTimeoutInSeconds: NotRequired[int]
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    EnableDefaultInternetAccess: NotRequired[bool]
    DomainJoinInfo: NotRequired[DomainJoinInfoTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    IdleDisconnectTimeoutInSeconds: NotRequired[int]
    IamRoleArn: NotRequired[str]
    StreamView: NotRequired[StreamViewType]
    Platform: NotRequired[PlatformTypeType]
    MaxConcurrentSessions: NotRequired[int]
    UsbDeviceFilterStrings: NotRequired[Sequence[str]]
    SessionScriptS3Location: NotRequired[S3LocationTypeDef]
    MaxSessionsPerInstance: NotRequired[int]

class CreateImageBuilderRequestTypeDef(TypedDict):
    Name: str
    InstanceType: str
    ImageName: NotRequired[str]
    ImageArn: NotRequired[str]
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    IamRoleArn: NotRequired[str]
    EnableDefaultInternetAccess: NotRequired[bool]
    DomainJoinInfo: NotRequired[DomainJoinInfoTypeDef]
    AppstreamAgentVersion: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    AccessEndpoints: NotRequired[Sequence[AccessEndpointTypeDef]]

class UpdateAppBlockBuilderRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    Platform: NotRequired[PlatformTypeType]
    InstanceType: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    EnableDefaultInternetAccess: NotRequired[bool]
    IamRoleArn: NotRequired[str]
    AccessEndpoints: NotRequired[Sequence[AccessEndpointTypeDef]]
    AttributesToDelete: NotRequired[Sequence[AppBlockBuilderAttributeType]]

class UpdateFleetRequestTypeDef(TypedDict):
    ImageName: NotRequired[str]
    ImageArn: NotRequired[str]
    Name: NotRequired[str]
    InstanceType: NotRequired[str]
    ComputeCapacity: NotRequired[ComputeCapacityTypeDef]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    MaxUserDurationInSeconds: NotRequired[int]
    DisconnectTimeoutInSeconds: NotRequired[int]
    DeleteVpcConfig: NotRequired[bool]
    Description: NotRequired[str]
    DisplayName: NotRequired[str]
    EnableDefaultInternetAccess: NotRequired[bool]
    DomainJoinInfo: NotRequired[DomainJoinInfoTypeDef]
    IdleDisconnectTimeoutInSeconds: NotRequired[int]
    AttributesToDelete: NotRequired[Sequence[FleetAttributeType]]
    IamRoleArn: NotRequired[str]
    StreamView: NotRequired[StreamViewType]
    Platform: NotRequired[PlatformTypeType]
    MaxConcurrentSessions: NotRequired[int]
    UsbDeviceFilterStrings: NotRequired[Sequence[str]]
    SessionScriptS3Location: NotRequired[S3LocationTypeDef]
    MaxSessionsPerInstance: NotRequired[int]

class CreateUpdatedImageResultTypeDef(TypedDict):
    image: ImageTypeDef
    canUpdateImage: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageResultTypeDef(TypedDict):
    Image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImagesResultTypeDef(TypedDict):
    Images: List[ImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateAppBlockResultTypeDef(TypedDict):
    AppBlock: AppBlockTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlocksResultTypeDef(TypedDict):
    AppBlocks: List[AppBlockTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
