"""
Type annotations for auditmanager service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_auditmanager.client import AuditManagerClient

    session = Session()
    client: AuditManagerClient = session.client("auditmanager")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AssociateAssessmentReportEvidenceFolderRequestTypeDef,
    BatchAssociateAssessmentReportEvidenceRequestTypeDef,
    BatchAssociateAssessmentReportEvidenceResponseTypeDef,
    BatchCreateDelegationByAssessmentRequestTypeDef,
    BatchCreateDelegationByAssessmentResponseTypeDef,
    BatchDeleteDelegationByAssessmentRequestTypeDef,
    BatchDeleteDelegationByAssessmentResponseTypeDef,
    BatchDisassociateAssessmentReportEvidenceRequestTypeDef,
    BatchDisassociateAssessmentReportEvidenceResponseTypeDef,
    BatchImportEvidenceToAssessmentControlRequestTypeDef,
    BatchImportEvidenceToAssessmentControlResponseTypeDef,
    CreateAssessmentFrameworkRequestTypeDef,
    CreateAssessmentFrameworkResponseTypeDef,
    CreateAssessmentReportRequestTypeDef,
    CreateAssessmentReportResponseTypeDef,
    CreateAssessmentRequestTypeDef,
    CreateAssessmentResponseTypeDef,
    CreateControlRequestTypeDef,
    CreateControlResponseTypeDef,
    DeleteAssessmentFrameworkRequestTypeDef,
    DeleteAssessmentFrameworkShareRequestTypeDef,
    DeleteAssessmentReportRequestTypeDef,
    DeleteAssessmentRequestTypeDef,
    DeleteControlRequestTypeDef,
    DeregisterAccountResponseTypeDef,
    DeregisterOrganizationAdminAccountRequestTypeDef,
    DisassociateAssessmentReportEvidenceFolderRequestTypeDef,
    GetAccountStatusResponseTypeDef,
    GetAssessmentFrameworkRequestTypeDef,
    GetAssessmentFrameworkResponseTypeDef,
    GetAssessmentReportUrlRequestTypeDef,
    GetAssessmentReportUrlResponseTypeDef,
    GetAssessmentRequestTypeDef,
    GetAssessmentResponseTypeDef,
    GetChangeLogsRequestTypeDef,
    GetChangeLogsResponseTypeDef,
    GetControlRequestTypeDef,
    GetControlResponseTypeDef,
    GetDelegationsRequestTypeDef,
    GetDelegationsResponseTypeDef,
    GetEvidenceByEvidenceFolderRequestTypeDef,
    GetEvidenceByEvidenceFolderResponseTypeDef,
    GetEvidenceFileUploadUrlRequestTypeDef,
    GetEvidenceFileUploadUrlResponseTypeDef,
    GetEvidenceFolderRequestTypeDef,
    GetEvidenceFolderResponseTypeDef,
    GetEvidenceFoldersByAssessmentControlRequestTypeDef,
    GetEvidenceFoldersByAssessmentControlResponseTypeDef,
    GetEvidenceFoldersByAssessmentRequestTypeDef,
    GetEvidenceFoldersByAssessmentResponseTypeDef,
    GetEvidenceRequestTypeDef,
    GetEvidenceResponseTypeDef,
    GetInsightsByAssessmentRequestTypeDef,
    GetInsightsByAssessmentResponseTypeDef,
    GetInsightsResponseTypeDef,
    GetOrganizationAdminAccountResponseTypeDef,
    GetServicesInScopeResponseTypeDef,
    GetSettingsRequestTypeDef,
    GetSettingsResponseTypeDef,
    ListAssessmentControlInsightsByControlDomainRequestTypeDef,
    ListAssessmentControlInsightsByControlDomainResponseTypeDef,
    ListAssessmentFrameworkShareRequestsRequestTypeDef,
    ListAssessmentFrameworkShareRequestsResponseTypeDef,
    ListAssessmentFrameworksRequestTypeDef,
    ListAssessmentFrameworksResponseTypeDef,
    ListAssessmentReportsRequestTypeDef,
    ListAssessmentReportsResponseTypeDef,
    ListAssessmentsRequestTypeDef,
    ListAssessmentsResponseTypeDef,
    ListControlDomainInsightsByAssessmentRequestTypeDef,
    ListControlDomainInsightsByAssessmentResponseTypeDef,
    ListControlDomainInsightsRequestTypeDef,
    ListControlDomainInsightsResponseTypeDef,
    ListControlInsightsByControlDomainRequestTypeDef,
    ListControlInsightsByControlDomainResponseTypeDef,
    ListControlsRequestTypeDef,
    ListControlsResponseTypeDef,
    ListKeywordsForDataSourceRequestTypeDef,
    ListKeywordsForDataSourceResponseTypeDef,
    ListNotificationsRequestTypeDef,
    ListNotificationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterAccountRequestTypeDef,
    RegisterAccountResponseTypeDef,
    RegisterOrganizationAdminAccountRequestTypeDef,
    RegisterOrganizationAdminAccountResponseTypeDef,
    StartAssessmentFrameworkShareRequestTypeDef,
    StartAssessmentFrameworkShareResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAssessmentControlRequestTypeDef,
    UpdateAssessmentControlResponseTypeDef,
    UpdateAssessmentControlSetStatusRequestTypeDef,
    UpdateAssessmentControlSetStatusResponseTypeDef,
    UpdateAssessmentFrameworkRequestTypeDef,
    UpdateAssessmentFrameworkResponseTypeDef,
    UpdateAssessmentFrameworkShareRequestTypeDef,
    UpdateAssessmentFrameworkShareResponseTypeDef,
    UpdateAssessmentRequestTypeDef,
    UpdateAssessmentResponseTypeDef,
    UpdateAssessmentStatusRequestTypeDef,
    UpdateAssessmentStatusResponseTypeDef,
    UpdateControlRequestTypeDef,
    UpdateControlResponseTypeDef,
    UpdateSettingsRequestTypeDef,
    UpdateSettingsResponseTypeDef,
    ValidateAssessmentReportIntegrityRequestTypeDef,
    ValidateAssessmentReportIntegrityResponseTypeDef,
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

__all__ = ("AuditManagerClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AuditManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AuditManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager.html#AuditManager.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#generate_presigned_url)
        """

    def associate_assessment_report_evidence_folder(
        self, **kwargs: Unpack[AssociateAssessmentReportEvidenceFolderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an evidence folder to an assessment report in an Audit Manager
        assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/associate_assessment_report_evidence_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#associate_assessment_report_evidence_folder)
        """

    def batch_associate_assessment_report_evidence(
        self, **kwargs: Unpack[BatchAssociateAssessmentReportEvidenceRequestTypeDef]
    ) -> BatchAssociateAssessmentReportEvidenceResponseTypeDef:
        """
        Associates a list of evidence to an assessment report in an Audit Manager
        assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/batch_associate_assessment_report_evidence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#batch_associate_assessment_report_evidence)
        """

    def batch_create_delegation_by_assessment(
        self, **kwargs: Unpack[BatchCreateDelegationByAssessmentRequestTypeDef]
    ) -> BatchCreateDelegationByAssessmentResponseTypeDef:
        """
        Creates a batch of delegations for an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/batch_create_delegation_by_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#batch_create_delegation_by_assessment)
        """

    def batch_delete_delegation_by_assessment(
        self, **kwargs: Unpack[BatchDeleteDelegationByAssessmentRequestTypeDef]
    ) -> BatchDeleteDelegationByAssessmentResponseTypeDef:
        """
        Deletes a batch of delegations for an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/batch_delete_delegation_by_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#batch_delete_delegation_by_assessment)
        """

    def batch_disassociate_assessment_report_evidence(
        self, **kwargs: Unpack[BatchDisassociateAssessmentReportEvidenceRequestTypeDef]
    ) -> BatchDisassociateAssessmentReportEvidenceResponseTypeDef:
        """
        Disassociates a list of evidence from an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/batch_disassociate_assessment_report_evidence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#batch_disassociate_assessment_report_evidence)
        """

    def batch_import_evidence_to_assessment_control(
        self, **kwargs: Unpack[BatchImportEvidenceToAssessmentControlRequestTypeDef]
    ) -> BatchImportEvidenceToAssessmentControlResponseTypeDef:
        """
        Adds one or more pieces of evidence to a control in an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/batch_import_evidence_to_assessment_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#batch_import_evidence_to_assessment_control)
        """

    def create_assessment(
        self, **kwargs: Unpack[CreateAssessmentRequestTypeDef]
    ) -> CreateAssessmentResponseTypeDef:
        """
        Creates an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/create_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#create_assessment)
        """

    def create_assessment_framework(
        self, **kwargs: Unpack[CreateAssessmentFrameworkRequestTypeDef]
    ) -> CreateAssessmentFrameworkResponseTypeDef:
        """
        Creates a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/create_assessment_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#create_assessment_framework)
        """

    def create_assessment_report(
        self, **kwargs: Unpack[CreateAssessmentReportRequestTypeDef]
    ) -> CreateAssessmentReportResponseTypeDef:
        """
        Creates an assessment report for the specified assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/create_assessment_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#create_assessment_report)
        """

    def create_control(
        self, **kwargs: Unpack[CreateControlRequestTypeDef]
    ) -> CreateControlResponseTypeDef:
        """
        Creates a new custom control in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/create_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#create_control)
        """

    def delete_assessment(self, **kwargs: Unpack[DeleteAssessmentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/delete_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#delete_assessment)
        """

    def delete_assessment_framework(
        self, **kwargs: Unpack[DeleteAssessmentFrameworkRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/delete_assessment_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#delete_assessment_framework)
        """

    def delete_assessment_framework_share(
        self, **kwargs: Unpack[DeleteAssessmentFrameworkShareRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a share request for a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/delete_assessment_framework_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#delete_assessment_framework_share)
        """

    def delete_assessment_report(
        self, **kwargs: Unpack[DeleteAssessmentReportRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/delete_assessment_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#delete_assessment_report)
        """

    def delete_control(self, **kwargs: Unpack[DeleteControlRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a custom control in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/delete_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#delete_control)
        """

    def deregister_account(self) -> DeregisterAccountResponseTypeDef:
        """
        Deregisters an account in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/deregister_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#deregister_account)
        """

    def deregister_organization_admin_account(
        self, **kwargs: Unpack[DeregisterOrganizationAdminAccountRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified Amazon Web Services account as a delegated administrator
        for Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/deregister_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#deregister_organization_admin_account)
        """

    def disassociate_assessment_report_evidence_folder(
        self, **kwargs: Unpack[DisassociateAssessmentReportEvidenceFolderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates an evidence folder from the specified assessment report in Audit
        Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/disassociate_assessment_report_evidence_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#disassociate_assessment_report_evidence_folder)
        """

    def get_account_status(self) -> GetAccountStatusResponseTypeDef:
        """
        Gets the registration status of an account in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_account_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_account_status)
        """

    def get_assessment(
        self, **kwargs: Unpack[GetAssessmentRequestTypeDef]
    ) -> GetAssessmentResponseTypeDef:
        """
        Gets information about a specified assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_assessment)
        """

    def get_assessment_framework(
        self, **kwargs: Unpack[GetAssessmentFrameworkRequestTypeDef]
    ) -> GetAssessmentFrameworkResponseTypeDef:
        """
        Gets information about a specified framework.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_assessment_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_assessment_framework)
        """

    def get_assessment_report_url(
        self, **kwargs: Unpack[GetAssessmentReportUrlRequestTypeDef]
    ) -> GetAssessmentReportUrlResponseTypeDef:
        """
        Gets the URL of an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_assessment_report_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_assessment_report_url)
        """

    def get_change_logs(
        self, **kwargs: Unpack[GetChangeLogsRequestTypeDef]
    ) -> GetChangeLogsResponseTypeDef:
        """
        Gets a list of changelogs from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_change_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_change_logs)
        """

    def get_control(self, **kwargs: Unpack[GetControlRequestTypeDef]) -> GetControlResponseTypeDef:
        """
        Gets information about a specified control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_control)
        """

    def get_delegations(
        self, **kwargs: Unpack[GetDelegationsRequestTypeDef]
    ) -> GetDelegationsResponseTypeDef:
        """
        Gets a list of delegations from an audit owner to a delegate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_delegations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_delegations)
        """

    def get_evidence(
        self, **kwargs: Unpack[GetEvidenceRequestTypeDef]
    ) -> GetEvidenceResponseTypeDef:
        """
        Gets information about a specified evidence item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_evidence.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_evidence)
        """

    def get_evidence_by_evidence_folder(
        self, **kwargs: Unpack[GetEvidenceByEvidenceFolderRequestTypeDef]
    ) -> GetEvidenceByEvidenceFolderResponseTypeDef:
        """
        Gets all evidence from a specified evidence folder in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_evidence_by_evidence_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_evidence_by_evidence_folder)
        """

    def get_evidence_file_upload_url(
        self, **kwargs: Unpack[GetEvidenceFileUploadUrlRequestTypeDef]
    ) -> GetEvidenceFileUploadUrlResponseTypeDef:
        """
        Creates a presigned Amazon S3 URL that can be used to upload a file as manual
        evidence.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_evidence_file_upload_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_evidence_file_upload_url)
        """

    def get_evidence_folder(
        self, **kwargs: Unpack[GetEvidenceFolderRequestTypeDef]
    ) -> GetEvidenceFolderResponseTypeDef:
        """
        Gets an evidence folder from a specified assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_evidence_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_evidence_folder)
        """

    def get_evidence_folders_by_assessment(
        self, **kwargs: Unpack[GetEvidenceFoldersByAssessmentRequestTypeDef]
    ) -> GetEvidenceFoldersByAssessmentResponseTypeDef:
        """
        Gets the evidence folders from a specified assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_evidence_folders_by_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_evidence_folders_by_assessment)
        """

    def get_evidence_folders_by_assessment_control(
        self, **kwargs: Unpack[GetEvidenceFoldersByAssessmentControlRequestTypeDef]
    ) -> GetEvidenceFoldersByAssessmentControlResponseTypeDef:
        """
        Gets a list of evidence folders that are associated with a specified control in
        an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_evidence_folders_by_assessment_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_evidence_folders_by_assessment_control)
        """

    def get_insights(self) -> GetInsightsResponseTypeDef:
        """
        Gets the latest analytics data for all your current active assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_insights)
        """

    def get_insights_by_assessment(
        self, **kwargs: Unpack[GetInsightsByAssessmentRequestTypeDef]
    ) -> GetInsightsByAssessmentResponseTypeDef:
        """
        Gets the latest analytics data for a specific active assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_insights_by_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_insights_by_assessment)
        """

    def get_organization_admin_account(self) -> GetOrganizationAdminAccountResponseTypeDef:
        """
        Gets the name of the delegated Amazon Web Services administrator account for a
        specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_organization_admin_account)
        """

    def get_services_in_scope(self) -> GetServicesInScopeResponseTypeDef:
        """
        Gets a list of the Amazon Web Services from which Audit Manager can collect
        evidence.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_services_in_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_services_in_scope)
        """

    def get_settings(
        self, **kwargs: Unpack[GetSettingsRequestTypeDef]
    ) -> GetSettingsResponseTypeDef:
        """
        Gets the settings for a specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/get_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#get_settings)
        """

    def list_assessment_control_insights_by_control_domain(
        self, **kwargs: Unpack[ListAssessmentControlInsightsByControlDomainRequestTypeDef]
    ) -> ListAssessmentControlInsightsByControlDomainResponseTypeDef:
        """
        Lists the latest analytics data for controls within a specific control domain
        and a specific active assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_assessment_control_insights_by_control_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_assessment_control_insights_by_control_domain)
        """

    def list_assessment_framework_share_requests(
        self, **kwargs: Unpack[ListAssessmentFrameworkShareRequestsRequestTypeDef]
    ) -> ListAssessmentFrameworkShareRequestsResponseTypeDef:
        """
        Returns a list of sent or received share requests for custom frameworks in
        Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_assessment_framework_share_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_assessment_framework_share_requests)
        """

    def list_assessment_frameworks(
        self, **kwargs: Unpack[ListAssessmentFrameworksRequestTypeDef]
    ) -> ListAssessmentFrameworksResponseTypeDef:
        """
        Returns a list of the frameworks that are available in the Audit Manager
        framework library.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_assessment_frameworks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_assessment_frameworks)
        """

    def list_assessment_reports(
        self, **kwargs: Unpack[ListAssessmentReportsRequestTypeDef]
    ) -> ListAssessmentReportsResponseTypeDef:
        """
        Returns a list of assessment reports created in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_assessment_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_assessment_reports)
        """

    def list_assessments(
        self, **kwargs: Unpack[ListAssessmentsRequestTypeDef]
    ) -> ListAssessmentsResponseTypeDef:
        """
        Returns a list of current and past assessments from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_assessments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_assessments)
        """

    def list_control_domain_insights(
        self, **kwargs: Unpack[ListControlDomainInsightsRequestTypeDef]
    ) -> ListControlDomainInsightsResponseTypeDef:
        """
        Lists the latest analytics data for control domains across all of your active
        assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_control_domain_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_control_domain_insights)
        """

    def list_control_domain_insights_by_assessment(
        self, **kwargs: Unpack[ListControlDomainInsightsByAssessmentRequestTypeDef]
    ) -> ListControlDomainInsightsByAssessmentResponseTypeDef:
        """
        Lists analytics data for control domains within a specified active assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_control_domain_insights_by_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_control_domain_insights_by_assessment)
        """

    def list_control_insights_by_control_domain(
        self, **kwargs: Unpack[ListControlInsightsByControlDomainRequestTypeDef]
    ) -> ListControlInsightsByControlDomainResponseTypeDef:
        """
        Lists the latest analytics data for controls within a specific control domain
        across all active assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_control_insights_by_control_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_control_insights_by_control_domain)
        """

    def list_controls(
        self, **kwargs: Unpack[ListControlsRequestTypeDef]
    ) -> ListControlsResponseTypeDef:
        """
        Returns a list of controls from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_controls)
        """

    def list_keywords_for_data_source(
        self, **kwargs: Unpack[ListKeywordsForDataSourceRequestTypeDef]
    ) -> ListKeywordsForDataSourceResponseTypeDef:
        """
        Returns a list of keywords that are pre-mapped to the specified control data
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_keywords_for_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_keywords_for_data_source)
        """

    def list_notifications(
        self, **kwargs: Unpack[ListNotificationsRequestTypeDef]
    ) -> ListNotificationsResponseTypeDef:
        """
        Returns a list of all Audit Manager notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_notifications)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for the specified resource in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#list_tags_for_resource)
        """

    def register_account(
        self, **kwargs: Unpack[RegisterAccountRequestTypeDef]
    ) -> RegisterAccountResponseTypeDef:
        """
        Enables Audit Manager for the specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/register_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#register_account)
        """

    def register_organization_admin_account(
        self, **kwargs: Unpack[RegisterOrganizationAdminAccountRequestTypeDef]
    ) -> RegisterOrganizationAdminAccountResponseTypeDef:
        """
        Enables an Amazon Web Services account within the organization as the delegated
        administrator for Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/register_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#register_organization_admin_account)
        """

    def start_assessment_framework_share(
        self, **kwargs: Unpack[StartAssessmentFrameworkShareRequestTypeDef]
    ) -> StartAssessmentFrameworkShareResponseTypeDef:
        """
        Creates a share request for a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/start_assessment_framework_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#start_assessment_framework_share)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags the specified resource in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a resource in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#untag_resource)
        """

    def update_assessment(
        self, **kwargs: Unpack[UpdateAssessmentRequestTypeDef]
    ) -> UpdateAssessmentResponseTypeDef:
        """
        Edits an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_assessment)
        """

    def update_assessment_control(
        self, **kwargs: Unpack[UpdateAssessmentControlRequestTypeDef]
    ) -> UpdateAssessmentControlResponseTypeDef:
        """
        Updates a control within an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_assessment_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_assessment_control)
        """

    def update_assessment_control_set_status(
        self, **kwargs: Unpack[UpdateAssessmentControlSetStatusRequestTypeDef]
    ) -> UpdateAssessmentControlSetStatusResponseTypeDef:
        """
        Updates the status of a control set in an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_assessment_control_set_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_assessment_control_set_status)
        """

    def update_assessment_framework(
        self, **kwargs: Unpack[UpdateAssessmentFrameworkRequestTypeDef]
    ) -> UpdateAssessmentFrameworkResponseTypeDef:
        """
        Updates a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_assessment_framework.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_assessment_framework)
        """

    def update_assessment_framework_share(
        self, **kwargs: Unpack[UpdateAssessmentFrameworkShareRequestTypeDef]
    ) -> UpdateAssessmentFrameworkShareResponseTypeDef:
        """
        Updates a share request for a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_assessment_framework_share.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_assessment_framework_share)
        """

    def update_assessment_status(
        self, **kwargs: Unpack[UpdateAssessmentStatusRequestTypeDef]
    ) -> UpdateAssessmentStatusResponseTypeDef:
        """
        Updates the status of an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_assessment_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_assessment_status)
        """

    def update_control(
        self, **kwargs: Unpack[UpdateControlRequestTypeDef]
    ) -> UpdateControlResponseTypeDef:
        """
        Updates a custom control in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_control)
        """

    def update_settings(
        self, **kwargs: Unpack[UpdateSettingsRequestTypeDef]
    ) -> UpdateSettingsResponseTypeDef:
        """
        Updates Audit Manager settings for the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/update_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#update_settings)
        """

    def validate_assessment_report_integrity(
        self, **kwargs: Unpack[ValidateAssessmentReportIntegrityRequestTypeDef]
    ) -> ValidateAssessmentReportIntegrityResponseTypeDef:
        """
        Validates the integrity of an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/auditmanager/client/validate_assessment_report_integrity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client/#validate_assessment_report_integrity)
        """
