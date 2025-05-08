"""
Type annotations for devicefarm service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_devicefarm.type_defs import TrialMinutesTypeDef

    data: TrialMinutesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "CreateDevicePoolRequestTypeDef",
    "CreateDevicePoolResultTypeDef",
    "CreateInstanceProfileRequestTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "CreateNetworkProfileRequestTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResultTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionRequestTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "CreateTestGridProjectRequestTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "CreateTestGridUrlRequestTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "CreateUploadRequestTypeDef",
    "CreateUploadResultTypeDef",
    "CreateVPCEConfigurationRequestTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "CustomerArtifactPathsOutputTypeDef",
    "CustomerArtifactPathsTypeDef",
    "CustomerArtifactPathsUnionTypeDef",
    "DeleteDevicePoolRequestTypeDef",
    "DeleteInstanceProfileRequestTypeDef",
    "DeleteNetworkProfileRequestTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteRemoteAccessSessionRequestTypeDef",
    "DeleteRunRequestTypeDef",
    "DeleteTestGridProjectRequestTypeDef",
    "DeleteUploadRequestTypeDef",
    "DeleteVPCEConfigurationRequestTypeDef",
    "DeviceFilterOutputTypeDef",
    "DeviceFilterTypeDef",
    "DeviceFilterUnionTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceProxyTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "GetDeviceInstanceRequestTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "GetDevicePoolCompatibilityRequestTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetDevicePoolRequestTypeDef",
    "GetDevicePoolResultTypeDef",
    "GetDeviceRequestTypeDef",
    "GetDeviceResultTypeDef",
    "GetInstanceProfileRequestTypeDef",
    "GetInstanceProfileResultTypeDef",
    "GetJobRequestTypeDef",
    "GetJobResultTypeDef",
    "GetNetworkProfileRequestTypeDef",
    "GetNetworkProfileResultTypeDef",
    "GetOfferingStatusRequestPaginateTypeDef",
    "GetOfferingStatusRequestTypeDef",
    "GetOfferingStatusResultTypeDef",
    "GetProjectRequestTypeDef",
    "GetProjectResultTypeDef",
    "GetRemoteAccessSessionRequestTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "GetRunRequestTypeDef",
    "GetRunResultTypeDef",
    "GetSuiteRequestTypeDef",
    "GetSuiteResultTypeDef",
    "GetTestGridProjectRequestTypeDef",
    "GetTestGridProjectResultTypeDef",
    "GetTestGridSessionRequestTypeDef",
    "GetTestGridSessionResultTypeDef",
    "GetTestRequestTypeDef",
    "GetTestResultTypeDef",
    "GetUploadRequestTypeDef",
    "GetUploadResultTypeDef",
    "GetVPCEConfigurationRequestTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstallToRemoteAccessSessionRequestTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "ListArtifactsRequestPaginateTypeDef",
    "ListArtifactsRequestTypeDef",
    "ListArtifactsResultTypeDef",
    "ListDeviceInstancesRequestPaginateTypeDef",
    "ListDeviceInstancesRequestTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "ListDevicePoolsRequestPaginateTypeDef",
    "ListDevicePoolsRequestTypeDef",
    "ListDevicePoolsResultTypeDef",
    "ListDevicesRequestPaginateTypeDef",
    "ListDevicesRequestTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesRequestPaginateTypeDef",
    "ListInstanceProfilesRequestTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResultTypeDef",
    "ListNetworkProfilesRequestPaginateTypeDef",
    "ListNetworkProfilesRequestTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "ListOfferingPromotionsRequestPaginateTypeDef",
    "ListOfferingPromotionsRequestTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListOfferingTransactionsRequestPaginateTypeDef",
    "ListOfferingTransactionsRequestTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsRequestPaginateTypeDef",
    "ListOfferingsRequestTypeDef",
    "ListOfferingsResultTypeDef",
    "ListProjectsRequestPaginateTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResultTypeDef",
    "ListRemoteAccessSessionsRequestPaginateTypeDef",
    "ListRemoteAccessSessionsRequestTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "ListRunsRequestPaginateTypeDef",
    "ListRunsRequestTypeDef",
    "ListRunsResultTypeDef",
    "ListSamplesRequestPaginateTypeDef",
    "ListSamplesRequestTypeDef",
    "ListSamplesResultTypeDef",
    "ListSuitesRequestPaginateTypeDef",
    "ListSuitesRequestTypeDef",
    "ListSuitesResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestGridProjectsRequestTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "ListTestGridSessionActionsRequestTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsRequestTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsRequestTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListTestsRequestPaginateTypeDef",
    "ListTestsRequestTypeDef",
    "ListTestsResultTypeDef",
    "ListUniqueProblemsRequestPaginateTypeDef",
    "ListUniqueProblemsRequestTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListUploadsRequestPaginateTypeDef",
    "ListUploadsRequestTypeDef",
    "ListUploadsResultTypeDef",
    "ListVPCEConfigurationsRequestPaginateTypeDef",
    "ListVPCEConfigurationsRequestTypeDef",
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
    "PurchaseOfferingRequestTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "RenewOfferingRequestTypeDef",
    "RenewOfferingResultTypeDef",
    "ResolutionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunRequestTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobRequestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionRequestTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunRequestTypeDef",
    "StopRunResultTypeDef",
    "SuiteTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestGridVpcConfigOutputTypeDef",
    "TestGridVpcConfigTypeDef",
    "TestGridVpcConfigUnionTypeDef",
    "TestTypeDef",
    "TimestampTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDeviceInstanceRequestTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolRequestTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileRequestTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileRequestTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectRequestTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadRequestTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationRequestTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigTypeDef",
    "VpcConfigUnionTypeDef",
)

class TrialMinutesTypeDef(TypedDict):
    total: NotRequired[float]
    remaining: NotRequired[float]

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ArtifactTypeType],
        "extension": NotRequired[str],
        "url": NotRequired[str],
    },
)

class CPUTypeDef(TypedDict):
    frequency: NotRequired[str]
    architecture: NotRequired[str]
    clock: NotRequired[float]

class CountersTypeDef(TypedDict):
    total: NotRequired[int]
    passed: NotRequired[int]
    failed: NotRequired[int]
    warned: NotRequired[int]
    errored: NotRequired[int]
    stopped: NotRequired[int]
    skipped: NotRequired[int]

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": NotRequired[DeviceAttributeType],
        "operator": NotRequired[RuleOperatorType],
        "value": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateInstanceProfileRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    packageCleanup: NotRequired[bool]
    excludeAppPackagesFromCleanup: NotRequired[Sequence[str]]
    rebootAfterUse: NotRequired[bool]

class InstanceProfileTypeDef(TypedDict):
    arn: NotRequired[str]
    packageCleanup: NotRequired[bool]
    excludeAppPackagesFromCleanup: NotRequired[List[str]]
    rebootAfterUse: NotRequired[bool]
    name: NotRequired[str]
    description: NotRequired[str]

CreateNetworkProfileRequestTypeDef = TypedDict(
    "CreateNetworkProfileRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)

class DeviceProxyTypeDef(TypedDict):
    host: str
    port: int

class CreateTestGridUrlRequestTypeDef(TypedDict):
    projectArn: str
    expiresInSeconds: int

CreateUploadRequestTypeDef = TypedDict(
    "CreateUploadRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "type": UploadTypeType,
        "contentType": NotRequired[str],
    },
)
UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "type": NotRequired[UploadTypeType],
        "status": NotRequired[UploadStatusType],
        "url": NotRequired[str],
        "metadata": NotRequired[str],
        "contentType": NotRequired[str],
        "message": NotRequired[str],
        "category": NotRequired[UploadCategoryType],
    },
)

class CreateVPCEConfigurationRequestTypeDef(TypedDict):
    vpceConfigurationName: str
    vpceServiceName: str
    serviceDnsName: str
    vpceConfigurationDescription: NotRequired[str]

class VPCEConfigurationTypeDef(TypedDict):
    arn: NotRequired[str]
    vpceConfigurationName: NotRequired[str]
    vpceServiceName: NotRequired[str]
    serviceDnsName: NotRequired[str]
    vpceConfigurationDescription: NotRequired[str]

class CustomerArtifactPathsOutputTypeDef(TypedDict):
    iosPaths: NotRequired[List[str]]
    androidPaths: NotRequired[List[str]]
    deviceHostPaths: NotRequired[List[str]]

class CustomerArtifactPathsTypeDef(TypedDict):
    iosPaths: NotRequired[Sequence[str]]
    androidPaths: NotRequired[Sequence[str]]
    deviceHostPaths: NotRequired[Sequence[str]]

class DeleteDevicePoolRequestTypeDef(TypedDict):
    arn: str

class DeleteInstanceProfileRequestTypeDef(TypedDict):
    arn: str

class DeleteNetworkProfileRequestTypeDef(TypedDict):
    arn: str

class DeleteProjectRequestTypeDef(TypedDict):
    arn: str

class DeleteRemoteAccessSessionRequestTypeDef(TypedDict):
    arn: str

class DeleteRunRequestTypeDef(TypedDict):
    arn: str

class DeleteTestGridProjectRequestTypeDef(TypedDict):
    projectArn: str

class DeleteUploadRequestTypeDef(TypedDict):
    arn: str

class DeleteVPCEConfigurationRequestTypeDef(TypedDict):
    arn: str

DeviceFilterOutputTypeDef = TypedDict(
    "DeviceFilterOutputTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": List[str],
    },
)
DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": Sequence[str],
    },
)

class DeviceMinutesTypeDef(TypedDict):
    total: NotRequired[float]
    metered: NotRequired[float]
    unmetered: NotRequired[float]

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": NotRequired[str],
        "type": NotRequired[DeviceAttributeType],
    },
)

class ResolutionTypeDef(TypedDict):
    width: NotRequired[int]
    height: NotRequired[int]

class ExecutionConfigurationTypeDef(TypedDict):
    jobTimeoutMinutes: NotRequired[int]
    accountsCleanup: NotRequired[bool]
    appPackagesCleanup: NotRequired[bool]
    videoCapture: NotRequired[bool]
    skipAppResign: NotRequired[bool]

class GetDeviceInstanceRequestTypeDef(TypedDict):
    arn: str

ScheduleRunTestTypeDef = TypedDict(
    "ScheduleRunTestTypeDef",
    {
        "type": TestTypeType,
        "testPackageArn": NotRequired[str],
        "testSpecArn": NotRequired[str],
        "filter": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
    },
)

class GetDevicePoolRequestTypeDef(TypedDict):
    arn: str

class GetDeviceRequestTypeDef(TypedDict):
    arn: str

class GetInstanceProfileRequestTypeDef(TypedDict):
    arn: str

class GetJobRequestTypeDef(TypedDict):
    arn: str

class GetNetworkProfileRequestTypeDef(TypedDict):
    arn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetOfferingStatusRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class GetProjectRequestTypeDef(TypedDict):
    arn: str

class GetRemoteAccessSessionRequestTypeDef(TypedDict):
    arn: str

class GetRunRequestTypeDef(TypedDict):
    arn: str

class GetSuiteRequestTypeDef(TypedDict):
    arn: str

class GetTestGridProjectRequestTypeDef(TypedDict):
    projectArn: str

class GetTestGridSessionRequestTypeDef(TypedDict):
    projectArn: NotRequired[str]
    sessionId: NotRequired[str]
    sessionArn: NotRequired[str]

class TestGridSessionTypeDef(TypedDict):
    arn: NotRequired[str]
    status: NotRequired[TestGridSessionStatusType]
    created: NotRequired[datetime]
    ended: NotRequired[datetime]
    billingMinutes: NotRequired[float]
    seleniumProperties: NotRequired[str]

class GetTestRequestTypeDef(TypedDict):
    arn: str

class GetUploadRequestTypeDef(TypedDict):
    arn: str

class GetVPCEConfigurationRequestTypeDef(TypedDict):
    arn: str

class InstallToRemoteAccessSessionRequestTypeDef(TypedDict):
    remoteAccessSessionArn: str
    appArn: str

ListArtifactsRequestTypeDef = TypedDict(
    "ListArtifactsRequestTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "nextToken": NotRequired[str],
    },
)

class ListDeviceInstancesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ListDevicePoolsRequestTypeDef = TypedDict(
    "ListDevicePoolsRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "nextToken": NotRequired[str],
    },
)

class ListInstanceProfilesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListJobsRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

ListNetworkProfilesRequestTypeDef = TypedDict(
    "ListNetworkProfilesRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "nextToken": NotRequired[str],
    },
)

class ListOfferingPromotionsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
    },
)

class ListOfferingTransactionsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class ListOfferingsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class ListProjectsRequestTypeDef(TypedDict):
    arn: NotRequired[str]
    nextToken: NotRequired[str]

class ListRemoteAccessSessionsRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

class ListRunsRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

class ListSamplesRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[SampleTypeType],
        "url": NotRequired[str],
    },
)

class ListSuitesRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ListTestGridProjectsRequestTypeDef(TypedDict):
    maxResult: NotRequired[int]
    nextToken: NotRequired[str]

class ListTestGridSessionActionsRequestTypeDef(TypedDict):
    sessionArn: str
    maxResult: NotRequired[int]
    nextToken: NotRequired[str]

class TestGridSessionActionTypeDef(TypedDict):
    action: NotRequired[str]
    started: NotRequired[datetime]
    duration: NotRequired[int]
    statusCode: NotRequired[str]
    requestMethod: NotRequired[str]

ListTestGridSessionArtifactsRequestTypeDef = TypedDict(
    "ListTestGridSessionArtifactsRequestTypeDef",
    {
        "sessionArn": str,
        "type": NotRequired[TestGridSessionArtifactCategoryType],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {
        "filename": NotRequired[str],
        "type": NotRequired[TestGridSessionArtifactTypeType],
        "url": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]

class ListTestsRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

class ListUniqueProblemsRequestTypeDef(TypedDict):
    arn: str
    nextToken: NotRequired[str]

ListUploadsRequestTypeDef = TypedDict(
    "ListUploadsRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "nextToken": NotRequired[str],
    },
)

class ListVPCEConfigurationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class LocationTypeDef(TypedDict):
    latitude: float
    longitude: float

class MonetaryAmountTypeDef(TypedDict):
    amount: NotRequired[float]
    currencyCode: NotRequired[Literal["USD"]]

class ProblemDetailTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]

class VpcConfigOutputTypeDef(TypedDict):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class PurchaseOfferingRequestTypeDef(TypedDict):
    offeringId: str
    quantity: int
    offeringPromotionId: NotRequired[str]

class RadiosTypeDef(TypedDict):
    wifi: NotRequired[bool]
    bluetooth: NotRequired[bool]
    nfc: NotRequired[bool]
    gps: NotRequired[bool]

class RenewOfferingRequestTypeDef(TypedDict):
    offeringId: str
    quantity: int

class StopJobRequestTypeDef(TypedDict):
    arn: str

class StopRemoteAccessSessionRequestTypeDef(TypedDict):
    arn: str

class StopRunRequestTypeDef(TypedDict):
    arn: str

class TestGridVpcConfigOutputTypeDef(TypedDict):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class TestGridVpcConfigTypeDef(TypedDict):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDeviceInstanceRequestTypeDef(TypedDict):
    arn: str
    profileArn: NotRequired[str]
    labels: NotRequired[Sequence[str]]

class UpdateInstanceProfileRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    description: NotRequired[str]
    packageCleanup: NotRequired[bool]
    excludeAppPackagesFromCleanup: NotRequired[Sequence[str]]
    rebootAfterUse: NotRequired[bool]

UpdateNetworkProfileRequestTypeDef = TypedDict(
    "UpdateNetworkProfileRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)

class UpdateUploadRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    contentType: NotRequired[str]
    editContent: NotRequired[bool]

class UpdateVPCEConfigurationRequestTypeDef(TypedDict):
    arn: str
    vpceConfigurationName: NotRequired[str]
    vpceServiceName: NotRequired[str]
    serviceDnsName: NotRequired[str]
    vpceConfigurationDescription: NotRequired[str]

class VpcConfigTypeDef(TypedDict):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str

class AccountSettingsTypeDef(TypedDict):
    awsAccountNumber: NotRequired[str]
    unmeteredDevices: NotRequired[Dict[DevicePlatformType, int]]
    unmeteredRemoteAccessDevices: NotRequired[Dict[DevicePlatformType, int]]
    maxJobTimeoutMinutes: NotRequired[int]
    trialMinutes: NotRequired[TrialMinutesTypeDef]
    maxSlots: NotRequired[Dict[str, int]]
    defaultJobTimeoutMinutes: NotRequired[int]
    skipAppResign: NotRequired[bool]

class CreateDevicePoolRequestTypeDef(TypedDict):
    projectArn: str
    name: str
    rules: Sequence[RuleTypeDef]
    description: NotRequired[str]
    maxDevices: NotRequired[int]

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[DevicePoolTypeType],
        "rules": NotRequired[List[RuleTypeDef]],
        "maxDevices": NotRequired[int],
    },
)

class UpdateDevicePoolRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    description: NotRequired[str]
    rules: NotRequired[Sequence[RuleTypeDef]]
    maxDevices: NotRequired[int]
    clearMaxDevices: NotRequired[bool]

class CreateTestGridUrlResultTypeDef(TypedDict):
    url: str
    expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListArtifactsResultTypeDef(TypedDict):
    artifacts: List[ArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateInstanceProfileResultTypeDef(TypedDict):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceInstanceTypeDef(TypedDict):
    arn: NotRequired[str]
    deviceArn: NotRequired[str]
    labels: NotRequired[List[str]]
    status: NotRequired[InstanceStatusType]
    udid: NotRequired[str]
    instanceProfile: NotRequired[InstanceProfileTypeDef]

class GetInstanceProfileResultTypeDef(TypedDict):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesResultTypeDef(TypedDict):
    instanceProfiles: List[InstanceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateInstanceProfileResultTypeDef(TypedDict):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkProfileResultTypeDef(TypedDict):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkProfileResultTypeDef(TypedDict):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkProfilesResultTypeDef(TypedDict):
    networkProfiles: List[NetworkProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateNetworkProfileResultTypeDef(TypedDict):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRemoteAccessSessionConfigurationTypeDef(TypedDict):
    billingMethod: NotRequired[BillingMethodType]
    vpceConfigurationArns: NotRequired[Sequence[str]]
    deviceProxy: NotRequired[DeviceProxyTypeDef]

class CreateUploadResultTypeDef(TypedDict):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUploadResultTypeDef(TypedDict):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstallToRemoteAccessSessionResultTypeDef(TypedDict):
    appUpload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUploadsResultTypeDef(TypedDict):
    uploads: List[UploadTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateUploadResultTypeDef(TypedDict):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVPCEConfigurationResultTypeDef(TypedDict):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVPCEConfigurationResultTypeDef(TypedDict):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVPCEConfigurationsResultTypeDef(TypedDict):
    vpceConfigurations: List[VPCEConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateVPCEConfigurationResultTypeDef(TypedDict):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CustomerArtifactPathsUnionTypeDef = Union[
    CustomerArtifactPathsTypeDef, CustomerArtifactPathsOutputTypeDef
]

class DeviceSelectionResultTypeDef(TypedDict):
    filters: NotRequired[List[DeviceFilterOutputTypeDef]]
    matchedDevicesCount: NotRequired[int]
    maxDevices: NotRequired[int]

DeviceFilterUnionTypeDef = Union[DeviceFilterTypeDef, DeviceFilterOutputTypeDef]
SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
    },
)
TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
    },
)

class GetOfferingStatusRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListArtifactsRequestPaginateTypeDef = TypedDict(
    "ListArtifactsRequestPaginateTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListDeviceInstancesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListDevicePoolsRequestPaginateTypeDef = TypedDict(
    "ListDevicePoolsRequestPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListInstanceProfilesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListNetworkProfilesRequestPaginateTypeDef = TypedDict(
    "ListNetworkProfilesRequestPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListOfferingPromotionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOfferingTransactionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOfferingsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsRequestPaginateTypeDef(TypedDict):
    arn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRemoteAccessSessionsRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRunsRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSamplesRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSuitesRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTestsRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUniqueProblemsRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListUploadsRequestPaginateTypeDef = TypedDict(
    "ListUploadsRequestPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListVPCEConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTestGridSessionResultTypeDef(TypedDict):
    testGridSession: TestGridSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionsResultTypeDef(TypedDict):
    testGridSessions: List[TestGridSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListOfferingPromotionsResultTypeDef(TypedDict):
    offeringPromotions: List[OfferingPromotionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSamplesResultTypeDef(TypedDict):
    samples: List[SampleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListTestGridSessionActionsResultTypeDef(TypedDict):
    actions: List[TestGridSessionActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestGridSessionArtifactsResultTypeDef(TypedDict):
    artifacts: List[TestGridSessionArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestGridSessionsRequestTypeDef(TypedDict):
    projectArn: str
    status: NotRequired[TestGridSessionStatusType]
    creationTimeAfter: NotRequired[TimestampTypeDef]
    creationTimeBefore: NotRequired[TimestampTypeDef]
    endTimeAfter: NotRequired[TimestampTypeDef]
    endTimeBefore: NotRequired[TimestampTypeDef]
    maxResult: NotRequired[int]
    nextToken: NotRequired[str]

class RecurringChargeTypeDef(TypedDict):
    cost: NotRequired[MonetaryAmountTypeDef]
    frequency: NotRequired[Literal["MONTHLY"]]

class ProjectTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    defaultJobTimeoutMinutes: NotRequired[int]
    created: NotRequired[datetime]
    vpcConfig: NotRequired[VpcConfigOutputTypeDef]

class TestGridProjectTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    vpcConfig: NotRequired[TestGridVpcConfigOutputTypeDef]
    created: NotRequired[datetime]

TestGridVpcConfigUnionTypeDef = Union[TestGridVpcConfigTypeDef, TestGridVpcConfigOutputTypeDef]
VpcConfigUnionTypeDef = Union[VpcConfigTypeDef, VpcConfigOutputTypeDef]

class GetAccountSettingsResultTypeDef(TypedDict):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevicePoolResultTypeDef(TypedDict):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePoolResultTypeDef(TypedDict):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicePoolsResultTypeDef(TypedDict):
    devicePools: List[DevicePoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDevicePoolResultTypeDef(TypedDict):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    manufacturer: NotRequired[str]
    model: NotRequired[str]
    modelId: NotRequired[str]
    formFactor: NotRequired[DeviceFormFactorType]
    platform: NotRequired[DevicePlatformType]
    os: NotRequired[str]
    cpu: NotRequired[CPUTypeDef]
    resolution: NotRequired[ResolutionTypeDef]
    heapSize: NotRequired[int]
    memory: NotRequired[int]
    image: NotRequired[str]
    carrier: NotRequired[str]
    radio: NotRequired[str]
    remoteAccessEnabled: NotRequired[bool]
    remoteDebugEnabled: NotRequired[bool]
    fleetType: NotRequired[str]
    fleetName: NotRequired[str]
    instances: NotRequired[List[DeviceInstanceTypeDef]]
    availability: NotRequired[DeviceAvailabilityType]

class GetDeviceInstanceResultTypeDef(TypedDict):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceInstancesResultTypeDef(TypedDict):
    deviceInstances: List[DeviceInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDeviceInstanceResultTypeDef(TypedDict):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRemoteAccessSessionRequestTypeDef(TypedDict):
    projectArn: str
    deviceArn: str
    instanceArn: NotRequired[str]
    sshPublicKey: NotRequired[str]
    remoteDebugEnabled: NotRequired[bool]
    remoteRecordEnabled: NotRequired[bool]
    remoteRecordAppArn: NotRequired[str]
    name: NotRequired[str]
    clientId: NotRequired[str]
    configuration: NotRequired[CreateRemoteAccessSessionConfigurationTypeDef]
    interactionMode: NotRequired[InteractionModeType]
    skipAppResign: NotRequired[bool]

class ScheduleRunConfigurationTypeDef(TypedDict):
    extraDataPackageArn: NotRequired[str]
    networkProfileArn: NotRequired[str]
    locale: NotRequired[str]
    location: NotRequired[LocationTypeDef]
    vpceConfigurationArns: NotRequired[Sequence[str]]
    deviceProxy: NotRequired[DeviceProxyTypeDef]
    customerArtifactPaths: NotRequired[CustomerArtifactPathsUnionTypeDef]
    radios: NotRequired[RadiosTypeDef]
    auxiliaryApps: NotRequired[Sequence[str]]
    billingMethod: NotRequired[BillingMethodType]

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "platform": NotRequired[DevicePlatformType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "totalJobs": NotRequired[int],
        "completedJobs": NotRequired[int],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "networkProfile": NotRequired[NetworkProfileTypeDef],
        "deviceProxy": NotRequired[DeviceProxyTypeDef],
        "parsingResultUrl": NotRequired[str],
        "resultCode": NotRequired[ExecutionResultCodeType],
        "seed": NotRequired[int],
        "appUpload": NotRequired[str],
        "eventCount": NotRequired[int],
        "jobTimeoutMinutes": NotRequired[int],
        "devicePoolArn": NotRequired[str],
        "locale": NotRequired[str],
        "radios": NotRequired[RadiosTypeDef],
        "location": NotRequired[LocationTypeDef],
        "customerArtifactPaths": NotRequired[CustomerArtifactPathsOutputTypeDef],
        "webUrl": NotRequired[str],
        "skipAppResign": NotRequired[bool],
        "testSpecArn": NotRequired[str],
        "deviceSelectionResult": NotRequired[DeviceSelectionResultTypeDef],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
    },
)

class DeviceSelectionConfigurationTypeDef(TypedDict):
    filters: Sequence[DeviceFilterUnionTypeDef]
    maxDevices: int

class ListDevicesRequestPaginateTypeDef(TypedDict):
    arn: NotRequired[str]
    filters: NotRequired[Sequence[DeviceFilterUnionTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDevicesRequestTypeDef(TypedDict):
    arn: NotRequired[str]
    nextToken: NotRequired[str]
    filters: NotRequired[Sequence[DeviceFilterUnionTypeDef]]

class GetSuiteResultTypeDef(TypedDict):
    suite: SuiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSuitesResultTypeDef(TypedDict):
    suites: List[SuiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetTestResultTypeDef(TypedDict):
    test: TestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestsResultTypeDef(TypedDict):
    tests: List[TestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[Literal["RECURRING"]],
        "platform": NotRequired[DevicePlatformType],
        "recurringCharges": NotRequired[List[RecurringChargeTypeDef]],
    },
)

class CreateProjectResultTypeDef(TypedDict):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResultTypeDef(TypedDict):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResultTypeDef(TypedDict):
    projects: List[ProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateProjectResultTypeDef(TypedDict):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestGridProjectResultTypeDef(TypedDict):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestGridProjectResultTypeDef(TypedDict):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridProjectsResultTypeDef(TypedDict):
    testGridProjects: List[TestGridProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateTestGridProjectResultTypeDef(TypedDict):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTestGridProjectRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    vpcConfig: NotRequired[TestGridVpcConfigUnionTypeDef]

class UpdateTestGridProjectRequestTypeDef(TypedDict):
    projectArn: str
    name: NotRequired[str]
    description: NotRequired[str]
    vpcConfig: NotRequired[TestGridVpcConfigUnionTypeDef]

class CreateProjectRequestTypeDef(TypedDict):
    name: str
    defaultJobTimeoutMinutes: NotRequired[int]
    vpcConfig: NotRequired[VpcConfigUnionTypeDef]

class UpdateProjectRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    defaultJobTimeoutMinutes: NotRequired[int]
    vpcConfig: NotRequired[VpcConfigUnionTypeDef]

class DevicePoolCompatibilityResultTypeDef(TypedDict):
    device: NotRequired[DeviceTypeDef]
    compatible: NotRequired[bool]
    incompatibilityMessages: NotRequired[List[IncompatibilityMessageTypeDef]]

class GetDeviceResultTypeDef(TypedDict):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "device": NotRequired[DeviceTypeDef],
        "instanceArn": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "videoEndpoint": NotRequired[str],
        "videoCapture": NotRequired[bool],
    },
)

class ListDevicesResultTypeDef(TypedDict):
    devices: List[DeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ProblemTypeDef(TypedDict):
    run: NotRequired[ProblemDetailTypeDef]
    job: NotRequired[ProblemDetailTypeDef]
    suite: NotRequired[ProblemDetailTypeDef]
    test: NotRequired[ProblemDetailTypeDef]
    device: NotRequired[DeviceTypeDef]
    result: NotRequired[ExecutionResultType]
    message: NotRequired[str]

class RemoteAccessSessionTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    created: NotRequired[datetime]
    status: NotRequired[ExecutionStatusType]
    result: NotRequired[ExecutionResultType]
    message: NotRequired[str]
    started: NotRequired[datetime]
    stopped: NotRequired[datetime]
    device: NotRequired[DeviceTypeDef]
    instanceArn: NotRequired[str]
    remoteDebugEnabled: NotRequired[bool]
    remoteRecordEnabled: NotRequired[bool]
    remoteRecordAppArn: NotRequired[str]
    hostAddress: NotRequired[str]
    clientId: NotRequired[str]
    billingMethod: NotRequired[BillingMethodType]
    deviceMinutes: NotRequired[DeviceMinutesTypeDef]
    endpoint: NotRequired[str]
    deviceUdid: NotRequired[str]
    interactionMode: NotRequired[InteractionModeType]
    skipAppResign: NotRequired[bool]
    vpcConfig: NotRequired[VpcConfigOutputTypeDef]
    deviceProxy: NotRequired[DeviceProxyTypeDef]

class GetDevicePoolCompatibilityRequestTypeDef(TypedDict):
    devicePoolArn: str
    appArn: NotRequired[str]
    testType: NotRequired[TestTypeType]
    test: NotRequired[ScheduleRunTestTypeDef]
    configuration: NotRequired[ScheduleRunConfigurationTypeDef]
    projectArn: NotRequired[str]

class GetRunResultTypeDef(TypedDict):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunsResultTypeDef(TypedDict):
    runs: List[RunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ScheduleRunResultTypeDef(TypedDict):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopRunResultTypeDef(TypedDict):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduleRunRequestTypeDef(TypedDict):
    projectArn: str
    test: ScheduleRunTestTypeDef
    appArn: NotRequired[str]
    devicePoolArn: NotRequired[str]
    deviceSelectionConfiguration: NotRequired[DeviceSelectionConfigurationTypeDef]
    name: NotRequired[str]
    configuration: NotRequired[ScheduleRunConfigurationTypeDef]
    executionConfiguration: NotRequired[ExecutionConfigurationTypeDef]

class ListOfferingsResultTypeDef(TypedDict):
    offerings: List[OfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": NotRequired[OfferingTransactionTypeType],
        "offering": NotRequired[OfferingTypeDef],
        "quantity": NotRequired[int],
        "effectiveOn": NotRequired[datetime],
    },
)

class GetDevicePoolCompatibilityResultTypeDef(TypedDict):
    compatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    incompatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResultTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResultTypeDef(TypedDict):
    jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StopJobResultTypeDef(TypedDict):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UniqueProblemTypeDef(TypedDict):
    message: NotRequired[str]
    problems: NotRequired[List[ProblemTypeDef]]

class CreateRemoteAccessSessionResultTypeDef(TypedDict):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRemoteAccessSessionResultTypeDef(TypedDict):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRemoteAccessSessionsResultTypeDef(TypedDict):
    remoteAccessSessions: List[RemoteAccessSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StopRemoteAccessSessionResultTypeDef(TypedDict):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOfferingStatusResultTypeDef(TypedDict):
    current: Dict[str, OfferingStatusTypeDef]
    nextPeriod: Dict[str, OfferingStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class OfferingTransactionTypeDef(TypedDict):
    offeringStatus: NotRequired[OfferingStatusTypeDef]
    transactionId: NotRequired[str]
    offeringPromotionId: NotRequired[str]
    createdOn: NotRequired[datetime]
    cost: NotRequired[MonetaryAmountTypeDef]

class ListUniqueProblemsResultTypeDef(TypedDict):
    uniqueProblems: Dict[ExecutionResultType, List[UniqueProblemTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListOfferingTransactionsResultTypeDef(TypedDict):
    offeringTransactions: List[OfferingTransactionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PurchaseOfferingResultTypeDef(TypedDict):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RenewOfferingResultTypeDef(TypedDict):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
