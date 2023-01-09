"""
Type annotations for iottwinmaker service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iottwinmaker/literals.html)

Usage::

    ```python
    from mypy_boto3_iottwinmaker.literals import ColumnTypeType

    data: ColumnTypeType = "EDGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ColumnTypeType",
    "ComponentUpdateTypeType",
    "ErrorCodeType",
    "GroupTypeType",
    "InterpolationTypeType",
    "OrderByTimeType",
    "OrderType",
    "ParentEntityUpdateTypeType",
    "PricingModeType",
    "PricingTierType",
    "PropertyGroupUpdateTypeType",
    "PropertyUpdateTypeType",
    "ScopeType",
    "StateType",
    "SyncJobStateType",
    "SyncResourceStateType",
    "SyncResourceTypeType",
    "TypeType",
    "UpdateReasonType",
)

ColumnTypeType = Literal["EDGE", "NODE", "VALUE"]
ComponentUpdateTypeType = Literal["CREATE", "DELETE", "UPDATE"]
ErrorCodeType = Literal[
    "INTERNAL_FAILURE",
    "SYNC_CREATING_ERROR",
    "SYNC_INITIALIZING_ERROR",
    "SYNC_PROCESSING_ERROR",
    "VALIDATION_ERROR",
]
GroupTypeType = Literal["TABULAR"]
InterpolationTypeType = Literal["LINEAR"]
OrderByTimeType = Literal["ASCENDING", "DESCENDING"]
OrderType = Literal["ASCENDING", "DESCENDING"]
ParentEntityUpdateTypeType = Literal["DELETE", "UPDATE"]
PricingModeType = Literal["BASIC", "STANDARD", "TIERED_BUNDLE"]
PricingTierType = Literal["TIER_1", "TIER_2", "TIER_3", "TIER_4"]
PropertyGroupUpdateTypeType = Literal["CREATE", "DELETE", "UPDATE"]
PropertyUpdateTypeType = Literal["CREATE", "DELETE", "UPDATE"]
ScopeType = Literal["ENTITY", "WORKSPACE"]
StateType = Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "UPDATING"]
SyncJobStateType = Literal["ACTIVE", "CREATING", "DELETING", "ERROR", "INITIALIZING"]
SyncResourceStateType = Literal["DELETED", "ERROR", "INITIALIZING", "IN_SYNC", "PROCESSING"]
SyncResourceTypeType = Literal["COMPONENT_TYPE", "ENTITY"]
TypeType = Literal["BOOLEAN", "DOUBLE", "INTEGER", "LIST", "LONG", "MAP", "RELATIONSHIP", "STRING"]
UpdateReasonType = Literal[
    "DEFAULT", "ENTITY_COUNT_UPDATE", "OVERWRITTEN", "PRICING_MODE_UPDATE", "PRICING_TIER_UPDATE"
]
