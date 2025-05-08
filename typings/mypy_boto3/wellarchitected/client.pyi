"""
Type annotations for wellarchitected service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_wellarchitected.client import WellArchitectedClient

    session = Session()
    client: WellArchitectedClient = session.client("wellarchitected")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AssociateLensesInputTypeDef,
    AssociateProfilesInputTypeDef,
    CreateLensShareInputTypeDef,
    CreateLensShareOutputTypeDef,
    CreateLensVersionInputTypeDef,
    CreateLensVersionOutputTypeDef,
    CreateMilestoneInputTypeDef,
    CreateMilestoneOutputTypeDef,
    CreateProfileInputTypeDef,
    CreateProfileOutputTypeDef,
    CreateProfileShareInputTypeDef,
    CreateProfileShareOutputTypeDef,
    CreateReviewTemplateInputTypeDef,
    CreateReviewTemplateOutputTypeDef,
    CreateTemplateShareInputTypeDef,
    CreateTemplateShareOutputTypeDef,
    CreateWorkloadInputTypeDef,
    CreateWorkloadOutputTypeDef,
    CreateWorkloadShareInputTypeDef,
    CreateWorkloadShareOutputTypeDef,
    DeleteLensInputTypeDef,
    DeleteLensShareInputTypeDef,
    DeleteProfileInputTypeDef,
    DeleteProfileShareInputTypeDef,
    DeleteReviewTemplateInputTypeDef,
    DeleteTemplateShareInputTypeDef,
    DeleteWorkloadInputTypeDef,
    DeleteWorkloadShareInputTypeDef,
    DisassociateLensesInputTypeDef,
    DisassociateProfilesInputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportLensInputTypeDef,
    ExportLensOutputTypeDef,
    GetAnswerInputTypeDef,
    GetAnswerOutputTypeDef,
    GetConsolidatedReportInputTypeDef,
    GetConsolidatedReportOutputTypeDef,
    GetGlobalSettingsOutputTypeDef,
    GetLensInputTypeDef,
    GetLensOutputTypeDef,
    GetLensReviewInputTypeDef,
    GetLensReviewOutputTypeDef,
    GetLensReviewReportInputTypeDef,
    GetLensReviewReportOutputTypeDef,
    GetLensVersionDifferenceInputTypeDef,
    GetLensVersionDifferenceOutputTypeDef,
    GetMilestoneInputTypeDef,
    GetMilestoneOutputTypeDef,
    GetProfileInputTypeDef,
    GetProfileOutputTypeDef,
    GetProfileTemplateOutputTypeDef,
    GetReviewTemplateAnswerInputTypeDef,
    GetReviewTemplateAnswerOutputTypeDef,
    GetReviewTemplateInputTypeDef,
    GetReviewTemplateLensReviewInputTypeDef,
    GetReviewTemplateLensReviewOutputTypeDef,
    GetReviewTemplateOutputTypeDef,
    GetWorkloadInputTypeDef,
    GetWorkloadOutputTypeDef,
    ImportLensInputTypeDef,
    ImportLensOutputTypeDef,
    ListAnswersInputTypeDef,
    ListAnswersOutputTypeDef,
    ListCheckDetailsInputTypeDef,
    ListCheckDetailsOutputTypeDef,
    ListCheckSummariesInputTypeDef,
    ListCheckSummariesOutputTypeDef,
    ListLensesInputTypeDef,
    ListLensesOutputTypeDef,
    ListLensReviewImprovementsInputTypeDef,
    ListLensReviewImprovementsOutputTypeDef,
    ListLensReviewsInputTypeDef,
    ListLensReviewsOutputTypeDef,
    ListLensSharesInputTypeDef,
    ListLensSharesOutputTypeDef,
    ListMilestonesInputTypeDef,
    ListMilestonesOutputTypeDef,
    ListNotificationsInputTypeDef,
    ListNotificationsOutputTypeDef,
    ListProfileNotificationsInputTypeDef,
    ListProfileNotificationsOutputTypeDef,
    ListProfileSharesInputTypeDef,
    ListProfileSharesOutputTypeDef,
    ListProfilesInputTypeDef,
    ListProfilesOutputTypeDef,
    ListReviewTemplateAnswersInputTypeDef,
    ListReviewTemplateAnswersOutputTypeDef,
    ListReviewTemplatesInputTypeDef,
    ListReviewTemplatesOutputTypeDef,
    ListShareInvitationsInputTypeDef,
    ListShareInvitationsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTemplateSharesInputTypeDef,
    ListTemplateSharesOutputTypeDef,
    ListWorkloadSharesInputTypeDef,
    ListWorkloadSharesOutputTypeDef,
    ListWorkloadsInputTypeDef,
    ListWorkloadsOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateAnswerInputTypeDef,
    UpdateAnswerOutputTypeDef,
    UpdateGlobalSettingsInputTypeDef,
    UpdateIntegrationInputTypeDef,
    UpdateLensReviewInputTypeDef,
    UpdateLensReviewOutputTypeDef,
    UpdateProfileInputTypeDef,
    UpdateProfileOutputTypeDef,
    UpdateReviewTemplateAnswerInputTypeDef,
    UpdateReviewTemplateAnswerOutputTypeDef,
    UpdateReviewTemplateInputTypeDef,
    UpdateReviewTemplateLensReviewInputTypeDef,
    UpdateReviewTemplateLensReviewOutputTypeDef,
    UpdateReviewTemplateOutputTypeDef,
    UpdateShareInvitationInputTypeDef,
    UpdateShareInvitationOutputTypeDef,
    UpdateWorkloadInputTypeDef,
    UpdateWorkloadOutputTypeDef,
    UpdateWorkloadShareInputTypeDef,
    UpdateWorkloadShareOutputTypeDef,
    UpgradeLensReviewInputTypeDef,
    UpgradeProfileVersionInputTypeDef,
    UpgradeReviewTemplateLensReviewInputTypeDef,
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

__all__ = ("WellArchitectedClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WellArchitectedClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected.html#WellArchitected.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#generate_presigned_url)
        """

    def associate_lenses(
        self, **kwargs: Unpack[AssociateLensesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associate a lens to a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/associate_lenses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#associate_lenses)
        """

    def associate_profiles(
        self, **kwargs: Unpack[AssociateProfilesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associate a profile with a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/associate_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#associate_profiles)
        """

    def create_lens_share(
        self, **kwargs: Unpack[CreateLensShareInputTypeDef]
    ) -> CreateLensShareOutputTypeDef:
        """
        Create a lens share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_lens_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_lens_share)
        """

    def create_lens_version(
        self, **kwargs: Unpack[CreateLensVersionInputTypeDef]
    ) -> CreateLensVersionOutputTypeDef:
        """
        Create a new lens version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_lens_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_lens_version)
        """

    def create_milestone(
        self, **kwargs: Unpack[CreateMilestoneInputTypeDef]
    ) -> CreateMilestoneOutputTypeDef:
        """
        Create a milestone for an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_milestone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_milestone)
        """

    def create_profile(
        self, **kwargs: Unpack[CreateProfileInputTypeDef]
    ) -> CreateProfileOutputTypeDef:
        """
        Create a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_profile)
        """

    def create_profile_share(
        self, **kwargs: Unpack[CreateProfileShareInputTypeDef]
    ) -> CreateProfileShareOutputTypeDef:
        """
        Create a profile share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_profile_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_profile_share)
        """

    def create_review_template(
        self, **kwargs: Unpack[CreateReviewTemplateInputTypeDef]
    ) -> CreateReviewTemplateOutputTypeDef:
        """
        Create a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_review_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_review_template)
        """

    def create_template_share(
        self, **kwargs: Unpack[CreateTemplateShareInputTypeDef]
    ) -> CreateTemplateShareOutputTypeDef:
        """
        Create a review template share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_template_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_template_share)
        """

    def create_workload(
        self, **kwargs: Unpack[CreateWorkloadInputTypeDef]
    ) -> CreateWorkloadOutputTypeDef:
        """
        Create a new workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_workload)
        """

    def create_workload_share(
        self, **kwargs: Unpack[CreateWorkloadShareInputTypeDef]
    ) -> CreateWorkloadShareOutputTypeDef:
        """
        Create a workload share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/create_workload_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#create_workload_share)
        """

    def delete_lens(self, **kwargs: Unpack[DeleteLensInputTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Delete an existing lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_lens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_lens)
        """

    def delete_lens_share(
        self, **kwargs: Unpack[DeleteLensShareInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a lens share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_lens_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_lens_share)
        """

    def delete_profile(
        self, **kwargs: Unpack[DeleteProfileInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_profile)
        """

    def delete_profile_share(
        self, **kwargs: Unpack[DeleteProfileShareInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a profile share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_profile_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_profile_share)
        """

    def delete_review_template(
        self, **kwargs: Unpack[DeleteReviewTemplateInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_review_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_review_template)
        """

    def delete_template_share(
        self, **kwargs: Unpack[DeleteTemplateShareInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a review template share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_template_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_template_share)
        """

    def delete_workload(
        self, **kwargs: Unpack[DeleteWorkloadInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_workload)
        """

    def delete_workload_share(
        self, **kwargs: Unpack[DeleteWorkloadShareInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a workload share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/delete_workload_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#delete_workload_share)
        """

    def disassociate_lenses(
        self, **kwargs: Unpack[DisassociateLensesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociate a lens from a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/disassociate_lenses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#disassociate_lenses)
        """

    def disassociate_profiles(
        self, **kwargs: Unpack[DisassociateProfilesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociate a profile from a workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/disassociate_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#disassociate_profiles)
        """

    def export_lens(self, **kwargs: Unpack[ExportLensInputTypeDef]) -> ExportLensOutputTypeDef:
        """
        Export an existing lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/export_lens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#export_lens)
        """

    def get_answer(self, **kwargs: Unpack[GetAnswerInputTypeDef]) -> GetAnswerOutputTypeDef:
        """
        Get the answer to a specific question in a workload review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_answer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_answer)
        """

    def get_consolidated_report(
        self, **kwargs: Unpack[GetConsolidatedReportInputTypeDef]
    ) -> GetConsolidatedReportOutputTypeDef:
        """
        Get a consolidated report of your workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_consolidated_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_consolidated_report)
        """

    def get_global_settings(self) -> GetGlobalSettingsOutputTypeDef:
        """
        Global settings for all workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_global_settings)
        """

    def get_lens(self, **kwargs: Unpack[GetLensInputTypeDef]) -> GetLensOutputTypeDef:
        """
        Get an existing lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_lens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_lens)
        """

    def get_lens_review(
        self, **kwargs: Unpack[GetLensReviewInputTypeDef]
    ) -> GetLensReviewOutputTypeDef:
        """
        Get lens review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_lens_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_lens_review)
        """

    def get_lens_review_report(
        self, **kwargs: Unpack[GetLensReviewReportInputTypeDef]
    ) -> GetLensReviewReportOutputTypeDef:
        """
        Get lens review report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_lens_review_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_lens_review_report)
        """

    def get_lens_version_difference(
        self, **kwargs: Unpack[GetLensVersionDifferenceInputTypeDef]
    ) -> GetLensVersionDifferenceOutputTypeDef:
        """
        Get lens version differences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_lens_version_difference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_lens_version_difference)
        """

    def get_milestone(
        self, **kwargs: Unpack[GetMilestoneInputTypeDef]
    ) -> GetMilestoneOutputTypeDef:
        """
        Get a milestone for an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_milestone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_milestone)
        """

    def get_profile(self, **kwargs: Unpack[GetProfileInputTypeDef]) -> GetProfileOutputTypeDef:
        """
        Get profile information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_profile)
        """

    def get_profile_template(self) -> GetProfileTemplateOutputTypeDef:
        """
        Get profile template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_profile_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_profile_template)
        """

    def get_review_template(
        self, **kwargs: Unpack[GetReviewTemplateInputTypeDef]
    ) -> GetReviewTemplateOutputTypeDef:
        """
        Get review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_review_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_review_template)
        """

    def get_review_template_answer(
        self, **kwargs: Unpack[GetReviewTemplateAnswerInputTypeDef]
    ) -> GetReviewTemplateAnswerOutputTypeDef:
        """
        Get review template answer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_review_template_answer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_review_template_answer)
        """

    def get_review_template_lens_review(
        self, **kwargs: Unpack[GetReviewTemplateLensReviewInputTypeDef]
    ) -> GetReviewTemplateLensReviewOutputTypeDef:
        """
        Get a lens review associated with a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_review_template_lens_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_review_template_lens_review)
        """

    def get_workload(self, **kwargs: Unpack[GetWorkloadInputTypeDef]) -> GetWorkloadOutputTypeDef:
        """
        Get an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/get_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#get_workload)
        """

    def import_lens(self, **kwargs: Unpack[ImportLensInputTypeDef]) -> ImportLensOutputTypeDef:
        """
        Import a new custom lens or update an existing custom lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/import_lens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#import_lens)
        """

    def list_answers(self, **kwargs: Unpack[ListAnswersInputTypeDef]) -> ListAnswersOutputTypeDef:
        """
        List of answers for a particular workload and lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_answers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_answers)
        """

    def list_check_details(
        self, **kwargs: Unpack[ListCheckDetailsInputTypeDef]
    ) -> ListCheckDetailsOutputTypeDef:
        """
        List of Trusted Advisor check details by account related to the workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_check_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_check_details)
        """

    def list_check_summaries(
        self, **kwargs: Unpack[ListCheckSummariesInputTypeDef]
    ) -> ListCheckSummariesOutputTypeDef:
        """
        List of Trusted Advisor checks summarized for all accounts related to the
        workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_check_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_check_summaries)
        """

    def list_lens_review_improvements(
        self, **kwargs: Unpack[ListLensReviewImprovementsInputTypeDef]
    ) -> ListLensReviewImprovementsOutputTypeDef:
        """
        List the improvements of a particular lens review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_lens_review_improvements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_lens_review_improvements)
        """

    def list_lens_reviews(
        self, **kwargs: Unpack[ListLensReviewsInputTypeDef]
    ) -> ListLensReviewsOutputTypeDef:
        """
        List lens reviews for a particular workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_lens_reviews.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_lens_reviews)
        """

    def list_lens_shares(
        self, **kwargs: Unpack[ListLensSharesInputTypeDef]
    ) -> ListLensSharesOutputTypeDef:
        """
        List the lens shares associated with the lens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_lens_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_lens_shares)
        """

    def list_lenses(self, **kwargs: Unpack[ListLensesInputTypeDef]) -> ListLensesOutputTypeDef:
        """
        List the available lenses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_lenses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_lenses)
        """

    def list_milestones(
        self, **kwargs: Unpack[ListMilestonesInputTypeDef]
    ) -> ListMilestonesOutputTypeDef:
        """
        List all milestones for an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_milestones.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_milestones)
        """

    def list_notifications(
        self, **kwargs: Unpack[ListNotificationsInputTypeDef]
    ) -> ListNotificationsOutputTypeDef:
        """
        List lens notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_notifications)
        """

    def list_profile_notifications(
        self, **kwargs: Unpack[ListProfileNotificationsInputTypeDef]
    ) -> ListProfileNotificationsOutputTypeDef:
        """
        List profile notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_profile_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_profile_notifications)
        """

    def list_profile_shares(
        self, **kwargs: Unpack[ListProfileSharesInputTypeDef]
    ) -> ListProfileSharesOutputTypeDef:
        """
        List profile shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_profile_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_profile_shares)
        """

    def list_profiles(
        self, **kwargs: Unpack[ListProfilesInputTypeDef]
    ) -> ListProfilesOutputTypeDef:
        """
        List profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_profiles)
        """

    def list_review_template_answers(
        self, **kwargs: Unpack[ListReviewTemplateAnswersInputTypeDef]
    ) -> ListReviewTemplateAnswersOutputTypeDef:
        """
        List the answers of a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_review_template_answers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_review_template_answers)
        """

    def list_review_templates(
        self, **kwargs: Unpack[ListReviewTemplatesInputTypeDef]
    ) -> ListReviewTemplatesOutputTypeDef:
        """
        List review templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_review_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_review_templates)
        """

    def list_share_invitations(
        self, **kwargs: Unpack[ListShareInvitationsInputTypeDef]
    ) -> ListShareInvitationsOutputTypeDef:
        """
        List the share invitations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_share_invitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_share_invitations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_tags_for_resource)
        """

    def list_template_shares(
        self, **kwargs: Unpack[ListTemplateSharesInputTypeDef]
    ) -> ListTemplateSharesOutputTypeDef:
        """
        List review template shares.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_template_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_template_shares)
        """

    def list_workload_shares(
        self, **kwargs: Unpack[ListWorkloadSharesInputTypeDef]
    ) -> ListWorkloadSharesOutputTypeDef:
        """
        List the workload shares associated with the workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_workload_shares.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_workload_shares)
        """

    def list_workloads(
        self, **kwargs: Unpack[ListWorkloadsInputTypeDef]
    ) -> ListWorkloadsOutputTypeDef:
        """
        Paginated list of workloads.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/list_workloads.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#list_workloads)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#untag_resource)
        """

    def update_answer(
        self, **kwargs: Unpack[UpdateAnswerInputTypeDef]
    ) -> UpdateAnswerOutputTypeDef:
        """
        Update the answer to a specific question in a workload review.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_answer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_answer)
        """

    def update_global_settings(
        self, **kwargs: Unpack[UpdateGlobalSettingsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update whether the Amazon Web Services account is opted into organization
        sharing and discovery integration features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_global_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_global_settings)
        """

    def update_integration(
        self, **kwargs: Unpack[UpdateIntegrationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update integration features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_integration)
        """

    def update_lens_review(
        self, **kwargs: Unpack[UpdateLensReviewInputTypeDef]
    ) -> UpdateLensReviewOutputTypeDef:
        """
        Update lens review for a particular workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_lens_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_lens_review)
        """

    def update_profile(
        self, **kwargs: Unpack[UpdateProfileInputTypeDef]
    ) -> UpdateProfileOutputTypeDef:
        """
        Update a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_profile)
        """

    def update_review_template(
        self, **kwargs: Unpack[UpdateReviewTemplateInputTypeDef]
    ) -> UpdateReviewTemplateOutputTypeDef:
        """
        Update a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_review_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_review_template)
        """

    def update_review_template_answer(
        self, **kwargs: Unpack[UpdateReviewTemplateAnswerInputTypeDef]
    ) -> UpdateReviewTemplateAnswerOutputTypeDef:
        """
        Update a review template answer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_review_template_answer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_review_template_answer)
        """

    def update_review_template_lens_review(
        self, **kwargs: Unpack[UpdateReviewTemplateLensReviewInputTypeDef]
    ) -> UpdateReviewTemplateLensReviewOutputTypeDef:
        """
        Update a lens review associated with a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_review_template_lens_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_review_template_lens_review)
        """

    def update_share_invitation(
        self, **kwargs: Unpack[UpdateShareInvitationInputTypeDef]
    ) -> UpdateShareInvitationOutputTypeDef:
        """
        Update a workload or custom lens share invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_share_invitation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_share_invitation)
        """

    def update_workload(
        self, **kwargs: Unpack[UpdateWorkloadInputTypeDef]
    ) -> UpdateWorkloadOutputTypeDef:
        """
        Update an existing workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_workload)
        """

    def update_workload_share(
        self, **kwargs: Unpack[UpdateWorkloadShareInputTypeDef]
    ) -> UpdateWorkloadShareOutputTypeDef:
        """
        Update a workload share.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/update_workload_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#update_workload_share)
        """

    def upgrade_lens_review(
        self, **kwargs: Unpack[UpgradeLensReviewInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Upgrade lens review for a particular workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/upgrade_lens_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#upgrade_lens_review)
        """

    def upgrade_profile_version(
        self, **kwargs: Unpack[UpgradeProfileVersionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Upgrade a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/upgrade_profile_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#upgrade_profile_version)
        """

    def upgrade_review_template_lens_review(
        self, **kwargs: Unpack[UpgradeReviewTemplateLensReviewInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Upgrade the lens review of a review template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wellarchitected/client/upgrade_review_template_lens_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/client/#upgrade_review_template_lens_review)
        """
