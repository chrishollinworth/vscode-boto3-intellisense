"""
Type annotations for kinesisanalyticsv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalyticsv2 import KinesisAnalyticsV2Client

    client: KinesisAnalyticsV2Client = boto3.client("kinesisanalyticsv2")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ApplicationModeType, RuntimeEnvironmentType, UrlTypeType
from .paginator import ListApplicationSnapshotsPaginator, ListApplicationsPaginator
from .type_defs import (
    AddApplicationCloudWatchLoggingOptionResponseTypeDef,
    AddApplicationInputProcessingConfigurationResponseTypeDef,
    AddApplicationInputResponseTypeDef,
    AddApplicationOutputResponseTypeDef,
    AddApplicationReferenceDataSourceResponseTypeDef,
    AddApplicationVpcConfigurationResponseTypeDef,
    ApplicationConfigurationTypeDef,
    ApplicationConfigurationUpdateTypeDef,
    ApplicationMaintenanceConfigurationUpdateTypeDef,
    CloudWatchLoggingOptionTypeDef,
    CloudWatchLoggingOptionUpdateTypeDef,
    CreateApplicationPresignedUrlResponseTypeDef,
    CreateApplicationResponseTypeDef,
    DeleteApplicationCloudWatchLoggingOptionResponseTypeDef,
    DeleteApplicationInputProcessingConfigurationResponseTypeDef,
    DeleteApplicationOutputResponseTypeDef,
    DeleteApplicationReferenceDataSourceResponseTypeDef,
    DeleteApplicationVpcConfigurationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeApplicationSnapshotResponseTypeDef,
    DescribeApplicationVersionResponseTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    InputProcessingConfigurationTypeDef,
    InputStartingPositionConfigurationTypeDef,
    InputTypeDef,
    ListApplicationSnapshotsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    ReferenceDataSourceTypeDef,
    RollbackApplicationResponseTypeDef,
    RunConfigurationTypeDef,
    RunConfigurationUpdateTypeDef,
    S3ConfigurationTypeDef,
    TagTypeDef,
    UpdateApplicationMaintenanceConfigurationResponseTypeDef,
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

class KinesisAnalyticsV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisAnalyticsV2Client exceptions.
        """
    def add_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOption: "CloudWatchLoggingOptionTypeDef",
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> AddApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        Adds an Amazon CloudWatch log stream to monitor application configuration
        errors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_cloud_watch_logging_option)
        """
    def add_application_input(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, Input: "InputTypeDef"
    ) -> AddApplicationInputResponseTypeDef:
        """
        Adds a streaming source to your SQL-based Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_input)
        """
    def add_application_input_processing_configuration(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef"
    ) -> AddApplicationInputProcessingConfigurationResponseTypeDef:
        """
        Adds an  InputProcessingConfiguration to a SQL-based Kinesis Data Analytics
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_input_processing_configuration)
        """
    def add_application_output(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, Output: "OutputTypeDef"
    ) -> AddApplicationOutputResponseTypeDef:
        """
        Adds an external destination to your SQL-based Kinesis Data Analytics
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_output)
        """
    def add_application_reference_data_source(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: "ReferenceDataSourceTypeDef"
    ) -> AddApplicationReferenceDataSourceResponseTypeDef:
        """
        Adds a reference data source to an existing SQL-based Kinesis Data Analytics
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_reference_data_source)
        """
    def add_application_vpc_configuration(
        self,
        *,
        ApplicationName: str,
        VpcConfiguration: "VpcConfigurationTypeDef",
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> AddApplicationVpcConfigurationResponseTypeDef:
        """
        Adds a Virtual Private Cloud (VPC) configuration to the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.add_application_vpc_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#add_application_vpc_configuration)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#close)
        """
    def create_application(
        self,
        *,
        ApplicationName: str,
        RuntimeEnvironment: RuntimeEnvironmentType,
        ServiceExecutionRole: str,
        ApplicationDescription: str = None,
        ApplicationConfiguration: "ApplicationConfigurationTypeDef" = None,
        CloudWatchLoggingOptions: List["CloudWatchLoggingOptionTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        ApplicationMode: ApplicationModeType = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates a Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#create_application)
        """
    def create_application_presigned_url(
        self,
        *,
        ApplicationName: str,
        UrlType: UrlTypeType,
        SessionExpirationDurationInSeconds: int = None
    ) -> CreateApplicationPresignedUrlResponseTypeDef:
        """
        Creates and returns a URL that you can use to connect to an application's
        extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#create_application_presigned_url)
        """
    def create_application_snapshot(
        self, *, ApplicationName: str, SnapshotName: str
    ) -> Dict[str, Any]:
        """
        Creates a snapshot of the application's state data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.create_application_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#create_application_snapshot)
        """
    def delete_application(
        self, *, ApplicationName: str, CreateTimestamp: Union[datetime, str]
    ) -> Dict[str, Any]:
        """
        Deletes the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application)
        """
    def delete_application_cloud_watch_logging_option(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOptionId: str,
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> DeleteApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        Deletes an Amazon CloudWatch log stream from an Kinesis Data Analytics
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_cloud_watch_logging_option)
        """
    def delete_application_input_processing_configuration(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> DeleteApplicationInputProcessingConfigurationResponseTypeDef:
        """
        Deletes an  InputProcessingConfiguration from an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_input_processing_configuration)
        """
    def delete_application_output(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> DeleteApplicationOutputResponseTypeDef:
        """
        Deletes the output destination configuration from your SQL-based Kinesis Data
        Analytics application's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_output)
        """
    def delete_application_reference_data_source(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> DeleteApplicationReferenceDataSourceResponseTypeDef:
        """
        Deletes a reference data source configuration from the specified SQL-based
        Kinesis Data Analytics application's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_reference_data_source)
        """
    def delete_application_snapshot(
        self,
        *,
        ApplicationName: str,
        SnapshotName: str,
        SnapshotCreationTimestamp: Union[datetime, str]
    ) -> Dict[str, Any]:
        """
        Deletes a snapshot of application state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_snapshot)
        """
    def delete_application_vpc_configuration(
        self,
        *,
        ApplicationName: str,
        VpcConfigurationId: str,
        CurrentApplicationVersionId: int = None,
        ConditionalToken: str = None
    ) -> DeleteApplicationVpcConfigurationResponseTypeDef:
        """
        Removes a VPC configuration from a Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.delete_application_vpc_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#delete_application_vpc_configuration)
        """
    def describe_application(
        self, *, ApplicationName: str, IncludeAdditionalDetails: bool = None
    ) -> DescribeApplicationResponseTypeDef:
        """
        Returns information about a specific Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#describe_application)
        """
    def describe_application_snapshot(
        self, *, ApplicationName: str, SnapshotName: str
    ) -> DescribeApplicationSnapshotResponseTypeDef:
        """
        Returns information about a snapshot of application state data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#describe_application_snapshot)
        """
    def describe_application_version(
        self, *, ApplicationName: str, ApplicationVersionId: int
    ) -> DescribeApplicationVersionResponseTypeDef:
        """
        Provides a detailed description of a specified version of the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.describe_application_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#describe_application_version)
        """
    def discover_input_schema(
        self,
        *,
        ServiceExecutionRole: str,
        ResourceARN: str = None,
        InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
        S3Configuration: "S3ConfigurationTypeDef" = None,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        Infers a schema for a SQL-based Kinesis Data Analytics application by evaluating
        sample records on the specified streaming source (Kinesis data stream or Kinesis
        Data Firehose delivery stream) or Amazon S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.discover_input_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#discover_input_schema)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#generate_presigned_url)
        """
    def list_application_snapshots(
        self, *, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> ListApplicationSnapshotsResponseTypeDef:
        """
        Lists information about the current application snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_application_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_application_snapshots)
        """
    def list_application_versions(
        self, *, ApplicationName: str, Limit: int = None, NextToken: str = None
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        Lists all the versions for the specified application, including versions that
        were rolled back.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_application_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_application_versions)
        """
    def list_applications(
        self, *, Limit: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Returns a list of Kinesis Data Analytics applications in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_applications)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of key-value tags assigned to the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#list_tags_for_resource)
        """
    def rollback_application(
        self, *, ApplicationName: str, CurrentApplicationVersionId: int
    ) -> RollbackApplicationResponseTypeDef:
        """
        Reverts the application to the previous running version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.rollback_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#rollback_application)
        """
    def start_application(
        self, *, ApplicationName: str, RunConfiguration: "RunConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Starts the specified Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.start_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#start_application)
        """
    def stop_application(self, *, ApplicationName: str, Force: bool = None) -> Dict[str, Any]:
        """
        Stops the application from processing data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.stop_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#stop_application)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to a Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        ApplicationName: str,
        CurrentApplicationVersionId: int = None,
        ApplicationConfigurationUpdate: "ApplicationConfigurationUpdateTypeDef" = None,
        ServiceExecutionRoleUpdate: str = None,
        RunConfigurationUpdate: "RunConfigurationUpdateTypeDef" = None,
        CloudWatchLoggingOptionUpdates: List["CloudWatchLoggingOptionUpdateTypeDef"] = None,
        ConditionalToken: str = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates an existing Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#update_application)
        """
    def update_application_maintenance_configuration(
        self,
        *,
        ApplicationName: str,
        ApplicationMaintenanceConfigurationUpdate: "ApplicationMaintenanceConfigurationUpdateTypeDef"
    ) -> UpdateApplicationMaintenanceConfigurationResponseTypeDef:
        """
        Updates the maintenance configuration of the Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client.update_application_maintenance_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client.html#update_application_maintenance_configuration)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_snapshots"]
    ) -> ListApplicationSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationsnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationspaginator)
        """
