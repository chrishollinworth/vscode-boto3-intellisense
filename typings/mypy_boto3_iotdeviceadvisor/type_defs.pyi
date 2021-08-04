"""
Type annotations for iotdeviceadvisor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionRequestRequestTypeDef

    data: CreateSuiteDefinitionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import StatusType, SuiteRunStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateSuiteDefinitionRequestRequestTypeDef",
    "CreateSuiteDefinitionResponseTypeDef",
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    "DeviceUnderTestTypeDef",
    "GetSuiteDefinitionRequestRequestTypeDef",
    "GetSuiteDefinitionResponseTypeDef",
    "GetSuiteRunReportRequestRequestTypeDef",
    "GetSuiteRunReportResponseTypeDef",
    "GetSuiteRunRequestRequestTypeDef",
    "GetSuiteRunResponseTypeDef",
    "GroupResultTypeDef",
    "ListSuiteDefinitionsRequestRequestTypeDef",
    "ListSuiteDefinitionsResponseTypeDef",
    "ListSuiteRunsRequestRequestTypeDef",
    "ListSuiteRunsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSuiteRunRequestRequestTypeDef",
    "StartSuiteRunResponseTypeDef",
    "StopSuiteRunRequestRequestTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationTypeDef",
    "SuiteRunInformationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestCaseRunTypeDef",
    "TestResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
)

CreateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "CreateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSuiteDefinitionResponseTypeDef = TypedDict(
    "CreateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)

DeviceUnderTestTypeDef = TypedDict(
    "DeviceUnderTestTypeDef",
    {
        "thingArn": str,
        "certificateArn": str,
    },
    total=False,
)

_RequiredGetSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredGetSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
_OptionalGetSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalGetSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionVersion": str,
    },
    total=False,
)

class GetSuiteDefinitionRequestRequestTypeDef(
    _RequiredGetSuiteDefinitionRequestRequestTypeDef,
    _OptionalGetSuiteDefinitionRequestRequestTypeDef,
):
    pass

GetSuiteDefinitionResponseTypeDef = TypedDict(
    "GetSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionVersion": str,
        "latestVersion": str,
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRunReportRequestRequestTypeDef = TypedDict(
    "GetSuiteRunReportRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

GetSuiteRunReportResponseTypeDef = TypedDict(
    "GetSuiteRunReportResponseTypeDef",
    {
        "qualificationReportDownloadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRunRequestRequestTypeDef = TypedDict(
    "GetSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

GetSuiteRunResponseTypeDef = TypedDict(
    "GetSuiteRunResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "suiteRunId": str,
        "suiteRunArn": str,
        "suiteRunConfiguration": "SuiteRunConfigurationTypeDef",
        "testResult": "TestResultTypeDef",
        "startTime": datetime,
        "endTime": datetime,
        "status": SuiteRunStatusType,
        "errorReason": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupResultTypeDef = TypedDict(
    "GroupResultTypeDef",
    {
        "groupId": str,
        "groupName": str,
        "tests": List["TestCaseRunTypeDef"],
    },
    total=False,
)

ListSuiteDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSuiteDefinitionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSuiteDefinitionsResponseTypeDef = TypedDict(
    "ListSuiteDefinitionsResponseTypeDef",
    {
        "suiteDefinitionInformationList": List["SuiteDefinitionInformationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSuiteRunsRequestRequestTypeDef = TypedDict(
    "ListSuiteRunsRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSuiteRunsResponseTypeDef = TypedDict(
    "ListSuiteRunsResponseTypeDef",
    {
        "suiteRunsList": List["SuiteRunInformationTypeDef"],
        "nextToken": str,
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

_RequiredStartSuiteRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
_OptionalStartSuiteRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionVersion": str,
        "suiteRunConfiguration": "SuiteRunConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class StartSuiteRunRequestRequestTypeDef(
    _RequiredStartSuiteRunRequestRequestTypeDef, _OptionalStartSuiteRunRequestRequestTypeDef
):
    pass

StartSuiteRunResponseTypeDef = TypedDict(
    "StartSuiteRunResponseTypeDef",
    {
        "suiteRunId": str,
        "suiteRunArn": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSuiteRunRequestRequestTypeDef = TypedDict(
    "StopSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

SuiteDefinitionConfigurationTypeDef = TypedDict(
    "SuiteDefinitionConfigurationTypeDef",
    {
        "suiteDefinitionName": str,
        "devices": List["DeviceUnderTestTypeDef"],
        "intendedForQualification": bool,
        "rootGroup": str,
        "devicePermissionRoleArn": str,
    },
    total=False,
)

SuiteDefinitionInformationTypeDef = TypedDict(
    "SuiteDefinitionInformationTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionName": str,
        "defaultDevices": List["DeviceUnderTestTypeDef"],
        "intendedForQualification": bool,
        "createdAt": datetime,
    },
    total=False,
)

SuiteRunConfigurationTypeDef = TypedDict(
    "SuiteRunConfigurationTypeDef",
    {
        "primaryDevice": "DeviceUnderTestTypeDef",
        "selectedTestList": List[str],
    },
    total=False,
)

SuiteRunInformationTypeDef = TypedDict(
    "SuiteRunInformationTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "suiteDefinitionName": str,
        "suiteRunId": str,
        "createdAt": datetime,
        "startedAt": datetime,
        "endAt": datetime,
        "status": SuiteRunStatusType,
        "passed": int,
        "failed": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TestCaseRunTypeDef = TypedDict(
    "TestCaseRunTypeDef",
    {
        "testCaseRunId": str,
        "testCaseDefinitionId": str,
        "testCaseDefinitionName": str,
        "status": StatusType,
        "startTime": datetime,
        "endTime": datetime,
        "logUrl": str,
        "warnings": str,
        "failure": str,
    },
    total=False,
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "groups": List["GroupResultTypeDef"],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
_OptionalUpdateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
    },
    total=False,
)

class UpdateSuiteDefinitionRequestRequestTypeDef(
    _RequiredUpdateSuiteDefinitionRequestRequestTypeDef,
    _OptionalUpdateSuiteDefinitionRequestRequestTypeDef,
):
    pass

UpdateSuiteDefinitionResponseTypeDef = TypedDict(
    "UpdateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "suiteDefinitionVersion": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
