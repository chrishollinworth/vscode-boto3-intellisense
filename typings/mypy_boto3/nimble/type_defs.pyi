"""
Type annotations for nimble service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/type_defs.html)

Usage::

    ```python
    from mypy_boto3_nimble.type_defs import AcceptEulasRequestRequestTypeDef

    data: AcceptEulasRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    LaunchProfilePlatformType,
    LaunchProfileStateType,
    LaunchProfileStatusCodeType,
    StreamingClipboardModeType,
    StreamingImageStateType,
    StreamingImageStatusCodeType,
    StreamingInstanceTypeType,
    StreamingSessionStateType,
    StreamingSessionStatusCodeType,
    StreamingSessionStreamStateType,
    StreamingSessionStreamStatusCodeType,
    StudioComponentInitializationScriptRunContextType,
    StudioComponentStateType,
    StudioComponentStatusCodeType,
    StudioComponentSubtypeType,
    StudioComponentTypeType,
    StudioEncryptionConfigurationKeyTypeType,
    StudioStateType,
    StudioStatusCodeType,
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
    "AcceptEulasRequestRequestTypeDef",
    "AcceptEulasResponseTypeDef",
    "ActiveDirectoryComputerAttributeTypeDef",
    "ActiveDirectoryConfigurationTypeDef",
    "ComputeFarmConfigurationTypeDef",
    "CreateLaunchProfileRequestRequestTypeDef",
    "CreateLaunchProfileResponseTypeDef",
    "CreateStreamingImageRequestRequestTypeDef",
    "CreateStreamingImageResponseTypeDef",
    "CreateStreamingSessionRequestRequestTypeDef",
    "CreateStreamingSessionResponseTypeDef",
    "CreateStreamingSessionStreamRequestRequestTypeDef",
    "CreateStreamingSessionStreamResponseTypeDef",
    "CreateStudioComponentRequestRequestTypeDef",
    "CreateStudioComponentResponseTypeDef",
    "CreateStudioRequestRequestTypeDef",
    "CreateStudioResponseTypeDef",
    "DeleteLaunchProfileMemberRequestRequestTypeDef",
    "DeleteLaunchProfileRequestRequestTypeDef",
    "DeleteLaunchProfileResponseTypeDef",
    "DeleteStreamingImageRequestRequestTypeDef",
    "DeleteStreamingImageResponseTypeDef",
    "DeleteStreamingSessionRequestRequestTypeDef",
    "DeleteStreamingSessionResponseTypeDef",
    "DeleteStudioComponentRequestRequestTypeDef",
    "DeleteStudioComponentResponseTypeDef",
    "DeleteStudioMemberRequestRequestTypeDef",
    "DeleteStudioRequestRequestTypeDef",
    "DeleteStudioResponseTypeDef",
    "EulaAcceptanceTypeDef",
    "EulaTypeDef",
    "GetEulaRequestRequestTypeDef",
    "GetEulaResponseTypeDef",
    "GetLaunchProfileDetailsRequestRequestTypeDef",
    "GetLaunchProfileDetailsResponseTypeDef",
    "GetLaunchProfileInitializationRequestRequestTypeDef",
    "GetLaunchProfileInitializationResponseTypeDef",
    "GetLaunchProfileMemberRequestRequestTypeDef",
    "GetLaunchProfileMemberResponseTypeDef",
    "GetLaunchProfileRequestRequestTypeDef",
    "GetLaunchProfileResponseTypeDef",
    "GetStreamingImageRequestRequestTypeDef",
    "GetStreamingImageResponseTypeDef",
    "GetStreamingSessionRequestRequestTypeDef",
    "GetStreamingSessionResponseTypeDef",
    "GetStreamingSessionStreamRequestRequestTypeDef",
    "GetStreamingSessionStreamResponseTypeDef",
    "GetStudioComponentRequestRequestTypeDef",
    "GetStudioComponentResponseTypeDef",
    "GetStudioMemberRequestRequestTypeDef",
    "GetStudioMemberResponseTypeDef",
    "GetStudioRequestRequestTypeDef",
    "GetStudioResponseTypeDef",
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    "LaunchProfileInitializationScriptTypeDef",
    "LaunchProfileInitializationTypeDef",
    "LaunchProfileMembershipTypeDef",
    "LaunchProfileTypeDef",
    "LicenseServiceConfigurationTypeDef",
    "ListEulaAcceptancesRequestRequestTypeDef",
    "ListEulaAcceptancesResponseTypeDef",
    "ListEulasRequestRequestTypeDef",
    "ListEulasResponseTypeDef",
    "ListLaunchProfileMembersRequestRequestTypeDef",
    "ListLaunchProfileMembersResponseTypeDef",
    "ListLaunchProfilesRequestRequestTypeDef",
    "ListLaunchProfilesResponseTypeDef",
    "ListStreamingImagesRequestRequestTypeDef",
    "ListStreamingImagesResponseTypeDef",
    "ListStreamingSessionsRequestRequestTypeDef",
    "ListStreamingSessionsResponseTypeDef",
    "ListStudioComponentsRequestRequestTypeDef",
    "ListStudioComponentsResponseTypeDef",
    "ListStudioMembersRequestRequestTypeDef",
    "ListStudioMembersResponseTypeDef",
    "ListStudiosRequestRequestTypeDef",
    "ListStudiosResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NewLaunchProfileMemberTypeDef",
    "NewStudioMemberTypeDef",
    "PaginatorConfigTypeDef",
    "PutLaunchProfileMembersRequestRequestTypeDef",
    "PutStudioMembersRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScriptParameterKeyValueTypeDef",
    "SharedFileSystemConfigurationTypeDef",
    "StartStudioSSOConfigurationRepairRequestRequestTypeDef",
    "StartStudioSSOConfigurationRepairResponseTypeDef",
    "StreamConfigurationCreateTypeDef",
    "StreamConfigurationTypeDef",
    "StreamingImageEncryptionConfigurationTypeDef",
    "StreamingImageTypeDef",
    "StreamingSessionStreamTypeDef",
    "StreamingSessionTypeDef",
    "StudioComponentConfigurationTypeDef",
    "StudioComponentInitializationScriptTypeDef",
    "StudioComponentSummaryTypeDef",
    "StudioComponentTypeDef",
    "StudioEncryptionConfigurationTypeDef",
    "StudioMembershipTypeDef",
    "StudioTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLaunchProfileMemberRequestRequestTypeDef",
    "UpdateLaunchProfileMemberResponseTypeDef",
    "UpdateLaunchProfileRequestRequestTypeDef",
    "UpdateLaunchProfileResponseTypeDef",
    "UpdateStreamingImageRequestRequestTypeDef",
    "UpdateStreamingImageResponseTypeDef",
    "UpdateStudioComponentRequestRequestTypeDef",
    "UpdateStudioComponentResponseTypeDef",
    "UpdateStudioRequestRequestTypeDef",
    "UpdateStudioResponseTypeDef",
)

_RequiredAcceptEulasRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptEulasRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalAcceptEulasRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptEulasRequestRequestTypeDef",
    {
        "clientToken": str,
        "eulaIds": List[str],
    },
    total=False,
)

class AcceptEulasRequestRequestTypeDef(
    _RequiredAcceptEulasRequestRequestTypeDef, _OptionalAcceptEulasRequestRequestTypeDef
):
    pass

AcceptEulasResponseTypeDef = TypedDict(
    "AcceptEulasResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActiveDirectoryComputerAttributeTypeDef = TypedDict(
    "ActiveDirectoryComputerAttributeTypeDef",
    {
        "name": str,
        "value": str,
    },
    total=False,
)

ActiveDirectoryConfigurationTypeDef = TypedDict(
    "ActiveDirectoryConfigurationTypeDef",
    {
        "computerAttributes": List["ActiveDirectoryComputerAttributeTypeDef"],
        "directoryId": str,
        "organizationalUnitDistinguishedName": str,
    },
    total=False,
)

ComputeFarmConfigurationTypeDef = TypedDict(
    "ComputeFarmConfigurationTypeDef",
    {
        "activeDirectoryUser": str,
        "endpoint": str,
    },
    total=False,
)

_RequiredCreateLaunchProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchProfileRequestRequestTypeDef",
    {
        "ec2SubnetIds": List[str],
        "launchProfileProtocolVersions": List[str],
        "name": str,
        "streamConfiguration": "StreamConfigurationCreateTypeDef",
        "studioComponentIds": List[str],
        "studioId": str,
    },
)
_OptionalCreateLaunchProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchProfileRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLaunchProfileRequestRequestTypeDef(
    _RequiredCreateLaunchProfileRequestRequestTypeDef,
    _OptionalCreateLaunchProfileRequestRequestTypeDef,
):
    pass

CreateLaunchProfileResponseTypeDef = TypedDict(
    "CreateLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingImageRequestRequestTypeDef",
    {
        "ec2ImageId": str,
        "name": str,
        "studioId": str,
    },
)
_OptionalCreateStreamingImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingImageRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStreamingImageRequestRequestTypeDef(
    _RequiredCreateStreamingImageRequestRequestTypeDef,
    _OptionalCreateStreamingImageRequestRequestTypeDef,
):
    pass

CreateStreamingImageResponseTypeDef = TypedDict(
    "CreateStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingSessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingSessionRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalCreateStreamingSessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingSessionRequestRequestTypeDef",
    {
        "clientToken": str,
        "ec2InstanceType": StreamingInstanceTypeType,
        "launchProfileId": str,
        "streamingImageId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStreamingSessionRequestRequestTypeDef(
    _RequiredCreateStreamingSessionRequestRequestTypeDef,
    _OptionalCreateStreamingSessionRequestRequestTypeDef,
):
    pass

CreateStreamingSessionResponseTypeDef = TypedDict(
    "CreateStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamingSessionStreamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamingSessionStreamRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)
_OptionalCreateStreamingSessionStreamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamingSessionStreamRequestRequestTypeDef",
    {
        "clientToken": str,
        "expirationInSeconds": int,
    },
    total=False,
)

class CreateStreamingSessionStreamRequestRequestTypeDef(
    _RequiredCreateStreamingSessionStreamRequestRequestTypeDef,
    _OptionalCreateStreamingSessionStreamRequestRequestTypeDef,
):
    pass

CreateStreamingSessionStreamResponseTypeDef = TypedDict(
    "CreateStreamingSessionStreamResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStudioComponentRequestRequestTypeDef",
    {
        "name": str,
        "studioId": str,
        "type": StudioComponentTypeType,
    },
)
_OptionalCreateStudioComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStudioComponentRequestRequestTypeDef",
    {
        "clientToken": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "subtype": StudioComponentSubtypeType,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStudioComponentRequestRequestTypeDef(
    _RequiredCreateStudioComponentRequestRequestTypeDef,
    _OptionalCreateStudioComponentRequestRequestTypeDef,
):
    pass

CreateStudioComponentResponseTypeDef = TypedDict(
    "CreateStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStudioRequestRequestTypeDef",
    {
        "adminRoleArn": str,
        "displayName": str,
        "studioName": str,
        "userRoleArn": str,
    },
)
_OptionalCreateStudioRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStudioRequestRequestTypeDef",
    {
        "clientToken": str,
        "studioEncryptionConfiguration": "StudioEncryptionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStudioRequestRequestTypeDef(
    _RequiredCreateStudioRequestRequestTypeDef, _OptionalCreateStudioRequestRequestTypeDef
):
    pass

CreateStudioResponseTypeDef = TypedDict(
    "CreateStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLaunchProfileMemberRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "principalId": str,
        "studioId": str,
    },
)
_OptionalDeleteLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLaunchProfileMemberRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteLaunchProfileMemberRequestRequestTypeDef(
    _RequiredDeleteLaunchProfileMemberRequestRequestTypeDef,
    _OptionalDeleteLaunchProfileMemberRequestRequestTypeDef,
):
    pass

_RequiredDeleteLaunchProfileRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLaunchProfileRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)
_OptionalDeleteLaunchProfileRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLaunchProfileRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteLaunchProfileRequestRequestTypeDef(
    _RequiredDeleteLaunchProfileRequestRequestTypeDef,
    _OptionalDeleteLaunchProfileRequestRequestTypeDef,
):
    pass

DeleteLaunchProfileResponseTypeDef = TypedDict(
    "DeleteLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStreamingImageRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamingImageRequestRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)
_OptionalDeleteStreamingImageRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamingImageRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteStreamingImageRequestRequestTypeDef(
    _RequiredDeleteStreamingImageRequestRequestTypeDef,
    _OptionalDeleteStreamingImageRequestRequestTypeDef,
):
    pass

DeleteStreamingImageResponseTypeDef = TypedDict(
    "DeleteStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStreamingSessionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamingSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)
_OptionalDeleteStreamingSessionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamingSessionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteStreamingSessionRequestRequestTypeDef(
    _RequiredDeleteStreamingSessionRequestRequestTypeDef,
    _OptionalDeleteStreamingSessionRequestRequestTypeDef,
):
    pass

DeleteStreamingSessionResponseTypeDef = TypedDict(
    "DeleteStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStudioComponentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioComponentRequestRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)
_OptionalDeleteStudioComponentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteStudioComponentRequestRequestTypeDef(
    _RequiredDeleteStudioComponentRequestRequestTypeDef,
    _OptionalDeleteStudioComponentRequestRequestTypeDef,
):
    pass

DeleteStudioComponentResponseTypeDef = TypedDict(
    "DeleteStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteStudioMemberRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioMemberRequestRequestTypeDef",
    {
        "principalId": str,
        "studioId": str,
    },
)
_OptionalDeleteStudioMemberRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioMemberRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteStudioMemberRequestRequestTypeDef(
    _RequiredDeleteStudioMemberRequestRequestTypeDef,
    _OptionalDeleteStudioMemberRequestRequestTypeDef,
):
    pass

_RequiredDeleteStudioRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalDeleteStudioRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteStudioRequestRequestTypeDef(
    _RequiredDeleteStudioRequestRequestTypeDef, _OptionalDeleteStudioRequestRequestTypeDef
):
    pass

DeleteStudioResponseTypeDef = TypedDict(
    "DeleteStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EulaAcceptanceTypeDef = TypedDict(
    "EulaAcceptanceTypeDef",
    {
        "acceptedAt": datetime,
        "acceptedBy": str,
        "accepteeId": str,
        "eulaAcceptanceId": str,
        "eulaId": str,
    },
    total=False,
)

EulaTypeDef = TypedDict(
    "EulaTypeDef",
    {
        "content": str,
        "createdAt": datetime,
        "eulaId": str,
        "name": str,
        "updatedAt": datetime,
    },
    total=False,
)

GetEulaRequestRequestTypeDef = TypedDict(
    "GetEulaRequestRequestTypeDef",
    {
        "eulaId": str,
    },
)

GetEulaResponseTypeDef = TypedDict(
    "GetEulaResponseTypeDef",
    {
        "eula": "EulaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileDetailsRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileDetailsRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)

GetLaunchProfileDetailsResponseTypeDef = TypedDict(
    "GetLaunchProfileDetailsResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "streamingImages": List["StreamingImageTypeDef"],
        "studioComponentSummaries": List["StudioComponentSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileInitializationRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileInitializationRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "launchProfileProtocolVersions": List[str],
        "launchPurpose": str,
        "platform": str,
        "studioId": str,
    },
)

GetLaunchProfileInitializationResponseTypeDef = TypedDict(
    "GetLaunchProfileInitializationResponseTypeDef",
    {
        "launchProfileInitialization": "LaunchProfileInitializationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileMemberRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "principalId": str,
        "studioId": str,
    },
)

GetLaunchProfileMemberResponseTypeDef = TypedDict(
    "GetLaunchProfileMemberResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLaunchProfileRequestRequestTypeDef = TypedDict(
    "GetLaunchProfileRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)

GetLaunchProfileResponseTypeDef = TypedDict(
    "GetLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingImageRequestRequestTypeDef = TypedDict(
    "GetStreamingImageRequestRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)

GetStreamingImageResponseTypeDef = TypedDict(
    "GetStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingSessionRequestRequestTypeDef = TypedDict(
    "GetStreamingSessionRequestRequestTypeDef",
    {
        "sessionId": str,
        "studioId": str,
    },
)

GetStreamingSessionResponseTypeDef = TypedDict(
    "GetStreamingSessionResponseTypeDef",
    {
        "session": "StreamingSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamingSessionStreamRequestRequestTypeDef = TypedDict(
    "GetStreamingSessionStreamRequestRequestTypeDef",
    {
        "sessionId": str,
        "streamId": str,
        "studioId": str,
    },
)

GetStreamingSessionStreamResponseTypeDef = TypedDict(
    "GetStreamingSessionStreamResponseTypeDef",
    {
        "stream": "StreamingSessionStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioComponentRequestRequestTypeDef = TypedDict(
    "GetStudioComponentRequestRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)

GetStudioComponentResponseTypeDef = TypedDict(
    "GetStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioMemberRequestRequestTypeDef = TypedDict(
    "GetStudioMemberRequestRequestTypeDef",
    {
        "principalId": str,
        "studioId": str,
    },
)

GetStudioMemberResponseTypeDef = TypedDict(
    "GetStudioMemberResponseTypeDef",
    {
        "member": "StudioMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStudioRequestRequestTypeDef = TypedDict(
    "GetStudioRequestRequestTypeDef",
    {
        "studioId": str,
    },
)

GetStudioResponseTypeDef = TypedDict(
    "GetStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LaunchProfileInitializationActiveDirectoryTypeDef = TypedDict(
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    {
        "computerAttributes": List["ActiveDirectoryComputerAttributeTypeDef"],
        "directoryId": str,
        "directoryName": str,
        "dnsIpAddresses": List[str],
        "organizationalUnitDistinguishedName": str,
        "studioComponentId": str,
        "studioComponentName": str,
    },
    total=False,
)

LaunchProfileInitializationScriptTypeDef = TypedDict(
    "LaunchProfileInitializationScriptTypeDef",
    {
        "script": str,
        "studioComponentId": str,
        "studioComponentName": str,
    },
    total=False,
)

LaunchProfileInitializationTypeDef = TypedDict(
    "LaunchProfileInitializationTypeDef",
    {
        "activeDirectory": "LaunchProfileInitializationActiveDirectoryTypeDef",
        "ec2SecurityGroupIds": List[str],
        "launchProfileId": str,
        "launchProfileProtocolVersion": str,
        "launchPurpose": str,
        "name": str,
        "platform": LaunchProfilePlatformType,
        "systemInitializationScripts": List["LaunchProfileInitializationScriptTypeDef"],
        "userInitializationScripts": List["LaunchProfileInitializationScriptTypeDef"],
    },
    total=False,
)

LaunchProfileMembershipTypeDef = TypedDict(
    "LaunchProfileMembershipTypeDef",
    {
        "identityStoreId": str,
        "persona": Literal["USER"],
        "principalId": str,
    },
    total=False,
)

LaunchProfileTypeDef = TypedDict(
    "LaunchProfileTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "ec2SubnetIds": List[str],
        "launchProfileId": str,
        "launchProfileProtocolVersions": List[str],
        "name": str,
        "state": LaunchProfileStateType,
        "statusCode": LaunchProfileStatusCodeType,
        "statusMessage": str,
        "streamConfiguration": "StreamConfigurationTypeDef",
        "studioComponentIds": List[str],
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

LicenseServiceConfigurationTypeDef = TypedDict(
    "LicenseServiceConfigurationTypeDef",
    {
        "endpoint": str,
    },
    total=False,
)

_RequiredListEulaAcceptancesRequestRequestTypeDef = TypedDict(
    "_RequiredListEulaAcceptancesRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListEulaAcceptancesRequestRequestTypeDef = TypedDict(
    "_OptionalListEulaAcceptancesRequestRequestTypeDef",
    {
        "eulaIds": List[str],
        "nextToken": str,
    },
    total=False,
)

class ListEulaAcceptancesRequestRequestTypeDef(
    _RequiredListEulaAcceptancesRequestRequestTypeDef,
    _OptionalListEulaAcceptancesRequestRequestTypeDef,
):
    pass

ListEulaAcceptancesResponseTypeDef = TypedDict(
    "ListEulaAcceptancesResponseTypeDef",
    {
        "eulaAcceptances": List["EulaAcceptanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEulasRequestRequestTypeDef = TypedDict(
    "ListEulasRequestRequestTypeDef",
    {
        "eulaIds": List[str],
        "nextToken": str,
    },
    total=False,
)

ListEulasResponseTypeDef = TypedDict(
    "ListEulasResponseTypeDef",
    {
        "eulas": List["EulaTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchProfileMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListLaunchProfileMembersRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)
_OptionalListLaunchProfileMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListLaunchProfileMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListLaunchProfileMembersRequestRequestTypeDef(
    _RequiredListLaunchProfileMembersRequestRequestTypeDef,
    _OptionalListLaunchProfileMembersRequestRequestTypeDef,
):
    pass

ListLaunchProfileMembersResponseTypeDef = TypedDict(
    "ListLaunchProfileMembersResponseTypeDef",
    {
        "members": List["LaunchProfileMembershipTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLaunchProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListLaunchProfilesRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListLaunchProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListLaunchProfilesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "principalId": str,
        "states": List[str],
    },
    total=False,
)

class ListLaunchProfilesRequestRequestTypeDef(
    _RequiredListLaunchProfilesRequestRequestTypeDef,
    _OptionalListLaunchProfilesRequestRequestTypeDef,
):
    pass

ListLaunchProfilesResponseTypeDef = TypedDict(
    "ListLaunchProfilesResponseTypeDef",
    {
        "launchProfiles": List["LaunchProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamingImagesRequestRequestTypeDef = TypedDict(
    "_RequiredListStreamingImagesRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStreamingImagesRequestRequestTypeDef = TypedDict(
    "_OptionalListStreamingImagesRequestRequestTypeDef",
    {
        "nextToken": str,
        "owner": str,
    },
    total=False,
)

class ListStreamingImagesRequestRequestTypeDef(
    _RequiredListStreamingImagesRequestRequestTypeDef,
    _OptionalListStreamingImagesRequestRequestTypeDef,
):
    pass

ListStreamingImagesResponseTypeDef = TypedDict(
    "ListStreamingImagesResponseTypeDef",
    {
        "nextToken": str,
        "streamingImages": List["StreamingImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamingSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListStreamingSessionsRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStreamingSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListStreamingSessionsRequestRequestTypeDef",
    {
        "createdBy": str,
        "nextToken": str,
        "sessionIds": str,
    },
    total=False,
)

class ListStreamingSessionsRequestRequestTypeDef(
    _RequiredListStreamingSessionsRequestRequestTypeDef,
    _OptionalListStreamingSessionsRequestRequestTypeDef,
):
    pass

ListStreamingSessionsResponseTypeDef = TypedDict(
    "ListStreamingSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List["StreamingSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStudioComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListStudioComponentsRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStudioComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListStudioComponentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "states": List[str],
        "types": List[str],
    },
    total=False,
)

class ListStudioComponentsRequestRequestTypeDef(
    _RequiredListStudioComponentsRequestRequestTypeDef,
    _OptionalListStudioComponentsRequestRequestTypeDef,
):
    pass

ListStudioComponentsResponseTypeDef = TypedDict(
    "ListStudioComponentsResponseTypeDef",
    {
        "nextToken": str,
        "studioComponents": List["StudioComponentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStudioMembersRequestRequestTypeDef = TypedDict(
    "_RequiredListStudioMembersRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalListStudioMembersRequestRequestTypeDef = TypedDict(
    "_OptionalListStudioMembersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStudioMembersRequestRequestTypeDef(
    _RequiredListStudioMembersRequestRequestTypeDef, _OptionalListStudioMembersRequestRequestTypeDef
):
    pass

ListStudioMembersResponseTypeDef = TypedDict(
    "ListStudioMembersResponseTypeDef",
    {
        "members": List["StudioMembershipTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudiosRequestRequestTypeDef = TypedDict(
    "ListStudiosRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListStudiosResponseTypeDef = TypedDict(
    "ListStudiosResponseTypeDef",
    {
        "nextToken": str,
        "studios": List["StudioTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NewLaunchProfileMemberTypeDef = TypedDict(
    "NewLaunchProfileMemberTypeDef",
    {
        "persona": Literal["USER"],
        "principalId": str,
    },
)

NewStudioMemberTypeDef = TypedDict(
    "NewStudioMemberTypeDef",
    {
        "persona": Literal["ADMINISTRATOR"],
        "principalId": str,
    },
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

_RequiredPutLaunchProfileMembersRequestRequestTypeDef = TypedDict(
    "_RequiredPutLaunchProfileMembersRequestRequestTypeDef",
    {
        "identityStoreId": str,
        "launchProfileId": str,
        "members": List["NewLaunchProfileMemberTypeDef"],
        "studioId": str,
    },
)
_OptionalPutLaunchProfileMembersRequestRequestTypeDef = TypedDict(
    "_OptionalPutLaunchProfileMembersRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class PutLaunchProfileMembersRequestRequestTypeDef(
    _RequiredPutLaunchProfileMembersRequestRequestTypeDef,
    _OptionalPutLaunchProfileMembersRequestRequestTypeDef,
):
    pass

_RequiredPutStudioMembersRequestRequestTypeDef = TypedDict(
    "_RequiredPutStudioMembersRequestRequestTypeDef",
    {
        "identityStoreId": str,
        "members": List["NewStudioMemberTypeDef"],
        "studioId": str,
    },
)
_OptionalPutStudioMembersRequestRequestTypeDef = TypedDict(
    "_OptionalPutStudioMembersRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class PutStudioMembersRequestRequestTypeDef(
    _RequiredPutStudioMembersRequestRequestTypeDef, _OptionalPutStudioMembersRequestRequestTypeDef
):
    pass

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

ScriptParameterKeyValueTypeDef = TypedDict(
    "ScriptParameterKeyValueTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

SharedFileSystemConfigurationTypeDef = TypedDict(
    "SharedFileSystemConfigurationTypeDef",
    {
        "endpoint": str,
        "fileSystemId": str,
        "linuxMountPoint": str,
        "shareName": str,
        "windowsMountDrive": str,
    },
    total=False,
)

_RequiredStartStudioSSOConfigurationRepairRequestRequestTypeDef = TypedDict(
    "_RequiredStartStudioSSOConfigurationRepairRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalStartStudioSSOConfigurationRepairRequestRequestTypeDef = TypedDict(
    "_OptionalStartStudioSSOConfigurationRepairRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartStudioSSOConfigurationRepairRequestRequestTypeDef(
    _RequiredStartStudioSSOConfigurationRepairRequestRequestTypeDef,
    _OptionalStartStudioSSOConfigurationRepairRequestRequestTypeDef,
):
    pass

StartStudioSSOConfigurationRepairResponseTypeDef = TypedDict(
    "StartStudioSSOConfigurationRepairResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStreamConfigurationCreateTypeDef = TypedDict(
    "_RequiredStreamConfigurationCreateTypeDef",
    {
        "clipboardMode": StreamingClipboardModeType,
        "ec2InstanceTypes": List[StreamingInstanceTypeType],
        "streamingImageIds": List[str],
    },
)
_OptionalStreamConfigurationCreateTypeDef = TypedDict(
    "_OptionalStreamConfigurationCreateTypeDef",
    {
        "maxSessionLengthInMinutes": int,
    },
    total=False,
)

class StreamConfigurationCreateTypeDef(
    _RequiredStreamConfigurationCreateTypeDef, _OptionalStreamConfigurationCreateTypeDef
):
    pass

StreamConfigurationTypeDef = TypedDict(
    "StreamConfigurationTypeDef",
    {
        "clipboardMode": StreamingClipboardModeType,
        "ec2InstanceTypes": List[StreamingInstanceTypeType],
        "maxSessionLengthInMinutes": int,
        "streamingImageIds": List[str],
    },
    total=False,
)

_RequiredStreamingImageEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredStreamingImageEncryptionConfigurationTypeDef",
    {
        "keyType": Literal["CUSTOMER_MANAGED_KEY"],
    },
)
_OptionalStreamingImageEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalStreamingImageEncryptionConfigurationTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)

class StreamingImageEncryptionConfigurationTypeDef(
    _RequiredStreamingImageEncryptionConfigurationTypeDef,
    _OptionalStreamingImageEncryptionConfigurationTypeDef,
):
    pass

StreamingImageTypeDef = TypedDict(
    "StreamingImageTypeDef",
    {
        "arn": str,
        "description": str,
        "ec2ImageId": str,
        "encryptionConfiguration": "StreamingImageEncryptionConfigurationTypeDef",
        "eulaIds": List[str],
        "name": str,
        "owner": str,
        "platform": str,
        "state": StreamingImageStateType,
        "statusCode": StreamingImageStatusCodeType,
        "statusMessage": str,
        "streamingImageId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

StreamingSessionStreamTypeDef = TypedDict(
    "StreamingSessionStreamTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "expiresAt": datetime,
        "state": StreamingSessionStreamStateType,
        "statusCode": StreamingSessionStreamStatusCodeType,
        "streamId": str,
        "url": str,
    },
    total=False,
)

StreamingSessionTypeDef = TypedDict(
    "StreamingSessionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "ec2InstanceType": str,
        "launchProfileId": str,
        "sessionId": str,
        "state": StreamingSessionStateType,
        "statusCode": StreamingSessionStatusCodeType,
        "statusMessage": str,
        "streamingImageId": str,
        "tags": Dict[str, str],
        "terminateAt": datetime,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

StudioComponentConfigurationTypeDef = TypedDict(
    "StudioComponentConfigurationTypeDef",
    {
        "activeDirectoryConfiguration": "ActiveDirectoryConfigurationTypeDef",
        "computeFarmConfiguration": "ComputeFarmConfigurationTypeDef",
        "licenseServiceConfiguration": "LicenseServiceConfigurationTypeDef",
        "sharedFileSystemConfiguration": "SharedFileSystemConfigurationTypeDef",
    },
    total=False,
)

StudioComponentInitializationScriptTypeDef = TypedDict(
    "StudioComponentInitializationScriptTypeDef",
    {
        "launchProfileProtocolVersion": str,
        "platform": LaunchProfilePlatformType,
        "runContext": StudioComponentInitializationScriptRunContextType,
        "script": str,
    },
    total=False,
)

StudioComponentSummaryTypeDef = TypedDict(
    "StudioComponentSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "name": str,
        "studioComponentId": str,
        "subtype": StudioComponentSubtypeType,
        "type": StudioComponentTypeType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

StudioComponentTypeDef = TypedDict(
    "StudioComponentTypeDef",
    {
        "arn": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "name": str,
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "state": StudioComponentStateType,
        "statusCode": StudioComponentStatusCodeType,
        "statusMessage": str,
        "studioComponentId": str,
        "subtype": StudioComponentSubtypeType,
        "tags": Dict[str, str],
        "type": StudioComponentTypeType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

_RequiredStudioEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredStudioEncryptionConfigurationTypeDef",
    {
        "keyType": StudioEncryptionConfigurationKeyTypeType,
    },
)
_OptionalStudioEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalStudioEncryptionConfigurationTypeDef",
    {
        "keyArn": str,
    },
    total=False,
)

class StudioEncryptionConfigurationTypeDef(
    _RequiredStudioEncryptionConfigurationTypeDef, _OptionalStudioEncryptionConfigurationTypeDef
):
    pass

StudioMembershipTypeDef = TypedDict(
    "StudioMembershipTypeDef",
    {
        "identityStoreId": str,
        "persona": Literal["ADMINISTRATOR"],
        "principalId": str,
    },
    total=False,
)

StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "adminRoleArn": str,
        "arn": str,
        "createdAt": datetime,
        "displayName": str,
        "homeRegion": str,
        "ssoClientId": str,
        "state": StudioStateType,
        "statusCode": StudioStatusCodeType,
        "statusMessage": str,
        "studioEncryptionConfiguration": "StudioEncryptionConfigurationTypeDef",
        "studioId": str,
        "studioName": str,
        "studioUrl": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "userRoleArn": str,
    },
    total=False,
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchProfileMemberRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "persona": Literal["USER"],
        "principalId": str,
        "studioId": str,
    },
)
_OptionalUpdateLaunchProfileMemberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchProfileMemberRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateLaunchProfileMemberRequestRequestTypeDef(
    _RequiredUpdateLaunchProfileMemberRequestRequestTypeDef,
    _OptionalUpdateLaunchProfileMemberRequestRequestTypeDef,
):
    pass

UpdateLaunchProfileMemberResponseTypeDef = TypedDict(
    "UpdateLaunchProfileMemberResponseTypeDef",
    {
        "member": "LaunchProfileMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLaunchProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLaunchProfileRequestRequestTypeDef",
    {
        "launchProfileId": str,
        "studioId": str,
    },
)
_OptionalUpdateLaunchProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLaunchProfileRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "launchProfileProtocolVersions": List[str],
        "name": str,
        "streamConfiguration": "StreamConfigurationCreateTypeDef",
        "studioComponentIds": List[str],
    },
    total=False,
)

class UpdateLaunchProfileRequestRequestTypeDef(
    _RequiredUpdateLaunchProfileRequestRequestTypeDef,
    _OptionalUpdateLaunchProfileRequestRequestTypeDef,
):
    pass

UpdateLaunchProfileResponseTypeDef = TypedDict(
    "UpdateLaunchProfileResponseTypeDef",
    {
        "launchProfile": "LaunchProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStreamingImageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamingImageRequestRequestTypeDef",
    {
        "streamingImageId": str,
        "studioId": str,
    },
)
_OptionalUpdateStreamingImageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamingImageRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "name": str,
    },
    total=False,
)

class UpdateStreamingImageRequestRequestTypeDef(
    _RequiredUpdateStreamingImageRequestRequestTypeDef,
    _OptionalUpdateStreamingImageRequestRequestTypeDef,
):
    pass

UpdateStreamingImageResponseTypeDef = TypedDict(
    "UpdateStreamingImageResponseTypeDef",
    {
        "streamingImage": "StreamingImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStudioComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStudioComponentRequestRequestTypeDef",
    {
        "studioComponentId": str,
        "studioId": str,
    },
)
_OptionalUpdateStudioComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStudioComponentRequestRequestTypeDef",
    {
        "clientToken": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "name": str,
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "subtype": StudioComponentSubtypeType,
        "type": StudioComponentTypeType,
    },
    total=False,
)

class UpdateStudioComponentRequestRequestTypeDef(
    _RequiredUpdateStudioComponentRequestRequestTypeDef,
    _OptionalUpdateStudioComponentRequestRequestTypeDef,
):
    pass

UpdateStudioComponentResponseTypeDef = TypedDict(
    "UpdateStudioComponentResponseTypeDef",
    {
        "studioComponent": "StudioComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStudioRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStudioRequestRequestTypeDef",
    {
        "studioId": str,
    },
)
_OptionalUpdateStudioRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStudioRequestRequestTypeDef",
    {
        "adminRoleArn": str,
        "clientToken": str,
        "displayName": str,
        "userRoleArn": str,
    },
    total=False,
)

class UpdateStudioRequestRequestTypeDef(
    _RequiredUpdateStudioRequestRequestTypeDef, _OptionalUpdateStudioRequestRequestTypeDef
):
    pass

UpdateStudioResponseTypeDef = TypedDict(
    "UpdateStudioResponseTypeDef",
    {
        "studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
