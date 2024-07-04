"""
Type annotations for pca-connector-scep service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pca_connector_scep/literals.html)

Usage::

    ```python
    from mypy_boto3_pca_connector_scep.literals import ConnectorStatusReasonType

    data: ConnectorStatusReasonType = "INTERNAL_FAILURE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConnectorStatusReasonType",
    "ConnectorStatusType",
    "ConnectorTypeType",
    "ListChallengeMetadataPaginatorName",
    "ListConnectorsPaginatorName",
)

ConnectorStatusReasonType = Literal[
    "INTERNAL_FAILURE",
    "PRIVATECA_ACCESS_DENIED",
    "PRIVATECA_INVALID_STATE",
    "PRIVATECA_RESOURCE_NOT_FOUND",
]
ConnectorStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
ConnectorTypeType = Literal["GENERAL_PURPOSE", "INTUNE"]
ListChallengeMetadataPaginatorName = Literal["list_challenge_metadata"]
ListConnectorsPaginatorName = Literal["list_connectors"]
