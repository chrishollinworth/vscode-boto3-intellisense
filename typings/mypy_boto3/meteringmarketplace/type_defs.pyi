"""
Type annotations for meteringmarketplace service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_meteringmarketplace.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import UsageRecordResultStatusType

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
    "BatchMeterUsageRequestTypeDef",
    "BatchMeterUsageResultTypeDef",
    "MeterUsageRequestTypeDef",
    "MeterUsageResultTypeDef",
    "RegisterUsageRequestTypeDef",
    "RegisterUsageResultTypeDef",
    "ResolveCustomerRequestTypeDef",
    "ResolveCustomerResultTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UsageAllocationOutputTypeDef",
    "UsageAllocationTypeDef",
    "UsageAllocationUnionTypeDef",
    "UsageRecordOutputTypeDef",
    "UsageRecordResultTypeDef",
    "UsageRecordTypeDef",
    "UsageRecordUnionTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class RegisterUsageRequestTypeDef(TypedDict):
    ProductCode: str
    PublicKeyVersion: int
    Nonce: NotRequired[str]

class ResolveCustomerRequestTypeDef(TypedDict):
    RegistrationToken: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class MeterUsageResultTypeDef(TypedDict):
    MeteringRecordId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterUsageResultTypeDef(TypedDict):
    PublicKeyRotationTimestamp: datetime
    Signature: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveCustomerResultTypeDef(TypedDict):
    CustomerIdentifier: str
    ProductCode: str
    CustomerAWSAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageAllocationOutputTypeDef(TypedDict):
    AllocatedUsageQuantity: int
    Tags: NotRequired[List[TagTypeDef]]

class UsageAllocationTypeDef(TypedDict):
    AllocatedUsageQuantity: int
    Tags: NotRequired[Sequence[TagTypeDef]]

class UsageRecordOutputTypeDef(TypedDict):
    Timestamp: datetime
    Dimension: str
    CustomerIdentifier: NotRequired[str]
    Quantity: NotRequired[int]
    UsageAllocations: NotRequired[List[UsageAllocationOutputTypeDef]]
    CustomerAWSAccountId: NotRequired[str]

UsageAllocationUnionTypeDef = Union[UsageAllocationTypeDef, UsageAllocationOutputTypeDef]

class UsageRecordResultTypeDef(TypedDict):
    UsageRecord: NotRequired[UsageRecordOutputTypeDef]
    MeteringRecordId: NotRequired[str]
    Status: NotRequired[UsageRecordResultStatusType]

class MeterUsageRequestTypeDef(TypedDict):
    ProductCode: str
    Timestamp: TimestampTypeDef
    UsageDimension: str
    UsageQuantity: NotRequired[int]
    DryRun: NotRequired[bool]
    UsageAllocations: NotRequired[Sequence[UsageAllocationUnionTypeDef]]

class UsageRecordTypeDef(TypedDict):
    Timestamp: TimestampTypeDef
    Dimension: str
    CustomerIdentifier: NotRequired[str]
    Quantity: NotRequired[int]
    UsageAllocations: NotRequired[Sequence[UsageAllocationUnionTypeDef]]
    CustomerAWSAccountId: NotRequired[str]

class BatchMeterUsageResultTypeDef(TypedDict):
    Results: List[UsageRecordResultTypeDef]
    UnprocessedRecords: List[UsageRecordOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

UsageRecordUnionTypeDef = Union[UsageRecordTypeDef, UsageRecordOutputTypeDef]

class BatchMeterUsageRequestTypeDef(TypedDict):
    UsageRecords: Sequence[UsageRecordUnionTypeDef]
    ProductCode: str
