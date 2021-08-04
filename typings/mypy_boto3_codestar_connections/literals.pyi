"""
Type annotations for codestar-connections service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/literals.html)

Usage::

    ```python
    from mypy_boto3_codestar_connections.literals import ConnectionStatusType

    data: ConnectionStatusType = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ConnectionStatusType", "ProviderTypeType")

ConnectionStatusType = Literal["AVAILABLE", "ERROR", "PENDING"]
ProviderTypeType = Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"]
