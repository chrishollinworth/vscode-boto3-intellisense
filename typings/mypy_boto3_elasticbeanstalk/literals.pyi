"""
Type annotations for elasticbeanstalk service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/literals.html)

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.literals import ActionHistoryStatusType

    data: ActionHistoryStatusType = "Completed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionHistoryStatusType",
    "ActionStatusType",
    "ActionTypeType",
    "ApplicationVersionStatusType",
    "ComputeTypeType",
    "ConfigurationDeploymentStatusType",
    "ConfigurationOptionValueTypeType",
    "DescribeApplicationVersionsPaginatorName",
    "DescribeEnvironmentManagedActionHistoryPaginatorName",
    "DescribeEnvironmentsPaginatorName",
    "DescribeEventsPaginatorName",
    "EnvironmentExistsWaiterName",
    "EnvironmentHealthAttributeType",
    "EnvironmentHealthStatusType",
    "EnvironmentHealthType",
    "EnvironmentInfoTypeType",
    "EnvironmentStatusType",
    "EnvironmentTerminatedWaiterName",
    "EnvironmentUpdatedWaiterName",
    "EventSeverityType",
    "FailureTypeType",
    "InstancesHealthAttributeType",
    "ListPlatformVersionsPaginatorName",
    "PlatformStatusType",
    "SourceRepositoryType",
    "SourceTypeType",
    "ValidationSeverityType",
)

ActionHistoryStatusType = Literal["Completed", "Failed", "Unknown"]
ActionStatusType = Literal["Pending", "Running", "Scheduled", "Unknown"]
ActionTypeType = Literal["InstanceRefresh", "PlatformUpdate", "Unknown"]
ApplicationVersionStatusType = Literal[
    "Building", "Failed", "Processed", "Processing", "Unprocessed"
]
ComputeTypeType = Literal["BUILD_GENERAL1_LARGE", "BUILD_GENERAL1_MEDIUM", "BUILD_GENERAL1_SMALL"]
ConfigurationDeploymentStatusType = Literal["deployed", "failed", "pending"]
ConfigurationOptionValueTypeType = Literal["List", "Scalar"]
DescribeApplicationVersionsPaginatorName = Literal["describe_application_versions"]
DescribeEnvironmentManagedActionHistoryPaginatorName = Literal[
    "describe_environment_managed_action_history"
]
DescribeEnvironmentsPaginatorName = Literal["describe_environments"]
DescribeEventsPaginatorName = Literal["describe_events"]
EnvironmentExistsWaiterName = Literal["environment_exists"]
EnvironmentHealthAttributeType = Literal[
    "All",
    "ApplicationMetrics",
    "Causes",
    "Color",
    "HealthStatus",
    "InstancesHealth",
    "RefreshedAt",
    "Status",
]
EnvironmentHealthStatusType = Literal[
    "Degraded", "Info", "NoData", "Ok", "Pending", "Severe", "Suspended", "Unknown", "Warning"
]
EnvironmentHealthType = Literal["Green", "Grey", "Red", "Yellow"]
EnvironmentInfoTypeType = Literal["bundle", "tail"]
EnvironmentStatusType = Literal[
    "Aborting",
    "Launching",
    "LinkingFrom",
    "LinkingTo",
    "Ready",
    "Terminated",
    "Terminating",
    "Updating",
]
EnvironmentTerminatedWaiterName = Literal["environment_terminated"]
EnvironmentUpdatedWaiterName = Literal["environment_updated"]
EventSeverityType = Literal["DEBUG", "ERROR", "FATAL", "INFO", "TRACE", "WARN"]
FailureTypeType = Literal[
    "CancellationFailed",
    "InternalFailure",
    "InvalidEnvironmentState",
    "PermissionsError",
    "RollbackFailed",
    "RollbackSuccessful",
    "UpdateCancelled",
]
InstancesHealthAttributeType = Literal[
    "All",
    "ApplicationMetrics",
    "AvailabilityZone",
    "Causes",
    "Color",
    "Deployment",
    "HealthStatus",
    "InstanceType",
    "LaunchedAt",
    "RefreshedAt",
    "System",
]
ListPlatformVersionsPaginatorName = Literal["list_platform_versions"]
PlatformStatusType = Literal["Creating", "Deleted", "Deleting", "Failed", "Ready"]
SourceRepositoryType = Literal["CodeCommit", "S3"]
SourceTypeType = Literal["Git", "Zip"]
ValidationSeverityType = Literal["error", "warning"]
