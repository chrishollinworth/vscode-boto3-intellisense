"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import ChangesetInfoTypeDef

    data: ChangesetInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict

from .literals import (
    ChangesetStatusType,
    ChangeTypeType,
    ErrorCategoryType,
    FormatTypeType,
    locationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ChangesetInfoTypeDef",
    "CreateChangesetRequestRequestTypeDef",
    "CreateChangesetResponseTypeDef",
    "CredentialsTypeDef",
    "ErrorInfoTypeDef",
    "GetProgrammaticAccessCredentialsRequestRequestTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetWorkingLocationRequestRequestTypeDef",
    "GetWorkingLocationResponseTypeDef",
    "ResponseMetadataTypeDef",
)

ChangesetInfoTypeDef = TypedDict(
    "ChangesetInfoTypeDef",
    {
        "id": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceType": Literal["S3"],
        "sourceParams": Dict[str, str],
        "formatType": FormatTypeType,
        "formatParams": Dict[str, str],
        "createTimestamp": datetime,
        "status": ChangesetStatusType,
        "errorInfo": "ErrorInfoTypeDef",
        "changesetLabels": Dict[str, str],
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
    },
    total=False,
)

_RequiredCreateChangesetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChangesetRequestRequestTypeDef",
    {
        "datasetId": str,
        "changeType": ChangeTypeType,
        "sourceType": Literal["S3"],
        "sourceParams": Dict[str, str],
    },
)
_OptionalCreateChangesetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChangesetRequestRequestTypeDef",
    {
        "formatType": FormatTypeType,
        "formatParams": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateChangesetRequestRequestTypeDef(
    _RequiredCreateChangesetRequestRequestTypeDef, _OptionalCreateChangesetRequestRequestTypeDef
):
    pass

CreateChangesetResponseTypeDef = TypedDict(
    "CreateChangesetResponseTypeDef",
    {
        "changeset": "ChangesetInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "errorMessage": str,
        "errorCategory": ErrorCategoryType,
    },
    total=False,
)

_RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef",
    {
        "durationInMinutes": int,
    },
    total=False,
)

class GetProgrammaticAccessCredentialsRequestRequestTypeDef(
    _RequiredGetProgrammaticAccessCredentialsRequestRequestTypeDef,
    _OptionalGetProgrammaticAccessCredentialsRequestRequestTypeDef,
):
    pass

GetProgrammaticAccessCredentialsResponseTypeDef = TypedDict(
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    {
        "credentials": "CredentialsTypeDef",
        "durationInMinutes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkingLocationRequestRequestTypeDef = TypedDict(
    "GetWorkingLocationRequestRequestTypeDef",
    {
        "locationType": locationTypeType,
    },
    total=False,
)

GetWorkingLocationResponseTypeDef = TypedDict(
    "GetWorkingLocationResponseTypeDef",
    {
        "s3Uri": str,
        "s3Path": str,
        "s3Bucket": str,
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
