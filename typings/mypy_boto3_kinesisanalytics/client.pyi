"""
Type annotations for kinesisanalytics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalytics import KinesisAnalyticsClient

    client: KinesisAnalyticsClient = boto3.client("kinesisanalytics")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    ApplicationUpdateTypeDef,
    CloudWatchLoggingOptionTypeDef,
    CreateApplicationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    InputConfigurationTypeDef,
    InputProcessingConfigurationTypeDef,
    InputStartingPositionConfigurationTypeDef,
    InputTypeDef,
    ListApplicationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    ReferenceDataSourceTypeDef,
    S3ConfigurationTypeDef,
    TagTypeDef,
)

__all__ = ("KinesisAnalyticsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    CodeValidationException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidApplicationConfigurationException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceProvisionedThroughputExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnableToDetectSchemaException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class KinesisAnalyticsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisAnalyticsClient exceptions.
        """
    def add_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: "CloudWatchLoggingOptionTypeDef"
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add_application_cloud_watch_logging_option)
        """
    def add_application_input(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, Input: "InputTypeDef"
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add_application_input)
        """
    def add_application_input_processing_configuration(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add_application_input_processing_configuration)
        """
    def add_application_output(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, Output: "OutputTypeDef"
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add_application_output)
        """
    def add_application_reference_data_source(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: "ReferenceDataSourceTypeDef"
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add_application_reference_data_source)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#close)
        """
    def create_application(
        self,
        *,
        ApplicationName: str,
        ApplicationDescription: str = None,
        Inputs: List["InputTypeDef"] = None,
        Outputs: List["OutputTypeDef"] = None,
        CloudWatchLoggingOptions: List["CloudWatchLoggingOptionTypeDef"] = None,
        ApplicationCode: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#create_application)
        """
    def delete_application(
        self, *, ApplicationName: str, CreateTimestamp: Union[datetime, str]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete_application)
        """
    def delete_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOptionId: str
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete_application_cloud_watch_logging_option)
        """
    def delete_application_input_processing_configuration(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete_application_input_processing_configuration)
        """
    def delete_application_output(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete_application_output)
        """
    def delete_application_reference_data_source(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete_application_reference_data_source)
        """
    def describe_application(self, *, ApplicationName: str) -> DescribeApplicationResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#describe_application)
        """
    def discover_input_schema(
        self,
        *,
        ResourceARN: str = None,
        RoleARN: str = None,
        InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
        S3Configuration: "S3ConfigurationTypeDef" = None,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.discover_input_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#discover_input_schema)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#generate_presigned_url)
        """
    def list_applications(
        self, *, Limit: int = None, ExclusiveStartApplicationName: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#list_applications)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of key-value tags assigned to the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#list_tags_for_resource)
        """
    def start_application(
        self, *, ApplicationName: str, InputConfigurations: List["InputConfigurationTypeDef"]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.start_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#start_application)
        """
    def stop_application(self, *, ApplicationName: str) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.stop_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#stop_application)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to a Kinesis Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a Kinesis Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationUpdate: "ApplicationUpdateTypeDef"
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#update_application)
        """
