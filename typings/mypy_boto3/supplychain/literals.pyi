"""
Type annotations for supplychain service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_supplychain/literals.html)

Usage::

    ```python
    from mypy_boto3_supplychain.literals import ConfigurationJobStatusType

    data: ConfigurationJobStatusType = "FAILED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConfigurationJobStatusType", "DataIntegrationEventTypeType")

ConfigurationJobStatusType = Literal["FAILED", "IN_PROGRESS", "NEW", "QUEUED", "SUCCESS"]
DataIntegrationEventTypeType = Literal[
    "scn.data.forecast",
    "scn.data.inboundorder",
    "scn.data.inboundorderline",
    "scn.data.inboundorderlineschedule",
    "scn.data.inventorylevel",
    "scn.data.outboundorderline",
    "scn.data.outboundshipment",
    "scn.data.processheader",
    "scn.data.processoperation",
    "scn.data.processproduct",
    "scn.data.reservation",
    "scn.data.shipment",
    "scn.data.shipmentstop",
    "scn.data.shipmentstoporder",
    "scn.data.supplyplan",
]
