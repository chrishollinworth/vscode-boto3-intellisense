"""
Type annotations for s3vectors service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3vectors/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_s3vectors.type_defs import EncryptionConfigurationTypeDef

    data: EncryptionConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import DistanceMetricType, SseTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CreateIndexInputTypeDef",
    "CreateIndexOutputTypeDef",
    "CreateVectorBucketInputTypeDef",
    "CreateVectorBucketOutputTypeDef",
    "DeleteIndexInputTypeDef",
    "DeleteVectorBucketInputTypeDef",
    "DeleteVectorBucketPolicyInputTypeDef",
    "DeleteVectorsInputTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetIndexInputTypeDef",
    "GetIndexOutputTypeDef",
    "GetOutputVectorTypeDef",
    "GetVectorBucketInputTypeDef",
    "GetVectorBucketOutputTypeDef",
    "GetVectorBucketPolicyInputTypeDef",
    "GetVectorBucketPolicyOutputTypeDef",
    "GetVectorsInputTypeDef",
    "GetVectorsOutputTypeDef",
    "IndexSummaryTypeDef",
    "IndexTypeDef",
    "ListIndexesInputPaginateTypeDef",
    "ListIndexesInputTypeDef",
    "ListIndexesOutputTypeDef",
    "ListOutputVectorTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVectorBucketsInputPaginateTypeDef",
    "ListVectorBucketsInputTypeDef",
    "ListVectorBucketsOutputTypeDef",
    "ListVectorsInputPaginateTypeDef",
    "ListVectorsInputTypeDef",
    "ListVectorsOutputTypeDef",
    "MetadataConfigurationOutputTypeDef",
    "MetadataConfigurationTypeDef",
    "MetadataConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PutInputVectorTypeDef",
    "PutVectorBucketPolicyInputTypeDef",
    "PutVectorsInputTypeDef",
    "QueryOutputVectorTypeDef",
    "QueryVectorsInputTypeDef",
    "QueryVectorsOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "VectorBucketSummaryTypeDef",
    "VectorBucketTypeDef",
    "VectorDataOutputTypeDef",
    "VectorDataTypeDef",
    "VectorDataUnionTypeDef",
)

class EncryptionConfigurationTypeDef(TypedDict):
    sseType: NotRequired[SseTypeType]
    kmsKeyArn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteIndexInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]

class DeleteVectorBucketInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]

class DeleteVectorBucketPolicyInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]

class DeleteVectorsInputTypeDef(TypedDict):
    keys: Sequence[str]
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]

class GetIndexInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]

class VectorDataOutputTypeDef(TypedDict):
    float32: NotRequired[List[float]]

class GetVectorBucketInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]

class GetVectorBucketPolicyInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]

class GetVectorsInputTypeDef(TypedDict):
    keys: Sequence[str]
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]
    returnData: NotRequired[bool]
    returnMetadata: NotRequired[bool]

class IndexSummaryTypeDef(TypedDict):
    vectorBucketName: str
    indexName: str
    indexArn: str
    creationTime: datetime

class MetadataConfigurationOutputTypeDef(TypedDict):
    nonFilterableMetadataKeys: List[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListIndexesInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    prefix: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class ListVectorBucketsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    prefix: NotRequired[str]

class VectorBucketSummaryTypeDef(TypedDict):
    vectorBucketName: str
    vectorBucketArn: str
    creationTime: datetime

class ListVectorsInputTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    segmentCount: NotRequired[int]
    segmentIndex: NotRequired[int]
    returnData: NotRequired[bool]
    returnMetadata: NotRequired[bool]

class MetadataConfigurationTypeDef(TypedDict):
    nonFilterableMetadataKeys: Sequence[str]

class PutVectorBucketPolicyInputTypeDef(TypedDict):
    policy: str
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]

class QueryOutputVectorTypeDef(TypedDict):
    key: str
    distance: NotRequired[float]
    metadata: NotRequired[Dict[str, Any]]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class VectorDataTypeDef(TypedDict):
    float32: NotRequired[Sequence[float]]

class CreateVectorBucketInputTypeDef(TypedDict):
    vectorBucketName: str
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class VectorBucketTypeDef(TypedDict):
    vectorBucketName: str
    vectorBucketArn: str
    creationTime: datetime
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]

class CreateIndexOutputTypeDef(TypedDict):
    indexArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVectorBucketOutputTypeDef(TypedDict):
    vectorBucketArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVectorBucketPolicyOutputTypeDef(TypedDict):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutputVectorTypeDef(TypedDict):
    key: str
    data: NotRequired[VectorDataOutputTypeDef]
    metadata: NotRequired[Dict[str, Any]]

class ListOutputVectorTypeDef(TypedDict):
    key: str
    data: NotRequired[VectorDataOutputTypeDef]
    metadata: NotRequired[Dict[str, Any]]

class ListIndexesOutputTypeDef(TypedDict):
    indexes: List[IndexSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class IndexTypeDef(TypedDict):
    vectorBucketName: str
    indexName: str
    indexArn: str
    creationTime: datetime
    dataType: Literal["float32"]
    dimension: int
    distanceMetric: DistanceMetricType
    metadataConfiguration: NotRequired[MetadataConfigurationOutputTypeDef]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]

class ListIndexesInputPaginateTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVectorBucketsInputPaginateTypeDef(TypedDict):
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVectorsInputPaginateTypeDef(TypedDict):
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]
    segmentCount: NotRequired[int]
    segmentIndex: NotRequired[int]
    returnData: NotRequired[bool]
    returnMetadata: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVectorBucketsOutputTypeDef(TypedDict):
    vectorBuckets: List[VectorBucketSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

MetadataConfigurationUnionTypeDef = Union[
    MetadataConfigurationTypeDef, MetadataConfigurationOutputTypeDef
]

class QueryVectorsOutputTypeDef(TypedDict):
    vectors: List[QueryOutputVectorTypeDef]
    distanceMetric: DistanceMetricType
    ResponseMetadata: ResponseMetadataTypeDef

VectorDataUnionTypeDef = Union[VectorDataTypeDef, VectorDataOutputTypeDef]

class GetVectorBucketOutputTypeDef(TypedDict):
    vectorBucket: VectorBucketTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVectorsOutputTypeDef(TypedDict):
    vectors: List[GetOutputVectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVectorsOutputTypeDef(TypedDict):
    vectors: List[ListOutputVectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetIndexOutputTypeDef(TypedDict):
    index: IndexTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexInputTypeDef(TypedDict):
    indexName: str
    dataType: Literal["float32"]
    dimension: int
    distanceMetric: DistanceMetricType
    vectorBucketName: NotRequired[str]
    vectorBucketArn: NotRequired[str]
    metadataConfiguration: NotRequired[MetadataConfigurationUnionTypeDef]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class PutInputVectorTypeDef(TypedDict):
    key: str
    data: VectorDataUnionTypeDef
    metadata: NotRequired[Mapping[str, Any]]

QueryVectorsInputTypeDef = TypedDict(
    "QueryVectorsInputTypeDef",
    {
        "topK": int,
        "queryVector": VectorDataUnionTypeDef,
        "vectorBucketName": NotRequired[str],
        "indexName": NotRequired[str],
        "indexArn": NotRequired[str],
        "filter": NotRequired[Mapping[str, Any]],
        "returnMetadata": NotRequired[bool],
        "returnDistance": NotRequired[bool],
    },
)

class PutVectorsInputTypeDef(TypedDict):
    vectors: Sequence[PutInputVectorTypeDef]
    vectorBucketName: NotRequired[str]
    indexName: NotRequired[str]
    indexArn: NotRequired[str]
