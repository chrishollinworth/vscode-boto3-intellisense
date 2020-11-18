"""
Main interface for migrationhub-config service type definitions.

Usage::

    ```python
    from mypy_boto3_migrationhub_config.type_defs import HomeRegionControlTypeDef

    data: HomeRegionControlTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "HomeRegionControlTypeDef",
    "TargetTypeDef",
    "CreateHomeRegionControlResultTypeDef",
    "DescribeHomeRegionControlsResultTypeDef",
    "GetHomeRegionResultTypeDef",
)

HomeRegionControlTypeDef = TypedDict(
    "HomeRegionControlTypeDef",
    {"ControlId": str, "HomeRegion": str, "Target": "TargetTypeDef", "RequestedTime": datetime},
    total=False,
)

_RequiredTargetTypeDef = TypedDict("_RequiredTargetTypeDef", {"Type": Literal["ACCOUNT"]})
_OptionalTargetTypeDef = TypedDict("_OptionalTargetTypeDef", {"Id": str}, total=False)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


CreateHomeRegionControlResultTypeDef = TypedDict(
    "CreateHomeRegionControlResultTypeDef",
    {"HomeRegionControl": "HomeRegionControlTypeDef"},
    total=False,
)

DescribeHomeRegionControlsResultTypeDef = TypedDict(
    "DescribeHomeRegionControlsResultTypeDef",
    {"HomeRegionControls": List["HomeRegionControlTypeDef"], "NextToken": str},
    total=False,
)

GetHomeRegionResultTypeDef = TypedDict(
    "GetHomeRegionResultTypeDef", {"HomeRegion": str}, total=False
)
