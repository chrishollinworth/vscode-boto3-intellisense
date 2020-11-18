"""
Main interface for appstream service type definitions.

Usage::

    ```python
    from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef

    data: AccessEndpointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

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
    "ApplicationSettingsResponseTypeDef",
    "ApplicationTypeDef",
    "ComputeCapacityStatusTypeDef",
    "DirectoryConfigTypeDef",
    "DomainJoinInfoTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "ResourceErrorTypeDef",
    "ServiceAccountCredentialsTypeDef",
    "SessionTypeDef",
    "SharedImagePermissionsTypeDef",
    "StackErrorTypeDef",
    "StackTypeDef",
    "StorageConnectorTypeDef",
    "UsageReportSubscriptionTypeDef",
    "UserSettingTypeDef",
    "UserStackAssociationErrorTypeDef",
    "UserStackAssociationTypeDef",
    "UserTypeDef",
    "VpcConfigTypeDef",
    "ApplicationSettingsTypeDef",
    "BatchAssociateUserStackResultTypeDef",
    "BatchDisassociateUserStackResultTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageResponseTypeDef",
    "CreateDirectoryConfigResultTypeDef",
    "CreateFleetResultTypeDef",
    "CreateImageBuilderResultTypeDef",
    "CreateImageBuilderStreamingURLResultTypeDef",
    "CreateStackResultTypeDef",
    "CreateStreamingURLResultTypeDef",
    "CreateUsageReportSubscriptionResultTypeDef",
    "DeleteImageBuilderResultTypeDef",
    "DeleteImageResultTypeDef",
    "DescribeDirectoryConfigsResultTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeImageBuildersResultTypeDef",
    "DescribeImagePermissionsResultTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeSessionsResultTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeUsageReportSubscriptionsResultTypeDef",
    "DescribeUserStackAssociationsResultTypeDef",
    "DescribeUsersResultTypeDef",
    "ListAssociatedFleetsResultTypeDef",
    "ListAssociatedStacksResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartImageBuilderResultTypeDef",
    "StopImageBuilderResultTypeDef",
    "UpdateDirectoryConfigResultTypeDef",
    "UpdateFleetResultTypeDef",
    "UpdateStackResultTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessEndpointTypeDef = TypedDict(
    "_RequiredAccessEndpointTypeDef", {"EndpointType": Literal["STREAMING"]}
)
_OptionalAccessEndpointTypeDef = TypedDict(
    "_OptionalAccessEndpointTypeDef", {"VpceId": str}, total=False
)


class AccessEndpointTypeDef(_RequiredAccessEndpointTypeDef, _OptionalAccessEndpointTypeDef):
    pass


ApplicationSettingsResponseTypeDef = TypedDict(
    "ApplicationSettingsResponseTypeDef",
    {"Enabled": bool, "SettingsGroup": str, "S3BucketName": str},
    total=False,
)

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
    },
    total=False,
)

_RequiredComputeCapacityStatusTypeDef = TypedDict(
    "_RequiredComputeCapacityStatusTypeDef", {"Desired": int}
)
_OptionalComputeCapacityStatusTypeDef = TypedDict(
    "_OptionalComputeCapacityStatusTypeDef",
    {"Running": int, "InUse": int, "Available": int},
    total=False,
)


class ComputeCapacityStatusTypeDef(
    _RequiredComputeCapacityStatusTypeDef, _OptionalComputeCapacityStatusTypeDef
):
    pass


_RequiredDirectoryConfigTypeDef = TypedDict(
    "_RequiredDirectoryConfigTypeDef", {"DirectoryName": str}
)
_OptionalDirectoryConfigTypeDef = TypedDict(
    "_OptionalDirectoryConfigTypeDef",
    {
        "OrganizationalUnitDistinguishedNames": List[str],
        "ServiceAccountCredentials": "ServiceAccountCredentialsTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)


class DirectoryConfigTypeDef(_RequiredDirectoryConfigTypeDef, _OptionalDirectoryConfigTypeDef):
    pass


DomainJoinInfoTypeDef = TypedDict(
    "DomainJoinInfoTypeDef",
    {"DirectoryName": str, "OrganizationalUnitDistinguishedName": str},
    total=False,
)

FleetErrorTypeDef = TypedDict(
    "FleetErrorTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
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
        "State": Literal["STARTING", "RUNNING", "STOPPING", "STOPPED"],
    },
)
_OptionalFleetTypeDef = TypedDict(
    "_OptionalFleetTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "ImageName": str,
        "ImageArn": str,
        "FleetType": Literal["ALWAYS_ON", "ON_DEMAND"],
        "MaxUserDurationInSeconds": int,
        "DisconnectTimeoutInSeconds": int,
        "VpcConfig": "VpcConfigTypeDef",
        "CreatedTime": datetime,
        "FleetErrors": List["FleetErrorTypeDef"],
        "EnableDefaultInternetAccess": bool,
        "DomainJoinInfo": "DomainJoinInfoTypeDef",
        "IdleDisconnectTimeoutInSeconds": int,
        "IamRoleArn": str,
        "StreamView": Literal["APP", "DESKTOP"],
    },
    total=False,
)


class FleetTypeDef(_RequiredFleetTypeDef, _OptionalFleetTypeDef):
    pass


ImageBuilderStateChangeReasonTypeDef = TypedDict(
    "ImageBuilderStateChangeReasonTypeDef",
    {"Code": Literal["INTERNAL_ERROR", "IMAGE_UNAVAILABLE"], "Message": str},
    total=False,
)

_RequiredImageBuilderTypeDef = TypedDict("_RequiredImageBuilderTypeDef", {"Name": str})
_OptionalImageBuilderTypeDef = TypedDict(
    "_OptionalImageBuilderTypeDef",
    {
        "Arn": str,
        "ImageArn": str,
        "Description": str,
        "DisplayName": str,
        "VpcConfig": "VpcConfigTypeDef",
        "InstanceType": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "IamRoleArn": str,
        "State": Literal[
            "PENDING",
            "UPDATING_AGENT",
            "RUNNING",
            "STOPPING",
            "STOPPED",
            "REBOOTING",
            "SNAPSHOTTING",
            "DELETING",
            "FAILED",
        ],
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
    "ImagePermissionsTypeDef", {"allowFleet": bool, "allowImageBuilder": bool}, total=False
)

ImageStateChangeReasonTypeDef = TypedDict(
    "ImageStateChangeReasonTypeDef",
    {
        "Code": Literal["INTERNAL_ERROR", "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE"],
        "Message": str,
    },
    total=False,
)

_RequiredImageTypeDef = TypedDict("_RequiredImageTypeDef", {"Name": str})
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {
        "Arn": str,
        "BaseImageArn": str,
        "DisplayName": str,
        "State": Literal["PENDING", "AVAILABLE", "FAILED", "COPYING", "DELETING"],
        "Visibility": Literal["PUBLIC", "PRIVATE", "SHARED"],
        "ImageBuilderSupported": bool,
        "ImageBuilderName": str,
        "Platform": Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"],
        "Description": str,
        "StateChangeReason": "ImageStateChangeReasonTypeDef",
        "Applications": List["ApplicationTypeDef"],
        "CreatedTime": datetime,
        "PublicBaseImageReleasedDate": datetime,
        "AppstreamAgentVersion": str,
        "ImagePermissions": "ImagePermissionsTypeDef",
    },
    total=False,
)


class ImageTypeDef(_RequiredImageTypeDef, _OptionalImageTypeDef):
    pass


LastReportGenerationExecutionErrorTypeDef = TypedDict(
    "LastReportGenerationExecutionErrorTypeDef",
    {
        "ErrorCode": Literal["RESOURCE_NOT_FOUND", "ACCESS_DENIED", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef", {"EniPrivateIpAddress": str, "EniId": str}, total=False
)

ResourceErrorTypeDef = TypedDict(
    "ResourceErrorTypeDef",
    {
        "ErrorCode": Literal[
            "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
            "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
            "NETWORK_INTERFACE_LIMIT_EXCEEDED",
            "INTERNAL_SERVICE_ERROR",
            "IAM_SERVICE_ROLE_IS_MISSING",
            "MACHINE_ROLE_IS_MISSING",
            "STS_DISABLED_IN_REGION",
            "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
            "SUBNET_NOT_FOUND",
            "IMAGE_NOT_FOUND",
            "INVALID_SUBNET_CONFIGURATION",
            "SECURITY_GROUPS_NOT_FOUND",
            "IGW_NOT_ATTACHED",
            "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
            "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
            "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
            "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
            "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
            "DOMAIN_JOIN_ERROR_MORE_DATA",
            "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
            "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
            "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
            "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
            "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
            "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
            "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
        ],
        "ErrorMessage": str,
        "ErrorTimestamp": datetime,
    },
    total=False,
)

ServiceAccountCredentialsTypeDef = TypedDict(
    "ServiceAccountCredentialsTypeDef", {"AccountName": str, "AccountPassword": str}
)

_RequiredSessionTypeDef = TypedDict(
    "_RequiredSessionTypeDef",
    {
        "Id": str,
        "UserId": str,
        "StackName": str,
        "FleetName": str,
        "State": Literal["ACTIVE", "PENDING", "EXPIRED"],
    },
)
_OptionalSessionTypeDef = TypedDict(
    "_OptionalSessionTypeDef",
    {
        "ConnectionState": Literal["CONNECTED", "NOT_CONNECTED"],
        "StartTime": datetime,
        "MaxExpirationTime": datetime,
        "AuthenticationType": Literal["API", "SAML", "USERPOOL"],
        "NetworkAccessConfiguration": "NetworkAccessConfigurationTypeDef",
    },
    total=False,
)


class SessionTypeDef(_RequiredSessionTypeDef, _OptionalSessionTypeDef):
    pass


SharedImagePermissionsTypeDef = TypedDict(
    "SharedImagePermissionsTypeDef",
    {"sharedAccountId": str, "imagePermissions": "ImagePermissionsTypeDef"},
)

StackErrorTypeDef = TypedDict(
    "StackErrorTypeDef",
    {
        "ErrorCode": Literal["STORAGE_CONNECTOR_ERROR", "INTERNAL_SERVICE_ERROR"],
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredStackTypeDef = TypedDict("_RequiredStackTypeDef", {"Name": str})
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
    },
    total=False,
)


class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass


_RequiredStorageConnectorTypeDef = TypedDict(
    "_RequiredStorageConnectorTypeDef",
    {"ConnectorType": Literal["HOMEFOLDERS", "GOOGLE_DRIVE", "ONE_DRIVE"]},
)
_OptionalStorageConnectorTypeDef = TypedDict(
    "_OptionalStorageConnectorTypeDef",
    {"ResourceIdentifier": str, "Domains": List[str]},
    total=False,
)


class StorageConnectorTypeDef(_RequiredStorageConnectorTypeDef, _OptionalStorageConnectorTypeDef):
    pass


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

UserSettingTypeDef = TypedDict(
    "UserSettingTypeDef",
    {
        "Action": Literal[
            "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
            "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
            "FILE_UPLOAD",
            "FILE_DOWNLOAD",
            "PRINTING_TO_LOCAL_DEVICE",
        ],
        "Permission": Literal["ENABLED", "DISABLED"],
    },
)

UserStackAssociationErrorTypeDef = TypedDict(
    "UserStackAssociationErrorTypeDef",
    {
        "UserStackAssociation": "UserStackAssociationTypeDef",
        "ErrorCode": Literal[
            "STACK_NOT_FOUND", "USER_NAME_NOT_FOUND", "DIRECTORY_NOT_FOUND", "INTERNAL_ERROR"
        ],
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredUserStackAssociationTypeDef = TypedDict(
    "_RequiredUserStackAssociationTypeDef",
    {"StackName": str, "UserName": str, "AuthenticationType": Literal["API", "SAML", "USERPOOL"]},
)
_OptionalUserStackAssociationTypeDef = TypedDict(
    "_OptionalUserStackAssociationTypeDef", {"SendEmailNotification": bool}, total=False
)


class UserStackAssociationTypeDef(
    _RequiredUserStackAssociationTypeDef, _OptionalUserStackAssociationTypeDef
):
    pass


_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef", {"AuthenticationType": Literal["API", "SAML", "USERPOOL"]}
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
    "VpcConfigTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}, total=False
)

_RequiredApplicationSettingsTypeDef = TypedDict(
    "_RequiredApplicationSettingsTypeDef", {"Enabled": bool}
)
_OptionalApplicationSettingsTypeDef = TypedDict(
    "_OptionalApplicationSettingsTypeDef", {"SettingsGroup": str}, total=False
)


class ApplicationSettingsTypeDef(
    _RequiredApplicationSettingsTypeDef, _OptionalApplicationSettingsTypeDef
):
    pass


BatchAssociateUserStackResultTypeDef = TypedDict(
    "BatchAssociateUserStackResultTypeDef",
    {"errors": List["UserStackAssociationErrorTypeDef"]},
    total=False,
)

BatchDisassociateUserStackResultTypeDef = TypedDict(
    "BatchDisassociateUserStackResultTypeDef",
    {"errors": List["UserStackAssociationErrorTypeDef"]},
    total=False,
)

ComputeCapacityTypeDef = TypedDict("ComputeCapacityTypeDef", {"DesiredInstances": int})

CopyImageResponseTypeDef = TypedDict(
    "CopyImageResponseTypeDef", {"DestinationImageName": str}, total=False
)

CreateDirectoryConfigResultTypeDef = TypedDict(
    "CreateDirectoryConfigResultTypeDef", {"DirectoryConfig": "DirectoryConfigTypeDef"}, total=False
)

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef", {"Fleet": "FleetTypeDef"}, total=False
)

CreateImageBuilderResultTypeDef = TypedDict(
    "CreateImageBuilderResultTypeDef", {"ImageBuilder": "ImageBuilderTypeDef"}, total=False
)

CreateImageBuilderStreamingURLResultTypeDef = TypedDict(
    "CreateImageBuilderStreamingURLResultTypeDef",
    {"StreamingURL": str, "Expires": datetime},
    total=False,
)

CreateStackResultTypeDef = TypedDict(
    "CreateStackResultTypeDef", {"Stack": "StackTypeDef"}, total=False
)

CreateStreamingURLResultTypeDef = TypedDict(
    "CreateStreamingURLResultTypeDef", {"StreamingURL": str, "Expires": datetime}, total=False
)

CreateUsageReportSubscriptionResultTypeDef = TypedDict(
    "CreateUsageReportSubscriptionResultTypeDef",
    {"S3BucketName": str, "Schedule": Literal["DAILY"]},
    total=False,
)

DeleteImageBuilderResultTypeDef = TypedDict(
    "DeleteImageBuilderResultTypeDef", {"ImageBuilder": "ImageBuilderTypeDef"}, total=False
)

DeleteImageResultTypeDef = TypedDict(
    "DeleteImageResultTypeDef", {"Image": "ImageTypeDef"}, total=False
)

DescribeDirectoryConfigsResultTypeDef = TypedDict(
    "DescribeDirectoryConfigsResultTypeDef",
    {"DirectoryConfigs": List["DirectoryConfigTypeDef"], "NextToken": str},
    total=False,
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef", {"Fleets": List["FleetTypeDef"], "NextToken": str}, total=False
)

DescribeImageBuildersResultTypeDef = TypedDict(
    "DescribeImageBuildersResultTypeDef",
    {"ImageBuilders": List["ImageBuilderTypeDef"], "NextToken": str},
    total=False,
)

DescribeImagePermissionsResultTypeDef = TypedDict(
    "DescribeImagePermissionsResultTypeDef",
    {
        "Name": str,
        "SharedImagePermissionsList": List["SharedImagePermissionsTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef", {"Images": List["ImageTypeDef"], "NextToken": str}, total=False
)

DescribeSessionsResultTypeDef = TypedDict(
    "DescribeSessionsResultTypeDef",
    {"Sessions": List["SessionTypeDef"], "NextToken": str},
    total=False,
)

DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef", {"Stacks": List["StackTypeDef"], "NextToken": str}, total=False
)

DescribeUsageReportSubscriptionsResultTypeDef = TypedDict(
    "DescribeUsageReportSubscriptionsResultTypeDef",
    {"UsageReportSubscriptions": List["UsageReportSubscriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeUserStackAssociationsResultTypeDef = TypedDict(
    "DescribeUserStackAssociationsResultTypeDef",
    {"UserStackAssociations": List["UserStackAssociationTypeDef"], "NextToken": str},
    total=False,
)

DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef", {"Users": List["UserTypeDef"], "NextToken": str}, total=False
)

ListAssociatedFleetsResultTypeDef = TypedDict(
    "ListAssociatedFleetsResultTypeDef", {"Names": List[str], "NextToken": str}, total=False
)

ListAssociatedStacksResultTypeDef = TypedDict(
    "ListAssociatedStacksResultTypeDef", {"Names": List[str], "NextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartImageBuilderResultTypeDef = TypedDict(
    "StartImageBuilderResultTypeDef", {"ImageBuilder": "ImageBuilderTypeDef"}, total=False
)

StopImageBuilderResultTypeDef = TypedDict(
    "StopImageBuilderResultTypeDef", {"ImageBuilder": "ImageBuilderTypeDef"}, total=False
)

UpdateDirectoryConfigResultTypeDef = TypedDict(
    "UpdateDirectoryConfigResultTypeDef", {"DirectoryConfig": "DirectoryConfigTypeDef"}, total=False
)

UpdateFleetResultTypeDef = TypedDict(
    "UpdateFleetResultTypeDef", {"Fleet": "FleetTypeDef"}, total=False
)

UpdateStackResultTypeDef = TypedDict(
    "UpdateStackResultTypeDef", {"Stack": "StackTypeDef"}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
