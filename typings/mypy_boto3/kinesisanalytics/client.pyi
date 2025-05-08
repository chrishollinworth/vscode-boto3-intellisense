"""
Type annotations for kinesisanalytics service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kinesisanalytics.client import KinesisAnalyticsClient

    session = Session()
    client: KinesisAnalyticsClient = session.client("kinesisanalytics")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AddApplicationCloudWatchLoggingOptionRequestTypeDef,
    AddApplicationInputProcessingConfigurationRequestTypeDef,
    AddApplicationInputRequestTypeDef,
    AddApplicationOutputRequestTypeDef,
    AddApplicationReferenceDataSourceRequestTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    DeleteApplicationCloudWatchLoggingOptionRequestTypeDef,
    DeleteApplicationInputProcessingConfigurationRequestTypeDef,
    DeleteApplicationOutputRequestTypeDef,
    DeleteApplicationReferenceDataSourceRequestTypeDef,
    DeleteApplicationRequestTypeDef,
    DescribeApplicationRequestTypeDef,
    DescribeApplicationResponseTypeDef,
    DiscoverInputSchemaRequestTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartApplicationRequestTypeDef,
    StopApplicationRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("KinesisAnalyticsClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisAnalyticsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics.html#KinesisAnalytics.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#generate_presigned_url)
        """

    def add_application_cloud_watch_logging_option(
        self, **kwargs: Unpack[AddApplicationCloudWatchLoggingOptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/add_application_cloud_watch_logging_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#add_application_cloud_watch_logging_option)
        """

    def add_application_input(
        self, **kwargs: Unpack[AddApplicationInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/add_application_input.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#add_application_input)
        """

    def add_application_input_processing_configuration(
        self, **kwargs: Unpack[AddApplicationInputProcessingConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/add_application_input_processing_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#add_application_input_processing_configuration)
        """

    def add_application_output(
        self, **kwargs: Unpack[AddApplicationOutputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/add_application_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#add_application_output)
        """

    def add_application_reference_data_source(
        self, **kwargs: Unpack[AddApplicationReferenceDataSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/add_application_reference_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#add_application_reference_data_source)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#create_application)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#delete_application)
        """

    def delete_application_cloud_watch_logging_option(
        self, **kwargs: Unpack[DeleteApplicationCloudWatchLoggingOptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/delete_application_cloud_watch_logging_option.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#delete_application_cloud_watch_logging_option)
        """

    def delete_application_input_processing_configuration(
        self, **kwargs: Unpack[DeleteApplicationInputProcessingConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/delete_application_input_processing_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#delete_application_input_processing_configuration)
        """

    def delete_application_output(
        self, **kwargs: Unpack[DeleteApplicationOutputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/delete_application_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#delete_application_output)
        """

    def delete_application_reference_data_source(
        self, **kwargs: Unpack[DeleteApplicationReferenceDataSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/delete_application_reference_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#delete_application_reference_data_source)
        """

    def describe_application(
        self, **kwargs: Unpack[DescribeApplicationRequestTypeDef]
    ) -> DescribeApplicationResponseTypeDef:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/describe_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#describe_application)
        """

    def discover_input_schema(
        self, **kwargs: Unpack[DiscoverInputSchemaRequestTypeDef]
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/discover_input_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#discover_input_schema)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#list_applications)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of key-value tags assigned to the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#list_tags_for_resource)
        """

    def start_application(self, **kwargs: Unpack[StartApplicationRequestTypeDef]) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/start_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#start_application)
        """

    def stop_application(self, **kwargs: Unpack[StopApplicationRequestTypeDef]) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/stop_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#stop_application)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to a Kinesis Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a Kinesis Analytics application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This documentation is for version 1 of the Amazon Kinesis Data Analytics API,
        which only supports SQL applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalytics/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client/#update_application)
        """
