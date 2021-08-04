"""
Type annotations for appconfig service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import ApplicationResponseMetadataTypeDef

    data: ApplicationResponseMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    DeploymentEventTypeType,
    DeploymentStateType,
    EnvironmentStateType,
    GrowthTypeType,
    ReplicateToType,
    TriggeredByType,
    ValidatorTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationResponseMetadataTypeDef",
    "ApplicationTypeDef",
    "ApplicationsTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ConfigurationProfileTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateConfigurationProfileRequestRequestTypeDef",
    "CreateDeploymentStrategyRequestRequestTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateHostedConfigurationVersionRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteConfigurationProfileRequestRequestTypeDef",
    "DeleteDeploymentStrategyRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteHostedConfigurationVersionRequestRequestTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentStrategyResponseMetadataTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "EnvironmentResponseMetadataTypeDef",
    "EnvironmentTypeDef",
    "EnvironmentsTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetConfigurationProfileRequestRequestTypeDef",
    "GetConfigurationRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentStrategyRequestRequestTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetHostedConfigurationVersionRequestRequestTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "HostedConfigurationVersionTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListConfigurationProfilesRequestRequestTypeDef",
    "ListDeploymentStrategiesRequestRequestTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListHostedConfigurationVersionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MonitorTypeDef",
    "ResourceTagsTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StopDeploymentRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateConfigurationProfileRequestRequestTypeDef",
    "UpdateDeploymentStrategyRequestRequestTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "ValidateConfigurationRequestRequestTypeDef",
    "ValidatorTypeDef",
)

ApplicationResponseMetadataTypeDef = TypedDict(
    "ApplicationResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

ApplicationsTypeDef = TypedDict(
    "ApplicationsTypeDef",
    {
        "Items": List["ApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationProfileSummaryTypeDef = TypedDict(
    "ConfigurationProfileSummaryTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "LocationUri": str,
        "ValidatorTypes": List[ValidatorTypeType],
    },
    total=False,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationProfilesTypeDef = TypedDict(
    "ConfigurationProfilesTypeDef",
    {
        "Items": List["ConfigurationProfileSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Content": bytes,
        "ConfigurationVersion": str,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

_RequiredCreateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "LocationUri": str,
    },
)
_OptionalCreateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationProfileRequestRequestTypeDef",
    {
        "Description": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateConfigurationProfileRequestRequestTypeDef(
    _RequiredCreateConfigurationProfileRequestRequestTypeDef,
    _OptionalCreateConfigurationProfileRequestRequestTypeDef,
):
    pass

_RequiredCreateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentStrategyRequestRequestTypeDef",
    {
        "Name": str,
        "DeploymentDurationInMinutes": int,
        "GrowthFactor": float,
        "ReplicateTo": ReplicateToType,
    },
)
_OptionalCreateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentStrategyRequestRequestTypeDef",
    {
        "Description": str,
        "FinalBakeTimeInMinutes": int,
        "GrowthType": GrowthTypeType,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDeploymentStrategyRequestRequestTypeDef(
    _RequiredCreateDeploymentStrategyRequestRequestTypeDef,
    _OptionalCreateDeploymentStrategyRequestRequestTypeDef,
):
    pass

_RequiredCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
    },
)
_OptionalCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestRequestTypeDef",
    {
        "Description": str,
        "Monitors": List["MonitorTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEnvironmentRequestRequestTypeDef(
    _RequiredCreateEnvironmentRequestRequestTypeDef, _OptionalCreateEnvironmentRequestRequestTypeDef
):
    pass

_RequiredCreateHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "Content": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": str,
    },
)
_OptionalCreateHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHostedConfigurationVersionRequestRequestTypeDef",
    {
        "Description": str,
        "LatestVersionNumber": int,
    },
    total=False,
)

class CreateHostedConfigurationVersionRequestRequestTypeDef(
    _RequiredCreateHostedConfigurationVersionRequestRequestTypeDef,
    _OptionalCreateHostedConfigurationVersionRequestRequestTypeDef,
):
    pass

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DeleteConfigurationProfileRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)

DeleteDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)

DeleteHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "DeleteHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
)

DeploymentEventTypeDef = TypedDict(
    "DeploymentEventTypeDef",
    {
        "EventType": DeploymentEventTypeType,
        "TriggeredBy": TriggeredByType,
        "Description": str,
        "OccurredAt": datetime,
    },
    total=False,
)

DeploymentStrategiesTypeDef = TypedDict(
    "DeploymentStrategiesTypeDef",
    {
        "Items": List["DeploymentStrategyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentStrategyResponseMetadataTypeDef = TypedDict(
    "DeploymentStrategyResponseMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": ReplicateToType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentStrategyTypeDef = TypedDict(
    "DeploymentStrategyTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": ReplicateToType,
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
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": DeploymentStateType,
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
    },
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
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": DeploymentStateType,
        "EventLog": List["DeploymentEventTypeDef"],
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef",
    {
        "Items": List["DeploymentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentResponseMetadataTypeDef = TypedDict(
    "EnvironmentResponseMetadataTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": EnvironmentStateType,
        "Monitors": List["MonitorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": EnvironmentStateType,
        "Monitors": List["MonitorTypeDef"],
    },
    total=False,
)

EnvironmentsTypeDef = TypedDict(
    "EnvironmentsTypeDef",
    {
        "Items": List["EnvironmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetConfigurationProfileRequestRequestTypeDef = TypedDict(
    "GetConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)

_RequiredGetConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetConfigurationRequestRequestTypeDef",
    {
        "Application": str,
        "Environment": str,
        "Configuration": str,
        "ClientId": str,
    },
)
_OptionalGetConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetConfigurationRequestRequestTypeDef",
    {
        "ClientConfigurationVersion": str,
    },
    total=False,
)

class GetConfigurationRequestRequestTypeDef(
    _RequiredGetConfigurationRequestRequestTypeDef, _OptionalGetConfigurationRequestRequestTypeDef
):
    pass

GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)

GetDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "GetDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)

GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)

GetHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "GetHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
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

HostedConfigurationVersionTypeDef = TypedDict(
    "HostedConfigurationVersionTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "Content": bytes,
        "ContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostedConfigurationVersionsTypeDef = TypedDict(
    "HostedConfigurationVersionsTypeDef",
    {
        "Items": List["HostedConfigurationVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListConfigurationProfilesRequestRequestTypeDef = TypedDict(
    "_RequiredListConfigurationProfilesRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListConfigurationProfilesRequestRequestTypeDef = TypedDict(
    "_OptionalListConfigurationProfilesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListConfigurationProfilesRequestRequestTypeDef(
    _RequiredListConfigurationProfilesRequestRequestTypeDef,
    _OptionalListConfigurationProfilesRequestRequestTypeDef,
):
    pass

ListDeploymentStrategiesRequestRequestTypeDef = TypedDict(
    "ListDeploymentStrategiesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

_RequiredListDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDeploymentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)
_OptionalListDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDeploymentsRequestRequestTypeDef(
    _RequiredListDeploymentsRequestRequestTypeDef, _OptionalListDeploymentsRequestRequestTypeDef
):
    pass

_RequiredListEnvironmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListEnvironmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEnvironmentsRequestRequestTypeDef(
    _RequiredListEnvironmentsRequestRequestTypeDef, _OptionalListEnvironmentsRequestRequestTypeDef
):
    pass

_RequiredListHostedConfigurationVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListHostedConfigurationVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)
_OptionalListHostedConfigurationVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListHostedConfigurationVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListHostedConfigurationVersionsRequestRequestTypeDef(
    _RequiredListHostedConfigurationVersionsRequestRequestTypeDef,
    _OptionalListHostedConfigurationVersionsRequestRequestTypeDef,
):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "AlarmArn": str,
        "AlarmRoleArn": str,
    },
    total=False,
)

ResourceTagsTypeDef = TypedDict(
    "ResourceTagsTypeDef",
    {
        "Tags": Dict[str, str],
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

_RequiredStartDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredStartDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
    },
)
_OptionalStartDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalStartDeploymentRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class StartDeploymentRequestRequestTypeDef(
    _RequiredStartDeploymentRequestRequestTypeDef, _OptionalStartDeploymentRequestRequestTypeDef
):
    pass

StopDeploymentRequestRequestTypeDef = TypedDict(
    "StopDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

_RequiredUpdateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)
_OptionalUpdateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationProfileRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "RetrievalRoleArn": str,
        "Validators": List["ValidatorTypeDef"],
    },
    total=False,
)

class UpdateConfigurationProfileRequestRequestTypeDef(
    _RequiredUpdateConfigurationProfileRequestRequestTypeDef,
    _OptionalUpdateConfigurationProfileRequestRequestTypeDef,
):
    pass

_RequiredUpdateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)
_OptionalUpdateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeploymentStrategyRequestRequestTypeDef",
    {
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "FinalBakeTimeInMinutes": int,
        "GrowthFactor": float,
        "GrowthType": GrowthTypeType,
    },
    total=False,
)

class UpdateDeploymentStrategyRequestRequestTypeDef(
    _RequiredUpdateDeploymentStrategyRequestRequestTypeDef,
    _OptionalUpdateDeploymentStrategyRequestRequestTypeDef,
):
    pass

_RequiredUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Monitors": List["MonitorTypeDef"],
    },
    total=False,
)

class UpdateEnvironmentRequestRequestTypeDef(
    _RequiredUpdateEnvironmentRequestRequestTypeDef, _OptionalUpdateEnvironmentRequestRequestTypeDef
):
    pass

ValidateConfigurationRequestRequestTypeDef = TypedDict(
    "ValidateConfigurationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
    },
)

ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "Type": ValidatorTypeType,
        "Content": str,
    },
)
