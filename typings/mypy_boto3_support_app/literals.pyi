"""
Type annotations for support-app service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/literals.html)

Usage::

    ```python
    from mypy_boto3_support_app.literals import NotificationSeverityLevelType

    data: NotificationSeverityLevelType = "all"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NotificationSeverityLevelType",)

NotificationSeverityLevelType = Literal["all", "high", "none"]
