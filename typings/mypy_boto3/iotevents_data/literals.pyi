"""
Type annotations for iotevents-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/literals.html)

Usage::

    ```python
    from mypy_boto3_iotevents_data.literals import AlarmStateNameType

    data: AlarmStateNameType = "ACKNOWLEDGED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlarmStateNameType",
    "ComparisonOperatorType",
    "CustomerActionNameType",
    "ErrorCodeType",
    "EventTypeType",
    "TriggerTypeType",
)

AlarmStateNameType = Literal[
    "ACKNOWLEDGED", "ACTIVE", "DISABLED", "LATCHED", "NORMAL", "SNOOZE_DISABLED"
]
ComparisonOperatorType = Literal[
    "EQUAL", "GREATER", "GREATER_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "NOT_EQUAL"
]
CustomerActionNameType = Literal["ACKNOWLEDGE", "DISABLE", "ENABLE", "RESET", "SNOOZE"]
ErrorCodeType = Literal[
    "InternalFailureException",
    "InvalidRequestException",
    "ResourceNotFoundException",
    "ServiceUnavailableException",
    "ThrottlingException",
]
EventTypeType = Literal["STATE_CHANGE"]
TriggerTypeType = Literal["SNOOZE_TIMEOUT"]
