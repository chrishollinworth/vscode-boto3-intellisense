"""
Type annotations for kinesisanalyticsv2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kinesisanalyticsv2.client import KinesisAnalyticsV2Client

    session = Session()
    client: KinesisAnalyticsV2Client = session.client("kinesisanalyticsv2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationOperationsPaginator,
    ListApplicationSnapshotsPaginator,
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
)
from .type_defs import (
    AddApplicationCloudWatchLoggingOptionRequestTypeDef,
    AddApplicationCloudWatchLoggingOptionResponseTypeDef,
    AddApplicationInputProcessingConfigurationRequestTypeDef,
    AddApplicationInputProcessingConfigurationResponseTypeDef,
    AddApplicationInputRequestTypeDef,
    AddApplicationInputResponseTypeDef,
    AddApplicationOutputRequestTypeDef,
    AddApplicationOutputResponseTypeDef,
    AddApplicationReferenceDataSourceRequestTypeDef,
    AddApplicationReferenceDataSourceResponseTypeDef,
    AddApplicationVpcConfigurationRequestTypeDef,
    AddApplicationVpcConfigurationResponseTypeDef,
    CreateApplicationPresignedUrlRequestTypeDef,
    CreateApplicationPresignedUrlResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateApplicationSnapshotRequestTypeDef,
    DeleteApplicationCloudWatchLoggingOptionRequestTypeDef,
    DeleteApplicationCloudWatchLoggingOptionResponseTypeDef,
    DeleteApplicationInputProcessingConfigurationRequestTypeDef,
    DeleteApplicationInputProcessingConfigurationResponseTypeDef,
    DeleteApplicationOutputRequestTypeDef,
    DeleteApplicationOutputResponseTypeDef,
    DeleteApplicationReferenceDataSourceRequestTypeDef,
    DeleteApplicationReferenceDataSourceResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteApplicationSnapshotRequestTypeDef,
    DeleteApplicationVpcConfigurationRequestTypeDef,
    DeleteApplicationVpcConfigurationResponseTypeDef,
    DescribeApplicationOperationRequestTypeDef,
    DescribeApplicationOperationResponseTypeDef,
    DescribeApplicationRequestTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeApplicationSnapshotRequestTypeDef,
    DescribeApplicationSnapshotResponseTypeDef,
    DescribeApplicationVersionRequestTypeDef,
    DescribeApplicationVersionResponseTypeDef,
    DiscoverInputSchemaRequestTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    ListApplicationOperationsRequestTypeDef,
    ListApplicationOperationsResponseTypeDef,
    ListApplicationSnapshotsRequestTypeDef,
    ListApplicationSnapshotsResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsRequestTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RollbackApplicationRequestTypeDef,
    RollbackApplicationResponseTypeDef,
    StartApplicationRequestTypeDef,
    StartApplicationResponseTypeDef,
    StopApplicationRequestTypeDef,
    StopApplicationResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationMaintenanceConfigurationRequestTypeDef,
    UpdateApplicationMaintenanceConfigurationResponseTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("KinesisAnalyticsV2Client",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisAnalyticsV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#generate_presigned_url)
        """

    def add_application_cloud_watch_logging_option(
        self, **kwargs: Unpack[AddApplicationCloudWatchLoggingOptionRequestTypeDef]
    ) -> AddApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        Adds an Amazon CloudWatch log stream to monitor application configuration
        errors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/add_application_cloud_watch_logging_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self, **kwargs: Unpack[AddApplicationInputRequestTypeDef]
    ) -> AddApplicationInputResponseTypeDef:
        """
        Adds a streaming source to your SQL-based Kinesis Data Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/add_application_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#add_application_input)
        """

    def add_application_input_processing_configuration(
        self, **kwargs: Unpack[AddApplicationInputProcessingConfigurationRequestTypeDef]
    ) -> AddApplicationInputProcessingConfigurationResponseTypeDef:
        """
        Adds an <a>InputProcessingConfiguration</a> to a SQL-based Kinesis Data
        Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/add_application_input_processing_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#add_application_input_processing_configuration)
        """

    def add_application_output(
        self, **kwargs: Unpack[AddApplicationOutputRequestTypeDef]
    ) -> AddApplicationOutputResponseTypeDef:
        """
        Adds an external destination to your SQL-based Kinesis Data Analytics
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/add_application_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#add_application_output)
        """

    def add_application_reference_data_source(
        self, **kwargs: Unpack[AddApplicationReferenceDataSourceRequestTypeDef]
    ) -> AddApplicationReferenceDataSourceResponseTypeDef:
        """
        Adds a reference data source to an existing SQL-based Kinesis Data Analytics
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/add_application_reference_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#add_application_reference_data_source)
        """

    def add_application_vpc_configuration(
        self, **kwargs: Unpack[AddApplicationVpcConfigurationRequestTypeDef]
    ) -> AddApplicationVpcConfigurationResponseTypeDef:
        """
        Adds a Virtual Private Cloud (VPC) configuration to the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/add_application_vpc_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#add_application_vpc_configuration)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates a Managed Service for Apache Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#create_application)
        """

    def create_application_presigned_url(
        self, **kwargs: Unpack[CreateApplicationPresignedUrlRequestTypeDef]
    ) -> CreateApplicationPresignedUrlResponseTypeDef:
        """
        Creates and returns a URL that you can use to connect to an application's
        extension.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/create_application_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#create_application_presigned_url)
        """

    def create_application_snapshot(
        self, **kwargs: Unpack[CreateApplicationSnapshotRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a snapshot of the application's state data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/create_application_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#create_application_snapshot)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self, **kwargs: Unpack[DeleteApplicationCloudWatchLoggingOptionRequestTypeDef]
    ) -> DeleteApplicationCloudWatchLoggingOptionResponseTypeDef:
        """
        Deletes an Amazon CloudWatch log stream from an SQL-based Kinesis Data
        Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application_cloud_watch_logging_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, **kwargs: Unpack[DeleteApplicationInputProcessingConfigurationRequestTypeDef]
    ) -> DeleteApplicationInputProcessingConfigurationResponseTypeDef:
        """
        Deletes an <a>InputProcessingConfiguration</a> from an input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application_input_processing_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, **kwargs: Unpack[DeleteApplicationOutputRequestTypeDef]
    ) -> DeleteApplicationOutputResponseTypeDef:
        """
        Deletes the output destination configuration from your SQL-based Kinesis Data
        Analytics application's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application_output)
        """

    def delete_application_reference_data_source(
        self, **kwargs: Unpack[DeleteApplicationReferenceDataSourceRequestTypeDef]
    ) -> DeleteApplicationReferenceDataSourceResponseTypeDef:
        """
        Deletes a reference data source configuration from the specified SQL-based
        Kinesis Data Analytics application's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application_reference_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application_reference_data_source)
        """

    def delete_application_snapshot(
        self, **kwargs: Unpack[DeleteApplicationSnapshotRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a snapshot of application state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application_snapshot)
        """

    def delete_application_vpc_configuration(
        self, **kwargs: Unpack[DeleteApplicationVpcConfigurationRequestTypeDef]
    ) -> DeleteApplicationVpcConfigurationResponseTypeDef:
        """
        Removes a VPC configuration from a Managed Service for Apache Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/delete_application_vpc_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#delete_application_vpc_configuration)
        """

    def describe_application(
        self, **kwargs: Unpack[DescribeApplicationRequestTypeDef]
    ) -> DescribeApplicationResponseTypeDef:
        """
        Returns information about a specific Managed Service for Apache Flink
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/describe_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#describe_application)
        """

    def describe_application_operation(
        self, **kwargs: Unpack[DescribeApplicationOperationRequestTypeDef]
    ) -> DescribeApplicationOperationResponseTypeDef:
        """
        Returns information about a specific operation performed on a Managed Service
        for Apache Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/describe_application_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#describe_application_operation)
        """

    def describe_application_snapshot(
        self, **kwargs: Unpack[DescribeApplicationSnapshotRequestTypeDef]
    ) -> DescribeApplicationSnapshotResponseTypeDef:
        """
        Returns information about a snapshot of application state data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/describe_application_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#describe_application_snapshot)
        """

    def describe_application_version(
        self, **kwargs: Unpack[DescribeApplicationVersionRequestTypeDef]
    ) -> DescribeApplicationVersionResponseTypeDef:
        """
        Provides a detailed description of a specified version of the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/describe_application_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#describe_application_version)
        """

    def discover_input_schema(
        self, **kwargs: Unpack[DiscoverInputSchemaRequestTypeDef]
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        Infers a schema for a SQL-based Kinesis Data Analytics application by
        evaluating sample records on the specified streaming source (Kinesis data
        stream or Kinesis Data Firehose delivery stream) or Amazon S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/discover_input_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#discover_input_schema)
        """

    def list_application_operations(
        self, **kwargs: Unpack[ListApplicationOperationsRequestTypeDef]
    ) -> ListApplicationOperationsResponseTypeDef:
        """
        Lists information about operations performed on a Managed Service for Apache
        Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/list_application_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#list_application_operations)
        """

    def list_application_snapshots(
        self, **kwargs: Unpack[ListApplicationSnapshotsRequestTypeDef]
    ) -> ListApplicationSnapshotsResponseTypeDef:
        """
        Lists information about the current application snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/list_application_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#list_application_snapshots)
        """

    def list_application_versions(
        self, **kwargs: Unpack[ListApplicationVersionsRequestTypeDef]
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        Lists all the versions for the specified application, including versions that
        were rolled back.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/list_application_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#list_application_versions)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Returns a list of Managed Service for Apache Flink applications in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#list_applications)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of key-value tags assigned to the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#list_tags_for_resource)
        """

    def rollback_application(
        self, **kwargs: Unpack[RollbackApplicationRequestTypeDef]
    ) -> RollbackApplicationResponseTypeDef:
        """
        Reverts the application to the previous running version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/rollback_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#rollback_application)
        """

    def start_application(
        self, **kwargs: Unpack[StartApplicationRequestTypeDef]
    ) -> StartApplicationResponseTypeDef:
        """
        Starts the specified Managed Service for Apache Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/start_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#start_application)
        """

    def stop_application(
        self, **kwargs: Unpack[StopApplicationRequestTypeDef]
    ) -> StopApplicationResponseTypeDef:
        """
        Stops the application from processing data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/stop_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#stop_application)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to a Managed Service for Apache Flink
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a Managed Service for Apache Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates an existing Managed Service for Apache Flink application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#update_application)
        """

    def update_application_maintenance_configuration(
        self, **kwargs: Unpack[UpdateApplicationMaintenanceConfigurationRequestTypeDef]
    ) -> UpdateApplicationMaintenanceConfigurationResponseTypeDef:
        """
        Updates the maintenance configuration of the Managed Service for Apache Flink
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/update_application_maintenance_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#update_application_maintenance_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_operations"]
    ) -> ListApplicationOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_snapshots"]
    ) -> ListApplicationSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_application_versions"]
    ) -> ListApplicationVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/client/#get_paginator)
        """
