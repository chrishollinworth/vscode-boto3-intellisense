"""
Type annotations for controlcatalog service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_controlcatalog.type_defs import AssociatedDomainSummaryTypeDef

    data: AssociatedDomainSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    ControlBehaviorType,
    ControlRelationTypeType,
    ControlScopeType,
    ControlSeverityType,
    MappingTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociatedDomainSummaryTypeDef",
    "AssociatedObjectiveSummaryTypeDef",
    "CommonControlFilterTypeDef",
    "CommonControlMappingDetailsTypeDef",
    "CommonControlSummaryTypeDef",
    "ControlFilterTypeDef",
    "ControlMappingFilterTypeDef",
    "ControlMappingTypeDef",
    "ControlParameterTypeDef",
    "ControlSummaryTypeDef",
    "DomainResourceFilterTypeDef",
    "DomainSummaryTypeDef",
    "FrameworkMappingDetailsTypeDef",
    "GetControlRequestTypeDef",
    "GetControlResponseTypeDef",
    "ImplementationDetailsTypeDef",
    "ImplementationFilterTypeDef",
    "ImplementationSummaryTypeDef",
    "ListCommonControlsRequestPaginateTypeDef",
    "ListCommonControlsRequestTypeDef",
    "ListCommonControlsResponseTypeDef",
    "ListControlMappingsRequestPaginateTypeDef",
    "ListControlMappingsRequestTypeDef",
    "ListControlMappingsResponseTypeDef",
    "ListControlsRequestPaginateTypeDef",
    "ListControlsRequestTypeDef",
    "ListControlsResponseTypeDef",
    "ListDomainsRequestPaginateTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListObjectivesRequestPaginateTypeDef",
    "ListObjectivesRequestTypeDef",
    "ListObjectivesResponseTypeDef",
    "MappingTypeDef",
    "ObjectiveFilterTypeDef",
    "ObjectiveResourceFilterTypeDef",
    "ObjectiveSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "RegionConfigurationTypeDef",
    "RelatedControlMappingDetailsTypeDef",
    "ResponseMetadataTypeDef",
)

class AssociatedDomainSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class AssociatedObjectiveSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class ObjectiveResourceFilterTypeDef(TypedDict):
    Arn: NotRequired[str]

class CommonControlMappingDetailsTypeDef(TypedDict):
    CommonControlArn: str

class ImplementationFilterTypeDef(TypedDict):
    Types: NotRequired[Sequence[str]]
    Identifiers: NotRequired[Sequence[str]]

class ControlMappingFilterTypeDef(TypedDict):
    ControlArns: NotRequired[Sequence[str]]
    CommonControlArns: NotRequired[Sequence[str]]
    MappingTypes: NotRequired[Sequence[MappingTypeType]]

class ControlParameterTypeDef(TypedDict):
    Name: str

ImplementationSummaryTypeDef = TypedDict(
    "ImplementationSummaryTypeDef",
    {
        "Type": str,
        "Identifier": NotRequired[str],
    },
)

class DomainResourceFilterTypeDef(TypedDict):
    Arn: NotRequired[str]

class DomainSummaryTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    CreateTime: datetime
    LastUpdateTime: datetime

class FrameworkMappingDetailsTypeDef(TypedDict):
    Name: str
    Item: str

class GetControlRequestTypeDef(TypedDict):
    ControlArn: str

ImplementationDetailsTypeDef = TypedDict(
    "ImplementationDetailsTypeDef",
    {
        "Type": str,
        "Identifier": NotRequired[str],
    },
)

class RegionConfigurationTypeDef(TypedDict):
    Scope: ControlScopeType
    DeployableRegions: NotRequired[List[str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDomainsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RelatedControlMappingDetailsTypeDef(TypedDict):
    RelationType: ControlRelationTypeType
    ControlArn: NotRequired[str]

class ObjectiveSummaryTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    CreateTime: datetime
    LastUpdateTime: datetime

class CommonControlSummaryTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    Objective: AssociatedObjectiveSummaryTypeDef
    CreateTime: datetime
    LastUpdateTime: datetime

class CommonControlFilterTypeDef(TypedDict):
    Objectives: NotRequired[Sequence[ObjectiveResourceFilterTypeDef]]

class ControlFilterTypeDef(TypedDict):
    Implementations: NotRequired[ImplementationFilterTypeDef]

class ListControlMappingsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filter: NotRequired[ControlMappingFilterTypeDef]

class ControlSummaryTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    Aliases: NotRequired[List[str]]
    Behavior: NotRequired[ControlBehaviorType]
    Severity: NotRequired[ControlSeverityType]
    Implementation: NotRequired[ImplementationSummaryTypeDef]
    CreateTime: NotRequired[datetime]
    GovernedResources: NotRequired[List[str]]

class ObjectiveFilterTypeDef(TypedDict):
    Domains: NotRequired[Sequence[DomainResourceFilterTypeDef]]

class GetControlResponseTypeDef(TypedDict):
    Arn: str
    Aliases: List[str]
    Name: str
    Description: str
    Behavior: ControlBehaviorType
    Severity: ControlSeverityType
    RegionConfiguration: RegionConfigurationTypeDef
    Implementation: ImplementationDetailsTypeDef
    Parameters: List[ControlParameterTypeDef]
    CreateTime: datetime
    GovernedResources: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(TypedDict):
    Domains: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListControlMappingsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[ControlMappingFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class MappingTypeDef(TypedDict):
    Framework: NotRequired[FrameworkMappingDetailsTypeDef]
    CommonControl: NotRequired[CommonControlMappingDetailsTypeDef]
    RelatedControl: NotRequired[RelatedControlMappingDetailsTypeDef]

class ListObjectivesResponseTypeDef(TypedDict):
    Objectives: List[ObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCommonControlsResponseTypeDef(TypedDict):
    CommonControls: List[CommonControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCommonControlsRequestPaginateTypeDef(TypedDict):
    CommonControlFilter: NotRequired[CommonControlFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCommonControlsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    CommonControlFilter: NotRequired[CommonControlFilterTypeDef]

class ListControlsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[ControlFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListControlsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filter: NotRequired[ControlFilterTypeDef]

class ListControlsResponseTypeDef(TypedDict):
    Controls: List[ControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListObjectivesRequestPaginateTypeDef(TypedDict):
    ObjectiveFilter: NotRequired[ObjectiveFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListObjectivesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ObjectiveFilter: NotRequired[ObjectiveFilterTypeDef]

ControlMappingTypeDef = TypedDict(
    "ControlMappingTypeDef",
    {
        "ControlArn": str,
        "MappingType": MappingTypeType,
        "Mapping": MappingTypeDef,
    },
)

class ListControlMappingsResponseTypeDef(TypedDict):
    ControlMappings: List[ControlMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
