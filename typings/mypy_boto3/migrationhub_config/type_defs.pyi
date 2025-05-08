"""
Type annotations for migrationhub-config service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_migrationhub_config.type_defs import TargetTypeDef

    data: TargetTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CreateHomeRegionControlRequestTypeDef",
    "CreateHomeRegionControlResultTypeDef",
    "DeleteHomeRegionControlRequestTypeDef",
    "DescribeHomeRegionControlsRequestTypeDef",
    "DescribeHomeRegionControlsResultTypeDef",
    "GetHomeRegionResultTypeDef",
    "HomeRegionControlTypeDef",
    "ResponseMetadataTypeDef",
    "TargetTypeDef",
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Type": Literal["ACCOUNT"],
        "Id": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteHomeRegionControlRequestTypeDef(TypedDict):
    ControlId: str

class CreateHomeRegionControlRequestTypeDef(TypedDict):
    HomeRegion: str
    Target: TargetTypeDef
    DryRun: NotRequired[bool]

class DescribeHomeRegionControlsRequestTypeDef(TypedDict):
    ControlId: NotRequired[str]
    HomeRegion: NotRequired[str]
    Target: NotRequired[TargetTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class HomeRegionControlTypeDef(TypedDict):
    ControlId: NotRequired[str]
    HomeRegion: NotRequired[str]
    Target: NotRequired[TargetTypeDef]
    RequestedTime: NotRequired[datetime]

class GetHomeRegionResultTypeDef(TypedDict):
    HomeRegion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHomeRegionControlResultTypeDef(TypedDict):
    HomeRegionControl: HomeRegionControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHomeRegionControlsResultTypeDef(TypedDict):
    HomeRegionControls: List[HomeRegionControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
