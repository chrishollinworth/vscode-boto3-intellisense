"""
Type annotations for migrationhub-config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhub_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_migrationhub_config.type_defs import CreateHomeRegionControlRequestRequestTypeDef

    data: CreateHomeRegionControlRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateHomeRegionControlRequestRequestTypeDef",
    "CreateHomeRegionControlResultTypeDef",
    "DescribeHomeRegionControlsRequestRequestTypeDef",
    "DescribeHomeRegionControlsResultTypeDef",
    "GetHomeRegionResultTypeDef",
    "HomeRegionControlTypeDef",
    "ResponseMetadataTypeDef",
    "TargetTypeDef",
)

_RequiredCreateHomeRegionControlRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHomeRegionControlRequestRequestTypeDef",
    {
        "HomeRegion": str,
        "Target": "TargetTypeDef",
    },
)
_OptionalCreateHomeRegionControlRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHomeRegionControlRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateHomeRegionControlRequestRequestTypeDef(
    _RequiredCreateHomeRegionControlRequestRequestTypeDef,
    _OptionalCreateHomeRegionControlRequestRequestTypeDef,
):
    pass

CreateHomeRegionControlResultTypeDef = TypedDict(
    "CreateHomeRegionControlResultTypeDef",
    {
        "HomeRegionControl": "HomeRegionControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHomeRegionControlsRequestRequestTypeDef = TypedDict(
    "DescribeHomeRegionControlsRequestRequestTypeDef",
    {
        "ControlId": str,
        "HomeRegion": str,
        "Target": "TargetTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeHomeRegionControlsResultTypeDef = TypedDict(
    "DescribeHomeRegionControlsResultTypeDef",
    {
        "HomeRegionControls": List["HomeRegionControlTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHomeRegionResultTypeDef = TypedDict(
    "GetHomeRegionResultTypeDef",
    {
        "HomeRegion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HomeRegionControlTypeDef = TypedDict(
    "HomeRegionControlTypeDef",
    {
        "ControlId": str,
        "HomeRegion": str,
        "Target": "TargetTypeDef",
        "RequestedTime": datetime,
    },
    total=False,
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

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Type": Literal["ACCOUNT"],
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "Id": str,
    },
    total=False,
)

class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass
