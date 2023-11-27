"""
Type annotations for inspector-scan service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_inspector_scan import inspectorscanClient

    client: inspectorscanClient = boto3.client("inspector-scan")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import OutputFormatType
from .type_defs import ScanSbomResponseTypeDef

__all__ = ("inspectorscanClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class inspectorscanClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/inspector-scan.html#inspectorscan.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        inspectorscanClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/inspector-scan.html#inspectorscan.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/inspector-scan.html#inspectorscan.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/client.html#close)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/inspector-scan.html#inspectorscan.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/client.html#generate_presigned_url)
        """
    def scan_sbom(
        self, *, sbom: Dict[str, Any], outputFormat: OutputFormatType = None
    ) -> ScanSbomResponseTypeDef:
        """
        Scans a provided CycloneDX 1.5 SBOM and reports on any vulnerabilities
        discovered in that SBOM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/inspector-scan.html#inspectorscan.Client.scan_sbom)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/client.html#scan_sbom)
        """
