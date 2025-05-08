"""
Type annotations for resiliencehub service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resiliencehub.client import ResilienceHubClient

    session = Session()
    client: ResilienceHubClient = session.client("resiliencehub")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAppAssessmentResourceDriftsPaginator,
    ListMetricsPaginator,
    ListResourceGroupingRecommendationsPaginator,
)
from .type_defs import (
    AcceptResourceGroupingRecommendationsRequestTypeDef,
    AcceptResourceGroupingRecommendationsResponseTypeDef,
    AddDraftAppVersionResourceMappingsRequestTypeDef,
    AddDraftAppVersionResourceMappingsResponseTypeDef,
    BatchUpdateRecommendationStatusRequestTypeDef,
    BatchUpdateRecommendationStatusResponseTypeDef,
    CreateAppRequestTypeDef,
    CreateAppResponseTypeDef,
    CreateAppVersionAppComponentRequestTypeDef,
    CreateAppVersionAppComponentResponseTypeDef,
    CreateAppVersionResourceRequestTypeDef,
    CreateAppVersionResourceResponseTypeDef,
    CreateRecommendationTemplateRequestTypeDef,
    CreateRecommendationTemplateResponseTypeDef,
    CreateResiliencyPolicyRequestTypeDef,
    CreateResiliencyPolicyResponseTypeDef,
    DeleteAppAssessmentRequestTypeDef,
    DeleteAppAssessmentResponseTypeDef,
    DeleteAppInputSourceRequestTypeDef,
    DeleteAppInputSourceResponseTypeDef,
    DeleteAppRequestTypeDef,
    DeleteAppResponseTypeDef,
    DeleteAppVersionAppComponentRequestTypeDef,
    DeleteAppVersionAppComponentResponseTypeDef,
    DeleteAppVersionResourceRequestTypeDef,
    DeleteAppVersionResourceResponseTypeDef,
    DeleteRecommendationTemplateRequestTypeDef,
    DeleteRecommendationTemplateResponseTypeDef,
    DeleteResiliencyPolicyRequestTypeDef,
    DeleteResiliencyPolicyResponseTypeDef,
    DescribeAppAssessmentRequestTypeDef,
    DescribeAppAssessmentResponseTypeDef,
    DescribeAppRequestTypeDef,
    DescribeAppResponseTypeDef,
    DescribeAppVersionAppComponentRequestTypeDef,
    DescribeAppVersionAppComponentResponseTypeDef,
    DescribeAppVersionRequestTypeDef,
    DescribeAppVersionResourceRequestTypeDef,
    DescribeAppVersionResourceResponseTypeDef,
    DescribeAppVersionResourcesResolutionStatusRequestTypeDef,
    DescribeAppVersionResourcesResolutionStatusResponseTypeDef,
    DescribeAppVersionResponseTypeDef,
    DescribeAppVersionTemplateRequestTypeDef,
    DescribeAppVersionTemplateResponseTypeDef,
    DescribeDraftAppVersionResourcesImportStatusRequestTypeDef,
    DescribeDraftAppVersionResourcesImportStatusResponseTypeDef,
    DescribeMetricsExportRequestTypeDef,
    DescribeMetricsExportResponseTypeDef,
    DescribeResiliencyPolicyRequestTypeDef,
    DescribeResiliencyPolicyResponseTypeDef,
    DescribeResourceGroupingRecommendationTaskRequestTypeDef,
    DescribeResourceGroupingRecommendationTaskResponseTypeDef,
    ImportResourcesToDraftAppVersionRequestTypeDef,
    ImportResourcesToDraftAppVersionResponseTypeDef,
    ListAlarmRecommendationsRequestTypeDef,
    ListAlarmRecommendationsResponseTypeDef,
    ListAppAssessmentComplianceDriftsRequestTypeDef,
    ListAppAssessmentComplianceDriftsResponseTypeDef,
    ListAppAssessmentResourceDriftsRequestTypeDef,
    ListAppAssessmentResourceDriftsResponseTypeDef,
    ListAppAssessmentsRequestTypeDef,
    ListAppAssessmentsResponseTypeDef,
    ListAppComponentCompliancesRequestTypeDef,
    ListAppComponentCompliancesResponseTypeDef,
    ListAppComponentRecommendationsRequestTypeDef,
    ListAppComponentRecommendationsResponseTypeDef,
    ListAppInputSourcesRequestTypeDef,
    ListAppInputSourcesResponseTypeDef,
    ListAppsRequestTypeDef,
    ListAppsResponseTypeDef,
    ListAppVersionAppComponentsRequestTypeDef,
    ListAppVersionAppComponentsResponseTypeDef,
    ListAppVersionResourceMappingsRequestTypeDef,
    ListAppVersionResourceMappingsResponseTypeDef,
    ListAppVersionResourcesRequestTypeDef,
    ListAppVersionResourcesResponseTypeDef,
    ListAppVersionsRequestTypeDef,
    ListAppVersionsResponseTypeDef,
    ListMetricsRequestTypeDef,
    ListMetricsResponseTypeDef,
    ListRecommendationTemplatesRequestTypeDef,
    ListRecommendationTemplatesResponseTypeDef,
    ListResiliencyPoliciesRequestTypeDef,
    ListResiliencyPoliciesResponseTypeDef,
    ListResourceGroupingRecommendationsRequestTypeDef,
    ListResourceGroupingRecommendationsResponseTypeDef,
    ListSopRecommendationsRequestTypeDef,
    ListSopRecommendationsResponseTypeDef,
    ListSuggestedResiliencyPoliciesRequestTypeDef,
    ListSuggestedResiliencyPoliciesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestRecommendationsRequestTypeDef,
    ListTestRecommendationsResponseTypeDef,
    ListUnsupportedAppVersionResourcesRequestTypeDef,
    ListUnsupportedAppVersionResourcesResponseTypeDef,
    PublishAppVersionRequestTypeDef,
    PublishAppVersionResponseTypeDef,
    PutDraftAppVersionTemplateRequestTypeDef,
    PutDraftAppVersionTemplateResponseTypeDef,
    RejectResourceGroupingRecommendationsRequestTypeDef,
    RejectResourceGroupingRecommendationsResponseTypeDef,
    RemoveDraftAppVersionResourceMappingsRequestTypeDef,
    RemoveDraftAppVersionResourceMappingsResponseTypeDef,
    ResolveAppVersionResourcesRequestTypeDef,
    ResolveAppVersionResourcesResponseTypeDef,
    StartAppAssessmentRequestTypeDef,
    StartAppAssessmentResponseTypeDef,
    StartMetricsExportRequestTypeDef,
    StartMetricsExportResponseTypeDef,
    StartResourceGroupingRecommendationTaskRequestTypeDef,
    StartResourceGroupingRecommendationTaskResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAppRequestTypeDef,
    UpdateAppResponseTypeDef,
    UpdateAppVersionAppComponentRequestTypeDef,
    UpdateAppVersionAppComponentResponseTypeDef,
    UpdateAppVersionRequestTypeDef,
    UpdateAppVersionResourceRequestTypeDef,
    UpdateAppVersionResourceResponseTypeDef,
    UpdateAppVersionResponseTypeDef,
    UpdateResiliencyPolicyRequestTypeDef,
    UpdateResiliencyPolicyResponseTypeDef,
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

__all__ = ("ResilienceHubClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html#ResilienceHub.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResilienceHubClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html#ResilienceHub.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#generate_presigned_url)
        """

    def accept_resource_grouping_recommendations(
        self, **kwargs: Unpack[AcceptResourceGroupingRecommendationsRequestTypeDef]
    ) -> AcceptResourceGroupingRecommendationsResponseTypeDef:
        """
        Accepts the resource grouping recommendations suggested by Resilience Hub for
        your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/accept_resource_grouping_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#accept_resource_grouping_recommendations)
        """

    def add_draft_app_version_resource_mappings(
        self, **kwargs: Unpack[AddDraftAppVersionResourceMappingsRequestTypeDef]
    ) -> AddDraftAppVersionResourceMappingsResponseTypeDef:
        """
        Adds the source of resource-maps to the draft version of an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/add_draft_app_version_resource_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#add_draft_app_version_resource_mappings)
        """

    def batch_update_recommendation_status(
        self, **kwargs: Unpack[BatchUpdateRecommendationStatusRequestTypeDef]
    ) -> BatchUpdateRecommendationStatusResponseTypeDef:
        """
        Enables you to include or exclude one or more operational recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/batch_update_recommendation_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#batch_update_recommendation_status)
        """

    def create_app(self, **kwargs: Unpack[CreateAppRequestTypeDef]) -> CreateAppResponseTypeDef:
        """
        Creates an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/create_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#create_app)
        """

    def create_app_version_app_component(
        self, **kwargs: Unpack[CreateAppVersionAppComponentRequestTypeDef]
    ) -> CreateAppVersionAppComponentResponseTypeDef:
        """
        Creates a new Application Component in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/create_app_version_app_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#create_app_version_app_component)
        """

    def create_app_version_resource(
        self, **kwargs: Unpack[CreateAppVersionResourceRequestTypeDef]
    ) -> CreateAppVersionResourceResponseTypeDef:
        """
        Adds a resource to the Resilience Hub application and assigns it to the
        specified Application Components.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/create_app_version_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#create_app_version_resource)
        """

    def create_recommendation_template(
        self, **kwargs: Unpack[CreateRecommendationTemplateRequestTypeDef]
    ) -> CreateRecommendationTemplateResponseTypeDef:
        """
        Creates a new recommendation template for the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/create_recommendation_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#create_recommendation_template)
        """

    def create_resiliency_policy(
        self, **kwargs: Unpack[CreateResiliencyPolicyRequestTypeDef]
    ) -> CreateResiliencyPolicyResponseTypeDef:
        """
        Creates a resiliency policy for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/create_resiliency_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#create_resiliency_policy)
        """

    def delete_app(self, **kwargs: Unpack[DeleteAppRequestTypeDef]) -> DeleteAppResponseTypeDef:
        """
        Deletes an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_app)
        """

    def delete_app_assessment(
        self, **kwargs: Unpack[DeleteAppAssessmentRequestTypeDef]
    ) -> DeleteAppAssessmentResponseTypeDef:
        """
        Deletes an Resilience Hub application assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_app_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_app_assessment)
        """

    def delete_app_input_source(
        self, **kwargs: Unpack[DeleteAppInputSourceRequestTypeDef]
    ) -> DeleteAppInputSourceResponseTypeDef:
        """
        Deletes the input source and all of its imported resources from the Resilience
        Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_app_input_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_app_input_source)
        """

    def delete_app_version_app_component(
        self, **kwargs: Unpack[DeleteAppVersionAppComponentRequestTypeDef]
    ) -> DeleteAppVersionAppComponentResponseTypeDef:
        """
        Deletes an Application Component from the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_app_version_app_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_app_version_app_component)
        """

    def delete_app_version_resource(
        self, **kwargs: Unpack[DeleteAppVersionResourceRequestTypeDef]
    ) -> DeleteAppVersionResourceResponseTypeDef:
        """
        Deletes a resource from the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_app_version_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_app_version_resource)
        """

    def delete_recommendation_template(
        self, **kwargs: Unpack[DeleteRecommendationTemplateRequestTypeDef]
    ) -> DeleteRecommendationTemplateResponseTypeDef:
        """
        Deletes a recommendation template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_recommendation_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_recommendation_template)
        """

    def delete_resiliency_policy(
        self, **kwargs: Unpack[DeleteResiliencyPolicyRequestTypeDef]
    ) -> DeleteResiliencyPolicyResponseTypeDef:
        """
        Deletes a resiliency policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/delete_resiliency_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#delete_resiliency_policy)
        """

    def describe_app(
        self, **kwargs: Unpack[DescribeAppRequestTypeDef]
    ) -> DescribeAppResponseTypeDef:
        """
        Describes an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app)
        """

    def describe_app_assessment(
        self, **kwargs: Unpack[DescribeAppAssessmentRequestTypeDef]
    ) -> DescribeAppAssessmentResponseTypeDef:
        """
        Describes an assessment for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app_assessment)
        """

    def describe_app_version(
        self, **kwargs: Unpack[DescribeAppVersionRequestTypeDef]
    ) -> DescribeAppVersionResponseTypeDef:
        """
        Describes the Resilience Hub application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app_version)
        """

    def describe_app_version_app_component(
        self, **kwargs: Unpack[DescribeAppVersionAppComponentRequestTypeDef]
    ) -> DescribeAppVersionAppComponentResponseTypeDef:
        """
        Describes an Application Component in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app_version_app_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app_version_app_component)
        """

    def describe_app_version_resource(
        self, **kwargs: Unpack[DescribeAppVersionResourceRequestTypeDef]
    ) -> DescribeAppVersionResourceResponseTypeDef:
        """
        Describes a resource of the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app_version_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app_version_resource)
        """

    def describe_app_version_resources_resolution_status(
        self, **kwargs: Unpack[DescribeAppVersionResourcesResolutionStatusRequestTypeDef]
    ) -> DescribeAppVersionResourcesResolutionStatusResponseTypeDef:
        """
        Returns the resolution status for the specified resolution identifier for an
        application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app_version_resources_resolution_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app_version_resources_resolution_status)
        """

    def describe_app_version_template(
        self, **kwargs: Unpack[DescribeAppVersionTemplateRequestTypeDef]
    ) -> DescribeAppVersionTemplateResponseTypeDef:
        """
        Describes details about an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_app_version_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_app_version_template)
        """

    def describe_draft_app_version_resources_import_status(
        self, **kwargs: Unpack[DescribeDraftAppVersionResourcesImportStatusRequestTypeDef]
    ) -> DescribeDraftAppVersionResourcesImportStatusResponseTypeDef:
        """
        Describes the status of importing resources to an application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_draft_app_version_resources_import_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_draft_app_version_resources_import_status)
        """

    def describe_metrics_export(
        self, **kwargs: Unpack[DescribeMetricsExportRequestTypeDef]
    ) -> DescribeMetricsExportResponseTypeDef:
        """
        Describes the metrics of the application configuration being exported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_metrics_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_metrics_export)
        """

    def describe_resiliency_policy(
        self, **kwargs: Unpack[DescribeResiliencyPolicyRequestTypeDef]
    ) -> DescribeResiliencyPolicyResponseTypeDef:
        """
        Describes a specified resiliency policy for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_resiliency_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_resiliency_policy)
        """

    def describe_resource_grouping_recommendation_task(
        self, **kwargs: Unpack[DescribeResourceGroupingRecommendationTaskRequestTypeDef]
    ) -> DescribeResourceGroupingRecommendationTaskResponseTypeDef:
        """
        Describes the resource grouping recommendation tasks run by Resilience Hub for
        your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/describe_resource_grouping_recommendation_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#describe_resource_grouping_recommendation_task)
        """

    def import_resources_to_draft_app_version(
        self, **kwargs: Unpack[ImportResourcesToDraftAppVersionRequestTypeDef]
    ) -> ImportResourcesToDraftAppVersionResponseTypeDef:
        """
        Imports resources to Resilience Hub application draft version from different
        input sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/import_resources_to_draft_app_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#import_resources_to_draft_app_version)
        """

    def list_alarm_recommendations(
        self, **kwargs: Unpack[ListAlarmRecommendationsRequestTypeDef]
    ) -> ListAlarmRecommendationsResponseTypeDef:
        """
        Lists the alarm recommendations for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_alarm_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_alarm_recommendations)
        """

    def list_app_assessment_compliance_drifts(
        self, **kwargs: Unpack[ListAppAssessmentComplianceDriftsRequestTypeDef]
    ) -> ListAppAssessmentComplianceDriftsResponseTypeDef:
        """
        List of compliance drifts that were detected while running an assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_assessment_compliance_drifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_assessment_compliance_drifts)
        """

    def list_app_assessment_resource_drifts(
        self, **kwargs: Unpack[ListAppAssessmentResourceDriftsRequestTypeDef]
    ) -> ListAppAssessmentResourceDriftsResponseTypeDef:
        """
        List of resource drifts that were detected while running an assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_assessment_resource_drifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_assessment_resource_drifts)
        """

    def list_app_assessments(
        self, **kwargs: Unpack[ListAppAssessmentsRequestTypeDef]
    ) -> ListAppAssessmentsResponseTypeDef:
        """
        Lists the assessments for an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_assessments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_assessments)
        """

    def list_app_component_compliances(
        self, **kwargs: Unpack[ListAppComponentCompliancesRequestTypeDef]
    ) -> ListAppComponentCompliancesResponseTypeDef:
        """
        Lists the compliances for an Resilience Hub Application Component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_component_compliances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_component_compliances)
        """

    def list_app_component_recommendations(
        self, **kwargs: Unpack[ListAppComponentRecommendationsRequestTypeDef]
    ) -> ListAppComponentRecommendationsResponseTypeDef:
        """
        Lists the recommendations for an Resilience Hub Application Component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_component_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_component_recommendations)
        """

    def list_app_input_sources(
        self, **kwargs: Unpack[ListAppInputSourcesRequestTypeDef]
    ) -> ListAppInputSourcesResponseTypeDef:
        """
        Lists all the input sources of the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_input_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_input_sources)
        """

    def list_app_version_app_components(
        self, **kwargs: Unpack[ListAppVersionAppComponentsRequestTypeDef]
    ) -> ListAppVersionAppComponentsResponseTypeDef:
        """
        Lists all the Application Components in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_version_app_components.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_version_app_components)
        """

    def list_app_version_resource_mappings(
        self, **kwargs: Unpack[ListAppVersionResourceMappingsRequestTypeDef]
    ) -> ListAppVersionResourceMappingsResponseTypeDef:
        """
        Lists how the resources in an application version are mapped/sourced from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_version_resource_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_version_resource_mappings)
        """

    def list_app_version_resources(
        self, **kwargs: Unpack[ListAppVersionResourcesRequestTypeDef]
    ) -> ListAppVersionResourcesResponseTypeDef:
        """
        Lists all the resources in an Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_version_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_version_resources)
        """

    def list_app_versions(
        self, **kwargs: Unpack[ListAppVersionsRequestTypeDef]
    ) -> ListAppVersionsResponseTypeDef:
        """
        Lists the different versions for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_app_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_app_versions)
        """

    def list_apps(self, **kwargs: Unpack[ListAppsRequestTypeDef]) -> ListAppsResponseTypeDef:
        """
        Lists your Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_apps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_apps)
        """

    def list_metrics(
        self, **kwargs: Unpack[ListMetricsRequestTypeDef]
    ) -> ListMetricsResponseTypeDef:
        """
        Lists the metrics that can be exported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_metrics)
        """

    def list_recommendation_templates(
        self, **kwargs: Unpack[ListRecommendationTemplatesRequestTypeDef]
    ) -> ListRecommendationTemplatesResponseTypeDef:
        """
        Lists the recommendation templates for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_recommendation_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_recommendation_templates)
        """

    def list_resiliency_policies(
        self, **kwargs: Unpack[ListResiliencyPoliciesRequestTypeDef]
    ) -> ListResiliencyPoliciesResponseTypeDef:
        """
        Lists the resiliency policies for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_resiliency_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_resiliency_policies)
        """

    def list_resource_grouping_recommendations(
        self, **kwargs: Unpack[ListResourceGroupingRecommendationsRequestTypeDef]
    ) -> ListResourceGroupingRecommendationsResponseTypeDef:
        """
        Lists the resource grouping recommendations suggested by Resilience Hub for
        your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_resource_grouping_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_resource_grouping_recommendations)
        """

    def list_sop_recommendations(
        self, **kwargs: Unpack[ListSopRecommendationsRequestTypeDef]
    ) -> ListSopRecommendationsResponseTypeDef:
        """
        Lists the standard operating procedure (SOP) recommendations for the Resilience
        Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_sop_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_sop_recommendations)
        """

    def list_suggested_resiliency_policies(
        self, **kwargs: Unpack[ListSuggestedResiliencyPoliciesRequestTypeDef]
    ) -> ListSuggestedResiliencyPoliciesResponseTypeDef:
        """
        Lists the suggested resiliency policies for the Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_suggested_resiliency_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_suggested_resiliency_policies)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for your resources in your Resilience Hub applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_tags_for_resource)
        """

    def list_test_recommendations(
        self, **kwargs: Unpack[ListTestRecommendationsRequestTypeDef]
    ) -> ListTestRecommendationsResponseTypeDef:
        """
        Lists the test recommendations for the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_test_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_test_recommendations)
        """

    def list_unsupported_app_version_resources(
        self, **kwargs: Unpack[ListUnsupportedAppVersionResourcesRequestTypeDef]
    ) -> ListUnsupportedAppVersionResourcesResponseTypeDef:
        """
        Lists the resources that are not currently supported in Resilience Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/list_unsupported_app_version_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#list_unsupported_app_version_resources)
        """

    def publish_app_version(
        self, **kwargs: Unpack[PublishAppVersionRequestTypeDef]
    ) -> PublishAppVersionResponseTypeDef:
        """
        Publishes a new version of a specific Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/publish_app_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#publish_app_version)
        """

    def put_draft_app_version_template(
        self, **kwargs: Unpack[PutDraftAppVersionTemplateRequestTypeDef]
    ) -> PutDraftAppVersionTemplateResponseTypeDef:
        """
        Adds or updates the app template for an Resilience Hub application draft
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/put_draft_app_version_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#put_draft_app_version_template)
        """

    def reject_resource_grouping_recommendations(
        self, **kwargs: Unpack[RejectResourceGroupingRecommendationsRequestTypeDef]
    ) -> RejectResourceGroupingRecommendationsResponseTypeDef:
        """
        Rejects resource grouping recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/reject_resource_grouping_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#reject_resource_grouping_recommendations)
        """

    def remove_draft_app_version_resource_mappings(
        self, **kwargs: Unpack[RemoveDraftAppVersionResourceMappingsRequestTypeDef]
    ) -> RemoveDraftAppVersionResourceMappingsResponseTypeDef:
        """
        Removes resource mappings from a draft application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/remove_draft_app_version_resource_mappings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#remove_draft_app_version_resource_mappings)
        """

    def resolve_app_version_resources(
        self, **kwargs: Unpack[ResolveAppVersionResourcesRequestTypeDef]
    ) -> ResolveAppVersionResourcesResponseTypeDef:
        """
        Resolves the resources for an application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/resolve_app_version_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#resolve_app_version_resources)
        """

    def start_app_assessment(
        self, **kwargs: Unpack[StartAppAssessmentRequestTypeDef]
    ) -> StartAppAssessmentResponseTypeDef:
        """
        Creates a new application assessment for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/start_app_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#start_app_assessment)
        """

    def start_metrics_export(
        self, **kwargs: Unpack[StartMetricsExportRequestTypeDef]
    ) -> StartMetricsExportResponseTypeDef:
        """
        Initiates the export task of metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/start_metrics_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#start_metrics_export)
        """

    def start_resource_grouping_recommendation_task(
        self, **kwargs: Unpack[StartResourceGroupingRecommendationTaskRequestTypeDef]
    ) -> StartResourceGroupingRecommendationTaskResponseTypeDef:
        """
        Starts grouping recommendation task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/start_resource_grouping_recommendation_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#start_resource_grouping_recommendation_task)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies one or more tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#untag_resource)
        """

    def update_app(self, **kwargs: Unpack[UpdateAppRequestTypeDef]) -> UpdateAppResponseTypeDef:
        """
        Updates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/update_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#update_app)
        """

    def update_app_version(
        self, **kwargs: Unpack[UpdateAppVersionRequestTypeDef]
    ) -> UpdateAppVersionResponseTypeDef:
        """
        Updates the Resilience Hub application version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/update_app_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#update_app_version)
        """

    def update_app_version_app_component(
        self, **kwargs: Unpack[UpdateAppVersionAppComponentRequestTypeDef]
    ) -> UpdateAppVersionAppComponentResponseTypeDef:
        """
        Updates an existing Application Component in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/update_app_version_app_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#update_app_version_app_component)
        """

    def update_app_version_resource(
        self, **kwargs: Unpack[UpdateAppVersionResourceRequestTypeDef]
    ) -> UpdateAppVersionResourceResponseTypeDef:
        """
        Updates the resource details in the Resilience Hub application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/update_app_version_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#update_app_version_resource)
        """

    def update_resiliency_policy(
        self, **kwargs: Unpack[UpdateResiliencyPolicyRequestTypeDef]
    ) -> UpdateResiliencyPolicyResponseTypeDef:
        """
        Updates a resiliency policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/update_resiliency_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#update_resiliency_policy)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_app_assessment_resource_drifts"]
    ) -> ListAppAssessmentResourceDriftsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_metrics"]
    ) -> ListMetricsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_grouping_recommendations"]
    ) -> ListResourceGroupingRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/client/#get_paginator)
        """
