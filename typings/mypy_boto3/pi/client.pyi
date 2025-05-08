"""
Type annotations for pi service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pi.client import PIClient

    session = Session()
    client: PIClient = session.client("pi")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreatePerformanceAnalysisReportRequestTypeDef,
    CreatePerformanceAnalysisReportResponseTypeDef,
    DeletePerformanceAnalysisReportRequestTypeDef,
    DescribeDimensionKeysRequestTypeDef,
    DescribeDimensionKeysResponseTypeDef,
    GetDimensionKeyDetailsRequestTypeDef,
    GetDimensionKeyDetailsResponseTypeDef,
    GetPerformanceAnalysisReportRequestTypeDef,
    GetPerformanceAnalysisReportResponseTypeDef,
    GetResourceMetadataRequestTypeDef,
    GetResourceMetadataResponseTypeDef,
    GetResourceMetricsRequestTypeDef,
    GetResourceMetricsResponseTypeDef,
    ListAvailableResourceDimensionsRequestTypeDef,
    ListAvailableResourceDimensionsResponseTypeDef,
    ListAvailableResourceMetricsRequestTypeDef,
    ListAvailableResourceMetricsResponseTypeDef,
    ListPerformanceAnalysisReportsRequestTypeDef,
    ListPerformanceAnalysisReportsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
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

__all__ = ("PIClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]

class PIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi.html#PI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#generate_presigned_url)
        """

    def create_performance_analysis_report(
        self, **kwargs: Unpack[CreatePerformanceAnalysisReportRequestTypeDef]
    ) -> CreatePerformanceAnalysisReportResponseTypeDef:
        """
        Creates a new performance analysis report for a specific time period for the DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/create_performance_analysis_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#create_performance_analysis_report)
        """

    def delete_performance_analysis_report(
        self, **kwargs: Unpack[DeletePerformanceAnalysisReportRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a performance analysis report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/delete_performance_analysis_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#delete_performance_analysis_report)
        """

    def describe_dimension_keys(
        self, **kwargs: Unpack[DescribeDimensionKeysRequestTypeDef]
    ) -> DescribeDimensionKeysResponseTypeDef:
        """
        For a specific time period, retrieve the top <code>N</code> dimension keys for
        a metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/describe_dimension_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#describe_dimension_keys)
        """

    def get_dimension_key_details(
        self, **kwargs: Unpack[GetDimensionKeyDetailsRequestTypeDef]
    ) -> GetDimensionKeyDetailsResponseTypeDef:
        """
        Get the attributes of the specified dimension group for a DB instance or data
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/get_dimension_key_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#get_dimension_key_details)
        """

    def get_performance_analysis_report(
        self, **kwargs: Unpack[GetPerformanceAnalysisReportRequestTypeDef]
    ) -> GetPerformanceAnalysisReportResponseTypeDef:
        """
        Retrieves the report including the report ID, status, time details, and the
        insights with recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/get_performance_analysis_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#get_performance_analysis_report)
        """

    def get_resource_metadata(
        self, **kwargs: Unpack[GetResourceMetadataRequestTypeDef]
    ) -> GetResourceMetadataResponseTypeDef:
        """
        Retrieve the metadata for different features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/get_resource_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#get_resource_metadata)
        """

    def get_resource_metrics(
        self, **kwargs: Unpack[GetResourceMetricsRequestTypeDef]
    ) -> GetResourceMetricsResponseTypeDef:
        """
        Retrieve Performance Insights metrics for a set of data sources over a time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/get_resource_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#get_resource_metrics)
        """

    def list_available_resource_dimensions(
        self, **kwargs: Unpack[ListAvailableResourceDimensionsRequestTypeDef]
    ) -> ListAvailableResourceDimensionsResponseTypeDef:
        """
        Retrieve the dimensions that can be queried for each specified metric type on a
        specified DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/list_available_resource_dimensions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#list_available_resource_dimensions)
        """

    def list_available_resource_metrics(
        self, **kwargs: Unpack[ListAvailableResourceMetricsRequestTypeDef]
    ) -> ListAvailableResourceMetricsResponseTypeDef:
        """
        Retrieve metrics of the specified types that can be queried for a specified DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/list_available_resource_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#list_available_resource_metrics)
        """

    def list_performance_analysis_reports(
        self, **kwargs: Unpack[ListPerformanceAnalysisReportsRequestTypeDef]
    ) -> ListPerformanceAnalysisReportsResponseTypeDef:
        """
        Lists all the analysis reports created for the DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/list_performance_analysis_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#list_performance_analysis_reports)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves all the metadata tags associated with Amazon RDS Performance Insights
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds metadata tags to the Amazon RDS Performance Insights resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the metadata tags from the Amazon RDS Performance Insights resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pi/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/client/#untag_resource)
        """
