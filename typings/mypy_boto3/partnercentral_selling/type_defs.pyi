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
    AwsProductInsightsCurrencyCodeEnumType,
    ChannelType,
    ClosedLostReasonType,
    CompetitorNameType,
    CountryCodeType,
    CurrencyCodeType,
    DeliveryModelType,
    EngagementContextTypeType,
    EngagementInvitationPayloadTypeType,
    EngagementScoreType,
    ExpectedCustomerSpendCurrencyCodeEnumType,
    IndustryType,
    InvitationStatusType,
    InvolvementTypeChangeReasonType,
    MarketingSourceType,
    MarketSegmentType,
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
    "AwsProductDetailsTypeDef",
    "AwsProductInsightsTypeDef",
    "AwsProductOptimizationTypeDef",
    "AwsProductsSpendInsightsBySourceTypeDef",
    "AwsSubmissionTypeDef",
    "AwsTeamMemberTypeDef",
    "ContactTypeDef",
    "CreateEngagementContextRequestTypeDef",
    "CreateEngagementContextResponseTypeDef",
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
    "EngagementContextDetailsOutputTypeDef",
    "EngagementContextDetailsTypeDef",
    "EngagementContextDetailsUnionTypeDef",
    "EngagementContextPayloadOutputTypeDef",
    "EngagementContextPayloadTypeDef",
    "EngagementContextPayloadUnionTypeDef",
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
    "LeadContactTypeDef",
    "LeadContextOutputTypeDef",
    "LeadContextTypeDef",
    "LeadContextUnionTypeDef",
    "LeadCustomerTypeDef",
    "LeadInteractionOutputTypeDef",
    "LeadInteractionTypeDef",
    "LeadInteractionUnionTypeDef",
    "LeadInvitationCustomerTypeDef",
    "LeadInvitationInteractionTypeDef",
    "LeadInvitationPayloadTypeDef",
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
    "ListOpportunityFromEngagementTaskSummaryTypeDef",
    "ListOpportunityFromEngagementTasksRequestPaginateTypeDef",
    "ListOpportunityFromEngagementTasksRequestTypeDef",
    "ListOpportunityFromEngagementTasksResponseTypeDef",
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
    "StartOpportunityFromEngagementTaskRequestTypeDef",
    "StartOpportunityFromEngagementTaskResponseTypeDef",
    "StartResourceSnapshotJobRequestTypeDef",
    "StopResourceSnapshotJobRequestTypeDef",
    "SubmitOpportunityRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEngagementContextPayloadTypeDef",
    "UpdateEngagementContextRequestTypeDef",
    "UpdateEngagementContextResponseTypeDef",
    "UpdateLeadContextTypeDef",
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
    PostalCode: NotRequired[str]
    StateOrRegion: NotRequired[str]
    CountryCode: NotRequired[CountryCodeType]

class AddressTypeDef(TypedDict):
    City: NotRequired[str]
    PostalCode: NotRequired[str]
    StateOrRegion: NotRequired[str]
    CountryCode: NotRequired[CountryCodeType]
    StreetAddress: NotRequired[str]

class AssigneeContactTypeDef(TypedDict):
    Email: str
    FirstName: str
    LastName: str
    BusinessTitle: str
    Phone: NotRequired[str]

class AssociateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType
    RelatedEntityIdentifier: str

class ContactTypeDef(TypedDict):
    Email: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    BusinessTitle: NotRequired[str]
    Phone: NotRequired[str]

class ProfileNextStepsHistoryTypeDef(TypedDict):
    Value: str
    Time: datetime

class ExpectedCustomerSpendTypeDef(TypedDict):
    CurrencyCode: ExpectedCustomerSpendCurrencyCodeEnumType
    Frequency: Literal["Monthly"]
    TargetCompany: str
    Amount: NotRequired[str]
    EstimationUrl: NotRequired[str]

class AwsOpportunityRelatedEntitiesTypeDef(TypedDict):
    AwsProducts: NotRequired[List[str]]
    Solutions: NotRequired[List[str]]

class AwsProductOptimizationTypeDef(TypedDict):
    Description: str
    SavingsAmount: str

class AwsSubmissionTypeDef(TypedDict):
    InvolvementType: SalesInvolvementTypeType
    Visibility: NotRequired[VisibilityType]

class AwsTeamMemberTypeDef(TypedDict):
    Email: NotRequired[str]
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    BusinessTitle: NotRequired[AwsMemberBusinessTitleType]

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
    EngagementIdentifier: str
    ResourceType: Literal["Opportunity"]
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    ClientToken: str

class EngagementCustomerProjectDetailsTypeDef(TypedDict):
    Title: str
    BusinessProblem: str
    TargetCompletionDate: str

class EngagementCustomerTypeDef(TypedDict):
    Industry: IndustryType
    CompanyName: str
    WebsiteUrl: str
    CountryCode: CountryCodeType

class DeleteResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobIdentifier: str

class DisassociateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    OpportunityIdentifier: str
    RelatedEntityType: RelatedEntityTypeType
    RelatedEntityIdentifier: str

