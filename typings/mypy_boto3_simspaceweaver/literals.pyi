"""
Type annotations for simspaceweaver service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_simspaceweaver/literals.html)

Usage::

    ```python
    from mypy_boto3_simspaceweaver.literals import ClockStatusType

    data: ClockStatusType = "STARTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ClockStatusType",
    "ClockTargetStatusType",
    "LifecycleManagementStrategyType",
    "SimulationAppStatusType",
    "SimulationAppTargetStatusType",
    "SimulationStatusType",
    "SimulationTargetStatusType",
)

ClockStatusType = Literal["STARTED", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"]
ClockTargetStatusType = Literal["STARTED", "STOPPED", "UNKNOWN"]
LifecycleManagementStrategyType = Literal[
    "ByRequest", "BySpatialSubdivision", "PerWorker", "Unknown"
]
SimulationAppStatusType = Literal["ERROR", "STARTED", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"]
SimulationAppTargetStatusType = Literal["STARTED", "STOPPED", "UNKNOWN"]
SimulationStatusType = Literal[
    "DELETED", "DELETING", "FAILED", "STARTED", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"
]
SimulationTargetStatusType = Literal["DELETED", "STARTED", "STOPPED", "UNKNOWN"]
