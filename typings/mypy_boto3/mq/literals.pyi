"""
Type annotations for mq service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/literals.html)

Usage::

    ```python
    from mypy_boto3_mq.literals import AuthenticationStrategyType

    data: AuthenticationStrategyType = "LDAP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthenticationStrategyType",
    "BrokerStateType",
    "BrokerStorageTypeType",
    "ChangeTypeType",
    "DayOfWeekType",
    "DeploymentModeType",
    "EngineTypeType",
    "ListBrokersPaginatorName",
    "SanitizationWarningReasonType",
)

AuthenticationStrategyType = Literal["LDAP", "SIMPLE"]
BrokerStateType = Literal[
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "DELETION_IN_PROGRESS",
    "REBOOT_IN_PROGRESS",
    "RUNNING",
]
BrokerStorageTypeType = Literal["EBS", "EFS"]
ChangeTypeType = Literal["CREATE", "DELETE", "UPDATE"]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DeploymentModeType = Literal["ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ", "SINGLE_INSTANCE"]
EngineTypeType = Literal["ACTIVEMQ", "RABBITMQ"]
ListBrokersPaginatorName = Literal["list_brokers"]
SanitizationWarningReasonType = Literal[
    "DISALLOWED_ATTRIBUTE_REMOVED", "DISALLOWED_ELEMENT_REMOVED", "INVALID_ATTRIBUTE_VALUE_REMOVED"
]
