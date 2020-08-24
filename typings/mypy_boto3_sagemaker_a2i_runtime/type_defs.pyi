"""
Main interface for sagemaker-a2i-runtime service type definitions.

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopOutputTypeDef

    data: HumanLoopOutputTypeDef = {...}
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
    "HumanLoopOutputTypeDef",
    "HumanLoopSummaryTypeDef",
    "DescribeHumanLoopResponseTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartHumanLoopResponseTypeDef",
)

HumanLoopOutputTypeDef = TypedDict("HumanLoopOutputTypeDef", {"OutputS3Uri": str})

HumanLoopSummaryTypeDef = TypedDict(
    "HumanLoopSummaryTypeDef",
    {
        "HumanLoopName": str,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "CreationTime": datetime,
        "FailureReason": str,
        "FlowDefinitionArn": str,
    },
    total=False,
)

_RequiredDescribeHumanLoopResponseTypeDef = TypedDict(
    "_RequiredDescribeHumanLoopResponseTypeDef",
    {
        "CreationTime": datetime,
        "HumanLoopStatus": Literal["InProgress", "Failed", "Completed", "Stopped", "Stopping"],
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
    },
)
_OptionalDescribeHumanLoopResponseTypeDef = TypedDict(
    "_OptionalDescribeHumanLoopResponseTypeDef",
    {"FailureReason": str, "FailureCode": str, "HumanLoopOutput": "HumanLoopOutputTypeDef"},
    total=False,
)


class DescribeHumanLoopResponseTypeDef(
    _RequiredDescribeHumanLoopResponseTypeDef, _OptionalDescribeHumanLoopResponseTypeDef
):
    pass


HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
)

HumanLoopInputTypeDef = TypedDict("HumanLoopInputTypeDef", {"InputContent": str})

_RequiredListHumanLoopsResponseTypeDef = TypedDict(
    "_RequiredListHumanLoopsResponseTypeDef",
    {"HumanLoopSummaries": List["HumanLoopSummaryTypeDef"]},
)
_OptionalListHumanLoopsResponseTypeDef = TypedDict(
    "_OptionalListHumanLoopsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHumanLoopsResponseTypeDef(
    _RequiredListHumanLoopsResponseTypeDef, _OptionalListHumanLoopsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartHumanLoopResponseTypeDef = TypedDict(
    "StartHumanLoopResponseTypeDef", {"HumanLoopArn": str}, total=False
)
