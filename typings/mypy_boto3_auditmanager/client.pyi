"""
Type annotations for auditmanager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_auditmanager import AuditManagerClient

    client: AuditManagerClient = boto3.client("auditmanager")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AssessmentStatusType,
    ControlSetStatusType,
    ControlStatusType,
    ControlTypeType,
    FrameworkTypeType,
    SettingAttributeType,
    ShareRequestActionType,
    ShareRequestTypeType,
    SourceTypeType,
)
from .type_defs import (
    AssessmentReportsDestinationTypeDef,
    BatchAssociateAssessmentReportEvidenceResponseTypeDef,
    BatchCreateDelegationByAssessmentResponseTypeDef,
    BatchDeleteDelegationByAssessmentResponseTypeDef,
    BatchDisassociateAssessmentReportEvidenceResponseTypeDef,
    BatchImportEvidenceToAssessmentControlResponseTypeDef,
    ControlMappingSourceTypeDef,
    CreateAssessmentFrameworkControlSetTypeDef,
    CreateAssessmentFrameworkResponseTypeDef,
    CreateAssessmentReportResponseTypeDef,
    CreateAssessmentResponseTypeDef,
    CreateControlMappingSourceTypeDef,
    CreateControlResponseTypeDef,
    CreateDelegationRequestTypeDef,
    DeregisterAccountResponseTypeDef,
    DeregistrationPolicyTypeDef,
    GetAccountStatusResponseTypeDef,
    GetAssessmentFrameworkResponseTypeDef,
    GetAssessmentReportUrlResponseTypeDef,
    GetAssessmentResponseTypeDef,
    GetChangeLogsResponseTypeDef,
    GetControlResponseTypeDef,
    GetDelegationsResponseTypeDef,
    GetEvidenceByEvidenceFolderResponseTypeDef,
    GetEvidenceFolderResponseTypeDef,
    GetEvidenceFoldersByAssessmentControlResponseTypeDef,
    GetEvidenceFoldersByAssessmentResponseTypeDef,
    GetEvidenceResponseTypeDef,
    GetInsightsByAssessmentResponseTypeDef,
    GetInsightsResponseTypeDef,
    GetOrganizationAdminAccountResponseTypeDef,
    GetServicesInScopeResponseTypeDef,
    GetSettingsResponseTypeDef,
    ListAssessmentControlInsightsByControlDomainResponseTypeDef,
    ListAssessmentFrameworkShareRequestsResponseTypeDef,
    ListAssessmentFrameworksResponseTypeDef,
    ListAssessmentReportsResponseTypeDef,
    ListAssessmentsResponseTypeDef,
    ListControlDomainInsightsByAssessmentResponseTypeDef,
    ListControlDomainInsightsResponseTypeDef,
    ListControlInsightsByControlDomainResponseTypeDef,
    ListControlsResponseTypeDef,
    ListKeywordsForDataSourceResponseTypeDef,
    ListNotificationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ManualEvidenceTypeDef,
    RegisterAccountResponseTypeDef,
    RegisterOrganizationAdminAccountResponseTypeDef,
    RoleTypeDef,
    ScopeTypeDef,
    StartAssessmentFrameworkShareResponseTypeDef,
    UpdateAssessmentControlResponseTypeDef,
    UpdateAssessmentControlSetStatusResponseTypeDef,
    UpdateAssessmentFrameworkControlSetTypeDef,
    UpdateAssessmentFrameworkResponseTypeDef,
    UpdateAssessmentFrameworkShareResponseTypeDef,
    UpdateAssessmentResponseTypeDef,
    UpdateAssessmentStatusResponseTypeDef,
    UpdateControlResponseTypeDef,
    UpdateSettingsResponseTypeDef,
    ValidateAssessmentReportIntegrityResponseTypeDef,
)

__all__ = ("AuditManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AuditManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AuditManagerClient exceptions.
        """
    def associate_assessment_report_evidence_folder(
        self, *, assessmentId: str, evidenceFolderId: str
    ) -> Dict[str, Any]:
        """
        Associates an evidence folder to an assessment report in an Audit Manager
        assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.associate_assessment_report_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#associate_assessment_report_evidence_folder)
        """
    def batch_associate_assessment_report_evidence(
        self, *, assessmentId: str, evidenceFolderId: str, evidenceIds: List[str]
    ) -> BatchAssociateAssessmentReportEvidenceResponseTypeDef:
        """
        Associates a list of evidence to an assessment report in an Audit Manager
        assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.batch_associate_assessment_report_evidence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_associate_assessment_report_evidence)
        """
    def batch_create_delegation_by_assessment(
        self, *, createDelegationRequests: List["CreateDelegationRequestTypeDef"], assessmentId: str
    ) -> BatchCreateDelegationByAssessmentResponseTypeDef:
        """
        Creates a batch of delegations for an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.batch_create_delegation_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_create_delegation_by_assessment)
        """
    def batch_delete_delegation_by_assessment(
        self, *, delegationIds: List[str], assessmentId: str
    ) -> BatchDeleteDelegationByAssessmentResponseTypeDef:
        """
        Deletes a batch of delegations for an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.batch_delete_delegation_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_delete_delegation_by_assessment)
        """
    def batch_disassociate_assessment_report_evidence(
        self, *, assessmentId: str, evidenceFolderId: str, evidenceIds: List[str]
    ) -> BatchDisassociateAssessmentReportEvidenceResponseTypeDef:
        """
        Disassociates a list of evidence from an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.batch_disassociate_assessment_report_evidence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_disassociate_assessment_report_evidence)
        """
    def batch_import_evidence_to_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        manualEvidence: List["ManualEvidenceTypeDef"]
    ) -> BatchImportEvidenceToAssessmentControlResponseTypeDef:
        """
        Uploads one or more pieces of evidence to a control in an Audit Manager
        assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.batch_import_evidence_to_assessment_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#batch_import_evidence_to_assessment_control)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#close)
        """
    def create_assessment(
        self,
        *,
        name: str,
        assessmentReportsDestination: "AssessmentReportsDestinationTypeDef",
        scope: "ScopeTypeDef",
        roles: List["RoleTypeDef"],
        frameworkId: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssessmentResponseTypeDef:
        """
        Creates an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.create_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_assessment)
        """
    def create_assessment_framework(
        self,
        *,
        name: str,
        controlSets: List["CreateAssessmentFrameworkControlSetTypeDef"],
        description: str = None,
        complianceType: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssessmentFrameworkResponseTypeDef:
        """
        Creates a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.create_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_assessment_framework)
        """
    def create_assessment_report(
        self, *, name: str, assessmentId: str, description: str = None, queryStatement: str = None
    ) -> CreateAssessmentReportResponseTypeDef:
        """
        Creates an assessment report for the specified assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.create_assessment_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_assessment_report)
        """
    def create_control(
        self,
        *,
        name: str,
        controlMappingSources: List["CreateControlMappingSourceTypeDef"],
        description: str = None,
        testingInformation: str = None,
        actionPlanTitle: str = None,
        actionPlanInstructions: str = None,
        tags: Dict[str, str] = None
    ) -> CreateControlResponseTypeDef:
        """
        Creates a new custom control in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.create_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#create_control)
        """
    def delete_assessment(self, *, assessmentId: str) -> Dict[str, Any]:
        """
        Deletes an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.delete_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment)
        """
    def delete_assessment_framework(self, *, frameworkId: str) -> Dict[str, Any]:
        """
        Deletes a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment_framework)
        """
    def delete_assessment_framework_share(
        self, *, requestId: str, requestType: ShareRequestTypeType
    ) -> Dict[str, Any]:
        """
        Deletes a share request for a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_framework_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment_framework_share)
        """
    def delete_assessment_report(
        self, *, assessmentId: str, assessmentReportId: str
    ) -> Dict[str, Any]:
        """
        Deletes an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_assessment_report)
        """
    def delete_control(self, *, controlId: str) -> Dict[str, Any]:
        """
        Deletes a custom control in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.delete_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#delete_control)
        """
    def deregister_account(self) -> DeregisterAccountResponseTypeDef:
        """
        Deregisters an account in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.deregister_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#deregister_account)
        """
    def deregister_organization_admin_account(
        self, *, adminAccountId: str = None
    ) -> Dict[str, Any]:
        """
        Removes the specified Amazon Web Services account as a delegated administrator
        for Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.deregister_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#deregister_organization_admin_account)
        """
    def disassociate_assessment_report_evidence_folder(
        self, *, assessmentId: str, evidenceFolderId: str
    ) -> Dict[str, Any]:
        """
        Disassociates an evidence folder from the specified assessment report in Audit
        Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.disassociate_assessment_report_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#disassociate_assessment_report_evidence_folder)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#generate_presigned_url)
        """
    def get_account_status(self) -> GetAccountStatusResponseTypeDef:
        """
        Returns the registration status of an account in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_account_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_account_status)
        """
    def get_assessment(self, *, assessmentId: str) -> GetAssessmentResponseTypeDef:
        """
        Returns an assessment from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_assessment)
        """
    def get_assessment_framework(
        self, *, frameworkId: str
    ) -> GetAssessmentFrameworkResponseTypeDef:
        """
        Returns a framework from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_assessment_framework)
        """
    def get_assessment_report_url(
        self, *, assessmentReportId: str, assessmentId: str
    ) -> GetAssessmentReportUrlResponseTypeDef:
        """
        Returns the URL of an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_assessment_report_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_assessment_report_url)
        """
    def get_change_logs(
        self,
        *,
        assessmentId: str,
        controlSetId: str = None,
        controlId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetChangeLogsResponseTypeDef:
        """
        Returns a list of changelogs from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_change_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_change_logs)
        """
    def get_control(self, *, controlId: str) -> GetControlResponseTypeDef:
        """
        Returns a control from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_control)
        """
    def get_delegations(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> GetDelegationsResponseTypeDef:
        """
        Returns a list of delegations from an audit owner to a delegate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_delegations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_delegations)
        """
    def get_evidence(
        self, *, assessmentId: str, controlSetId: str, evidenceFolderId: str, evidenceId: str
    ) -> GetEvidenceResponseTypeDef:
        """
        Returns evidence from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_evidence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence)
        """
    def get_evidence_by_evidence_folder(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        evidenceFolderId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetEvidenceByEvidenceFolderResponseTypeDef:
        """
        Returns all evidence from a specified evidence folder in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_evidence_by_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_by_evidence_folder)
        """
    def get_evidence_folder(
        self, *, assessmentId: str, controlSetId: str, evidenceFolderId: str
    ) -> GetEvidenceFolderResponseTypeDef:
        """
        Returns an evidence folder from the specified assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_folder)
        """
    def get_evidence_folders_by_assessment(
        self, *, assessmentId: str, nextToken: str = None, maxResults: int = None
    ) -> GetEvidenceFoldersByAssessmentResponseTypeDef:
        """
        Returns the evidence folders from a specified assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_folders_by_assessment)
        """
    def get_evidence_folders_by_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetEvidenceFoldersByAssessmentControlResponseTypeDef:
        """
        Returns a list of evidence folders that are associated with a specified control
        in an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_evidence_folders_by_assessment_control)
        """
    def get_insights(self) -> GetInsightsResponseTypeDef:
        """
        Gets the latest analytics data for all your current active assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_insights)
        """
    def get_insights_by_assessment(
        self, *, assessmentId: str
    ) -> GetInsightsByAssessmentResponseTypeDef:
        """
        Gets the latest analytics data for a specific active assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_insights_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_insights_by_assessment)
        """
    def get_organization_admin_account(self) -> GetOrganizationAdminAccountResponseTypeDef:
        """
        Returns the name of the delegated Amazon Web Services administrator account for
        the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_organization_admin_account)
        """
    def get_services_in_scope(self) -> GetServicesInScopeResponseTypeDef:
        """
        Returns a list of all of the Amazon Web Services that you can choose to include
        in your assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_services_in_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_services_in_scope)
        """
    def get_settings(self, *, attribute: SettingAttributeType) -> GetSettingsResponseTypeDef:
        """
        Returns the settings for the specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.get_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#get_settings)
        """
    def list_assessment_control_insights_by_control_domain(
        self,
        *,
        controlDomainId: str,
        assessmentId: str,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAssessmentControlInsightsByControlDomainResponseTypeDef:
        """
        Lists the latest analytics data for controls within a specific control domain
        and a specific active assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_assessment_control_insights_by_control_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessment_control_insights_by_control_domain)
        """
    def list_assessment_framework_share_requests(
        self, *, requestType: ShareRequestTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentFrameworkShareRequestsResponseTypeDef:
        """
        Returns a list of sent or received share requests for custom frameworks in Audit
        Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_assessment_framework_share_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessment_framework_share_requests)
        """
    def list_assessment_frameworks(
        self, *, frameworkType: FrameworkTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentFrameworksResponseTypeDef:
        """
        Returns a list of the frameworks that are available in the Audit Manager
        framework library.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_assessment_frameworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessment_frameworks)
        """
    def list_assessment_reports(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentReportsResponseTypeDef:
        """
        Returns a list of assessment reports created in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_assessment_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessment_reports)
        """
    def list_assessments(
        self, *, status: AssessmentStatusType = None, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentsResponseTypeDef:
        """
        Returns a list of current and past assessments from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_assessments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_assessments)
        """
    def list_control_domain_insights(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListControlDomainInsightsResponseTypeDef:
        """
        Lists the latest analytics data for control domains across all of your active
        assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_control_domain_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_control_domain_insights)
        """
    def list_control_domain_insights_by_assessment(
        self, *, assessmentId: str, nextToken: str = None, maxResults: int = None
    ) -> ListControlDomainInsightsByAssessmentResponseTypeDef:
        """
        Lists analytics data for control domains within a specified active assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_control_domain_insights_by_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_control_domain_insights_by_assessment)
        """
    def list_control_insights_by_control_domain(
        self, *, controlDomainId: str, nextToken: str = None, maxResults: int = None
    ) -> ListControlInsightsByControlDomainResponseTypeDef:
        """
        Lists the latest analytics data for controls within a specific control domain
        across all active assessments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_control_insights_by_control_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_control_insights_by_control_domain)
        """
    def list_controls(
        self, *, controlType: ControlTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListControlsResponseTypeDef:
        """
        Returns a list of controls from Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_controls)
        """
    def list_keywords_for_data_source(
        self, *, source: SourceTypeType, nextToken: str = None, maxResults: int = None
    ) -> ListKeywordsForDataSourceResponseTypeDef:
        """
        Returns a list of keywords that are pre-mapped to the specified control data
        source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_keywords_for_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_keywords_for_data_source)
        """
    def list_notifications(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListNotificationsResponseTypeDef:
        """
        Returns a list of all Audit Manager notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_notifications)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for the specified resource in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#list_tags_for_resource)
        """
    def register_account(
        self, *, kmsKey: str = None, delegatedAdminAccount: str = None
    ) -> RegisterAccountResponseTypeDef:
        """
        Enables Audit Manager for the specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.register_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#register_account)
        """
    def register_organization_admin_account(
        self, *, adminAccountId: str
    ) -> RegisterOrganizationAdminAccountResponseTypeDef:
        """
        Enables an Amazon Web Services account within the organization as the delegated
        administrator for Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.register_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#register_organization_admin_account)
        """
    def start_assessment_framework_share(
        self,
        *,
        frameworkId: str,
        destinationAccount: str,
        destinationRegion: str,
        comment: str = None
    ) -> StartAssessmentFrameworkShareResponseTypeDef:
        """
        Creates a share request for a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.start_assessment_framework_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#start_assessment_framework_share)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags the specified resource in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#untag_resource)
        """
    def update_assessment(
        self,
        *,
        assessmentId: str,
        scope: "ScopeTypeDef",
        assessmentName: str = None,
        assessmentDescription: str = None,
        assessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
        roles: List["RoleTypeDef"] = None
    ) -> UpdateAssessmentResponseTypeDef:
        """
        Edits an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment)
        """
    def update_assessment_control(
        self,
        *,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        controlStatus: ControlStatusType = None,
        commentBody: str = None
    ) -> UpdateAssessmentControlResponseTypeDef:
        """
        Updates a control within an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_control)
        """
    def update_assessment_control_set_status(
        self, *, assessmentId: str, controlSetId: str, status: ControlSetStatusType, comment: str
    ) -> UpdateAssessmentControlSetStatusResponseTypeDef:
        """
        Updates the status of a control set in an Audit Manager assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control_set_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_control_set_status)
        """
    def update_assessment_framework(
        self,
        *,
        frameworkId: str,
        name: str,
        controlSets: List["UpdateAssessmentFrameworkControlSetTypeDef"],
        description: str = None,
        complianceType: str = None
    ) -> UpdateAssessmentFrameworkResponseTypeDef:
        """
        Updates a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_assessment_framework)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_framework)
        """
    def update_assessment_framework_share(
        self, *, requestId: str, requestType: ShareRequestTypeType, action: ShareRequestActionType
    ) -> UpdateAssessmentFrameworkShareResponseTypeDef:
        """
        Updates a share request for a custom framework in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_assessment_framework_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_framework_share)
        """
    def update_assessment_status(
        self, *, assessmentId: str, status: AssessmentStatusType
    ) -> UpdateAssessmentStatusResponseTypeDef:
        """
        Updates the status of an assessment in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_assessment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_assessment_status)
        """
    def update_control(
        self,
        *,
        controlId: str,
        name: str,
        controlMappingSources: List["ControlMappingSourceTypeDef"],
        description: str = None,
        testingInformation: str = None,
        actionPlanTitle: str = None,
        actionPlanInstructions: str = None
    ) -> UpdateControlResponseTypeDef:
        """
        Updates a custom control in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_control)
        """
    def update_settings(
        self,
        *,
        snsTopic: str = None,
        defaultAssessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
        defaultProcessOwners: List["RoleTypeDef"] = None,
        kmsKey: str = None,
        evidenceFinderEnabled: bool = None,
        deregistrationPolicy: "DeregistrationPolicyTypeDef" = None
    ) -> UpdateSettingsResponseTypeDef:
        """
        Updates Audit Manager settings for the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.update_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#update_settings)
        """
    def validate_assessment_report_integrity(
        self, *, s3RelativePath: str
    ) -> ValidateAssessmentReportIntegrityResponseTypeDef:
        """
        Validates the integrity of an assessment report in Audit Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/auditmanager.html#AuditManager.Client.validate_assessment_report_integrity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/client.html#validate_assessment_report_integrity)
        """
