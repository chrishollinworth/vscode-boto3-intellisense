# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for inspector service client

Usage::

    ```python
    import boto3
    from mypy_boto3_inspector import InspectorClient

    client: InspectorClient = boto3.client("inspector")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_inspector.paginator import (
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
from mypy_boto3_inspector.type_defs import (
    AddAttributesToFindingsResponseTypeDef,
    AgentFilterTypeDef,
    AssessmentRunFilterTypeDef,
    AssessmentTargetFilterTypeDef,
    AssessmentTemplateFilterTypeDef,
    AttributeTypeDef,
    CreateAssessmentTargetResponseTypeDef,
    CreateAssessmentTemplateResponseTypeDef,
    CreateExclusionsPreviewResponseTypeDef,
    CreateResourceGroupResponseTypeDef,
    DescribeAssessmentRunsResponseTypeDef,
    DescribeAssessmentTargetsResponseTypeDef,
    DescribeAssessmentTemplatesResponseTypeDef,
    DescribeCrossAccountAccessRoleResponseTypeDef,
    DescribeExclusionsResponseTypeDef,
    DescribeFindingsResponseTypeDef,
    DescribeResourceGroupsResponseTypeDef,
    DescribeRulesPackagesResponseTypeDef,
    FindingFilterTypeDef,
    GetAssessmentReportResponseTypeDef,
    GetExclusionsPreviewResponseTypeDef,
    GetTelemetryMetadataResponseTypeDef,
    ListAssessmentRunAgentsResponseTypeDef,
    ListAssessmentRunsResponseTypeDef,
    ListAssessmentTargetsResponseTypeDef,
    ListAssessmentTemplatesResponseTypeDef,
    ListEventSubscriptionsResponseTypeDef,
    ListExclusionsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListRulesPackagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PreviewAgentsResponseTypeDef,
    RemoveAttributesFromFindingsResponseTypeDef,
    ResourceGroupTagTypeDef,
    StartAssessmentRunResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("InspectorClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    AgentsAlreadyRunningAssessmentException: Type[Boto3ClientError]
    AssessmentRunInProgressException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InternalException: Type[Boto3ClientError]
    InvalidCrossAccountRoleException: Type[Boto3ClientError]
    InvalidInputException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NoSuchEntityException: Type[Boto3ClientError]
    PreviewGenerationInProgressException: Type[Boto3ClientError]
    ServiceTemporarilyUnavailableException: Type[Boto3ClientError]
    UnsupportedFeatureException: Type[Boto3ClientError]


class InspectorClient:
    """
    [Inspector.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client)
    """

    exceptions: Exceptions

    def add_attributes_to_findings(
        self, findingArns: List[str], attributes: List["AttributeTypeDef"]
    ) -> AddAttributesToFindingsResponseTypeDef:
        """
        [Client.add_attributes_to_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.add_attributes_to_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.can_paginate)
        """

    def create_assessment_target(
        self, assessmentTargetName: str, resourceGroupArn: str = None
    ) -> CreateAssessmentTargetResponseTypeDef:
        """
        [Client.create_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.create_assessment_target)
        """

    def create_assessment_template(
        self,
        assessmentTargetArn: str,
        assessmentTemplateName: str,
        durationInSeconds: int,
        rulesPackageArns: List[str],
        userAttributesForFindings: List["AttributeTypeDef"] = None,
    ) -> CreateAssessmentTemplateResponseTypeDef:
        """
        [Client.create_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.create_assessment_template)
        """

    def create_exclusions_preview(
        self, assessmentTemplateArn: str
    ) -> CreateExclusionsPreviewResponseTypeDef:
        """
        [Client.create_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.create_exclusions_preview)
        """

    def create_resource_group(
        self, resourceGroupTags: List["ResourceGroupTagTypeDef"]
    ) -> CreateResourceGroupResponseTypeDef:
        """
        [Client.create_resource_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.create_resource_group)
        """

    def delete_assessment_run(self, assessmentRunArn: str) -> None:
        """
        [Client.delete_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.delete_assessment_run)
        """

    def delete_assessment_target(self, assessmentTargetArn: str) -> None:
        """
        [Client.delete_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.delete_assessment_target)
        """

    def delete_assessment_template(self, assessmentTemplateArn: str) -> None:
        """
        [Client.delete_assessment_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.delete_assessment_template)
        """

    def describe_assessment_runs(
        self, assessmentRunArns: List[str]
    ) -> DescribeAssessmentRunsResponseTypeDef:
        """
        [Client.describe_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_assessment_runs)
        """

    def describe_assessment_targets(
        self, assessmentTargetArns: List[str]
    ) -> DescribeAssessmentTargetsResponseTypeDef:
        """
        [Client.describe_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_assessment_targets)
        """

    def describe_assessment_templates(
        self, assessmentTemplateArns: List[str]
    ) -> DescribeAssessmentTemplatesResponseTypeDef:
        """
        [Client.describe_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_assessment_templates)
        """

    def describe_cross_account_access_role(self) -> DescribeCrossAccountAccessRoleResponseTypeDef:
        """
        [Client.describe_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_cross_account_access_role)
        """

    def describe_exclusions(
        self, exclusionArns: List[str], locale: Literal["EN_US"] = None
    ) -> DescribeExclusionsResponseTypeDef:
        """
        [Client.describe_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_exclusions)
        """

    def describe_findings(
        self, findingArns: List[str], locale: Literal["EN_US"] = None
    ) -> DescribeFindingsResponseTypeDef:
        """
        [Client.describe_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_findings)
        """

    def describe_resource_groups(
        self, resourceGroupArns: List[str]
    ) -> DescribeResourceGroupsResponseTypeDef:
        """
        [Client.describe_resource_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_resource_groups)
        """

    def describe_rules_packages(
        self, rulesPackageArns: List[str], locale: Literal["EN_US"] = None
    ) -> DescribeRulesPackagesResponseTypeDef:
        """
        [Client.describe_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.describe_rules_packages)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.generate_presigned_url)
        """

    def get_assessment_report(
        self,
        assessmentRunArn: str,
        reportFileFormat: Literal["HTML", "PDF"],
        reportType: Literal["FINDING", "FULL"],
    ) -> GetAssessmentReportResponseTypeDef:
        """
        [Client.get_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.get_assessment_report)
        """

    def get_exclusions_preview(
        self,
        assessmentTemplateArn: str,
        previewToken: str,
        nextToken: str = None,
        maxResults: int = None,
        locale: Literal["EN_US"] = None,
    ) -> GetExclusionsPreviewResponseTypeDef:
        """
        [Client.get_exclusions_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.get_exclusions_preview)
        """

    def get_telemetry_metadata(self, assessmentRunArn: str) -> GetTelemetryMetadataResponseTypeDef:
        """
        [Client.get_telemetry_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.get_telemetry_metadata)
        """

    def list_assessment_run_agents(
        self,
        assessmentRunArn: str,
        filter: AgentFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentRunAgentsResponseTypeDef:
        """
        [Client.list_assessment_run_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_assessment_run_agents)
        """

    def list_assessment_runs(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: AssessmentRunFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentRunsResponseTypeDef:
        """
        [Client.list_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_assessment_runs)
        """

    def list_assessment_targets(
        self,
        filter: AssessmentTargetFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentTargetsResponseTypeDef:
        """
        [Client.list_assessment_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_assessment_targets)
        """

    def list_assessment_templates(
        self,
        assessmentTargetArns: List[str] = None,
        filter: AssessmentTemplateFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentTemplatesResponseTypeDef:
        """
        [Client.list_assessment_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_assessment_templates)
        """

    def list_event_subscriptions(
        self, resourceArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListEventSubscriptionsResponseTypeDef:
        """
        [Client.list_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_event_subscriptions)
        """

    def list_exclusions(
        self, assessmentRunArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListExclusionsResponseTypeDef:
        """
        [Client.list_exclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_exclusions)
        """

    def list_findings(
        self,
        assessmentRunArns: List[str] = None,
        filter: FindingFilterTypeDef = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_findings)
        """

    def list_rules_packages(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListRulesPackagesResponseTypeDef:
        """
        [Client.list_rules_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_rules_packages)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.list_tags_for_resource)
        """

    def preview_agents(
        self, previewAgentsArn: str, nextToken: str = None, maxResults: int = None
    ) -> PreviewAgentsResponseTypeDef:
        """
        [Client.preview_agents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.preview_agents)
        """

    def register_cross_account_access_role(self, roleArn: str) -> None:
        """
        [Client.register_cross_account_access_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.register_cross_account_access_role)
        """

    def remove_attributes_from_findings(
        self, findingArns: List[str], attributeKeys: List[str]
    ) -> RemoveAttributesFromFindingsResponseTypeDef:
        """
        [Client.remove_attributes_from_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.remove_attributes_from_findings)
        """

    def set_tags_for_resource(self, resourceArn: str, tags: List["TagTypeDef"] = None) -> None:
        """
        [Client.set_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.set_tags_for_resource)
        """

    def start_assessment_run(
        self, assessmentTemplateArn: str, assessmentRunName: str = None
    ) -> StartAssessmentRunResponseTypeDef:
        """
        [Client.start_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.start_assessment_run)
        """

    def stop_assessment_run(
        self,
        assessmentRunArn: str,
        stopAction: Literal["START_EVALUATION", "SKIP_EVALUATION"] = None,
    ) -> None:
        """
        [Client.stop_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.stop_assessment_run)
        """

    def subscribe_to_event(
        self,
        resourceArn: str,
        event: Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        topicArn: str,
    ) -> None:
        """
        [Client.subscribe_to_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.subscribe_to_event)
        """

    def unsubscribe_from_event(
        self,
        resourceArn: str,
        event: Literal[
            "ASSESSMENT_RUN_STARTED",
            "ASSESSMENT_RUN_COMPLETED",
            "ASSESSMENT_RUN_STATE_CHANGED",
            "FINDING_REPORTED",
            "OTHER",
        ],
        topicArn: str,
    ) -> None:
        """
        [Client.unsubscribe_from_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.unsubscribe_from_event)
        """

    def update_assessment_target(
        self, assessmentTargetArn: str, assessmentTargetName: str, resourceGroupArn: str = None
    ) -> None:
        """
        [Client.update_assessment_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Client.update_assessment_target)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_run_agents"]
    ) -> ListAssessmentRunAgentsPaginator:
        """
        [Paginator.ListAssessmentRunAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_runs"]
    ) -> ListAssessmentRunsPaginator:
        """
        [Paginator.ListAssessmentRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_targets"]
    ) -> ListAssessmentTargetsPaginator:
        """
        [Paginator.ListAssessmentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assessment_templates"]
    ) -> ListAssessmentTemplatesPaginator:
        """
        [Paginator.ListAssessmentTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_subscriptions"]
    ) -> ListEventSubscriptionsPaginator:
        """
        [Paginator.ListEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_exclusions"]) -> ListExclusionsPaginator:
        """
        [Paginator.ListExclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListExclusions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rules_packages"]
    ) -> ListRulesPackagesPaginator:
        """
        [Paginator.ListRulesPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages)
        """

    @overload
    def get_paginator(self, operation_name: Literal["preview_agents"]) -> PreviewAgentsPaginator:
        """
        [Paginator.PreviewAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/inspector.html#Inspector.Paginator.PreviewAgents)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
