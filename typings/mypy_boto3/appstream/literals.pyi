"""
Type annotations for appstream service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/literals.html)

Usage::

    ```python
    from mypy_boto3_appstream.literals import AccessEndpointTypeType

    data: AccessEndpointTypeType = "STREAMING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessEndpointTypeType",
    "ActionType",
    "AppVisibilityType",
    "ApplicationAttributeType",
    "AuthenticationTypeType",
    "CertificateBasedAuthStatusType",
    "DescribeDirectoryConfigsPaginatorName",
    "DescribeFleetsPaginatorName",
    "DescribeImageBuildersPaginatorName",
    "DescribeImagesPaginatorName",
    "DescribeSessionsPaginatorName",
    "DescribeStacksPaginatorName",
    "DescribeUserStackAssociationsPaginatorName",
    "DescribeUsersPaginatorName",
    "FleetAttributeType",
    "FleetErrorCodeType",
    "FleetStartedWaiterName",
    "FleetStateType",
    "FleetStoppedWaiterName",
    "FleetTypeType",
    "ImageBuilderStateChangeReasonCodeType",
    "ImageBuilderStateType",
    "ImageStateChangeReasonCodeType",
    "ImageStateType",
    "ListAssociatedFleetsPaginatorName",
    "ListAssociatedStacksPaginatorName",
    "MessageActionType",
    "PermissionType",
    "PlatformTypeType",
    "PreferredProtocolType",
    "SessionConnectionStateType",
    "SessionStateType",
    "StackAttributeType",
    "StackErrorCodeType",
    "StorageConnectorTypeType",
    "StreamViewType",
    "UsageReportExecutionErrorCodeType",
    "UsageReportScheduleType",
    "UserStackAssociationErrorCodeType",
    "VisibilityTypeType",
)

AccessEndpointTypeType = Literal["STREAMING"]
ActionType = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "DOMAIN_PASSWORD_SIGNIN",
    "DOMAIN_SMART_CARD_SIGNIN",
    "FILE_DOWNLOAD",
    "FILE_UPLOAD",
    "PRINTING_TO_LOCAL_DEVICE",
]
AppVisibilityType = Literal["ALL", "ASSOCIATED"]
ApplicationAttributeType = Literal["LAUNCH_PARAMETERS", "WORKING_DIRECTORY"]
AuthenticationTypeType = Literal["API", "AWS_AD", "SAML", "USERPOOL"]
CertificateBasedAuthStatusType = Literal[
    "DISABLED", "ENABLED", "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK"
]
DescribeDirectoryConfigsPaginatorName = Literal["describe_directory_configs"]
DescribeFleetsPaginatorName = Literal["describe_fleets"]
DescribeImageBuildersPaginatorName = Literal["describe_image_builders"]
DescribeImagesPaginatorName = Literal["describe_images"]
DescribeSessionsPaginatorName = Literal["describe_sessions"]
DescribeStacksPaginatorName = Literal["describe_stacks"]
DescribeUserStackAssociationsPaginatorName = Literal["describe_user_stack_associations"]
DescribeUsersPaginatorName = Literal["describe_users"]
FleetAttributeType = Literal[
    "DOMAIN_JOIN_INFO",
    "IAM_ROLE_ARN",
    "SESSION_SCRIPT_S3_LOCATION",
    "USB_DEVICE_FILTER_STRINGS",
    "VPC_CONFIGURATION",
    "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
]
FleetErrorCodeType = Literal[
    "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
    "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
    "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
    "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
    "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
    "DOMAIN_JOIN_ERROR_MORE_DATA",
    "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
    "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
    "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
    "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
    "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
    "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
    "FLEET_INSTANCE_PROVISIONING_FAILURE",
    "FLEET_STOPPED",
    "IAM_SERVICE_ROLE_IS_MISSING",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
    "IGW_NOT_ATTACHED",
    "IMAGE_NOT_FOUND",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_SUBNET_CONFIGURATION",
    "MACHINE_ROLE_IS_MISSING",
    "NETWORK_INTERFACE_LIMIT_EXCEEDED",
    "SECURITY_GROUPS_NOT_FOUND",
    "STS_DISABLED_IN_REGION",
    "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
    "SUBNET_NOT_FOUND",
]
FleetStartedWaiterName = Literal["fleet_started"]
FleetStateType = Literal["RUNNING", "STARTING", "STOPPED", "STOPPING"]
FleetStoppedWaiterName = Literal["fleet_stopped"]
FleetTypeType = Literal["ALWAYS_ON", "ELASTIC", "ON_DEMAND"]
ImageBuilderStateChangeReasonCodeType = Literal["IMAGE_UNAVAILABLE", "INTERNAL_ERROR"]
ImageBuilderStateType = Literal[
    "DELETING",
    "FAILED",
    "PENDING",
    "PENDING_QUALIFICATION",
    "REBOOTING",
    "RUNNING",
    "SNAPSHOTTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
    "UPDATING_AGENT",
]
ImageStateChangeReasonCodeType = Literal[
    "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE", "INTERNAL_ERROR"
]
ImageStateType = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETING", "FAILED", "IMPORTING", "PENDING"
]
ListAssociatedFleetsPaginatorName = Literal["list_associated_fleets"]
ListAssociatedStacksPaginatorName = Literal["list_associated_stacks"]
MessageActionType = Literal["RESEND", "SUPPRESS"]
PermissionType = Literal["DISABLED", "ENABLED"]
PlatformTypeType = Literal["AMAZON_LINUX2", "WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"]
PreferredProtocolType = Literal["TCP", "UDP"]
SessionConnectionStateType = Literal["CONNECTED", "NOT_CONNECTED"]
SessionStateType = Literal["ACTIVE", "EXPIRED", "PENDING"]
StackAttributeType = Literal[
    "ACCESS_ENDPOINTS",
    "EMBED_HOST_DOMAINS",
    "FEEDBACK_URL",
    "IAM_ROLE_ARN",
    "REDIRECT_URL",
    "STORAGE_CONNECTORS",
    "STORAGE_CONNECTOR_GOOGLE_DRIVE",
    "STORAGE_CONNECTOR_HOMEFOLDERS",
    "STORAGE_CONNECTOR_ONE_DRIVE",
    "STREAMING_EXPERIENCE_SETTINGS",
    "THEME_NAME",
    "USER_SETTINGS",
]
StackErrorCodeType = Literal["INTERNAL_SERVICE_ERROR", "STORAGE_CONNECTOR_ERROR"]
StorageConnectorTypeType = Literal["GOOGLE_DRIVE", "HOMEFOLDERS", "ONE_DRIVE"]
StreamViewType = Literal["APP", "DESKTOP"]
UsageReportExecutionErrorCodeType = Literal[
    "ACCESS_DENIED", "INTERNAL_SERVICE_ERROR", "RESOURCE_NOT_FOUND"
]
UsageReportScheduleType = Literal["DAILY"]
UserStackAssociationErrorCodeType = Literal[
    "DIRECTORY_NOT_FOUND", "INTERNAL_ERROR", "STACK_NOT_FOUND", "USER_NAME_NOT_FOUND"
]
VisibilityTypeType = Literal["PRIVATE", "PUBLIC", "SHARED"]
