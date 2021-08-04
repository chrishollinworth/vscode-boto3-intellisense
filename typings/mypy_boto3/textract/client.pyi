"""
Type annotations for textract service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_textract import TextractClient

    client: TextractClient = boto3.client("textract")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import FeatureTypeType
from .type_defs import (
    AnalyzeDocumentResponseTypeDef,
    AnalyzeExpenseResponseTypeDef,
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

class TextractClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        TextractClient exceptions.
        """
    def analyze_document(
        self,
        *,
        Document: "DocumentTypeDef",
        FeatureTypes: List[FeatureTypeType],
        HumanLoopConfig: "HumanLoopConfigTypeDef" = None
    ) -> AnalyzeDocumentResponseTypeDef:
        """
        Analyzes an input document for relationships between detected items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.analyze_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#analyze_document)
        """
    def analyze_expense(self, *, Document: "DocumentTypeDef") -> AnalyzeExpenseResponseTypeDef:
        """
        Analyzes an input document for financially related relationships between text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.analyze_expense)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#analyze_expense)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#can_paginate)
        """
    def detect_document_text(
        self, *, Document: "DocumentTypeDef"
    ) -> DetectDocumentTextResponseTypeDef:
        """
        Detects text in the input document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.detect_document_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#detect_document_text)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#generate_presigned_url)
        """
    def get_document_analysis(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentAnalysisResponseTypeDef:
        """
        Gets the results for an Amazon Textract asynchronous operation that analyzes
        text in a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.get_document_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_document_analysis)
        """
    def get_document_text_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentTextDetectionResponseTypeDef:
        """
        Gets the results for an Amazon Textract asynchronous operation that detects text
        in a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.get_document_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_document_text_detection)
        """
    def start_document_analysis(
        self,
        *,
        DocumentLocation: "DocumentLocationTypeDef",
        FeatureTypes: List[FeatureTypeType],
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        OutputConfig: "OutputConfigTypeDef" = None,
        KMSKeyId: str = None
    ) -> StartDocumentAnalysisResponseTypeDef:
        """
        Starts the asynchronous analysis of an input document for relationships between
        detected items such as key-value pairs, tables, and selection elements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.start_document_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#start_document_analysis)
        """
    def start_document_text_detection(
        self,
        *,
        DocumentLocation: "DocumentLocationTypeDef",
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        OutputConfig: "OutputConfigTypeDef" = None,
        KMSKeyId: str = None
    ) -> StartDocumentTextDetectionResponseTypeDef:
        """
        Starts the asynchronous detection of text in a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/textract.html#Textract.Client.start_document_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#start_document_text_detection)
        """
