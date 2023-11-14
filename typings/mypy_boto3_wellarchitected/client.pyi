"""
Type annotations for wellarchitected service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_wellarchitected import WellArchitectedClient

    client: WellArchitectedClient = boto3.client("wellarchitected")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AnswerReasonType,
    DiscoveryIntegrationStatusType,
    LensStatusTypeType,
    LensTypeType,
    OrganizationSharingStatusType,
    PermissionTypeType,
    ProfileOwnerTypeType,
    QuestionPriorityType,
    ReportFormatType,
    ShareInvitationActionType,
    ShareResourceTypeType,
    ShareStatusType,
    WorkloadEnvironmentType,
    WorkloadImprovementStatusType,
)
from .type_defs import (
    ChoiceUpdateTypeDef,
    CreateLensShareOutputTypeDef,
    CreateLensVersionOutputTypeDef,
    CreateMilestoneOutputTypeDef,
    CreateProfileOutputTypeDef,
    CreateProfileShareOutputTypeDef,
    CreateReviewTemplateOutputTypeDef,
    CreateTemplateShareOutputTypeDef,
    CreateWorkloadOutputTypeDef,
    CreateWorkloadShareOutputTypeDef,
    ExportLensOutputTypeDef,
    GetAnswerOutputTypeDef,
    GetConsolidatedReportOutputTypeDef,
    GetLensOutputTypeDef,
    GetLensReviewOutputTypeDef,
    GetLensReviewReportOutputTypeDef,
    GetLensVersionDifferenceOutputTypeDef,
    GetMilestoneOutputTypeDef,
    GetProfileOutputTypeDef,
    GetProfileTemplateOutputTypeDef,
    GetReviewTemplateAnswerOutputTypeDef,
    GetReviewTemplateLensReviewOutputTypeDef,
    GetReviewTemplateOutputTypeDef,
    GetWorkloadOutputTypeDef,
    ImportLensOutputTypeDef,
    ListAnswersOutputTypeDef,
    ListCheckDetailsOutputTypeDef,
    ListCheckSummariesOutputTypeDef,
    ListLensesOutputTypeDef,
    ListLensReviewImprovementsOutputTypeDef,
    ListLensReviewsOutputTypeDef,
    ListLensSharesOutputTypeDef,
    ListMilestonesOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListProfileNotificationsOutputTypeDef,
    ListProfileSharesOutputTypeDef,
    ListProfilesOutputTypeDef,
    ListReviewTemplateAnswersOutputTypeDef,
    ListReviewTemplatesOutputTypeDef,
    ListShareInvitationsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTemplateSharesOutputTypeDef,
    ListWorkloadSharesOutputTypeDef,
    ListWorkloadsOutputTypeDef,
    ProfileQuestionUpdateTypeDef,
    UpdateAnswerOutputTypeDef,
    UpdateLensReviewOutputTypeDef,
    UpdateProfileOutputTypeDef,
    UpdateReviewTemplateAnswerOutputTypeDef,
    UpdateReviewTemplateLensReviewOutputTypeDef,
    UpdateReviewTemplateOutputTypeDef,
    UpdateShareInvitationOutputTypeDef,
    UpdateWorkloadOutputTypeDef,
    UpdateWorkloadShareOutputTypeDef,
    WorkloadDiscoveryConfigTypeDef,
)

__all__ = ("WellArchitectedClient",)

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

class WellArchitectedClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WellArchitectedClient exceptions.
        """
    def associate_lenses(self, *, WorkloadId: str, LensAliases: List[str]) -> None:
        """
        Associate a lens to a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.associate_lenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#associate_lenses)
        """
    def associate_profiles(self, *, WorkloadId: str, ProfileArns: List[str]) -> None:
        """
        Associate a profile with a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.associate_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#associate_profiles)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#close)
        """
    def create_lens_share(
        self, *, LensAlias: str, SharedWith: str, ClientRequestToken: str
    ) -> CreateLensShareOutputTypeDef:
        """
        Create a lens share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_lens_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_lens_share)
        """
    def create_lens_version(
        self,
        *,
        LensAlias: str,
        LensVersion: str,
        ClientRequestToken: str,
        IsMajorVersion: bool = None
    ) -> CreateLensVersionOutputTypeDef:
        """
        Create a new lens version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_lens_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_lens_version)
        """
    def create_milestone(
        self, *, WorkloadId: str, MilestoneName: str, ClientRequestToken: str
    ) -> CreateMilestoneOutputTypeDef:
        """
        Create a milestone for an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_milestone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_milestone)
        """
    def create_profile(
        self,
        *,
        ProfileName: str,
        ProfileDescription: str,
        ProfileQuestions: List["ProfileQuestionUpdateTypeDef"],
        ClientRequestToken: str,
        Tags: Dict[str, str] = None
    ) -> CreateProfileOutputTypeDef:
        """
        Create a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_profile)
        """
    def create_profile_share(
        self, *, ProfileArn: str, SharedWith: str, ClientRequestToken: str
    ) -> CreateProfileShareOutputTypeDef:
        """
        Create a profile share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_profile_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_profile_share)
        """
    def create_review_template(
        self,
        *,
        TemplateName: str,
        Description: str,
        Lenses: List[str],
        ClientRequestToken: str,
        Notes: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateReviewTemplateOutputTypeDef:
        """
        Create a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_review_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_review_template)
        """
    def create_template_share(
        self, *, TemplateArn: str, SharedWith: str, ClientRequestToken: str
    ) -> CreateTemplateShareOutputTypeDef:
        """
        Create a review template share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_template_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_template_share)
        """
    def create_workload(
        self,
        *,
        WorkloadName: str,
        Description: str,
        Environment: WorkloadEnvironmentType,
        Lenses: List[str],
        ClientRequestToken: str,
        AccountIds: List[str] = None,
        AwsRegions: List[str] = None,
        NonAwsRegions: List[str] = None,
        PillarPriorities: List[str] = None,
        ArchitecturalDesign: str = None,
        ReviewOwner: str = None,
        IndustryType: str = None,
        Industry: str = None,
        Notes: str = None,
        Tags: Dict[str, str] = None,
        DiscoveryConfig: "WorkloadDiscoveryConfigTypeDef" = None,
        Applications: List[str] = None,
        ProfileArns: List[str] = None,
        ReviewTemplateArns: List[str] = None
    ) -> CreateWorkloadOutputTypeDef:
        """
        Create a new workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_workload)
        """
    def create_workload_share(
        self,
        *,
        WorkloadId: str,
        SharedWith: str,
        PermissionType: PermissionTypeType,
        ClientRequestToken: str
    ) -> CreateWorkloadShareOutputTypeDef:
        """
        Create a workload share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.create_workload_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#create_workload_share)
        """
    def delete_lens(
        self, *, LensAlias: str, ClientRequestToken: str, LensStatus: LensStatusTypeType
    ) -> None:
        """
        Delete an existing lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_lens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_lens)
        """
    def delete_lens_share(self, *, ShareId: str, LensAlias: str, ClientRequestToken: str) -> None:
        """
        Delete a lens share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_lens_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_lens_share)
        """
    def delete_profile(self, *, ProfileArn: str, ClientRequestToken: str) -> None:
        """
        Delete a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_profile)
        """
    def delete_profile_share(
        self, *, ShareId: str, ProfileArn: str, ClientRequestToken: str
    ) -> None:
        """
        Delete a profile share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_profile_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_profile_share)
        """
    def delete_review_template(self, *, TemplateArn: str, ClientRequestToken: str) -> None:
        """
        Delete a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_review_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_review_template)
        """
    def delete_template_share(
        self, *, ShareId: str, TemplateArn: str, ClientRequestToken: str
    ) -> None:
        """
        Delete a review template share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_template_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_template_share)
        """
    def delete_workload(self, *, WorkloadId: str, ClientRequestToken: str) -> None:
        """
        Delete an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_workload)
        """
    def delete_workload_share(
        self, *, ShareId: str, WorkloadId: str, ClientRequestToken: str
    ) -> None:
        """
        Delete a workload share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.delete_workload_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#delete_workload_share)
        """
    def disassociate_lenses(self, *, WorkloadId: str, LensAliases: List[str]) -> None:
        """
        Disassociate a lens from a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.disassociate_lenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#disassociate_lenses)
        """
    def disassociate_profiles(self, *, WorkloadId: str, ProfileArns: List[str]) -> None:
        """
        Disassociate a profile from a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.disassociate_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#disassociate_profiles)
        """
    def export_lens(self, *, LensAlias: str, LensVersion: str = None) -> ExportLensOutputTypeDef:
        """
        Export an existing lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.export_lens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#export_lens)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#generate_presigned_url)
        """
    def get_answer(
        self, *, WorkloadId: str, LensAlias: str, QuestionId: str, MilestoneNumber: int = None
    ) -> GetAnswerOutputTypeDef:
        """
        Get the answer to a specific question in a workload review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_answer)
        """
    def get_consolidated_report(
        self,
        *,
        Format: ReportFormatType,
        IncludeSharedResources: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetConsolidatedReportOutputTypeDef:
        """
        Get a consolidated report of your workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_consolidated_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_consolidated_report)
        """
    def get_lens(self, *, LensAlias: str, LensVersion: str = None) -> GetLensOutputTypeDef:
        """
        Get an existing lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_lens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens)
        """
    def get_lens_review(
        self, *, WorkloadId: str, LensAlias: str, MilestoneNumber: int = None
    ) -> GetLensReviewOutputTypeDef:
        """
        Get lens review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens_review)
        """
    def get_lens_review_report(
        self, *, WorkloadId: str, LensAlias: str, MilestoneNumber: int = None
    ) -> GetLensReviewReportOutputTypeDef:
        """
        Get lens review report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_review_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens_review_report)
        """
    def get_lens_version_difference(
        self, *, LensAlias: str, BaseLensVersion: str = None, TargetLensVersion: str = None
    ) -> GetLensVersionDifferenceOutputTypeDef:
        """
        Get lens version differences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_lens_version_difference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_lens_version_difference)
        """
    def get_milestone(self, *, WorkloadId: str, MilestoneNumber: int) -> GetMilestoneOutputTypeDef:
        """
        Get a milestone for an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_milestone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_milestone)
        """
    def get_profile(
        self, *, ProfileArn: str, ProfileVersion: str = None
    ) -> GetProfileOutputTypeDef:
        """
        Get profile information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_profile)
        """
    def get_profile_template(self) -> GetProfileTemplateOutputTypeDef:
        """
        Get profile template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_profile_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_profile_template)
        """
    def get_review_template(self, *, TemplateArn: str) -> GetReviewTemplateOutputTypeDef:
        """
        Get review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_review_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_review_template)
        """
    def get_review_template_answer(
        self, *, TemplateArn: str, LensAlias: str, QuestionId: str
    ) -> GetReviewTemplateAnswerOutputTypeDef:
        """
        Get review template answer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_review_template_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_review_template_answer)
        """
    def get_review_template_lens_review(
        self, *, TemplateArn: str, LensAlias: str
    ) -> GetReviewTemplateLensReviewOutputTypeDef:
        """
        Get a lens review associated with a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_review_template_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_review_template_lens_review)
        """
    def get_workload(self, *, WorkloadId: str) -> GetWorkloadOutputTypeDef:
        """
        Get an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.get_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#get_workload)
        """
    def import_lens(
        self,
        *,
        JSONString: str,
        ClientRequestToken: str,
        LensAlias: str = None,
        Tags: Dict[str, str] = None
    ) -> ImportLensOutputTypeDef:
        """
        Import a new custom lens or update an existing custom lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.import_lens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#import_lens)
        """
    def list_answers(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        PillarId: str = None,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None,
        QuestionPriority: QuestionPriorityType = None
    ) -> ListAnswersOutputTypeDef:
        """
        List of answers for a particular workload and lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_answers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_answers)
        """
    def list_check_details(
        self,
        *,
        WorkloadId: str,
        LensArn: str,
        PillarId: str,
        QuestionId: str,
        ChoiceId: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCheckDetailsOutputTypeDef:
        """
        List of Trusted Advisor check details by account related to the workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_check_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_check_details)
        """
    def list_check_summaries(
        self,
        *,
        WorkloadId: str,
        LensArn: str,
        PillarId: str,
        QuestionId: str,
        ChoiceId: str,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListCheckSummariesOutputTypeDef:
        """
        List of Trusted Advisor checks summarized for all accounts related to the
        workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_check_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_check_summaries)
        """
    def list_lens_review_improvements(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        PillarId: str = None,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None,
        QuestionPriority: QuestionPriorityType = None
    ) -> ListLensReviewImprovementsOutputTypeDef:
        """
        List lens review improvements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_review_improvements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lens_review_improvements)
        """
    def list_lens_reviews(
        self,
        *,
        WorkloadId: str,
        MilestoneNumber: int = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLensReviewsOutputTypeDef:
        """
        List lens reviews for a particular workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_reviews)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lens_reviews)
        """
    def list_lens_shares(
        self,
        *,
        LensAlias: str,
        SharedWithPrefix: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ShareStatusType = None
    ) -> ListLensSharesOutputTypeDef:
        """
        List the lens shares associated with the lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_lens_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lens_shares)
        """
    def list_lenses(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        LensType: LensTypeType = None,
        LensStatus: LensStatusTypeType = None,
        LensName: str = None
    ) -> ListLensesOutputTypeDef:
        """
        List the available lenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_lenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_lenses)
        """
    def list_milestones(
        self, *, WorkloadId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMilestonesOutputTypeDef:
        """
        List all milestones for an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_milestones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_milestones)
        """
    def list_notifications(
        self,
        *,
        WorkloadId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        ResourceArn: str = None
    ) -> ListNotificationsOutputTypeDef:
        """
        List lens notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_notifications)
        """
    def list_profile_notifications(
        self, *, WorkloadId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListProfileNotificationsOutputTypeDef:
        """
        List profile notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_profile_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_profile_notifications)
        """
    def list_profile_shares(
        self,
        *,
        ProfileArn: str,
        SharedWithPrefix: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ShareStatusType = None
    ) -> ListProfileSharesOutputTypeDef:
        """
        List profile shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_profile_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_profile_shares)
        """
    def list_profiles(
        self,
        *,
        ProfileNamePrefix: str = None,
        ProfileOwnerType: ProfileOwnerTypeType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListProfilesOutputTypeDef:
        """
        List profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_profiles)
        """
    def list_review_template_answers(
        self,
        *,
        TemplateArn: str,
        LensAlias: str,
        PillarId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListReviewTemplateAnswersOutputTypeDef:
        """
        List the answers of a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_review_template_answers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_review_template_answers)
        """
    def list_review_templates(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListReviewTemplatesOutputTypeDef:
        """
        List review templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_review_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_review_templates)
        """
    def list_share_invitations(
        self,
        *,
        WorkloadNamePrefix: str = None,
        LensNamePrefix: str = None,
        ShareResourceType: ShareResourceTypeType = None,
        NextToken: str = None,
        MaxResults: int = None,
        ProfileNamePrefix: str = None,
        TemplateNamePrefix: str = None
    ) -> ListShareInvitationsOutputTypeDef:
        """
        List the share invitations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_share_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_share_invitations)
        """
    def list_tags_for_resource(self, *, WorkloadArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        List the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_tags_for_resource)
        """
    def list_template_shares(
        self,
        *,
        TemplateArn: str,
        SharedWithPrefix: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ShareStatusType = None
    ) -> ListTemplateSharesOutputTypeDef:
        """
        List review template shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_template_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_template_shares)
        """
    def list_workload_shares(
        self,
        *,
        WorkloadId: str,
        SharedWithPrefix: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ShareStatusType = None
    ) -> ListWorkloadSharesOutputTypeDef:
        """
        List the workload shares associated with the workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_workload_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_workload_shares)
        """
    def list_workloads(
        self, *, WorkloadNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListWorkloadsOutputTypeDef:
        """
        Paginated list of workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.list_workloads)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#list_workloads)
        """
    def tag_resource(self, *, WorkloadArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#tag_resource)
        """
    def untag_resource(self, *, WorkloadArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#untag_resource)
        """
    def update_answer(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        QuestionId: str,
        SelectedChoices: List[str] = None,
        ChoiceUpdates: Dict[str, "ChoiceUpdateTypeDef"] = None,
        Notes: str = None,
        IsApplicable: bool = None,
        Reason: AnswerReasonType = None
    ) -> UpdateAnswerOutputTypeDef:
        """
        Update the answer to a specific question in a workload review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_answer)
        """
    def update_global_settings(
        self,
        *,
        OrganizationSharingStatus: OrganizationSharingStatusType = None,
        DiscoveryIntegrationStatus: DiscoveryIntegrationStatusType = None
    ) -> None:
        """
        Updates whether the Amazon Web Services account is opted into organization
        sharing and discovery integration features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_global_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_global_settings)
        """
    def update_lens_review(
        self,
        *,
        WorkloadId: str,
        LensAlias: str,
        LensNotes: str = None,
        PillarNotes: Dict[str, str] = None
    ) -> UpdateLensReviewOutputTypeDef:
        """
        Update lens review for a particular workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_lens_review)
        """
    def update_profile(
        self,
        *,
        ProfileArn: str,
        ProfileDescription: str = None,
        ProfileQuestions: List["ProfileQuestionUpdateTypeDef"] = None
    ) -> UpdateProfileOutputTypeDef:
        """
        Update a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_profile)
        """
    def update_review_template(
        self,
        *,
        TemplateArn: str,
        TemplateName: str = None,
        Description: str = None,
        Notes: str = None,
        LensesToAssociate: List[str] = None,
        LensesToDisassociate: List[str] = None
    ) -> UpdateReviewTemplateOutputTypeDef:
        """
        Update a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_review_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_review_template)
        """
    def update_review_template_answer(
        self,
        *,
        TemplateArn: str,
        LensAlias: str,
        QuestionId: str,
        SelectedChoices: List[str] = None,
        ChoiceUpdates: Dict[str, "ChoiceUpdateTypeDef"] = None,
        Notes: str = None,
        IsApplicable: bool = None,
        Reason: AnswerReasonType = None
    ) -> UpdateReviewTemplateAnswerOutputTypeDef:
        """
        Update a review template answer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_review_template_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_review_template_answer)
        """
    def update_review_template_lens_review(
        self,
        *,
        TemplateArn: str,
        LensAlias: str,
        LensNotes: str = None,
        PillarNotes: Dict[str, str] = None
    ) -> UpdateReviewTemplateLensReviewOutputTypeDef:
        """
        Update a lens review associated with a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_review_template_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_review_template_lens_review)
        """
    def update_share_invitation(
        self, *, ShareInvitationId: str, ShareInvitationAction: ShareInvitationActionType
    ) -> UpdateShareInvitationOutputTypeDef:
        """
        Update a workload or custom lens share invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_share_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_share_invitation)
        """
    def update_workload(
        self,
        *,
        WorkloadId: str,
        WorkloadName: str = None,
        Description: str = None,
        Environment: WorkloadEnvironmentType = None,
        AccountIds: List[str] = None,
        AwsRegions: List[str] = None,
        NonAwsRegions: List[str] = None,
        PillarPriorities: List[str] = None,
        ArchitecturalDesign: str = None,
        ReviewOwner: str = None,
        IsReviewOwnerUpdateAcknowledged: bool = None,
        IndustryType: str = None,
        Industry: str = None,
        Notes: str = None,
        ImprovementStatus: WorkloadImprovementStatusType = None,
        DiscoveryConfig: "WorkloadDiscoveryConfigTypeDef" = None,
        Applications: List[str] = None
    ) -> UpdateWorkloadOutputTypeDef:
        """
        Update an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_workload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_workload)
        """
    def update_workload_share(
        self, *, ShareId: str, WorkloadId: str, PermissionType: PermissionTypeType
    ) -> UpdateWorkloadShareOutputTypeDef:
        """
        Update a workload share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.update_workload_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#update_workload_share)
        """
    def upgrade_lens_review(
        self, *, WorkloadId: str, LensAlias: str, MilestoneName: str, ClientRequestToken: str = None
    ) -> None:
        """
        Upgrade lens review for a particular workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.upgrade_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#upgrade_lens_review)
        """
    def upgrade_profile_version(
        self,
        *,
        WorkloadId: str,
        ProfileArn: str,
        MilestoneName: str = None,
        ClientRequestToken: str = None
    ) -> None:
        """
        Upgrade a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.upgrade_profile_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#upgrade_profile_version)
        """
    def upgrade_review_template_lens_review(
        self, *, TemplateArn: str, LensAlias: str, ClientRequestToken: str = None
    ) -> None:
        """
        Upgrade the lens review of a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/wellarchitected.html#WellArchitected.Client.upgrade_review_template_lens_review)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client.html#upgrade_review_template_lens_review)
        """
