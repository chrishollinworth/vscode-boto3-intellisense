"""
Type annotations for apptest service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apptest/literals.html)

Usage::

    ```python
    from mypy_boto3_apptest.literals import CaptureToolType

    data: CaptureToolType = "AWS DMS"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CaptureToolType",
    "CloudFormationActionTypeType",
    "ComparisonStatusEnumType",
    "DataSetTypeType",
    "FormatType",
    "ListTestCasesPaginatorName",
    "ListTestConfigurationsPaginatorName",
    "ListTestRunStepsPaginatorName",
    "ListTestRunTestCasesPaginatorName",
    "ListTestRunsPaginatorName",
    "ListTestSuitesPaginatorName",
    "M2ManagedActionTypeType",
    "M2ManagedRuntimeType",
    "M2NonManagedActionTypeType",
    "M2NonManagedRuntimeType",
    "ScriptTypeType",
    "SourceDatabaseType",
    "StepRunStatusType",
    "TargetDatabaseType",
    "TestCaseLifecycleType",
    "TestCaseRunStatusType",
    "TestConfigurationLifecycleType",
    "TestRunStatusType",
    "TestSuiteLifecycleType",
)

CaptureToolType = Literal["AWS DMS", "Precisely"]
CloudFormationActionTypeType = Literal["Create", "Delete"]
ComparisonStatusEnumType = Literal["Different", "Equal", "Equivalent"]
DataSetTypeType = Literal["PS"]
FormatType = Literal["FIXED", "LINE_SEQUENTIAL", "VARIABLE"]
ListTestCasesPaginatorName = Literal["list_test_cases"]
ListTestConfigurationsPaginatorName = Literal["list_test_configurations"]
ListTestRunStepsPaginatorName = Literal["list_test_run_steps"]
ListTestRunTestCasesPaginatorName = Literal["list_test_run_test_cases"]
ListTestRunsPaginatorName = Literal["list_test_runs"]
ListTestSuitesPaginatorName = Literal["list_test_suites"]
M2ManagedActionTypeType = Literal["Configure", "Deconfigure"]
M2ManagedRuntimeType = Literal["MicroFocus"]
M2NonManagedActionTypeType = Literal["Configure", "Deconfigure"]
M2NonManagedRuntimeType = Literal["BluAge"]
ScriptTypeType = Literal["Selenium"]
SourceDatabaseType = Literal["z/OS-DB2"]
StepRunStatusType = Literal["Failed", "Running", "Success"]
TargetDatabaseType = Literal["PostgreSQL"]
TestCaseLifecycleType = Literal["Active", "Deleting"]
TestCaseRunStatusType = Literal["Failed", "Running", "Success"]
TestConfigurationLifecycleType = Literal["Active", "Deleting"]
TestRunStatusType = Literal["Deleting", "Failed", "Running", "Success"]
TestSuiteLifecycleType = Literal["Active", "Creating", "Deleting", "Failed", "Updating"]
