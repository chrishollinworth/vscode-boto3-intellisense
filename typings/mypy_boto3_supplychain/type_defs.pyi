"""
Type annotations for supplychain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_supplychain.type_defs import BillOfMaterialsImportJobTypeDef

    data: BillOfMaterialsImportJobTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, Union

from .literals import ConfigurationJobStatusType, DataIntegrationEventTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BillOfMaterialsImportJobTypeDef",
    "CreateBillOfMaterialsImportJobRequestRequestTypeDef",
    "CreateBillOfMaterialsImportJobResponseTypeDef",
    "GetBillOfMaterialsImportJobRequestRequestTypeDef",
    "GetBillOfMaterialsImportJobResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SendDataIntegrationEventRequestRequestTypeDef",
    "SendDataIntegrationEventResponseTypeDef",
)

_RequiredBillOfMaterialsImportJobTypeDef = TypedDict(
    "_RequiredBillOfMaterialsImportJobTypeDef",
    {
        "instanceId": str,
        "jobId": str,
        "status": ConfigurationJobStatusType,
        "s3uri": str,
    },
)
_OptionalBillOfMaterialsImportJobTypeDef = TypedDict(
    "_OptionalBillOfMaterialsImportJobTypeDef",
    {
        "message": str,
    },
    total=False,
)

class BillOfMaterialsImportJobTypeDef(
    _RequiredBillOfMaterialsImportJobTypeDef, _OptionalBillOfMaterialsImportJobTypeDef
):
    pass

_RequiredCreateBillOfMaterialsImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBillOfMaterialsImportJobRequestRequestTypeDef",
    {
        "instanceId": str,
        "s3uri": str,
    },
)
_OptionalCreateBillOfMaterialsImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBillOfMaterialsImportJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateBillOfMaterialsImportJobRequestRequestTypeDef(
    _RequiredCreateBillOfMaterialsImportJobRequestRequestTypeDef,
    _OptionalCreateBillOfMaterialsImportJobRequestRequestTypeDef,
):
    pass

CreateBillOfMaterialsImportJobResponseTypeDef = TypedDict(
    "CreateBillOfMaterialsImportJobResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBillOfMaterialsImportJobRequestRequestTypeDef = TypedDict(
    "GetBillOfMaterialsImportJobRequestRequestTypeDef",
    {
        "instanceId": str,
        "jobId": str,
    },
)

GetBillOfMaterialsImportJobResponseTypeDef = TypedDict(
    "GetBillOfMaterialsImportJobResponseTypeDef",
    {
        "job": "BillOfMaterialsImportJobTypeDef",
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

_RequiredSendDataIntegrationEventRequestRequestTypeDef = TypedDict(
    "_RequiredSendDataIntegrationEventRequestRequestTypeDef",
    {
        "instanceId": str,
        "eventType": DataIntegrationEventTypeType,
        "data": str,
        "eventGroupId": str,
    },
)
_OptionalSendDataIntegrationEventRequestRequestTypeDef = TypedDict(
    "_OptionalSendDataIntegrationEventRequestRequestTypeDef",
    {
        "eventTimestamp": Union[datetime, str],
        "clientToken": str,
    },
    total=False,
)

class SendDataIntegrationEventRequestRequestTypeDef(
    _RequiredSendDataIntegrationEventRequestRequestTypeDef,
    _OptionalSendDataIntegrationEventRequestRequestTypeDef,
):
    pass

SendDataIntegrationEventResponseTypeDef = TypedDict(
    "SendDataIntegrationEventResponseTypeDef",
    {
        "eventId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
