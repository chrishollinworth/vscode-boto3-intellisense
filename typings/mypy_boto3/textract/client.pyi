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
    AnalyzeIDResponseTypeDef,
    DetectDocumentTextResponseTypeDef,
    DocumentLocationTypeDef,
    DocumentTypeDef,
    GetDocumentAnalysisResponseTypeDef,
    GetDocumentTextDetectionResponseTypeDef,
    GetExpenseAnalysisResponseTypeDef,
    GetLendingAnalysisResponseTypeDef,
    GetLendingAnalysisSummaryResponseTypeDef,
    HumanLoopConfigTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    QueriesConfigTypeDef,
    StartDocumentAnalysisResponseTypeDef,
    StartDocumentTextDetectionResponseTypeDef,
    StartExpenseAnalysisResponseTypeDef,
    StartLendingAnalysisResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client)
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
        HumanLoopConfig: "HumanLoopConfigTypeDef" = None,
        QueriesConfig: "QueriesConfigTypeDef" = None
    ) -> AnalyzeDocumentResponseTypeDef:
        """
        Analyzes an input document for relationships between detected items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.analyze_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#analyze_document)
        """
    def analyze_expense(self, *, Document: "DocumentTypeDef") -> AnalyzeExpenseResponseTypeDef:
        """
        `AnalyzeExpense` synchronously analyzes an input document for financially
        related relationships between text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.analyze_expense)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#analyze_expense)
        """
    def analyze_id(self, *, DocumentPages: List["DocumentTypeDef"]) -> AnalyzeIDResponseTypeDef:
        """
        Analyzes identity documents for relevant information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.analyze_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#analyze_id)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#close)
        """
    def detect_document_text(
        self, *, Document: "DocumentTypeDef"
    ) -> DetectDocumentTextResponseTypeDef:
        """
        Detects text in the input document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.detect_document_text)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#generate_presigned_url)
        """
    def get_document_analysis(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentAnalysisResponseTypeDef:
        """
        Gets the results for an Amazon Textract asynchronous operation that analyzes
        text in a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.get_document_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_document_analysis)
        """
    def get_document_text_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetDocumentTextDetectionResponseTypeDef:
        """
        Gets the results for an Amazon Textract asynchronous operation that detects text
        in a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.get_document_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_document_text_detection)
        """
    def get_expense_analysis(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetExpenseAnalysisResponseTypeDef:
        """
        Gets the results for an Amazon Textract asynchronous operation that analyzes
        invoices and receipts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.get_expense_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_expense_analysis)
        """
    def get_lending_analysis(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetLendingAnalysisResponseTypeDef:
        """
        Gets the results for an Amazon Textract asynchronous operation that analyzes
        text in a lending document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.get_lending_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_lending_analysis)
        """
    def get_lending_analysis_summary(
        self, *, JobId: str
    ) -> GetLendingAnalysisSummaryResponseTypeDef:
        """
        Gets summarized results for the `StartLendingAnalysis` operation, which analyzes
        text in a lending document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.get_lending_analysis_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#get_lending_analysis_summary)
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
        KMSKeyId: str = None,
        QueriesConfig: "QueriesConfigTypeDef" = None
    ) -> StartDocumentAnalysisResponseTypeDef:
        """
        Starts the asynchronous analysis of an input document for relationships between
        detected items such as key-value pairs, tables, and selection elements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.start_document_analysis)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.start_document_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#start_document_text_detection)
        """
    def start_expense_analysis(
        self,
        *,
        DocumentLocation: "DocumentLocationTypeDef",
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        OutputConfig: "OutputConfigTypeDef" = None,
        KMSKeyId: str = None
    ) -> StartExpenseAnalysisResponseTypeDef:
        """
        Starts the asynchronous analysis of invoices or receipts for data like contact
        information, items purchased, and vendor names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.start_expense_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#start_expense_analysis)
        """
    def start_lending_analysis(
        self,
        *,
        DocumentLocation: "DocumentLocationTypeDef",
        ClientRequestToken: str = None,
        JobTag: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        OutputConfig: "OutputConfigTypeDef" = None,
        KMSKeyId: str = None
    ) -> StartLendingAnalysisResponseTypeDef:
        """
        Starts the classification and analysis of an input document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/textract.html#Textract.Client.start_lending_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/client.html#start_lending_analysis)
        """
