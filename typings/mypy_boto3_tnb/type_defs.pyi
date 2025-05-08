"""
Type annotations for tnb service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_tnb.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    LcmOperationTypeType,
    NsdOnboardingStateType,
    NsdOperationalStateType,
    NsdUsageStateType,
    NsLcmOperationStateType,
    NsStateType,
    OnboardingStateType,
    OperationalStateType,
    TaskStatusType,
    UpdateSolNetworkTypeType,
    UsageStateType,
    VnfInstantiationStateType,
    VnfOperationalStateType,
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
    "BlobTypeDef",
    "CancelSolNetworkOperationInputTypeDef",
    "CreateSolFunctionPackageInputTypeDef",
    "CreateSolFunctionPackageOutputTypeDef",
    "CreateSolNetworkInstanceInputTypeDef",
    "CreateSolNetworkInstanceOutputTypeDef",
    "CreateSolNetworkPackageInputTypeDef",
    "CreateSolNetworkPackageOutputTypeDef",
    "DeleteSolFunctionPackageInputTypeDef",
    "DeleteSolNetworkInstanceInputTypeDef",
    "DeleteSolNetworkPackageInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ErrorInfoTypeDef",
    "FunctionArtifactMetaTypeDef",
    "GetSolFunctionInstanceInputTypeDef",
    "GetSolFunctionInstanceMetadataTypeDef",
    "GetSolFunctionInstanceOutputTypeDef",
    "GetSolFunctionPackageContentInputTypeDef",
    "GetSolFunctionPackageContentOutputTypeDef",
    "GetSolFunctionPackageDescriptorInputTypeDef",
    "GetSolFunctionPackageDescriptorOutputTypeDef",
    "GetSolFunctionPackageInputTypeDef",
    "GetSolFunctionPackageMetadataTypeDef",
    "GetSolFunctionPackageOutputTypeDef",
    "GetSolInstantiatedVnfInfoTypeDef",
    "GetSolNetworkInstanceInputTypeDef",
    "GetSolNetworkInstanceMetadataTypeDef",
    "GetSolNetworkInstanceOutputTypeDef",
    "GetSolNetworkOperationInputTypeDef",
    "GetSolNetworkOperationMetadataTypeDef",
    "GetSolNetworkOperationOutputTypeDef",
    "GetSolNetworkOperationTaskDetailsTypeDef",
    "GetSolNetworkPackageContentInputTypeDef",
    "GetSolNetworkPackageContentOutputTypeDef",
    "GetSolNetworkPackageDescriptorInputTypeDef",
    "GetSolNetworkPackageDescriptorOutputTypeDef",
    "GetSolNetworkPackageInputTypeDef",
    "GetSolNetworkPackageMetadataTypeDef",
    "GetSolNetworkPackageOutputTypeDef",
    "GetSolVnfInfoTypeDef",
    "GetSolVnfcResourceInfoMetadataTypeDef",
    "GetSolVnfcResourceInfoTypeDef",
    "InstantiateMetadataTypeDef",
    "InstantiateSolNetworkInstanceInputTypeDef",
    "InstantiateSolNetworkInstanceOutputTypeDef",
    "LcmOperationInfoTypeDef",
    "ListSolFunctionInstanceInfoTypeDef",
    "ListSolFunctionInstanceMetadataTypeDef",
    "ListSolFunctionInstancesInputPaginateTypeDef",
    "ListSolFunctionInstancesInputTypeDef",
    "ListSolFunctionInstancesOutputTypeDef",
    "ListSolFunctionPackageInfoTypeDef",
    "ListSolFunctionPackageMetadataTypeDef",
    "ListSolFunctionPackagesInputPaginateTypeDef",
    "ListSolFunctionPackagesInputTypeDef",
    "ListSolFunctionPackagesOutputTypeDef",
    "ListSolNetworkInstanceInfoTypeDef",
    "ListSolNetworkInstanceMetadataTypeDef",
    "ListSolNetworkInstancesInputPaginateTypeDef",
    "ListSolNetworkInstancesInputTypeDef",
    "ListSolNetworkInstancesOutputTypeDef",
    "ListSolNetworkOperationsInfoTypeDef",
    "ListSolNetworkOperationsInputPaginateTypeDef",
    "ListSolNetworkOperationsInputTypeDef",
    "ListSolNetworkOperationsMetadataTypeDef",
    "ListSolNetworkOperationsOutputTypeDef",
    "ListSolNetworkPackageInfoTypeDef",
    "ListSolNetworkPackageMetadataTypeDef",
    "ListSolNetworkPackagesInputPaginateTypeDef",
    "ListSolNetworkPackagesInputTypeDef",
    "ListSolNetworkPackagesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ModifyVnfInfoMetadataTypeDef",
    "NetworkArtifactMetaTypeDef",
    "PaginatorConfigTypeDef",
    "ProblemDetailsTypeDef",
    "PutSolFunctionPackageContentInputTypeDef",
    "PutSolFunctionPackageContentMetadataTypeDef",
    "PutSolFunctionPackageContentOutputTypeDef",
    "PutSolNetworkPackageContentInputTypeDef",
    "PutSolNetworkPackageContentMetadataTypeDef",
    "PutSolNetworkPackageContentOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "TerminateSolNetworkInstanceInputTypeDef",
    "TerminateSolNetworkInstanceOutputTypeDef",
    "ToscaOverrideTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateNsMetadataTypeDef",
    "UpdateSolFunctionPackageInputTypeDef",
    "UpdateSolFunctionPackageOutputTypeDef",
    "UpdateSolNetworkInstanceInputTypeDef",
    "UpdateSolNetworkInstanceOutputTypeDef",
    "UpdateSolNetworkModifyTypeDef",
    "UpdateSolNetworkPackageInputTypeDef",
    "UpdateSolNetworkPackageOutputTypeDef",
    "UpdateSolNetworkServiceDataTypeDef",
    "ValidateSolFunctionPackageContentInputTypeDef",
    "ValidateSolFunctionPackageContentMetadataTypeDef",
    "ValidateSolFunctionPackageContentOutputTypeDef",
    "ValidateSolNetworkPackageContentInputTypeDef",
    "ValidateSolNetworkPackageContentMetadataTypeDef",
    "ValidateSolNetworkPackageContentOutputTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelSolNetworkOperationInputTypeDef(TypedDict):
    nsLcmOpOccId: str

class CreateSolFunctionPackageInputTypeDef(TypedDict):
    tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateSolNetworkInstanceInputTypeDef(TypedDict):
    nsName: str
    nsdInfoId: str
    nsDescription: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateSolNetworkPackageInputTypeDef(TypedDict):
    tags: NotRequired[Mapping[str, str]]

class DeleteSolFunctionPackageInputTypeDef(TypedDict):
    vnfPkgId: str

class DeleteSolNetworkInstanceInputTypeDef(TypedDict):
    nsInstanceId: str

class DeleteSolNetworkPackageInputTypeDef(TypedDict):
    nsdInfoId: str

class ErrorInfoTypeDef(TypedDict):
    cause: NotRequired[str]
    details: NotRequired[str]

class ToscaOverrideTypeDef(TypedDict):
    defaultValue: NotRequired[str]
    name: NotRequired[str]

class GetSolFunctionInstanceInputTypeDef(TypedDict):
    vnfInstanceId: str

class GetSolFunctionInstanceMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime

class GetSolFunctionPackageContentInputTypeDef(TypedDict):
    accept: Literal["application/zip"]
    vnfPkgId: str

class GetSolFunctionPackageDescriptorInputTypeDef(TypedDict):
    accept: Literal["text/plain"]
    vnfPkgId: str

class GetSolFunctionPackageInputTypeDef(TypedDict):
    vnfPkgId: str

class GetSolInstantiatedVnfInfoTypeDef(TypedDict):
    vnfState: NotRequired[VnfOperationalStateType]

class GetSolNetworkInstanceInputTypeDef(TypedDict):
    nsInstanceId: str

class GetSolNetworkInstanceMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime

class LcmOperationInfoTypeDef(TypedDict):
    nsLcmOpOccId: str

class GetSolNetworkOperationInputTypeDef(TypedDict):
    nsLcmOpOccId: str

class InstantiateMetadataTypeDef(TypedDict):
    nsdInfoId: str
    additionalParamsForNs: NotRequired[Dict[str, Any]]

class ModifyVnfInfoMetadataTypeDef(TypedDict):
    vnfConfigurableProperties: Dict[str, Any]
    vnfInstanceId: str

class UpdateNsMetadataTypeDef(TypedDict):
    nsdInfoId: str
    additionalParamsForNs: NotRequired[Dict[str, Any]]

class ProblemDetailsTypeDef(TypedDict):
    detail: str
    title: NotRequired[str]

class GetSolNetworkPackageContentInputTypeDef(TypedDict):
    accept: Literal["application/zip"]
    nsdInfoId: str

class GetSolNetworkPackageDescriptorInputTypeDef(TypedDict):
    nsdInfoId: str

class GetSolNetworkPackageInputTypeDef(TypedDict):
    nsdInfoId: str

class GetSolVnfcResourceInfoMetadataTypeDef(TypedDict):
    cluster: NotRequired[str]
    helmChart: NotRequired[str]
    nodeGroup: NotRequired[str]

class InstantiateSolNetworkInstanceInputTypeDef(TypedDict):
    nsInstanceId: str
    additionalParamsForNs: NotRequired[Mapping[str, Any]]
    dryRun: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class ListSolFunctionInstanceMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSolFunctionInstancesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSolFunctionPackageMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime

class ListSolFunctionPackagesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSolNetworkInstanceMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkInstancesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSolNetworkOperationsMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime
    nsdInfoId: NotRequired[str]
    vnfInstanceId: NotRequired[str]

class ListSolNetworkOperationsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    nsInstanceId: NotRequired[str]

class ListSolNetworkPackageMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime

class ListSolNetworkPackagesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TerminateSolNetworkInstanceInputTypeDef(TypedDict):
    nsInstanceId: str
    tags: NotRequired[Mapping[str, str]]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateSolFunctionPackageInputTypeDef(TypedDict):
    operationalState: OperationalStateType
    vnfPkgId: str

class UpdateSolNetworkModifyTypeDef(TypedDict):
    vnfConfigurableProperties: Mapping[str, Any]
    vnfInstanceId: str

class UpdateSolNetworkServiceDataTypeDef(TypedDict):
    nsdInfoId: str
    additionalParamsForNs: NotRequired[Mapping[str, Any]]

class UpdateSolNetworkPackageInputTypeDef(TypedDict):
    nsdInfoId: str
    nsdOperationalState: NsdOperationalStateType

class PutSolFunctionPackageContentInputTypeDef(TypedDict):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: NotRequired[Literal["application/zip"]]

class PutSolNetworkPackageContentInputTypeDef(TypedDict):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: NotRequired[Literal["application/zip"]]

class ValidateSolFunctionPackageContentInputTypeDef(TypedDict):
    file: BlobTypeDef
    vnfPkgId: str
    contentType: NotRequired[Literal["application/zip"]]

class ValidateSolNetworkPackageContentInputTypeDef(TypedDict):
    file: BlobTypeDef
    nsdInfoId: str
    contentType: NotRequired[Literal["application/zip"]]

CreateSolFunctionPackageOutputTypeDef = TypedDict(
    "CreateSolFunctionPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "tags": Dict[str, str],
        "usageState": UsageStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSolNetworkInstanceOutputTypeDef = TypedDict(
    "CreateSolNetworkInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "nsInstanceName": str,
        "nsdInfoId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSolNetworkPackageOutputTypeDef = TypedDict(
    "CreateSolNetworkPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageContentOutputTypeDef(TypedDict):
    contentType: Literal["application/zip"]
    packageContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolFunctionPackageDescriptorOutputTypeDef(TypedDict):
    contentType: Literal["text/plain"]
    vnfd: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkPackageContentOutputTypeDef(TypedDict):
    contentType: Literal["application/zip"]
    nsdContent: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkPackageDescriptorOutputTypeDef(TypedDict):
    contentType: Literal["text/plain"]
    nsd: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class InstantiateSolNetworkInstanceOutputTypeDef(TypedDict):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateSolNetworkInstanceOutputTypeDef(TypedDict):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSolFunctionPackageOutputTypeDef(TypedDict):
    operationalState: OperationalStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSolNetworkInstanceOutputTypeDef(TypedDict):
    nsLcmOpOccId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSolNetworkPackageOutputTypeDef(TypedDict):
    nsdOperationalState: NsdOperationalStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolNetworkOperationTaskDetailsTypeDef(TypedDict):
    taskContext: NotRequired[Dict[str, str]]
    taskEndTime: NotRequired[datetime]
    taskErrorDetails: NotRequired[ErrorInfoTypeDef]
    taskName: NotRequired[str]
    taskStartTime: NotRequired[datetime]
    taskStatus: NotRequired[TaskStatusType]

class FunctionArtifactMetaTypeDef(TypedDict):
    overrides: NotRequired[List[ToscaOverrideTypeDef]]

class NetworkArtifactMetaTypeDef(TypedDict):
    overrides: NotRequired[List[ToscaOverrideTypeDef]]

GetSolNetworkInstanceOutputTypeDef = TypedDict(
    "GetSolNetworkInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "lcmOpInfo": LcmOperationInfoTypeDef,
        "metadata": GetSolNetworkInstanceMetadataTypeDef,
        "nsInstanceDescription": str,
        "nsInstanceName": str,
        "nsState": NsStateType,
        "nsdId": str,
        "nsdInfoId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetSolNetworkOperationMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime
    instantiateMetadata: NotRequired[InstantiateMetadataTypeDef]
    modifyVnfInfoMetadata: NotRequired[ModifyVnfInfoMetadataTypeDef]
    updateNsMetadata: NotRequired[UpdateNsMetadataTypeDef]

class GetSolVnfcResourceInfoTypeDef(TypedDict):
    metadata: NotRequired[GetSolVnfcResourceInfoMetadataTypeDef]

ListSolFunctionInstanceInfoTypeDef = TypedDict(
    "ListSolFunctionInstanceInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "instantiationState": VnfInstantiationStateType,
        "metadata": ListSolFunctionInstanceMetadataTypeDef,
        "nsInstanceId": str,
        "vnfPkgId": str,
        "instantiatedVnfInfo": NotRequired[GetSolInstantiatedVnfInfoTypeDef],
        "vnfPkgName": NotRequired[str],
    },
)

class ListSolFunctionInstancesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSolFunctionPackagesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSolNetworkInstancesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSolNetworkOperationsInputPaginateTypeDef(TypedDict):
    nsInstanceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSolNetworkPackagesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListSolFunctionPackageInfoTypeDef = TypedDict(
    "ListSolFunctionPackageInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "usageState": UsageStateType,
        "metadata": NotRequired[ListSolFunctionPackageMetadataTypeDef],
        "vnfProductName": NotRequired[str],
        "vnfProvider": NotRequired[str],
        "vnfdId": NotRequired[str],
        "vnfdVersion": NotRequired[str],
    },
)
ListSolNetworkInstanceInfoTypeDef = TypedDict(
    "ListSolNetworkInstanceInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": ListSolNetworkInstanceMetadataTypeDef,
        "nsInstanceDescription": str,
        "nsInstanceName": str,
        "nsState": NsStateType,
        "nsdId": str,
        "nsdInfoId": str,
    },
)
ListSolNetworkOperationsInfoTypeDef = TypedDict(
    "ListSolNetworkOperationsInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "lcmOperationType": LcmOperationTypeType,
        "nsInstanceId": str,
        "operationState": NsLcmOperationStateType,
        "error": NotRequired[ProblemDetailsTypeDef],
        "metadata": NotRequired[ListSolNetworkOperationsMetadataTypeDef],
        "updateType": NotRequired[UpdateSolNetworkTypeType],
    },
)
ListSolNetworkPackageInfoTypeDef = TypedDict(
    "ListSolNetworkPackageInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": ListSolNetworkPackageMetadataTypeDef,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "nsdDesigner": NotRequired[str],
        "nsdId": NotRequired[str],
        "nsdInvariantId": NotRequired[str],
        "nsdName": NotRequired[str],
        "nsdVersion": NotRequired[str],
        "vnfPkgIds": NotRequired[List[str]],
    },
)

class UpdateSolNetworkInstanceInputTypeDef(TypedDict):
    nsInstanceId: str
    updateType: UpdateSolNetworkTypeType
    modifyVnfInfoData: NotRequired[UpdateSolNetworkModifyTypeDef]
    tags: NotRequired[Mapping[str, str]]
    updateNs: NotRequired[UpdateSolNetworkServiceDataTypeDef]

class GetSolFunctionPackageMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime
    vnfd: NotRequired[FunctionArtifactMetaTypeDef]

class PutSolFunctionPackageContentMetadataTypeDef(TypedDict):
    vnfd: NotRequired[FunctionArtifactMetaTypeDef]

class ValidateSolFunctionPackageContentMetadataTypeDef(TypedDict):
    vnfd: NotRequired[FunctionArtifactMetaTypeDef]

class GetSolNetworkPackageMetadataTypeDef(TypedDict):
    createdAt: datetime
    lastModified: datetime
    nsd: NotRequired[NetworkArtifactMetaTypeDef]

class PutSolNetworkPackageContentMetadataTypeDef(TypedDict):
    nsd: NotRequired[NetworkArtifactMetaTypeDef]

class ValidateSolNetworkPackageContentMetadataTypeDef(TypedDict):
    nsd: NotRequired[NetworkArtifactMetaTypeDef]

GetSolNetworkOperationOutputTypeDef = TypedDict(
    "GetSolNetworkOperationOutputTypeDef",
    {
        "arn": str,
        "error": ProblemDetailsTypeDef,
        "id": str,
        "lcmOperationType": LcmOperationTypeType,
        "metadata": GetSolNetworkOperationMetadataTypeDef,
        "nsInstanceId": str,
        "operationState": NsLcmOperationStateType,
        "tags": Dict[str, str],
        "tasks": List[GetSolNetworkOperationTaskDetailsTypeDef],
        "updateType": UpdateSolNetworkTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetSolVnfInfoTypeDef(TypedDict):
    vnfState: NotRequired[VnfOperationalStateType]
    vnfcResourceInfo: NotRequired[List[GetSolVnfcResourceInfoTypeDef]]

class ListSolFunctionInstancesOutputTypeDef(TypedDict):
    functionInstances: List[ListSolFunctionInstanceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSolFunctionPackagesOutputTypeDef(TypedDict):
    functionPackages: List[ListSolFunctionPackageInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSolNetworkInstancesOutputTypeDef(TypedDict):
    networkInstances: List[ListSolNetworkInstanceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSolNetworkOperationsOutputTypeDef(TypedDict):
    networkOperations: List[ListSolNetworkOperationsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSolNetworkPackagesOutputTypeDef(TypedDict):
    networkPackages: List[ListSolNetworkPackageInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetSolFunctionPackageOutputTypeDef = TypedDict(
    "GetSolFunctionPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": GetSolFunctionPackageMetadataTypeDef,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "tags": Dict[str, str],
        "usageState": UsageStateType,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSolFunctionPackageContentOutputTypeDef = TypedDict(
    "PutSolFunctionPackageContentOutputTypeDef",
    {
        "id": str,
        "metadata": PutSolFunctionPackageContentMetadataTypeDef,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateSolFunctionPackageContentOutputTypeDef = TypedDict(
    "ValidateSolFunctionPackageContentOutputTypeDef",
    {
        "id": str,
        "metadata": ValidateSolFunctionPackageContentMetadataTypeDef,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolNetworkPackageOutputTypeDef = TypedDict(
    "GetSolNetworkPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": GetSolNetworkPackageMetadataTypeDef,
        "nsdId": str,
        "nsdName": str,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "nsdVersion": str,
        "tags": Dict[str, str],
        "vnfPkgIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSolNetworkPackageContentOutputTypeDef = TypedDict(
    "PutSolNetworkPackageContentOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": PutSolNetworkPackageContentMetadataTypeDef,
        "nsdId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateSolNetworkPackageContentOutputTypeDef = TypedDict(
    "ValidateSolNetworkPackageContentOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": ValidateSolNetworkPackageContentMetadataTypeDef,
        "nsdId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolFunctionInstanceOutputTypeDef = TypedDict(
    "GetSolFunctionInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "instantiatedVnfInfo": GetSolVnfInfoTypeDef,
        "instantiationState": VnfInstantiationStateType,
        "metadata": GetSolFunctionInstanceMetadataTypeDef,
        "nsInstanceId": str,
        "tags": Dict[str, str],
        "vnfPkgId": str,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
