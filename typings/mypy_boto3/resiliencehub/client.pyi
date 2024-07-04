"""
Type annotations for resiliencehub service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_resiliencehub import ResilienceHubClient

    client: ResilienceHubClient = boto3.client("resiliencehub")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AppAssessmentScheduleTypeType,
    AssessmentInvokerType,
    AssessmentStatusType,
    ComplianceStatusType,
    DataLocationConstraintType,
    DisruptionTypeType,
    RecommendationTemplateStatusType,
    RenderRecommendationTypeType,
    ResiliencyPolicyTierType,
    ResourceImportStrategyTypeType,
    TemplateFormatType,
)
from .paginator import ListAppAssessmentResourceDriftsPaginator
from .type_defs import (
    AddDraftAppVersionResourceMappingsResponseTypeDef,
    BatchUpdateRecommendationStatusResponseTypeDef,
    CreateAppResponseTypeDef,
    CreateAppVersionAppComponentResponseTypeDef,
    CreateAppVersionResourceResponseTypeDef,
    CreateRecommendationTemplateResponseTypeDef,
    CreateResiliencyPolicyResponseTypeDef,
    DeleteAppAssessmentResponseTypeDef,
    DeleteAppInputSourceResponseTypeDef,
    DeleteAppResponseTypeDef,
    DeleteAppVersionAppComponentResponseTypeDef,
    DeleteAppVersionResourceResponseTypeDef,
    DeleteRecommendationTemplateResponseTypeDef,
    DeleteResiliencyPolicyResponseTypeDef,
    DescribeAppAssessmentResponseTypeDef,
    DescribeAppResponseTypeDef,
    DescribeAppVersionAppComponentResponseTypeDef,
    DescribeAppVersionResourceResponseTypeDef,
    DescribeAppVersionResourcesResolutionStatusResponseTypeDef,
    DescribeAppVersionResponseTypeDef,
    DescribeAppVersionTemplateResponseTypeDef,
    DescribeDraftAppVersionResourcesImportStatusResponseTypeDef,
    DescribeResiliencyPolicyResponseTypeDef,
    EksSourceClusterNamespaceTypeDef,
    EksSourceTypeDef,
    EventSubscriptionTypeDef,
    FailurePolicyTypeDef,
    ImportResourcesToDraftAppVersionResponseTypeDef,
    ListAlarmRecommendationsResponseTypeDef,
    ListAppAssessmentComplianceDriftsResponseTypeDef,
    ListAppAssessmentResourceDriftsResponseTypeDef,
    ListAppAssessmentsResponseTypeDef,
    ListAppComponentCompliancesResponseTypeDef,
    ListAppComponentRecommendationsResponseTypeDef,
    ListAppInputSourcesResponseTypeDef,
    ListAppsResponseTypeDef,
    ListAppVersionAppComponentsResponseTypeDef,
    ListAppVersionResourceMappingsResponseTypeDef,
    ListAppVersionResourcesResponseTypeDef,
    ListAppVersionsResponseTypeDef,
    ListRecommendationTemplatesResponseTypeDef,
    ListResiliencyPoliciesResponseTypeDef,
    ListSopRecommendationsResponseTypeDef,
    ListSuggestedResiliencyPoliciesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestRecommendationsResponseTypeDef,
    ListUnsupportedAppVersionResourcesResponseTypeDef,
    LogicalResourceIdTypeDef,
    PermissionModelTypeDef,
    PublishAppVersionResponseTypeDef,
    PutDraftAppVersionTemplateResponseTypeDef,
    RemoveDraftAppVersionResourceMappingsResponseTypeDef,
    ResolveAppVersionResourcesResponseTypeDef,
    ResourceMappingTypeDef,
    StartAppAssessmentResponseTypeDef,
    TerraformSourceTypeDef,
    UpdateAppResponseTypeDef,
    UpdateAppVersionAppComponentResponseTypeDef,
    UpdateAppVersionResourceResponseTypeDef,
    UpdateAppVersionResponseTypeDef,
    UpdateRecommendationStatusRequestEntryTypeDef,
    UpdateResiliencyPolicyResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ResilienceHubClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ResilienceHubClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResilienceHubClient exceptions.
        """

    def add_draft_app_version_resource_mappings(
        self, *, appArn: str, resourceMappings: List["ResourceMappingTypeDef"]
    ) -> AddDraftAppVersionResourceMappingsResponseTypeDef:
        """
        Adds the source of resource-maps to the draft version of an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.add_draft_app_version_resource_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#add_draft_app_version_resource_mappings)
        """

    def batch_update_recommendation_status(
        self, *, appArn: str, requestEntries: List["UpdateRecommendationStatusRequestEntryTypeDef"]
    ) -> BatchUpdateRecommendationStatusResponseTypeDef:
        """
        Enables you to include or exclude one or more operational recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.batch_update_recommendation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#batch_update_recommendation_status)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#close)
        """

    def create_app(
        self,
        *,
        name: str,
        assessmentSchedule: AppAssessmentScheduleTypeType = None,
        clientToken: str = None,
        description: str = None,
        eventSubscriptions: List["EventSubscriptionTypeDef"] = None,
        permissionModel: "PermissionModelTypeDef" = None,
        policyArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAppResponseTypeDef:
        """
        Creates an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#create_app)
        """

    def create_app_version_app_component(
        self,
        *,
        appArn: str,
        name: str,
        type: str,
        additionalInfo: Dict[str, List[str]] = None,
        clientToken: str = None,
        id: str = None
    ) -> CreateAppVersionAppComponentResponseTypeDef:
        """
        Creates a new Application Component in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.create_app_version_app_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#create_app_version_app_component)
        """

    def create_app_version_resource(
        self,
        *,
        appArn: str,
        appComponents: List[str],
        logicalResourceId: "LogicalResourceIdTypeDef",
        physicalResourceId: str,
        resourceType: str,
        additionalInfo: Dict[str, List[str]] = None,
        awsAccountId: str = None,
        awsRegion: str = None,
        clientToken: str = None,
        resourceName: str = None
    ) -> CreateAppVersionResourceResponseTypeDef:
        """
        Adds a resource to the Resilience Hub application and assigns it to the
        specified Application Components.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.create_app_version_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#create_app_version_resource)
        """

    def create_recommendation_template(
        self,
        *,
        assessmentArn: str,
        name: str,
        bucketName: str = None,
        clientToken: str = None,
        format: TemplateFormatType = None,
        recommendationIds: List[str] = None,
        recommendationTypes: List[RenderRecommendationTypeType] = None,
        tags: Dict[str, str] = None
    ) -> CreateRecommendationTemplateResponseTypeDef:
        """
        Creates a new recommendation template for the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.create_recommendation_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#create_recommendation_template)
        """

    def create_resiliency_policy(
        self,
        *,
        policy: Dict[DisruptionTypeType, "FailurePolicyTypeDef"],
        policyName: str,
        tier: ResiliencyPolicyTierType,
        clientToken: str = None,
        dataLocationConstraint: DataLocationConstraintType = None,
        policyDescription: str = None,
        tags: Dict[str, str] = None
    ) -> CreateResiliencyPolicyResponseTypeDef:
        """
        Creates a resiliency policy for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.create_resiliency_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#create_resiliency_policy)
        """

    def delete_app(
        self, *, appArn: str, clientToken: str = None, forceDelete: bool = None
    ) -> DeleteAppResponseTypeDef:
        """
        Deletes an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_app)
        """

    def delete_app_assessment(
        self, *, assessmentArn: str, clientToken: str = None
    ) -> DeleteAppAssessmentResponseTypeDef:
        """
        Deletes an Resilience Hub application assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_app_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_app_assessment)
        """

    def delete_app_input_source(
        self,
        *,
        appArn: str,
        clientToken: str = None,
        eksSourceClusterNamespace: "EksSourceClusterNamespaceTypeDef" = None,
        sourceArn: str = None,
        terraformSource: "TerraformSourceTypeDef" = None
    ) -> DeleteAppInputSourceResponseTypeDef:
        """
        Deletes the input source and all of its imported resources from the Resilience
        Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_app_input_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_app_input_source)
        """

    def delete_app_version_app_component(
        self, *, appArn: str, id: str, clientToken: str = None
    ) -> DeleteAppVersionAppComponentResponseTypeDef:
        """
        Deletes an Application Component from the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_app_version_app_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_app_version_app_component)
        """

    def delete_app_version_resource(
        self,
        *,
        appArn: str,
        awsAccountId: str = None,
        awsRegion: str = None,
        clientToken: str = None,
        logicalResourceId: "LogicalResourceIdTypeDef" = None,
        physicalResourceId: str = None,
        resourceName: str = None
    ) -> DeleteAppVersionResourceResponseTypeDef:
        """
        Deletes a resource from the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_app_version_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_app_version_resource)
        """

    def delete_recommendation_template(
        self, *, recommendationTemplateArn: str, clientToken: str = None
    ) -> DeleteRecommendationTemplateResponseTypeDef:
        """
        Deletes a recommendation template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_recommendation_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_recommendation_template)
        """

    def delete_resiliency_policy(
        self, *, policyArn: str, clientToken: str = None
    ) -> DeleteResiliencyPolicyResponseTypeDef:
        """
        Deletes a resiliency policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.delete_resiliency_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#delete_resiliency_policy)
        """

    def describe_app(self, *, appArn: str) -> DescribeAppResponseTypeDef:
        """
        Describes an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app)
        """

    def describe_app_assessment(
        self, *, assessmentArn: str
    ) -> DescribeAppAssessmentResponseTypeDef:
        """
        Describes an assessment for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app_assessment)
        """

    def describe_app_version(
        self, *, appArn: str, appVersion: str
    ) -> DescribeAppVersionResponseTypeDef:
        """
        Describes the Resilience Hub application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app_version)
        """

    def describe_app_version_app_component(
        self, *, appArn: str, appVersion: str, id: str
    ) -> DescribeAppVersionAppComponentResponseTypeDef:
        """
        Describes an Application Component in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app_version_app_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app_version_app_component)
        """

    def describe_app_version_resource(
        self,
        *,
        appArn: str,
        appVersion: str,
        awsAccountId: str = None,
        awsRegion: str = None,
        logicalResourceId: "LogicalResourceIdTypeDef" = None,
        physicalResourceId: str = None,
        resourceName: str = None
    ) -> DescribeAppVersionResourceResponseTypeDef:
        """
        Describes a resource of the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app_version_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app_version_resource)
        """

    def describe_app_version_resources_resolution_status(
        self, *, appArn: str, appVersion: str, resolutionId: str = None
    ) -> DescribeAppVersionResourcesResolutionStatusResponseTypeDef:
        """
        Returns the resolution status for the specified resolution identifier for an
        application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app_version_resources_resolution_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app_version_resources_resolution_status)
        """

    def describe_app_version_template(
        self, *, appArn: str, appVersion: str
    ) -> DescribeAppVersionTemplateResponseTypeDef:
        """
        Describes details about an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_app_version_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_app_version_template)
        """

    def describe_draft_app_version_resources_import_status(
        self, *, appArn: str
    ) -> DescribeDraftAppVersionResourcesImportStatusResponseTypeDef:
        """
        Describes the status of importing resources to an application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_draft_app_version_resources_import_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_draft_app_version_resources_import_status)
        """

    def describe_resiliency_policy(
        self, *, policyArn: str
    ) -> DescribeResiliencyPolicyResponseTypeDef:
        """
        Describes a specified resiliency policy for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.describe_resiliency_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#describe_resiliency_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#generate_presigned_url)
        """

    def import_resources_to_draft_app_version(
        self,
        *,
        appArn: str,
        eksSources: List["EksSourceTypeDef"] = None,
        importStrategy: ResourceImportStrategyTypeType = None,
        sourceArns: List[str] = None,
        terraformSources: List["TerraformSourceTypeDef"] = None
    ) -> ImportResourcesToDraftAppVersionResponseTypeDef:
        """
        Imports resources to Resilience Hub application draft version from different
        input sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.import_resources_to_draft_app_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#import_resources_to_draft_app_version)
        """

    def list_alarm_recommendations(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAlarmRecommendationsResponseTypeDef:
        """
        Lists the alarm recommendations for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_alarm_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_alarm_recommendations)
        """

    def list_app_assessment_compliance_drifts(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppAssessmentComplianceDriftsResponseTypeDef:
        """
        List of compliance drifts that were detected while running an assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_assessment_compliance_drifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_assessment_compliance_drifts)
        """

    def list_app_assessment_resource_drifts(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppAssessmentResourceDriftsResponseTypeDef:
        """
        Indicates the list of resource drifts that were detected while running an
        assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_assessment_resource_drifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_assessment_resource_drifts)
        """

    def list_app_assessments(
        self,
        *,
        appArn: str = None,
        assessmentName: str = None,
        assessmentStatus: List[AssessmentStatusType] = None,
        complianceStatus: ComplianceStatusType = None,
        invoker: AssessmentInvokerType = None,
        maxResults: int = None,
        nextToken: str = None,
        reverseOrder: bool = None
    ) -> ListAppAssessmentsResponseTypeDef:
        """
        Lists the assessments for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_assessments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_assessments)
        """

    def list_app_component_compliances(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppComponentCompliancesResponseTypeDef:
        """
        Lists the compliances for an Resilience Hub Application Component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_component_compliances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_component_compliances)
        """

    def list_app_component_recommendations(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppComponentRecommendationsResponseTypeDef:
        """
        Lists the recommendations for an Resilience Hub Application Component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_component_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_component_recommendations)
        """

    def list_app_input_sources(
        self, *, appArn: str, appVersion: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppInputSourcesResponseTypeDef:
        """
        Lists all the input sources of the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_input_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_input_sources)
        """

    def list_app_version_app_components(
        self, *, appArn: str, appVersion: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppVersionAppComponentsResponseTypeDef:
        """
        Lists all the Application Components in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_version_app_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_version_app_components)
        """

    def list_app_version_resource_mappings(
        self, *, appArn: str, appVersion: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppVersionResourceMappingsResponseTypeDef:
        """
        Lists how the resources in an application version are mapped/sourced from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_version_resource_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_version_resource_mappings)
        """

    def list_app_version_resources(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int = None,
        nextToken: str = None,
        resolutionId: str = None
    ) -> ListAppVersionResourcesResponseTypeDef:
        """
        Lists all the resources in an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_version_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_version_resources)
        """

    def list_app_versions(
        self,
        *,
        appArn: str,
        endTime: Union[datetime, str] = None,
        maxResults: int = None,
        nextToken: str = None,
        startTime: Union[datetime, str] = None
    ) -> ListAppVersionsResponseTypeDef:
        """
        Lists the different versions for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_app_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_app_versions)
        """

    def list_apps(
        self,
        *,
        appArn: str = None,
        fromLastAssessmentTime: Union[datetime, str] = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None,
        reverseOrder: bool = None,
        toLastAssessmentTime: Union[datetime, str] = None
    ) -> ListAppsResponseTypeDef:
        """
        Lists your Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_apps)
        """

    def list_recommendation_templates(
        self,
        *,
        assessmentArn: str = None,
        maxResults: int = None,
        name: str = None,
        nextToken: str = None,
        recommendationTemplateArn: str = None,
        reverseOrder: bool = None,
        status: List[RecommendationTemplateStatusType] = None
    ) -> ListRecommendationTemplatesResponseTypeDef:
        """
        Lists the recommendation templates for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_recommendation_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_recommendation_templates)
        """

    def list_resiliency_policies(
        self, *, maxResults: int = None, nextToken: str = None, policyName: str = None
    ) -> ListResiliencyPoliciesResponseTypeDef:
        """
        Lists the resiliency policies for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_resiliency_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_resiliency_policies)
        """

    def list_sop_recommendations(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListSopRecommendationsResponseTypeDef:
        """
        Lists the standard operating procedure (SOP) recommendations for the Resilience
        Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_sop_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_sop_recommendations)
        """

    def list_suggested_resiliency_policies(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSuggestedResiliencyPoliciesResponseTypeDef:
        """
        Lists the suggested resiliency policies for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_suggested_resiliency_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_suggested_resiliency_policies)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for your resources in your Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_tags_for_resource)
        """

    def list_test_recommendations(
        self, *, assessmentArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListTestRecommendationsResponseTypeDef:
        """
        Lists the test recommendations for the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_test_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_test_recommendations)
        """

    def list_unsupported_app_version_resources(
        self,
        *,
        appArn: str,
        appVersion: str,
        maxResults: int = None,
        nextToken: str = None,
        resolutionId: str = None
    ) -> ListUnsupportedAppVersionResourcesResponseTypeDef:
        """
        Lists the resources that are not currently supported in Resilience Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.list_unsupported_app_version_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#list_unsupported_app_version_resources)
        """

    def publish_app_version(
        self, *, appArn: str, versionName: str = None
    ) -> PublishAppVersionResponseTypeDef:
        """
        Publishes a new version of a specific Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.publish_app_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#publish_app_version)
        """

    def put_draft_app_version_template(
        self, *, appArn: str, appTemplateBody: str
    ) -> PutDraftAppVersionTemplateResponseTypeDef:
        """
        Adds or updates the app template for an Resilience Hub application draft
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.put_draft_app_version_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#put_draft_app_version_template)
        """

    def remove_draft_app_version_resource_mappings(
        self,
        *,
        appArn: str,
        appRegistryAppNames: List[str] = None,
        eksSourceNames: List[str] = None,
        logicalStackNames: List[str] = None,
        resourceGroupNames: List[str] = None,
        resourceNames: List[str] = None,
        terraformSourceNames: List[str] = None
    ) -> RemoveDraftAppVersionResourceMappingsResponseTypeDef:
        """
        Removes resource mappings from a draft application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.remove_draft_app_version_resource_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#remove_draft_app_version_resource_mappings)
        """

    def resolve_app_version_resources(
        self, *, appArn: str, appVersion: str
    ) -> ResolveAppVersionResourcesResponseTypeDef:
        """
        Resolves the resources for an application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.resolve_app_version_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#resolve_app_version_resources)
        """

    def start_app_assessment(
        self,
        *,
        appArn: str,
        appVersion: str,
        assessmentName: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> StartAppAssessmentResponseTypeDef:
        """
        Creates a new application assessment for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.start_app_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#start_app_assessment)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#untag_resource)
        """

    def update_app(
        self,
        *,
        appArn: str,
        assessmentSchedule: AppAssessmentScheduleTypeType = None,
        clearResiliencyPolicyArn: bool = None,
        description: str = None,
        eventSubscriptions: List["EventSubscriptionTypeDef"] = None,
        permissionModel: "PermissionModelTypeDef" = None,
        policyArn: str = None
    ) -> UpdateAppResponseTypeDef:
        """
        Updates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.update_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#update_app)
        """

    def update_app_version(
        self, *, appArn: str, additionalInfo: Dict[str, List[str]] = None
    ) -> UpdateAppVersionResponseTypeDef:
        """
        Updates the Resilience Hub application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.update_app_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#update_app_version)
        """

    def update_app_version_app_component(
        self,
        *,
        appArn: str,
        id: str,
        additionalInfo: Dict[str, List[str]] = None,
        name: str = None,
        type: str = None
    ) -> UpdateAppVersionAppComponentResponseTypeDef:
        """
        Updates an existing Application Component in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.update_app_version_app_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#update_app_version_app_component)
        """

    def update_app_version_resource(
        self,
        *,
        appArn: str,
        additionalInfo: Dict[str, List[str]] = None,
        appComponents: List[str] = None,
        awsAccountId: str = None,
        awsRegion: str = None,
        excluded: bool = None,
        logicalResourceId: "LogicalResourceIdTypeDef" = None,
        physicalResourceId: str = None,
        resourceName: str = None,
        resourceType: str = None
    ) -> UpdateAppVersionResourceResponseTypeDef:
        """
        Updates the resource details in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.update_app_version_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#update_app_version_resource)
        """

    def update_resiliency_policy(
        self,
        *,
        policyArn: str,
        dataLocationConstraint: DataLocationConstraintType = None,
        policy: Dict[DisruptionTypeType, "FailurePolicyTypeDef"] = None,
        policyDescription: str = None,
        policyName: str = None,
        tier: ResiliencyPolicyTierType = None
    ) -> UpdateResiliencyPolicyResponseTypeDef:
        """
        Updates a resiliency policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Client.update_resiliency_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client.html#update_resiliency_policy)
        """

    def get_paginator(
        self, operation_name: Literal["list_app_assessment_resource_drifts"]
    ) -> ListAppAssessmentResourceDriftsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators.html#listappassessmentresourcedriftspaginator)
        """
