"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import GenerateDataSetRequestRequestTypeDef

    data: GenerateDataSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Union

from .literals import DataSetTypeType, SupportDataSetTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GenerateDataSetRequestRequestTypeDef",
    "GenerateDataSetResultTypeDef",
    "ResponseMetadataTypeDef",
    "StartSupportDataExportRequestRequestTypeDef",
    "StartSupportDataExportResultTypeDef",
)

_RequiredGenerateDataSetRequestRequestTypeDef = TypedDict(
    "_RequiredGenerateDataSetRequestRequestTypeDef",
    {
        "dataSetType": DataSetTypeType,
        "dataSetPublicationDate": Union[datetime, str],
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
    },
)
_OptionalGenerateDataSetRequestRequestTypeDef = TypedDict(
    "_OptionalGenerateDataSetRequestRequestTypeDef",
    {
        "destinationS3Prefix": str,
        "customerDefinedValues": Dict[str, str],
    },
    total=False,
)

class GenerateDataSetRequestRequestTypeDef(
    _RequiredGenerateDataSetRequestRequestTypeDef, _OptionalGenerateDataSetRequestRequestTypeDef
):
    pass

GenerateDataSetResultTypeDef = TypedDict(
    "GenerateDataSetResultTypeDef",
    {
        "dataSetRequestId": str,
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

_RequiredStartSupportDataExportRequestRequestTypeDef = TypedDict(
    "_RequiredStartSupportDataExportRequestRequestTypeDef",
    {
        "dataSetType": SupportDataSetTypeType,
        "fromDate": Union[datetime, str],
        "roleNameArn": str,
        "destinationS3BucketName": str,
        "snsTopicArn": str,
    },
)
_OptionalStartSupportDataExportRequestRequestTypeDef = TypedDict(
    "_OptionalStartSupportDataExportRequestRequestTypeDef",
    {
        "destinationS3Prefix": str,
        "customerDefinedValues": Dict[str, str],
    },
    total=False,
)

class StartSupportDataExportRequestRequestTypeDef(
    _RequiredStartSupportDataExportRequestRequestTypeDef,
    _OptionalStartSupportDataExportRequestRequestTypeDef,
):
    pass

StartSupportDataExportResultTypeDef = TypedDict(
    "StartSupportDataExportResultTypeDef",
    {
        "dataSetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
