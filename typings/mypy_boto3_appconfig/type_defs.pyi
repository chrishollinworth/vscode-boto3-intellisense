"""
Main interface for appconfig service type definitions.

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import ApplicationTypeDef

    data: ApplicationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "EnvironmentTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "MonitorTypeDef",
    "ValidatorTypeDef",
    "ApplicationsTypeDef",
    "ConfigurationProfileTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "EnvironmentsTypeDef",
    "HostedConfigurationVersionTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "ResourceTagsTypeDef",
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef", {"Id": str, "Name": str, "Description": str}, total=False
)

ConfigurationProfileSummaryTypeDef = TypedDict(
    "ConfigurationProfileSummaryTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "LocationUri": str,
        "ValidatorTypes": List[Literal["JSON_SCHEMA", "LAMBDA"]],
    },
    total=False,
)

DeploymentEventTypeDef = TypedDict(
    "DeploymentEventTypeDef",
    {
        "EventType": Literal[
            "PERCENTAGE_UPDATED",
            "ROLLBACK_STARTED",
            "ROLLBACK_COMPLETED",
            "BAKE_TIME_STARTED",
            "DEPLOYMENT_STARTED",
            "DEPLOYMENT_COMPLETED",
        ],
        "TriggeredBy": Literal["USER", "APPCONFIG", "CLOUDWATCH_ALARM", "INTERNAL_ERROR"],
        "Description": str,
        "OccurredAt": datetime,
    },
    total=False,
)

DeploymentStrategyTypeDef = TypedDict(
    "DeploymentStrategyTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": Literal["LINEAR", "EXPONENTIAL"],
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": Literal["NONE", "SSM_DOCUMENT"],
    },
    total=False,
)

DeploymentSummaryTypeDef = TypedDict(
    "DeploymentSummaryTypeDef",
    {
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationVersion": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": Literal["LINEAR", "EXPONENTIAL"],
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": Literal[
            "BAKING", "VALIDATING", "DEPLOYING", "COMPLETE", "ROLLING_BACK", "ROLLED_BACK"
        ],
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": Literal["READY_FOR_DEPLOYMENT", "DEPLOYING", "ROLLING_BACK", "ROLLED_BACK"],
        "Monitors": List["MonitorTypeDef"],
    },
    total=False,
)

HostedConfigurationVersionSummaryTypeDef = TypedDict(
    "HostedConfigurationVersionSummaryTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "ContentType": str,
    },
    total=False,
)

MonitorTypeDef = TypedDict("MonitorTypeDef", {"AlarmArn": str, "AlarmRoleArn": str}, total=False)

ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef", {"Type": Literal["JSON_SCHEMA", "LAMBDA"], "Content": str}
)

ApplicationsTypeDef = TypedDict(
    "ApplicationsTypeDef", {"Items": List["ApplicationTypeDef"], "NextToken": str}, total=False
)

ConfigurationProfileTypeDef = TypedDict(
    "ConfigurationProfileTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
    },
    total=False,
)

ConfigurationProfilesTypeDef = TypedDict(
    "ConfigurationProfilesTypeDef",
    {"Items": List["ConfigurationProfileSummaryTypeDef"], "NextToken": str},
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {"Content": Union[bytes, IO[bytes]], "ConfigurationVersion": str, "ContentType": str},
    total=False,
)

DeploymentStrategiesTypeDef = TypedDict(
    "DeploymentStrategiesTypeDef",
    {"Items": List["DeploymentStrategyTypeDef"], "NextToken": str},
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": Literal["LINEAR", "EXPONENTIAL"],
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": Literal[
            "BAKING", "VALIDATING", "DEPLOYING", "COMPLETE", "ROLLING_BACK", "ROLLED_BACK"
        ],
        "EventLog": List["DeploymentEventTypeDef"],
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
    total=False,
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef", {"Items": List["DeploymentSummaryTypeDef"], "NextToken": str}, total=False
)

EnvironmentsTypeDef = TypedDict(
    "EnvironmentsTypeDef", {"Items": List["EnvironmentTypeDef"], "NextToken": str}, total=False
)

HostedConfigurationVersionTypeDef = TypedDict(
    "HostedConfigurationVersionTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "Content": Union[bytes, IO[bytes]],
        "ContentType": str,
    },
    total=False,
)

HostedConfigurationVersionsTypeDef = TypedDict(
    "HostedConfigurationVersionsTypeDef",
    {"Items": List["HostedConfigurationVersionSummaryTypeDef"], "NextToken": str},
    total=False,
)

ResourceTagsTypeDef = TypedDict("ResourceTagsTypeDef", {"Tags": Dict[str, str]}, total=False)
