# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kinesisanalytics service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalytics import KinesisAnalyticsClient

    client: KinesisAnalyticsClient = boto3.client("kinesisanalytics")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_kinesisanalytics.type_defs import (
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


class KinesisAnalyticsClient:
    """
    [KinesisAnalytics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self, ApplicationName: str, CurrentApplicationVersionId: int, Input: InputTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.add_application_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input)
        """

    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef",
    ) -> Dict[str, Any]:
        """
        [Client.add_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input_processing_configuration)
        """

    def add_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, Output: OutputTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.add_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_output)
        """

    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: ReferenceDataSourceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.add_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_reference_data_source)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.can_paginate)
        """

    def create_application(
        self,
        ApplicationName: str,
        ApplicationDescription: str = None,
        Inputs: List[InputTypeDef] = None,
        Outputs: List[OutputTypeDef] = None,
        CloudWatchLoggingOptions: List[CloudWatchLoggingOptionTypeDef] = None,
        ApplicationCode: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.create_application)
        """

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_output)
        """

    def delete_application_reference_data_source(
        self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_reference_data_source)
        """

    def describe_application(self, ApplicationName: str) -> DescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.describe_application)
        """

    def discover_input_schema(
        self,
        ResourceARN: str = None,
        RoleARN: str = None,
        InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
        S3Configuration: S3ConfigurationTypeDef = None,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None,
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        [Client.discover_input_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.discover_input_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.generate_presigned_url)
        """

    def list_applications(
        self, Limit: int = None, ExclusiveStartApplicationName: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_applications)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_tags_for_resource)
        """

    def start_application(
        self, ApplicationName: str, InputConfigurations: List[InputConfigurationTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.start_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.start_application)
        """

    def stop_application(self, ApplicationName: str) -> Dict[str, Any]:
        """
        [Client.stop_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.stop_application)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.untag_resource)
        """

    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationUpdate: ApplicationUpdateTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.update_application)
        """
