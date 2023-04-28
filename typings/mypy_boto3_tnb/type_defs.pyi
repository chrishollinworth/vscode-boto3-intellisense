"""
Type annotations for tnb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_tnb.type_defs import CancelSolNetworkOperationInputRequestTypeDef

    data: CancelSolNetworkOperationInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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
    UsageStateType,
    VnfInstantiationStateType,
    VnfOperationalStateType,
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
    "CancelSolNetworkOperationInputRequestTypeDef",
    "CreateSolFunctionPackageInputRequestTypeDef",
    "CreateSolFunctionPackageOutputTypeDef",
    "CreateSolNetworkInstanceInputRequestTypeDef",
    "CreateSolNetworkInstanceOutputTypeDef",
    "CreateSolNetworkPackageInputRequestTypeDef",
    "CreateSolNetworkPackageOutputTypeDef",
    "DeleteSolFunctionPackageInputRequestTypeDef",
    "DeleteSolNetworkInstanceInputRequestTypeDef",
    "DeleteSolNetworkPackageInputRequestTypeDef",
    "ErrorInfoTypeDef",
    "FunctionArtifactMetaTypeDef",
    "GetSolFunctionInstanceInputRequestTypeDef",
    "GetSolFunctionInstanceMetadataTypeDef",
    "GetSolFunctionInstanceOutputTypeDef",
    "GetSolFunctionPackageContentInputRequestTypeDef",
    "GetSolFunctionPackageContentOutputTypeDef",
    "GetSolFunctionPackageDescriptorInputRequestTypeDef",
    "GetSolFunctionPackageDescriptorOutputTypeDef",
    "GetSolFunctionPackageInputRequestTypeDef",
    "GetSolFunctionPackageMetadataTypeDef",
    "GetSolFunctionPackageOutputTypeDef",
    "GetSolInstantiatedVnfInfoTypeDef",
    "GetSolNetworkInstanceInputRequestTypeDef",
    "GetSolNetworkInstanceMetadataTypeDef",
    "GetSolNetworkInstanceOutputTypeDef",
    "GetSolNetworkOperationInputRequestTypeDef",
    "GetSolNetworkOperationMetadataTypeDef",
    "GetSolNetworkOperationOutputTypeDef",
    "GetSolNetworkOperationTaskDetailsTypeDef",
    "GetSolNetworkPackageContentInputRequestTypeDef",
    "GetSolNetworkPackageContentOutputTypeDef",
    "GetSolNetworkPackageDescriptorInputRequestTypeDef",
    "GetSolNetworkPackageDescriptorOutputTypeDef",
    "GetSolNetworkPackageInputRequestTypeDef",
    "GetSolNetworkPackageMetadataTypeDef",
    "GetSolNetworkPackageOutputTypeDef",
    "GetSolVnfInfoTypeDef",
    "GetSolVnfcResourceInfoMetadataTypeDef",
    "GetSolVnfcResourceInfoTypeDef",
    "InstantiateSolNetworkInstanceInputRequestTypeDef",
    "InstantiateSolNetworkInstanceOutputTypeDef",
    "LcmOperationInfoTypeDef",
    "ListSolFunctionInstanceInfoTypeDef",
    "ListSolFunctionInstanceMetadataTypeDef",
    "ListSolFunctionInstancesInputRequestTypeDef",
    "ListSolFunctionInstancesOutputTypeDef",
    "ListSolFunctionPackageInfoTypeDef",
    "ListSolFunctionPackageMetadataTypeDef",
    "ListSolFunctionPackagesInputRequestTypeDef",
    "ListSolFunctionPackagesOutputTypeDef",
    "ListSolNetworkInstanceInfoTypeDef",
    "ListSolNetworkInstanceMetadataTypeDef",
    "ListSolNetworkInstancesInputRequestTypeDef",
    "ListSolNetworkInstancesOutputTypeDef",
    "ListSolNetworkOperationsInfoTypeDef",
    "ListSolNetworkOperationsInputRequestTypeDef",
    "ListSolNetworkOperationsMetadataTypeDef",
    "ListSolNetworkOperationsOutputTypeDef",
    "ListSolNetworkPackageInfoTypeDef",
    "ListSolNetworkPackageMetadataTypeDef",
    "ListSolNetworkPackagesInputRequestTypeDef",
    "ListSolNetworkPackagesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NetworkArtifactMetaTypeDef",
    "PaginatorConfigTypeDef",
    "ProblemDetailsTypeDef",
    "PutSolFunctionPackageContentInputRequestTypeDef",
    "PutSolFunctionPackageContentMetadataTypeDef",
    "PutSolFunctionPackageContentOutputTypeDef",
    "PutSolNetworkPackageContentInputRequestTypeDef",
    "PutSolNetworkPackageContentMetadataTypeDef",
    "PutSolNetworkPackageContentOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "TerminateSolNetworkInstanceInputRequestTypeDef",
    "TerminateSolNetworkInstanceOutputTypeDef",
    "ToscaOverrideTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateSolFunctionPackageInputRequestTypeDef",
    "UpdateSolFunctionPackageOutputTypeDef",
    "UpdateSolNetworkInstanceInputRequestTypeDef",
    "UpdateSolNetworkInstanceOutputTypeDef",
    "UpdateSolNetworkModifyTypeDef",
    "UpdateSolNetworkPackageInputRequestTypeDef",
    "UpdateSolNetworkPackageOutputTypeDef",
    "ValidateSolFunctionPackageContentInputRequestTypeDef",
    "ValidateSolFunctionPackageContentMetadataTypeDef",
    "ValidateSolFunctionPackageContentOutputTypeDef",
    "ValidateSolNetworkPackageContentInputRequestTypeDef",
    "ValidateSolNetworkPackageContentMetadataTypeDef",
    "ValidateSolNetworkPackageContentOutputTypeDef",
)

CancelSolNetworkOperationInputRequestTypeDef = TypedDict(
    "CancelSolNetworkOperationInputRequestTypeDef",
    {
        "nsLcmOpOccId": str,
    },
)

CreateSolFunctionPackageInputRequestTypeDef = TypedDict(
    "CreateSolFunctionPackageInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSolFunctionPackageOutputTypeDef = TypedDict(
    "CreateSolFunctionPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "tags": Dict[str, str],
        "usageState": UsageStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_RequiredCreateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsName": str,
        "nsdInfoId": str,
    },
)
_OptionalCreateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_OptionalCreateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsDescription": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSolNetworkInstanceInputRequestTypeDef(
    _RequiredCreateSolNetworkInstanceInputRequestTypeDef,
    _OptionalCreateSolNetworkInstanceInputRequestTypeDef,
):
    pass

CreateSolNetworkInstanceOutputTypeDef = TypedDict(
    "CreateSolNetworkInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "nsInstanceName": str,
        "nsdInfoId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSolNetworkPackageInputRequestTypeDef = TypedDict(
    "CreateSolNetworkPackageInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSolFunctionPackageInputRequestTypeDef = TypedDict(
    "DeleteSolFunctionPackageInputRequestTypeDef",
    {
        "vnfPkgId": str,
    },
)

DeleteSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "DeleteSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
    },
)

DeleteSolNetworkPackageInputRequestTypeDef = TypedDict(
    "DeleteSolNetworkPackageInputRequestTypeDef",
    {
        "nsdInfoId": str,
    },
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "cause": str,
        "details": str,
    },
    total=False,
)

FunctionArtifactMetaTypeDef = TypedDict(
    "FunctionArtifactMetaTypeDef",
    {
        "overrides": List["ToscaOverrideTypeDef"],
    },
    total=False,
)

GetSolFunctionInstanceInputRequestTypeDef = TypedDict(
    "GetSolFunctionInstanceInputRequestTypeDef",
    {
        "vnfInstanceId": str,
    },
)

GetSolFunctionInstanceMetadataTypeDef = TypedDict(
    "GetSolFunctionInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

GetSolFunctionInstanceOutputTypeDef = TypedDict(
    "GetSolFunctionInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "instantiatedVnfInfo": "GetSolVnfInfoTypeDef",
        "instantiationState": VnfInstantiationStateType,
        "metadata": "GetSolFunctionInstanceMetadataTypeDef",
        "nsInstanceId": str,
        "tags": Dict[str, str],
        "vnfPkgId": str,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "GetSolFunctionPackageContentInputRequestTypeDef",
    {
        "accept": Literal["application/zip"],
        "vnfPkgId": str,
    },
)

GetSolFunctionPackageContentOutputTypeDef = TypedDict(
    "GetSolFunctionPackageContentOutputTypeDef",
    {
        "contentType": Literal["application/zip"],
        "packageContent": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolFunctionPackageDescriptorInputRequestTypeDef = TypedDict(
    "GetSolFunctionPackageDescriptorInputRequestTypeDef",
    {
        "accept": Literal["text/plain"],
        "vnfPkgId": str,
    },
)

GetSolFunctionPackageDescriptorOutputTypeDef = TypedDict(
    "GetSolFunctionPackageDescriptorOutputTypeDef",
    {
        "contentType": Literal["text/plain"],
        "vnfd": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolFunctionPackageInputRequestTypeDef = TypedDict(
    "GetSolFunctionPackageInputRequestTypeDef",
    {
        "vnfPkgId": str,
    },
)

_RequiredGetSolFunctionPackageMetadataTypeDef = TypedDict(
    "_RequiredGetSolFunctionPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
_OptionalGetSolFunctionPackageMetadataTypeDef = TypedDict(
    "_OptionalGetSolFunctionPackageMetadataTypeDef",
    {
        "vnfd": "FunctionArtifactMetaTypeDef",
    },
    total=False,
)

class GetSolFunctionPackageMetadataTypeDef(
    _RequiredGetSolFunctionPackageMetadataTypeDef, _OptionalGetSolFunctionPackageMetadataTypeDef
):
    pass

GetSolFunctionPackageOutputTypeDef = TypedDict(
    "GetSolFunctionPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": "GetSolFunctionPackageMetadataTypeDef",
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "tags": Dict[str, str],
        "usageState": UsageStateType,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolInstantiatedVnfInfoTypeDef = TypedDict(
    "GetSolInstantiatedVnfInfoTypeDef",
    {
        "vnfState": VnfOperationalStateType,
    },
    total=False,
)

GetSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "GetSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
    },
)

GetSolNetworkInstanceMetadataTypeDef = TypedDict(
    "GetSolNetworkInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

GetSolNetworkInstanceOutputTypeDef = TypedDict(
    "GetSolNetworkInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "lcmOpInfo": "LcmOperationInfoTypeDef",
        "metadata": "GetSolNetworkInstanceMetadataTypeDef",
        "nsInstanceDescription": str,
        "nsInstanceName": str,
        "nsState": NsStateType,
        "nsdId": str,
        "nsdInfoId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolNetworkOperationInputRequestTypeDef = TypedDict(
    "GetSolNetworkOperationInputRequestTypeDef",
    {
        "nsLcmOpOccId": str,
    },
)

GetSolNetworkOperationMetadataTypeDef = TypedDict(
    "GetSolNetworkOperationMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

GetSolNetworkOperationOutputTypeDef = TypedDict(
    "GetSolNetworkOperationOutputTypeDef",
    {
        "arn": str,
        "error": "ProblemDetailsTypeDef",
        "id": str,
        "lcmOperationType": LcmOperationTypeType,
        "metadata": "GetSolNetworkOperationMetadataTypeDef",
        "nsInstanceId": str,
        "operationState": NsLcmOperationStateType,
        "tags": Dict[str, str],
        "tasks": List["GetSolNetworkOperationTaskDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolNetworkOperationTaskDetailsTypeDef = TypedDict(
    "GetSolNetworkOperationTaskDetailsTypeDef",
    {
        "taskContext": Dict[str, str],
        "taskEndTime": datetime,
        "taskErrorDetails": "ErrorInfoTypeDef",
        "taskName": str,
        "taskStartTime": datetime,
        "taskStatus": TaskStatusType,
    },
    total=False,
)

GetSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "GetSolNetworkPackageContentInputRequestTypeDef",
    {
        "accept": Literal["application/zip"],
        "nsdInfoId": str,
    },
)

GetSolNetworkPackageContentOutputTypeDef = TypedDict(
    "GetSolNetworkPackageContentOutputTypeDef",
    {
        "contentType": Literal["application/zip"],
        "nsdContent": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolNetworkPackageDescriptorInputRequestTypeDef = TypedDict(
    "GetSolNetworkPackageDescriptorInputRequestTypeDef",
    {
        "nsdInfoId": str,
    },
)

GetSolNetworkPackageDescriptorOutputTypeDef = TypedDict(
    "GetSolNetworkPackageDescriptorOutputTypeDef",
    {
        "contentType": Literal["text/plain"],
        "nsd": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolNetworkPackageInputRequestTypeDef = TypedDict(
    "GetSolNetworkPackageInputRequestTypeDef",
    {
        "nsdInfoId": str,
    },
)

_RequiredGetSolNetworkPackageMetadataTypeDef = TypedDict(
    "_RequiredGetSolNetworkPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
_OptionalGetSolNetworkPackageMetadataTypeDef = TypedDict(
    "_OptionalGetSolNetworkPackageMetadataTypeDef",
    {
        "nsd": "NetworkArtifactMetaTypeDef",
    },
    total=False,
)

class GetSolNetworkPackageMetadataTypeDef(
    _RequiredGetSolNetworkPackageMetadataTypeDef, _OptionalGetSolNetworkPackageMetadataTypeDef
):
    pass

GetSolNetworkPackageOutputTypeDef = TypedDict(
    "GetSolNetworkPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": "GetSolNetworkPackageMetadataTypeDef",
        "nsdId": str,
        "nsdName": str,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "nsdVersion": str,
        "tags": Dict[str, str],
        "vnfPkgIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSolVnfInfoTypeDef = TypedDict(
    "GetSolVnfInfoTypeDef",
    {
        "vnfState": VnfOperationalStateType,
        "vnfcResourceInfo": List["GetSolVnfcResourceInfoTypeDef"],
    },
    total=False,
)

GetSolVnfcResourceInfoMetadataTypeDef = TypedDict(
    "GetSolVnfcResourceInfoMetadataTypeDef",
    {
        "cluster": str,
        "helmChart": str,
        "nodeGroup": str,
    },
    total=False,
)

GetSolVnfcResourceInfoTypeDef = TypedDict(
    "GetSolVnfcResourceInfoTypeDef",
    {
        "metadata": "GetSolVnfcResourceInfoMetadataTypeDef",
    },
    total=False,
)

_RequiredInstantiateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_RequiredInstantiateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
    },
)
_OptionalInstantiateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_OptionalInstantiateSolNetworkInstanceInputRequestTypeDef",
    {
        "additionalParamsForNs": Dict[str, Any],
        "dryRun": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class InstantiateSolNetworkInstanceInputRequestTypeDef(
    _RequiredInstantiateSolNetworkInstanceInputRequestTypeDef,
    _OptionalInstantiateSolNetworkInstanceInputRequestTypeDef,
):
    pass

InstantiateSolNetworkInstanceOutputTypeDef = TypedDict(
    "InstantiateSolNetworkInstanceOutputTypeDef",
    {
        "nsLcmOpOccId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LcmOperationInfoTypeDef = TypedDict(
    "LcmOperationInfoTypeDef",
    {
        "nsLcmOpOccId": str,
    },
)

_RequiredListSolFunctionInstanceInfoTypeDef = TypedDict(
    "_RequiredListSolFunctionInstanceInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "instantiationState": VnfInstantiationStateType,
        "metadata": "ListSolFunctionInstanceMetadataTypeDef",
        "nsInstanceId": str,
        "vnfPkgId": str,
    },
)
_OptionalListSolFunctionInstanceInfoTypeDef = TypedDict(
    "_OptionalListSolFunctionInstanceInfoTypeDef",
    {
        "instantiatedVnfInfo": "GetSolInstantiatedVnfInfoTypeDef",
        "vnfPkgName": str,
    },
    total=False,
)

class ListSolFunctionInstanceInfoTypeDef(
    _RequiredListSolFunctionInstanceInfoTypeDef, _OptionalListSolFunctionInstanceInfoTypeDef
):
    pass

ListSolFunctionInstanceMetadataTypeDef = TypedDict(
    "ListSolFunctionInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

ListSolFunctionInstancesInputRequestTypeDef = TypedDict(
    "ListSolFunctionInstancesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSolFunctionInstancesOutputTypeDef = TypedDict(
    "ListSolFunctionInstancesOutputTypeDef",
    {
        "functionInstances": List["ListSolFunctionInstanceInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSolFunctionPackageInfoTypeDef = TypedDict(
    "_RequiredListSolFunctionPackageInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "usageState": UsageStateType,
    },
)
_OptionalListSolFunctionPackageInfoTypeDef = TypedDict(
    "_OptionalListSolFunctionPackageInfoTypeDef",
    {
        "metadata": "ListSolFunctionPackageMetadataTypeDef",
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
    },
    total=False,
)

class ListSolFunctionPackageInfoTypeDef(
    _RequiredListSolFunctionPackageInfoTypeDef, _OptionalListSolFunctionPackageInfoTypeDef
):
    pass

ListSolFunctionPackageMetadataTypeDef = TypedDict(
    "ListSolFunctionPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

ListSolFunctionPackagesInputRequestTypeDef = TypedDict(
    "ListSolFunctionPackagesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSolFunctionPackagesOutputTypeDef = TypedDict(
    "ListSolFunctionPackagesOutputTypeDef",
    {
        "functionPackages": List["ListSolFunctionPackageInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSolNetworkInstanceInfoTypeDef = TypedDict(
    "ListSolNetworkInstanceInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": "ListSolNetworkInstanceMetadataTypeDef",
        "nsInstanceDescription": str,
        "nsInstanceName": str,
        "nsState": NsStateType,
        "nsdId": str,
        "nsdInfoId": str,
    },
)

ListSolNetworkInstanceMetadataTypeDef = TypedDict(
    "ListSolNetworkInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

ListSolNetworkInstancesInputRequestTypeDef = TypedDict(
    "ListSolNetworkInstancesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSolNetworkInstancesOutputTypeDef = TypedDict(
    "ListSolNetworkInstancesOutputTypeDef",
    {
        "networkInstances": List["ListSolNetworkInstanceInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSolNetworkOperationsInfoTypeDef = TypedDict(
    "_RequiredListSolNetworkOperationsInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "lcmOperationType": LcmOperationTypeType,
        "nsInstanceId": str,
        "operationState": NsLcmOperationStateType,
    },
)
_OptionalListSolNetworkOperationsInfoTypeDef = TypedDict(
    "_OptionalListSolNetworkOperationsInfoTypeDef",
    {
        "error": "ProblemDetailsTypeDef",
        "metadata": "ListSolNetworkOperationsMetadataTypeDef",
    },
    total=False,
)

class ListSolNetworkOperationsInfoTypeDef(
    _RequiredListSolNetworkOperationsInfoTypeDef, _OptionalListSolNetworkOperationsInfoTypeDef
):
    pass

ListSolNetworkOperationsInputRequestTypeDef = TypedDict(
    "ListSolNetworkOperationsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSolNetworkOperationsMetadataTypeDef = TypedDict(
    "ListSolNetworkOperationsMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

ListSolNetworkOperationsOutputTypeDef = TypedDict(
    "ListSolNetworkOperationsOutputTypeDef",
    {
        "networkOperations": List["ListSolNetworkOperationsInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSolNetworkPackageInfoTypeDef = TypedDict(
    "_RequiredListSolNetworkPackageInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": "ListSolNetworkPackageMetadataTypeDef",
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
    },
)
_OptionalListSolNetworkPackageInfoTypeDef = TypedDict(
    "_OptionalListSolNetworkPackageInfoTypeDef",
    {
        "nsdDesigner": str,
        "nsdId": str,
        "nsdInvariantId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
    },
    total=False,
)

class ListSolNetworkPackageInfoTypeDef(
    _RequiredListSolNetworkPackageInfoTypeDef, _OptionalListSolNetworkPackageInfoTypeDef
):
    pass

ListSolNetworkPackageMetadataTypeDef = TypedDict(
    "ListSolNetworkPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)

ListSolNetworkPackagesInputRequestTypeDef = TypedDict(
    "ListSolNetworkPackagesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSolNetworkPackagesOutputTypeDef = TypedDict(
    "ListSolNetworkPackagesOutputTypeDef",
    {
        "networkPackages": List["ListSolNetworkPackageInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkArtifactMetaTypeDef = TypedDict(
    "NetworkArtifactMetaTypeDef",
    {
        "overrides": List["ToscaOverrideTypeDef"],
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

_RequiredProblemDetailsTypeDef = TypedDict(
    "_RequiredProblemDetailsTypeDef",
    {
        "detail": str,
    },
)
_OptionalProblemDetailsTypeDef = TypedDict(
    "_OptionalProblemDetailsTypeDef",
    {
        "title": str,
    },
    total=False,
)

class ProblemDetailsTypeDef(_RequiredProblemDetailsTypeDef, _OptionalProblemDetailsTypeDef):
    pass

_RequiredPutSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "_RequiredPutSolFunctionPackageContentInputRequestTypeDef",
    {
        "file": Union[bytes, IO[bytes], StreamingBody],
        "vnfPkgId": str,
    },
)
_OptionalPutSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "_OptionalPutSolFunctionPackageContentInputRequestTypeDef",
    {
        "contentType": Literal["application/zip"],
    },
    total=False,
)

class PutSolFunctionPackageContentInputRequestTypeDef(
    _RequiredPutSolFunctionPackageContentInputRequestTypeDef,
    _OptionalPutSolFunctionPackageContentInputRequestTypeDef,
):
    pass

PutSolFunctionPackageContentMetadataTypeDef = TypedDict(
    "PutSolFunctionPackageContentMetadataTypeDef",
    {
        "vnfd": "FunctionArtifactMetaTypeDef",
    },
    total=False,
)

PutSolFunctionPackageContentOutputTypeDef = TypedDict(
    "PutSolFunctionPackageContentOutputTypeDef",
    {
        "id": str,
        "metadata": "PutSolFunctionPackageContentMetadataTypeDef",
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "_RequiredPutSolNetworkPackageContentInputRequestTypeDef",
    {
        "file": Union[bytes, IO[bytes], StreamingBody],
        "nsdInfoId": str,
    },
)
_OptionalPutSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "_OptionalPutSolNetworkPackageContentInputRequestTypeDef",
    {
        "contentType": Literal["application/zip"],
    },
    total=False,
)

class PutSolNetworkPackageContentInputRequestTypeDef(
    _RequiredPutSolNetworkPackageContentInputRequestTypeDef,
    _OptionalPutSolNetworkPackageContentInputRequestTypeDef,
):
    pass

PutSolNetworkPackageContentMetadataTypeDef = TypedDict(
    "PutSolNetworkPackageContentMetadataTypeDef",
    {
        "nsd": "NetworkArtifactMetaTypeDef",
    },
    total=False,
)

PutSolNetworkPackageContentOutputTypeDef = TypedDict(
    "PutSolNetworkPackageContentOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": "PutSolNetworkPackageContentMetadataTypeDef",
        "nsdId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

_RequiredTerminateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_RequiredTerminateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
    },
)
_OptionalTerminateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_OptionalTerminateSolNetworkInstanceInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class TerminateSolNetworkInstanceInputRequestTypeDef(
    _RequiredTerminateSolNetworkInstanceInputRequestTypeDef,
    _OptionalTerminateSolNetworkInstanceInputRequestTypeDef,
):
    pass

TerminateSolNetworkInstanceOutputTypeDef = TypedDict(
    "TerminateSolNetworkInstanceOutputTypeDef",
    {
        "nsLcmOpOccId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ToscaOverrideTypeDef = TypedDict(
    "ToscaOverrideTypeDef",
    {
        "defaultValue": str,
        "name": str,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateSolFunctionPackageInputRequestTypeDef = TypedDict(
    "UpdateSolFunctionPackageInputRequestTypeDef",
    {
        "operationalState": OperationalStateType,
        "vnfPkgId": str,
    },
)

UpdateSolFunctionPackageOutputTypeDef = TypedDict(
    "UpdateSolFunctionPackageOutputTypeDef",
    {
        "operationalState": OperationalStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
        "updateType": Literal["MODIFY_VNF_INFORMATION"],
    },
)
_OptionalUpdateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSolNetworkInstanceInputRequestTypeDef",
    {
        "modifyVnfInfoData": "UpdateSolNetworkModifyTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class UpdateSolNetworkInstanceInputRequestTypeDef(
    _RequiredUpdateSolNetworkInstanceInputRequestTypeDef,
    _OptionalUpdateSolNetworkInstanceInputRequestTypeDef,
):
    pass

UpdateSolNetworkInstanceOutputTypeDef = TypedDict(
    "UpdateSolNetworkInstanceOutputTypeDef",
    {
        "nsLcmOpOccId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSolNetworkModifyTypeDef = TypedDict(
    "UpdateSolNetworkModifyTypeDef",
    {
        "vnfConfigurableProperties": Dict[str, Any],
        "vnfInstanceId": str,
    },
)

UpdateSolNetworkPackageInputRequestTypeDef = TypedDict(
    "UpdateSolNetworkPackageInputRequestTypeDef",
    {
        "nsdInfoId": str,
        "nsdOperationalState": NsdOperationalStateType,
    },
)

UpdateSolNetworkPackageOutputTypeDef = TypedDict(
    "UpdateSolNetworkPackageOutputTypeDef",
    {
        "nsdOperationalState": NsdOperationalStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredValidateSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "_RequiredValidateSolFunctionPackageContentInputRequestTypeDef",
    {
        "file": Union[bytes, IO[bytes], StreamingBody],
        "vnfPkgId": str,
    },
)
_OptionalValidateSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "_OptionalValidateSolFunctionPackageContentInputRequestTypeDef",
    {
        "contentType": Literal["application/zip"],
    },
    total=False,
)

class ValidateSolFunctionPackageContentInputRequestTypeDef(
    _RequiredValidateSolFunctionPackageContentInputRequestTypeDef,
    _OptionalValidateSolFunctionPackageContentInputRequestTypeDef,
):
    pass

ValidateSolFunctionPackageContentMetadataTypeDef = TypedDict(
    "ValidateSolFunctionPackageContentMetadataTypeDef",
    {
        "vnfd": "FunctionArtifactMetaTypeDef",
    },
    total=False,
)

ValidateSolFunctionPackageContentOutputTypeDef = TypedDict(
    "ValidateSolFunctionPackageContentOutputTypeDef",
    {
        "id": str,
        "metadata": "ValidateSolFunctionPackageContentMetadataTypeDef",
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredValidateSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "_RequiredValidateSolNetworkPackageContentInputRequestTypeDef",
    {
        "file": Union[bytes, IO[bytes], StreamingBody],
        "nsdInfoId": str,
    },
)
_OptionalValidateSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "_OptionalValidateSolNetworkPackageContentInputRequestTypeDef",
    {
        "contentType": Literal["application/zip"],
    },
    total=False,
)

class ValidateSolNetworkPackageContentInputRequestTypeDef(
    _RequiredValidateSolNetworkPackageContentInputRequestTypeDef,
    _OptionalValidateSolNetworkPackageContentInputRequestTypeDef,
):
    pass

ValidateSolNetworkPackageContentMetadataTypeDef = TypedDict(
    "ValidateSolNetworkPackageContentMetadataTypeDef",
    {
        "nsd": "NetworkArtifactMetaTypeDef",
    },
    total=False,
)

ValidateSolNetworkPackageContentOutputTypeDef = TypedDict(
    "ValidateSolNetworkPackageContentOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": "ValidateSolNetworkPackageContentMetadataTypeDef",
        "nsdId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