class EngagementMemberSummaryTypeDef(TypedDict):
    CompanyName: NotRequired[str]
    WebsiteUrl: NotRequired[str]

class EngagementMemberTypeDef(TypedDict):
    CompanyName: NotRequired[str]
    WebsiteUrl: NotRequired[str]
    AccountId: NotRequired[str]

class EngagementResourceAssociationSummaryTypeDef(TypedDict):
    Catalog: str
    EngagementId: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    ResourceId: NotRequired[str]
    CreatedBy: NotRequired[str]

class EngagementSortTypeDef(TypedDict):
    SortOrder: SortOrderType
    SortBy: Literal["CreatedDate"]

class EngagementSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Title: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    CreatedBy: NotRequired[str]
    MemberCount: NotRequired[int]
    ModifiedAt: NotRequired[datetime]
    ModifiedBy: NotRequired[str]
    ContextTypes: NotRequired[List[EngagementContextTypeType]]

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
    CampaignName: NotRequired[str]
    Source: NotRequired[MarketingSourceType]
    UseCases: NotRequired[List[str]]
    Channels: NotRequired[List[ChannelType]]
    AwsFundingUsed: NotRequired[AwsFundingUsedType]

class RelatedEntityIdentifiersTypeDef(TypedDict):
    AwsMarketplaceOffers: NotRequired[List[str]]
    AwsMarketplaceOfferSets: NotRequired[List[str]]
    Solutions: NotRequired[List[str]]
    AwsProducts: NotRequired[List[str]]

class GetResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ResourceSnapshotJobIdentifier: str

class GetResourceSnapshotRequestTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: str
    ResourceType: Literal["Opportunity"]
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
    Revision: NotRequired[int]

class GetSellingSystemSettingsRequestTypeDef(TypedDict):
    Catalog: str

TimestampTypeDef = Union[datetime, str]

class LeadContactTypeDef(TypedDict):
    BusinessTitle: str
    Email: str
    FirstName: str
    LastName: str
    Phone: NotRequired[str]

class LeadInvitationCustomerTypeDef(TypedDict):
    CompanyName: str
    CountryCode: CountryCodeType
    Industry: NotRequired[IndustryType]
    WebsiteUrl: NotRequired[str]
    AwsMaturity: NotRequired[str]
    MarketSegment: NotRequired[MarketSegmentType]

class LeadInvitationInteractionTypeDef(TypedDict):
    SourceType: str
    SourceId: str
    SourceName: str
    ContactBusinessTitle: str
    Usecase: NotRequired[str]

class LifeCycleForViewTypeDef(TypedDict):
    TargetCloseDate: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    Stage: NotRequired[StageType]
    NextSteps: NotRequired[str]

class NextStepsHistoryOutputTypeDef(TypedDict):
    Value: str
    Time: datetime

class LifeCycleSummaryTypeDef(TypedDict):
    Stage: NotRequired[StageType]
    ClosedLostReason: NotRequired[ClosedLostReasonType]
    NextSteps: NotRequired[str]
    TargetCloseDate: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    ReviewComments: NotRequired[str]
    ReviewStatusReason: NotRequired[str]

class ListEngagementByAcceptingInvitationTaskSummaryTypeDef(TypedDict):
    TaskId: NotRequired[str]
    TaskArn: NotRequired[str]
    StartTime: NotRequired[datetime]
    TaskStatus: NotRequired[TaskStatusType]
    Message: NotRequired[str]
    ReasonCode: NotRequired[ReasonCodeType]
    OpportunityId: NotRequired[str]
    ResourceSnapshotJobId: NotRequired[str]
    EngagementInvitationId: NotRequired[str]

class ListTasksSortBaseTypeDef(TypedDict):
    SortOrder: SortOrderType
    SortBy: Literal["StartTime"]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListEngagementFromOpportunityTaskSummaryTypeDef(TypedDict):
    TaskId: NotRequired[str]
    TaskArn: NotRequired[str]
    StartTime: NotRequired[datetime]
    TaskStatus: NotRequired[TaskStatusType]
    Message: NotRequired[str]
    ReasonCode: NotRequired[ReasonCodeType]
    OpportunityId: NotRequired[str]
    ResourceSnapshotJobId: NotRequired[str]
    EngagementId: NotRequired[str]
    EngagementInvitationId: NotRequired[str]

class OpportunityEngagementInvitationSortTypeDef(TypedDict):
    SortOrder: SortOrderType
    SortBy: Literal["InvitationDate"]

class ListEngagementMembersRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListEngagementResourceAssociationsRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    EngagementIdentifier: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    ResourceIdentifier: NotRequired[str]
    CreatedBy: NotRequired[str]

class OpportunitySortTypeDef(TypedDict):
    SortOrder: SortOrderType
    SortBy: OpportunitySortNameType

