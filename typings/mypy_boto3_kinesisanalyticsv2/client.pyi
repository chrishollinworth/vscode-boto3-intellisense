# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kinesisanalyticsv2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalyticsv2 import KinesisAnalyticsV2Client

    client: KinesisAnalyticsV2Client = boto3.client("kinesisanalyticsv2")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_kinesisanalyticsv2.paginator import (
    ListApplicationSnapshotsPaginator,
    ListApplicationsPaginator,
)
from mypy_boto3_kinesisanalyticsv2.type_defs import (
    AddApplicationCloudWatchLoggingOptionResponseTypeDef,
    AddApplicationInputProcessingConfigurationResponseTypeDef,
    AddApplicationInputResponseTypeDef,
    AddApplicationOutputResponseTypeDef,
    AddApplicationReferenceDataSourceResponseTypeDef,
    AddApplicationVpcConfigurationResponseTypeDef,
    ApplicationConfigurationTypeDef,
    ApplicationConfigurationUpdateTypeDef,
    CloudWatchLoggingOptionTypeDef,
    CloudWatchLoggingOptionUpdateTypeDef,
    CreateApplicationResponseTypeDef,
    DeleteApplicationCloudWatchLoggingOptionResponseTypeDef,
    DeleteApplicationInputProcessingConfigurationResponseTypeDef,
    DeleteApplicationOutputResponseTypeDef,
    DeleteApplicationReferenceDataSourceResponseTypeDef,
    DeleteApplicationVpcConfigurationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeApplicationSnapshotResponseTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    InputProcessingConfigurationTypeDef,
    InputStartingPositionConfigurationTypeDef,
    InputTypeDef,
    ListApplicationSnapshotsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    ReferenceDataSourceTypeDef,
    RunConfigurationTypeDef,
    RunConfigurationUpdateTypeDef,
    S3ConfigurationTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
    VpcConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisAnalyticsV2Client",)


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
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceProvisionedThroughputExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnableToDetectSchemaException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class KinesisAnalyticsV2Client:
    """
    [KinesisAnalyticsV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef,
    ) -> AddApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        [Client.add_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self, ApplicationName: str, CurrentApplicationVersionId: int, Input: "InputTypeDef"
    ) -> AddApplicationInputResponseTypeDef:
        """
        [Client.add_application_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input)
        """

    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef",
    ) -> AddApplicationInputProcessingConfigurationResponseTypeDef:
        """
        [Client.add_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input_processing_configuration)
        """

    def add_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, Output: "OutputTypeDef"
    ) -> AddApplicationOutputResponseTypeDef:
        """
        [Client.add_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_output)
        """

    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: "ReferenceDataSourceTypeDef",
    ) -> AddApplicationReferenceDataSourceResponseTypeDef:
        """
        [Client.add_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_reference_data_source)
        """

    def add_application_vpc_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        VpcConfiguration: "VpcConfigurationTypeDef",
    ) -> AddApplicationVpcConfigurationResponseTypeDef:
        """
        [Client.add_application_vpc_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_vpc_configuration)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.can_paginate)
        """

    def create_application(
        self,
        ApplicationName: str,
        RuntimeEnvironment: Literal["SQL-1_0", "FLINK-1_6", "FLINK-1_8"],
        ServiceExecutionRole: str,
        ApplicationDescription: str = None,
        ApplicationConfiguration: ApplicationConfigurationTypeDef = None,
        CloudWatchLoggingOptions: List[CloudWatchLoggingOptionTypeDef] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application)
        """

    def create_application_snapshot(
        self, ApplicationName: str, SnapshotName: str
    ) -> Dict[str, Any]:
        """
        [Client.create_application_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application_snapshot)
        """

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str
    ) -> DeleteApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        [Client.delete_application_cloud_watch_logging_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> DeleteApplicationInputProcessingConfigurationResponseTypeDef:
        """
        [Client.delete_application_input_processing_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> DeleteApplicationOutputResponseTypeDef:
        """
        [Client.delete_application_output documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_output)
        """

    def delete_application_reference_data_source(
        self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> DeleteApplicationReferenceDataSourceResponseTypeDef:
        """
        [Client.delete_application_reference_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_reference_data_source)
        """

    def delete_application_snapshot(
        self, ApplicationName: str, SnapshotName: str, SnapshotCreationTimestamp: datetime
    ) -> Dict[str, Any]:
        """
        [Client.delete_application_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_snapshot)
        """

    def delete_application_vpc_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, VpcConfigurationId: str
    ) -> DeleteApplicationVpcConfigurationResponseTypeDef:
        """
        [Client.delete_application_vpc_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_vpc_configuration)
        """

    def describe_application(
        self, ApplicationName: str, IncludeAdditionalDetails: bool = None
    ) -> DescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application)
        """

    def describe_application_snapshot(
        self, ApplicationName: str, SnapshotName: str
    ) -> DescribeApplicationSnapshotResponseTypeDef:
        """
        [Client.describe_application_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application_snapshot)
        """

    def discover_input_schema(
        self,
        ServiceExecutionRole: str,
        ResourceARN: str = None,
        InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
        S3Configuration: S3ConfigurationTypeDef = None,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None,
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        [Client.discover_input_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.discover_input_schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.generate_presigned_url)
        """

    def list_application_snapshots(
        self, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> ListApplicationSnapshotsResponseTypeDef:
        """
        [Client.list_application_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_application_snapshots)
        """

    def list_applications(
        self, Limit: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_applications)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_tags_for_resource)
        """

    def start_application(
        self, ApplicationName: str, RunConfiguration: RunConfigurationTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.start_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.start_application)
        """

    def stop_application(self, ApplicationName: str, Force: bool = None) -> Dict[str, Any]:
        """
        [Client.stop_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.stop_application)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.untag_resource)
        """

    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationConfigurationUpdate: ApplicationConfigurationUpdateTypeDef = None,
        ServiceExecutionRoleUpdate: str = None,
        RunConfigurationUpdate: RunConfigurationUpdateTypeDef = None,
        CloudWatchLoggingOptionUpdates: List[CloudWatchLoggingOptionUpdateTypeDef] = None,
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.update_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_snapshots"]
    ) -> ListApplicationSnapshotsPaginator:
        """
        [Paginator.ListApplicationSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Paginator.ListApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications)
        """
