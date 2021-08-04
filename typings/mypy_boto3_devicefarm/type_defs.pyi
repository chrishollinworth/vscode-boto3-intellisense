"""
Type annotations for devicefarm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devicefarm.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ArtifactCategoryType,
    ArtifactTypeType,
    BillingMethodType,
    DeviceAttributeType,
    DeviceAvailabilityType,
    DeviceFilterAttributeType,
    DeviceFormFactorType,
    DevicePlatformType,
    DevicePoolTypeType,
    ExecutionResultCodeType,
    ExecutionResultType,
    ExecutionStatusType,
    InstanceStatusType,
    InteractionModeType,
    NetworkProfileTypeType,
    OfferingTransactionTypeType,
    RuleOperatorType,
    SampleTypeType,
    TestGridSessionArtifactCategoryType,
    TestGridSessionArtifactTypeType,
    TestGridSessionStatusType,
    TestTypeType,
    UploadCategoryType,
    UploadStatusType,
    UploadTypeType,
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
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "CreateDevicePoolRequestRequestTypeDef",
    "CreateDevicePoolResultTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "CreateNetworkProfileRequestRequestTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResultTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "CreateTestGridProjectRequestRequestTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "CreateTestGridUrlRequestRequestTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "CreateUploadRequestRequestTypeDef",
    "CreateUploadResultTypeDef",
    "CreateVPCEConfigurationRequestRequestTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeleteDevicePoolRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteNetworkProfileRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteTestGridProjectRequestRequestTypeDef",
    "DeleteUploadRequestRequestTypeDef",
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "GetDeviceInstanceRequestRequestTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetDevicePoolRequestRequestTypeDef",
    "GetDevicePoolResultTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResultTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetInstanceProfileResultTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResultTypeDef",
    "GetNetworkProfileRequestRequestTypeDef",
    "GetNetworkProfileResultTypeDef",
    "GetOfferingStatusRequestRequestTypeDef",
    "GetOfferingStatusResultTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetProjectResultTypeDef",
    "GetRemoteAccessSessionRequestRequestTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "GetRunRequestRequestTypeDef",
    "GetRunResultTypeDef",
    "GetSuiteRequestRequestTypeDef",
    "GetSuiteResultTypeDef",
    "GetTestGridProjectRequestRequestTypeDef",
    "GetTestGridProjectResultTypeDef",
    "GetTestGridSessionRequestRequestTypeDef",
    "GetTestGridSessionResultTypeDef",
    "GetTestRequestRequestTypeDef",
    "GetTestResultTypeDef",
    "GetUploadRequestRequestTypeDef",
    "GetUploadResultTypeDef",
    "GetVPCEConfigurationRequestRequestTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListArtifactsResultTypeDef",
    "ListDeviceInstancesRequestRequestTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "ListDevicePoolsRequestRequestTypeDef",
    "ListDevicePoolsResultTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListNetworkProfilesRequestRequestTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "ListOfferingPromotionsRequestRequestTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListOfferingTransactionsRequestRequestTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResultTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResultTypeDef",
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "ListRunsRequestRequestTypeDef",
    "ListRunsResultTypeDef",
    "ListSamplesRequestRequestTypeDef",
    "ListSamplesResultTypeDef",
    "ListSuitesRequestRequestTypeDef",
    "ListSuitesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestGridProjectsRequestRequestTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "ListTestGridSessionActionsRequestRequestTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsRequestRequestTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListTestsRequestRequestTypeDef",
    "ListTestsResultTypeDef",
    "ListUniqueProblemsRequestRequestTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListUploadsRequestRequestTypeDef",
    "ListUploadsResultTypeDef",
    "ListVPCEConfigurationsRequestRequestTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "NetworkProfileTypeDef",
    "OfferingPromotionTypeDef",
    "OfferingStatusTypeDef",
    "OfferingTransactionTypeDef",
    "OfferingTypeDef",
    "PaginatorConfigTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "ProjectTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "RenewOfferingRequestRequestTypeDef",
    "RenewOfferingResultTypeDef",
    "ResolutionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunRequestRequestTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobRequestRequestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionRequestRequestTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunRequestRequestTypeDef",
    "StopRunResultTypeDef",
    "SuiteTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestGridVpcConfigTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceInstanceRequestRequestTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolRequestRequestTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileRequestRequestTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileRequestRequestTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectRequestRequestTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadRequestRequestTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": str,
        "unmeteredDevices": Dict[DevicePlatformType, int],
        "unmeteredRemoteAccessDevices": Dict[DevicePlatformType, int],
        "maxJobTimeoutMinutes": int,
        "trialMinutes": "TrialMinutesTypeDef",
        "maxSlots": Dict[str, int],
        "defaultJobTimeoutMinutes": int,
        "skipAppResign": bool,
    },
    total=False,
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ArtifactTypeType,
        "extension": str,
        "url": str,
    },
    total=False,
)

CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "frequency": str,
        "architecture": str,
        "clock": float,
    },
    total=False,
)

CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

_RequiredCreateDevicePoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDevicePoolRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "rules": List["RuleTypeDef"],
    },
)
_OptionalCreateDevicePoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDevicePoolRequestRequestTypeDef",
    {
        "description": str,
        "maxDevices": int,
    },
    total=False,
)

class CreateDevicePoolRequestRequestTypeDef(
    _RequiredCreateDevicePoolRequestRequestTypeDef, _OptionalCreateDevicePoolRequestRequestTypeDef
):
    pass

CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceProfileRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceProfileRequestRequestTypeDef",
    {
        "description": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
    },
    total=False,
)

class CreateInstanceProfileRequestRequestTypeDef(
    _RequiredCreateInstanceProfileRequestRequestTypeDef,
    _OptionalCreateInstanceProfileRequestRequestTypeDef,
):
    pass

CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkProfileRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
    },
)
_OptionalCreateNetworkProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkProfileRequestRequestTypeDef",
    {
        "description": str,
        "type": NetworkProfileTypeType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

class CreateNetworkProfileRequestRequestTypeDef(
    _RequiredCreateNetworkProfileRequestRequestTypeDef,
    _OptionalCreateNetworkProfileRequestRequestTypeDef,
):
    pass

CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "defaultJobTimeoutMinutes": int,
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {
        "billingMethod": BillingMethodType,
        "vpceConfigurationArns": List[str],
    },
    total=False,
)

_RequiredCreateRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRemoteAccessSessionRequestRequestTypeDef",
    {
        "projectArn": str,
        "deviceArn": str,
    },
)
_OptionalCreateRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRemoteAccessSessionRequestRequestTypeDef",
    {
        "instanceArn": str,
        "sshPublicKey": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "name": str,
        "clientId": str,
        "configuration": "CreateRemoteAccessSessionConfigurationTypeDef",
        "interactionMode": InteractionModeType,
        "skipAppResign": bool,
    },
    total=False,
)

class CreateRemoteAccessSessionRequestRequestTypeDef(
    _RequiredCreateRemoteAccessSessionRequestRequestTypeDef,
    _OptionalCreateRemoteAccessSessionRequestRequestTypeDef,
):
    pass

CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTestGridProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTestGridProjectRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateTestGridProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTestGridProjectRequestRequestTypeDef",
    {
        "description": str,
        "vpcConfig": "TestGridVpcConfigTypeDef",
    },
    total=False,
)

class CreateTestGridProjectRequestRequestTypeDef(
    _RequiredCreateTestGridProjectRequestRequestTypeDef,
    _OptionalCreateTestGridProjectRequestRequestTypeDef,
):
    pass

CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTestGridUrlRequestRequestTypeDef = TypedDict(
    "CreateTestGridUrlRequestRequestTypeDef",
    {
        "projectArn": str,
        "expiresInSeconds": int,
    },
)

CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef",
    {
        "url": str,
        "expires": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUploadRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "type": UploadTypeType,
    },
)
_OptionalCreateUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUploadRequestRequestTypeDef",
    {
        "contentType": str,
    },
    total=False,
)

class CreateUploadRequestRequestTypeDef(
    _RequiredCreateUploadRequestRequestTypeDef, _OptionalCreateUploadRequestRequestTypeDef
):
    pass

CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVPCEConfigurationRequestRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
    },
)
_OptionalCreateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVPCEConfigurationRequestRequestTypeDef",
    {
        "vpceConfigurationDescription": str,
    },
    total=False,
)

class CreateVPCEConfigurationRequestRequestTypeDef(
    _RequiredCreateVPCEConfigurationRequestRequestTypeDef,
    _OptionalCreateVPCEConfigurationRequestRequestTypeDef,
):
    pass

CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {
        "iosPaths": List[str],
        "androidPaths": List[str],
        "deviceHostPaths": List[str],
    },
    total=False,
)

DeleteDevicePoolRequestRequestTypeDef = TypedDict(
    "DeleteDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteNetworkProfileRequestRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRunRequestRequestTypeDef = TypedDict(
    "DeleteRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteTestGridProjectRequestRequestTypeDef = TypedDict(
    "DeleteTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)

DeleteUploadRequestRequestTypeDef = TypedDict(
    "DeleteUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": List[str],
    },
)

DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": InstanceStatusType,
        "udid": str,
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef",
    {
        "total": float,
        "metered": float,
        "unmetered": float,
    },
    total=False,
)

DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": "DeviceTypeDef",
        "compatible": bool,
        "incompatibilityMessages": List["IncompatibilityMessageTypeDef"],
    },
    total=False,
)

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": DevicePoolTypeType,
        "rules": List["RuleTypeDef"],
        "maxDevices": int,
    },
    total=False,
)

DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {
        "filters": List["DeviceFilterTypeDef"],
        "maxDevices": int,
    },
)

DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {
        "filters": List["DeviceFilterTypeDef"],
        "matchedDevicesCount": int,
        "maxDevices": int,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": DeviceFormFactorType,
        "platform": DevicePlatformType,
        "os": str,
        "cpu": "CPUTypeDef",
        "resolution": "ResolutionTypeDef",
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List["DeviceInstanceTypeDef"],
        "availability": DeviceAvailabilityType,
    },
    total=False,
)

ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": int,
        "accountsCleanup": bool,
        "appPackagesCleanup": bool,
        "videoCapture": bool,
        "skipAppResign": bool,
    },
    total=False,
)

GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceInstanceRequestRequestTypeDef = TypedDict(
    "GetDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDevicePoolCompatibilityRequestRequestTypeDef = TypedDict(
    "_RequiredGetDevicePoolCompatibilityRequestRequestTypeDef",
    {
        "devicePoolArn": str,
    },
)
_OptionalGetDevicePoolCompatibilityRequestRequestTypeDef = TypedDict(
    "_OptionalGetDevicePoolCompatibilityRequestRequestTypeDef",
    {
        "appArn": str,
        "testType": TestTypeType,
        "test": "ScheduleRunTestTypeDef",
        "configuration": "ScheduleRunConfigurationTypeDef",
    },
    total=False,
)

class GetDevicePoolCompatibilityRequestRequestTypeDef(
    _RequiredGetDevicePoolCompatibilityRequestRequestTypeDef,
    _OptionalGetDevicePoolCompatibilityRequestRequestTypeDef,
):
    pass

GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "incompatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicePoolRequestRequestTypeDef = TypedDict(
    "GetDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef",
    {
        "device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetJobResultTypeDef = TypedDict(
    "GetJobResultTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkProfileRequestRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOfferingStatusRequestRequestTypeDef = TypedDict(
    "GetOfferingStatusRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, "OfferingStatusTypeDef"],
        "nextPeriod": Dict[str, "OfferingStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "GetRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRunRequestRequestTypeDef = TypedDict(
    "GetRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetRunResultTypeDef = TypedDict(
    "GetRunResultTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRequestRequestTypeDef = TypedDict(
    "GetSuiteRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetSuiteResultTypeDef = TypedDict(
    "GetSuiteResultTypeDef",
    {
        "suite": "SuiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestGridProjectRequestRequestTypeDef = TypedDict(
    "GetTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)

GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestGridSessionRequestRequestTypeDef = TypedDict(
    "GetTestGridSessionRequestRequestTypeDef",
    {
        "projectArn": str,
        "sessionId": str,
        "sessionArn": str,
    },
    total=False,
)

GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef",
    {
        "testGridSession": "TestGridSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTestRequestRequestTypeDef = TypedDict(
    "GetTestRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetTestResultTypeDef = TypedDict(
    "GetTestResultTypeDef",
    {
        "test": "TestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUploadRequestRequestTypeDef = TypedDict(
    "GetUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "GetVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": str,
        "type": DeviceAttributeType,
    },
    total=False,
)

InstallToRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    {
        "remoteAccessSessionArn": str,
        "appArn": str,
    },
)

InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef",
    {
        "appUpload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

_RequiredListArtifactsRequestRequestTypeDef = TypedDict(
    "_RequiredListArtifactsRequestRequestTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
    },
)
_OptionalListArtifactsRequestRequestTypeDef = TypedDict(
    "_OptionalListArtifactsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListArtifactsRequestRequestTypeDef(
    _RequiredListArtifactsRequestRequestTypeDef, _OptionalListArtifactsRequestRequestTypeDef
):
    pass

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {
        "artifacts": List["ArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceInstancesRequestRequestTypeDef = TypedDict(
    "ListDeviceInstancesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {
        "deviceInstances": List["DeviceInstanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDevicePoolsRequestRequestTypeDef = TypedDict(
    "_RequiredListDevicePoolsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListDevicePoolsRequestRequestTypeDef = TypedDict(
    "_OptionalListDevicePoolsRequestRequestTypeDef",
    {
        "type": DevicePoolTypeType,
        "nextToken": str,
    },
    total=False,
)

class ListDevicePoolsRequestRequestTypeDef(
    _RequiredListDevicePoolsRequestRequestTypeDef, _OptionalListDevicePoolsRequestRequestTypeDef
):
    pass

ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {
        "devicePools": List["DevicePoolTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": str,
        "filters": List["DeviceFilterTypeDef"],
    },
    total=False,
)

ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef",
    {
        "devices": List["DeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {
        "instanceProfiles": List["InstanceProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListJobsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListJobsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListJobsRequestRequestTypeDef(
    _RequiredListJobsRequestRequestTypeDef, _OptionalListJobsRequestRequestTypeDef
):
    pass

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNetworkProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListNetworkProfilesRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListNetworkProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListNetworkProfilesRequestRequestTypeDef",
    {
        "type": NetworkProfileTypeType,
        "nextToken": str,
    },
    total=False,
)

class ListNetworkProfilesRequestRequestTypeDef(
    _RequiredListNetworkProfilesRequestRequestTypeDef,
    _OptionalListNetworkProfilesRequestRequestTypeDef,
):
    pass

ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {
        "networkProfiles": List["NetworkProfileTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingPromotionsRequestRequestTypeDef = TypedDict(
    "ListOfferingPromotionsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {
        "offeringPromotions": List["OfferingPromotionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingTransactionsRequestRequestTypeDef = TypedDict(
    "ListOfferingTransactionsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {
        "offeringTransactions": List["OfferingTransactionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {
        "offerings": List["OfferingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": str,
    },
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRemoteAccessSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListRemoteAccessSessionsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListRemoteAccessSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListRemoteAccessSessionsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListRemoteAccessSessionsRequestRequestTypeDef(
    _RequiredListRemoteAccessSessionsRequestRequestTypeDef,
    _OptionalListRemoteAccessSessionsRequestRequestTypeDef,
):
    pass

ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {
        "remoteAccessSessions": List["RemoteAccessSessionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListRunsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListRunsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListRunsRequestRequestTypeDef(
    _RequiredListRunsRequestRequestTypeDef, _OptionalListRunsRequestRequestTypeDef
):
    pass

ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef",
    {
        "runs": List["RunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSamplesRequestRequestTypeDef = TypedDict(
    "_RequiredListSamplesRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListSamplesRequestRequestTypeDef = TypedDict(
    "_OptionalListSamplesRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListSamplesRequestRequestTypeDef(
    _RequiredListSamplesRequestRequestTypeDef, _OptionalListSamplesRequestRequestTypeDef
):
    pass

ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef",
    {
        "samples": List["SampleTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSuitesRequestRequestTypeDef = TypedDict(
    "_RequiredListSuitesRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListSuitesRequestRequestTypeDef = TypedDict(
    "_OptionalListSuitesRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListSuitesRequestRequestTypeDef(
    _RequiredListSuitesRequestRequestTypeDef, _OptionalListSuitesRequestRequestTypeDef
):
    pass

ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef",
    {
        "suites": List["SuiteTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTestGridProjectsRequestRequestTypeDef = TypedDict(
    "ListTestGridProjectsRequestRequestTypeDef",
    {
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)

ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {
        "testGridProjects": List["TestGridProjectTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestGridSessionActionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestGridSessionActionsRequestRequestTypeDef",
    {
        "sessionArn": str,
    },
)
_OptionalListTestGridSessionActionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestGridSessionActionsRequestRequestTypeDef",
    {
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)

class ListTestGridSessionActionsRequestRequestTypeDef(
    _RequiredListTestGridSessionActionsRequestRequestTypeDef,
    _OptionalListTestGridSessionActionsRequestRequestTypeDef,
):
    pass

ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {
        "actions": List["TestGridSessionActionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestGridSessionArtifactsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestGridSessionArtifactsRequestRequestTypeDef",
    {
        "sessionArn": str,
    },
)
_OptionalListTestGridSessionArtifactsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestGridSessionArtifactsRequestRequestTypeDef",
    {
        "type": TestGridSessionArtifactCategoryType,
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)

class ListTestGridSessionArtifactsRequestRequestTypeDef(
    _RequiredListTestGridSessionArtifactsRequestRequestTypeDef,
    _OptionalListTestGridSessionArtifactsRequestRequestTypeDef,
):
    pass

ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {
        "artifacts": List["TestGridSessionArtifactTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestGridSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestGridSessionsRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)
_OptionalListTestGridSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestGridSessionsRequestRequestTypeDef",
    {
        "status": TestGridSessionStatusType,
        "creationTimeAfter": Union[datetime, str],
        "creationTimeBefore": Union[datetime, str],
        "endTimeAfter": Union[datetime, str],
        "endTimeBefore": Union[datetime, str],
        "maxResult": int,
        "nextToken": str,
    },
    total=False,
)

class ListTestGridSessionsRequestRequestTypeDef(
    _RequiredListTestGridSessionsRequestRequestTypeDef,
    _OptionalListTestGridSessionsRequestRequestTypeDef,
):
    pass

ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {
        "testGridSessions": List["TestGridSessionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListTestsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListTestsRequestRequestTypeDef(
    _RequiredListTestsRequestRequestTypeDef, _OptionalListTestsRequestRequestTypeDef
):
    pass

ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef",
    {
        "tests": List["TestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUniqueProblemsRequestRequestTypeDef = TypedDict(
    "_RequiredListUniqueProblemsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListUniqueProblemsRequestRequestTypeDef = TypedDict(
    "_OptionalListUniqueProblemsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListUniqueProblemsRequestRequestTypeDef(
    _RequiredListUniqueProblemsRequestRequestTypeDef,
    _OptionalListUniqueProblemsRequestRequestTypeDef,
):
    pass

ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[ExecutionResultType, List["UniqueProblemTypeDef"]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUploadsRequestRequestTypeDef = TypedDict(
    "_RequiredListUploadsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListUploadsRequestRequestTypeDef = TypedDict(
    "_OptionalListUploadsRequestRequestTypeDef",
    {
        "type": UploadTypeType,
        "nextToken": str,
    },
    total=False,
)

class ListUploadsRequestRequestTypeDef(
    _RequiredListUploadsRequestRequestTypeDef, _OptionalListUploadsRequestRequestTypeDef
):
    pass

ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef",
    {
        "uploads": List["UploadTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVPCEConfigurationsRequestRequestTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {
        "vpceConfigurations": List["VPCEConfigurationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "latitude": float,
        "longitude": float,
    },
)

MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef",
    {
        "amount": float,
        "currencyCode": Literal["USD"],
    },
    total=False,
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": NetworkProfileTypeType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef",
    {
        "id": str,
        "description": str,
    },
    total=False,
)

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": OfferingTransactionTypeType,
        "offering": "OfferingTypeDef",
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": "OfferingStatusTypeDef",
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": "MonetaryAmountTypeDef",
    },
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": Literal["RECURRING"],
        "platform": DevicePlatformType,
        "recurringCharges": List["RecurringChargeTypeDef"],
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

ProblemDetailTypeDef = TypedDict(
    "ProblemDetailTypeDef",
    {
        "arn": str,
        "name": str,
    },
    total=False,
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": "ProblemDetailTypeDef",
        "job": "ProblemDetailTypeDef",
        "suite": "ProblemDetailTypeDef",
        "test": "ProblemDetailTypeDef",
        "device": "DeviceTypeDef",
        "result": ExecutionResultType,
        "message": str,
    },
    total=False,
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": str,
        "name": str,
        "defaultJobTimeoutMinutes": int,
        "created": datetime,
    },
    total=False,
)

_RequiredPurchaseOfferingRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)
_OptionalPurchaseOfferingRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseOfferingRequestRequestTypeDef",
    {
        "offeringPromotionId": str,
    },
    total=False,
)

class PurchaseOfferingRequestRequestTypeDef(
    _RequiredPurchaseOfferingRequestRequestTypeDef, _OptionalPurchaseOfferingRequestRequestTypeDef
):
    pass

PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RadiosTypeDef = TypedDict(
    "RadiosTypeDef",
    {
        "wifi": bool,
        "bluetooth": bool,
        "nfc": bool,
        "gps": bool,
    },
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "cost": "MonetaryAmountTypeDef",
        "frequency": Literal["MONTHLY"],
    },
    total=False,
)

RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": BillingMethodType,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": InteractionModeType,
        "skipAppResign": bool,
    },
    total=False,
)

RenewOfferingRequestRequestTypeDef = TypedDict(
    "RenewOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)

RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef",
    {
        "offeringTransaction": "OfferingTransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolutionTypeDef = TypedDict(
    "ResolutionTypeDef",
    {
        "width": int,
        "height": int,
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

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": DeviceAttributeType,
        "operator": RuleOperatorType,
        "value": str,
    },
    total=False,
)

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "platform": DevicePlatformType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": BillingMethodType,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "networkProfile": "NetworkProfileTypeDef",
        "parsingResultUrl": str,
        "resultCode": ExecutionResultCodeType,
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": "RadiosTypeDef",
        "location": "LocationTypeDef",
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": "DeviceSelectionResultTypeDef",
    },
    total=False,
)

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": str,
        "type": SampleTypeType,
        "url": str,
    },
    total=False,
)

ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": "LocationTypeDef",
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "radios": "RadiosTypeDef",
        "auxiliaryApps": List[str],
        "billingMethod": BillingMethodType,
    },
    total=False,
)

_RequiredScheduleRunRequestRequestTypeDef = TypedDict(
    "_RequiredScheduleRunRequestRequestTypeDef",
    {
        "projectArn": str,
        "test": "ScheduleRunTestTypeDef",
    },
)
_OptionalScheduleRunRequestRequestTypeDef = TypedDict(
    "_OptionalScheduleRunRequestRequestTypeDef",
    {
        "appArn": str,
        "devicePoolArn": str,
        "deviceSelectionConfiguration": "DeviceSelectionConfigurationTypeDef",
        "name": str,
        "configuration": "ScheduleRunConfigurationTypeDef",
        "executionConfiguration": "ExecutionConfigurationTypeDef",
    },
    total=False,
)

class ScheduleRunRequestRequestTypeDef(
    _RequiredScheduleRunRequestRequestTypeDef, _OptionalScheduleRunRequestRequestTypeDef
):
    pass

ScheduleRunResultTypeDef = TypedDict(
    "ScheduleRunResultTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredScheduleRunTestTypeDef = TypedDict(
    "_RequiredScheduleRunTestTypeDef",
    {
        "type": TestTypeType,
    },
)
_OptionalScheduleRunTestTypeDef = TypedDict(
    "_OptionalScheduleRunTestTypeDef",
    {
        "testPackageArn": str,
        "testSpecArn": str,
        "filter": str,
        "parameters": Dict[str, str],
    },
    total=False,
)

class ScheduleRunTestTypeDef(_RequiredScheduleRunTestTypeDef, _OptionalScheduleRunTestTypeDef):
    pass

StopJobRequestRequestTypeDef = TypedDict(
    "StopJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)

StopJobResultTypeDef = TypedDict(
    "StopJobResultTypeDef",
    {
        "job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "StopRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": "RemoteAccessSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRunRequestRequestTypeDef = TypedDict(
    "StopRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)

StopRunResultTypeDef = TypedDict(
    "StopRunResultTypeDef",
    {
        "run": "RunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "vpcConfig": "TestGridVpcConfigTypeDef",
        "created": datetime,
    },
    total=False,
)

TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {
        "action": str,
        "started": datetime,
        "duration": int,
        "statusCode": str,
        "requestMethod": str,
    },
    total=False,
)

TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {
        "filename": str,
        "type": TestGridSessionArtifactTypeType,
        "url": str,
    },
    total=False,
)

TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": str,
        "status": TestGridSessionStatusType,
        "created": datetime,
        "ended": datetime,
        "billingMinutes": float,
        "seleniumProperties": str,
    },
    total=False,
)

TestGridVpcConfigTypeDef = TypedDict(
    "TestGridVpcConfigTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)

TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": TestTypeType,
        "created": datetime,
        "status": ExecutionStatusType,
        "result": ExecutionResultType,
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef",
    {
        "total": float,
        "remaining": float,
    },
    total=False,
)

UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef",
    {
        "message": str,
        "problems": List["ProblemTypeDef"],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDeviceInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateDeviceInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceInstanceRequestRequestTypeDef",
    {
        "profileArn": str,
        "labels": List[str],
    },
    total=False,
)

class UpdateDeviceInstanceRequestRequestTypeDef(
    _RequiredUpdateDeviceInstanceRequestRequestTypeDef,
    _OptionalUpdateDeviceInstanceRequestRequestTypeDef,
):
    pass

UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef",
    {
        "deviceInstance": "DeviceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDevicePoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateDevicePoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDevicePoolRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "rules": List["RuleTypeDef"],
        "maxDevices": int,
        "clearMaxDevices": bool,
    },
    total=False,
)

class UpdateDevicePoolRequestRequestTypeDef(
    _RequiredUpdateDevicePoolRequestRequestTypeDef, _OptionalUpdateDevicePoolRequestRequestTypeDef
):
    pass

UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef",
    {
        "devicePool": "DevicePoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInstanceProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateInstanceProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInstanceProfileRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
    },
    total=False,
)

class UpdateInstanceProfileRequestRequestTypeDef(
    _RequiredUpdateInstanceProfileRequestRequestTypeDef,
    _OptionalUpdateInstanceProfileRequestRequestTypeDef,
):
    pass

UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef",
    {
        "instanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNetworkProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateNetworkProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkProfileRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "type": NetworkProfileTypeType,
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

class UpdateNetworkProfileRequestRequestTypeDef(
    _RequiredUpdateNetworkProfileRequestRequestTypeDef,
    _OptionalUpdateNetworkProfileRequestRequestTypeDef,
):
    pass

UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef",
    {
        "networkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "name": str,
        "defaultJobTimeoutMinutes": int,
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "project": "ProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTestGridProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)
_OptionalUpdateTestGridProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTestGridProjectRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "vpcConfig": "TestGridVpcConfigTypeDef",
    },
    total=False,
)

class UpdateTestGridProjectRequestRequestTypeDef(
    _RequiredUpdateTestGridProjectRequestRequestTypeDef,
    _OptionalUpdateTestGridProjectRequestRequestTypeDef,
):
    pass

UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef",
    {
        "testGridProject": "TestGridProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUploadRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateUploadRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUploadRequestRequestTypeDef",
    {
        "name": str,
        "contentType": str,
        "editContent": bool,
    },
    total=False,
)

class UpdateUploadRequestRequestTypeDef(
    _RequiredUpdateUploadRequestRequestTypeDef, _OptionalUpdateUploadRequestRequestTypeDef
):
    pass

UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef",
    {
        "upload": "UploadTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVPCEConfigurationRequestRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

class UpdateVPCEConfigurationRequestRequestTypeDef(
    _RequiredUpdateVPCEConfigurationRequestRequestTypeDef,
    _OptionalUpdateVPCEConfigurationRequestRequestTypeDef,
):
    pass

UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": "VPCEConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": UploadTypeType,
        "status": UploadStatusType,
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": UploadCategoryType,
    },
    total=False,
)

VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)
