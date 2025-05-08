"""
Type annotations for ssm-quicksetup service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ssm_quicksetup.type_defs import ConfigurationDefinitionInputTypeDef

    data: ConfigurationDefinitionInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import StatusType, StatusTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ConfigurationDefinitionInputTypeDef",
    "ConfigurationDefinitionSummaryTypeDef",
    "ConfigurationDefinitionTypeDef",
    "ConfigurationManagerSummaryTypeDef",
    "ConfigurationSummaryTypeDef",
    "CreateConfigurationManagerInputTypeDef",
    "CreateConfigurationManagerOutputTypeDef",
    "DeleteConfigurationManagerInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FilterTypeDef",
    "GetConfigurationInputTypeDef",
    "GetConfigurationManagerInputTypeDef",
    "GetConfigurationManagerOutputTypeDef",
    "GetConfigurationOutputTypeDef",
    "GetServiceSettingsOutputTypeDef",
    "ListConfigurationManagersInputPaginateTypeDef",
    "ListConfigurationManagersInputTypeDef",
    "ListConfigurationManagersOutputTypeDef",
    "ListConfigurationsInputPaginateTypeDef",
    "ListConfigurationsInputTypeDef",
    "ListConfigurationsOutputTypeDef",
    "ListQuickSetupTypesOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuickSetupTypeOutputTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceSettingsTypeDef",
    "StatusSummaryTypeDef",
    "TagEntryTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateConfigurationDefinitionInputTypeDef",
    "UpdateConfigurationManagerInputTypeDef",
    "UpdateServiceSettingsInputTypeDef",
)

ConfigurationDefinitionInputTypeDef = TypedDict(
    "ConfigurationDefinitionInputTypeDef",
    {
        "Parameters": Mapping[str, str],
        "Type": str,
        "LocalDeploymentAdministrationRoleArn": NotRequired[str],
        "LocalDeploymentExecutionRoleName": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)
ConfigurationDefinitionSummaryTypeDef = TypedDict(
    "ConfigurationDefinitionSummaryTypeDef",
    {
        "FirstClassParameters": NotRequired[Dict[str, str]],
        "Id": NotRequired[str],
        "Type": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)
ConfigurationDefinitionTypeDef = TypedDict(
    "ConfigurationDefinitionTypeDef",
    {
        "Parameters": Dict[str, str],
        "Type": str,
        "Id": NotRequired[str],
        "LocalDeploymentAdministrationRoleArn": NotRequired[str],
        "LocalDeploymentExecutionRoleName": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)
StatusSummaryTypeDef = TypedDict(
    "StatusSummaryTypeDef",
    {
        "LastUpdatedAt": datetime,
        "StatusType": StatusTypeType,
        "Status": NotRequired[StatusType],
        "StatusDetails": NotRequired[Dict[str, str]],
        "StatusMessage": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteConfigurationManagerInputTypeDef(TypedDict):
    ManagerArn: str

class FilterTypeDef(TypedDict):
    Key: str
    Values: Sequence[str]

class GetConfigurationInputTypeDef(TypedDict):
    ConfigurationId: str

class GetConfigurationManagerInputTypeDef(TypedDict):
    ManagerArn: str

class ServiceSettingsTypeDef(TypedDict):
    ExplorerEnablingRoleArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

QuickSetupTypeOutputTypeDef = TypedDict(
    "QuickSetupTypeOutputTypeDef",
    {
        "LatestVersion": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TagEntryTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConfigurationDefinitionInputTypeDef(TypedDict):
    Id: str
    ManagerArn: str
    LocalDeploymentAdministrationRoleArn: NotRequired[str]
    LocalDeploymentExecutionRoleName: NotRequired[str]
    Parameters: NotRequired[Mapping[str, str]]
    TypeVersion: NotRequired[str]

class UpdateConfigurationManagerInputTypeDef(TypedDict):
    ManagerArn: str
    Description: NotRequired[str]
    Name: NotRequired[str]

class UpdateServiceSettingsInputTypeDef(TypedDict):
    ExplorerEnablingRoleArn: NotRequired[str]

class CreateConfigurationManagerInputTypeDef(TypedDict):
    ConfigurationDefinitions: Sequence[ConfigurationDefinitionInputTypeDef]
    Description: NotRequired[str]
    Name: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ConfigurationManagerSummaryTypeDef(TypedDict):
    ManagerArn: str
    ConfigurationDefinitionSummaries: NotRequired[List[ConfigurationDefinitionSummaryTypeDef]]
    Description: NotRequired[str]
    Name: NotRequired[str]
    StatusSummaries: NotRequired[List[StatusSummaryTypeDef]]

ConfigurationSummaryTypeDef = TypedDict(
    "ConfigurationSummaryTypeDef",
    {
        "Account": NotRequired[str],
        "ConfigurationDefinitionId": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "FirstClassParameters": NotRequired[Dict[str, str]],
        "Id": NotRequired[str],
        "ManagerArn": NotRequired[str],
        "Region": NotRequired[str],
        "StatusSummaries": NotRequired[List[StatusSummaryTypeDef]],
        "Type": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)

class CreateConfigurationManagerOutputTypeDef(TypedDict):
    ManagerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationManagerOutputTypeDef(TypedDict):
    ConfigurationDefinitions: List[ConfigurationDefinitionTypeDef]
    CreatedAt: datetime
    Description: str
    LastModifiedAt: datetime
    ManagerArn: str
    Name: str
    StatusSummaries: List[StatusSummaryTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

GetConfigurationOutputTypeDef = TypedDict(
    "GetConfigurationOutputTypeDef",
    {
        "Account": str,
        "ConfigurationDefinitionId": str,
        "CreatedAt": datetime,
        "Id": str,
        "LastModifiedAt": datetime,
        "ManagerArn": str,
        "Parameters": Dict[str, str],
        "Region": str,
        "StatusSummaries": List[StatusSummaryTypeDef],
        "Type": str,
        "TypeVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListConfigurationManagersInputTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxItems: NotRequired[int]
    StartingToken: NotRequired[str]

class ListConfigurationsInputTypeDef(TypedDict):
    ConfigurationDefinitionId: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    ManagerArn: NotRequired[str]
    MaxItems: NotRequired[int]
    StartingToken: NotRequired[str]

class GetServiceSettingsOutputTypeDef(TypedDict):
    ServiceSettings: ServiceSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationManagersInputPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConfigurationsInputPaginateTypeDef(TypedDict):
    ConfigurationDefinitionId: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    ManagerArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQuickSetupTypesOutputTypeDef(TypedDict):
    QuickSetupTypeList: List[QuickSetupTypeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationManagersOutputTypeDef(TypedDict):
    ConfigurationManagersList: List[ConfigurationManagerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListConfigurationsOutputTypeDef(TypedDict):
    ConfigurationsList: List[ConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
