"""
Type annotations for meteringmarketplace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_meteringmarketplace.type_defs import BatchMeterUsageRequestRequestTypeDef

    data: BatchMeterUsageRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import UsageRecordResultStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchMeterUsageRequestRequestTypeDef",
    "BatchMeterUsageResultTypeDef",
    "MeterUsageRequestRequestTypeDef",
    "MeterUsageResultTypeDef",
    "RegisterUsageRequestRequestTypeDef",
    "RegisterUsageResultTypeDef",
    "ResolveCustomerRequestRequestTypeDef",
    "ResolveCustomerResultTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "UsageAllocationTypeDef",
    "UsageRecordResultTypeDef",
    "UsageRecordTypeDef",
)

BatchMeterUsageRequestRequestTypeDef = TypedDict(
    "BatchMeterUsageRequestRequestTypeDef",
    {
        "UsageRecords": List["UsageRecordTypeDef"],
        "ProductCode": str,
    },
)

BatchMeterUsageResultTypeDef = TypedDict(
    "BatchMeterUsageResultTypeDef",
    {
        "Results": List["UsageRecordResultTypeDef"],
        "UnprocessedRecords": List["UsageRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMeterUsageRequestRequestTypeDef = TypedDict(
    "_RequiredMeterUsageRequestRequestTypeDef",
    {
        "ProductCode": str,
        "Timestamp": Union[datetime, str],
        "UsageDimension": str,
    },
)
_OptionalMeterUsageRequestRequestTypeDef = TypedDict(
    "_OptionalMeterUsageRequestRequestTypeDef",
    {
        "UsageQuantity": int,
        "DryRun": bool,
        "UsageAllocations": List["UsageAllocationTypeDef"],
    },
    total=False,
)

class MeterUsageRequestRequestTypeDef(
    _RequiredMeterUsageRequestRequestTypeDef, _OptionalMeterUsageRequestRequestTypeDef
):
    pass

MeterUsageResultTypeDef = TypedDict(
    "MeterUsageResultTypeDef",
    {
        "MeteringRecordId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterUsageRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterUsageRequestRequestTypeDef",
    {
        "ProductCode": str,
        "PublicKeyVersion": int,
    },
)
_OptionalRegisterUsageRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterUsageRequestRequestTypeDef",
    {
        "Nonce": str,
    },
    total=False,
)

class RegisterUsageRequestRequestTypeDef(
    _RequiredRegisterUsageRequestRequestTypeDef, _OptionalRegisterUsageRequestRequestTypeDef
):
    pass

RegisterUsageResultTypeDef = TypedDict(
    "RegisterUsageResultTypeDef",
    {
        "PublicKeyRotationTimestamp": datetime,
        "Signature": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveCustomerRequestRequestTypeDef = TypedDict(
    "ResolveCustomerRequestRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)

ResolveCustomerResultTypeDef = TypedDict(
    "ResolveCustomerResultTypeDef",
    {
        "CustomerIdentifier": str,
        "ProductCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredUsageAllocationTypeDef = TypedDict(
    "_RequiredUsageAllocationTypeDef",
    {
        "AllocatedUsageQuantity": int,
    },
)
_OptionalUsageAllocationTypeDef = TypedDict(
    "_OptionalUsageAllocationTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UsageAllocationTypeDef(_RequiredUsageAllocationTypeDef, _OptionalUsageAllocationTypeDef):
    pass

UsageRecordResultTypeDef = TypedDict(
    "UsageRecordResultTypeDef",
    {
        "UsageRecord": "UsageRecordTypeDef",
        "MeteringRecordId": str,
        "Status": UsageRecordResultStatusType,
    },
    total=False,
)

_RequiredUsageRecordTypeDef = TypedDict(
    "_RequiredUsageRecordTypeDef",
    {
        "Timestamp": Union[datetime, str],
        "CustomerIdentifier": str,
        "Dimension": str,
    },
)
_OptionalUsageRecordTypeDef = TypedDict(
    "_OptionalUsageRecordTypeDef",
    {
        "Quantity": int,
        "UsageAllocations": List["UsageAllocationTypeDef"],
    },
    total=False,
)

class UsageRecordTypeDef(_RequiredUsageRecordTypeDef, _OptionalUsageRecordTypeDef):
    pass
