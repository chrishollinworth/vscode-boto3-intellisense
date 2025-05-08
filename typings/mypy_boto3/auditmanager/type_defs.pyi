"""
Type annotations for auditmanager service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef

    data: AWSAccountTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccountStatusType,
    ActionEnumType,
    AssessmentReportStatusType,
    AssessmentStatusType,
    ControlResponseType,
    ControlSetStatusType,
    ControlStateType,
    ControlStatusType,
    ControlTypeType,
    DataSourceTypeType,
    DelegationStatusType,
    DeleteResourcesType,
    EvidenceFinderBackfillStatusType,
    EvidenceFinderEnablementStatusType,
    FrameworkTypeType,
    KeywordInputTypeType,
    ObjectTypeEnumType,
    RoleTypeType,
    SettingAttributeType,
    ShareRequestActionType,
    ShareRequestStatusType,
    ShareRequestTypeType,
    SourceFrequencyType,
    SourceSetUpOptionType,
    SourceTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AWSAccountTypeDef",
    "AWSServiceTypeDef",
    "AssessmentControlSetTypeDef",
    "AssessmentControlTypeDef",
    "AssessmentEvidenceFolderTypeDef",
    "AssessmentFrameworkMetadataTypeDef",
    "AssessmentFrameworkShareRequestTypeDef",
    "AssessmentFrameworkTypeDef",
    "AssessmentMetadataItemTypeDef",
    "AssessmentMetadataTypeDef",
    "AssessmentReportEvidenceErrorTypeDef",
    "AssessmentReportMetadataTypeDef",
    "AssessmentReportTypeDef",
    "AssessmentReportsDestinationTypeDef",
    "AssessmentTypeDef",
    "AssociateAssessmentReportEvidenceFolderRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentRequestTypeDef",
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentRequestTypeDef",
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceRequestTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlRequestTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    "ChangeLogTypeDef",
    "ControlCommentTypeDef",
    "ControlDomainInsightsTypeDef",
    "ControlInsightsMetadataByAssessmentItemTypeDef",
    "ControlInsightsMetadataItemTypeDef",
    "ControlMappingSourceTypeDef",
    "ControlMetadataTypeDef",
    "ControlSetTypeDef",
    "ControlTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentFrameworkRequestTypeDef",
    "CreateAssessmentFrameworkResponseTypeDef",
    "CreateAssessmentReportRequestTypeDef",
    "CreateAssessmentReportResponseTypeDef",
    "CreateAssessmentRequestTypeDef",
    "CreateAssessmentResponseTypeDef",
    "CreateControlMappingSourceTypeDef",
    "CreateControlRequestTypeDef",
    "CreateControlResponseTypeDef",
    "CreateDelegationRequestTypeDef",
    "DefaultExportDestinationTypeDef",
    "DelegationMetadataTypeDef",
    "DelegationTypeDef",
    "DeleteAssessmentFrameworkRequestTypeDef",
    "DeleteAssessmentFrameworkShareRequestTypeDef",
    "DeleteAssessmentReportRequestTypeDef",
    "DeleteAssessmentRequestTypeDef",
    "DeleteControlRequestTypeDef",
    "DeregisterAccountResponseTypeDef",
    "DeregisterOrganizationAdminAccountRequestTypeDef",
    "DeregistrationPolicyTypeDef",
    "DisassociateAssessmentReportEvidenceFolderRequestTypeDef",
    "EvidenceFinderEnablementTypeDef",
    "EvidenceInsightsTypeDef",
    "EvidenceTypeDef",
    "FrameworkMetadataTypeDef",
    "FrameworkTypeDef",
    "GetAccountStatusResponseTypeDef",
    "GetAssessmentFrameworkRequestTypeDef",
    "GetAssessmentFrameworkResponseTypeDef",
    "GetAssessmentReportUrlRequestTypeDef",
    "GetAssessmentReportUrlResponseTypeDef",
    "GetAssessmentRequestTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetChangeLogsRequestTypeDef",
    "GetChangeLogsResponseTypeDef",
    "GetControlRequestTypeDef",
    "GetControlResponseTypeDef",
    "GetDelegationsRequestTypeDef",
    "GetDelegationsResponseTypeDef",
    "GetEvidenceByEvidenceFolderRequestTypeDef",
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    "GetEvidenceFileUploadUrlRequestTypeDef",
    "GetEvidenceFileUploadUrlResponseTypeDef",
    "GetEvidenceFolderRequestTypeDef",
    "GetEvidenceFolderResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlRequestTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    "GetEvidenceFoldersByAssessmentRequestTypeDef",
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    "GetEvidenceRequestTypeDef",
    "GetEvidenceResponseTypeDef",
    "GetInsightsByAssessmentRequestTypeDef",
    "GetInsightsByAssessmentResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "GetOrganizationAdminAccountResponseTypeDef",
    "GetServicesInScopeResponseTypeDef",
    "GetSettingsRequestTypeDef",
    "GetSettingsResponseTypeDef",
    "InsightsByAssessmentTypeDef",
    "InsightsTypeDef",
    "ListAssessmentControlInsightsByControlDomainRequestTypeDef",
    "ListAssessmentControlInsightsByControlDomainResponseTypeDef",
    "ListAssessmentFrameworkShareRequestsRequestTypeDef",
    "ListAssessmentFrameworkShareRequestsResponseTypeDef",
    "ListAssessmentFrameworksRequestTypeDef",
    "ListAssessmentFrameworksResponseTypeDef",
    "ListAssessmentReportsRequestTypeDef",
    "ListAssessmentReportsResponseTypeDef",
    "ListAssessmentsRequestTypeDef",
    "ListAssessmentsResponseTypeDef",
    "ListControlDomainInsightsByAssessmentRequestTypeDef",
    "ListControlDomainInsightsByAssessmentResponseTypeDef",
    "ListControlDomainInsightsRequestTypeDef",
    "ListControlDomainInsightsResponseTypeDef",
    "ListControlInsightsByControlDomainRequestTypeDef",
    "ListControlInsightsByControlDomainResponseTypeDef",
    "ListControlsRequestTypeDef",
    "ListControlsResponseTypeDef",
    "ListKeywordsForDataSourceRequestTypeDef",
    "ListKeywordsForDataSourceResponseTypeDef",
    "ListNotificationsRequestTypeDef",
    "ListNotificationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManualEvidenceTypeDef",
    "NotificationTypeDef",
    "RegisterAccountRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "RegisterOrganizationAdminAccountRequestTypeDef",
    "RegisterOrganizationAdminAccountResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RoleTypeDef",
    "ScopeOutputTypeDef",
    "ScopeTypeDef",
    "ScopeUnionTypeDef",
    "ServiceMetadataTypeDef",
    "SettingsTypeDef",
    "SourceKeywordTypeDef",
    "StartAssessmentFrameworkShareRequestTypeDef",
    "StartAssessmentFrameworkShareResponseTypeDef",
    "TagResourceRequestTypeDef",
    "URLTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAssessmentControlRequestTypeDef",
    "UpdateAssessmentControlResponseTypeDef",
    "UpdateAssessmentControlSetStatusRequestTypeDef",
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkRequestTypeDef",
    "UpdateAssessmentFrameworkResponseTypeDef",
    "UpdateAssessmentFrameworkShareRequestTypeDef",
    "UpdateAssessmentFrameworkShareResponseTypeDef",
    "UpdateAssessmentRequestTypeDef",
    "UpdateAssessmentResponseTypeDef",
    "UpdateAssessmentStatusRequestTypeDef",
    "UpdateAssessmentStatusResponseTypeDef",
    "UpdateControlRequestTypeDef",
    "UpdateControlResponseTypeDef",
    "UpdateSettingsRequestTypeDef",
    "UpdateSettingsResponseTypeDef",
    "ValidateAssessmentReportIntegrityRequestTypeDef",
    "ValidateAssessmentReportIntegrityResponseTypeDef",
)

AWSAccountTypeDef = TypedDict(
    "AWSAccountTypeDef",
    {
        "id": NotRequired[str],
        "emailAddress": NotRequired[str],
        "name": NotRequired[str],
    },
)

class AWSServiceTypeDef(TypedDict):
    serviceName: NotRequired[str]

DelegationTypeDef = TypedDict(
    "DelegationTypeDef",
    {
        "id": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentId": NotRequired[str],
        "status": NotRequired[DelegationStatusType],
        "roleArn": NotRequired[str],
        "roleType": NotRequired[RoleTypeType],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "controlSetId": NotRequired[str],
        "comment": NotRequired[str],
        "createdBy": NotRequired[str],
    },
)

class RoleTypeDef(TypedDict):
    roleType: RoleTypeType
    roleArn: str

class ControlCommentTypeDef(TypedDict):
    authorName: NotRequired[str]
    commentBody: NotRequired[str]
    postedDate: NotRequired[datetime]

AssessmentEvidenceFolderTypeDef = TypedDict(
    "AssessmentEvidenceFolderTypeDef",
    {
        "name": NotRequired[str],
        "date": NotRequired[datetime],
        "assessmentId": NotRequired[str],
        "controlSetId": NotRequired[str],
        "controlId": NotRequired[str],
        "id": NotRequired[str],
        "dataSource": NotRequired[str],
        "author": NotRequired[str],
        "totalEvidence": NotRequired[int],
        "assessmentReportSelectionCount": NotRequired[int],
        "controlName": NotRequired[str],
        "evidenceResourcesIncludedCount": NotRequired[int],
        "evidenceByTypeConfigurationDataCount": NotRequired[int],
        "evidenceByTypeManualCount": NotRequired[int],
        "evidenceByTypeComplianceCheckCount": NotRequired[int],
        "evidenceByTypeComplianceCheckIssuesCount": NotRequired[int],
        "evidenceByTypeUserActivityCount": NotRequired[int],
        "evidenceAwsServiceSourceCount": NotRequired[int],
    },
)
AssessmentFrameworkMetadataTypeDef = TypedDict(
    "AssessmentFrameworkMetadataTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "type": NotRequired[FrameworkTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "complianceType": NotRequired[str],
        "controlsCount": NotRequired[int],
        "controlSetsCount": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
AssessmentFrameworkShareRequestTypeDef = TypedDict(
    "AssessmentFrameworkShareRequestTypeDef",
    {
        "id": NotRequired[str],
        "frameworkId": NotRequired[str],
        "frameworkName": NotRequired[str],
        "frameworkDescription": NotRequired[str],
        "status": NotRequired[ShareRequestStatusType],
        "sourceAccount": NotRequired[str],
        "destinationAccount": NotRequired[str],
        "destinationRegion": NotRequired[str],
        "expirationTime": NotRequired[datetime],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "comment": NotRequired[str],
        "standardControlsCount": NotRequired[int],
        "customControlsCount": NotRequired[int],
        "complianceType": NotRequired[str],
    },
)

class FrameworkMetadataTypeDef(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    logo: NotRequired[str]
    complianceType: NotRequired[str]

class AssessmentReportsDestinationTypeDef(TypedDict):
    destinationType: NotRequired[Literal["S3"]]
    destination: NotRequired[str]

class AssessmentReportEvidenceErrorTypeDef(TypedDict):
    evidenceId: NotRequired[str]
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

AssessmentReportMetadataTypeDef = TypedDict(
    "AssessmentReportMetadataTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "author": NotRequired[str],
        "status": NotRequired[AssessmentReportStatusType],
        "creationTime": NotRequired[datetime],
    },
)
AssessmentReportTypeDef = TypedDict(
    "AssessmentReportTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "author": NotRequired[str],
        "status": NotRequired[AssessmentReportStatusType],
        "creationTime": NotRequired[datetime],
    },
)

class AssociateAssessmentReportEvidenceFolderRequestTypeDef(TypedDict):
    assessmentId: str
    evidenceFolderId: str

class BatchAssociateAssessmentReportEvidenceRequestTypeDef(TypedDict):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateDelegationRequestTypeDef(TypedDict):
    comment: NotRequired[str]
    controlSetId: NotRequired[str]
    roleArn: NotRequired[str]
    roleType: NotRequired[RoleTypeType]

class BatchDeleteDelegationByAssessmentErrorTypeDef(TypedDict):
    delegationId: NotRequired[str]
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

class BatchDeleteDelegationByAssessmentRequestTypeDef(TypedDict):
    delegationIds: Sequence[str]
    assessmentId: str

class BatchDisassociateAssessmentReportEvidenceRequestTypeDef(TypedDict):
    assessmentId: str
    evidenceFolderId: str
    evidenceIds: Sequence[str]

class ManualEvidenceTypeDef(TypedDict):
    s3ResourcePath: NotRequired[str]
    textResponse: NotRequired[str]
    evidenceFileName: NotRequired[str]

class ChangeLogTypeDef(TypedDict):
    objectType: NotRequired[ObjectTypeEnumType]
    objectName: NotRequired[str]
    action: NotRequired[ActionEnumType]
    createdAt: NotRequired[datetime]
    createdBy: NotRequired[str]

class EvidenceInsightsTypeDef(TypedDict):
    noncompliantEvidenceCount: NotRequired[int]
    compliantEvidenceCount: NotRequired[int]
    inconclusiveEvidenceCount: NotRequired[int]

class SourceKeywordTypeDef(TypedDict):
    keywordInputType: NotRequired[KeywordInputTypeType]
    keywordValue: NotRequired[str]

ControlMetadataTypeDef = TypedDict(
    "ControlMetadataTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "controlSources": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
CreateAssessmentFrameworkControlTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlTypeDef",
    {
        "id": str,
    },
)

class CreateAssessmentReportRequestTypeDef(TypedDict):
    name: str
    assessmentId: str
    description: NotRequired[str]
    queryStatement: NotRequired[str]

class DefaultExportDestinationTypeDef(TypedDict):
    destinationType: NotRequired[Literal["S3"]]
    destination: NotRequired[str]

DelegationMetadataTypeDef = TypedDict(
    "DelegationMetadataTypeDef",
    {
        "id": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentId": NotRequired[str],
        "status": NotRequired[DelegationStatusType],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "controlSetName": NotRequired[str],
    },
)

class DeleteAssessmentFrameworkRequestTypeDef(TypedDict):
    frameworkId: str

class DeleteAssessmentFrameworkShareRequestTypeDef(TypedDict):
    requestId: str
    requestType: ShareRequestTypeType

class DeleteAssessmentReportRequestTypeDef(TypedDict):
    assessmentId: str
    assessmentReportId: str

class DeleteAssessmentRequestTypeDef(TypedDict):
    assessmentId: str

class DeleteControlRequestTypeDef(TypedDict):
    controlId: str

class DeregisterOrganizationAdminAccountRequestTypeDef(TypedDict):
    adminAccountId: NotRequired[str]

class DeregistrationPolicyTypeDef(TypedDict):
    deleteResources: NotRequired[DeleteResourcesType]

class DisassociateAssessmentReportEvidenceFolderRequestTypeDef(TypedDict):
    assessmentId: str
    evidenceFolderId: str

class EvidenceFinderEnablementTypeDef(TypedDict):
    eventDataStoreArn: NotRequired[str]
    enablementStatus: NotRequired[EvidenceFinderEnablementStatusType]
    backfillStatus: NotRequired[EvidenceFinderBackfillStatusType]
    error: NotRequired[str]

class ResourceTypeDef(TypedDict):
    arn: NotRequired[str]
    value: NotRequired[str]
    complianceCheck: NotRequired[str]

class GetAssessmentFrameworkRequestTypeDef(TypedDict):
    frameworkId: str

class GetAssessmentReportUrlRequestTypeDef(TypedDict):
    assessmentReportId: str
    assessmentId: str

class URLTypeDef(TypedDict):
    hyperlinkName: NotRequired[str]
    link: NotRequired[str]

class GetAssessmentRequestTypeDef(TypedDict):
    assessmentId: str

class GetChangeLogsRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: NotRequired[str]
    controlId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetControlRequestTypeDef(TypedDict):
    controlId: str

class GetDelegationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetEvidenceByEvidenceFolderRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetEvidenceFileUploadUrlRequestTypeDef(TypedDict):
    fileName: str

class GetEvidenceFolderRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str

class GetEvidenceFoldersByAssessmentControlRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    controlId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetEvidenceFoldersByAssessmentRequestTypeDef(TypedDict):
    assessmentId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetEvidenceRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    evidenceFolderId: str
    evidenceId: str

class GetInsightsByAssessmentRequestTypeDef(TypedDict):
    assessmentId: str

class InsightsByAssessmentTypeDef(TypedDict):
    noncompliantEvidenceCount: NotRequired[int]
    compliantEvidenceCount: NotRequired[int]
    inconclusiveEvidenceCount: NotRequired[int]
    assessmentControlsCountByNoncompliantEvidence: NotRequired[int]
    totalAssessmentControlsCount: NotRequired[int]
    lastUpdated: NotRequired[datetime]

class InsightsTypeDef(TypedDict):
    activeAssessmentsCount: NotRequired[int]
    noncompliantEvidenceCount: NotRequired[int]
    compliantEvidenceCount: NotRequired[int]
    inconclusiveEvidenceCount: NotRequired[int]
    assessmentControlsCountByNoncompliantEvidence: NotRequired[int]
    totalAssessmentControlsCount: NotRequired[int]
    lastUpdated: NotRequired[datetime]

class ServiceMetadataTypeDef(TypedDict):
    name: NotRequired[str]
    displayName: NotRequired[str]
    description: NotRequired[str]
    category: NotRequired[str]

class GetSettingsRequestTypeDef(TypedDict):
    attribute: SettingAttributeType

class ListAssessmentControlInsightsByControlDomainRequestTypeDef(TypedDict):
    controlDomainId: str
    assessmentId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAssessmentFrameworkShareRequestsRequestTypeDef(TypedDict):
    requestType: ShareRequestTypeType
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAssessmentFrameworksRequestTypeDef(TypedDict):
    frameworkType: FrameworkTypeType
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAssessmentReportsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListAssessmentsRequestTypeDef(TypedDict):
    status: NotRequired[AssessmentStatusType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListControlDomainInsightsByAssessmentRequestTypeDef(TypedDict):
    assessmentId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListControlDomainInsightsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListControlInsightsByControlDomainRequestTypeDef(TypedDict):
    controlDomainId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListControlsRequestTypeDef(TypedDict):
    controlType: ControlTypeType
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    controlCatalogId: NotRequired[str]

class ListKeywordsForDataSourceRequestTypeDef(TypedDict):
    source: DataSourceTypeType
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListNotificationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "id": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "controlSetId": NotRequired[str],
        "controlSetName": NotRequired[str],
        "description": NotRequired[str],
        "eventTime": NotRequired[datetime],
        "source": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class RegisterAccountRequestTypeDef(TypedDict):
    kmsKey: NotRequired[str]
    delegatedAdminAccount: NotRequired[str]

class RegisterOrganizationAdminAccountRequestTypeDef(TypedDict):
    adminAccountId: str

class StartAssessmentFrameworkShareRequestTypeDef(TypedDict):
    frameworkId: str
    destinationAccount: str
    destinationRegion: str
    comment: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAssessmentControlRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    controlId: str
    controlStatus: NotRequired[ControlStatusType]
    commentBody: NotRequired[str]

class UpdateAssessmentControlSetStatusRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    status: ControlSetStatusType
    comment: str

class UpdateAssessmentFrameworkShareRequestTypeDef(TypedDict):
    requestId: str
    requestType: ShareRequestTypeType
    action: ShareRequestActionType

class UpdateAssessmentStatusRequestTypeDef(TypedDict):
    assessmentId: str
    status: AssessmentStatusType

class ValidateAssessmentReportIntegrityRequestTypeDef(TypedDict):
    s3RelativePath: str

class ScopeOutputTypeDef(TypedDict):
    awsAccounts: NotRequired[List[AWSAccountTypeDef]]
    awsServices: NotRequired[List[AWSServiceTypeDef]]

class ScopeTypeDef(TypedDict):
    awsAccounts: NotRequired[Sequence[AWSAccountTypeDef]]
    awsServices: NotRequired[Sequence[AWSServiceTypeDef]]

AssessmentMetadataItemTypeDef = TypedDict(
    "AssessmentMetadataItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "complianceType": NotRequired[str],
        "status": NotRequired[AssessmentStatusType],
        "roles": NotRequired[List[RoleTypeDef]],
        "delegations": NotRequired[List[DelegationTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
    },
)
AssessmentControlTypeDef = TypedDict(
    "AssessmentControlTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ControlStatusType],
        "response": NotRequired[ControlResponseType],
        "comments": NotRequired[List[ControlCommentTypeDef]],
        "evidenceSources": NotRequired[List[str]],
        "evidenceCount": NotRequired[int],
        "assessmentReportEvidenceCount": NotRequired[int],
    },
)

class BatchAssociateAssessmentReportEvidenceResponseTypeDef(TypedDict):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateAssessmentReportEvidenceResponseTypeDef(TypedDict):
    evidenceIds: List[str]
    errors: List[AssessmentReportEvidenceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentReportResponseTypeDef(TypedDict):
    assessmentReport: AssessmentReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterAccountResponseTypeDef(TypedDict):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountStatusResponseTypeDef(TypedDict):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFileUploadUrlResponseTypeDef(TypedDict):
    evidenceFileName: str
    uploadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFolderResponseTypeDef(TypedDict):
    evidenceFolder: AssessmentEvidenceFolderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceFoldersByAssessmentControlResponseTypeDef(TypedDict):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEvidenceFoldersByAssessmentResponseTypeDef(TypedDict):
    evidenceFolders: List[AssessmentEvidenceFolderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetOrganizationAdminAccountResponseTypeDef(TypedDict):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssessmentFrameworkShareRequestsResponseTypeDef(TypedDict):
    assessmentFrameworkShareRequests: List[AssessmentFrameworkShareRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAssessmentFrameworksResponseTypeDef(TypedDict):
    frameworkMetadataList: List[AssessmentFrameworkMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAssessmentReportsResponseTypeDef(TypedDict):
    assessmentReports: List[AssessmentReportMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListKeywordsForDataSourceResponseTypeDef(TypedDict):
    keywords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAccountResponseTypeDef(TypedDict):
    status: AccountStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterOrganizationAdminAccountResponseTypeDef(TypedDict):
    adminAccountId: str
    organizationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAssessmentFrameworkShareResponseTypeDef(TypedDict):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentFrameworkShareResponseTypeDef(TypedDict):
    assessmentFrameworkShareRequest: AssessmentFrameworkShareRequestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateAssessmentReportIntegrityResponseTypeDef(TypedDict):
    signatureValid: bool
    signatureAlgorithm: str
    signatureDateTime: str
    signatureKeyId: str
    validationErrors: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDelegationByAssessmentErrorTypeDef(TypedDict):
    createDelegationRequest: NotRequired[CreateDelegationRequestTypeDef]
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

class BatchCreateDelegationByAssessmentRequestTypeDef(TypedDict):
    createDelegationRequests: Sequence[CreateDelegationRequestTypeDef]
    assessmentId: str

class BatchDeleteDelegationByAssessmentResponseTypeDef(TypedDict):
    errors: List[BatchDeleteDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchImportEvidenceToAssessmentControlErrorTypeDef(TypedDict):
    manualEvidence: NotRequired[ManualEvidenceTypeDef]
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

class BatchImportEvidenceToAssessmentControlRequestTypeDef(TypedDict):
    assessmentId: str
    controlSetId: str
    controlId: str
    manualEvidence: Sequence[ManualEvidenceTypeDef]

class GetChangeLogsResponseTypeDef(TypedDict):
    changeLogs: List[ChangeLogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ControlDomainInsightsTypeDef = TypedDict(
    "ControlDomainInsightsTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "controlsCountByNoncompliantEvidence": NotRequired[int],
        "totalControlsCount": NotRequired[int],
        "evidenceInsights": NotRequired[EvidenceInsightsTypeDef],
        "lastUpdated": NotRequired[datetime],
    },
)
ControlInsightsMetadataByAssessmentItemTypeDef = TypedDict(
    "ControlInsightsMetadataByAssessmentItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "evidenceInsights": NotRequired[EvidenceInsightsTypeDef],
        "controlSetName": NotRequired[str],
        "lastUpdated": NotRequired[datetime],
    },
)
ControlInsightsMetadataItemTypeDef = TypedDict(
    "ControlInsightsMetadataItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "evidenceInsights": NotRequired[EvidenceInsightsTypeDef],
        "lastUpdated": NotRequired[datetime],
    },
)

class ControlMappingSourceTypeDef(TypedDict):
    sourceId: NotRequired[str]
    sourceName: NotRequired[str]
    sourceDescription: NotRequired[str]
    sourceSetUpOption: NotRequired[SourceSetUpOptionType]
    sourceType: NotRequired[SourceTypeType]
    sourceKeyword: NotRequired[SourceKeywordTypeDef]
    sourceFrequency: NotRequired[SourceFrequencyType]
    troubleshootingText: NotRequired[str]

class CreateControlMappingSourceTypeDef(TypedDict):
    sourceName: NotRequired[str]
    sourceDescription: NotRequired[str]
    sourceSetUpOption: NotRequired[SourceSetUpOptionType]
    sourceType: NotRequired[SourceTypeType]
    sourceKeyword: NotRequired[SourceKeywordTypeDef]
    sourceFrequency: NotRequired[SourceFrequencyType]
    troubleshootingText: NotRequired[str]

class ListControlsResponseTypeDef(TypedDict):
    controlMetadataList: List[ControlMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAssessmentFrameworkControlSetTypeDef(TypedDict):
    name: str
    controls: NotRequired[Sequence[CreateAssessmentFrameworkControlTypeDef]]

UpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "UpdateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
        "controls": Sequence[CreateAssessmentFrameworkControlTypeDef],
        "id": NotRequired[str],
    },
)

class GetDelegationsResponseTypeDef(TypedDict):
    delegations: List[DelegationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateSettingsRequestTypeDef(TypedDict):
    snsTopic: NotRequired[str]
    defaultAssessmentReportsDestination: NotRequired[AssessmentReportsDestinationTypeDef]
    defaultProcessOwners: NotRequired[Sequence[RoleTypeDef]]
    kmsKey: NotRequired[str]
    evidenceFinderEnabled: NotRequired[bool]
    deregistrationPolicy: NotRequired[DeregistrationPolicyTypeDef]
    defaultExportDestination: NotRequired[DefaultExportDestinationTypeDef]

class SettingsTypeDef(TypedDict):
    isAwsOrgEnabled: NotRequired[bool]
    snsTopic: NotRequired[str]
    defaultAssessmentReportsDestination: NotRequired[AssessmentReportsDestinationTypeDef]
    defaultProcessOwners: NotRequired[List[RoleTypeDef]]
    kmsKey: NotRequired[str]
    evidenceFinderEnablement: NotRequired[EvidenceFinderEnablementTypeDef]
    deregistrationPolicy: NotRequired[DeregistrationPolicyTypeDef]
    defaultExportDestination: NotRequired[DefaultExportDestinationTypeDef]

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "dataSource": NotRequired[str],
        "evidenceAwsAccountId": NotRequired[str],
        "time": NotRequired[datetime],
        "eventSource": NotRequired[str],
        "eventName": NotRequired[str],
        "evidenceByType": NotRequired[str],
        "resourcesIncluded": NotRequired[List[ResourceTypeDef]],
        "attributes": NotRequired[Dict[str, str]],
        "iamId": NotRequired[str],
        "complianceCheck": NotRequired[str],
        "awsOrganization": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "evidenceFolderId": NotRequired[str],
        "id": NotRequired[str],
        "assessmentReportSelection": NotRequired[str],
    },
)

class GetAssessmentReportUrlResponseTypeDef(TypedDict):
    preSignedUrl: URLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsByAssessmentResponseTypeDef(TypedDict):
    insights: InsightsByAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInsightsResponseTypeDef(TypedDict):
    insights: InsightsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServicesInScopeResponseTypeDef(TypedDict):
    serviceMetadata: List[ServiceMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationsResponseTypeDef(TypedDict):
    notifications: List[NotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

AssessmentMetadataTypeDef = TypedDict(
    "AssessmentMetadataTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
        "status": NotRequired[AssessmentStatusType],
        "assessmentReportsDestination": NotRequired[AssessmentReportsDestinationTypeDef],
        "scope": NotRequired[ScopeOutputTypeDef],
        "roles": NotRequired[List[RoleTypeDef]],
        "delegations": NotRequired[List[DelegationTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
    },
)
ScopeUnionTypeDef = Union[ScopeTypeDef, ScopeOutputTypeDef]

class ListAssessmentsResponseTypeDef(TypedDict):
    assessmentMetadata: List[AssessmentMetadataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

AssessmentControlSetTypeDef = TypedDict(
    "AssessmentControlSetTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ControlSetStatusType],
        "roles": NotRequired[List[RoleTypeDef]],
        "controls": NotRequired[List[AssessmentControlTypeDef]],
        "delegations": NotRequired[List[DelegationTypeDef]],
        "systemEvidenceCount": NotRequired[int],
        "manualEvidenceCount": NotRequired[int],
    },
)

class UpdateAssessmentControlResponseTypeDef(TypedDict):
    control: AssessmentControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateDelegationByAssessmentResponseTypeDef(TypedDict):
    delegations: List[DelegationTypeDef]
    errors: List[BatchCreateDelegationByAssessmentErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchImportEvidenceToAssessmentControlResponseTypeDef(TypedDict):
    errors: List[BatchImportEvidenceToAssessmentControlErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlDomainInsightsByAssessmentResponseTypeDef(TypedDict):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListControlDomainInsightsResponseTypeDef(TypedDict):
    controlDomainInsights: List[ControlDomainInsightsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAssessmentControlInsightsByControlDomainResponseTypeDef(TypedDict):
    controlInsightsByAssessment: List[ControlInsightsMetadataByAssessmentItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListControlInsightsByControlDomainResponseTypeDef(TypedDict):
    controlInsightsMetadata: List[ControlInsightsMetadataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ControlTypeDef = TypedDict(
    "ControlTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "type": NotRequired[ControlTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
        "controlSources": NotRequired[str],
        "controlMappingSources": NotRequired[List[ControlMappingSourceTypeDef]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "state": NotRequired[ControlStateType],
    },
)

class UpdateControlRequestTypeDef(TypedDict):
    controlId: str
    name: str
    controlMappingSources: Sequence[ControlMappingSourceTypeDef]
    description: NotRequired[str]
    testingInformation: NotRequired[str]
    actionPlanTitle: NotRequired[str]
    actionPlanInstructions: NotRequired[str]

class CreateControlRequestTypeDef(TypedDict):
    name: str
    controlMappingSources: Sequence[CreateControlMappingSourceTypeDef]
    description: NotRequired[str]
    testingInformation: NotRequired[str]
    actionPlanTitle: NotRequired[str]
    actionPlanInstructions: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateAssessmentFrameworkRequestTypeDef(TypedDict):
    name: str
    controlSets: Sequence[CreateAssessmentFrameworkControlSetTypeDef]
    description: NotRequired[str]
    complianceType: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateAssessmentFrameworkRequestTypeDef(TypedDict):
    frameworkId: str
    name: str
    controlSets: Sequence[UpdateAssessmentFrameworkControlSetTypeDef]
    description: NotRequired[str]
    complianceType: NotRequired[str]

class GetSettingsResponseTypeDef(TypedDict):
    settings: SettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsResponseTypeDef(TypedDict):
    settings: SettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEvidenceByEvidenceFolderResponseTypeDef(TypedDict):
    evidence: List[EvidenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetEvidenceResponseTypeDef(TypedDict):
    evidence: EvidenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentRequestTypeDef(TypedDict):
    name: str
    assessmentReportsDestination: AssessmentReportsDestinationTypeDef
    scope: ScopeUnionTypeDef
    roles: Sequence[RoleTypeDef]
    frameworkId: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateAssessmentRequestTypeDef(TypedDict):
    assessmentId: str
    scope: ScopeUnionTypeDef
    assessmentName: NotRequired[str]
    assessmentDescription: NotRequired[str]
    assessmentReportsDestination: NotRequired[AssessmentReportsDestinationTypeDef]
    roles: NotRequired[Sequence[RoleTypeDef]]

AssessmentFrameworkTypeDef = TypedDict(
    "AssessmentFrameworkTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "metadata": NotRequired[FrameworkMetadataTypeDef],
        "controlSets": NotRequired[List[AssessmentControlSetTypeDef]],
    },
)

class UpdateAssessmentControlSetStatusResponseTypeDef(TypedDict):
    controlSet: AssessmentControlSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ControlSetTypeDef = TypedDict(
    "ControlSetTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "controls": NotRequired[List[ControlTypeDef]],
    },
)

class CreateControlResponseTypeDef(TypedDict):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetControlResponseTypeDef(TypedDict):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateControlResponseTypeDef(TypedDict):
    control: ControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssessmentTypeDef(TypedDict):
    arn: NotRequired[str]
    awsAccount: NotRequired[AWSAccountTypeDef]
    metadata: NotRequired[AssessmentMetadataTypeDef]
    framework: NotRequired[AssessmentFrameworkTypeDef]
    tags: NotRequired[Dict[str, str]]

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[FrameworkTypeType],
        "complianceType": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "controlSources": NotRequired[str],
        "controlSets": NotRequired[List[ControlSetTypeDef]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

class CreateAssessmentResponseTypeDef(TypedDict):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentResponseTypeDef(TypedDict):
    assessment: AssessmentTypeDef
    userRole: RoleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentResponseTypeDef(TypedDict):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentStatusResponseTypeDef(TypedDict):
    assessment: AssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssessmentFrameworkResponseTypeDef(TypedDict):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssessmentFrameworkResponseTypeDef(TypedDict):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssessmentFrameworkResponseTypeDef(TypedDict):
    framework: FrameworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
