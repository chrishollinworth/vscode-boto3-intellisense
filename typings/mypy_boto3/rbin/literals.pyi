"""
Type annotations for rbin service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/literals.html)

Usage::

    ```python
    from mypy_boto3_rbin.literals import ListRulesPaginatorName

    data: ListRulesPaginatorName = "list_rules"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListRulesPaginatorName",
    "ResourceTypeType",
    "RetentionPeriodUnitType",
    "RuleStatusType",
)

ListRulesPaginatorName = Literal["list_rules"]
ResourceTypeType = Literal["EBS_SNAPSHOT", "EC2_IMAGE"]
RetentionPeriodUnitType = Literal["DAYS"]
RuleStatusType = Literal["available", "pending"]
