"""
Type annotations for arc-zonal-shift service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/literals.html)

Usage::

    ```python
    from mypy_boto3_arc_zonal_shift.literals import AppliedStatusType

    data: AppliedStatusType = "APPLIED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AppliedStatusType",
    "AutoshiftAppliedStatusType",
    "AutoshiftExecutionStatusType",
    "ControlConditionTypeType",
    "ListAutoshiftsPaginatorName",
    "ListManagedResourcesPaginatorName",
    "ListZonalShiftsPaginatorName",
    "PracticeRunOutcomeType",
    "ZonalAutoshiftStatusType",
    "ZonalShiftStatusType",
)

AppliedStatusType = Literal["APPLIED", "NOT_APPLIED"]
AutoshiftAppliedStatusType = Literal["APPLIED", "NOT_APPLIED"]
AutoshiftExecutionStatusType = Literal["ACTIVE", "COMPLETED"]
ControlConditionTypeType = Literal["CLOUDWATCH"]
ListAutoshiftsPaginatorName = Literal["list_autoshifts"]
ListManagedResourcesPaginatorName = Literal["list_managed_resources"]
ListZonalShiftsPaginatorName = Literal["list_zonal_shifts"]
PracticeRunOutcomeType = Literal["FAILED", "INTERRUPTED", "PENDING", "SUCCEEDED"]
ZonalAutoshiftStatusType = Literal["DISABLED", "ENABLED"]
ZonalShiftStatusType = Literal["ACTIVE", "CANCELED", "EXPIRED"]
