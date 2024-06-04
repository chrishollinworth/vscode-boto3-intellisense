"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import (
    DeletionModeType,
    ExpirationTimeResponseType,
    TargetStoreType,
    TtlDurationUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "BatchGetRecordRequestRequestTypeDef",
    "BatchGetRecordResponseTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "DeleteRecordRequestRequestTypeDef",
    "FeatureValueTypeDef",
    "GetRecordRequestRequestTypeDef",
    "GetRecordResponseTypeDef",
    "PutRecordRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TtlDurationTypeDef",
)

BatchGetRecordErrorTypeDef = TypedDict(
    "BatchGetRecordErrorTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

_RequiredBatchGetRecordIdentifierTypeDef = TypedDict(
    "_RequiredBatchGetRecordIdentifierTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifiersValueAsString": List[str],
    },
)
_OptionalBatchGetRecordIdentifierTypeDef = TypedDict(
    "_OptionalBatchGetRecordIdentifierTypeDef",
    {
        "FeatureNames": List[str],
    },
    total=False,
)

class BatchGetRecordIdentifierTypeDef(
    _RequiredBatchGetRecordIdentifierTypeDef, _OptionalBatchGetRecordIdentifierTypeDef
):
    pass

_RequiredBatchGetRecordRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetRecordRequestRequestTypeDef",
    {
        "Identifiers": List["BatchGetRecordIdentifierTypeDef"],
    },
)
_OptionalBatchGetRecordRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetRecordRequestRequestTypeDef",
    {
        "ExpirationTimeResponse": ExpirationTimeResponseType,
    },
    total=False,
)

class BatchGetRecordRequestRequestTypeDef(
    _RequiredBatchGetRecordRequestRequestTypeDef, _OptionalBatchGetRecordRequestRequestTypeDef
):
    pass

BatchGetRecordResponseTypeDef = TypedDict(
    "BatchGetRecordResponseTypeDef",
    {
        "Records": List["BatchGetRecordResultDetailTypeDef"],
        "Errors": List["BatchGetRecordErrorTypeDef"],
        "UnprocessedIdentifiers": List["BatchGetRecordIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetRecordResultDetailTypeDef = TypedDict(
    "_RequiredBatchGetRecordResultDetailTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "Record": List["FeatureValueTypeDef"],
    },
)
_OptionalBatchGetRecordResultDetailTypeDef = TypedDict(
    "_OptionalBatchGetRecordResultDetailTypeDef",
    {
        "ExpiresAt": str,
    },
    total=False,
)

class BatchGetRecordResultDetailTypeDef(
    _RequiredBatchGetRecordResultDetailTypeDef, _OptionalBatchGetRecordResultDetailTypeDef
):
    pass

_RequiredDeleteRecordRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "EventTime": str,
    },
)
_OptionalDeleteRecordRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRecordRequestRequestTypeDef",
    {
        "TargetStores": List[TargetStoreType],
        "DeletionMode": DeletionModeType,
    },
    total=False,
)

class DeleteRecordRequestRequestTypeDef(
    _RequiredDeleteRecordRequestRequestTypeDef, _OptionalDeleteRecordRequestRequestTypeDef
):
    pass

_RequiredFeatureValueTypeDef = TypedDict(
    "_RequiredFeatureValueTypeDef",
    {
        "FeatureName": str,
    },
)
_OptionalFeatureValueTypeDef = TypedDict(
    "_OptionalFeatureValueTypeDef",
    {
        "ValueAsString": str,
        "ValueAsStringList": List[str],
    },
    total=False,
)

class FeatureValueTypeDef(_RequiredFeatureValueTypeDef, _OptionalFeatureValueTypeDef):
    pass

_RequiredGetRecordRequestRequestTypeDef = TypedDict(
    "_RequiredGetRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
    },
)
_OptionalGetRecordRequestRequestTypeDef = TypedDict(
    "_OptionalGetRecordRequestRequestTypeDef",
    {
        "FeatureNames": List[str],
        "ExpirationTimeResponse": ExpirationTimeResponseType,
    },
    total=False,
)

class GetRecordRequestRequestTypeDef(
    _RequiredGetRecordRequestRequestTypeDef, _OptionalGetRecordRequestRequestTypeDef
):
    pass

GetRecordResponseTypeDef = TypedDict(
    "GetRecordResponseTypeDef",
    {
        "Record": List["FeatureValueTypeDef"],
        "ExpiresAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRecordRequestRequestTypeDef = TypedDict(
    "_RequiredPutRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "Record": List["FeatureValueTypeDef"],
    },
)
_OptionalPutRecordRequestRequestTypeDef = TypedDict(
    "_OptionalPutRecordRequestRequestTypeDef",
    {
        "TargetStores": List[TargetStoreType],
        "TtlDuration": "TtlDurationTypeDef",
    },
    total=False,
)

class PutRecordRequestRequestTypeDef(
    _RequiredPutRecordRequestRequestTypeDef, _OptionalPutRecordRequestRequestTypeDef
):
    pass

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

TtlDurationTypeDef = TypedDict(
    "TtlDurationTypeDef",
    {
        "Unit": TtlDurationUnitType,
        "Value": int,
    },
)
