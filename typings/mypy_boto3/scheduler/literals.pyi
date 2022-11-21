"""
Type annotations for scheduler service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/literals.html)

Usage::

    ```python
    from mypy_boto3_scheduler.literals import AssignPublicIpType

    data: AssignPublicIpType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssignPublicIpType",
    "FlexibleTimeWindowModeType",
    "LaunchTypeType",
    "ListScheduleGroupsPaginatorName",
    "ListSchedulesPaginatorName",
    "PlacementConstraintTypeType",
    "PlacementStrategyTypeType",
    "PropagateTagsType",
    "ScheduleGroupStateType",
    "ScheduleStateType",
)

AssignPublicIpType = Literal["DISABLED", "ENABLED"]
FlexibleTimeWindowModeType = Literal["FLEXIBLE", "OFF"]
LaunchTypeType = Literal["EC2", "EXTERNAL", "FARGATE"]
ListScheduleGroupsPaginatorName = Literal["list_schedule_groups"]
ListSchedulesPaginatorName = Literal["list_schedules"]
PlacementConstraintTypeType = Literal["distinctInstance", "memberOf"]
PlacementStrategyTypeType = Literal["binpack", "random", "spread"]
PropagateTagsType = Literal["TASK_DEFINITION"]
ScheduleGroupStateType = Literal["ACTIVE", "DELETING"]
ScheduleStateType = Literal["DISABLED", "ENABLED"]
