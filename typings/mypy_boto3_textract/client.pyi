# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_textract.type_defs import (
    AnalyzeDocumentResponseTypeDef,
    DetectDocumentTextResponseTypeDef,
    DocumentLocationTypeDef,
    DocumentTypeDef,
    GetDocumentAnalysisResponseTypeDef,
    GetDocumentTextDetectionResponseTypeDef,
    HumanLoopConfigTypeDef,
    NotificationChannelTypeDef,
    StartDocumentAnalysisResponseTypeDef,
    StartDocumentTextDetectionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TextractClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    BadDocumentException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    DocumentTooLargeException: Type[Boto3ClientError]
    HumanLoopQuotaExceededException: Type[Boto3ClientError]
    IdempotentParameterMismatchException: Type[Boto3ClientError]
    InternalServerError: Type[Boto3ClientError]
    InvalidJobIdException: Type[Boto3ClientError]
    InvalidParameterException: Type[Boto3ClientError]
    InvalidS3ObjectException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ProvisionedThroughputExceededException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    UnsupportedDocumentException: Type[Boto3ClientError]


class TextractClient:
    """
    [Textract.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client)
    """

    exceptions: Exceptions

    def analyze_document(
        self,
        Document: DocumentTypeDef,
        FeatureTypes: List[Literal["TABLES", "FORMS"]],
        HumanLoopConfig: HumanLoopConfigTypeDef = None,
    ) -> AnalyzeDocumentResponseTypeDef:
        """
        [Client.analyze_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.analyze_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.can_paginate)
        """

    def detect_document_text(self, Document: DocumentTypeDef) -> DetectDocumentTextResponseTypeDef:
        """
        [Client.detect_document_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.detect_document_text)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.generate_presigned_url)
        """

    def get_document_analysis(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentAnalysisResponseTypeDef:
        """
        [Client.get_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.get_document_analysis)
        """

    def get_document_text_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentTextDetectionResponseTypeDef:
        """
        [Client.get_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.get_document_text_detection)
        """

    def start_document_analysis(
        self,
        DocumentLocation: DocumentLocationTypeDef,
        FeatureTypes: List[Literal["TABLES", "FORMS"]],
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
    ) -> StartDocumentAnalysisResponseTypeDef:
        """
        [Client.start_document_analysis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.start_document_analysis)
        """

    def start_document_text_detection(
        self,
        DocumentLocation: DocumentLocationTypeDef,
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
    ) -> StartDocumentTextDetectionResponseTypeDef:
        """
        [Client.start_document_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/textract.html#Textract.Client.start_document_text_detection)
        """
