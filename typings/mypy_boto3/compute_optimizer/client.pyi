"""
Type annotations for compute-optimizer service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_compute_optimizer import ComputeOptimizerClient

    client: ComputeOptimizerClient = boto3.client("compute-optimizer")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    EnhancedInfrastructureMetricsType,
    ExportableAutoScalingGroupFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableVolumeFieldType,
    InferredWorkloadTypesPreferenceType,
    MetricStatisticType,
    RecommendationPreferenceNameType,
    ResourceTypeType,
    StatusType,
)
from .type_defs import (
    DescribeRecommendationExportJobsResponseTypeDef,
    EBSFilterTypeDef,
    EnrollmentFilterTypeDef,
    ExportAutoScalingGroupRecommendationsResponseTypeDef,
    ExportEBSVolumeRecommendationsResponseTypeDef,
    ExportEC2InstanceRecommendationsResponseTypeDef,
    ExportLambdaFunctionRecommendationsResponseTypeDef,
    FilterTypeDef,
    GetAutoScalingGroupRecommendationsResponseTypeDef,
    GetEBSVolumeRecommendationsResponseTypeDef,
    GetEC2InstanceRecommendationsResponseTypeDef,
    GetEC2RecommendationProjectedMetricsResponseTypeDef,
    GetEffectiveRecommendationPreferencesResponseTypeDef,
    GetEnrollmentStatusesForOrganizationResponseTypeDef,
    GetEnrollmentStatusResponseTypeDef,
    GetLambdaFunctionRecommendationsResponseTypeDef,
    GetRecommendationPreferencesResponseTypeDef,
    GetRecommendationSummariesResponseTypeDef,
    JobFilterTypeDef,
    LambdaFunctionRecommendationFilterTypeDef,
    RecommendationPreferencesTypeDef,
    S3DestinationConfigTypeDef,
    ScopeTypeDef,
    UpdateEnrollmentStatusResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ComputeOptimizerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingAuthenticationToken: Type[BotocoreClientError]
    OptInRequiredException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class ComputeOptimizerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ComputeOptimizerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#close)
        """
    def delete_recommendation_preferences(
        self,
        *,
        resourceType: ResourceTypeType,
        recommendationPreferenceNames: List[RecommendationPreferenceNameType],
        scope: "ScopeTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Deletes a recommendation preference, such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.delete_recommendation_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#delete_recommendation_preferences)
        """
    def describe_recommendation_export_jobs(
        self,
        *,
        jobIds: List[str] = None,
        filters: List["JobFilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeRecommendationExportJobsResponseTypeDef:
        """
        Describes recommendation export jobs created in the last seven days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.describe_recommendation_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#describe_recommendation_export_jobs)
        """
    def export_auto_scaling_group_recommendations(
        self,
        *,
        s3DestinationConfig: "S3DestinationConfigTypeDef",
        accountIds: List[str] = None,
        filters: List["FilterTypeDef"] = None,
        fieldsToExport: List[ExportableAutoScalingGroupFieldType] = None,
        fileFormat: Literal["Csv"] = None,
        includeMemberAccounts: bool = None,
        recommendationPreferences: "RecommendationPreferencesTypeDef" = None
    ) -> ExportAutoScalingGroupRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Auto Scaling groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_auto_scaling_group_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#export_auto_scaling_group_recommendations)
        """
    def export_ebs_volume_recommendations(
        self,
        *,
        s3DestinationConfig: "S3DestinationConfigTypeDef",
        accountIds: List[str] = None,
        filters: List["EBSFilterTypeDef"] = None,
        fieldsToExport: List[ExportableVolumeFieldType] = None,
        fileFormat: Literal["Csv"] = None,
        includeMemberAccounts: bool = None
    ) -> ExportEBSVolumeRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon EBS volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ebs_volume_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#export_ebs_volume_recommendations)
        """
    def export_ec2_instance_recommendations(
        self,
        *,
        s3DestinationConfig: "S3DestinationConfigTypeDef",
        accountIds: List[str] = None,
        filters: List["FilterTypeDef"] = None,
        fieldsToExport: List[ExportableInstanceFieldType] = None,
        fileFormat: Literal["Csv"] = None,
        includeMemberAccounts: bool = None,
        recommendationPreferences: "RecommendationPreferencesTypeDef" = None
    ) -> ExportEC2InstanceRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Amazon EC2 instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_ec2_instance_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#export_ec2_instance_recommendations)
        """
    def export_lambda_function_recommendations(
        self,
        *,
        s3DestinationConfig: "S3DestinationConfigTypeDef",
        accountIds: List[str] = None,
        filters: List["LambdaFunctionRecommendationFilterTypeDef"] = None,
        fieldsToExport: List[ExportableLambdaFunctionFieldType] = None,
        fileFormat: Literal["Csv"] = None,
        includeMemberAccounts: bool = None
    ) -> ExportLambdaFunctionRecommendationsResponseTypeDef:
        """
        Exports optimization recommendations for Lambda functions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.export_lambda_function_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#export_lambda_function_recommendations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#generate_presigned_url)
        """
    def get_auto_scaling_group_recommendations(
        self,
        *,
        accountIds: List[str] = None,
        autoScalingGroupArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List["FilterTypeDef"] = None,
        recommendationPreferences: "RecommendationPreferencesTypeDef" = None
    ) -> GetAutoScalingGroupRecommendationsResponseTypeDef:
        """
        Returns Auto Scaling group recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_auto_scaling_group_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_auto_scaling_group_recommendations)
        """
    def get_ebs_volume_recommendations(
        self,
        *,
        volumeArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List["EBSFilterTypeDef"] = None,
        accountIds: List[str] = None
    ) -> GetEBSVolumeRecommendationsResponseTypeDef:
        """
        Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ebs_volume_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_ebs_volume_recommendations)
        """
    def get_ec2_instance_recommendations(
        self,
        *,
        instanceArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        filters: List["FilterTypeDef"] = None,
        accountIds: List[str] = None,
        recommendationPreferences: "RecommendationPreferencesTypeDef" = None
    ) -> GetEC2InstanceRecommendationsResponseTypeDef:
        """
        Returns Amazon EC2 instance recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_instance_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_ec2_instance_recommendations)
        """
    def get_ec2_recommendation_projected_metrics(
        self,
        *,
        instanceArn: str,
        stat: MetricStatisticType,
        period: int,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        recommendationPreferences: "RecommendationPreferencesTypeDef" = None
    ) -> GetEC2RecommendationProjectedMetricsResponseTypeDef:
        """
        Returns the projected utilization metrics of Amazon EC2 instance
        recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_ec2_recommendation_projected_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_ec2_recommendation_projected_metrics)
        """
    def get_effective_recommendation_preferences(
        self, *, resourceArn: str
    ) -> GetEffectiveRecommendationPreferencesResponseTypeDef:
        """
        Returns the recommendation preferences that are in effect for a given resource,
        such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_effective_recommendation_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_effective_recommendation_preferences)
        """
    def get_enrollment_status(self) -> GetEnrollmentStatusResponseTypeDef:
        """
        Returns the enrollment (opt in) status of an account to the Compute Optimizer
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_enrollment_status)
        """
    def get_enrollment_statuses_for_organization(
        self,
        *,
        filters: List["EnrollmentFilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetEnrollmentStatusesForOrganizationResponseTypeDef:
        """
        Returns the Compute Optimizer enrollment (opt-in) status of organization member
        accounts, if your account is an organization management account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_enrollment_statuses_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_enrollment_statuses_for_organization)
        """
    def get_lambda_function_recommendations(
        self,
        *,
        functionArns: List[str] = None,
        accountIds: List[str] = None,
        filters: List["LambdaFunctionRecommendationFilterTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetLambdaFunctionRecommendationsResponseTypeDef:
        """
        Returns Lambda function recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_lambda_function_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_lambda_function_recommendations)
        """
    def get_recommendation_preferences(
        self,
        *,
        resourceType: ResourceTypeType,
        scope: "ScopeTypeDef" = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetRecommendationPreferencesResponseTypeDef:
        """
        Returns existing recommendation preferences, such as enhanced infrastructure
        metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_recommendation_preferences)
        """
    def get_recommendation_summaries(
        self, *, accountIds: List[str] = None, nextToken: str = None, maxResults: int = None
    ) -> GetRecommendationSummariesResponseTypeDef:
        """
        Returns the optimization findings for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.get_recommendation_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#get_recommendation_summaries)
        """
    def put_recommendation_preferences(
        self,
        *,
        resourceType: ResourceTypeType,
        scope: "ScopeTypeDef" = None,
        enhancedInfrastructureMetrics: EnhancedInfrastructureMetricsType = None,
        inferredWorkloadTypes: InferredWorkloadTypesPreferenceType = None
    ) -> Dict[str, Any]:
        """
        Creates a new recommendation preference or updates an existing recommendation
        preference, such as enhanced infrastructure metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.put_recommendation_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#put_recommendation_preferences)
        """
    def update_enrollment_status(
        self, *, status: StatusType, includeMemberAccounts: bool = None
    ) -> UpdateEnrollmentStatusResponseTypeDef:
        """
        Updates the enrollment (opt in and opt out) status of an account to the Compute
        Optimizer service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/compute-optimizer.html#ComputeOptimizer.Client.update_enrollment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/client.html#update_enrollment_status)
        """
