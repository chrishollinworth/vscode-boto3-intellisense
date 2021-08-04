"""
Type annotations for qldb-session service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb_session.type_defs import AbortTransactionResultTypeDef

    data: AbortTransactionResultTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AbortTransactionResultTypeDef",
    "CommitTransactionRequestTypeDef",
    "CommitTransactionResultTypeDef",
    "EndSessionResultTypeDef",
    "ExecuteStatementRequestTypeDef",
    "ExecuteStatementResultTypeDef",
    "FetchPageRequestTypeDef",
    "FetchPageResultTypeDef",
    "IOUsageTypeDef",
    "PageTypeDef",
    "ResponseMetadataTypeDef",
    "SendCommandRequestRequestTypeDef",
    "SendCommandResultTypeDef",
    "StartSessionRequestTypeDef",
    "StartSessionResultTypeDef",
    "StartTransactionResultTypeDef",
    "TimingInformationTypeDef",
    "ValueHolderTypeDef",
)

AbortTransactionResultTypeDef = TypedDict(
    "AbortTransactionResultTypeDef",
    {
        "TimingInformation": "TimingInformationTypeDef",
    },
    total=False,
)

CommitTransactionRequestTypeDef = TypedDict(
    "CommitTransactionRequestTypeDef",
    {
        "TransactionId": str,
        "CommitDigest": Union[bytes, IO[bytes], StreamingBody],
    },
)

CommitTransactionResultTypeDef = TypedDict(
    "CommitTransactionResultTypeDef",
    {
        "TransactionId": str,
        "CommitDigest": bytes,
        "TimingInformation": "TimingInformationTypeDef",
        "ConsumedIOs": "IOUsageTypeDef",
    },
    total=False,
)

EndSessionResultTypeDef = TypedDict(
    "EndSessionResultTypeDef",
    {
        "TimingInformation": "TimingInformationTypeDef",
    },
    total=False,
)

_RequiredExecuteStatementRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementRequestTypeDef",
    {
        "TransactionId": str,
        "Statement": str,
    },
)
_OptionalExecuteStatementRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementRequestTypeDef",
    {
        "Parameters": List["ValueHolderTypeDef"],
    },
    total=False,
)

class ExecuteStatementRequestTypeDef(
    _RequiredExecuteStatementRequestTypeDef, _OptionalExecuteStatementRequestTypeDef
):
    pass

ExecuteStatementResultTypeDef = TypedDict(
    "ExecuteStatementResultTypeDef",
    {
        "FirstPage": "PageTypeDef",
        "TimingInformation": "TimingInformationTypeDef",
        "ConsumedIOs": "IOUsageTypeDef",
    },
    total=False,
)

FetchPageRequestTypeDef = TypedDict(
    "FetchPageRequestTypeDef",
    {
        "TransactionId": str,
        "NextPageToken": str,
    },
)

FetchPageResultTypeDef = TypedDict(
    "FetchPageResultTypeDef",
    {
        "Page": "PageTypeDef",
        "TimingInformation": "TimingInformationTypeDef",
        "ConsumedIOs": "IOUsageTypeDef",
    },
    total=False,
)

IOUsageTypeDef = TypedDict(
    "IOUsageTypeDef",
    {
        "ReadIOs": int,
        "WriteIOs": int,
    },
    total=False,
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "Values": List["ValueHolderTypeDef"],
        "NextPageToken": str,
    },
    total=False,
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

SendCommandRequestRequestTypeDef = TypedDict(
    "SendCommandRequestRequestTypeDef",
    {
        "SessionToken": str,
        "StartSession": "StartSessionRequestTypeDef",
        "StartTransaction": Dict[str, Any],
        "EndSession": Dict[str, Any],
        "CommitTransaction": "CommitTransactionRequestTypeDef",
        "AbortTransaction": Dict[str, Any],
        "ExecuteStatement": "ExecuteStatementRequestTypeDef",
        "FetchPage": "FetchPageRequestTypeDef",
    },
    total=False,
)

SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef",
    {
        "StartSession": "StartSessionResultTypeDef",
        "StartTransaction": "StartTransactionResultTypeDef",
        "EndSession": "EndSessionResultTypeDef",
        "CommitTransaction": "CommitTransactionResultTypeDef",
        "AbortTransaction": "AbortTransactionResultTypeDef",
        "ExecuteStatement": "ExecuteStatementResultTypeDef",
        "FetchPage": "FetchPageResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSessionRequestTypeDef = TypedDict(
    "StartSessionRequestTypeDef",
    {
        "LedgerName": str,
    },
)

StartSessionResultTypeDef = TypedDict(
    "StartSessionResultTypeDef",
    {
        "SessionToken": str,
        "TimingInformation": "TimingInformationTypeDef",
    },
    total=False,
)

StartTransactionResultTypeDef = TypedDict(
    "StartTransactionResultTypeDef",
    {
        "TransactionId": str,
        "TimingInformation": "TimingInformationTypeDef",
    },
    total=False,
)

TimingInformationTypeDef = TypedDict(
    "TimingInformationTypeDef",
    {
        "ProcessingTimeMilliseconds": int,
    },
    total=False,
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonBinary": Union[bytes, IO[bytes], StreamingBody],
        "IonText": str,
    },
    total=False,
)
