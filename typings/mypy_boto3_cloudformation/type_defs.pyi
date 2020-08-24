"""
Main interface for cloudformation service type definitions.

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = {...}
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
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "AutoDeploymentTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "DeploymentTargetsTypeDef",
    "ExportTypeDef",
    "LoggingConfigTypeDef",
    "OutputTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsOutputTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterTypeOutputTypeDef",
    "ResourceToImportTypeDef",
    "StackInstanceFilterTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WaiterConfigTypeDef",
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef",
    {"Status": Literal["SUCCEEDED", "FAILED", "SKIPPED"], "StatusReason": str},
    total=False,
)

AccountLimitTypeDef = TypedDict("AccountLimitTypeDef", {"Name": str, "Value": int}, total=False)

AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef", {"Enabled": bool, "RetainStacksOnAccountRemoval": bool}, total=False
)

ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
    },
    total=False,
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {"Type": Literal["Resource"], "ResourceChange": "ResourceChangeTypeDef"},
    total=False,
)

DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {"Accounts": List[str], "OrganizationalUnitIds": List[str]},
    total=False,
)

ExportTypeDef = TypedDict(
    "ExportTypeDef", {"ExportingStackId": str, "Name": str, "Value": str}, total=False
)

LoggingConfigTypeDef = TypedDict("LoggingConfigTypeDef", {"LogRoleArn": str, "LogGroupName": str})

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {"OutputKey": str, "OutputValue": str, "Description": str, "ExportName": str},
    total=False,
)

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef", {"AllowedValues": List[str]}, total=False
)

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": "ParameterConstraintsTypeDef",
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

PhysicalResourceIdContextKeyValuePairTypeDef = TypedDict(
    "PhysicalResourceIdContextKeyValuePairTypeDef", {"Key": str, "Value": str}
)

PropertyDifferenceTypeDef = TypedDict(
    "PropertyDifferenceTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": Literal["ADD", "REMOVE", "NOT_EQUAL"],
    },
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": Literal["Static", "Dynamic"],
        "ChangeSource": Literal[
            "ResourceReference",
            "ParameterReference",
            "ResourceAttribute",
            "DirectModification",
            "Automatic",
        ],
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": Literal["Add", "Modify", "Remove", "Import"],
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Literal["True", "False", "Conditional"],
        "Scope": List[
            Literal[
                "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
            ]
        ],
        "Details": List["ResourceChangeDetailTypeDef"],
    },
    total=False,
)

ResourceIdentifierSummaryTypeDef = TypedDict(
    "ResourceIdentifierSummaryTypeDef",
    {"ResourceType": str, "LogicalResourceIds": List[str], "ResourceIdentifiers": List[str]},
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": Literal[
            "Properties", "Metadata", "CreationPolicy", "UpdatePolicy", "DeletionPolicy", "Tags"
        ],
        "Name": str,
        "RequiresRecreation": Literal["Never", "Conditionally", "Always"],
    },
    total=False,
)

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {"RollbackTriggers": List["RollbackTriggerTypeDef"], "MonitoringTimeInMinutes": int},
    total=False,
)

RollbackTriggerTypeDef = TypedDict("RollbackTriggerTypeDef", {"Arn": str, "Type": str})

_RequiredStackDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackDriftInformationSummaryTypeDef",
    {"StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"]},
)
_OptionalStackDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackDriftInformationSummaryTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackDriftInformationSummaryTypeDef(
    _RequiredStackDriftInformationSummaryTypeDef, _OptionalStackDriftInformationSummaryTypeDef
):
    pass


_RequiredStackDriftInformationTypeDef = TypedDict(
    "_RequiredStackDriftInformationTypeDef",
    {"StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"]},
)
_OptionalStackDriftInformationTypeDef = TypedDict(
    "_OptionalStackDriftInformationTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackDriftInformationTypeDef(
    _RequiredStackDriftInformationTypeDef, _OptionalStackDriftInformationTypeDef
):
    pass


_RequiredStackEventTypeDef = TypedDict(
    "_RequiredStackEventTypeDef",
    {"StackId": str, "EventId": str, "StackName": str, "Timestamp": datetime},
)
_OptionalStackEventTypeDef = TypedDict(
    "_OptionalStackEventTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StackEventTypeDef(_RequiredStackEventTypeDef, _OptionalStackEventTypeDef):
    pass


StackInstanceComprehensiveStatusTypeDef = TypedDict(
    "StackInstanceComprehensiveStatusTypeDef",
    {
        "DetailedStatus": Literal[
            "PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED", "INOPERABLE"
        ]
    },
    total=False,
)

StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StatusReason": str,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "OrganizationalUnitId": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List["ParameterTypeDef"],
        "Status": Literal["CURRENT", "OUTDATED", "INOPERABLE"],
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

_RequiredStackResourceDetailTypeDef = TypedDict(
    "_RequiredStackResourceDetailTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackResourceDetailTypeDef = TypedDict(
    "_OptionalStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
    },
    total=False,
)


class StackResourceDetailTypeDef(
    _RequiredStackResourceDetailTypeDef, _OptionalStackResourceDetailTypeDef
):
    pass


_RequiredStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationSummaryTypeDef",
    {"StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"]},
)
_OptionalStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationSummaryTypeDef",
    {"LastCheckTimestamp": datetime},
    total=False,
)


class StackResourceDriftInformationSummaryTypeDef(
    _RequiredStackResourceDriftInformationSummaryTypeDef,
    _OptionalStackResourceDriftInformationSummaryTypeDef,
):
    pass


_RequiredStackResourceDriftInformationTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationTypeDef",
    {"StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"]},
)
_OptionalStackResourceDriftInformationTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackResourceDriftInformationTypeDef(
    _RequiredStackResourceDriftInformationTypeDef, _OptionalStackResourceDriftInformationTypeDef
):
    pass


_RequiredStackResourceDriftTypeDef = TypedDict(
    "_RequiredStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": Literal["IN_SYNC", "MODIFIED", "DELETED", "NOT_CHECKED"],
        "Timestamp": datetime,
    },
)
_OptionalStackResourceDriftTypeDef = TypedDict(
    "_OptionalStackResourceDriftTypeDef",
    {
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List["PhysicalResourceIdContextKeyValuePairTypeDef"],
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List["PropertyDifferenceTypeDef"],
    },
    total=False,
)


class StackResourceDriftTypeDef(
    _RequiredStackResourceDriftTypeDef, _OptionalStackResourceDriftTypeDef
):
    pass


_RequiredStackResourceSummaryTypeDef = TypedDict(
    "_RequiredStackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackResourceSummaryTypeDef = TypedDict(
    "_OptionalStackResourceSummaryTypeDef",
    {
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "DriftInformation": "StackResourceDriftInformationSummaryTypeDef",
    },
    total=False,
)


class StackResourceSummaryTypeDef(
    _RequiredStackResourceSummaryTypeDef, _OptionalStackResourceSummaryTypeDef
):
    pass


_RequiredStackResourceTypeDef = TypedDict(
    "_RequiredStackResourceTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "DELETE_SKIPPED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_FAILED",
            "UPDATE_COMPLETE",
            "IMPORT_FAILED",
            "IMPORT_COMPLETE",
            "IMPORT_IN_PROGRESS",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackResourceTypeDef = TypedDict(
    "_OptionalStackResourceTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
    },
    total=False,
)


class StackResourceTypeDef(_RequiredStackResourceTypeDef, _OptionalStackResourceTypeDef):
    pass


StackSetDriftDetectionDetailsTypeDef = TypedDict(
    "StackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"],
        "DriftDetectionStatus": Literal[
            "COMPLETED", "FAILED", "PARTIAL_SUCCESS", "IN_PROGRESS", "STOPPED"
        ],
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

StackSetOperationPreferencesTypeDef = TypedDict(
    "StackSetOperationPreferencesTypeDef",
    {
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"],
        "StatusReason": str,
        "AccountGateResult": "AccountGateResultTypeDef",
        "OrganizationalUnitId": str,
    },
    total=False,
)

StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED", "QUEUED"],
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

StackSetOperationTypeDef = TypedDict(
    "StackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": Literal["CREATE", "UPDATE", "DELETE", "DETECT_DRIFT"],
        "Status": Literal["RUNNING", "SUCCEEDED", "FAILED", "STOPPING", "STOPPED", "QUEUED"],
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
    },
    total=False,
)

StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": Literal["SERVICE_MANAGED", "SELF_MANAGED"],
        "DriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackSetTypeDef = TypedDict(
    "StackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": Literal["ACTIVE", "DELETED"],
        "TemplateBody": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List["TagTypeDef"],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": Literal["SERVICE_MANAGED", "SELF_MANAGED"],
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

_RequiredStackSummaryTypeDef = TypedDict(
    "_RequiredStackSummaryTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackSummaryTypeDef = TypedDict(
    "_OptionalStackSummaryTypeDef",
    {
        "StackId": str,
        "TemplateDescription": str,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationSummaryTypeDef",
    },
    total=False,
)


class StackSummaryTypeDef(_RequiredStackSummaryTypeDef, _OptionalStackSummaryTypeDef):
    pass


_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_FAILED",
            "CREATE_COMPLETE",
            "ROLLBACK_IN_PROGRESS",
            "ROLLBACK_FAILED",
            "ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_FAILED",
            "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_IN_PROGRESS",
            "UPDATE_ROLLBACK_FAILED",
            "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
            "UPDATE_ROLLBACK_COMPLETE",
            "REVIEW_IN_PROGRESS",
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_ROLLBACK_IN_PROGRESS",
            "IMPORT_ROLLBACK_FAILED",
            "IMPORT_ROLLBACK_COMPLETE",
        ],
    },
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "StackId": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Outputs": List["OutputTypeDef"],
        "RoleARN": str,
        "Tags": List["TagTypeDef"],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationTypeDef",
    },
    total=False,
)


class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TemplateParameterTypeDef = TypedDict(
    "TemplateParameterTypeDef",
    {"ParameterKey": str, "DefaultValue": str, "NoEcho": bool, "Description": str},
    total=False,
)

TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": Literal["RESOURCE"],
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)

TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": Literal["RESOURCE"],
        "TypeName": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)

CreateChangeSetOutputTypeDef = TypedDict(
    "CreateChangeSetOutputTypeDef", {"Id": str, "StackId": str}, total=False
)

CreateStackInstancesOutputTypeDef = TypedDict(
    "CreateStackInstancesOutputTypeDef", {"OperationId": str}, total=False
)

CreateStackOutputTypeDef = TypedDict("CreateStackOutputTypeDef", {"StackId": str}, total=False)

CreateStackSetOutputTypeDef = TypedDict(
    "CreateStackSetOutputTypeDef", {"StackSetId": str}, total=False
)

DeleteStackInstancesOutputTypeDef = TypedDict(
    "DeleteStackInstancesOutputTypeDef", {"OperationId": str}, total=False
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {"AccountLimits": List["AccountLimitTypeDef"], "NextToken": str},
    total=False,
)

DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "CreationTime": datetime,
        "ExecutionStatus": Literal[
            "UNAVAILABLE",
            "AVAILABLE",
            "EXECUTE_IN_PROGRESS",
            "EXECUTE_COMPLETE",
            "EXECUTE_FAILED",
            "OBSOLETE",
        ],
        "Status": Literal[
            "CREATE_PENDING", "CREATE_IN_PROGRESS", "CREATE_COMPLETE", "DELETE_COMPLETE", "FAILED"
        ],
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "Tags": List["TagTypeDef"],
        "Changes": List["ChangeTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredDescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "_RequiredDescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "DetectionStatus": Literal[
            "DETECTION_IN_PROGRESS", "DETECTION_FAILED", "DETECTION_COMPLETE"
        ],
        "Timestamp": datetime,
    },
)
_OptionalDescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "_OptionalDescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackDriftStatus": Literal["DRIFTED", "IN_SYNC", "UNKNOWN", "NOT_CHECKED"],
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
    },
    total=False,
)


class DescribeStackDriftDetectionStatusOutputTypeDef(
    _RequiredDescribeStackDriftDetectionStatusOutputTypeDef,
    _OptionalDescribeStackDriftDetectionStatusOutputTypeDef,
):
    pass


DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {"StackEvents": List["StackEventTypeDef"], "NextToken": str},
    total=False,
)

DescribeStackInstanceOutputTypeDef = TypedDict(
    "DescribeStackInstanceOutputTypeDef", {"StackInstance": "StackInstanceTypeDef"}, total=False
)

_RequiredDescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "_RequiredDescribeStackResourceDriftsOutputTypeDef",
    {"StackResourceDrifts": List["StackResourceDriftTypeDef"]},
)
_OptionalDescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "_OptionalDescribeStackResourceDriftsOutputTypeDef", {"NextToken": str}, total=False
)


class DescribeStackResourceDriftsOutputTypeDef(
    _RequiredDescribeStackResourceDriftsOutputTypeDef,
    _OptionalDescribeStackResourceDriftsOutputTypeDef,
):
    pass


DescribeStackResourceOutputTypeDef = TypedDict(
    "DescribeStackResourceOutputTypeDef",
    {"StackResourceDetail": "StackResourceDetailTypeDef"},
    total=False,
)

DescribeStackResourcesOutputTypeDef = TypedDict(
    "DescribeStackResourcesOutputTypeDef",
    {"StackResources": List["StackResourceTypeDef"]},
    total=False,
)

DescribeStackSetOperationOutputTypeDef = TypedDict(
    "DescribeStackSetOperationOutputTypeDef",
    {"StackSetOperation": "StackSetOperationTypeDef"},
    total=False,
)

DescribeStackSetOutputTypeDef = TypedDict(
    "DescribeStackSetOutputTypeDef", {"StackSet": "StackSetTypeDef"}, total=False
)

DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef", {"Stacks": List["StackTypeDef"], "NextToken": str}, total=False
)

DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": Literal["RESOURCE"],
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "Description": str,
        "Schema": str,
        "ProvisioningType": Literal["NON_PROVISIONABLE", "IMMUTABLE", "FULLY_MUTABLE"],
        "DeprecatedStatus": Literal["LIVE", "DEPRECATED"],
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
    },
    total=False,
)

DescribeTypeRegistrationOutputTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputTypeDef",
    {
        "ProgressStatus": Literal["COMPLETE", "IN_PROGRESS", "FAILED"],
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
    },
    total=False,
)

DetectStackDriftOutputTypeDef = TypedDict(
    "DetectStackDriftOutputTypeDef", {"StackDriftDetectionId": str}
)

DetectStackResourceDriftOutputTypeDef = TypedDict(
    "DetectStackResourceDriftOutputTypeDef", {"StackResourceDrift": "StackResourceDriftTypeDef"}
)

DetectStackSetDriftOutputTypeDef = TypedDict(
    "DetectStackSetDriftOutputTypeDef", {"OperationId": str}, total=False
)

EstimateTemplateCostOutputTypeDef = TypedDict(
    "EstimateTemplateCostOutputTypeDef", {"Url": str}, total=False
)

GetStackPolicyOutputTypeDef = TypedDict(
    "GetStackPolicyOutputTypeDef", {"StackPolicyBody": str}, total=False
)

GetTemplateOutputTypeDef = TypedDict(
    "GetTemplateOutputTypeDef",
    {"TemplateBody": str, "StagesAvailable": List[Literal["Original", "Processed"]]},
    total=False,
)

GetTemplateSummaryOutputTypeDef = TypedDict(
    "GetTemplateSummaryOutputTypeDef",
    {
        "Parameters": List["ParameterDeclarationTypeDef"],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List["ResourceIdentifierSummaryTypeDef"],
    },
    total=False,
)

ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {"Summaries": List["ChangeSetSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef", {"Exports": List["ExportTypeDef"], "NextToken": str}, total=False
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef", {"Imports": List[str], "NextToken": str}, total=False
)

ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {"Summaries": List["StackInstanceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {"StackResourceSummaries": List["StackResourceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {"Summaries": List["StackSetOperationResultSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {"Summaries": List["StackSetOperationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {"Summaries": List["StackSetSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {"StackSummaries": List["StackSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTypeRegistrationsOutputTypeDef = TypedDict(
    "ListTypeRegistrationsOutputTypeDef",
    {"RegistrationTokenList": List[str], "NextToken": str},
    total=False,
)

ListTypeVersionsOutputTypeDef = TypedDict(
    "ListTypeVersionsOutputTypeDef",
    {"TypeVersionSummaries": List["TypeVersionSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTypesOutputTypeDef = TypedDict(
    "ListTypesOutputTypeDef",
    {"TypeSummaries": List["TypeSummaryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterTypeOutputTypeDef = TypedDict(
    "RegisterTypeOutputTypeDef", {"RegistrationToken": str}, total=False
)

ResourceToImportTypeDef = TypedDict(
    "ResourceToImportTypeDef",
    {"ResourceType": str, "LogicalResourceId": str, "ResourceIdentifier": Dict[str, str]},
)

StackInstanceFilterTypeDef = TypedDict(
    "StackInstanceFilterTypeDef", {"Name": Literal["DETAILED_STATUS"], "Values": str}, total=False
)

UpdateStackInstancesOutputTypeDef = TypedDict(
    "UpdateStackInstancesOutputTypeDef", {"OperationId": str}, total=False
)

UpdateStackOutputTypeDef = TypedDict("UpdateStackOutputTypeDef", {"StackId": str}, total=False)

UpdateStackSetOutputTypeDef = TypedDict(
    "UpdateStackSetOutputTypeDef", {"OperationId": str}, total=False
)

UpdateTerminationProtectionOutputTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputTypeDef", {"StackId": str}, total=False
)

ValidateTemplateOutputTypeDef = TypedDict(
    "ValidateTemplateOutputTypeDef",
    {
        "Parameters": List["TemplateParameterTypeDef"],
        "Description": str,
        "Capabilities": List[
            Literal["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]
        ],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
