"""
Type annotations for partnercentral-selling service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_selling/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_partnercentral_selling.type_defs import AcceptEngagementInvitationRequestTypeDef

    data: AcceptEngagementInvitationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AwsClosedLostReasonType,
    AwsFundingUsedType,
    AwsMemberBusinessTitleType,
    AwsOpportunityStageType,
    ChannelType,
    ClosedLostReasonType,
    CompetitorNameType,
    CountryCodeType,
    CurrencyCodeType,
    DeliveryModelType,
    EngagementScoreType,
    ExpectedCustomerSpendCurrencyCodeEnumType,
    IndustryType,
    InvitationStatusType,
    InvolvementTypeChangeReasonType,
    MarketingSourceType,
    NationalSecurityType,
    OpportunityOriginType,
    OpportunitySortNameType,
    OpportunityTypeType,
    ParticipantTypeType,
    PrimaryNeedFromAwsType,
    ReasonCodeType,
    ReceiverResponsibilityType,
    RelatedEntityTypeType,
    ResourceSnapshotJobStatusType,
    RevenueModelType,
    ReviewStatusType,
    SalesActivityType,
    SalesInvolvementTypeType,
    SolutionSortNameType,
    SolutionStatusType,
    SortOrderType,
    StageType,
    TaskStatusType,
    VisibilityType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptEngagementInvitationRequestTypeDef",
    "AccountReceiverTypeDef",
    "AccountSummaryTypeDef",
    "AccountTypeDef",
    "AddressSummaryTypeDef",
    "AddressTypeDef",
    "AssignOpportunityRequestTypeDef",
    "AssigneeContactTypeDef",
    "AssociateOpportunityRequestTypeDef",
    "AwsOpportunityCustomerTypeDef",
    "AwsOpportunityInsightsTypeDef",
    "AwsOpportunityLifeCycleTypeDef",
    "AwsOpportunityProjectTypeDef",
    "AwsOpportunityRelatedEntitiesTypeDef",
    "AwsSubmissionTypeDef",
    "AwsTeamMemberTypeDef",
    "ContactTypeDef",
    "CreateEngagementInvitationRequestTypeDef",
    "CreateEngagementInvitationResponseTypeDef",
    "CreateEngagementRequestTypeDef",
    "CreateEngagementResponseTypeDef",
    "CreateOpportunityRequestTypeDef",
    "CreateOpportunityResponseTypeDef",
    "CreateResourceSnapshotJobRequestTypeDef",
    "CreateResourceSnapshotJobResponseTypeDef",
    "CreateResourceSnapshotRequestTypeDef",
    "CreateResourceSnapshotResponseTypeDef",
    "CustomerOutputTypeDef",
    "CustomerProjectsContextTypeDef",
    "CustomerSummaryTypeDef",
    "CustomerTypeDef",
    "CustomerUnionTypeDef",
    "DeleteResourceSnapshotJobRequestTypeDef",
    "DisassociateOpportunityRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EngagementContextDetailsTypeDef",
    "EngagementContextPayloadTypeDef",
    "EngagementCustomerProjectDetailsTypeDef",
    "EngagementCustomerTypeDef",
    "EngagementInvitationSummaryTypeDef",
    "EngagementMemberSummaryTypeDef",
    "EngagementMemberTypeDef",
    "EngagementResourceAssociationSummaryTypeDef",
    "EngagementSortTypeDef",
    "EngagementSummaryTypeDef",
    "ExpectedCustomerSpendTypeDef",
    "GetAwsOpportunitySummaryRequestTypeDef",
    "GetAwsOpportunitySummaryResponseTypeDef",
    "GetEngagementInvitationRequestTypeDef",
    "GetEngagementInvitationResponseTypeDef",
    "GetEngagementRequestTypeDef",
    "GetEngagementResponseTypeDef",
    "GetOpportunityRequestTypeDef",
    "GetOpportunityResponseTypeDef",
    "GetResourceSnapshotJobRequestTypeDef",
    "GetResourceSnapshotJobResponseTypeDef",
    "GetResourceSnapshotRequestTypeDef",
    "GetResourceSnapshotResponseTypeDef",
    "GetSellingSystemSettingsRequestTypeDef",
    "GetSellingSystemSettingsResponseTypeDef",
    "InvitationTypeDef",
    "LastModifiedDateTypeDef",
    "LifeCycleForViewTypeDef",
    "LifeCycleOutputTypeDef",
    "LifeCycleSummaryTypeDef",
    "LifeCycleTypeDef",
    "LifeCycleUnionTypeDef",
    "ListEngagementByAcceptingInvitationTaskSummaryTypeDef",
    "ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef",
    "ListEngagementByAcceptingInvitationTasksRequestTypeDef",
    "ListEngagementByAcceptingInvitationTasksResponseTypeDef",
    "ListEngagementFromOpportunityTaskSummaryTypeDef",
    "ListEngagementFromOpportunityTasksRequestPaginateTypeDef",
    "ListEngagementFromOpportunityTasksRequestTypeDef",
    "ListEngagementFromOpportunityTasksResponseTypeDef",
    "ListEngagementInvitationsRequestPaginateTypeDef",
    "ListEngagementInvitationsRequestTypeDef",
    "ListEngagementInvitationsResponseTypeDef",
    "ListEngagementMembersRequestPaginateTypeDef",
    "ListEngagementMembersRequestTypeDef",
    "ListEngagementMembersResponseTypeDef",
    "ListEngagementResourceAssociationsRequestPaginateTypeDef",
    "ListEngagementResourceAssociationsRequestTypeDef",
    "ListEngagementResourceAssociationsResponseTypeDef",
    "ListEngagementsRequestPaginateTypeDef",
    "ListEngagementsRequestTypeDef",
    "ListEngagementsResponseTypeDef",
    "ListOpportunitiesRequestPaginateTypeDef",
    "ListOpportunitiesRequestTypeDef",
    "ListOpportunitiesResponseTypeDef",
    "ListResourceSnapshotJobsRequestPaginateTypeDef",
    "ListResourceSnapshotJobsRequestTypeDef",
    "ListResourceSnapshotJobsResponseTypeDef",
    "ListResourceSnapshotsRequestPaginateTypeDef",
    "ListResourceSnapshotsRequestTypeDef",
    "ListResourceSnapshotsResponseTypeDef",
    "ListSolutionsRequestPaginateTypeDef",
    "ListSolutionsRequestTypeDef",
    "ListSolutionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTasksSortBaseTypeDef",
    "MarketingOutputTypeDef",
    "MarketingTypeDef",
    "MarketingUnionTypeDef",
    "MonetaryValueTypeDef",
    "NextStepsHistoryOutputTypeDef",
    "NextStepsHistoryTypeDef",
    "OpportunityEngagementInvitationSortTypeDef",
    "OpportunityInvitationPayloadOutputTypeDef",
    "OpportunityInvitationPayloadTypeDef",
    "OpportunityInvitationPayloadUnionTypeDef",
    "OpportunitySortTypeDef",
    "OpportunitySummaryTypeDef",
    "OpportunitySummaryViewTypeDef",
    "PaginatorConfigTypeDef",
    "PayloadOutputTypeDef",
    "PayloadTypeDef",
    "PayloadUnionTypeDef",
    "ProfileNextStepsHistoryTypeDef",
    "ProjectDetailsOutputTypeDef",
    "ProjectDetailsTypeDef",
    "ProjectDetailsUnionTypeDef",
    "ProjectOutputTypeDef",
    "ProjectSummaryTypeDef",
    "ProjectTypeDef",
    "ProjectUnionTypeDef",
    "ProjectViewTypeDef",
    "PutSellingSystemSettingsRequestTypeDef",
    "PutSellingSystemSettingsResponseTypeDef",
    "ReceiverTypeDef",
    "RejectEngagementInvitationRequestTypeDef",
    "RelatedEntityIdentifiersTypeDef",
    "ResourceSnapshotJobSummaryTypeDef",
    "ResourceSnapshotPayloadTypeDef",
    "ResourceSnapshotSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SenderContactTypeDef",
    "SoftwareRevenueTypeDef",
    "SolutionBaseTypeDef",
    "SolutionSortTypeDef",
    "SortObjectTypeDef",
    "StartEngagementByAcceptingInvitationTaskRequestTypeDef",
    "StartEngagementByAcceptingInvitationTaskResponseTypeDef",
    "StartEngagementFromOpportunityTaskRequestTypeDef",
    "StartEngagementFromOpportunityTaskResponseTypeDef",
    "StartResourceSnapshotJobRequestTypeDef",
    "StopResourceSnapshotJobRequestTypeDef",
    "SubmitOpportunityRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateOpportunityRequestTypeDef",
    "UpdateOpportunityResponseTypeDef",
)

class AcceptEngagementInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class AccountReceiverTypeDef(TypedDict):
    AwsAccountId: str
    Alias: NotRequired[str]

class AddressSummaryTypeDef(TypedDict):
    City: NotRequired[str]
    CountryCode: NotRequired[CountryCodeType]
    PostalCode: NotRequired[str]
    StateOrRegion: NotRequired[str]

class AddressTypeDef(TypedDict):
    City: NotRequired[str]
    CountryCode: NotRequired[CountryCodeType]
    PostalCode: NotRequired[str]
    StateOrRegion: NotRequired[str]
    StreetAddress: NotRequired[str]

class AssigneeContactTypeDef(TypedDict):
    BusinessTitle: str
    Email: str
    FirstName: str
    LastName: str

class AssociateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType

class ContactTypeDef(TypedDict):
    BusinessTitle: NotRequired[str]
    Email: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    Phone: NotRequired[str]

class AwsOpportunityInsightsTypeDef(TypedDict):
    EngagementScore: NotRequired[EngagementScoreType]
    NextBestActions: NotRequired[str]

class ProfileNextStepsHistoryTypeDef(TypedDict):
    Time: datetime
    Value: str

class ExpectedCustomerSpendTypeDef(TypedDict):
    Amount: str
    CurrencyCode: ExpectedCustomerSpendCurrencyCodeEnumType
    Frequency: Literal["Monthly"]
    TargetCompany: str
    EstimationUrl: NotRequired[str]

class AwsOpportunityRelatedEntitiesTypeDef(TypedDict):
    AwsProducts: NotRequired[List[str]]
    Solutions: NotRequired[List[str]]

class AwsSubmissionTypeDef(TypedDict):
    InvolvementType: SalesInvolvementTypeType
    Visibility: NotRequired[VisibilityType]

class AwsTeamMemberTypeDef(TypedDict):
    BusinessTitle: NotRequired[AwsMemberBusinessTitleType]
    Email: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateResourceSnapshotRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal["Opportunity"]

class EngagementCustomerProjectDetailsTypeDef(TypedDict):
    BusinessProblem: str
    TargetCompletionDate: str
    Title: str

class EngagementCustomerTypeDef(TypedDict):
    CompanyName: str
    CountryCode: CountryCodeType
    Industry: IndustryType
    WebsiteUrl: str

class DeleteResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobIdentifier: str

class DisassociateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType

class EngagementMemberSummaryTypeDef(TypedDict):
    CompanyName: NotRequired[str]
    WebsiteUrl: NotRequired[str]

class EngagementMemberTypeDef(TypedDict):
    AccountId: NotRequired[str]
    CompanyName: NotRequired[str]
    WebsiteUrl: NotRequired[str]

class EngagementResourceAssociationSummaryTypeDef(TypedDict):
    Catalog: str
    CreatedBy: NotRequired[str]
    EngagementId: NotRequired[str]
    ResourceId: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]

class EngagementSortTypeDef(TypedDict):
    SortBy: Literal["CreatedDate"]
    SortOrder: SortOrderType

class EngagementSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    CreatedBy: NotRequired[str]
    Id: NotRequired[str]
    MemberCount: NotRequired[int]
    Title: NotRequired[str]

class GetAwsOpportunitySummaryRequestTypeDef(TypedDict):
    Catalog: str
    RelatedOpportunityIdentifier: str

class GetEngagementInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetEngagementRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class GetOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str

class MarketingOutputTypeDef(TypedDict):
    AwsFundingUsed: NotRequired[AwsFundingUsedType]
    CampaignName: NotRequired[str]
    Channels: NotRequired[List[ChannelType]]
    Source: NotRequired[MarketingSourceType]
    UseCases: NotRequired[List[str]]

class RelatedEntityIdentifiersTypeDef(TypedDict):
    AwsMarketplaceOffers: NotRequired[List[str]]
    AwsProducts: NotRequired[List[str]]
    Solutions: NotRequired[List[str]]

class GetResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobIdentifier: str

class GetResourceSnapshotRequestTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal["Opportunity"]
    Revision: NotRequired[int]

class GetSellingSystemSettingsRequestTypeDef(TypedDict):
    Catalog: str

TimestampTypeDef = Union[datetime, str]

class LifeCycleForViewTypeDef(TypedDict):
    NextSteps: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    Stage: NotRequired[StageType]
    TargetCloseDate: NotRequired[str]

class NextStepsHistoryOutputTypeDef(TypedDict):
    Time: datetime
    Value: str

class LifeCycleSummaryTypeDef(TypedDict):
    ClosedLostReason: NotRequired[ClosedLostReasonType]
    NextSteps: NotRequired[str]
    ReviewComments: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    ReviewStatusReason: NotRequired[str]
    Stage: NotRequired[StageType]
    TargetCloseDate: NotRequired[str]

class ListEngagementByAcceptingInvitationTaskSummaryTypeDef(TypedDict):
    EngagementInvitationId: NotRequired[str]
    Message: NotRequired[str]
    OpportunityId: NotRequired[str]
    ReasonCode: NotRequired[ReasonCodeType]
    ResourceSnapshotJobId: NotRequired[str]
    StartTime: NotRequired[datetime]
    TaskArn: NotRequired[str]
    TaskId: NotRequired[str]
    TaskStatus: NotRequired[TaskStatusType]

class ListTasksSortBaseTypeDef(TypedDict):
    SortBy: Literal["StartTime"]
    SortOrder: SortOrderType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEngagementFromOpportunityTaskSummaryTypeDef(TypedDict):
    EngagementId: NotRequired[str]
    EngagementInvitationId: NotRequired[str]
    Message: NotRequired[str]
    OpportunityId: NotRequired[str]
    ReasonCode: NotRequired[ReasonCodeType]
    ResourceSnapshotJobId: NotRequired[str]
    StartTime: NotRequired[datetime]
    TaskArn: NotRequired[str]
    TaskId: NotRequired[str]
    TaskStatus: NotRequired[TaskStatusType]

class OpportunityEngagementInvitationSortTypeDef(TypedDict):
    SortBy: Literal["InvitationDate"]
    SortOrder: SortOrderType

class ListEngagementMembersRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListEngagementResourceAssociationsRequestTypeDef(TypedDict):
    Catalog: str
    CreatedBy: NotRequired[str]
    EngagementIdentifier: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]

class OpportunitySortTypeDef(TypedDict):
    SortBy: OpportunitySortNameType
    SortOrder: SortOrderType

class SortObjectTypeDef(TypedDict):
    SortBy: NotRequired[Literal["CreatedDate"]]
    SortOrder: NotRequired[SortOrderType]

class ResourceSnapshotJobSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    EngagementId: NotRequired[str]
    Id: NotRequired[str]
    Status: NotRequired[ResourceSnapshotJobStatusType]

class ListResourceSnapshotsRequestTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: str
    CreatedBy: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    ResourceSnapshotTemplateIdentifier: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]

class ResourceSnapshotSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedBy: NotRequired[str]
    ResourceId: NotRequired[str]
    ResourceSnapshotTemplateName: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    Revision: NotRequired[int]

class SolutionSortTypeDef(TypedDict):
    SortBy: SolutionSortNameType
    SortOrder: SortOrderType

class SolutionBaseTypeDef(TypedDict):
    Catalog: str
    Category: str
    CreatedDate: datetime
    Id: str
    Name: str
    Status: SolutionStatusType
    Arn: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class MarketingTypeDef(TypedDict):
    AwsFundingUsed: NotRequired[AwsFundingUsedType]
    CampaignName: NotRequired[str]
    Channels: NotRequired[Sequence[ChannelType]]
    Source: NotRequired[MarketingSourceType]
    UseCases: NotRequired[Sequence[str]]

class MonetaryValueTypeDef(TypedDict):
    Amount: str
    CurrencyCode: CurrencyCodeType

class SenderContactTypeDef(TypedDict):
    Email: str
    BusinessTitle: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    Phone: NotRequired[str]

class PutSellingSystemSettingsRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobRoleIdentifier: NotRequired[str]

class RejectEngagementInvitationRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    RejectionReason: NotRequired[str]

class StartResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobIdentifier: str

class StopResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobIdentifier: str

class SubmitOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    InvolvementType: SalesInvolvementTypeType
    Visibility: NotRequired[VisibilityType]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ReceiverTypeDef(TypedDict):
    Account: NotRequired[AccountReceiverTypeDef]

class AccountSummaryTypeDef(TypedDict):
    CompanyName: str
    Address: NotRequired[AddressSummaryTypeDef]
    Industry: NotRequired[IndustryType]
    OtherIndustry: NotRequired[str]
    WebsiteUrl: NotRequired[str]

class AccountTypeDef(TypedDict):
    CompanyName: str
    Address: NotRequired[AddressTypeDef]
    AwsAccountId: NotRequired[str]
    Duns: NotRequired[str]
    Industry: NotRequired[IndustryType]
    OtherIndustry: NotRequired[str]
    WebsiteUrl: NotRequired[str]

class AssignOpportunityRequestTypeDef(TypedDict):
    Assignee: AssigneeContactTypeDef
    Catalog: str
    Identifier: str

class AwsOpportunityCustomerTypeDef(TypedDict):
    Contacts: NotRequired[List[ContactTypeDef]]

class AwsOpportunityLifeCycleTypeDef(TypedDict):
    ClosedLostReason: NotRequired[AwsClosedLostReasonType]
    NextSteps: NotRequired[str]
    NextStepsHistory: NotRequired[List[ProfileNextStepsHistoryTypeDef]]
    Stage: NotRequired[AwsOpportunityStageType]
    TargetCloseDate: NotRequired[str]

class AwsOpportunityProjectTypeDef(TypedDict):
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]

class ProjectDetailsOutputTypeDef(TypedDict):
    BusinessProblem: str
    ExpectedCustomerSpend: List[ExpectedCustomerSpendTypeDef]
    TargetCompletionDate: str
    Title: str

class ProjectDetailsTypeDef(TypedDict):
    BusinessProblem: str
    ExpectedCustomerSpend: Sequence[ExpectedCustomerSpendTypeDef]
    TargetCompletionDate: str
    Title: str

class ProjectOutputTypeDef(TypedDict):
    AdditionalComments: NotRequired[str]
    ApnPrograms: NotRequired[List[str]]
    CompetitorName: NotRequired[CompetitorNameType]
    CustomerBusinessProblem: NotRequired[str]
    CustomerUseCase: NotRequired[str]
    DeliveryModels: NotRequired[List[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]
    OtherCompetitorNames: NotRequired[str]
    OtherSolutionDescription: NotRequired[str]
    RelatedOpportunityIdentifier: NotRequired[str]
    SalesActivities: NotRequired[List[SalesActivityType]]
    Title: NotRequired[str]

class ProjectSummaryTypeDef(TypedDict):
    DeliveryModels: NotRequired[List[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]

class ProjectTypeDef(TypedDict):
    AdditionalComments: NotRequired[str]
    ApnPrograms: NotRequired[Sequence[str]]
    CompetitorName: NotRequired[CompetitorNameType]
    CustomerBusinessProblem: NotRequired[str]
    CustomerUseCase: NotRequired[str]
    DeliveryModels: NotRequired[Sequence[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[Sequence[ExpectedCustomerSpendTypeDef]]
    OtherCompetitorNames: NotRequired[str]
    OtherSolutionDescription: NotRequired[str]
    RelatedOpportunityIdentifier: NotRequired[str]
    SalesActivities: NotRequired[Sequence[SalesActivityType]]
    Title: NotRequired[str]

class ProjectViewTypeDef(TypedDict):
    CustomerUseCase: NotRequired[str]
    DeliveryModels: NotRequired[List[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]
    OtherSolutionDescription: NotRequired[str]
    SalesActivities: NotRequired[List[SalesActivityType]]

class CreateEngagementInvitationResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEngagementResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOpportunityResponseTypeDef(TypedDict):
    Id: str
    LastModifiedDate: datetime
    PartnerOpportunityIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceSnapshotJobResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceSnapshotResponseTypeDef(TypedDict):
    Arn: str
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSnapshotJobResponseTypeDef(TypedDict):
    Arn: str
    Catalog: str
    CreatedAt: datetime
    EngagementId: str
    Id: str
    LastFailure: str
    LastSuccessfulExecutionDate: datetime
    ResourceArn: str
    ResourceId: str
    ResourceSnapshotTemplateName: str
    ResourceType: Literal["Opportunity"]
    Status: ResourceSnapshotJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetSellingSystemSettingsResponseTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSellingSystemSettingsResponseTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartEngagementByAcceptingInvitationTaskResponseTypeDef(TypedDict):
    EngagementInvitationId: str
    Message: str
    OpportunityId: str
    ReasonCode: ReasonCodeType
    ResourceSnapshotJobId: str
    StartTime: datetime
    TaskArn: str
    TaskId: str
    TaskStatus: TaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartEngagementFromOpportunityTaskResponseTypeDef(TypedDict):
    EngagementId: str
    EngagementInvitationId: str
    Message: str
    OpportunityId: str
    ReasonCode: ReasonCodeType
    ResourceSnapshotJobId: str
    StartTime: datetime
    TaskArn: str
    TaskId: str
    TaskStatus: TaskStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOpportunityResponseTypeDef(TypedDict):
    Id: str
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ResourceType: Literal["Opportunity"]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartEngagementByAcceptingInvitationTaskRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    Identifier: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartEngagementFromOpportunityTaskRequestTypeDef(TypedDict):
    AwsSubmission: AwsSubmissionTypeDef
    Catalog: str
    ClientToken: str
    Identifier: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CustomerProjectsContextTypeDef(TypedDict):
    Customer: NotRequired[EngagementCustomerTypeDef]
    Project: NotRequired[EngagementCustomerProjectDetailsTypeDef]

class ListEngagementMembersResponseTypeDef(TypedDict):
    EngagementMemberList: List[EngagementMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEngagementResourceAssociationsResponseTypeDef(TypedDict):
    EngagementResourceAssociationSummaries: List[EngagementResourceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEngagementsRequestTypeDef(TypedDict):
    Catalog: str
    CreatedBy: NotRequired[Sequence[str]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    ExcludeCreatedBy: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[EngagementSortTypeDef]

class ListEngagementsResponseTypeDef(TypedDict):
    EngagementSummaryList: List[EngagementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LastModifiedDateTypeDef(TypedDict):
    AfterLastModifiedDate: NotRequired[TimestampTypeDef]
    BeforeLastModifiedDate: NotRequired[TimestampTypeDef]

class NextStepsHistoryTypeDef(TypedDict):
    Time: TimestampTypeDef
    Value: str

class LifeCycleOutputTypeDef(TypedDict):
    ClosedLostReason: NotRequired[ClosedLostReasonType]
    NextSteps: NotRequired[str]
    NextStepsHistory: NotRequired[List[NextStepsHistoryOutputTypeDef]]
    ReviewComments: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    ReviewStatusReason: NotRequired[str]
    Stage: NotRequired[StageType]
    TargetCloseDate: NotRequired[str]

class ListEngagementByAcceptingInvitationTasksResponseTypeDef(TypedDict):
    TaskSummaries: List[ListEngagementByAcceptingInvitationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEngagementByAcceptingInvitationTasksRequestTypeDef(TypedDict):
    Catalog: str
    EngagementInvitationIdentifier: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskIdentifier: NotRequired[Sequence[str]]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]

class ListEngagementFromOpportunityTasksRequestTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskIdentifier: NotRequired[Sequence[str]]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]

class ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementInvitationIdentifier: NotRequired[Sequence[str]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskIdentifier: NotRequired[Sequence[str]]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementFromOpportunityTasksRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: NotRequired[Sequence[str]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskIdentifier: NotRequired[Sequence[str]]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementMembersRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementResourceAssociationsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    CreatedBy: NotRequired[str]
    EngagementIdentifier: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    CreatedBy: NotRequired[Sequence[str]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    ExcludeCreatedBy: NotRequired[Sequence[str]]
    Sort: NotRequired[EngagementSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceSnapshotsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: str
    CreatedBy: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    ResourceSnapshotTemplateIdentifier: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementFromOpportunityTasksResponseTypeDef(TypedDict):
    TaskSummaries: List[ListEngagementFromOpportunityTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEngagementInvitationsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    ParticipantType: ParticipantTypeType
    EngagementIdentifier: NotRequired[Sequence[str]]
    PayloadType: NotRequired[Sequence[Literal["OpportunityInvitation"]]]
    SenderAwsAccountId: NotRequired[Sequence[str]]
    Sort: NotRequired[OpportunityEngagementInvitationSortTypeDef]
    Status: NotRequired[Sequence[InvitationStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementInvitationsRequestTypeDef(TypedDict):
    Catalog: str
    ParticipantType: ParticipantTypeType
    EngagementIdentifier: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    PayloadType: NotRequired[Sequence[Literal["OpportunityInvitation"]]]
    SenderAwsAccountId: NotRequired[Sequence[str]]
    Sort: NotRequired[OpportunityEngagementInvitationSortTypeDef]
    Status: NotRequired[Sequence[InvitationStatusType]]

class ListResourceSnapshotJobsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: NotRequired[str]
    Sort: NotRequired[SortObjectTypeDef]
    Status: NotRequired[ResourceSnapshotJobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceSnapshotJobsRequestTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[SortObjectTypeDef]
    Status: NotRequired[ResourceSnapshotJobStatusType]

class ListResourceSnapshotJobsResponseTypeDef(TypedDict):
    ResourceSnapshotJobSummaries: List[ResourceSnapshotJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceSnapshotsResponseTypeDef(TypedDict):
    ResourceSnapshotSummaries: List[ResourceSnapshotSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSolutionsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Category: NotRequired[Sequence[str]]
    Identifier: NotRequired[Sequence[str]]
    Sort: NotRequired[SolutionSortTypeDef]
    Status: NotRequired[Sequence[SolutionStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSolutionsRequestTypeDef(TypedDict):
    Catalog: str
    Category: NotRequired[Sequence[str]]
    Identifier: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[SolutionSortTypeDef]
    Status: NotRequired[Sequence[SolutionStatusType]]

class ListSolutionsResponseTypeDef(TypedDict):
    SolutionSummaries: List[SolutionBaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MarketingUnionTypeDef = Union[MarketingTypeDef, MarketingOutputTypeDef]

class SoftwareRevenueTypeDef(TypedDict):
    DeliveryModel: NotRequired[RevenueModelType]
    EffectiveDate: NotRequired[str]
    ExpirationDate: NotRequired[str]
    Value: NotRequired[MonetaryValueTypeDef]

class EngagementInvitationSummaryTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: NotRequired[str]
    EngagementId: NotRequired[str]
    EngagementTitle: NotRequired[str]
    ExpirationDate: NotRequired[datetime]
    InvitationDate: NotRequired[datetime]
    ParticipantType: NotRequired[ParticipantTypeType]
    PayloadType: NotRequired[Literal["OpportunityInvitation"]]
    Receiver: NotRequired[ReceiverTypeDef]
    SenderAwsAccountId: NotRequired[str]
    SenderCompanyName: NotRequired[str]
    Status: NotRequired[InvitationStatusType]

class CustomerSummaryTypeDef(TypedDict):
    Account: NotRequired[AccountSummaryTypeDef]

class CustomerOutputTypeDef(TypedDict):
    Account: NotRequired[AccountTypeDef]
    Contacts: NotRequired[List[ContactTypeDef]]

class CustomerTypeDef(TypedDict):
    Account: NotRequired[AccountTypeDef]
    Contacts: NotRequired[Sequence[ContactTypeDef]]

class GetAwsOpportunitySummaryResponseTypeDef(TypedDict):
    Catalog: str
    Customer: AwsOpportunityCustomerTypeDef
    Insights: AwsOpportunityInsightsTypeDef
    InvolvementType: SalesInvolvementTypeType
    InvolvementTypeChangeReason: InvolvementTypeChangeReasonType
    LifeCycle: AwsOpportunityLifeCycleTypeDef
    OpportunityTeam: List[AwsTeamMemberTypeDef]
    Origin: OpportunityOriginType
    Project: AwsOpportunityProjectTypeDef
    RelatedEntityIds: AwsOpportunityRelatedEntitiesTypeDef
    RelatedOpportunityId: str
    Visibility: VisibilityType
    ResponseMetadata: ResponseMetadataTypeDef

class OpportunityInvitationPayloadOutputTypeDef(TypedDict):
    Customer: EngagementCustomerTypeDef
    Project: ProjectDetailsOutputTypeDef
    ReceiverResponsibilities: List[ReceiverResponsibilityType]
    SenderContacts: NotRequired[List[SenderContactTypeDef]]

ProjectDetailsUnionTypeDef = Union[ProjectDetailsTypeDef, ProjectDetailsOutputTypeDef]
ProjectUnionTypeDef = Union[ProjectTypeDef, ProjectOutputTypeDef]

class EngagementContextPayloadTypeDef(TypedDict):
    CustomerProject: NotRequired[CustomerProjectsContextTypeDef]

class ListOpportunitiesRequestPaginateTypeDef(TypedDict):
    Catalog: str
    CustomerCompanyName: NotRequired[Sequence[str]]
    Identifier: NotRequired[Sequence[str]]
    LastModifiedDate: NotRequired[LastModifiedDateTypeDef]
    LifeCycleReviewStatus: NotRequired[Sequence[ReviewStatusType]]
    LifeCycleStage: NotRequired[Sequence[StageType]]
    Sort: NotRequired[OpportunitySortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOpportunitiesRequestTypeDef(TypedDict):
    Catalog: str
    CustomerCompanyName: NotRequired[Sequence[str]]
    Identifier: NotRequired[Sequence[str]]
    LastModifiedDate: NotRequired[LastModifiedDateTypeDef]
    LifeCycleReviewStatus: NotRequired[Sequence[ReviewStatusType]]
    LifeCycleStage: NotRequired[Sequence[StageType]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[OpportunitySortTypeDef]

class LifeCycleTypeDef(TypedDict):
    ClosedLostReason: NotRequired[ClosedLostReasonType]
    NextSteps: NotRequired[str]
    NextStepsHistory: NotRequired[Sequence[NextStepsHistoryTypeDef]]
    ReviewComments: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    ReviewStatusReason: NotRequired[str]
    Stage: NotRequired[StageType]
    TargetCloseDate: NotRequired[str]

class ListEngagementInvitationsResponseTypeDef(TypedDict):
    EngagementInvitationSummaries: List[EngagementInvitationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OpportunitySummaryTypeDef(TypedDict):
    Catalog: str
    Arn: NotRequired[str]
    CreatedDate: NotRequired[datetime]
    Customer: NotRequired[CustomerSummaryTypeDef]
    Id: NotRequired[str]
    LastModifiedDate: NotRequired[datetime]
    LifeCycle: NotRequired[LifeCycleSummaryTypeDef]
    OpportunityType: NotRequired[OpportunityTypeType]
    PartnerOpportunityIdentifier: NotRequired[str]
    Project: NotRequired[ProjectSummaryTypeDef]

class GetOpportunityResponseTypeDef(TypedDict):
    Arn: str
    Catalog: str
    CreatedDate: datetime
    Customer: CustomerOutputTypeDef
    Id: str
    LastModifiedDate: datetime
    LifeCycle: LifeCycleOutputTypeDef
    Marketing: MarketingOutputTypeDef
    NationalSecurity: NationalSecurityType
    OpportunityTeam: List[ContactTypeDef]
    OpportunityType: OpportunityTypeType
    PartnerOpportunityIdentifier: str
    PrimaryNeedsFromAws: List[PrimaryNeedFromAwsType]
    Project: ProjectOutputTypeDef
    RelatedEntityIdentifiers: RelatedEntityIdentifiersTypeDef
    SoftwareRevenue: SoftwareRevenueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OpportunitySummaryViewTypeDef(TypedDict):
    Customer: NotRequired[CustomerOutputTypeDef]
    Lifecycle: NotRequired[LifeCycleForViewTypeDef]
    OpportunityTeam: NotRequired[List[ContactTypeDef]]
    OpportunityType: NotRequired[OpportunityTypeType]
    PrimaryNeedsFromAws: NotRequired[List[PrimaryNeedFromAwsType]]
    Project: NotRequired[ProjectViewTypeDef]
    RelatedEntityIdentifiers: NotRequired[RelatedEntityIdentifiersTypeDef]

CustomerUnionTypeDef = Union[CustomerTypeDef, CustomerOutputTypeDef]

class PayloadOutputTypeDef(TypedDict):
    OpportunityInvitation: NotRequired[OpportunityInvitationPayloadOutputTypeDef]

class OpportunityInvitationPayloadTypeDef(TypedDict):
    Customer: EngagementCustomerTypeDef
    Project: ProjectDetailsUnionTypeDef
    ReceiverResponsibilities: Sequence[ReceiverResponsibilityType]
    SenderContacts: NotRequired[Sequence[SenderContactTypeDef]]

EngagementContextDetailsTypeDef = TypedDict(
    "EngagementContextDetailsTypeDef",
    {
        "Type": Literal["CustomerProject"],
        "Payload": NotRequired[EngagementContextPayloadTypeDef],
    },
)
LifeCycleUnionTypeDef = Union[LifeCycleTypeDef, LifeCycleOutputTypeDef]

class ListOpportunitiesResponseTypeDef(TypedDict):
    OpportunitySummaries: List[OpportunitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResourceSnapshotPayloadTypeDef(TypedDict):
    OpportunitySummary: NotRequired[OpportunitySummaryViewTypeDef]

class GetEngagementInvitationResponseTypeDef(TypedDict):
    Arn: str
    Catalog: str
    EngagementDescription: str
    EngagementId: str
    EngagementTitle: str
    ExistingMembers: List[EngagementMemberSummaryTypeDef]
    ExpirationDate: datetime
    Id: str
    InvitationDate: datetime
    InvitationMessage: str
    Payload: PayloadOutputTypeDef
    PayloadType: Literal["OpportunityInvitation"]
    Receiver: ReceiverTypeDef
    RejectionReason: str
    SenderAwsAccountId: str
    SenderCompanyName: str
    Status: InvitationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

OpportunityInvitationPayloadUnionTypeDef = Union[
    OpportunityInvitationPayloadTypeDef, OpportunityInvitationPayloadOutputTypeDef
]

class CreateEngagementRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    Description: str
    Title: str
    Contexts: NotRequired[Sequence[EngagementContextDetailsTypeDef]]

class GetEngagementResponseTypeDef(TypedDict):
    Arn: str
    Contexts: List[EngagementContextDetailsTypeDef]
    CreatedAt: datetime
    CreatedBy: str
    Description: str
    Id: str
    MemberCount: int
    Title: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    Customer: NotRequired[CustomerUnionTypeDef]
    LifeCycle: NotRequired[LifeCycleUnionTypeDef]
    Marketing: NotRequired[MarketingUnionTypeDef]
    NationalSecurity: NotRequired[NationalSecurityType]
    OpportunityTeam: NotRequired[Sequence[ContactTypeDef]]
    OpportunityType: NotRequired[OpportunityTypeType]
    Origin: NotRequired[OpportunityOriginType]
    PartnerOpportunityIdentifier: NotRequired[str]
    PrimaryNeedsFromAws: NotRequired[Sequence[PrimaryNeedFromAwsType]]
    Project: NotRequired[ProjectUnionTypeDef]
    SoftwareRevenue: NotRequired[SoftwareRevenueTypeDef]

class UpdateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    LastModifiedDate: TimestampTypeDef
    Customer: NotRequired[CustomerUnionTypeDef]
    LifeCycle: NotRequired[LifeCycleUnionTypeDef]
    Marketing: NotRequired[MarketingUnionTypeDef]
    NationalSecurity: NotRequired[NationalSecurityType]
    OpportunityType: NotRequired[OpportunityTypeType]
    PartnerOpportunityIdentifier: NotRequired[str]
    PrimaryNeedsFromAws: NotRequired[Sequence[PrimaryNeedFromAwsType]]
    Project: NotRequired[ProjectUnionTypeDef]
    SoftwareRevenue: NotRequired[SoftwareRevenueTypeDef]

class GetResourceSnapshotResponseTypeDef(TypedDict):
    Arn: str
    Catalog: str
    CreatedAt: datetime
    CreatedBy: str
    EngagementId: str
    Payload: ResourceSnapshotPayloadTypeDef
    ResourceId: str
    ResourceSnapshotTemplateName: str
    ResourceType: Literal["Opportunity"]
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class PayloadTypeDef(TypedDict):
    OpportunityInvitation: NotRequired[OpportunityInvitationPayloadUnionTypeDef]

PayloadUnionTypeDef = Union[PayloadTypeDef, PayloadOutputTypeDef]

class InvitationTypeDef(TypedDict):
    Message: str
    Payload: PayloadUnionTypeDef
    Receiver: ReceiverTypeDef

class CreateEngagementInvitationRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    Invitation: InvitationTypeDef
