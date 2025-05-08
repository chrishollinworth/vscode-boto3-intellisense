"""
Type annotations for inspector service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_inspector.client import InspectorClient

    session = Session()
    client: InspectorClient = session.client("inspector")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAssessmentRunAgentsPaginator,
    ListAssessmentRunsPaginator,
    ListAssessmentTargetsPaginator,
    ListAssessmentTemplatesPaginator,
    ListEventSubscriptionsPaginator,
    ListExclusionsPaginator,
    ListFindingsPaginator,
    ListRulesPackagesPaginator,
    PreviewAgentsPaginator,
)
from .type_defs import (
    AddAttributesToFindingsRequestTypeDef,
    AddAttributesToFindingsResponseTypeDef,
    CreateAssessmentTargetRequestTypeDef,
    CreateAssessmentTargetResponseTypeDef,
    CreateAssessmentTemplateRequestTypeDef,
    CreateAssessmentTemplateResponseTypeDef,
    CreateExclusionsPreviewRequestTypeDef,
    CreateExclusionsPreviewResponseTypeDef,
    CreateResourceGroupRequestTypeDef,
    CreateResourceGroupResponseTypeDef,
    DeleteAssessmentRunRequestTypeDef,
    DeleteAssessmentTargetRequestTypeDef,
    DeleteAssessmentTemplateRequestTypeDef,
    DescribeAssessmentRunsRequestTypeDef,
    DescribeAssessmentRunsResponseTypeDef,
    DescribeAssessmentTargetsRequestTypeDef,
    DescribeAssessmentTargetsResponseTypeDef,
    DescribeAssessmentTemplatesRequestTypeDef,
    DescribeAssessmentTemplatesResponseTypeDef,
    DescribeCrossAccountAccessRoleResponseTypeDef,
    DescribeExclusionsRequestTypeDef,
    DescribeExclusionsResponseTypeDef,
    DescribeFindingsRequestTypeDef,
    DescribeFindingsResponseTypeDef,
    DescribeResourceGroupsRequestTypeDef,
    DescribeResourceGroupsResponseTypeDef,
    DescribeRulesPackagesRequestTypeDef,
    DescribeRulesPackagesResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAssessmentReportRequestTypeDef,
    GetAssessmentReportResponseTypeDef,
    GetExclusionsPreviewRequestTypeDef,
    GetExclusionsPreviewResponseTypeDef,
    GetTelemetryMetadataRequestTypeDef,
    GetTelemetryMetadataResponseTypeDef,
    ListAssessmentRunAgentsRequestTypeDef,
    ListAssessmentRunAgentsResponseTypeDef,
    ListAssessmentRunsRequestTypeDef,
    ListAssessmentRunsResponseTypeDef,
    ListAssessmentTargetsRequestTypeDef,
    ListAssessmentTargetsResponseTypeDef,
    ListAssessmentTemplatesRequestTypeDef,
    ListAssessmentTemplatesResponseTypeDef,
    ListEventSubscriptionsRequestTypeDef,
    ListEventSubscriptionsResponseTypeDef,
    ListExclusionsRequestTypeDef,
    ListExclusionsResponseTypeDef,
    ListFindingsRequestTypeDef,
    ListFindingsResponseTypeDef,
    ListRulesPackagesRequestTypeDef,
    ListRulesPackagesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PreviewAgentsRequestTypeDef,
    PreviewAgentsResponseTypeDef,
    RegisterCrossAccountAccessRoleRequestTypeDef,
    RemoveAttributesFromFindingsRequestTypeDef,
    RemoveAttributesFromFindingsResponseTypeDef,
    SetTagsForResourceRequestTypeDef,
    StartAssessmentRunRequestTypeDef,
    StartAssessmentRunResponseTypeDef,
    StopAssessmentRunRequestTypeDef,
    SubscribeToEventRequestTypeDef,
    UnsubscribeFromEventRequestTypeDef,
    UpdateAssessmentTargetRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("InspectorClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    AgentsAlreadyRunningAssessmentException: Type[BotocoreClientError]
    AssessmentRunInProgressException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidCrossAccountRoleException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NoSuchEntityException: Type[BotocoreClientError]
    PreviewGenerationInProgressException: Type[BotocoreClientError]
    ServiceTemporarilyUnavailableException: Type[BotocoreClientError]
    UnsupportedFeatureException: Type[BotocoreClientError]

class InspectorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        InspectorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector.html#Inspector.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#generate_presigned_url)
        """

    def add_attributes_to_findings(
        self, **kwargs: Unpack[AddAttributesToFindingsRequestTypeDef]
    ) -> AddAttributesToFindingsResponseTypeDef:
        """
        Assigns attributes (key and value pairs) to the findings that are specified by
        the ARNs of the findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/add_attributes_to_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#add_attributes_to_findings)
        """

    def create_assessment_target(
        self, **kwargs: Unpack[CreateAssessmentTargetRequestTypeDef]
    ) -> CreateAssessmentTargetResponseTypeDef:
        """
        Creates a new assessment target using the ARN of the resource group that is
        generated by <a>CreateResourceGroup</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/create_assessment_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#create_assessment_target)
        """

    def create_assessment_template(
        self, **kwargs: Unpack[CreateAssessmentTemplateRequestTypeDef]
    ) -> CreateAssessmentTemplateResponseTypeDef:
        """
        Creates an assessment template for the assessment target that is specified by
        the ARN of the assessment target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/create_assessment_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#create_assessment_template)
        """

    def create_exclusions_preview(
        self, **kwargs: Unpack[CreateExclusionsPreviewRequestTypeDef]
    ) -> CreateExclusionsPreviewResponseTypeDef:
        """
        Starts the generation of an exclusions preview for the specified assessment
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/create_exclusions_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#create_exclusions_preview)
        """

    def create_resource_group(
        self, **kwargs: Unpack[CreateResourceGroupRequestTypeDef]
    ) -> CreateResourceGroupResponseTypeDef:
        """
        Creates a resource group using the specified set of tags (key and value pairs)
        that are used to select the EC2 instances to be included in an Amazon Inspector
        assessment target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/create_resource_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#create_resource_group)
        """

    def delete_assessment_run(
        self, **kwargs: Unpack[DeleteAssessmentRunRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the assessment run that is specified by the ARN of the assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/delete_assessment_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#delete_assessment_run)
        """

    def delete_assessment_target(
        self, **kwargs: Unpack[DeleteAssessmentTargetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the assessment target that is specified by the ARN of the assessment
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/delete_assessment_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#delete_assessment_target)
        """

    def delete_assessment_template(
        self, **kwargs: Unpack[DeleteAssessmentTemplateRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the assessment template that is specified by the ARN of the assessment
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/delete_assessment_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#delete_assessment_template)
        """

    def describe_assessment_runs(
        self, **kwargs: Unpack[DescribeAssessmentRunsRequestTypeDef]
    ) -> DescribeAssessmentRunsResponseTypeDef:
        """
        Describes the assessment runs that are specified by the ARNs of the assessment
        runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_assessment_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_assessment_runs)
        """

    def describe_assessment_targets(
        self, **kwargs: Unpack[DescribeAssessmentTargetsRequestTypeDef]
    ) -> DescribeAssessmentTargetsResponseTypeDef:
        """
        Describes the assessment targets that are specified by the ARNs of the
        assessment targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_assessment_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_assessment_targets)
        """

    def describe_assessment_templates(
        self, **kwargs: Unpack[DescribeAssessmentTemplatesRequestTypeDef]
    ) -> DescribeAssessmentTemplatesResponseTypeDef:
        """
        Describes the assessment templates that are specified by the ARNs of the
        assessment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_assessment_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_assessment_templates)
        """

    def describe_cross_account_access_role(self) -> DescribeCrossAccountAccessRoleResponseTypeDef:
        """
        Describes the IAM role that enables Amazon Inspector to access your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_cross_account_access_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_cross_account_access_role)
        """

    def describe_exclusions(
        self, **kwargs: Unpack[DescribeExclusionsRequestTypeDef]
    ) -> DescribeExclusionsResponseTypeDef:
        """
        Describes the exclusions that are specified by the exclusions' ARNs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_exclusions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_exclusions)
        """

    def describe_findings(
        self, **kwargs: Unpack[DescribeFindingsRequestTypeDef]
    ) -> DescribeFindingsResponseTypeDef:
        """
        Describes the findings that are specified by the ARNs of the findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_findings)
        """

    def describe_resource_groups(
        self, **kwargs: Unpack[DescribeResourceGroupsRequestTypeDef]
    ) -> DescribeResourceGroupsResponseTypeDef:
        """
        Describes the resource groups that are specified by the ARNs of the resource
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_resource_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_resource_groups)
        """

    def describe_rules_packages(
        self, **kwargs: Unpack[DescribeRulesPackagesRequestTypeDef]
    ) -> DescribeRulesPackagesResponseTypeDef:
        """
        Describes the rules packages that are specified by the ARNs of the rules
        packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/describe_rules_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#describe_rules_packages)
        """

    def get_assessment_report(
        self, **kwargs: Unpack[GetAssessmentReportRequestTypeDef]
    ) -> GetAssessmentReportResponseTypeDef:
        """
        Produces an assessment report that includes detailed and comprehensive results
        of a specified assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_assessment_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_assessment_report)
        """

    def get_exclusions_preview(
        self, **kwargs: Unpack[GetExclusionsPreviewRequestTypeDef]
    ) -> GetExclusionsPreviewResponseTypeDef:
        """
        Retrieves the exclusions preview (a list of ExclusionPreview objects) specified
        by the preview token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_exclusions_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_exclusions_preview)
        """

    def get_telemetry_metadata(
        self, **kwargs: Unpack[GetTelemetryMetadataRequestTypeDef]
    ) -> GetTelemetryMetadataResponseTypeDef:
        """
        Information about the data that is collected for the specified assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_telemetry_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_telemetry_metadata)
        """

    def list_assessment_run_agents(
        self, **kwargs: Unpack[ListAssessmentRunAgentsRequestTypeDef]
    ) -> ListAssessmentRunAgentsResponseTypeDef:
        """
        Lists the agents of the assessment runs that are specified by the ARNs of the
        assessment runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_assessment_run_agents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_assessment_run_agents)
        """

    def list_assessment_runs(
        self, **kwargs: Unpack[ListAssessmentRunsRequestTypeDef]
    ) -> ListAssessmentRunsResponseTypeDef:
        """
        Lists the assessment runs that correspond to the assessment templates that are
        specified by the ARNs of the assessment templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_assessment_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_assessment_runs)
        """

    def list_assessment_targets(
        self, **kwargs: Unpack[ListAssessmentTargetsRequestTypeDef]
    ) -> ListAssessmentTargetsResponseTypeDef:
        """
        Lists the ARNs of the assessment targets within this AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_assessment_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_assessment_targets)
        """

    def list_assessment_templates(
        self, **kwargs: Unpack[ListAssessmentTemplatesRequestTypeDef]
    ) -> ListAssessmentTemplatesResponseTypeDef:
        """
        Lists the assessment templates that correspond to the assessment targets that
        are specified by the ARNs of the assessment targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_assessment_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_assessment_templates)
        """

    def list_event_subscriptions(
        self, **kwargs: Unpack[ListEventSubscriptionsRequestTypeDef]
    ) -> ListEventSubscriptionsResponseTypeDef:
        """
        Lists all the event subscriptions for the assessment template that is specified
        by the ARN of the assessment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_event_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_event_subscriptions)
        """

    def list_exclusions(
        self, **kwargs: Unpack[ListExclusionsRequestTypeDef]
    ) -> ListExclusionsResponseTypeDef:
        """
        List exclusions that are generated by the assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_exclusions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_exclusions)
        """

    def list_findings(
        self, **kwargs: Unpack[ListFindingsRequestTypeDef]
    ) -> ListFindingsResponseTypeDef:
        """
        Lists findings that are generated by the assessment runs that are specified by
        the ARNs of the assessment runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_findings)
        """

    def list_rules_packages(
        self, **kwargs: Unpack[ListRulesPackagesRequestTypeDef]
    ) -> ListRulesPackagesResponseTypeDef:
        """
        Lists all available Amazon Inspector rules packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_rules_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_rules_packages)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with an assessment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#list_tags_for_resource)
        """

    def preview_agents(
        self, **kwargs: Unpack[PreviewAgentsRequestTypeDef]
    ) -> PreviewAgentsResponseTypeDef:
        """
        Previews the agents installed on the EC2 instances that are part of the
        specified assessment target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/preview_agents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#preview_agents)
        """

    def register_cross_account_access_role(
        self, **kwargs: Unpack[RegisterCrossAccountAccessRoleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Registers the IAM role that grants Amazon Inspector access to AWS Services
        needed to perform security assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/register_cross_account_access_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#register_cross_account_access_role)
        """

    def remove_attributes_from_findings(
        self, **kwargs: Unpack[RemoveAttributesFromFindingsRequestTypeDef]
    ) -> RemoveAttributesFromFindingsResponseTypeDef:
        """
        Removes entire attributes (key and value pairs) from the findings that are
        specified by the ARNs of the findings where an attribute with the specified key
        exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/remove_attributes_from_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#remove_attributes_from_findings)
        """

    def set_tags_for_resource(
        self, **kwargs: Unpack[SetTagsForResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets tags (key and value pairs) to the assessment template that is specified by
        the ARN of the assessment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/set_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#set_tags_for_resource)
        """

    def start_assessment_run(
        self, **kwargs: Unpack[StartAssessmentRunRequestTypeDef]
    ) -> StartAssessmentRunResponseTypeDef:
        """
        Starts the assessment run specified by the ARN of the assessment template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/start_assessment_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#start_assessment_run)
        """

    def stop_assessment_run(
        self, **kwargs: Unpack[StopAssessmentRunRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops the assessment run that is specified by the ARN of the assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/stop_assessment_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#stop_assessment_run)
        """

    def subscribe_to_event(
        self, **kwargs: Unpack[SubscribeToEventRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables the process of sending Amazon Simple Notification Service (SNS)
        notifications about a specified event to a specified SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/subscribe_to_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#subscribe_to_event)
        """

    def unsubscribe_from_event(
        self, **kwargs: Unpack[UnsubscribeFromEventRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables the process of sending Amazon Simple Notification Service (SNS)
        notifications about a specified event to a specified SNS topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/unsubscribe_from_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#unsubscribe_from_event)
        """

    def update_assessment_target(
        self, **kwargs: Unpack[UpdateAssessmentTargetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the assessment target that is specified by the ARN of the assessment
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/update_assessment_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#update_assessment_target)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assessment_run_agents"]
    ) -> ListAssessmentRunAgentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assessment_runs"]
    ) -> ListAssessmentRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assessment_targets"]
    ) -> ListAssessmentTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assessment_templates"]
    ) -> ListAssessmentTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_subscriptions"]
    ) -> ListEventSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_exclusions"]
    ) -> ListExclusionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_findings"]
    ) -> ListFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules_packages"]
    ) -> ListRulesPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["preview_agents"]
    ) -> PreviewAgentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/client/#get_paginator)
        """