class ListOpportunityFromEngagementTaskSummaryTypeDef(TypedDict):
    TaskId: NotRequired[str]
    TaskArn: NotRequired[str]
    StartTime: NotRequired[datetime]
    TaskStatus: NotRequired[TaskStatusType]
    Message: NotRequired[str]
    ReasonCode: NotRequired[ReasonCodeType]
    OpportunityId: NotRequired[str]
    ResourceSnapshotJobId: NotRequired[str]
    EngagementId: NotRequired[str]
    ContextId: NotRequired[str]

class SortObjectTypeDef(TypedDict):
    SortBy: NotRequired[Literal["CreatedDate"]]
    SortOrder: NotRequired[SortOrderType]

class ResourceSnapshotJobSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    EngagementId: NotRequired[str]
    Status: NotRequired[ResourceSnapshotJobStatusType]

class ListResourceSnapshotsRequestTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    ResourceIdentifier: NotRequired[str]
    ResourceSnapshotTemplateIdentifier: NotRequired[str]
    CreatedBy: NotRequired[str]

class ResourceSnapshotSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Revision: NotRequired[int]
    ResourceType: NotRequired[Literal["Opportunity"]]
    ResourceId: NotRequired[str]
    ResourceSnapshotTemplateName: NotRequired[str]
    CreatedBy: NotRequired[str]

class SolutionSortTypeDef(TypedDict):
    SortOrder: SortOrderType
    SortBy: SolutionSortNameType

class SolutionBaseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Name: str
    Status: SolutionStatusType
    Category: str
    CreatedDate: datetime
    Arn: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class MarketingTypeDef(TypedDict):
    CampaignName: NotRequired[str]
    Source: NotRequired[MarketingSourceType]
    UseCases: NotRequired[Sequence[str]]
    Channels: NotRequired[Sequence[ChannelType]]
    AwsFundingUsed: NotRequired[AwsFundingUsedType]

class MonetaryValueTypeDef(TypedDict):
    Amount: str
    CurrencyCode: CurrencyCodeType

class SenderContactTypeDef(TypedDict):
    Email: str
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    BusinessTitle: NotRequired[str]
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
    Industry: NotRequired[IndustryType]
    OtherIndustry: NotRequired[str]
    WebsiteUrl: NotRequired[str]
    Address: NotRequired[AddressSummaryTypeDef]

class LeadCustomerTypeDef(TypedDict):
    CompanyName: str
    Address: AddressSummaryTypeDef
    Industry: NotRequired[IndustryType]
    WebsiteUrl: NotRequired[str]
    AwsMaturity: NotRequired[str]
    MarketSegment: NotRequired[MarketSegmentType]

class AccountTypeDef(TypedDict):
    CompanyName: str
    Industry: NotRequired[IndustryType]
    OtherIndustry: NotRequired[str]
    WebsiteUrl: NotRequired[str]
    AwsAccountId: NotRequired[str]
    Address: NotRequired[AddressTypeDef]
    Duns: NotRequired[str]

class AssignOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    Assignee: AssigneeContactTypeDef

class AwsOpportunityCustomerTypeDef(TypedDict):
    Contacts: NotRequired[List[ContactTypeDef]]

class AwsOpportunityLifeCycleTypeDef(TypedDict):
    TargetCloseDate: NotRequired[str]
    ClosedLostReason: NotRequired[AwsClosedLostReasonType]
    Stage: NotRequired[AwsOpportunityStageType]
    NextSteps: NotRequired[str]
    NextStepsHistory: NotRequired[List[ProfileNextStepsHistoryTypeDef]]

class AwsOpportunityProjectTypeDef(TypedDict):
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]
    AwsPartition: NotRequired[Literal["aws-eusc"]]

class ProjectDetailsOutputTypeDef(TypedDict):
    BusinessProblem: str
    Title: str
    TargetCompletionDate: str
    ExpectedCustomerSpend: List[ExpectedCustomerSpendTypeDef]

class ProjectDetailsTypeDef(TypedDict):
    BusinessProblem: str
    Title: str
    TargetCompletionDate: str
    ExpectedCustomerSpend: Sequence[ExpectedCustomerSpendTypeDef]

