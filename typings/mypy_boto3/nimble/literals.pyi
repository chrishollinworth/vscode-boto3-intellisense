"""
Type annotations for nimble service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/literals.html)

Usage::

    ```python
    from mypy_boto3_nimble.literals import AutomaticTerminationModeType

    data: AutomaticTerminationModeType = "ACTIVATED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AutomaticTerminationModeType",
    "LaunchProfileDeletedWaiterName",
    "LaunchProfilePersonaType",
    "LaunchProfilePlatformType",
    "LaunchProfileReadyWaiterName",
    "LaunchProfileStateType",
    "LaunchProfileStatusCodeType",
    "LaunchProfileValidationStateType",
    "LaunchProfileValidationStatusCodeType",
    "LaunchProfileValidationTypeType",
    "ListEulaAcceptancesPaginatorName",
    "ListEulasPaginatorName",
    "ListLaunchProfileMembersPaginatorName",
    "ListLaunchProfilesPaginatorName",
    "ListStreamingImagesPaginatorName",
    "ListStreamingSessionBackupsPaginatorName",
    "ListStreamingSessionsPaginatorName",
    "ListStudioComponentsPaginatorName",
    "ListStudioMembersPaginatorName",
    "ListStudiosPaginatorName",
    "SessionBackupModeType",
    "SessionPersistenceModeType",
    "StreamingClipboardModeType",
    "StreamingImageDeletedWaiterName",
    "StreamingImageEncryptionConfigurationKeyTypeType",
    "StreamingImageReadyWaiterName",
    "StreamingImageStateType",
    "StreamingImageStatusCodeType",
    "StreamingInstanceTypeType",
    "StreamingSessionDeletedWaiterName",
    "StreamingSessionReadyWaiterName",
    "StreamingSessionStateType",
    "StreamingSessionStatusCodeType",
    "StreamingSessionStoppedWaiterName",
    "StreamingSessionStorageModeType",
    "StreamingSessionStreamReadyWaiterName",
    "StreamingSessionStreamStateType",
    "StreamingSessionStreamStatusCodeType",
    "StudioComponentDeletedWaiterName",
    "StudioComponentInitializationScriptRunContextType",
    "StudioComponentReadyWaiterName",
    "StudioComponentStateType",
    "StudioComponentStatusCodeType",
    "StudioComponentSubtypeType",
    "StudioComponentTypeType",
    "StudioDeletedWaiterName",
    "StudioEncryptionConfigurationKeyTypeType",
    "StudioPersonaType",
    "StudioReadyWaiterName",
    "StudioStateType",
    "StudioStatusCodeType",
    "VolumeRetentionModeType",
)

AutomaticTerminationModeType = Literal["ACTIVATED", "DEACTIVATED"]
LaunchProfileDeletedWaiterName = Literal["launch_profile_deleted"]
LaunchProfilePersonaType = Literal["USER"]
LaunchProfilePlatformType = Literal["LINUX", "WINDOWS"]
LaunchProfileReadyWaiterName = Literal["launch_profile_ready"]
LaunchProfileStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
LaunchProfileStatusCodeType = Literal[
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "INVALID_INSTANCE_TYPES_PROVIDED",
    "INVALID_SUBNETS_COMBINATION",
    "INVALID_SUBNETS_PROVIDED",
    "LAUNCH_PROFILE_CREATED",
    "LAUNCH_PROFILE_CREATE_IN_PROGRESS",
    "LAUNCH_PROFILE_DELETED",
    "LAUNCH_PROFILE_DELETE_IN_PROGRESS",
    "LAUNCH_PROFILE_UPDATED",
    "LAUNCH_PROFILE_UPDATE_IN_PROGRESS",
    "LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED",
    "STREAMING_IMAGE_NOT_FOUND",
    "STREAMING_IMAGE_NOT_READY",
]
LaunchProfileValidationStateType = Literal[
    "VALIDATION_FAILED",
    "VALIDATION_FAILED_INTERNAL_SERVER_ERROR",
    "VALIDATION_IN_PROGRESS",
    "VALIDATION_NOT_STARTED",
    "VALIDATION_SUCCESS",
]
LaunchProfileValidationStatusCodeType = Literal[
    "VALIDATION_FAILED_INTERNAL_SERVER_ERROR",
    "VALIDATION_FAILED_INVALID_ACTIVE_DIRECTORY",
    "VALIDATION_FAILED_INVALID_SECURITY_GROUP_ASSOCIATION",
    "VALIDATION_FAILED_INVALID_SUBNET_ROUTE_TABLE_ASSOCIATION",
    "VALIDATION_FAILED_SUBNET_NOT_FOUND",
    "VALIDATION_FAILED_UNAUTHORIZED",
    "VALIDATION_IN_PROGRESS",
    "VALIDATION_NOT_STARTED",
    "VALIDATION_SUCCESS",
]
LaunchProfileValidationTypeType = Literal[
    "VALIDATE_ACTIVE_DIRECTORY_STUDIO_COMPONENT",
    "VALIDATE_NETWORK_ACL_ASSOCIATION",
    "VALIDATE_SECURITY_GROUP_ASSOCIATION",
    "VALIDATE_SUBNET_ASSOCIATION",
]
ListEulaAcceptancesPaginatorName = Literal["list_eula_acceptances"]
ListEulasPaginatorName = Literal["list_eulas"]
ListLaunchProfileMembersPaginatorName = Literal["list_launch_profile_members"]
ListLaunchProfilesPaginatorName = Literal["list_launch_profiles"]
ListStreamingImagesPaginatorName = Literal["list_streaming_images"]
ListStreamingSessionBackupsPaginatorName = Literal["list_streaming_session_backups"]
ListStreamingSessionsPaginatorName = Literal["list_streaming_sessions"]
ListStudioComponentsPaginatorName = Literal["list_studio_components"]
ListStudioMembersPaginatorName = Literal["list_studio_members"]
ListStudiosPaginatorName = Literal["list_studios"]
SessionBackupModeType = Literal["AUTOMATIC", "DEACTIVATED"]
SessionPersistenceModeType = Literal["ACTIVATED", "DEACTIVATED"]
StreamingClipboardModeType = Literal["DISABLED", "ENABLED"]
StreamingImageDeletedWaiterName = Literal["streaming_image_deleted"]
StreamingImageEncryptionConfigurationKeyTypeType = Literal["CUSTOMER_MANAGED_KEY"]
StreamingImageReadyWaiterName = Literal["streaming_image_ready"]
StreamingImageStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StreamingImageStatusCodeType = Literal[
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
    "STREAMING_IMAGE_CREATE_IN_PROGRESS",
    "STREAMING_IMAGE_DELETED",
    "STREAMING_IMAGE_DELETE_IN_PROGRESS",
    "STREAMING_IMAGE_READY",
    "STREAMING_IMAGE_UPDATE_IN_PROGRESS",
]
StreamingInstanceTypeType = Literal[
    "g3.4xlarge",
    "g3s.xlarge",
    "g4dn.12xlarge",
    "g4dn.16xlarge",
    "g4dn.2xlarge",
    "g4dn.4xlarge",
    "g4dn.8xlarge",
    "g4dn.xlarge",
    "g5.16xlarge",
    "g5.2xlarge",
    "g5.4xlarge",
    "g5.8xlarge",
    "g5.xlarge",
]
StreamingSessionDeletedWaiterName = Literal["streaming_session_deleted"]
StreamingSessionReadyWaiterName = Literal["streaming_session_ready"]
StreamingSessionStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "START_FAILED",
    "START_IN_PROGRESS",
    "STOPPED",
    "STOP_FAILED",
    "STOP_IN_PROGRESS",
]
StreamingSessionStatusCodeType = Literal[
    "ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
    "AMI_VALIDATION_ERROR",
    "DECRYPT_STREAMING_IMAGE_ERROR",
    "INITIALIZATION_SCRIPT_ERROR",
    "INSUFFICIENT_CAPACITY",
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "NETWORK_INTERFACE_ERROR",
    "STREAMING_SESSION_CREATE_IN_PROGRESS",
    "STREAMING_SESSION_DELETED",
    "STREAMING_SESSION_DELETE_IN_PROGRESS",
    "STREAMING_SESSION_READY",
    "STREAMING_SESSION_STARTED",
    "STREAMING_SESSION_START_IN_PROGRESS",
    "STREAMING_SESSION_STOPPED",
    "STREAMING_SESSION_STOP_IN_PROGRESS",
]
StreamingSessionStoppedWaiterName = Literal["streaming_session_stopped"]
StreamingSessionStorageModeType = Literal["UPLOAD"]
StreamingSessionStreamReadyWaiterName = Literal["streaming_session_stream_ready"]
StreamingSessionStreamStateType = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"
]
StreamingSessionStreamStatusCodeType = Literal[
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "STREAM_CREATE_IN_PROGRESS",
    "STREAM_DELETED",
    "STREAM_DELETE_IN_PROGRESS",
    "STREAM_READY",
]
StudioComponentDeletedWaiterName = Literal["studio_component_deleted"]
StudioComponentInitializationScriptRunContextType = Literal[
    "SYSTEM_INITIALIZATION", "USER_INITIALIZATION"
]
StudioComponentReadyWaiterName = Literal["studio_component_ready"]
StudioComponentStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StudioComponentStatusCodeType = Literal[
    "ACTIVE_DIRECTORY_ALREADY_EXISTS",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "STUDIO_COMPONENT_CREATED",
    "STUDIO_COMPONENT_CREATE_IN_PROGRESS",
    "STUDIO_COMPONENT_DELETED",
    "STUDIO_COMPONENT_DELETE_IN_PROGRESS",
    "STUDIO_COMPONENT_UPDATED",
    "STUDIO_COMPONENT_UPDATE_IN_PROGRESS",
]
StudioComponentSubtypeType = Literal[
    "AMAZON_FSX_FOR_LUSTRE", "AMAZON_FSX_FOR_WINDOWS", "AWS_MANAGED_MICROSOFT_AD", "CUSTOM"
]
StudioComponentTypeType = Literal[
    "ACTIVE_DIRECTORY", "COMPUTE_FARM", "CUSTOM", "LICENSE_SERVICE", "SHARED_FILE_SYSTEM"
]
StudioDeletedWaiterName = Literal["studio_deleted"]
StudioEncryptionConfigurationKeyTypeType = Literal["AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY"]
StudioPersonaType = Literal["ADMINISTRATOR"]
StudioReadyWaiterName = Literal["studio_ready"]
StudioStateType = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StudioStatusCodeType = Literal[
    "AWS_SSO_ACCESS_DENIED",
    "AWS_SSO_CONFIGURATION_REPAIRED",
    "AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS",
    "AWS_SSO_NOT_ENABLED",
    "AWS_STS_REGION_DISABLED",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "ROLE_COULD_NOT_BE_ASSUMED",
    "ROLE_NOT_OWNED_BY_STUDIO_OWNER",
    "STUDIO_CREATED",
    "STUDIO_CREATE_IN_PROGRESS",
    "STUDIO_DELETED",
    "STUDIO_DELETE_IN_PROGRESS",
    "STUDIO_UPDATED",
    "STUDIO_UPDATE_IN_PROGRESS",
    "STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED",
    "STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED",
    "STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED",
]
VolumeRetentionModeType = Literal["DELETE", "RETAIN"]
