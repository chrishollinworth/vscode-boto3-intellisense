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

from .literals import (
    AuthenticationMethodType,
    ProtocolType,
    StatusType,
    SuiteRunStatusType,
    TestCaseScenarioStatusType,
    TestCaseScenarioTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateSuiteDefinitionRequestRequestTypeDef",
    "CreateSuiteDefinitionResponseTypeDef",
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    "DeviceUnderTestTypeDef",
    "GetEndpointRequestRequestTypeDef",
    "GetEndpointResponseTypeDef",
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
    "TestCaseScenarioTypeDef",
    "TestResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
)

_RequiredCreateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
    },
)
_OptionalCreateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSuiteDefinitionRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSuiteDefinitionRequestRequestTypeDef(
    _RequiredCreateSuiteDefinitionRequestRequestTypeDef,
    _OptionalCreateSuiteDefinitionRequestRequestTypeDef,
):
    pass

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
        "deviceRoleArn": str,
    },
    total=False,
)

GetEndpointRequestRequestTypeDef = TypedDict(
    "GetEndpointRequestRequestTypeDef",
    {
        "thingArn": str,
        "certificateArn": str,
        "deviceRoleArn": str,
        "authenticationMethod": AuthenticationMethodType,
    },
    total=False,
)

GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef",
    {
        "endpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "suiteRunConfiguration": "SuiteRunConfigurationTypeDef",
    },
)
_OptionalStartSuiteRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionVersion": str,
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
        "endpoint": str,
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

_RequiredSuiteDefinitionConfigurationTypeDef = TypedDict(
    "_RequiredSuiteDefinitionConfigurationTypeDef",
    {
        "suiteDefinitionName": str,
        "rootGroup": str,
        "devicePermissionRoleArn": str,
    },
)
_OptionalSuiteDefinitionConfigurationTypeDef = TypedDict(
    "_OptionalSuiteDefinitionConfigurationTypeDef",
    {
        "devices": List["DeviceUnderTestTypeDef"],
        "intendedForQualification": bool,
        "isLongDurationTest": bool,
        "protocol": ProtocolType,
    },
    total=False,
)

class SuiteDefinitionConfigurationTypeDef(
    _RequiredSuiteDefinitionConfigurationTypeDef, _OptionalSuiteDefinitionConfigurationTypeDef
):
    pass

SuiteDefinitionInformationTypeDef = TypedDict(
    "SuiteDefinitionInformationTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionName": str,
        "defaultDevices": List["DeviceUnderTestTypeDef"],
        "intendedForQualification": bool,
        "isLongDurationTest": bool,
        "protocol": ProtocolType,
        "createdAt": datetime,
    },
    total=False,
)

_RequiredSuiteRunConfigurationTypeDef = TypedDict(
    "_RequiredSuiteRunConfigurationTypeDef",
    {
        "primaryDevice": "DeviceUnderTestTypeDef",
    },
)
_OptionalSuiteRunConfigurationTypeDef = TypedDict(
    "_OptionalSuiteRunConfigurationTypeDef",
    {
        "selectedTestList": List[str],
        "parallelRun": bool,
    },
    total=False,
)

class SuiteRunConfigurationTypeDef(
    _RequiredSuiteRunConfigurationTypeDef, _OptionalSuiteRunConfigurationTypeDef
):
    pass

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
        "testScenarios": List["TestCaseScenarioTypeDef"],
    },
    total=False,
)

TestCaseScenarioTypeDef = TypedDict(
    "TestCaseScenarioTypeDef",
    {
        "testCaseScenarioId": str,
        "testCaseScenarioType": TestCaseScenarioTypeType,
        "status": TestCaseScenarioStatusType,
        "failure": str,
        "systemMessage": str,
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

UpdateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
    },
)

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
