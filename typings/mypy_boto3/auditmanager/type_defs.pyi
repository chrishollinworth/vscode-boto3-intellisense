"""
Type annotations for auditmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef

    data: AWSAccountTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccountStatusType,
    ActionEnumType,
    AssessmentReportStatusType,
    AssessmentStatusType,
    ControlResponseType,
    ControlSetStatusType,
    ControlStatusType,
    ControlTypeType,
    DelegationStatusType,
    FrameworkTypeType,
    ObjectTypeEnumType,
    RoleTypeType,
    SettingAttributeType,
    SourceFrequencyType,
    SourceSetUpOptionType,
    SourceTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AWSAccountTypeDef",
    "AWSServiceTypeDef",
    "AssessmentControlSetTypeDef",
    "AssessmentControlTypeDef",
    "AssessmentEvidenceFolderTypeDef",
    "AssessmentFrameworkMetadataTypeDef",
    "AssessmentFrameworkTypeDef",
    "AssessmentMetadataItemTypeDef",
    "AssessmentMetadataTypeDef",
    "AssessmentReportEvidenceErrorTypeDef",
    "AssessmentReportMetadataTypeDef",
    "AssessmentReportTypeDef",
    "AssessmentReportsDestinationTypeDef",
    "AssessmentTypeDef",
    "AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentRequestRequestTypeDef",
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentRequestRequestTypeDef",
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlRequestRequestTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    "ChangeLogTypeDef",
    "ControlCommentTypeDef",
    "ControlMappingSourceTypeDef",
    "ControlMetadataTypeDef",
    "ControlSetTypeDef",
    "ControlTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentFrameworkRequestRequestTypeDef",
    "CreateAssessmentFrameworkResponseTypeDef",
    "CreateAssessmentReportRequestRequestTypeDef",
    "CreateAssessmentReportResponseTypeDef",
    "CreateAssessmentRequestRequestTypeDef",
    "CreateAssessmentResponseTypeDef",
    "CreateControlMappingSourceTypeDef",
    "CreateControlRequestRequestTypeDef",
    "CreateControlResponseTypeDef",
    "CreateDelegationRequestTypeDef",
    "DelegationMetadataTypeDef",
    "DelegationTypeDef",
    "DeleteAssessmentFrameworkRequestRequestTypeDef",
    "DeleteAssessmentReportRequestRequestTypeDef",
    "DeleteAssessmentRequestRequestTypeDef",
    "DeleteControlRequestRequestTypeDef",
    "DeregisterAccountResponseTypeDef",
    "DeregisterOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    "EvidenceTypeDef",
    "FrameworkMetadataTypeDef",
    "FrameworkTypeDef",
    "GetAccountStatusResponseTypeDef",
    "GetAssessmentFrameworkRequestRequestTypeDef",
    "GetAssessmentFrameworkResponseTypeDef",
    "GetAssessmentReportUrlRequestRequestTypeDef",
    "GetAssessmentReportUrlResponseTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetChangeLogsRequestRequestTypeDef",
    "GetChangeLogsResponseTypeDef",
    "GetControlRequestRequestTypeDef",
    "GetControlResponseTypeDef",
    "GetDelegationsRequestRequestTypeDef",
    "GetDelegationsResponseTypeDef",
    "GetEvidenceByEvidenceFolderRequestRequestTypeDef",
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    "GetEvidenceFolderRequestRequestTypeDef",
    "GetEvidenceFolderResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    "GetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    "GetEvidenceRequestRequestTypeDef",
    "GetEvidenceResponseTypeDef",
    "GetOrganizationAdminAccountResponseTypeDef",
    "GetServicesInScopeResponseTypeDef",
    "GetSettingsRequestRequestTypeDef",
    "GetSettingsResponseTypeDef",
    "ListAssessmentFrameworksRequestRequestTypeDef",
    "ListAssessmentFrameworksResponseTypeDef",
    "ListAssessmentReportsRequestRequestTypeDef",
    "ListAssessmentReportsResponseTypeDef",
    "ListAssessmentsRequestRequestTypeDef",
    "ListAssessmentsResponseTypeDef",
    "ListControlsRequestRequestTypeDef",
    "ListControlsResponseTypeDef",
    "ListKeywordsForDataSourceRequestRequestTypeDef",
    "ListKeywordsForDataSourceResponseTypeDef",
    "ListNotificationsRequestRequestTypeDef",
    "ListNotificationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManualEvidenceTypeDef",
    "NotificationTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "RegisterOrganizationAdminAccountRequestRequestTypeDef",
    "RegisterOrganizationAdminAccountResponseTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RoleTypeDef",
    "ScopeTypeDef",
    "ServiceMetadataTypeDef",
    "SettingsTypeDef",
    "SourceKeywordTypeDef",
    "TagResourceRequestRequestTypeDef",
    "URLTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssessmentControlRequestRequestTypeDef",
    "UpdateAssessmentControlResponseTypeDef",
    "UpdateAssessmentControlSetStatusRequestRequestTypeDef",
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkRequestRequestTypeDef",
    "UpdateAssessmentFrameworkResponseTypeDef",
    "UpdateAssessmentRequestRequestTypeDef",
    "UpdateAssessmentResponseTypeDef",
    "UpdateAssessmentStatusRequestRequestTypeDef",
    "UpdateAssessmentStatusResponseTypeDef",
    "UpdateControlRequestRequestTypeDef",
    "UpdateControlResponseTypeDef",
    "UpdateSettingsRequestRequestTypeDef",
    "UpdateSettingsResponseTypeDef",
    "ValidateAssessmentReportIntegrityRequestRequestTypeDef",
    "ValidateAssessmentReportIntegrityResponseTypeDef",
)

AWSAccountTypeDef = TypedDict(
    "AWSAccountTypeDef",
    {
        "id": str,
        "emailAddress": str,
        "name": str,
    },
    total=False,
)

AWSServiceTypeDef = TypedDict(
    "AWSServiceTypeDef",
    {
        "serviceName": str,
    },
    total=False,
)

AssessmentControlSetTypeDef = TypedDict(
    "AssessmentControlSetTypeDef",
    {
        "id": str,
        "description": str,
        "status": ControlSetStatusType,
        "roles": List["RoleTypeDef"],
        "controls": List["AssessmentControlTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "systemEvidenceCount": int,
        "manualEvidenceCount": int,
    },
    total=False,
)

AssessmentControlTypeDef = TypedDict(
    "AssessmentControlTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "status": ControlStatusType,
        "response": ControlResponseType,
        "comments": List["ControlCommentTypeDef"],
        "evidenceSources": List[str],
        "evidenceCount": int,
        "assessmentReportEvidenceCount": int,
    },
    total=False,
)

AssessmentEvidenceFolderTypeDef = TypedDict(
    "AssessmentEvidenceFolderTypeDef",
    {
        "name": str,
        "date": datetime,
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "id": str,
        "dataSource": str,
        "author": str,
        "totalEvidence": int,
        "assessmentReportSelectionCount": int,
        "controlName": str,
        "evidenceResourcesIncludedCount": int,
        "evidenceByTypeConfigurationDataCount": int,
        "evidenceByTypeManualCount": int,
        "evidenceByTypeComplianceCheckCount": int,
        "evidenceByTypeComplianceCheckIssuesCount": int,
        "evidenceByTypeUserActivityCount": int,
        "evidenceAwsServiceSourceCount": int,
    },
    total=False,
)

AssessmentFrameworkMetadataTypeDef = TypedDict(
    "AssessmentFrameworkMetadataTypeDef",
    {
        "arn": str,
        "id": str,
        "type": FrameworkTypeType,
        "name": str,
        "description": str,
        "logo": str,
        "complianceType": str,
        "controlsCount": int,
        "controlSetsCount": int,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

AssessmentFrameworkTypeDef = TypedDict(
    "AssessmentFrameworkTypeDef",
    {
        "id": str,
        "arn": str,
        "metadata": "FrameworkMetadataTypeDef",
        "controlSets": List["AssessmentControlSetTypeDef"],
    },
    total=False,
)

AssessmentMetadataItemTypeDef = TypedDict(
    "AssessmentMetadataItemTypeDef",
    {
        "name": str,
        "id": str,
        "complianceType": str,
        "status": AssessmentStatusType,
        "roles": List["RoleTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "creationTime": datetime,
        "lastUpdated": datetime,
    },
    total=False,
)

AssessmentMetadataTypeDef = TypedDict(
    "AssessmentMetadataTypeDef",
    {
        "name": str,
        "id": str,
        "description": str,
        "complianceType": str,
        "status": AssessmentStatusType,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "scope": "ScopeTypeDef",
        "roles": List["RoleTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "creationTime": datetime,
        "lastUpdated": datetime,
    },
    total=False,
)

AssessmentReportEvidenceErrorTypeDef = TypedDict(
    "AssessmentReportEvidenceErrorTypeDef",
    {
        "evidenceId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

AssessmentReportMetadataTypeDef = TypedDict(
    "AssessmentReportMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "assessmentId": str,
        "assessmentName": str,
        "author": str,
        "status": AssessmentReportStatusType,
        "creationTime": datetime,
    },
    total=False,
)

AssessmentReportTypeDef = TypedDict(
    "AssessmentReportTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "awsAccountId": str,
        "assessmentId": str,
        "assessmentName": str,
        "author": str,
        "status": AssessmentReportStatusType,
        "creationTime": datetime,
    },
    total=False,
)

AssessmentReportsDestinationTypeDef = TypedDict(
    "AssessmentReportsDestinationTypeDef",
    {
        "destinationType": Literal["S3"],
        "destination": str,
    },
    total=False,
)

AssessmentTypeDef = TypedDict(
    "AssessmentTypeDef",
    {
        "arn": str,
        "awsAccount": "AWSAccountTypeDef",
        "metadata": "AssessmentMetadataTypeDef",
        "framework": "AssessmentFrameworkTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef = TypedDict(
    "AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)

BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": List[str],
    },
)

BatchAssociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    {
        "createDelegationRequest": "CreateDelegationRequestTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchCreateDelegationByAssessmentRequestRequestTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentRequestRequestTypeDef",
    {
        "createDelegationRequests": List["CreateDelegationRequestTypeDef"],
        "assessmentId": str,
    },
)

BatchCreateDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    {
        "delegations": List["DelegationTypeDef"],
        "errors": List["BatchCreateDelegationByAssessmentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    {
        "delegationId": str,
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchDeleteDelegationByAssessmentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentRequestRequestTypeDef",
    {
        "delegationIds": List[str],
        "assessmentId": str,
    },
)

BatchDeleteDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    {
        "errors": List["BatchDeleteDelegationByAssessmentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": List[str],
    },
)

BatchDisassociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List["AssessmentReportEvidenceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchImportEvidenceToAssessmentControlErrorTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    {
        "manualEvidence": "ManualEvidenceTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

BatchImportEvidenceToAssessmentControlRequestRequestTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "manualEvidence": List["ManualEvidenceTypeDef"],
    },
)

BatchImportEvidenceToAssessmentControlResponseTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    {
        "errors": List["BatchImportEvidenceToAssessmentControlErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeLogTypeDef = TypedDict(
    "ChangeLogTypeDef",
    {
        "objectType": ObjectTypeEnumType,
        "objectName": str,
        "action": ActionEnumType,
        "createdAt": datetime,
        "createdBy": str,
    },
    total=False,
)

ControlCommentTypeDef = TypedDict(
    "ControlCommentTypeDef",
    {
        "authorName": str,
        "commentBody": str,
        "postedDate": datetime,
    },
    total=False,
)

ControlMappingSourceTypeDef = TypedDict(
    "ControlMappingSourceTypeDef",
    {
        "sourceId": str,
        "sourceName": str,
        "sourceDescription": str,
        "sourceSetUpOption": SourceSetUpOptionType,
        "sourceType": SourceTypeType,
        "sourceKeyword": "SourceKeywordTypeDef",
        "sourceFrequency": SourceFrequencyType,
        "troubleshootingText": str,
    },
    total=False,
)

ControlMetadataTypeDef = TypedDict(
    "ControlMetadataTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "controlSources": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

ControlSetTypeDef = TypedDict(
    "ControlSetTypeDef",
    {
        "id": str,
        "name": str,
        "controls": List["ControlTypeDef"],
    },
    total=False,
)

ControlTypeDef = TypedDict(
    "ControlTypeDef",
    {
        "arn": str,
        "id": str,
        "type": ControlTypeType,
        "name": str,
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
        "controlSources": str,
        "controlMappingSources": List["ControlMappingSourceTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_RequiredCreateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_OptionalCreateAssessmentFrameworkControlSetTypeDef",
    {
        "controls": List["CreateAssessmentFrameworkControlTypeDef"],
    },
    total=False,
)

class CreateAssessmentFrameworkControlSetTypeDef(
    _RequiredCreateAssessmentFrameworkControlSetTypeDef,
    _OptionalCreateAssessmentFrameworkControlSetTypeDef,
):
    pass

CreateAssessmentFrameworkControlTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlTypeDef",
    {
        "id": str,
    },
    total=False,
)

_RequiredCreateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentFrameworkRequestRequestTypeDef",
    {
        "name": str,
        "controlSets": List["CreateAssessmentFrameworkControlSetTypeDef"],
    },
)
_OptionalCreateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentFrameworkRequestRequestTypeDef",
    {
        "description": str,
        "complianceType": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAssessmentFrameworkRequestRequestTypeDef(
    _RequiredCreateAssessmentFrameworkRequestRequestTypeDef,
    _OptionalCreateAssessmentFrameworkRequestRequestTypeDef,
):
    pass

CreateAssessmentFrameworkResponseTypeDef = TypedDict(
    "CreateAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssessmentReportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentReportRequestRequestTypeDef",
    {
        "name": str,
        "assessmentId": str,
    },
)
_OptionalCreateAssessmentReportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentReportRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateAssessmentReportRequestRequestTypeDef(
    _RequiredCreateAssessmentReportRequestRequestTypeDef,
    _OptionalCreateAssessmentReportRequestRequestTypeDef,
):
    pass

CreateAssessmentReportResponseTypeDef = TypedDict(
    "CreateAssessmentReportResponseTypeDef",
    {
        "assessmentReport": "AssessmentReportTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssessmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssessmentRequestRequestTypeDef",
    {
        "name": str,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "scope": "ScopeTypeDef",
        "roles": List["RoleTypeDef"],
        "frameworkId": str,
    },
)
_OptionalCreateAssessmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssessmentRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAssessmentRequestRequestTypeDef(
    _RequiredCreateAssessmentRequestRequestTypeDef, _OptionalCreateAssessmentRequestRequestTypeDef
):
    pass

CreateAssessmentResponseTypeDef = TypedDict(
    "CreateAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateControlMappingSourceTypeDef = TypedDict(
    "CreateControlMappingSourceTypeDef",
    {
        "sourceName": str,
        "sourceDescription": str,
        "sourceSetUpOption": SourceSetUpOptionType,
        "sourceType": SourceTypeType,
        "sourceKeyword": "SourceKeywordTypeDef",
        "sourceFrequency": SourceFrequencyType,
        "troubleshootingText": str,
    },
    total=False,
)

_RequiredCreateControlRequestRequestTypeDef = TypedDict(
    "_RequiredCreateControlRequestRequestTypeDef",
    {
        "name": str,
        "controlMappingSources": List["CreateControlMappingSourceTypeDef"],
    },
)
_OptionalCreateControlRequestRequestTypeDef = TypedDict(
    "_OptionalCreateControlRequestRequestTypeDef",
    {
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateControlRequestRequestTypeDef(
    _RequiredCreateControlRequestRequestTypeDef, _OptionalCreateControlRequestRequestTypeDef
):
    pass

CreateControlResponseTypeDef = TypedDict(
    "CreateControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDelegationRequestTypeDef = TypedDict(
    "CreateDelegationRequestTypeDef",
    {
        "comment": str,
        "controlSetId": str,
        "roleArn": str,
        "roleType": RoleTypeType,
    },
    total=False,
)

DelegationMetadataTypeDef = TypedDict(
    "DelegationMetadataTypeDef",
    {
        "id": str,
        "assessmentName": str,
        "assessmentId": str,
        "status": DelegationStatusType,
        "roleArn": str,
        "creationTime": datetime,
        "controlSetName": str,
    },
    total=False,
)

DelegationTypeDef = TypedDict(
    "DelegationTypeDef",
    {
        "id": str,
        "assessmentName": str,
        "assessmentId": str,
        "status": DelegationStatusType,
        "roleArn": str,
        "roleType": RoleTypeType,
        "creationTime": datetime,
        "lastUpdated": datetime,
        "controlSetId": str,
        "comment": str,
        "createdBy": str,
    },
    total=False,
)

DeleteAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
    },
)

DeleteAssessmentReportRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentReportRequestRequestTypeDef",
    {
        "assessmentId": str,
        "assessmentReportId": str,
    },
)

DeleteAssessmentRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

DeleteControlRequestRequestTypeDef = TypedDict(
    "DeleteControlRequestRequestTypeDef",
    {
        "controlId": str,
    },
)

DeregisterAccountResponseTypeDef = TypedDict(
    "DeregisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DeregisterOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
    total=False,
)

DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef = TypedDict(
    "DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)

EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "dataSource": str,
        "evidenceAwsAccountId": str,
        "time": datetime,
        "eventSource": str,
        "eventName": str,
        "evidenceByType": str,
        "resourcesIncluded": List["ResourceTypeDef"],
        "attributes": Dict[str, str],
        "iamId": str,
        "complianceCheck": str,
        "awsOrganization": str,
        "awsAccountId": str,
        "evidenceFolderId": str,
        "id": str,
        "assessmentReportSelection": str,
    },
    total=False,
)

FrameworkMetadataTypeDef = TypedDict(
    "FrameworkMetadataTypeDef",
    {
        "name": str,
        "description": str,
        "logo": str,
        "complianceType": str,
    },
    total=False,
)

FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "type": FrameworkTypeType,
        "complianceType": str,
        "description": str,
        "logo": str,
        "controlSources": str,
        "controlSets": List["ControlSetTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GetAccountStatusResponseTypeDef = TypedDict(
    "GetAccountStatusResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "GetAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
    },
)

GetAssessmentFrameworkResponseTypeDef = TypedDict(
    "GetAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentReportUrlRequestRequestTypeDef = TypedDict(
    "GetAssessmentReportUrlRequestRequestTypeDef",
    {
        "assessmentReportId": str,
        "assessmentId": str,
    },
)

GetAssessmentReportUrlResponseTypeDef = TypedDict(
    "GetAssessmentReportUrlResponseTypeDef",
    {
        "preSignedUrl": "URLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)

GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "userRole": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetChangeLogsRequestRequestTypeDef = TypedDict(
    "_RequiredGetChangeLogsRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
_OptionalGetChangeLogsRequestRequestTypeDef = TypedDict(
    "_OptionalGetChangeLogsRequestRequestTypeDef",
    {
        "controlSetId": str,
        "controlId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetChangeLogsRequestRequestTypeDef(
    _RequiredGetChangeLogsRequestRequestTypeDef, _OptionalGetChangeLogsRequestRequestTypeDef
):
    pass

GetChangeLogsResponseTypeDef = TypedDict(
    "GetChangeLogsResponseTypeDef",
    {
        "changeLogs": List["ChangeLogTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetControlRequestRequestTypeDef = TypedDict(
    "GetControlRequestRequestTypeDef",
    {
        "controlId": str,
    },
)

GetControlResponseTypeDef = TypedDict(
    "GetControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDelegationsRequestRequestTypeDef = TypedDict(
    "GetDelegationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetDelegationsResponseTypeDef = TypedDict(
    "GetDelegationsResponseTypeDef",
    {
        "delegations": List["DelegationMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEvidenceByEvidenceFolderRequestRequestTypeDef = TypedDict(
    "_RequiredGetEvidenceByEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
    },
)
_OptionalGetEvidenceByEvidenceFolderRequestRequestTypeDef = TypedDict(
    "_OptionalGetEvidenceByEvidenceFolderRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetEvidenceByEvidenceFolderRequestRequestTypeDef(
    _RequiredGetEvidenceByEvidenceFolderRequestRequestTypeDef,
    _OptionalGetEvidenceByEvidenceFolderRequestRequestTypeDef,
):
    pass

GetEvidenceByEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    {
        "evidence": List["EvidenceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceFolderRequestRequestTypeDef = TypedDict(
    "GetEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
    },
)

GetEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceFolderResponseTypeDef",
    {
        "evidenceFolder": "AssessmentEvidenceFolderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEvidenceFoldersByAssessmentControlRequestRequestTypeDef = TypedDict(
    "_RequiredGetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
    },
)
_OptionalGetEvidenceFoldersByAssessmentControlRequestRequestTypeDef = TypedDict(
    "_OptionalGetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef(
    _RequiredGetEvidenceFoldersByAssessmentControlRequestRequestTypeDef,
    _OptionalGetEvidenceFoldersByAssessmentControlRequestRequestTypeDef,
):
    pass

GetEvidenceFoldersByAssessmentControlResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetEvidenceFoldersByAssessmentRequestRequestTypeDef = TypedDict(
    "_RequiredGetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
_OptionalGetEvidenceFoldersByAssessmentRequestRequestTypeDef = TypedDict(
    "_OptionalGetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetEvidenceFoldersByAssessmentRequestRequestTypeDef(
    _RequiredGetEvidenceFoldersByAssessmentRequestRequestTypeDef,
    _OptionalGetEvidenceFoldersByAssessmentRequestRequestTypeDef,
):
    pass

GetEvidenceFoldersByAssessmentResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    {
        "evidenceFolders": List["AssessmentEvidenceFolderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvidenceRequestRequestTypeDef = TypedDict(
    "GetEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
        "evidenceId": str,
    },
)

GetEvidenceResponseTypeDef = TypedDict(
    "GetEvidenceResponseTypeDef",
    {
        "evidence": "EvidenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrganizationAdminAccountResponseTypeDef = TypedDict(
    "GetOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServicesInScopeResponseTypeDef = TypedDict(
    "GetServicesInScopeResponseTypeDef",
    {
        "serviceMetadata": List["ServiceMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSettingsRequestRequestTypeDef = TypedDict(
    "GetSettingsRequestRequestTypeDef",
    {
        "attribute": SettingAttributeType,
    },
)

GetSettingsResponseTypeDef = TypedDict(
    "GetSettingsResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssessmentFrameworksRequestRequestTypeDef = TypedDict(
    "_RequiredListAssessmentFrameworksRequestRequestTypeDef",
    {
        "frameworkType": FrameworkTypeType,
    },
)
_OptionalListAssessmentFrameworksRequestRequestTypeDef = TypedDict(
    "_OptionalListAssessmentFrameworksRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssessmentFrameworksRequestRequestTypeDef(
    _RequiredListAssessmentFrameworksRequestRequestTypeDef,
    _OptionalListAssessmentFrameworksRequestRequestTypeDef,
):
    pass

ListAssessmentFrameworksResponseTypeDef = TypedDict(
    "ListAssessmentFrameworksResponseTypeDef",
    {
        "frameworkMetadataList": List["AssessmentFrameworkMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentReportsRequestRequestTypeDef = TypedDict(
    "ListAssessmentReportsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentReportsResponseTypeDef = TypedDict(
    "ListAssessmentReportsResponseTypeDef",
    {
        "assessmentReports": List["AssessmentReportMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssessmentsRequestRequestTypeDef = TypedDict(
    "ListAssessmentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAssessmentsResponseTypeDef = TypedDict(
    "ListAssessmentsResponseTypeDef",
    {
        "assessmentMetadata": List["AssessmentMetadataItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListControlsRequestRequestTypeDef = TypedDict(
    "_RequiredListControlsRequestRequestTypeDef",
    {
        "controlType": ControlTypeType,
    },
)
_OptionalListControlsRequestRequestTypeDef = TypedDict(
    "_OptionalListControlsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListControlsRequestRequestTypeDef(
    _RequiredListControlsRequestRequestTypeDef, _OptionalListControlsRequestRequestTypeDef
):
    pass

ListControlsResponseTypeDef = TypedDict(
    "ListControlsResponseTypeDef",
    {
        "controlMetadataList": List["ControlMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListKeywordsForDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredListKeywordsForDataSourceRequestRequestTypeDef",
    {
        "source": SourceTypeType,
    },
)
_OptionalListKeywordsForDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalListKeywordsForDataSourceRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListKeywordsForDataSourceRequestRequestTypeDef(
    _RequiredListKeywordsForDataSourceRequestRequestTypeDef,
    _OptionalListKeywordsForDataSourceRequestRequestTypeDef,
):
    pass

ListKeywordsForDataSourceResponseTypeDef = TypedDict(
    "ListKeywordsForDataSourceResponseTypeDef",
    {
        "keywords": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationsRequestRequestTypeDef = TypedDict(
    "ListNotificationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListNotificationsResponseTypeDef = TypedDict(
    "ListNotificationsResponseTypeDef",
    {
        "notifications": List["NotificationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManualEvidenceTypeDef = TypedDict(
    "ManualEvidenceTypeDef",
    {
        "s3ResourcePath": str,
    },
    total=False,
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "id": str,
        "assessmentId": str,
        "assessmentName": str,
        "controlSetId": str,
        "controlSetName": str,
        "description": str,
        "eventTime": datetime,
        "source": str,
    },
    total=False,
)

RegisterAccountRequestRequestTypeDef = TypedDict(
    "RegisterAccountRequestRequestTypeDef",
    {
        "kmsKey": str,
        "delegatedAdminAccount": str,
    },
    total=False,
)

RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)

RegisterOrganizationAdminAccountResponseTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "value": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RoleTypeDef = TypedDict(
    "RoleTypeDef",
    {
        "roleType": RoleTypeType,
        "roleArn": str,
    },
    total=False,
)

ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "awsAccounts": List["AWSAccountTypeDef"],
        "awsServices": List["AWSServiceTypeDef"],
    },
    total=False,
)

ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "name": str,
        "displayName": str,
        "description": str,
        "category": str,
    },
    total=False,
)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "isAwsOrgEnabled": bool,
        "snsTopic": str,
        "defaultAssessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "defaultProcessOwners": List["RoleTypeDef"],
        "kmsKey": str,
    },
    total=False,
)

SourceKeywordTypeDef = TypedDict(
    "SourceKeywordTypeDef",
    {
        "keywordInputType": Literal["SELECT_FROM_LIST"],
        "keywordValue": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

URLTypeDef = TypedDict(
    "URLTypeDef",
    {
        "hyperlinkName": str,
        "link": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAssessmentControlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
    },
)
_OptionalUpdateAssessmentControlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentControlRequestRequestTypeDef",
    {
        "controlStatus": ControlStatusType,
        "commentBody": str,
    },
    total=False,
)

class UpdateAssessmentControlRequestRequestTypeDef(
    _RequiredUpdateAssessmentControlRequestRequestTypeDef,
    _OptionalUpdateAssessmentControlRequestRequestTypeDef,
):
    pass

UpdateAssessmentControlResponseTypeDef = TypedDict(
    "UpdateAssessmentControlResponseTypeDef",
    {
        "control": "AssessmentControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentControlSetStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "status": ControlSetStatusType,
        "comment": str,
    },
)

UpdateAssessmentControlSetStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    {
        "controlSet": "AssessmentControlSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_RequiredUpdateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_OptionalUpdateAssessmentFrameworkControlSetTypeDef",
    {
        "id": str,
        "controls": List["CreateAssessmentFrameworkControlTypeDef"],
    },
    total=False,
)

class UpdateAssessmentFrameworkControlSetTypeDef(
    _RequiredUpdateAssessmentFrameworkControlSetTypeDef,
    _OptionalUpdateAssessmentFrameworkControlSetTypeDef,
):
    pass

_RequiredUpdateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
        "name": str,
        "controlSets": List["UpdateAssessmentFrameworkControlSetTypeDef"],
    },
)
_OptionalUpdateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentFrameworkRequestRequestTypeDef",
    {
        "description": str,
        "complianceType": str,
    },
    total=False,
)

class UpdateAssessmentFrameworkRequestRequestTypeDef(
    _RequiredUpdateAssessmentFrameworkRequestRequestTypeDef,
    _OptionalUpdateAssessmentFrameworkRequestRequestTypeDef,
):
    pass

UpdateAssessmentFrameworkResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkResponseTypeDef",
    {
        "framework": "FrameworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssessmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "scope": "ScopeTypeDef",
    },
)
_OptionalUpdateAssessmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssessmentRequestRequestTypeDef",
    {
        "assessmentName": str,
        "assessmentDescription": str,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "roles": List["RoleTypeDef"],
    },
    total=False,
)

class UpdateAssessmentRequestRequestTypeDef(
    _RequiredUpdateAssessmentRequestRequestTypeDef, _OptionalUpdateAssessmentRequestRequestTypeDef
):
    pass

UpdateAssessmentResponseTypeDef = TypedDict(
    "UpdateAssessmentResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssessmentStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentStatusRequestRequestTypeDef",
    {
        "assessmentId": str,
        "status": AssessmentStatusType,
    },
)

UpdateAssessmentStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentStatusResponseTypeDef",
    {
        "assessment": "AssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateControlRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateControlRequestRequestTypeDef",
    {
        "controlId": str,
        "name": str,
        "controlMappingSources": List["ControlMappingSourceTypeDef"],
    },
)
_OptionalUpdateControlRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateControlRequestRequestTypeDef",
    {
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
    },
    total=False,
)

class UpdateControlRequestRequestTypeDef(
    _RequiredUpdateControlRequestRequestTypeDef, _OptionalUpdateControlRequestRequestTypeDef
):
    pass

UpdateControlResponseTypeDef = TypedDict(
    "UpdateControlResponseTypeDef",
    {
        "control": "ControlTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSettingsRequestRequestTypeDef = TypedDict(
    "UpdateSettingsRequestRequestTypeDef",
    {
        "snsTopic": str,
        "defaultAssessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "defaultProcessOwners": List["RoleTypeDef"],
        "kmsKey": str,
    },
    total=False,
)

UpdateSettingsResponseTypeDef = TypedDict(
    "UpdateSettingsResponseTypeDef",
    {
        "settings": "SettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateAssessmentReportIntegrityRequestRequestTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityRequestRequestTypeDef",
    {
        "s3RelativePath": str,
    },
)

ValidateAssessmentReportIntegrityResponseTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityResponseTypeDef",
    {
        "signatureValid": bool,
        "signatureAlgorithm": str,
        "signatureDateTime": str,
        "signatureKeyId": str,
        "validationErrors": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
