"""
Main interface for meteringmarketplace service type definitions.

Usage::

    ```python
    from mypy_boto3_meteringmarketplace.type_defs import TagTypeDef

    data: TagTypeDef = {...}
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
    "TagTypeDef",
    "UsageAllocationTypeDef",
    "UsageRecordResultTypeDef",
    "UsageRecordTypeDef",
    "BatchMeterUsageResultTypeDef",
    "MeterUsageResultTypeDef",
    "RegisterUsageResultTypeDef",
    "ResolveCustomerResultTypeDef",
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredUsageAllocationTypeDef = TypedDict(
    "_RequiredUsageAllocationTypeDef", {"AllocatedUsageQuantity": int}
)
_OptionalUsageAllocationTypeDef = TypedDict(
    "_OptionalUsageAllocationTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)


class UsageAllocationTypeDef(_RequiredUsageAllocationTypeDef, _OptionalUsageAllocationTypeDef):
    pass


UsageRecordResultTypeDef = TypedDict(
    "UsageRecordResultTypeDef",
    {
        "UsageRecord": "UsageRecordTypeDef",
        "MeteringRecordId": str,
        "Status": Literal["Success", "CustomerNotSubscribed", "DuplicateRecord"],
    },
    total=False,
)

_RequiredUsageRecordTypeDef = TypedDict(
    "_RequiredUsageRecordTypeDef",
    {"Timestamp": datetime, "CustomerIdentifier": str, "Dimension": str},
)
_OptionalUsageRecordTypeDef = TypedDict(
    "_OptionalUsageRecordTypeDef",
    {"Quantity": int, "UsageAllocations": List["UsageAllocationTypeDef"]},
    total=False,
)


class UsageRecordTypeDef(_RequiredUsageRecordTypeDef, _OptionalUsageRecordTypeDef):
    pass


BatchMeterUsageResultTypeDef = TypedDict(
    "BatchMeterUsageResultTypeDef",
    {"Results": List["UsageRecordResultTypeDef"], "UnprocessedRecords": List["UsageRecordTypeDef"]},
    total=False,
)

MeterUsageResultTypeDef = TypedDict(
    "MeterUsageResultTypeDef", {"MeteringRecordId": str}, total=False
)

RegisterUsageResultTypeDef = TypedDict(
    "RegisterUsageResultTypeDef",
    {"PublicKeyRotationTimestamp": datetime, "Signature": str},
    total=False,
)

ResolveCustomerResultTypeDef = TypedDict(
    "ResolveCustomerResultTypeDef", {"CustomerIdentifier": str, "ProductCode": str}, total=False
)
