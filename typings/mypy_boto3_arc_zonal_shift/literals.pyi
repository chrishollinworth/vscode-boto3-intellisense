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
    "ListManagedResourcesPaginatorName",
    "ListZonalShiftsPaginatorName",
    "ZonalShiftStatusType",
)

AppliedStatusType = Literal["APPLIED", "NOT_APPLIED"]
ListManagedResourcesPaginatorName = Literal["list_managed_resources"]
ListZonalShiftsPaginatorName = Literal["list_zonal_shifts"]
ZonalShiftStatusType = Literal["ACTIVE", "CANCELED", "EXPIRED"]
