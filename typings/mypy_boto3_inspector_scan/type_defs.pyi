"""
Type annotations for inspector-scan service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/type_defs.html)

Usage::

    ```python
    from mypy_boto3_inspector_scan.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict

from .literals import OutputFormatType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = ("ResponseMetadataTypeDef", "ScanSbomRequestRequestTypeDef", "ScanSbomResponseTypeDef")

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredScanSbomRequestRequestTypeDef = TypedDict(
    "_RequiredScanSbomRequestRequestTypeDef",
    {
        "sbom": Dict[str, Any],
    },
)
_OptionalScanSbomRequestRequestTypeDef = TypedDict(
    "_OptionalScanSbomRequestRequestTypeDef",
    {
        "outputFormat": OutputFormatType,
    },
    total=False,
)

class ScanSbomRequestRequestTypeDef(
    _RequiredScanSbomRequestRequestTypeDef, _OptionalScanSbomRequestRequestTypeDef
):
    pass

ScanSbomResponseTypeDef = TypedDict(
    "ScanSbomResponseTypeDef",
    {
        "sbom": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
