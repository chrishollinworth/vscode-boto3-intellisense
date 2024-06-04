"""
Type annotations for license-manager-linux-subscriptions service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager_linux_subscriptions/literals.html)

Usage::

    ```python
    from mypy_boto3_license_manager_linux_subscriptions.literals import LinuxSubscriptionsDiscoveryType

    data: LinuxSubscriptionsDiscoveryType = "Disabled"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "LinuxSubscriptionsDiscoveryType",
    "ListLinuxSubscriptionInstancesPaginatorName",
    "ListLinuxSubscriptionsPaginatorName",
    "OperatorType",
    "OrganizationIntegrationType",
    "StatusType",
)

LinuxSubscriptionsDiscoveryType = Literal["Disabled", "Enabled"]
ListLinuxSubscriptionInstancesPaginatorName = Literal["list_linux_subscription_instances"]
ListLinuxSubscriptionsPaginatorName = Literal["list_linux_subscriptions"]
OperatorType = Literal["Contains", "Equal", "NotEqual"]
OrganizationIntegrationType = Literal["Disabled", "Enabled"]
StatusType = Literal["Completed", "Failed", "InProgress", "Successful"]
