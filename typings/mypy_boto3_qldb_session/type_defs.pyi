"""
Main interface for qldb-session service type definitions.

Usage::

    ```python
    from mypy_boto3_qldb_session.type_defs import CommitTransactionResultTypeDef

    data: CommitTransactionResultTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CommitTransactionResultTypeDef",
    "ExecuteStatementResultTypeDef",
    "FetchPageResultTypeDef",
    "PageTypeDef",
    "StartSessionResultTypeDef",
    "StartTransactionResultTypeDef",
    "ValueHolderTypeDef",
    "CommitTransactionRequestTypeDef",
    "ExecuteStatementRequestTypeDef",
    "FetchPageRequestTypeDef",
    "SendCommandResultTypeDef",
    "StartSessionRequestTypeDef",
)

CommitTransactionResultTypeDef = TypedDict(
    "CommitTransactionResultTypeDef",
    {"TransactionId": str, "CommitDigest": Union[bytes, IO[bytes]]},
    total=False,
)

ExecuteStatementResultTypeDef = TypedDict(
    "ExecuteStatementResultTypeDef", {"FirstPage": "PageTypeDef"}, total=False
)

FetchPageResultTypeDef = TypedDict("FetchPageResultTypeDef", {"Page": "PageTypeDef"}, total=False)

PageTypeDef = TypedDict(
    "PageTypeDef", {"Values": List["ValueHolderTypeDef"], "NextPageToken": str}, total=False
)

StartSessionResultTypeDef = TypedDict(
    "StartSessionResultTypeDef", {"SessionToken": str}, total=False
)

StartTransactionResultTypeDef = TypedDict(
    "StartTransactionResultTypeDef", {"TransactionId": str}, total=False
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
        "EndSession": Dict[str, Any],
        "CommitTransaction": "CommitTransactionResultTypeDef",
        "AbortTransaction": Dict[str, Any],
        "ExecuteStatement": "ExecuteStatementResultTypeDef",
        "FetchPage": "FetchPageResultTypeDef",
    },
    total=False,
)

StartSessionRequestTypeDef = TypedDict("StartSessionRequestTypeDef", {"LedgerName": str})
