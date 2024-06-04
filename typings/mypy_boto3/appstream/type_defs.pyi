"""
Type annotations for appstream service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef

    data: AccessEndpointTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActionType,
    AppBlockBuilderAttributeType,
    AppBlockBuilderStateType,
    AppBlockStateType,
    ApplicationAttributeType,
    AppVisibilityType,
    AuthenticationTypeType,
    CertificateBasedAuthStatusType,
    FleetAttributeType,
    FleetErrorCodeType,
    FleetStateType,
    FleetTypeType,
    ImageBuilderStateChangeReasonCodeType,
    ImageBuilderStateType,
    ImageStateChangeReasonCodeType,
    ImageStateType,
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
    UsageReportExecutionErrorCodeType,
    UserStackAssociationErrorCodeType,
    VisibilityTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

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
    "AssociateAppBlockBuilderAppBlockRequestRequestTypeDef",
    "AssociateAppBlockBuilderAppBlockResultTypeDef",
    "AssociateApplicationFleetRequestRequestTypeDef",
    "AssociateApplicationFleetResultTypeDef",
    "AssociateApplicationToEntitlementRequestRequestTypeDef",
    "AssociateFleetRequestRequestTypeDef",
    "BatchAssociateUserStackRequestRequestTypeDef",
    "BatchAssociateUserStackResultTypeDef",
    "BatchDisassociateUserStackRequestRequestTypeDef",
    "BatchDisassociateUserStackResultTypeDef",
    "CertificateBasedAuthPropertiesTypeDef",
    "ComputeCapacityStatusTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageRequestRequestTypeDef",
    "CopyImageResponseTypeDef",
    "CreateAppBlockBuilderRequestRequestTypeDef",
    "CreateAppBlockBuilderResultTypeDef",
    "CreateAppBlockBuilderStreamingURLRequestRequestTypeDef",
    "CreateAppBlockBuilderStreamingURLResultTypeDef",
    "CreateAppBlockRequestRequestTypeDef",
    "CreateAppBlockResultTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResultTypeDef",
    "CreateDirectoryConfigRequestRequestTypeDef",
    "CreateDirectoryConfigResultTypeDef",
    "CreateEntitlementRequestRequestTypeDef",
    "CreateEntitlementResultTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResultTypeDef",
    "CreateImageBuilderRequestRequestTypeDef",
    "CreateImageBuilderResultTypeDef",
    "CreateImageBuilderStreamingURLRequestRequestTypeDef",
    "CreateImageBuilderStreamingURLResultTypeDef",
    "CreateStackRequestRequestTypeDef",
    "CreateStackResultTypeDef",
    "CreateStreamingURLRequestRequestTypeDef",
    "CreateStreamingURLResultTypeDef",
    "CreateUpdatedImageRequestRequestTypeDef",
    "CreateUpdatedImageResultTypeDef",
    "CreateUsageReportSubscriptionResultTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DeleteAppBlockBuilderRequestRequestTypeDef",
    "DeleteAppBlockRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteDirectoryConfigRequestRequestTypeDef",
    "DeleteEntitlementRequestRequestTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteImageBuilderRequestRequestTypeDef",
    "DeleteImageBuilderResultTypeDef",
    "DeleteImagePermissionsRequestRequestTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageResultTypeDef",
    "DeleteStackRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef",
    "DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef",
    "DescribeAppBlockBuildersRequestRequestTypeDef",
    "DescribeAppBlockBuildersResultTypeDef",
    "DescribeAppBlocksRequestRequestTypeDef",
    "DescribeAppBlocksResultTypeDef",
    "DescribeApplicationFleetAssociationsRequestRequestTypeDef",
    "DescribeApplicationFleetAssociationsResultTypeDef",
    "DescribeApplicationsRequestRequestTypeDef",
    "DescribeApplicationsResultTypeDef",
    "DescribeDirectoryConfigsRequestRequestTypeDef",
    "DescribeDirectoryConfigsResultTypeDef",
    "DescribeEntitlementsRequestRequestTypeDef",
    "DescribeEntitlementsResultTypeDef",
    "DescribeFleetsRequestRequestTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeImageBuildersRequestRequestTypeDef",
    "DescribeImageBuildersResultTypeDef",
    "DescribeImagePermissionsRequestRequestTypeDef",
    "DescribeImagePermissionsResultTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeSessionsRequestRequestTypeDef",
    "DescribeSessionsResultTypeDef",
    "DescribeStacksRequestRequestTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeUsageReportSubscriptionsRequestRequestTypeDef",
    "DescribeUsageReportSubscriptionsResultTypeDef",
    "DescribeUserStackAssociationsRequestRequestTypeDef",
    "DescribeUserStackAssociationsResultTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "DescribeUsersResultTypeDef",
    "DirectoryConfigTypeDef",
    "DisableUserRequestRequestTypeDef",
    "DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef",
    "DisassociateApplicationFleetRequestRequestTypeDef",
    "DisassociateApplicationFromEntitlementRequestRequestTypeDef",
    "DisassociateFleetRequestRequestTypeDef",
    "DomainJoinInfoTypeDef",
    "EnableUserRequestRequestTypeDef",
    "EntitledApplicationTypeDef",
    "EntitlementAttributeTypeDef",
    "EntitlementTypeDef",
    "ErrorDetailsTypeDef",
    "ExpireSessionRequestRequestTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "ListAssociatedFleetsRequestRequestTypeDef",
    "ListAssociatedFleetsResultTypeDef",
    "ListAssociatedStacksRequestRequestTypeDef",
    "ListAssociatedStacksResultTypeDef",
    "ListEntitledApplicationsRequestRequestTypeDef",
    "ListEntitledApplicationsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
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
    "StartAppBlockBuilderRequestRequestTypeDef",
    "StartAppBlockBuilderResultTypeDef",
    "StartFleetRequestRequestTypeDef",
    "StartImageBuilderRequestRequestTypeDef",
    "StartImageBuilderResultTypeDef",
    "StopAppBlockBuilderRequestRequestTypeDef",
    "StopAppBlockBuilderResultTypeDef",
    "StopFleetRequestRequestTypeDef",
    "StopImageBuilderRequestRequestTypeDef",
    "StopImageBuilderResultTypeDef",
    "StorageConnectorTypeDef",
    "StreamingExperienceSettingsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppBlockBuilderRequestRequestTypeDef",
    "UpdateAppBlockBuilderResultTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResultTypeDef",
    "UpdateDirectoryConfigRequestRequestTypeDef",
    "UpdateDirectoryConfigResultTypeDef",
    "UpdateEntitlementRequestRequestTypeDef",
    "UpdateEntitlementResultTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateFleetResultTypeDef",
    "UpdateImagePermissionsRequestRequestTypeDef",
    "UpdateStackRequestRequestTypeDef",
    "UpdateStackResultTypeDef",
    "UsageReportSubscriptionTypeDef",
    "UserSettingTypeDef",
    "UserStackAssociationErrorTypeDef",
    "UserStackAssociationTypeDef",
    "UserTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessEndpointTypeDef = TypedDict(
    "_RequiredAccessEndpointTypeDef",
    {
        "EndpointType": Literal["STREAMING"],
    },
)
_OptionalAccessEndpointTypeDef = TypedDict(
    "_OptionalAccessEndpointTypeDef",
    {
        "VpceId": str,
    },
    total=False,
)

class AccessEndpointTypeDef(_RequiredAccessEndpointTypeDef, _OptionalAccessEndpointTypeDef):
    pass

AppBlockBuilderAppBlockAssociationTypeDef = TypedDict(
    "AppBlockBuilderAppBlockAssociationTypeDef",
    {
        "AppBlockArn": str,
        "AppBlockBuilderName": str,
    },
)

AppBlockBuilderStateChangeReasonTypeDef = TypedDict(
    "AppBlockBuilderStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR"],
        "Message": str,
    },
    total=False,
)

_RequiredAppBlockBuilderTypeDef = TypedDict(
    "_RequiredAppBlockBuilderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Platform": Literal["WINDOWS_SERVER_2019"],
        "InstanceType": str,
        "VpcConfig": "VpcConfigTypeDef",
        "State": AppBlockBuilderStateType,
    },
)
_OptionalAppBlockBuilderTypeDef = TypedDict(
    "_OptionalAppBlockBuilderTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "EnableDefaultInternetAccess": bool,
        "IamRoleArn": str,
        "CreatedTime": datetime,
        "AppBlockBuilderErrors": List["ResourceErrorTypeDef"],
        "StateChangeReason": "AppBlockBuilderStateChangeReasonTypeDef",
        "AccessEndpoints": List["AccessEndpointTypeDef"],
    },
    total=False,
)

class AppBlockBuilderTypeDef(_RequiredAppBlockBuilderTypeDef, _OptionalAppBlockBuilderTypeDef):
    pass

_RequiredAppBlockTypeDef = TypedDict(
    "_RequiredAppBlockTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
)
_OptionalAppBlockTypeDef = TypedDict(
    "_OptionalAppBlockTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "SourceS3Location": "S3LocationTypeDef",
        "SetupScriptDetails": "ScriptDetailsTypeDef",
        "CreatedTime": datetime,
        "PostSetupScriptDetails": "ScriptDetailsTypeDef",
        "PackagingType": PackagingTypeType,
        "State": AppBlockStateType,
        "AppBlockErrors": List["ErrorDetailsTypeDef"],
    },
    total=False,
)

class AppBlockTypeDef(_RequiredAppBlockTypeDef, _OptionalAppBlockTypeDef):
    pass

ApplicationFleetAssociationTypeDef = TypedDict(
    "ApplicationFleetAssociationTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
    },
)

ApplicationSettingsResponseTypeDef = TypedDict(
    "ApplicationSettingsResponseTypeDef",
    {
        "Enabled": bool,
        "SettingsGroup": str,
        "S3BucketName": str,
    },
    total=False,
)

_RequiredApplicationSettingsTypeDef = TypedDict(
    "_RequiredApplicationSettingsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalApplicationSettingsTypeDef = TypedDict(
    "_OptionalApplicationSettingsTypeDef",
    {
        "SettingsGroup": str,
    },
    total=False,
)

class ApplicationSettingsTypeDef(
    _RequiredApplicationSettingsTypeDef, _OptionalApplicationSettingsTypeDef
):
    pass

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "IconURL": str,
        "LaunchPath": str,
        "LaunchParameters": str,
        "Enabled": bool,
        "Metadata": Dict[str, str],
        "WorkingDirectory": str,
        "Description": str,
        "Arn": str,
        "AppBlockArn": str,
        "IconS3Location": "S3LocationTypeDef",
        "Platforms": List[PlatformTypeType],
        "InstanceFamilies": List[str],
        "CreatedTime": datetime,
    },
    total=False,
)

AssociateAppBlockBuilderAppBlockRequestRequestTypeDef = TypedDict(
    "AssociateAppBlockBuilderAppBlockRequestRequestTypeDef",
    {
        "AppBlockArn": str,
        "AppBlockBuilderName": str,
    },
)

AssociateAppBlockBuilderAppBlockResultTypeDef = TypedDict(
    "AssociateAppBlockBuilderAppBlockResultTypeDef",
    {
        "AppBlockBuilderAppBlockAssociation": "AppBlockBuilderAppBlockAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateApplicationFleetRequestRequestTypeDef = TypedDict(
    "AssociateApplicationFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
    },
)

AssociateApplicationFleetResultTypeDef = TypedDict(
    "AssociateApplicationFleetResultTypeDef",
    {
        "ApplicationFleetAssociation": "ApplicationFleetAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateApplicationToEntitlementRequestRequestTypeDef = TypedDict(
    "AssociateApplicationToEntitlementRequestRequestTypeDef",
    {
        "StackName": str,
        "EntitlementName": str,
        "ApplicationIdentifier": str,
    },
)

AssociateFleetRequestRequestTypeDef = TypedDict(
    "AssociateFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "StackName": str,
    },
)

BatchAssociateUserStackRequestRequestTypeDef = TypedDict(
    "BatchAssociateUserStackRequestRequestTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
    },
)

BatchAssociateUserStackResultTypeDef = TypedDict(
    "BatchAssociateUserStackResultTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateUserStackRequestRequestTypeDef = TypedDict(
    "BatchDisassociateUserStackRequestRequestTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
    },
)

BatchDisassociateUserStackResultTypeDef = TypedDict(
    "BatchDisassociateUserStackResultTypeDef",
    {
        "errors": List["UserStackAssociationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateBasedAuthPropertiesTypeDef = TypedDict(
    "CertificateBasedAuthPropertiesTypeDef",
    {
        "Status": CertificateBasedAuthStatusType,
        "CertificateAuthorityArn": str,
    },
    total=False,
)

_RequiredComputeCapacityStatusTypeDef = TypedDict(
    "_RequiredComputeCapacityStatusTypeDef",
    {
        "Desired": int,
    },
)
_OptionalComputeCapacityStatusTypeDef = TypedDict(
    "_OptionalComputeCapacityStatusTypeDef",
    {
        "Running": int,
        "InUse": int,
        "Available": int,
        "DesiredUserSessions": int,
        "AvailableUserSessions": int,
        "ActiveUserSessions": int,
        "ActualUserSessions": int,
    },
    total=False,
)

class ComputeCapacityStatusTypeDef(
    _RequiredComputeCapacityStatusTypeDef, _OptionalComputeCapacityStatusTypeDef
):
    pass

ComputeCapacityTypeDef = TypedDict(
    "ComputeCapacityTypeDef",
    {
        "DesiredInstances": int,
        "DesiredSessions": int,
    },
    total=False,
)

_RequiredCopyImageRequestRequestTypeDef = TypedDict(
    "_RequiredCopyImageRequestRequestTypeDef",
    {
        "SourceImageName": str,
        "DestinationImageName": str,
        "DestinationRegion": str,
    },
)
_OptionalCopyImageRequestRequestTypeDef = TypedDict(
    "_OptionalCopyImageRequestRequestTypeDef",
    {
        "DestinationImageDescription": str,
    },
    total=False,
)

class CopyImageRequestRequestTypeDef(
    _RequiredCopyImageRequestRequestTypeDef, _OptionalCopyImageRequestRequestTypeDef
):
    pass

CopyImageResponseTypeDef = TypedDict(
    "CopyImageResponseTypeDef",
    {
        "DestinationImageName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppBlockBuilderRequestRequestTypeDef",
    {
        "Name": str,
        "Platform": Literal["WINDOWS_SERVER_2019"],
        "InstanceType": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
)
_OptionalCreateAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppBlockBuilderRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "Tags": Dict[str, str],
        "EnableDefaultInternetAccess": bool,
        "IamRoleArn": str,
        "AccessEndpoints": List["AccessEndpointTypeDef"],
    },
    total=False,
)

class CreateAppBlockBuilderRequestRequestTypeDef(
    _RequiredCreateAppBlockBuilderRequestRequestTypeDef,
    _OptionalCreateAppBlockBuilderRequestRequestTypeDef,
):
    pass

CreateAppBlockBuilderResultTypeDef = TypedDict(
    "CreateAppBlockBuilderResultTypeDef",
    {
        "AppBlockBuilder": "AppBlockBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppBlockBuilderStreamingURLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppBlockBuilderStreamingURLRequestRequestTypeDef",
    {
        "AppBlockBuilderName": str,
    },
)
_OptionalCreateAppBlockBuilderStreamingURLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppBlockBuilderStreamingURLRequestRequestTypeDef",
    {
        "Validity": int,
    },
    total=False,
)

class CreateAppBlockBuilderStreamingURLRequestRequestTypeDef(
    _RequiredCreateAppBlockBuilderStreamingURLRequestRequestTypeDef,
    _OptionalCreateAppBlockBuilderStreamingURLRequestRequestTypeDef,
):
    pass

CreateAppBlockBuilderStreamingURLResultTypeDef = TypedDict(
    "CreateAppBlockBuilderStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppBlockRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppBlockRequestRequestTypeDef",
    {
        "Name": str,
        "SourceS3Location": "S3LocationTypeDef",
    },
)
_OptionalCreateAppBlockRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppBlockRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "SetupScriptDetails": "ScriptDetailsTypeDef",
        "Tags": Dict[str, str],
        "PostSetupScriptDetails": "ScriptDetailsTypeDef",
        "PackagingType": PackagingTypeType,
    },
    total=False,
)

class CreateAppBlockRequestRequestTypeDef(
    _RequiredCreateAppBlockRequestRequestTypeDef, _OptionalCreateAppBlockRequestRequestTypeDef
):
    pass

CreateAppBlockResultTypeDef = TypedDict(
    "CreateAppBlockResultTypeDef",
    {
        "AppBlock": "AppBlockTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "IconS3Location": "S3LocationTypeDef",
        "LaunchPath": str,
        "Platforms": List[PlatformTypeType],
        "InstanceFamilies": List[str],
        "AppBlockArn": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "WorkingDirectory": str,
        "LaunchParameters": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResultTypeDef = TypedDict(
    "CreateApplicationResultTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectoryConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDirectoryConfigRequestRequestTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedNames": List[str],
    },
)
_OptionalCreateDirectoryConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDirectoryConfigRequestRequestTypeDef",
    {
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
        "CertificateBasedAuthProperties": "CertificateBasedAuthPropertiesTypeDef",
    },
    total=False,
)

class CreateDirectoryConfigRequestRequestTypeDef(
    _RequiredCreateDirectoryConfigRequestRequestTypeDef,
    _OptionalCreateDirectoryConfigRequestRequestTypeDef,
):
    pass

CreateDirectoryConfigResultTypeDef = TypedDict(
    "CreateDirectoryConfigResultTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEntitlementRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEntitlementRequestRequestTypeDef",
    {
        "Name": str,
        "StackName": str,
        "AppVisibility": AppVisibilityType,
        "Attributes": List["EntitlementAttributeTypeDef"],
    },
)
_OptionalCreateEntitlementRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEntitlementRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreateEntitlementRequestRequestTypeDef(
    _RequiredCreateEntitlementRequestRequestTypeDef, _OptionalCreateEntitlementRequestRequestTypeDef
):
    pass

CreateEntitlementResultTypeDef = TypedDict(
    "CreateEntitlementResultTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceType": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "ImageName": str,
        "ImageArn": str,
        "FleetType": FleetTypeType,
        "ComputeCapacity": "ComputeCapacityTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "Description": str,
        "DisplayName": str,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "Tags": Dict[str, str],
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
        "StreamView": StreamViewType,
        "Platform": PlatformTypeType,
        "MaxConcurrentSessions": int,
        "UsbDeviceFilterStrings": List[str],
        "SessionScriptS3Location": "S3LocationTypeDef",
        "MaxSessionsPerInstance": int,
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "Fleet": "FleetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageBuilderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceType": str,
    },
)
_OptionalCreateImageBuilderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageBuilderRequestRequestTypeDef",
    {
        "ImageName": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": "VpcConfigTypeDef",
        "IamRoleArn": str,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "AppstreamAgentVersion": str,
        "Tags": Dict[str, str],
        "AccessEndpoints": List["AccessEndpointTypeDef"],
    },
    total=False,
)

class CreateImageBuilderRequestRequestTypeDef(
    _RequiredCreateImageBuilderRequestRequestTypeDef,
    _OptionalCreateImageBuilderRequestRequestTypeDef,
):
    pass

CreateImageBuilderResultTypeDef = TypedDict(
    "CreateImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageBuilderStreamingURLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageBuilderStreamingURLRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateImageBuilderStreamingURLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageBuilderStreamingURLRequestRequestTypeDef",
    {
        "Validity": int,
    },
    total=False,
)

class CreateImageBuilderStreamingURLRequestRequestTypeDef(
    _RequiredCreateImageBuilderStreamingURLRequestRequestTypeDef,
    _OptionalCreateImageBuilderStreamingURLRequestRequestTypeDef,
):
    pass

CreateImageBuilderStreamingURLResultTypeDef = TypedDict(
    "CreateImageBuilderStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStackRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStackRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateStackRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStackRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "StorageConnectors": List["StorageConnectorTypeDef"],
        "RedirectURL": str,
        "FeedbackURL": str,
        "UserSettings": List["UserSettingTypeDef"],
        "ApplicationSettings": "ApplicationSettingsTypeDef",
        "Tags": Dict[str, str],
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "EmbedHostDomains": List[str],
        "StreamingExperienceSettings": "StreamingExperienceSettingsTypeDef",
    },
    total=False,
)

class CreateStackRequestRequestTypeDef(
    _RequiredCreateStackRequestRequestTypeDef, _OptionalCreateStackRequestRequestTypeDef
):
    pass

CreateStackResultTypeDef = TypedDict(
    "CreateStackResultTypeDef",
    {
        "Stack": "StackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingURLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingURLRequestRequestTypeDef",
    {
        "StackName": str,
        "FleetName": str,
        "UserId": str,
    },
)
_OptionalCreateStreamingURLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingURLRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Validity": int,
        "SessionContext": str,
    },
    total=False,
)

class CreateStreamingURLRequestRequestTypeDef(
    _RequiredCreateStreamingURLRequestRequestTypeDef,
    _OptionalCreateStreamingURLRequestRequestTypeDef,
):
    pass

CreateStreamingURLResultTypeDef = TypedDict(
    "CreateStreamingURLResultTypeDef",
    {
        "StreamingURL": str,
        "Expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUpdatedImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUpdatedImageRequestRequestTypeDef",
    {
        "existingImageName": str,
        "newImageName": str,
    },
)
_OptionalCreateUpdatedImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUpdatedImageRequestRequestTypeDef",
    {
        "newImageDescription": str,
        "newImageDisplayName": str,
        "newImageTags": Dict[str, str],
        "dryRun": bool,
    },
    total=False,
)

class CreateUpdatedImageRequestRequestTypeDef(
    _RequiredCreateUpdatedImageRequestRequestTypeDef,
    _OptionalCreateUpdatedImageRequestRequestTypeDef,
):
    pass

CreateUpdatedImageResultTypeDef = TypedDict(
    "CreateUpdatedImageResultTypeDef",
    {
        "image": "ImageTypeDef",
        "canUpdateImage": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUsageReportSubscriptionResultTypeDef = TypedDict(
    "CreateUsageReportSubscriptionResultTypeDef",
    {
        "S3BucketName": str,
        "Schedule": Literal["DAILY"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "MessageAction": MessageActionType,
        "FirstName": str,
        "LastName": str,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

DeleteAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "DeleteAppBlockBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteAppBlockRequestRequestTypeDef = TypedDict(
    "DeleteAppBlockRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDirectoryConfigRequestRequestTypeDef = TypedDict(
    "DeleteDirectoryConfigRequestRequestTypeDef",
    {
        "DirectoryName": str,
    },
)

DeleteEntitlementRequestRequestTypeDef = TypedDict(
    "DeleteEntitlementRequestRequestTypeDef",
    {
        "Name": str,
        "StackName": str,
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageBuilderRequestRequestTypeDef = TypedDict(
    "DeleteImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageBuilderResultTypeDef = TypedDict(
    "DeleteImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePermissionsRequestRequestTypeDef = TypedDict(
    "DeleteImagePermissionsRequestRequestTypeDef",
    {
        "Name": str,
        "SharedAccountId": str,
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteImageResultTypeDef = TypedDict(
    "DeleteImageResultTypeDef",
    {
        "Image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStackRequestRequestTypeDef = TypedDict(
    "DeleteStackRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef",
    {
        "AppBlockArn": str,
        "AppBlockBuilderName": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef = TypedDict(
    "DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef",
    {
        "AppBlockBuilderAppBlockAssociations": List["AppBlockBuilderAppBlockAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppBlockBuildersRequestRequestTypeDef = TypedDict(
    "DescribeAppBlockBuildersRequestRequestTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAppBlockBuildersResultTypeDef = TypedDict(
    "DescribeAppBlockBuildersResultTypeDef",
    {
        "AppBlockBuilders": List["AppBlockBuilderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppBlocksRequestRequestTypeDef = TypedDict(
    "DescribeAppBlocksRequestRequestTypeDef",
    {
        "Arns": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAppBlocksResultTypeDef = TypedDict(
    "DescribeAppBlocksResultTypeDef",
    {
        "AppBlocks": List["AppBlockTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationFleetAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationFleetAssociationsRequestRequestTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeApplicationFleetAssociationsResultTypeDef = TypedDict(
    "DescribeApplicationFleetAssociationsResultTypeDef",
    {
        "ApplicationFleetAssociations": List["ApplicationFleetAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationsRequestRequestTypeDef",
    {
        "Arns": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeApplicationsResultTypeDef = TypedDict(
    "DescribeApplicationsResultTypeDef",
    {
        "Applications": List["ApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectoryConfigsRequestRequestTypeDef = TypedDict(
    "DescribeDirectoryConfigsRequestRequestTypeDef",
    {
        "DirectoryNames": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeDirectoryConfigsResultTypeDef = TypedDict(
    "DescribeDirectoryConfigsResultTypeDef",
    {
        "DirectoryConfigs": List["DirectoryConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEntitlementsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEntitlementsRequestRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalDescribeEntitlementsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEntitlementsRequestRequestTypeDef",
    {
        "Name": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeEntitlementsRequestRequestTypeDef(
    _RequiredDescribeEntitlementsRequestRequestTypeDef,
    _OptionalDescribeEntitlementsRequestRequestTypeDef,
):
    pass

DescribeEntitlementsResultTypeDef = TypedDict(
    "DescribeEntitlementsResultTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetsRequestRequestTypeDef = TypedDict(
    "DescribeFleetsRequestRequestTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {
        "Fleets": List["FleetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageBuildersRequestRequestTypeDef = TypedDict(
    "DescribeImageBuildersRequestRequestTypeDef",
    {
        "Names": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImageBuildersResultTypeDef = TypedDict(
    "DescribeImageBuildersResultTypeDef",
    {
        "ImageBuilders": List["ImageBuilderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImagePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImagePermissionsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeImagePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImagePermissionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "SharedAwsAccountIds": List[str],
        "NextToken": str,
    },
    total=False,
)

class DescribeImagePermissionsRequestRequestTypeDef(
    _RequiredDescribeImagePermissionsRequestRequestTypeDef,
    _OptionalDescribeImagePermissionsRequestRequestTypeDef,
):
    pass

DescribeImagePermissionsResultTypeDef = TypedDict(
    "DescribeImagePermissionsResultTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List["SharedImagePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "Names": List[str],
        "Arns": List[str],
        "Type": VisibilityTypeType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSessionsRequestRequestTypeDef",
    {
        "StackName": str,
        "FleetName": str,
    },
)
_OptionalDescribeSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSessionsRequestRequestTypeDef",
    {
        "UserId": str,
        "NextToken": str,
        "Limit": int,
        "AuthenticationType": AuthenticationTypeType,
        "InstanceId": str,
    },
    total=False,
)

class DescribeSessionsRequestRequestTypeDef(
    _RequiredDescribeSessionsRequestRequestTypeDef, _OptionalDescribeSessionsRequestRequestTypeDef
):
    pass

DescribeSessionsResultTypeDef = TypedDict(
    "DescribeSessionsResultTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksRequestRequestTypeDef = TypedDict(
    "DescribeStacksRequestRequestTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsageReportSubscriptionsRequestRequestTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeUsageReportSubscriptionsResultTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsResultTypeDef",
    {
        "UsageReportSubscriptions": List["UsageReportSubscriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserStackAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeUserStackAssociationsRequestRequestTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeUserStackAssociationsResultTypeDef = TypedDict(
    "DescribeUserStackAssociationsResultTypeDef",
    {
        "UserStackAssociations": List["UserStackAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeUsersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeUsersRequestRequestTypeDef",
    {
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalDescribeUsersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeUsersRequestRequestTypeDef(
    _RequiredDescribeUsersRequestRequestTypeDef, _OptionalDescribeUsersRequestRequestTypeDef
):
    pass

DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDirectoryConfigTypeDef = TypedDict(
    "_RequiredDirectoryConfigTypeDef",
    {
        "DirectoryName": str,
    },
)
_OptionalDirectoryConfigTypeDef = TypedDict(
    "_OptionalDirectoryConfigTypeDef",
    {
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
        "CreatedTime": datetime,
        "CertificateBasedAuthProperties": "CertificateBasedAuthPropertiesTypeDef",
    },
    total=False,
)

class DirectoryConfigTypeDef(_RequiredDirectoryConfigTypeDef, _OptionalDirectoryConfigTypeDef):
    pass

DisableUserRequestRequestTypeDef = TypedDict(
    "DisableUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef = TypedDict(
    "DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef",
    {
        "AppBlockArn": str,
        "AppBlockBuilderName": str,
    },
)

DisassociateApplicationFleetRequestRequestTypeDef = TypedDict(
    "DisassociateApplicationFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "ApplicationArn": str,
    },
)

DisassociateApplicationFromEntitlementRequestRequestTypeDef = TypedDict(
    "DisassociateApplicationFromEntitlementRequestRequestTypeDef",
    {
        "StackName": str,
        "EntitlementName": str,
        "ApplicationIdentifier": str,
    },
)

DisassociateFleetRequestRequestTypeDef = TypedDict(
    "DisassociateFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "StackName": str,
    },
)

DomainJoinInfoTypeDef = TypedDict(
    "DomainJoinInfoTypeDef",
    {
        "DirectoryName": str,
        "OrganizationalUnitDistinguishedName": str,
    },
    total=False,
)

EnableUserRequestRequestTypeDef = TypedDict(
    "EnableUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)

EntitledApplicationTypeDef = TypedDict(
    "EntitledApplicationTypeDef",
    {
        "ApplicationIdentifier": str,
    },
)

EntitlementAttributeTypeDef = TypedDict(
    "EntitlementAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef",
    {
        "Name": str,
        "StackName": str,
        "AppVisibility": AppVisibilityType,
        "Attributes": List["EntitlementAttributeTypeDef"],
    },
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {
        "Description": str,
        "CreatedTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ExpireSessionRequestRequestTypeDef = TypedDict(
    "ExpireSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

FleetErrorTypeDef = TypedDict(
    "FleetErrorTypeDef",
    {
        "ErrorCode": FleetErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredFleetTypeDef = TypedDict(
    "_RequiredFleetTypeDef",
    {
        "Arn": str,
        "Name": str,
        "InstanceType": str,
        "ComputeCapacityStatus": "ComputeCapacityStatusTypeDef",
        "State": FleetStateType,
    },
)
_OptionalFleetTypeDef = TypedDict(
    "_OptionalFleetTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "FleetType": FleetTypeType,
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "VpcConfig": "VpcConfigTypeDef",
        "CreatedTime": datetime,
        "FleetErrors": List["FleetErrorTypeDef"],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
        "StreamView": StreamViewType,
        "Platform": PlatformTypeType,
        "MaxConcurrentSessions": int,
        "UsbDeviceFilterStrings": List[str],
        "SessionScriptS3Location": "S3LocationTypeDef",
        "MaxSessionsPerInstance": int,
    },
    total=False,
)

class FleetTypeDef(_RequiredFleetTypeDef, _OptionalFleetTypeDef):
    pass

ImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ImageBuilderStateChangeReasonTypeDef",
    {
        "Code": ImageBuilderStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredImageBuilderTypeDef = TypedDict(
    "_RequiredImageBuilderTypeDef",
    {
        "Name": str,
    },
)
_OptionalImageBuilderTypeDef = TypedDict(
    "_OptionalImageBuilderTypeDef",
    {
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": "VpcConfigTypeDef",
        "InstanceType": str,
        "Platform": PlatformTypeType,
        "IamRoleArn": str,
        "State": ImageBuilderStateType,
        "StateChangeReason": "ImageBuilderStateChangeReasonTypeDef",
        "CreatedTime": datetime,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "NetworkAccessConfiguration": "NetworkAccessConfigurationTypeDef",
        "ImageBuilderErrors": List["ResourceErrorTypeDef"],
        "AppstreamAgentVersion": str,
        "AccessEndpoints": List["AccessEndpointTypeDef"],
    },
    total=False,
)

class ImageBuilderTypeDef(_RequiredImageBuilderTypeDef, _OptionalImageBuilderTypeDef):
    pass

ImagePermissionsTypeDef = TypedDict(
    "ImagePermissionsTypeDef",
    {
        "allowFleet": bool,
        "allowImageBuilder": bool,
    },
    total=False,
)

ImageStateChangeReasonTypeDef = TypedDict(
    "ImageStateChangeReasonTypeDef",
    {
        "Code": ImageStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredImageTypeDef = TypedDict(
    "_RequiredImageTypeDef",
    {
        "Name": str,
    },
)
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": ImageStateType,
        "Visibility": VisibilityTypeType,
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": PlatformTypeType,
        "Description": str,
        "StateChangeReason": "ImageStateChangeReasonTypeDef",
        "Applications": List["ApplicationTypeDef"],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": "ImagePermissionsTypeDef",
        "ImageErrors": List["ResourceErrorTypeDef"],
    },
    total=False,
)

class ImageTypeDef(_RequiredImageTypeDef, _OptionalImageTypeDef):
    pass

LastReportGenerationExecutionErrorTypeDef = TypedDict(
    "LastReportGenerationExecutionErrorTypeDef",
    {
        "ErrorCode": UsageReportExecutionErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredListAssociatedFleetsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedFleetsRequestRequestTypeDef",
    {
        "StackName": str,
    },
)
_OptionalListAssociatedFleetsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedFleetsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListAssociatedFleetsRequestRequestTypeDef(
    _RequiredListAssociatedFleetsRequestRequestTypeDef,
    _OptionalListAssociatedFleetsRequestRequestTypeDef,
):
    pass

ListAssociatedFleetsResultTypeDef = TypedDict(
    "ListAssociatedFleetsResultTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedStacksRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedStacksRequestRequestTypeDef",
    {
        "FleetName": str,
    },
)
_OptionalListAssociatedStacksRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedStacksRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListAssociatedStacksRequestRequestTypeDef(
    _RequiredListAssociatedStacksRequestRequestTypeDef,
    _OptionalListAssociatedStacksRequestRequestTypeDef,
):
    pass

ListAssociatedStacksResultTypeDef = TypedDict(
    "ListAssociatedStacksResultTypeDef",
    {
        "Names": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntitledApplicationsRequestRequestTypeDef = TypedDict(
    "_RequiredListEntitledApplicationsRequestRequestTypeDef",
    {
        "StackName": str,
        "EntitlementName": str,
    },
)
_OptionalListEntitledApplicationsRequestRequestTypeDef = TypedDict(
    "_OptionalListEntitledApplicationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListEntitledApplicationsRequestRequestTypeDef(
    _RequiredListEntitledApplicationsRequestRequestTypeDef,
    _OptionalListEntitledApplicationsRequestRequestTypeDef,
):
    pass

ListEntitledApplicationsResultTypeDef = TypedDict(
    "ListEntitledApplicationsResultTypeDef",
    {
        "EntitledApplications": List["EntitledApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "EniPrivateIpAddress": str,
        "EniId": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResourceErrorTypeDef = TypedDict(
    "ResourceErrorTypeDef",
    {
        "ErrorCode": FleetErrorCodeType,
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "S3Key": str,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

_RequiredScriptDetailsTypeDef = TypedDict(
    "_RequiredScriptDetailsTypeDef",
    {
        "ScriptS3Location": "S3LocationTypeDef",
        "ExecutablePath": str,
        "TimeoutInSeconds": int,
    },
)
_OptionalScriptDetailsTypeDef = TypedDict(
    "_OptionalScriptDetailsTypeDef",
    {
        "ExecutableParameters": str,
    },
    total=False,
)

class ScriptDetailsTypeDef(_RequiredScriptDetailsTypeDef, _OptionalScriptDetailsTypeDef):
    pass

ServiceAccountCredentialsTypeDef = TypedDict(
    "ServiceAccountCredentialsTypeDef",
    {
        "AccountName": str,
        "AccountPassword": str,
    },
)

_RequiredSessionTypeDef = TypedDict(
    "_RequiredSessionTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": SessionStateType,
    },
)
_OptionalSessionTypeDef = TypedDict(
    "_OptionalSessionTypeDef",
    {
        "ConnectionState": SessionConnectionStateType,
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": AuthenticationTypeType,
        "NetworkAccessConfiguration": "NetworkAccessConfigurationTypeDef",
        "InstanceId": str,
    },
    total=False,
)

class SessionTypeDef(_RequiredSessionTypeDef, _OptionalSessionTypeDef):
    pass

SharedImagePermissionsTypeDef = TypedDict(
    "SharedImagePermissionsTypeDef",
    {
        "sharedAccountId": str,
        "imagePermissions": "ImagePermissionsTypeDef",
    },
)

StackErrorTypeDef = TypedDict(
    "StackErrorTypeDef",
    {
        "ErrorCode": StackErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {
        "Name": str,
    },
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "Arn": str,
        "Description": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "StorageConnectors": List["StorageConnectorTypeDef"],
        "RedirectURL": str,
        "FeedbackURL": str,
        "StackErrors": List["StackErrorTypeDef"],
        "UserSettings": List["UserSettingTypeDef"],
        "ApplicationSettings": "ApplicationSettingsResponseTypeDef",
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "EmbedHostDomains": List[str],
        "StreamingExperienceSettings": "StreamingExperienceSettingsTypeDef",
    },
    total=False,
)

class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass

StartAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "StartAppBlockBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartAppBlockBuilderResultTypeDef = TypedDict(
    "StartAppBlockBuilderResultTypeDef",
    {
        "AppBlockBuilder": "AppBlockBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartFleetRequestRequestTypeDef = TypedDict(
    "StartFleetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredStartImageBuilderRequestRequestTypeDef = TypedDict(
    "_RequiredStartImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartImageBuilderRequestRequestTypeDef = TypedDict(
    "_OptionalStartImageBuilderRequestRequestTypeDef",
    {
        "AppstreamAgentVersion": str,
    },
    total=False,
)

class StartImageBuilderRequestRequestTypeDef(
    _RequiredStartImageBuilderRequestRequestTypeDef, _OptionalStartImageBuilderRequestRequestTypeDef
):
    pass

StartImageBuilderResultTypeDef = TypedDict(
    "StartImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "StopAppBlockBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopAppBlockBuilderResultTypeDef = TypedDict(
    "StopAppBlockBuilderResultTypeDef",
    {
        "AppBlockBuilder": "AppBlockBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFleetRequestRequestTypeDef = TypedDict(
    "StopFleetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopImageBuilderRequestRequestTypeDef = TypedDict(
    "StopImageBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopImageBuilderResultTypeDef = TypedDict(
    "StopImageBuilderResultTypeDef",
    {
        "ImageBuilder": "ImageBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStorageConnectorTypeDef = TypedDict(
    "_RequiredStorageConnectorTypeDef",
    {
        "ConnectorType": StorageConnectorTypeType,
    },
)
_OptionalStorageConnectorTypeDef = TypedDict(
    "_OptionalStorageConnectorTypeDef",
    {
        "ResourceIdentifier": str,
        "Domains": List[str],
    },
    total=False,
)

class StorageConnectorTypeDef(_RequiredStorageConnectorTypeDef, _OptionalStorageConnectorTypeDef):
    pass

StreamingExperienceSettingsTypeDef = TypedDict(
    "StreamingExperienceSettingsTypeDef",
    {
        "PreferredProtocol": PreferredProtocolType,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppBlockBuilderRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateAppBlockBuilderRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppBlockBuilderRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "Platform": PlatformTypeType,
        "InstanceType": str,
        "VpcConfig": "VpcConfigTypeDef",
        "EnableDefaultInternetAccess": bool,
        "IamRoleArn": str,
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "AttributesToDelete": List[AppBlockBuilderAttributeType],
    },
    total=False,
)

class UpdateAppBlockBuilderRequestRequestTypeDef(
    _RequiredUpdateAppBlockBuilderRequestRequestTypeDef,
    _OptionalUpdateAppBlockBuilderRequestRequestTypeDef,
):
    pass

UpdateAppBlockBuilderResultTypeDef = TypedDict(
    "UpdateAppBlockBuilderResultTypeDef",
    {
        "AppBlockBuilder": "AppBlockBuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "IconS3Location": "S3LocationTypeDef",
        "LaunchPath": str,
        "WorkingDirectory": str,
        "LaunchParameters": str,
        "AppBlockArn": str,
        "AttributesToDelete": List[ApplicationAttributeType],
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UpdateApplicationResultTypeDef = TypedDict(
    "UpdateApplicationResultTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDirectoryConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDirectoryConfigRequestRequestTypeDef",
    {
        "DirectoryName": str,
    },
)
_OptionalUpdateDirectoryConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDirectoryConfigRequestRequestTypeDef",
    {
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
        "CertificateBasedAuthProperties": "CertificateBasedAuthPropertiesTypeDef",
    },
    total=False,
)

class UpdateDirectoryConfigRequestRequestTypeDef(
    _RequiredUpdateDirectoryConfigRequestRequestTypeDef,
    _OptionalUpdateDirectoryConfigRequestRequestTypeDef,
):
    pass

UpdateDirectoryConfigResultTypeDef = TypedDict(
    "UpdateDirectoryConfigResultTypeDef",
    {
        "DirectoryConfig": "DirectoryConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEntitlementRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEntitlementRequestRequestTypeDef",
    {
        "Name": str,
        "StackName": str,
    },
)
_OptionalUpdateEntitlementRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEntitlementRequestRequestTypeDef",
    {
        "Description": str,
        "AppVisibility": AppVisibilityType,
        "Attributes": List["EntitlementAttributeTypeDef"],
    },
    total=False,
)

class UpdateEntitlementRequestRequestTypeDef(
    _RequiredUpdateEntitlementRequestRequestTypeDef, _OptionalUpdateEntitlementRequestRequestTypeDef
):
    pass

UpdateEntitlementResultTypeDef = TypedDict(
    "UpdateEntitlementResultTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetRequestRequestTypeDef = TypedDict(
    "UpdateFleetRequestRequestTypeDef",
    {
        "ImageName": str,
        "ImageArn": str,
        "Name": str,
        "InstanceType": str,
        "ComputeCapacity": "ComputeCapacityTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "DeleteVpcConfig": bool,
        "Description": str,
        "DisplayName": str,
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "IdleDisconnectTimeoutInSeconds": int,
        "AttributesToDelete": List[FleetAttributeType],
        "IamRoleArn": str,
        "StreamView": StreamViewType,
        "Platform": PlatformTypeType,
        "MaxConcurrentSessions": int,
        "UsbDeviceFilterStrings": List[str],
        "SessionScriptS3Location": "S3LocationTypeDef",
        "MaxSessionsPerInstance": int,
    },
    total=False,
)

UpdateFleetResultTypeDef = TypedDict(
    "UpdateFleetResultTypeDef",
    {
        "Fleet": "FleetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateImagePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateImagePermissionsRequestRequestTypeDef",
    {
        "Name": str,
        "SharedAccountId": str,
        "ImagePermissions": "ImagePermissionsTypeDef",
    },
)

_RequiredUpdateStackRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStackRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateStackRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStackRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "StorageConnectors": List["StorageConnectorTypeDef"],
        "DeleteStorageConnectors": bool,
        "RedirectURL": str,
        "FeedbackURL": str,
        "AttributesToDelete": List[StackAttributeType],
        "UserSettings": List["UserSettingTypeDef"],
        "ApplicationSettings": "ApplicationSettingsTypeDef",
        "AccessEndpoints": List["AccessEndpointTypeDef"],
        "EmbedHostDomains": List[str],
        "StreamingExperienceSettings": "StreamingExperienceSettingsTypeDef",
    },
    total=False,
)

class UpdateStackRequestRequestTypeDef(
    _RequiredUpdateStackRequestRequestTypeDef, _OptionalUpdateStackRequestRequestTypeDef
):
    pass

UpdateStackResultTypeDef = TypedDict(
    "UpdateStackResultTypeDef",
    {
        "Stack": "StackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageReportSubscriptionTypeDef = TypedDict(
    "UsageReportSubscriptionTypeDef",
    {
        "S3BucketName": str,
        "Schedule": Literal["DAILY"],
        "LastGeneratedReportDate": datetime,
        "SubscriptionErrors": List["LastReportGenerationExecutionErrorTypeDef"],
    },
    total=False,
)

_RequiredUserSettingTypeDef = TypedDict(
    "_RequiredUserSettingTypeDef",
    {
        "Action": ActionType,
        "Permission": PermissionType,
    },
)
_OptionalUserSettingTypeDef = TypedDict(
    "_OptionalUserSettingTypeDef",
    {
        "MaximumLength": int,
    },
    total=False,
)

class UserSettingTypeDef(_RequiredUserSettingTypeDef, _OptionalUserSettingTypeDef):
    pass

UserStackAssociationErrorTypeDef = TypedDict(
    "UserStackAssociationErrorTypeDef",
    {
        "UserStackAssociation": "UserStackAssociationTypeDef",
        "ErrorCode": UserStackAssociationErrorCodeType,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredUserStackAssociationTypeDef = TypedDict(
    "_RequiredUserStackAssociationTypeDef",
    {
        "StackName": str,
        "UserName": str,
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalUserStackAssociationTypeDef = TypedDict(
    "_OptionalUserStackAssociationTypeDef",
    {
        "SendEmailNotification": bool,
    },
    total=False,
)

class UserStackAssociationTypeDef(
    _RequiredUserStackAssociationTypeDef, _OptionalUserStackAssociationTypeDef
):
    pass

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "AuthenticationType": AuthenticationTypeType,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "Arn": str,
        "UserName": str,
        "Enabled": bool,
        "Status": str,
        "FirstName": str,
        "LastName": str,
        "CreatedTime": datetime,
    },
    total=False,
)

class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
