"""
Main interface for iotdeviceadvisor service type definitions.

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import DeviceUnderTestTypeDef

    data: DeviceUnderTestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeviceUnderTestTypeDef",
    "GroupResultTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationTypeDef",
    "SuiteRunInformationTypeDef",
    "TestCaseCategoryTypeDef",
    "TestCaseDefinitionTypeDef",
    "TestCaseRunTypeDef",
    "TestCaseTypeDef",
    "TestResultTypeDef",
    "CreateSuiteDefinitionResponseTypeDef",
    "GetSuiteDefinitionResponseTypeDef",
    "GetSuiteRunReportResponseTypeDef",
    "GetSuiteRunResponseTypeDef",
    "ListSuiteDefinitionsResponseTypeDef",
    "ListSuiteRunsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestCasesResponseTypeDef",
    "StartSuiteRunResponseTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
)

DeviceUnderTestTypeDef = TypedDict(
    "DeviceUnderTestTypeDef", {"thingArn": str, "certificateArn": str}, total=False
)

GroupResultTypeDef = TypedDict(
    "GroupResultTypeDef",
    {"groupId": str, "groupName": str, "tests": List["TestCaseRunTypeDef"]},
    total=False,
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
        "secondaryDevice": "DeviceUnderTestTypeDef",
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
        "status": Literal[
            "PASS", "FAIL", "CANCELED", "PENDING", "RUNNING", "PASS_WITH_WARNINGS", "ERROR"
        ],
        "passed": int,
        "failed": int,
    },
    total=False,
)

TestCaseCategoryTypeDef = TypedDict(
    "TestCaseCategoryTypeDef", {"name": str, "tests": List["TestCaseTypeDef"]}, total=False
)

TestCaseDefinitionTypeDef = TypedDict(
    "TestCaseDefinitionTypeDef", {"id": str, "testCaseVersion": str}, total=False
)

TestCaseRunTypeDef = TypedDict(
    "TestCaseRunTypeDef",
    {
        "testCaseRunId": str,
        "testCaseDefinitionId": str,
        "testCaseDefinitionName": str,
        "status": Literal[
            "PASS", "FAIL", "CANCELED", "PENDING", "RUNNING", "PASS_WITH_WARNINGS", "ERROR"
        ],
        "startTime": datetime,
        "endTime": datetime,
        "logUrl": str,
        "warnings": str,
        "failure": str,
    },
    total=False,
)

TestCaseTypeDef = TypedDict(
    "TestCaseTypeDef",
    {"name": str, "configuration": Dict[str, str], "test": "TestCaseDefinitionTypeDef"},
    total=False,
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef", {"groups": List["GroupResultTypeDef"]}, total=False
)

CreateSuiteDefinitionResponseTypeDef = TypedDict(
    "CreateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "createdAt": datetime,
    },
    total=False,
)

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
    },
    total=False,
)

GetSuiteRunReportResponseTypeDef = TypedDict(
    "GetSuiteRunReportResponseTypeDef", {"qualificationReportDownloadUrl": str}, total=False
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
        "status": Literal[
            "PASS", "FAIL", "CANCELED", "PENDING", "RUNNING", "PASS_WITH_WARNINGS", "ERROR"
        ],
        "errorReason": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ListSuiteDefinitionsResponseTypeDef = TypedDict(
    "ListSuiteDefinitionsResponseTypeDef",
    {"suiteDefinitionInformationList": List["SuiteDefinitionInformationTypeDef"], "nextToken": str},
    total=False,
)

ListSuiteRunsResponseTypeDef = TypedDict(
    "ListSuiteRunsResponseTypeDef",
    {"suiteRunsList": List["SuiteRunInformationTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListTestCasesResponseTypeDef = TypedDict(
    "ListTestCasesResponseTypeDef",
    {
        "categories": List["TestCaseCategoryTypeDef"],
        "rootGroupConfiguration": Dict[str, str],
        "groupConfiguration": Dict[str, str],
        "nextToken": str,
    },
    total=False,
)

StartSuiteRunResponseTypeDef = TypedDict(
    "StartSuiteRunResponseTypeDef",
    {"suiteRunId": str, "suiteRunArn": str, "createdAt": datetime},
    total=False,
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
    },
    total=False,
)
