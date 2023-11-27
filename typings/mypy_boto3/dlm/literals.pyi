"""
Type annotations for dlm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/literals.html)

Usage::

    ```python
    from mypy_boto3_dlm.literals import DefaultPoliciesTypeValuesType

    data: DefaultPoliciesTypeValuesType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DefaultPoliciesTypeValuesType",
    "DefaultPolicyTypeValuesType",
    "EventSourceValuesType",
    "EventTypeValuesType",
    "ExecutionHandlerServiceValuesType",
    "GettablePolicyStateValuesType",
    "IntervalUnitValuesType",
    "LocationValuesType",
    "PolicyLanguageValuesType",
    "PolicyTypeValuesType",
    "ResourceLocationValuesType",
    "ResourceTypeValuesType",
    "RetentionIntervalUnitValuesType",
    "SettablePolicyStateValuesType",
    "StageValuesType",
)

DefaultPoliciesTypeValuesType = Literal["ALL", "INSTANCE", "VOLUME"]
DefaultPolicyTypeValuesType = Literal["INSTANCE", "VOLUME"]
EventSourceValuesType = Literal["MANAGED_CWE"]
EventTypeValuesType = Literal["shareSnapshot"]
ExecutionHandlerServiceValuesType = Literal["AWS_SYSTEMS_MANAGER"]
GettablePolicyStateValuesType = Literal["DISABLED", "ENABLED", "ERROR"]
IntervalUnitValuesType = Literal["HOURS"]
LocationValuesType = Literal["CLOUD", "OUTPOST_LOCAL"]
PolicyLanguageValuesType = Literal["SIMPLIFIED", "STANDARD"]
PolicyTypeValuesType = Literal["EBS_SNAPSHOT_MANAGEMENT", "EVENT_BASED_POLICY", "IMAGE_MANAGEMENT"]
ResourceLocationValuesType = Literal["CLOUD", "OUTPOST"]
ResourceTypeValuesType = Literal["INSTANCE", "VOLUME"]
RetentionIntervalUnitValuesType = Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]
SettablePolicyStateValuesType = Literal["DISABLED", "ENABLED"]
StageValuesType = Literal["POST", "PRE"]
