"""
Type annotations for iot-roborunner service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/literals.html)

Usage::

    ```python
    from mypy_boto3_iot_roborunner.literals import DestinationStateType

    data: DestinationStateType = "DECOMMISSIONED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DestinationStateType",
    "ListDestinationsPaginatorName",
    "ListSitesPaginatorName",
    "ListWorkerFleetsPaginatorName",
    "ListWorkersPaginatorName",
)

DestinationStateType = Literal["DECOMMISSIONED", "DISABLED", "ENABLED"]
ListDestinationsPaginatorName = Literal["list_destinations"]
ListSitesPaginatorName = Literal["list_sites"]
ListWorkerFleetsPaginatorName = Literal["list_worker_fleets"]
ListWorkersPaginatorName = Literal["list_workers"]
