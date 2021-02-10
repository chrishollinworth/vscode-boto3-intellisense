"""
Main interface for auditmanager service client

Usage::

    ```python
    import boto3
    from mypy_boto3_auditmanager import AuditManagerClient

    client: AuditManagerClient = boto3.client("auditmanager")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_auditmanager.type_defs import (
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
    GetOrganizationAdminAccountResponseTypeDef,
    GetServicesInScopeResponseTypeDef,
    GetSettingsResponseTypeDef,
    ListAssessmentFrameworksResponseTypeDef,
    ListAssessmentReportsResponseTypeDef,
    ListAssessmentsResponseTypeDef,
    ListControlsResponseTypeDef,
    ListKeywordsForDataSourceResponseTypeDef,
    ListNotificationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ManualEvidenceTypeDef,
    RegisterAccountResponseTypeDef,
    RegisterOrganizationAdminAccountResponseTypeDef,
    RoleTypeDef,
    ScopeTypeDef,
    UpdateAssessmentControlResponseTypeDef,
    UpdateAssessmentControlSetStatusResponseTypeDef,
    UpdateAssessmentFrameworkControlSetTypeDef,
    UpdateAssessmentFrameworkResponseTypeDef,
    UpdateAssessmentResponseTypeDef,
    UpdateAssessmentStatusResponseTypeDef,
    UpdateControlResponseTypeDef,
    UpdateSettingsResponseTypeDef,
    ValidateAssessmentReportIntegrityResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    ValidationException: Type[BotocoreClientError]


class AuditManagerClient:
    """
    [AuditManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_assessment_report_evidence_folder(
        self, assessmentId: str, evidenceFolderId: str
    ) -> Dict[str, Any]:
        """
        [Client.associate_assessment_report_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.associate_assessment_report_evidence_folder)
        """

    def batch_associate_assessment_report_evidence(
        self, assessmentId: str, evidenceFolderId: str, evidenceIds: List[str]
    ) -> BatchAssociateAssessmentReportEvidenceResponseTypeDef:
        """
        [Client.batch_associate_assessment_report_evidence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.batch_associate_assessment_report_evidence)
        """

    def batch_create_delegation_by_assessment(
        self, createDelegationRequests: List["CreateDelegationRequestTypeDef"], assessmentId: str
    ) -> BatchCreateDelegationByAssessmentResponseTypeDef:
        """
        [Client.batch_create_delegation_by_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.batch_create_delegation_by_assessment)
        """

    def batch_delete_delegation_by_assessment(
        self, delegationIds: List[str], assessmentId: str
    ) -> BatchDeleteDelegationByAssessmentResponseTypeDef:
        """
        [Client.batch_delete_delegation_by_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.batch_delete_delegation_by_assessment)
        """

    def batch_disassociate_assessment_report_evidence(
        self, assessmentId: str, evidenceFolderId: str, evidenceIds: List[str]
    ) -> BatchDisassociateAssessmentReportEvidenceResponseTypeDef:
        """
        [Client.batch_disassociate_assessment_report_evidence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.batch_disassociate_assessment_report_evidence)
        """

    def batch_import_evidence_to_assessment_control(
        self,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        manualEvidence: List["ManualEvidenceTypeDef"],
    ) -> BatchImportEvidenceToAssessmentControlResponseTypeDef:
        """
        [Client.batch_import_evidence_to_assessment_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.batch_import_evidence_to_assessment_control)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.can_paginate)
        """

    def create_assessment(
        self,
        name: str,
        assessmentReportsDestination: "AssessmentReportsDestinationTypeDef",
        scope: "ScopeTypeDef",
        roles: List["RoleTypeDef"],
        frameworkId: str,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAssessmentResponseTypeDef:
        """
        [Client.create_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.create_assessment)
        """

    def create_assessment_framework(
        self,
        name: str,
        controlSets: List[CreateAssessmentFrameworkControlSetTypeDef],
        description: str = None,
        complianceType: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAssessmentFrameworkResponseTypeDef:
        """
        [Client.create_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.create_assessment_framework)
        """

    def create_assessment_report(
        self, name: str, assessmentId: str, description: str = None
    ) -> CreateAssessmentReportResponseTypeDef:
        """
        [Client.create_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.create_assessment_report)
        """

    def create_control(
        self,
        name: str,
        controlMappingSources: List[CreateControlMappingSourceTypeDef],
        description: str = None,
        testingInformation: str = None,
        actionPlanTitle: str = None,
        actionPlanInstructions: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateControlResponseTypeDef:
        """
        [Client.create_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.create_control)
        """

    def delete_assessment(self, assessmentId: str) -> Dict[str, Any]:
        """
        [Client.delete_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.delete_assessment)
        """

    def delete_assessment_framework(self, frameworkId: str) -> Dict[str, Any]:
        """
        [Client.delete_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_framework)
        """

    def delete_assessment_report(
        self, assessmentId: str, assessmentReportId: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_assessment_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.delete_assessment_report)
        """

    def delete_control(self, controlId: str) -> Dict[str, Any]:
        """
        [Client.delete_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.delete_control)
        """

    def deregister_account(self) -> DeregisterAccountResponseTypeDef:
        """
        [Client.deregister_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.deregister_account)
        """

    def deregister_organization_admin_account(self, adminAccountId: str = None) -> Dict[str, Any]:
        """
        [Client.deregister_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.deregister_organization_admin_account)
        """

    def disassociate_assessment_report_evidence_folder(
        self, assessmentId: str, evidenceFolderId: str
    ) -> Dict[str, Any]:
        """
        [Client.disassociate_assessment_report_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.disassociate_assessment_report_evidence_folder)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.generate_presigned_url)
        """

    def get_account_status(self) -> GetAccountStatusResponseTypeDef:
        """
        [Client.get_account_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_account_status)
        """

    def get_assessment(self, assessmentId: str) -> GetAssessmentResponseTypeDef:
        """
        [Client.get_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_assessment)
        """

    def get_assessment_framework(self, frameworkId: str) -> GetAssessmentFrameworkResponseTypeDef:
        """
        [Client.get_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_assessment_framework)
        """

    def get_assessment_report_url(
        self, assessmentReportId: str, assessmentId: str
    ) -> GetAssessmentReportUrlResponseTypeDef:
        """
        [Client.get_assessment_report_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_assessment_report_url)
        """

    def get_change_logs(
        self,
        assessmentId: str,
        controlSetId: str = None,
        controlId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetChangeLogsResponseTypeDef:
        """
        [Client.get_change_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_change_logs)
        """

    def get_control(self, controlId: str) -> GetControlResponseTypeDef:
        """
        [Client.get_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_control)
        """

    def get_delegations(
        self, nextToken: str = None, maxResults: int = None
    ) -> GetDelegationsResponseTypeDef:
        """
        [Client.get_delegations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_delegations)
        """

    def get_evidence(
        self, assessmentId: str, controlSetId: str, evidenceFolderId: str, evidenceId: str
    ) -> GetEvidenceResponseTypeDef:
        """
        [Client.get_evidence documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_evidence)
        """

    def get_evidence_by_evidence_folder(
        self,
        assessmentId: str,
        controlSetId: str,
        evidenceFolderId: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetEvidenceByEvidenceFolderResponseTypeDef:
        """
        [Client.get_evidence_by_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_evidence_by_evidence_folder)
        """

    def get_evidence_folder(
        self, assessmentId: str, controlSetId: str, evidenceFolderId: str
    ) -> GetEvidenceFolderResponseTypeDef:
        """
        [Client.get_evidence_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folder)
        """

    def get_evidence_folders_by_assessment(
        self, assessmentId: str, nextToken: str = None, maxResults: int = None
    ) -> GetEvidenceFoldersByAssessmentResponseTypeDef:
        """
        [Client.get_evidence_folders_by_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment)
        """

    def get_evidence_folders_by_assessment_control(
        self,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetEvidenceFoldersByAssessmentControlResponseTypeDef:
        """
        [Client.get_evidence_folders_by_assessment_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_evidence_folders_by_assessment_control)
        """

    def get_organization_admin_account(self) -> GetOrganizationAdminAccountResponseTypeDef:
        """
        [Client.get_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_organization_admin_account)
        """

    def get_services_in_scope(self) -> GetServicesInScopeResponseTypeDef:
        """
        [Client.get_services_in_scope documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_services_in_scope)
        """

    def get_settings(
        self,
        attribute: Literal[
            "ALL",
            "IS_AWS_ORG_ENABLED",
            "SNS_TOPIC",
            "DEFAULT_ASSESSMENT_REPORTS_DESTINATION",
            "DEFAULT_PROCESS_OWNERS",
        ],
    ) -> GetSettingsResponseTypeDef:
        """
        [Client.get_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.get_settings)
        """

    def list_assessment_frameworks(
        self,
        frameworkType: Literal["Standard", "Custom"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAssessmentFrameworksResponseTypeDef:
        """
        [Client.list_assessment_frameworks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_assessment_frameworks)
        """

    def list_assessment_reports(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentReportsResponseTypeDef:
        """
        [Client.list_assessment_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_assessment_reports)
        """

    def list_assessments(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListAssessmentsResponseTypeDef:
        """
        [Client.list_assessments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_assessments)
        """

    def list_controls(
        self,
        controlType: Literal["Standard", "Custom"],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListControlsResponseTypeDef:
        """
        [Client.list_controls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_controls)
        """

    def list_keywords_for_data_source(
        self,
        source: Literal[
            "AWS_Cloudtrail", "AWS_Config", "AWS_Security_Hub", "AWS_API_Call", "MANUAL"
        ],
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListKeywordsForDataSourceResponseTypeDef:
        """
        [Client.list_keywords_for_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_keywords_for_data_source)
        """

    def list_notifications(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListNotificationsResponseTypeDef:
        """
        [Client.list_notifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_notifications)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.list_tags_for_resource)
        """

    def register_account(
        self, kmsKey: str = None, delegatedAdminAccount: str = None
    ) -> RegisterAccountResponseTypeDef:
        """
        [Client.register_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.register_account)
        """

    def register_organization_admin_account(
        self, adminAccountId: str
    ) -> RegisterOrganizationAdminAccountResponseTypeDef:
        """
        [Client.register_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.register_organization_admin_account)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.untag_resource)
        """

    def update_assessment(
        self,
        assessmentId: str,
        scope: "ScopeTypeDef",
        assessmentName: str = None,
        assessmentDescription: str = None,
        assessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
        roles: List["RoleTypeDef"] = None,
    ) -> UpdateAssessmentResponseTypeDef:
        """
        [Client.update_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_assessment)
        """

    def update_assessment_control(
        self,
        assessmentId: str,
        controlSetId: str,
        controlId: str,
        controlStatus: Literal["UNDER_REVIEW", "REVIEWED", "INACTIVE"] = None,
        commentBody: str = None,
    ) -> UpdateAssessmentControlResponseTypeDef:
        """
        [Client.update_assessment_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control)
        """

    def update_assessment_control_set_status(
        self,
        assessmentId: str,
        controlSetId: str,
        status: Literal["ACTIVE", "UNDER_REVIEW", "REVIEWED"],
        comment: str,
    ) -> UpdateAssessmentControlSetStatusResponseTypeDef:
        """
        [Client.update_assessment_control_set_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_assessment_control_set_status)
        """

    def update_assessment_framework(
        self,
        frameworkId: str,
        name: str,
        controlSets: List[UpdateAssessmentFrameworkControlSetTypeDef],
        description: str = None,
        complianceType: str = None,
    ) -> UpdateAssessmentFrameworkResponseTypeDef:
        """
        [Client.update_assessment_framework documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_assessment_framework)
        """

    def update_assessment_status(
        self, assessmentId: str, status: Literal["ACTIVE", "INACTIVE"]
    ) -> UpdateAssessmentStatusResponseTypeDef:
        """
        [Client.update_assessment_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_assessment_status)
        """

    def update_control(
        self,
        controlId: str,
        name: str,
        controlMappingSources: List["ControlMappingSourceTypeDef"],
        description: str = None,
        testingInformation: str = None,
        actionPlanTitle: str = None,
        actionPlanInstructions: str = None,
    ) -> UpdateControlResponseTypeDef:
        """
        [Client.update_control documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_control)
        """

    def update_settings(
        self,
        snsTopic: str = None,
        defaultAssessmentReportsDestination: "AssessmentReportsDestinationTypeDef" = None,
        defaultProcessOwners: List["RoleTypeDef"] = None,
        kmsKey: str = None,
    ) -> UpdateSettingsResponseTypeDef:
        """
        [Client.update_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.update_settings)
        """

    def validate_assessment_report_integrity(
        self, s3RelativePath: str
    ) -> ValidateAssessmentReportIntegrityResponseTypeDef:
        """
        [Client.validate_assessment_report_integrity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/auditmanager.html#AuditManager.Client.validate_assessment_report_integrity)
        """