class ProjectOutputTypeDef(TypedDict):
    DeliveryModels: NotRequired[List[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]
    Title: NotRequired[str]
    ApnPrograms: NotRequired[List[str]]
    CustomerBusinessProblem: NotRequired[str]
    CustomerUseCase: NotRequired[str]
    RelatedOpportunityIdentifier: NotRequired[str]
    SalesActivities: NotRequired[List[SalesActivityType]]
    CompetitorName: NotRequired[CompetitorNameType]
    OtherCompetitorNames: NotRequired[str]
    OtherSolutionDescription: NotRequired[str]
    AdditionalComments: NotRequired[str]
    AwsPartition: NotRequired[Literal["aws-eusc"]]

class ProjectSummaryTypeDef(TypedDict):
    DeliveryModels: NotRequired[List[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]

class ProjectTypeDef(TypedDict):
    DeliveryModels: NotRequired[Sequence[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[Sequence[ExpectedCustomerSpendTypeDef]]
    Title: NotRequired[str]
    ApnPrograms: NotRequired[Sequence[str]]
    CustomerBusinessProblem: NotRequired[str]
    CustomerUseCase: NotRequired[str]
    RelatedOpportunityIdentifier: NotRequired[str]
    SalesActivities: NotRequired[Sequence[SalesActivityType]]
    CompetitorName: NotRequired[CompetitorNameType]
    OtherCompetitorNames: NotRequired[str]
    OtherSolutionDescription: NotRequired[str]
    AdditionalComments: NotRequired[str]
    AwsPartition: NotRequired[Literal["aws-eusc"]]

class ProjectViewTypeDef(TypedDict):
    DeliveryModels: NotRequired[List[DeliveryModelType]]
    ExpectedCustomerSpend: NotRequired[List[ExpectedCustomerSpendTypeDef]]
    CustomerUseCase: NotRequired[str]
    SalesActivities: NotRequired[List[SalesActivityType]]
    OtherSolutionDescription: NotRequired[str]

class AwsProductDetailsTypeDef(TypedDict):
    ProductCode: str
    Categories: List[str]
    Optimizations: List[AwsProductOptimizationTypeDef]
    ServiceCode: NotRequired[str]
    Amount: NotRequired[str]
    OptimizedAmount: NotRequired[str]
    PotentialSavingsAmount: NotRequired[str]

class CreateEngagementContextResponseTypeDef(TypedDict):
    EngagementId: str
    EngagementArn: str
    EngagementLastModifiedAt: datetime
    ContextId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEngagementInvitationResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEngagementResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ModifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOpportunityResponseTypeDef(TypedDict):
    Id: str
    PartnerOpportunityIdentifier: str
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceSnapshotJobResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceSnapshotResponseTypeDef(TypedDict):
    Arn: str
    Revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSnapshotJobResponseTypeDef(TypedDict):
    Catalog: str
    Id: str
    Arn: str
    EngagementId: str
    ResourceType: Literal["Opportunity"]
    ResourceId: str
    ResourceArn: str
    ResourceSnapshotTemplateName: str
    CreatedAt: datetime
    Status: ResourceSnapshotJobStatusType
    LastSuccessfulExecutionDate: datetime
    LastFailure: str
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
    TaskId: str
    TaskArn: str
    StartTime: datetime
    TaskStatus: TaskStatusType
    Message: str
    ReasonCode: ReasonCodeType
    OpportunityId: str
    ResourceSnapshotJobId: str
    EngagementInvitationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartEngagementFromOpportunityTaskResponseTypeDef(TypedDict):
    TaskId: str
    TaskArn: str
    StartTime: datetime
    TaskStatus: TaskStatusType
    Message: str
    ReasonCode: ReasonCodeType
    OpportunityId: str
    ResourceSnapshotJobId: str
    EngagementId: str
    EngagementInvitationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOpportunityFromEngagementTaskResponseTypeDef(TypedDict):
    TaskId: str
    TaskArn: str
    StartTime: datetime
    TaskStatus: TaskStatusType
    Message: str
    ReasonCode: ReasonCodeType
    OpportunityId: str
    ResourceSnapshotJobId: str
    EngagementId: str
    ContextId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEngagementContextResponseTypeDef(TypedDict):
    EngagementId: str
    EngagementArn: str
    EngagementLastModifiedAt: datetime
    ContextId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOpportunityResponseTypeDef(TypedDict):
    Id: str
    LastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceSnapshotJobRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    ResourceType: Literal["Opportunity"]
    ResourceIdentifier: str
    ResourceSnapshotTemplateIdentifier: str
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
    Catalog: str
    ClientToken: str
    Identifier: str
    AwsSubmission: AwsSubmissionTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartOpportunityFromEngagementTaskRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    Identifier: str
    ContextIdentifier: str
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
    ExcludeCreatedBy: NotRequired[Sequence[str]]
    ContextTypes: NotRequired[Sequence[EngagementContextTypeType]]
    ExcludeContextTypes: NotRequired[Sequence[EngagementContextTypeType]]
    Sort: NotRequired[EngagementSortTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    EngagementIdentifier: NotRequired[Sequence[str]]

class ListEngagementsResponseTypeDef(TypedDict):
    EngagementSummaryList: List[EngagementSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class LastModifiedDateTypeDef(TypedDict):
    AfterLastModifiedDate: NotRequired[TimestampTypeDef]
    BeforeLastModifiedDate: NotRequired[TimestampTypeDef]

class NextStepsHistoryTypeDef(TypedDict):
    Value: str
    Time: TimestampTypeDef

class LeadInteractionOutputTypeDef(TypedDict):
    SourceType: str
    SourceId: str
    SourceName: str
    CustomerAction: str
    Contact: LeadContactTypeDef
    Usecase: NotRequired[str]
    InteractionDate: NotRequired[datetime]
    BusinessProblem: NotRequired[str]

class LeadInteractionTypeDef(TypedDict):
    SourceType: str
    SourceId: str
    SourceName: str
    CustomerAction: str
    Contact: LeadContactTypeDef
    Usecase: NotRequired[str]
    InteractionDate: NotRequired[TimestampTypeDef]
    BusinessProblem: NotRequired[str]

class LeadInvitationPayloadTypeDef(TypedDict):
    Customer: LeadInvitationCustomerTypeDef
    Interaction: LeadInvitationInteractionTypeDef

class LifeCycleOutputTypeDef(TypedDict):
    Stage: NotRequired[StageType]
    ClosedLostReason: NotRequired[ClosedLostReasonType]
    NextSteps: NotRequired[str]
    TargetCloseDate: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    ReviewComments: NotRequired[str]
    ReviewStatusReason: NotRequired[str]
    NextStepsHistory: NotRequired[List[NextStepsHistoryOutputTypeDef]]

class ListEngagementByAcceptingInvitationTasksResponseTypeDef(TypedDict):
    TaskSummaries: List[ListEngagementByAcceptingInvitationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEngagementByAcceptingInvitationTasksRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    EngagementInvitationIdentifier: NotRequired[Sequence[str]]
    TaskIdentifier: NotRequired[Sequence[str]]

class ListEngagementFromOpportunityTasksRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    TaskIdentifier: NotRequired[Sequence[str]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    EngagementIdentifier: NotRequired[Sequence[str]]

class ListOpportunityFromEngagementTasksRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    TaskIdentifier: NotRequired[Sequence[str]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    ContextIdentifier: NotRequired[Sequence[str]]

class ListEngagementByAcceptingInvitationTasksRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    EngagementInvitationIdentifier: NotRequired[Sequence[str]]
    TaskIdentifier: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementFromOpportunityTasksRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    TaskIdentifier: NotRequired[Sequence[str]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementMembersRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Identifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementResourceAssociationsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: NotRequired[str]
    ResourceType: NotRequired[Literal["Opportunity"]]
    ResourceIdentifier: NotRequired[str]
    CreatedBy: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    CreatedBy: NotRequired[Sequence[str]]
    ExcludeCreatedBy: NotRequired[Sequence[str]]
    ContextTypes: NotRequired[Sequence[EngagementContextTypeType]]
    ExcludeContextTypes: NotRequired[Sequence[EngagementContextTypeType]]
    Sort: NotRequired[EngagementSortTypeDef]
    EngagementIdentifier: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOpportunityFromEngagementTasksRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Sort: NotRequired[ListTasksSortBaseTypeDef]
    TaskStatus: NotRequired[Sequence[TaskStatusType]]
    TaskIdentifier: NotRequired[Sequence[str]]
    OpportunityIdentifier: NotRequired[Sequence[str]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    ContextIdentifier: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceSnapshotsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: str
    ResourceType: NotRequired[Literal["Opportunity"]]
    ResourceIdentifier: NotRequired[str]
    ResourceSnapshotTemplateIdentifier: NotRequired[str]
    CreatedBy: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementFromOpportunityTasksResponseTypeDef(TypedDict):
    TaskSummaries: List[ListEngagementFromOpportunityTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEngagementInvitationsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    ParticipantType: ParticipantTypeType
    Sort: NotRequired[OpportunityEngagementInvitationSortTypeDef]
    PayloadType: NotRequired[Sequence[EngagementInvitationPayloadTypeType]]
    Status: NotRequired[Sequence[InvitationStatusType]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    SenderAwsAccountId: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementInvitationsRequestTypeDef(TypedDict):
    Catalog: str
    ParticipantType: ParticipantTypeType
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[OpportunityEngagementInvitationSortTypeDef]
    PayloadType: NotRequired[Sequence[EngagementInvitationPayloadTypeType]]
    Status: NotRequired[Sequence[InvitationStatusType]]
    EngagementIdentifier: NotRequired[Sequence[str]]
    SenderAwsAccountId: NotRequired[Sequence[str]]

class ListOpportunityFromEngagementTasksResponseTypeDef(TypedDict):
    TaskSummaries: List[ListOpportunityFromEngagementTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceSnapshotJobsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EngagementIdentifier: NotRequired[str]
    Status: NotRequired[ResourceSnapshotJobStatusType]
    Sort: NotRequired[SortObjectTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceSnapshotJobsRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    EngagementIdentifier: NotRequired[str]
    Status: NotRequired[ResourceSnapshotJobStatusType]
    Sort: NotRequired[SortObjectTypeDef]

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
    Sort: NotRequired[SolutionSortTypeDef]
    Status: NotRequired[Sequence[SolutionStatusType]]
    Identifier: NotRequired[Sequence[str]]
    Category: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSolutionsRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[SolutionSortTypeDef]
    Status: NotRequired[Sequence[SolutionStatusType]]
    Identifier: NotRequired[Sequence[str]]
    Category: NotRequired[Sequence[str]]

class ListSolutionsResponseTypeDef(TypedDict):
    SolutionSummaries: List[SolutionBaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

MarketingUnionTypeDef = Union[MarketingTypeDef, MarketingOutputTypeDef]

class SoftwareRevenueTypeDef(TypedDict):
    DeliveryModel: NotRequired[RevenueModelType]
    Value: NotRequired[MonetaryValueTypeDef]
    EffectiveDate: NotRequired[str]
    ExpirationDate: NotRequired[str]

class EngagementInvitationSummaryTypeDef(TypedDict):
    Id: str
    Catalog: str
    Arn: NotRequired[str]
    PayloadType: NotRequired[EngagementInvitationPayloadTypeType]
    EngagementId: NotRequired[str]
    EngagementTitle: NotRequired[str]
    Status: NotRequired[InvitationStatusType]
    InvitationDate: NotRequired[datetime]
    ExpirationDate: NotRequired[datetime]
    SenderAwsAccountId: NotRequired[str]
    SenderCompanyName: NotRequired[str]
    Receiver: NotRequired[ReceiverTypeDef]
    ParticipantType: NotRequired[ParticipantTypeType]

class CustomerSummaryTypeDef(TypedDict):
    Account: NotRequired[AccountSummaryTypeDef]

class CustomerOutputTypeDef(TypedDict):
    Account: NotRequired[AccountTypeDef]
    Contacts: NotRequired[List[ContactTypeDef]]

class CustomerTypeDef(TypedDict):
    Account: NotRequired[AccountTypeDef]
    Contacts: NotRequired[Sequence[ContactTypeDef]]

class OpportunityInvitationPayloadOutputTypeDef(TypedDict):
    ReceiverResponsibilities: List[ReceiverResponsibilityType]
    Customer: EngagementCustomerTypeDef
    Project: ProjectDetailsOutputTypeDef
    SenderContacts: NotRequired[List[SenderContactTypeDef]]

ProjectDetailsUnionTypeDef = Union[ProjectDetailsTypeDef, ProjectDetailsOutputTypeDef]
ProjectUnionTypeDef = Union[ProjectTypeDef, ProjectOutputTypeDef]

class AwsProductInsightsTypeDef(TypedDict):
    CurrencyCode: AwsProductInsightsCurrencyCodeEnumType
    Frequency: Literal["Monthly"]
    TotalAmountByCategory: Dict[str, str]
    AwsProducts: List[AwsProductDetailsTypeDef]
    TotalAmount: NotRequired[str]
    TotalOptimizedAmount: NotRequired[str]
    TotalPotentialSavingsAmount: NotRequired[str]

class ListOpportunitiesRequestPaginateTypeDef(TypedDict):
    Catalog: str
    Sort: NotRequired[OpportunitySortTypeDef]
    LastModifiedDate: NotRequired[LastModifiedDateTypeDef]
    Identifier: NotRequired[Sequence[str]]
    LifeCycleStage: NotRequired[Sequence[StageType]]
    LifeCycleReviewStatus: NotRequired[Sequence[ReviewStatusType]]
    CustomerCompanyName: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOpportunitiesRequestTypeDef(TypedDict):
    Catalog: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Sort: NotRequired[OpportunitySortTypeDef]
    LastModifiedDate: NotRequired[LastModifiedDateTypeDef]
    Identifier: NotRequired[Sequence[str]]
    LifeCycleStage: NotRequired[Sequence[StageType]]
    LifeCycleReviewStatus: NotRequired[Sequence[ReviewStatusType]]
    CustomerCompanyName: NotRequired[Sequence[str]]

class LifeCycleTypeDef(TypedDict):
    Stage: NotRequired[StageType]
    ClosedLostReason: NotRequired[ClosedLostReasonType]
    NextSteps: NotRequired[str]
    TargetCloseDate: NotRequired[str]
    ReviewStatus: NotRequired[ReviewStatusType]
    ReviewComments: NotRequired[str]
    ReviewStatusReason: NotRequired[str]
    NextStepsHistory: NotRequired[Sequence[NextStepsHistoryTypeDef]]

class LeadContextOutputTypeDef(TypedDict):
    Customer: LeadCustomerTypeDef
    Interactions: List[LeadInteractionOutputTypeDef]
    QualificationStatus: NotRequired[str]

LeadInteractionUnionTypeDef = Union[LeadInteractionTypeDef, LeadInteractionOutputTypeDef]

class ListEngagementInvitationsResponseTypeDef(TypedDict):
    EngagementInvitationSummaries: List[EngagementInvitationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OpportunitySummaryTypeDef(TypedDict):
    Catalog: str
    Id: NotRequired[str]
    Arn: NotRequired[str]
    PartnerOpportunityIdentifier: NotRequired[str]
    OpportunityType: NotRequired[OpportunityTypeType]
    LastModifiedDate: NotRequired[datetime]
    CreatedDate: NotRequired[datetime]
    LifeCycle: NotRequired[LifeCycleSummaryTypeDef]
    Customer: NotRequired[CustomerSummaryTypeDef]
    Project: NotRequired[ProjectSummaryTypeDef]

class GetOpportunityResponseTypeDef(TypedDict):
    Catalog: str
    PrimaryNeedsFromAws: List[PrimaryNeedFromAwsType]
    NationalSecurity: NationalSecurityType
    PartnerOpportunityIdentifier: str
    Customer: CustomerOutputTypeDef
    Project: ProjectOutputTypeDef
    OpportunityType: OpportunityTypeType
    Marketing: MarketingOutputTypeDef
    SoftwareRevenue: SoftwareRevenueTypeDef
    Id: str
    Arn: str
    LastModifiedDate: datetime
    CreatedDate: datetime
    RelatedEntityIdentifiers: RelatedEntityIdentifiersTypeDef
    LifeCycle: LifeCycleOutputTypeDef
    OpportunityTeam: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OpportunitySummaryViewTypeDef(TypedDict):
    OpportunityType: NotRequired[OpportunityTypeType]
    Lifecycle: NotRequired[LifeCycleForViewTypeDef]
    OpportunityTeam: NotRequired[List[ContactTypeDef]]
    PrimaryNeedsFromAws: NotRequired[List[PrimaryNeedFromAwsType]]
    Customer: NotRequired[CustomerOutputTypeDef]
    Project: NotRequired[ProjectViewTypeDef]
    RelatedEntityIdentifiers: NotRequired[RelatedEntityIdentifiersTypeDef]

CustomerUnionTypeDef = Union[CustomerTypeDef, CustomerOutputTypeDef]

class PayloadOutputTypeDef(TypedDict):
    OpportunityInvitation: NotRequired[OpportunityInvitationPayloadOutputTypeDef]
    LeadInvitation: NotRequired[LeadInvitationPayloadTypeDef]

class OpportunityInvitationPayloadTypeDef(TypedDict):
    ReceiverResponsibilities: Sequence[ReceiverResponsibilityType]
    Customer: EngagementCustomerTypeDef
    Project: ProjectDetailsUnionTypeDef
    SenderContacts: NotRequired[Sequence[SenderContactTypeDef]]

class AwsProductsSpendInsightsBySourceTypeDef(TypedDict):
    Partner: NotRequired[AwsProductInsightsTypeDef]
    AWS: NotRequired[AwsProductInsightsTypeDef]

LifeCycleUnionTypeDef = Union[LifeCycleTypeDef, LifeCycleOutputTypeDef]

class EngagementContextPayloadOutputTypeDef(TypedDict):
    CustomerProject: NotRequired[CustomerProjectsContextTypeDef]
    Lead: NotRequired[LeadContextOutputTypeDef]

class LeadContextTypeDef(TypedDict):
    Customer: LeadCustomerTypeDef
    Interactions: Sequence[LeadInteractionUnionTypeDef]
    QualificationStatus: NotRequired[str]

class UpdateLeadContextTypeDef(TypedDict):
    Customer: LeadCustomerTypeDef
    QualificationStatus: NotRequired[str]
    Interaction: NotRequired[LeadInteractionUnionTypeDef]

class ListOpportunitiesResponseTypeDef(TypedDict):
    OpportunitySummaries: List[OpportunitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResourceSnapshotPayloadTypeDef(TypedDict):
    OpportunitySummary: NotRequired[OpportunitySummaryViewTypeDef]

class GetEngagementInvitationResponseTypeDef(TypedDict):
    Arn: str
    PayloadType: EngagementInvitationPayloadTypeType
    Id: str
    EngagementId: str
    EngagementTitle: str
    Status: InvitationStatusType
    InvitationDate: datetime
    ExpirationDate: datetime
    SenderAwsAccountId: str
    SenderCompanyName: str
    Receiver: ReceiverTypeDef
    Catalog: str
    RejectionReason: str
    Payload: PayloadOutputTypeDef
    InvitationMessage: str
    EngagementDescription: str
    ExistingMembers: List[EngagementMemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

OpportunityInvitationPayloadUnionTypeDef = Union[
    OpportunityInvitationPayloadTypeDef, OpportunityInvitationPayloadOutputTypeDef
]

class AwsOpportunityInsightsTypeDef(TypedDict):
    NextBestActions: NotRequired[str]
    EngagementScore: NotRequired[EngagementScoreType]
    AwsProductsSpendInsightsBySource: NotRequired[AwsProductsSpendInsightsBySourceTypeDef]

class CreateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    PrimaryNeedsFromAws: NotRequired[Sequence[PrimaryNeedFromAwsType]]
    NationalSecurity: NotRequired[NationalSecurityType]
    PartnerOpportunityIdentifier: NotRequired[str]
    Customer: NotRequired[CustomerUnionTypeDef]
    Project: NotRequired[ProjectUnionTypeDef]
    OpportunityType: NotRequired[OpportunityTypeType]
    Marketing: NotRequired[MarketingUnionTypeDef]
    SoftwareRevenue: NotRequired[SoftwareRevenueTypeDef]
    LifeCycle: NotRequired[LifeCycleUnionTypeDef]
    Origin: NotRequired[OpportunityOriginType]
    OpportunityTeam: NotRequired[Sequence[ContactTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateOpportunityRequestTypeDef(TypedDict):
    Catalog: str
    LastModifiedDate: TimestampTypeDef
    Identifier: str
    PrimaryNeedsFromAws: NotRequired[Sequence[PrimaryNeedFromAwsType]]
    NationalSecurity: NotRequired[NationalSecurityType]
    PartnerOpportunityIdentifier: NotRequired[str]
    Customer: NotRequired[CustomerUnionTypeDef]
    Project: NotRequired[ProjectUnionTypeDef]
    OpportunityType: NotRequired[OpportunityTypeType]
    Marketing: NotRequired[MarketingUnionTypeDef]
    SoftwareRevenue: NotRequired[SoftwareRevenueTypeDef]
    LifeCycle: NotRequired[LifeCycleUnionTypeDef]

EngagementContextDetailsOutputTypeDef = TypedDict(
    "EngagementContextDetailsOutputTypeDef",
    {
        "Type": EngagementContextTypeType,
        "Id": NotRequired[str],
        "Payload": NotRequired[EngagementContextPayloadOutputTypeDef],
    },
)
LeadContextUnionTypeDef = Union[LeadContextTypeDef, LeadContextOutputTypeDef]

class UpdateEngagementContextPayloadTypeDef(TypedDict):
    Lead: NotRequired[UpdateLeadContextTypeDef]
    CustomerProject: NotRequired[CustomerProjectsContextTypeDef]

class GetResourceSnapshotResponseTypeDef(TypedDict):
    Catalog: str
    Arn: str
    CreatedBy: str
    CreatedAt: datetime
    EngagementId: str
    ResourceType: Literal["Opportunity"]
    ResourceId: str
    ResourceSnapshotTemplateName: str
    Revision: int
    Payload: ResourceSnapshotPayloadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PayloadTypeDef(TypedDict):
    OpportunityInvitation: NotRequired[OpportunityInvitationPayloadUnionTypeDef]
    LeadInvitation: NotRequired[LeadInvitationPayloadTypeDef]

class GetAwsOpportunitySummaryResponseTypeDef(TypedDict):
    RelatedOpportunityId: str
    Origin: OpportunityOriginType
    InvolvementType: SalesInvolvementTypeType
    Visibility: VisibilityType
    LifeCycle: AwsOpportunityLifeCycleTypeDef
    OpportunityTeam: List[AwsTeamMemberTypeDef]
    Insights: AwsOpportunityInsightsTypeDef
    InvolvementTypeChangeReason: InvolvementTypeChangeReasonType
    RelatedEntityIds: AwsOpportunityRelatedEntitiesTypeDef
    Customer: AwsOpportunityCustomerTypeDef
    Project: AwsOpportunityProjectTypeDef
    Catalog: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEngagementResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    Title: str
    Description: str
    CreatedAt: datetime
    CreatedBy: str
    MemberCount: int
    ModifiedAt: datetime
    ModifiedBy: str
    Contexts: List[EngagementContextDetailsOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EngagementContextPayloadTypeDef(TypedDict):
    CustomerProject: NotRequired[CustomerProjectsContextTypeDef]
    Lead: NotRequired[LeadContextUnionTypeDef]

UpdateEngagementContextRequestTypeDef = TypedDict(
    "UpdateEngagementContextRequestTypeDef",
    {
        "Catalog": str,
        "EngagementIdentifier": str,
        "ContextIdentifier": str,
        "EngagementLastModifiedAt": TimestampTypeDef,
        "Type": EngagementContextTypeType,
        "Payload": UpdateEngagementContextPayloadTypeDef,
    },
)
PayloadUnionTypeDef = Union[PayloadTypeDef, PayloadOutputTypeDef]
EngagementContextPayloadUnionTypeDef = Union[
    EngagementContextPayloadTypeDef, EngagementContextPayloadOutputTypeDef
]

class InvitationTypeDef(TypedDict):
    Message: str
    Receiver: ReceiverTypeDef
    Payload: PayloadUnionTypeDef

CreateEngagementContextRequestTypeDef = TypedDict(
    "CreateEngagementContextRequestTypeDef",
    {
        "Catalog": str,
        "EngagementIdentifier": str,
        "ClientToken": str,
        "Type": EngagementContextTypeType,
        "Payload": EngagementContextPayloadUnionTypeDef,
    },
)
EngagementContextDetailsTypeDef = TypedDict(
    "EngagementContextDetailsTypeDef",
    {
        "Type": EngagementContextTypeType,
        "Id": NotRequired[str],
        "Payload": NotRequired[EngagementContextPayloadUnionTypeDef],
    },
)

class CreateEngagementInvitationRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    EngagementIdentifier: str
    Invitation: InvitationTypeDef

EngagementContextDetailsUnionTypeDef = Union[
    EngagementContextDetailsTypeDef, EngagementContextDetailsOutputTypeDef
]

class CreateEngagementRequestTypeDef(TypedDict):
    Catalog: str
    ClientToken: str
    Title: str
    Description: str
    Contexts: NotRequired[Sequence[EngagementContextDetailsUnionTypeDef]]
