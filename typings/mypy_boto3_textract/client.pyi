# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for textract service client

Usage::

    ```python
    import boto3
    from mypy_boto3_textract import TextractClient

    client: TextractClient = boto3.client("textract")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_textract.type_defs import (
    AnalyzeDocumentResponseTypeDef,
    DetectDocumentTextResponseTypeDef,
    DocumentLocationTypeDef,
    DocumentTypeDef,
    GetDocumentAnalysisResponseTypeDef,
    GetDocumentTextDetectionResponseTypeDef,
    HumanLoopConfigTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    StartDocumentAnalysisResponseTypeDef,
    StartDocumentTextDetectionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TextractClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadDocumentException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DocumentTooLargeException: Type[BotocoreClientError]
    HumanLoopQuotaExceededException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidJobIdException: Type[BotocoreClientError]
    InvalidKMSKeyException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidS3ObjectException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedDocumentException: Type[BotocoreClientError]


class TextractClient:
    """
    [Textract.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def analyze_document(
        self,
        Document: DocumentTypeDef,
        FeatureTypes: List[Literal["TABLES", "FORMS"]],
        HumanLoopConfig: HumanLoopConfigTypeDef = None,
    ) -> AnalyzeDocumentResponseTypeDef:
        """
        [Client.analyze_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.analyze_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.can_paginate)
        """

    def detect_document_text(self, Document: DocumentTypeDef) -> DetectDocumentTextResponseTypeDef:
        """
        [Client.detect_document_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.detect_document_text)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.generate_presigned_url)
        """

    def get_document_analysis(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentAnalysisResponseTypeDef:
        """
        [Client.get_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.get_document_analysis)
        """

    def get_document_text_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentTextDetectionResponseTypeDef:
        """
        [Client.get_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.get_document_text_detection)
        """

    def start_document_analysis(
        self,
        DocumentLocation: DocumentLocationTypeDef,
        FeatureTypes: List[Literal["TABLES", "FORMS"]],
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        OutputConfig: OutputConfigTypeDef = None,
        KMSKeyId: str = None,
    ) -> StartDocumentAnalysisResponseTypeDef:
        """
        [Client.start_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.start_document_analysis)
        """

    def start_document_text_detection(
        self,
        DocumentLocation: DocumentLocationTypeDef,
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        OutputConfig: OutputConfigTypeDef = None,
        KMSKeyId: str = None,
    ) -> StartDocumentTextDetectionResponseTypeDef:
        """
        [Client.start_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/textract.html#Textract.Client.start_document_text_detection)
        """
