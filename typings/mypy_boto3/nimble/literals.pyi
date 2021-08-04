"""
Type annotations for nimble service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/literals.html)

Usage::

    ```python
    from mypy_boto3_nimble.literals import LaunchProfilePersonaType

    data: LaunchProfilePersonaType = "USER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "LaunchProfilePersonaType",
    "LaunchProfilePlatformType",
    "LaunchProfileStateType",
    "LaunchProfileStatusCodeType",
    "ListEulaAcceptancesPaginatorName",
    "ListEulasPaginatorName",
    "ListLaunchProfileMembersPaginatorName",
    "ListLaunchProfilesPaginatorName",
    "ListStreamingImagesPaginatorName",
    "ListStreamingSessionsPaginatorName",
    "ListStudioComponentsPaginatorName",
    "ListStudioMembersPaginatorName",
    "ListStudiosPaginatorName",
    "StreamingClipboardModeType",
    "StreamingImageEncryptionConfigurationKeyTypeType",
    "StreamingImageStateType",
    "StreamingImageStatusCodeType",
    "StreamingInstanceTypeType",
    "StreamingSessionStateType",
    "StreamingSessionStatusCodeType",
    "StreamingSessionStreamStateType",
    "StreamingSessionStreamStatusCodeType",
    "StudioComponentInitializationScriptRunContextType",
    "StudioComponentStateType",
    "StudioComponentStatusCodeType",
    "StudioComponentSubtypeType",
    "StudioComponentTypeType",
    "StudioEncryptionConfigurationKeyTypeType",
    "StudioPersonaType",
    "StudioStateType",
    "StudioStatusCodeType",
)

LaunchProfilePersonaType = Literal["USER"]
LaunchProfilePlatformType = Literal["LINUX", "WINDOWS"]
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
ListEulaAcceptancesPaginatorName = Literal["list_eula_acceptances"]
ListEulasPaginatorName = Literal["list_eulas"]
ListLaunchProfileMembersPaginatorName = Literal["list_launch_profile_members"]
ListLaunchProfilesPaginatorName = Literal["list_launch_profiles"]
ListStreamingImagesPaginatorName = Literal["list_streaming_images"]
ListStreamingSessionsPaginatorName = Literal["list_streaming_sessions"]
ListStudioComponentsPaginatorName = Literal["list_studio_components"]
ListStudioMembersPaginatorName = Literal["list_studio_members"]
ListStudiosPaginatorName = Literal["list_studios"]
StreamingClipboardModeType = Literal["DISABLED", "ENABLED"]
StreamingImageEncryptionConfigurationKeyTypeType = Literal["CUSTOMER_MANAGED_KEY"]
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
    "INTERNAL_ERROR",
    "STREAMING_IMAGE_CREATE_IN_PROGRESS",
    "STREAMING_IMAGE_DELETED",
    "STREAMING_IMAGE_DELETE_IN_PROGRESS",
    "STREAMING_IMAGE_READY",
    "STREAMING_IMAGE_UPDATE_IN_PROGRESS",
]
StreamingInstanceTypeType = Literal[
    "g4dn.12xlarge", "g4dn.16xlarge", "g4dn.2xlarge", "g4dn.4xlarge", "g4dn.8xlarge", "g4dn.xlarge"
]
StreamingSessionStateType = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"
]
StreamingSessionStatusCodeType = Literal[
    "ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
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
]
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
StudioComponentInitializationScriptRunContextType = Literal[
    "SYSTEM_INITIALIZATION", "USER_INITIALIZATION"
]
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
StudioEncryptionConfigurationKeyTypeType = Literal["AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY"]
StudioPersonaType = Literal["ADMINISTRATOR"]
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
