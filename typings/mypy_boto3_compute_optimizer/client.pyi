# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for compute-optimizer service client

Usage::

    ```python
    import boto3
    from mypy_boto3_compute_optimizer import ComputeOptimizerClient

    client: ComputeOptimizerClient = boto3.client("compute-optimizer")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_compute_optimizer.type_defs import (
    DescribeRecommendationExportJobsResponseTypeDef,
    ExportAutoScalingGroupRecommendationsResponseTypeDef,
    ExportEC2InstanceRecommendationsResponseTypeDef,
    FilterTypeDef,
    GetAutoScalingGroupRecommendationsResponseTypeDef,
    GetEC2InstanceRecommendationsResponseTypeDef,
    GetEC2RecommendationProjectedMetricsResponseTypeDef,
    GetEnrollmentStatusResponseTypeDef,
    GetRecommendationSummariesResponseTypeDef,
    JobFilterTypeDef,
    S3DestinationConfigTypeDef,
    UpdateEnrollmentStatusResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComputeOptimizerClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    InvalidParameterValueException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    MissingAuthenticationToken: Type[Boto3ClientError]
    OptInRequiredException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]


class ComputeOptimizerClient:
    """
    [ComputeOptimizer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.can_paginate)
        """

    def describe_recommendation_export_jobs(
        self,
        jobIds: List[str] = None,
        filters: List[JobFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeRecommendationExportJobsResponseTypeDef:
        """
        [Client.describe_recommendation_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.describe_recommendation_export_jobs)
        """

    def export_auto_scaling_group_recommendations(
        self,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        fieldsToExport: List[
            Literal[
                "AccountId",
                "AutoScalingGroupArn",
                "AutoScalingGroupName",
                "Finding",
                "UtilizationMetricsCpuMaximum",
                "UtilizationMetricsMemoryMaximum",
                "LookbackPeriodInDays",
                "CurrentConfigurationInstanceType",
                "CurrentConfigurationDesiredCapacity",
                "CurrentConfigurationMinSize",
                "CurrentConfigurationMaxSize",
                "CurrentOnDemandPrice",
                "CurrentStandardOneYearNoUpfrontReservedPrice",
                "CurrentStandardThreeYearNoUpfrontReservedPrice",
                "CurrentVCpus",
                "CurrentMemory",
                "CurrentStorage",
                "CurrentNetwork",
                "RecommendationOptionsConfigurationInstanceType",
                "RecommendationOptionsConfigurationDesiredCapacity",
                "RecommendationOptionsConfigurationMinSize",
                "RecommendationOptionsConfigurationMaxSize",
                "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
                "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
                "RecommendationOptionsPerformanceRisk",
                "RecommendationOptionsOnDemandPrice",
                "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
                "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
                "RecommendationOptionsVcpus",
                "RecommendationOptionsMemory",
                "RecommendationOptionsStorage",
                "RecommendationOptionsNetwork",
                "LastRefreshTimestamp",
            ]
        ] = None,
        fileFormat: Literal["Csv"] = None,
        includeMemberAccounts: bool = None,
    ) -> ExportAutoScalingGroupRecommendationsResponseTypeDef:
        """
        [Client.export_auto_scaling_group_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_auto_scaling_group_recommendations)
        """

    def export_ec2_instance_recommendations(
        self,
        s3DestinationConfig: S3DestinationConfigTypeDef,
        accountIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        fieldsToExport: List[
            Literal[
                "AccountId",
                "InstanceArn",
                "InstanceName",
                "Finding",
                "LookbackPeriodInDays",
                "CurrentInstanceType",
                "UtilizationMetricsCpuMaximum",
                "UtilizationMetricsMemoryMaximum",
                "CurrentOnDemandPrice",
                "CurrentStandardOneYearNoUpfrontReservedPrice",
                "CurrentStandardThreeYearNoUpfrontReservedPrice",
                "CurrentVCpus",
                "CurrentMemory",
                "CurrentStorage",
                "CurrentNetwork",
                "RecommendationOptionsInstanceType",
                "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
                "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
                "RecommendationOptionsPerformanceRisk",
                "RecommendationOptionsVcpus",
                "RecommendationOptionsMemory",
                "RecommendationOptionsStorage",
                "RecommendationOptionsNetwork",
                "RecommendationOptionsOnDemandPrice",
                "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
                "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
                "RecommendationsSourcesRecommendationSourceArn",
                "RecommendationsSourcesRecommendationSourceType",
                "LastRefreshTimestamp",
            ]
        ] = None,
        fileFormat: Literal["Csv"] = None,
        includeMemberAccounts: bool = None,
    ) -> ExportEC2InstanceRecommendationsResponseTypeDef:
        """
        [Client.export_ec2_instance_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ec2_instance_recommendations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.generate_presigned_url)
        """

    def get_auto_scaling_group_recommendations(
        self,
        accountIds: List[str] = None,
        autoScalingGroupArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None,
    ) -> GetAutoScalingGroupRecommendationsResponseTypeDef:
        """
        [Client.get_auto_scaling_group_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_auto_scaling_group_recommendations)
        """

    def get_ec2_instance_recommendations(
        self,
        instanceArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List[FilterTypeDef] = None,
        accountIds: List[str] = None,
    ) -> GetEC2InstanceRecommendationsResponseTypeDef:
        """
        [Client.get_ec2_instance_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_instance_recommendations)
        """

    def get_ec2_recommendation_projected_metrics(
        self,
        instanceArn: str,
        stat: Literal["Maximum", "Average"],
        period: int,
        startTime: datetime,
        endTime: datetime,
    ) -> GetEC2RecommendationProjectedMetricsResponseTypeDef:
        """
        [Client.get_ec2_recommendation_projected_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_recommendation_projected_metrics)
        """

    def get_enrollment_status(self) -> GetEnrollmentStatusResponseTypeDef:
        """
        [Client.get_enrollment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_status)
        """

    def get_recommendation_summaries(
        self, accountIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> GetRecommendationSummariesResponseTypeDef:
        """
        [Client.get_recommendation_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_summaries)
        """

    def update_enrollment_status(
        self,
        status: Literal["Active", "Inactive", "Pending", "Failed"],
        includeMemberAccounts: bool = None,
    ) -> UpdateEnrollmentStatusResponseTypeDef:
        """
        [Client.update_enrollment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/compute-optimizer.html#ComputeOptimizer.Client.update_enrollment_status)
        """
