"""
Main interface for qldb-session service type definitions.

Usage::

    ```python
    from mypy_boto3_qldb_session.type_defs import AbortTransactionResultTypeDef

    data: AbortTransactionResultTypeDef = {...}
    ```
"""
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AbortTransactionResultTypeDef",
    "CommitTransactionResultTypeDef",
    "EndSessionResultTypeDef",
    "ExecuteStatementResultTypeDef",
    "FetchPageResultTypeDef",
    "IOUsageTypeDef",
    "PageTypeDef",
    "StartSessionResultTypeDef",
    "StartTransactionResultTypeDef",
    "TimingInformationTypeDef",
    "ValueHolderTypeDef",
    "CommitTransactionRequestTypeDef",
    "ExecuteStatementRequestTypeDef",
    "FetchPageRequestTypeDef",
    "SendCommandResultTypeDef",
    "StartSessionRequestTypeDef",
)

AbortTransactionResultTypeDef = TypedDict(
    "AbortTransactionResultTypeDef", {"TimingInformation": "TimingInformationTypeDef"}, total=False
)

CommitTransactionResultTypeDef = TypedDict(
    "CommitTransactionResultTypeDef",
    {
        "TransactionId": str,
        "CommitDigest": Union[bytes, IO[bytes]],
        "TimingInformation": "TimingInformationTypeDef",
        "ConsumedIOs": "IOUsageTypeDef",
    },
    total=False,
)

EndSessionResultTypeDef = TypedDict(
    "EndSessionResultTypeDef", {"TimingInformation": "TimingInformationTypeDef"}, total=False
)

ExecuteStatementResultTypeDef = TypedDict(
    "ExecuteStatementResultTypeDef",
    {
        "FirstPage": "PageTypeDef",
        "TimingInformation": "TimingInformationTypeDef",
        "ConsumedIOs": "IOUsageTypeDef",
    },
    total=False,
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

IOUsageTypeDef = TypedDict("IOUsageTypeDef", {"ReadIOs": int, "WriteIOs": int}, total=False)

PageTypeDef = TypedDict(
    "PageTypeDef", {"Values": List["ValueHolderTypeDef"], "NextPageToken": str}, total=False
)

StartSessionResultTypeDef = TypedDict(
    "StartSessionResultTypeDef",
    {"SessionToken": str, "TimingInformation": "TimingInformationTypeDef"},
    total=False,
)

StartTransactionResultTypeDef = TypedDict(
    "StartTransactionResultTypeDef",
    {"TransactionId": str, "TimingInformation": "TimingInformationTypeDef"},
    total=False,
)

TimingInformationTypeDef = TypedDict(
    "TimingInformationTypeDef", {"ProcessingTimeMilliseconds": int}, total=False
)

ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef", {"IonBinary": Union[bytes, IO[bytes]], "IonText": str}, total=False
)

CommitTransactionRequestTypeDef = TypedDict(
    "CommitTransactionRequestTypeDef",
    {"TransactionId": str, "CommitDigest": Union[bytes, IO[bytes]]},
)

_RequiredExecuteStatementRequestTypeDef = TypedDict(
    "_RequiredExecuteStatementRequestTypeDef", {"TransactionId": str, "Statement": str}
)
_OptionalExecuteStatementRequestTypeDef = TypedDict(
    "_OptionalExecuteStatementRequestTypeDef",
    {"Parameters": List["ValueHolderTypeDef"]},
    total=False,
)


class ExecuteStatementRequestTypeDef(
    _RequiredExecuteStatementRequestTypeDef, _OptionalExecuteStatementRequestTypeDef
):
    pass


FetchPageRequestTypeDef = TypedDict(
    "FetchPageRequestTypeDef", {"TransactionId": str, "NextPageToken": str}
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
    },
    total=False,
)

StartSessionRequestTypeDef = TypedDict("StartSessionRequestTypeDef", {"LedgerName": str})
