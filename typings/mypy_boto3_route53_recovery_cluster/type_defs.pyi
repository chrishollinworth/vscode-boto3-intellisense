"""
Type annotations for route53-recovery-cluster service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_route53_recovery_cluster.type_defs import GetRoutingControlStateRequestTypeDef

    data: GetRoutingControlStateRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import RoutingControlStateType

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
    "GetRoutingControlStateRequestTypeDef",
    "GetRoutingControlStateResponseTypeDef",
    "ListRoutingControlsRequestPaginateTypeDef",
    "ListRoutingControlsRequestTypeDef",
    "ListRoutingControlsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingControlTypeDef",
    "UpdateRoutingControlStateEntryTypeDef",
    "UpdateRoutingControlStateRequestTypeDef",
    "UpdateRoutingControlStatesRequestTypeDef",
)

class GetRoutingControlStateRequestTypeDef(TypedDict):
    RoutingControlArn: str

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

class ListRoutingControlsRequestTypeDef(TypedDict):
    ControlPanelArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RoutingControlTypeDef(TypedDict):
    ControlPanelArn: NotRequired[str]
    ControlPanelName: NotRequired[str]
    RoutingControlArn: NotRequired[str]
    RoutingControlName: NotRequired[str]
    RoutingControlState: NotRequired[RoutingControlStateType]
    Owner: NotRequired[str]

class UpdateRoutingControlStateEntryTypeDef(TypedDict):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType

class UpdateRoutingControlStateRequestTypeDef(TypedDict):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    SafetyRulesToOverride: NotRequired[Sequence[str]]

class GetRoutingControlStateResponseTypeDef(TypedDict):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    RoutingControlName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoutingControlsRequestPaginateTypeDef(TypedDict):
    ControlPanelArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoutingControlsResponseTypeDef(TypedDict):
    RoutingControls: List[RoutingControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateRoutingControlStatesRequestTypeDef(TypedDict):
    UpdateRoutingControlStateEntries: Sequence[UpdateRoutingControlStateEntryTypeDef]
    SafetyRulesToOverride: NotRequired[Sequence[str]]
