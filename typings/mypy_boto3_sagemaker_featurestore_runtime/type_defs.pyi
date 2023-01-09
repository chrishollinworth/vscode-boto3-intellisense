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

from .literals import TargetStoreType

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

BatchGetRecordRequestRequestTypeDef = TypedDict(
    "BatchGetRecordRequestRequestTypeDef",
    {
        "Identifiers": List["BatchGetRecordIdentifierTypeDef"],
    },
)

BatchGetRecordResponseTypeDef = TypedDict(
    "BatchGetRecordResponseTypeDef",
    {
        "Records": List["BatchGetRecordResultDetailTypeDef"],
        "Errors": List["BatchGetRecordErrorTypeDef"],
        "UnprocessedIdentifiers": List["BatchGetRecordIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRecordResultDetailTypeDef = TypedDict(
    "BatchGetRecordResultDetailTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "Record": List["FeatureValueTypeDef"],
    },
)

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
    },
    total=False,
)

class DeleteRecordRequestRequestTypeDef(
    _RequiredDeleteRecordRequestRequestTypeDef, _OptionalDeleteRecordRequestRequestTypeDef
):
    pass

FeatureValueTypeDef = TypedDict(
    "FeatureValueTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": str,
    },
)

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
