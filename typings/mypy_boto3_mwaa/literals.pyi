"""
Type annotations for mwaa service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/literals.html)

Usage::

    ```python
    from mypy_boto3_mwaa.literals import EndpointManagementType

    data: EndpointManagementType = "CUSTOMER"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "EndpointManagementType",
    "EnvironmentStatusType",
    "ListEnvironmentsPaginatorName",
    "LoggingLevelType",
    "UnitType",
    "UpdateStatusType",
    "WebserverAccessModeType",
)

EndpointManagementType = Literal["CUSTOMER", "SERVICE"]
EnvironmentStatusType = Literal[
    "AVAILABLE",
    "CREATE_FAILED",
    "CREATING",
    "CREATING_SNAPSHOT",
    "DELETED",
    "DELETING",
    "MAINTENANCE",
    "PENDING",
    "ROLLING_BACK",
    "UNAVAILABLE",
    "UPDATE_FAILED",
    "UPDATING",
]
ListEnvironmentsPaginatorName = Literal["list_environments"]
LoggingLevelType = Literal["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"]
UnitType = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
UpdateStatusType = Literal["FAILED", "PENDING", "SUCCESS"]
WebserverAccessModeType = Literal["PRIVATE_ONLY", "PUBLIC_ONLY"]
