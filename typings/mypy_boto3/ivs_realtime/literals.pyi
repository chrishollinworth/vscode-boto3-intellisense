"""
Type annotations for ivs-realtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/literals.html)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.literals import ParticipantTokenCapabilityType

    data: ParticipantTokenCapabilityType = "PUBLISH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ParticipantTokenCapabilityType",)

ParticipantTokenCapabilityType = Literal["PUBLISH", "SUBSCRIBE"]
