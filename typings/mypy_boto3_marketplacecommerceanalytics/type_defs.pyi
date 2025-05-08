"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import DataSetTypeType, SupportDataSetTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GenerateDataSetRequestTypeDef",
    "GenerateDataSetResultTypeDef",
    "ResponseMetadataTypeDef",
    "StartSupportDataExportRequestTypeDef",
    "StartSupportDataExportResultTypeDef",
    "TimestampTypeDef",
)

TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GenerateDataSetRequestTypeDef(TypedDict):
    dataSetType: DataSetTypeType
    dataSetPublicationDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: NotRequired[str]
    customerDefinedValues: NotRequired[Mapping[str, str]]

class StartSupportDataExportRequestTypeDef(TypedDict):
    dataSetType: SupportDataSetTypeType
    fromDate: TimestampTypeDef
    roleNameArn: str
    destinationS3BucketName: str
    snsTopicArn: str
    destinationS3Prefix: NotRequired[str]
    customerDefinedValues: NotRequired[Mapping[str, str]]

class GenerateDataSetResultTypeDef(TypedDict):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSupportDataExportResultTypeDef(TypedDict):
    dataSetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
