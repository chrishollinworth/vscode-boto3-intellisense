"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    DeletionModeType,
    ExpirationTimeResponseType,
    TargetStoreType,
    TtlDurationUnitType,
)

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
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierOutputTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "BatchGetRecordIdentifierUnionTypeDef",
    "BatchGetRecordRequestTypeDef",
    "BatchGetRecordResponseTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "DeleteRecordRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FeatureValueOutputTypeDef",
    "FeatureValueTypeDef",
    "FeatureValueUnionTypeDef",
    "GetRecordRequestTypeDef",
    "GetRecordResponseTypeDef",
    "PutRecordRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TtlDurationTypeDef",
)

class BatchGetRecordErrorTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    ErrorCode: str
    ErrorMessage: str

class BatchGetRecordIdentifierOutputTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: List[str]
    FeatureNames: NotRequired[List[str]]

class BatchGetRecordIdentifierTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: Sequence[str]
    FeatureNames: NotRequired[Sequence[str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class FeatureValueOutputTypeDef(TypedDict):
    FeatureName: str
    ValueAsString: NotRequired[str]
    ValueAsStringList: NotRequired[List[str]]

class DeleteRecordRequestTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    EventTime: str
    TargetStores: NotRequired[Sequence[TargetStoreType]]
    DeletionMode: NotRequired[DeletionModeType]

class FeatureValueTypeDef(TypedDict):
    FeatureName: str
    ValueAsString: NotRequired[str]
    ValueAsStringList: NotRequired[Sequence[str]]

class GetRecordRequestTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: NotRequired[Sequence[str]]
    ExpirationTimeResponse: NotRequired[ExpirationTimeResponseType]

class TtlDurationTypeDef(TypedDict):
    Unit: TtlDurationUnitType
    Value: int

BatchGetRecordIdentifierUnionTypeDef = Union[
    BatchGetRecordIdentifierTypeDef, BatchGetRecordIdentifierOutputTypeDef
]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRecordResultDetailTypeDef(TypedDict):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: List[FeatureValueOutputTypeDef]
    ExpiresAt: NotRequired[str]

class GetRecordResponseTypeDef(TypedDict):
    Record: List[FeatureValueOutputTypeDef]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadataTypeDef

FeatureValueUnionTypeDef = Union[FeatureValueTypeDef, FeatureValueOutputTypeDef]

class BatchGetRecordRequestTypeDef(TypedDict):
    Identifiers: Sequence[BatchGetRecordIdentifierUnionTypeDef]
    ExpirationTimeResponse: NotRequired[ExpirationTimeResponseType]

class BatchGetRecordResponseTypeDef(TypedDict):
    Records: List[BatchGetRecordResultDetailTypeDef]
    Errors: List[BatchGetRecordErrorTypeDef]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordRequestTypeDef(TypedDict):
    FeatureGroupName: str
    Record: Sequence[FeatureValueUnionTypeDef]
    TargetStores: NotRequired[Sequence[TargetStoreType]]
    TtlDuration: NotRequired[TtlDurationTypeDef]
