"""
Type annotations for marketplace-reporting service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_marketplace_reporting.type_defs import GetBuyerDashboardInputTypeDef

    data: GetBuyerDashboardInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetBuyerDashboardInputTypeDef",
    "GetBuyerDashboardOutputTypeDef",
    "ResponseMetadataTypeDef",
)

class GetBuyerDashboardInputTypeDef(TypedDict):
    dashboardIdentifier: str
    embeddingDomains: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetBuyerDashboardOutputTypeDef(TypedDict):
    embedUrl: str
    dashboardIdentifier: str
    embeddingDomains: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
