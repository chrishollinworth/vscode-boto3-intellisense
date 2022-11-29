"""
Type annotations for macie2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_macie2 import Macie2Client

    client: Macie2Client = boto3.client("macie2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AutomatedDiscoveryStatusType,
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingTypeType,
    GroupByType,
    JobStatusType,
    JobTypeType,
    MacieStatusType,
    ManagedDataIdentifierSelectorType,
    TimeRangeType,
)
from .paginator import (
    DescribeBucketsPaginator,
    GetUsageStatisticsPaginator,
    ListAllowListsPaginator,
    ListClassificationJobsPaginator,
    ListClassificationScopesPaginator,
    ListCustomDataIdentifiersPaginator,
    ListFindingsFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListManagedDataIdentifiersPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListResourceProfileArtifactsPaginator,
    ListResourceProfileDetectionsPaginator,
    ListSensitivityInspectionTemplatesPaginator,
    SearchResourcesPaginator,
)
from .type_defs import (
    AccountDetailTypeDef,
    AllowListCriteriaTypeDef,
    BatchGetCustomDataIdentifiersResponseTypeDef,
    BucketCriteriaAdditionalPropertiesTypeDef,
    BucketSortCriteriaTypeDef,
    ClassificationExportConfigurationTypeDef,
    CreateAllowListResponseTypeDef,
    CreateClassificationJobResponseTypeDef,
    CreateCustomDataIdentifierResponseTypeDef,
    CreateFindingsFilterResponseTypeDef,
    CreateInvitationsResponseTypeDef,
    CreateMemberResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DescribeBucketsResponseTypeDef,
    DescribeClassificationJobResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    FindingCriteriaTypeDef,
    FindingStatisticsSortCriteriaTypeDef,
    GetAdministratorAccountResponseTypeDef,
    GetAllowListResponseTypeDef,
    GetAutomatedDiscoveryConfigurationResponseTypeDef,
    GetBucketStatisticsResponseTypeDef,
    GetClassificationExportConfigurationResponseTypeDef,
    GetClassificationScopeResponseTypeDef,
    GetCustomDataIdentifierResponseTypeDef,
    GetFindingsFilterResponseTypeDef,
    GetFindingsPublicationConfigurationResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMacieSessionResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberResponseTypeDef,
    GetResourceProfileResponseTypeDef,
    GetRevealConfigurationResponseTypeDef,
    GetSensitiveDataOccurrencesAvailabilityResponseTypeDef,
    GetSensitiveDataOccurrencesResponseTypeDef,
    GetSensitivityInspectionTemplateResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    GetUsageTotalsResponseTypeDef,
    JobScheduleFrequencyTypeDef,
    ListAllowListsResponseTypeDef,
    ListClassificationJobsResponseTypeDef,
    ListClassificationScopesResponseTypeDef,
    ListCustomDataIdentifiersResponseTypeDef,
    ListFindingsFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListJobsFilterCriteriaTypeDef,
    ListJobsSortCriteriaTypeDef,
    ListManagedDataIdentifiersResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListResourceProfileArtifactsResponseTypeDef,
    ListResourceProfileDetectionsResponseTypeDef,
    ListSensitivityInspectionTemplatesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutClassificationExportConfigurationResponseTypeDef,
    RevealConfigurationTypeDef,
    S3ClassificationScopeUpdateTypeDef,
    S3JobDefinitionTypeDef,
    SearchResourcesBucketCriteriaTypeDef,
    SearchResourcesResponseTypeDef,
    SearchResourcesSortCriteriaTypeDef,
    SecurityHubConfigurationTypeDef,
    SensitivityInspectionTemplateExcludesTypeDef,
    SensitivityInspectionTemplateIncludesTypeDef,
    SeverityLevelTypeDef,
    SortCriteriaTypeDef,
    SuppressDataIdentifierTypeDef,
    TestCustomDataIdentifierResponseTypeDef,
    UpdateAllowListResponseTypeDef,
    UpdateFindingsFilterResponseTypeDef,
    UpdateRevealConfigurationResponseTypeDef,
    UsageStatisticsFilterTypeDef,
    UsageStatisticsSortByTypeDef,
)
from .waiter import FindingRevealedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Macie2Client",)

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
    UnprocessableEntityException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Macie2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Macie2Client exceptions.
        """
    def accept_invitation(
        self, *, invitationId: str, administratorAccountId: str = None, masterAccount: str = None
    ) -> Dict[str, Any]:
        """
        Accepts an Amazon Macie membership invitation that was received from a specific
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#accept_invitation)
        """
    def batch_get_custom_data_identifiers(
        self, *, ids: List[str] = None
    ) -> BatchGetCustomDataIdentifiersResponseTypeDef:
        """
        Retrieves information about one or more custom data identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.batch_get_custom_data_identifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#batch_get_custom_data_identifiers)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#close)
        """
    def create_allow_list(
        self,
        *,
        clientToken: str,
        criteria: "AllowListCriteriaTypeDef",
        name: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAllowListResponseTypeDef:
        """
        Creates and defines the settings for an allow list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_allow_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_allow_list)
        """
    def create_classification_job(
        self,
        *,
        clientToken: str,
        jobType: JobTypeType,
        name: str,
        s3JobDefinition: "S3JobDefinitionTypeDef",
        allowListIds: List[str] = None,
        customDataIdentifierIds: List[str] = None,
        description: str = None,
        initialRun: bool = None,
        managedDataIdentifierIds: List[str] = None,
        managedDataIdentifierSelector: ManagedDataIdentifierSelectorType = None,
        samplingPercentage: int = None,
        scheduleFrequency: "JobScheduleFrequencyTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateClassificationJobResponseTypeDef:
        """
        Creates and defines the settings for a classification job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_classification_job)
        """
    def create_custom_data_identifier(
        self,
        *,
        name: str,
        regex: str,
        clientToken: str = None,
        description: str = None,
        ignoreWords: List[str] = None,
        keywords: List[str] = None,
        maximumMatchDistance: int = None,
        severityLevels: List["SeverityLevelTypeDef"] = None,
        tags: Dict[str, str] = None
    ) -> CreateCustomDataIdentifierResponseTypeDef:
        """
        Creates and defines the criteria and other settings for a custom data
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_custom_data_identifier)
        """
    def create_findings_filter(
        self,
        *,
        action: FindingsFilterActionType,
        findingCriteria: "FindingCriteriaTypeDef",
        name: str,
        clientToken: str = None,
        description: str = None,
        position: int = None,
        tags: Dict[str, str] = None
    ) -> CreateFindingsFilterResponseTypeDef:
        """
        Creates and defines the criteria and other settings for a findings filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_findings_filter)
        """
    def create_invitations(
        self, *, accountIds: List[str], disableEmailNotification: bool = None, message: str = None
    ) -> CreateInvitationsResponseTypeDef:
        """
        Sends an Amazon Macie membership invitation to one or more accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_invitations)
        """
    def create_member(
        self, *, account: "AccountDetailTypeDef", tags: Dict[str, str] = None
    ) -> CreateMemberResponseTypeDef:
        """
        Associates an account with an Amazon Macie administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_member)
        """
    def create_sample_findings(
        self, *, findingTypes: List[FindingTypeType] = None
    ) -> Dict[str, Any]:
        """
        Creates sample findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.create_sample_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#create_sample_findings)
        """
    def decline_invitations(self, *, accountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        Declines Amazon Macie membership invitations that were received from specific
        accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#decline_invitations)
        """
    def delete_allow_list(self, *, id: str, ignoreJobChecks: str = None) -> Dict[str, Any]:
        """
        Deletes an allow list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.delete_allow_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_allow_list)
        """
    def delete_custom_data_identifier(self, *, id: str) -> Dict[str, Any]:
        """
        Soft deletes a custom data identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.delete_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_custom_data_identifier)
        """
    def delete_findings_filter(self, *, id: str) -> Dict[str, Any]:
        """
        Deletes a findings filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.delete_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_findings_filter)
        """
    def delete_invitations(self, *, accountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        Deletes Amazon Macie membership invitations that were received from specific
        accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_invitations)
        """
    def delete_member(self, *, id: str) -> Dict[str, Any]:
        """
        Deletes the association between an Amazon Macie administrator account and an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.delete_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#delete_member)
        """
    def describe_buckets(
        self,
        *,
        criteria: Dict[str, "BucketCriteriaAdditionalPropertiesTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: "BucketSortCriteriaTypeDef" = None
    ) -> DescribeBucketsResponseTypeDef:
        """
        Retrieves (queries) statistical data and other information about one or more S3
        buckets that Amazon Macie monitors and analyzes for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.describe_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#describe_buckets)
        """
    def describe_classification_job(
        self, *, jobId: str
    ) -> DescribeClassificationJobResponseTypeDef:
        """
        Retrieves the status and settings for a classification job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.describe_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#describe_classification_job)
        """
    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Retrieves the Amazon Macie configuration settings for an organization in
        Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#describe_organization_configuration)
        """
    def disable_macie(self) -> Dict[str, Any]:
        """
        Disables Amazon Macie and deletes all settings and resources for a Macie
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.disable_macie)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disable_macie)
        """
    def disable_organization_admin_account(self, *, adminAccountId: str) -> Dict[str, Any]:
        """
        Disables an account as the delegated Amazon Macie administrator account for an
        organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disable_organization_admin_account)
        """
    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        Disassociates a member account from its Amazon Macie administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.disassociate_from_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disassociate_from_administrator_account)
        """
    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        (Deprecated) Disassociates a member account from its Amazon Macie administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disassociate_from_master_account)
        """
    def disassociate_member(self, *, id: str) -> Dict[str, Any]:
        """
        Disassociates an Amazon Macie administrator account from a member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.disassociate_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#disassociate_member)
        """
    def enable_macie(
        self,
        *,
        clientToken: str = None,
        findingPublishingFrequency: FindingPublishingFrequencyType = None,
        status: MacieStatusType = None
    ) -> Dict[str, Any]:
        """
        Enables Amazon Macie and specifies the configuration settings for a Macie
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.enable_macie)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#enable_macie)
        """
    def enable_organization_admin_account(
        self, *, adminAccountId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Designates an account as the delegated Amazon Macie administrator account for an
        organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#enable_organization_admin_account)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#generate_presigned_url)
        """
    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        Retrieves information about the Amazon Macie administrator account for an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_administrator_account)
        """
    def get_allow_list(self, *, id: str) -> GetAllowListResponseTypeDef:
        """
        Retrieves the settings and status of an allow list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_allow_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_allow_list)
        """
    def get_automated_discovery_configuration(
        self,
    ) -> GetAutomatedDiscoveryConfigurationResponseTypeDef:
        """
        Retrieves the configuration settings and status of automated sensitive data
        discovery for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_automated_discovery_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_automated_discovery_configuration)
        """
    def get_bucket_statistics(self, *, accountId: str = None) -> GetBucketStatisticsResponseTypeDef:
        """
        Retrieves (queries) aggregated statistical data about all the S3 buckets that
        Amazon Macie monitors and analyzes for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_bucket_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_bucket_statistics)
        """
    def get_classification_export_configuration(
        self,
    ) -> GetClassificationExportConfigurationResponseTypeDef:
        """
        Retrieves the configuration settings for storing data classification results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_classification_export_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_classification_export_configuration)
        """
    def get_classification_scope(self, *, id: str) -> GetClassificationScopeResponseTypeDef:
        """
        Retrieves the classification scope settings for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_classification_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_classification_scope)
        """
    def get_custom_data_identifier(self, *, id: str) -> GetCustomDataIdentifierResponseTypeDef:
        """
        Retrieves the criteria and other settings for a custom data identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_custom_data_identifier)
        """
    def get_finding_statistics(
        self,
        *,
        groupBy: GroupByType,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        size: int = None,
        sortCriteria: "FindingStatisticsSortCriteriaTypeDef" = None
    ) -> GetFindingStatisticsResponseTypeDef:
        """
        Retrieves (queries) aggregated statistical data about findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_finding_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_finding_statistics)
        """
    def get_findings(
        self, *, findingIds: List[str], sortCriteria: "SortCriteriaTypeDef" = None
    ) -> GetFindingsResponseTypeDef:
        """
        Retrieves the details of one or more findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_findings)
        """
    def get_findings_filter(self, *, id: str) -> GetFindingsFilterResponseTypeDef:
        """
        Retrieves the criteria and other settings for a findings filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_findings_filter)
        """
    def get_findings_publication_configuration(
        self,
    ) -> GetFindingsPublicationConfigurationResponseTypeDef:
        """
        Retrieves the configuration settings for publishing findings to Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_findings_publication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_findings_publication_configuration)
        """
    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        Retrieves the count of Amazon Macie membership invitations that were received by
        an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_invitations_count)
        """
    def get_macie_session(self) -> GetMacieSessionResponseTypeDef:
        """
        Retrieves the status and configuration settings for an Amazon Macie account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_macie_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_macie_session)
        """
    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        (Deprecated) Retrieves information about the Amazon Macie administrator account
        for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_master_account)
        """
    def get_member(self, *, id: str) -> GetMemberResponseTypeDef:
        """
        Retrieves information about an account that's associated with an Amazon Macie
        administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_member)
        """
    def get_resource_profile(self, *, resourceArn: str) -> GetResourceProfileResponseTypeDef:
        """
        Retrieves (queries) sensitive data discovery statistics and the sensitivity
        score for an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_resource_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_resource_profile)
        """
    def get_reveal_configuration(self) -> GetRevealConfigurationResponseTypeDef:
        """
        Retrieves the status and configuration settings for retrieving occurrences of
        sensitive data reported by findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_reveal_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_reveal_configuration)
        """
    def get_sensitive_data_occurrences(
        self, *, findingId: str
    ) -> GetSensitiveDataOccurrencesResponseTypeDef:
        """
        Retrieves occurrences of sensitive data reported by a finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_sensitive_data_occurrences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_sensitive_data_occurrences)
        """
    def get_sensitive_data_occurrences_availability(
        self, *, findingId: str
    ) -> GetSensitiveDataOccurrencesAvailabilityResponseTypeDef:
        """
        Checks whether occurrences of sensitive data can be retrieved for a finding.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_sensitive_data_occurrences_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_sensitive_data_occurrences_availability)
        """
    def get_sensitivity_inspection_template(
        self, *, id: str
    ) -> GetSensitivityInspectionTemplateResponseTypeDef:
        """
        Retrieves the settings for the sensitivity inspection template for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_sensitivity_inspection_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_sensitivity_inspection_template)
        """
    def get_usage_statistics(
        self,
        *,
        filterBy: List["UsageStatisticsFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: "UsageStatisticsSortByTypeDef" = None,
        timeRange: TimeRangeType = None
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        Retrieves (queries) quotas and aggregated usage data for one or more accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_usage_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_usage_statistics)
        """
    def get_usage_totals(self, *, timeRange: str = None) -> GetUsageTotalsResponseTypeDef:
        """
        Retrieves (queries) aggregated usage data for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.get_usage_totals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#get_usage_totals)
        """
    def list_allow_lists(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAllowListsResponseTypeDef:
        """
        Retrieves a subset of information about all the allow lists for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_allow_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_allow_lists)
        """
    def list_classification_jobs(
        self,
        *,
        filterCriteria: "ListJobsFilterCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: "ListJobsSortCriteriaTypeDef" = None
    ) -> ListClassificationJobsResponseTypeDef:
        """
        Retrieves a subset of information about one or more classification jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_classification_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_classification_jobs)
        """
    def list_classification_scopes(
        self, *, name: str = None, nextToken: str = None
    ) -> ListClassificationScopesResponseTypeDef:
        """
        Retrieves a subset of information about the classification scope for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_classification_scopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_classification_scopes)
        """
    def list_custom_data_identifiers(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListCustomDataIdentifiersResponseTypeDef:
        """
        Retrieves a subset of information about all the custom data identifiers for an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_custom_data_identifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_custom_data_identifiers)
        """
    def list_findings(
        self,
        *,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: "SortCriteriaTypeDef" = None
    ) -> ListFindingsResponseTypeDef:
        """
        Retrieves a subset of information about one or more findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_findings)
        """
    def list_findings_filters(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListFindingsFiltersResponseTypeDef:
        """
        Retrieves a subset of information about all the findings filters for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_findings_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_findings_filters)
        """
    def list_invitations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        Retrieves information about the Amazon Macie membership invitations that were
        received by an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_invitations)
        """
    def list_managed_data_identifiers(
        self, *, nextToken: str = None
    ) -> ListManagedDataIdentifiersResponseTypeDef:
        """
        Retrieves information about all the managed data identifiers that Amazon Macie
        currently provides.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_managed_data_identifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_managed_data_identifiers)
        """
    def list_members(
        self, *, maxResults: int = None, nextToken: str = None, onlyAssociated: str = None
    ) -> ListMembersResponseTypeDef:
        """
        Retrieves information about the accounts that are associated with an Amazon
        Macie administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_members)
        """
    def list_organization_admin_accounts(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        Retrieves information about the delegated Amazon Macie administrator account for
        an organization in Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_organization_admin_accounts)
        """
    def list_resource_profile_artifacts(
        self, *, resourceArn: str, nextToken: str = None
    ) -> ListResourceProfileArtifactsResponseTypeDef:
        """
        Retrieves information about objects that were selected from an S3 bucket for
        automated sensitive data discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_resource_profile_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_resource_profile_artifacts)
        """
    def list_resource_profile_detections(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListResourceProfileDetectionsResponseTypeDef:
        """
        Retrieves information about the types and amount of sensitive data that Amazon
        Macie found in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_resource_profile_detections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_resource_profile_detections)
        """
    def list_sensitivity_inspection_templates(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSensitivityInspectionTemplatesResponseTypeDef:
        """
        Retrieves a subset of information about the sensitivity inspection template for
        an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_sensitivity_inspection_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_sensitivity_inspection_templates)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags (keys and values) that are associated with an Amazon Macie
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#list_tags_for_resource)
        """
    def put_classification_export_configuration(
        self, *, configuration: "ClassificationExportConfigurationTypeDef"
    ) -> PutClassificationExportConfigurationResponseTypeDef:
        """
        Creates or updates the configuration settings for storing data classification
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.put_classification_export_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#put_classification_export_configuration)
        """
    def put_findings_publication_configuration(
        self,
        *,
        clientToken: str = None,
        securityHubConfiguration: "SecurityHubConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration settings for publishing findings to Security Hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.put_findings_publication_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#put_findings_publication_configuration)
        """
    def search_resources(
        self,
        *,
        bucketCriteria: "SearchResourcesBucketCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: "SearchResourcesSortCriteriaTypeDef" = None
    ) -> SearchResourcesResponseTypeDef:
        """
        Retrieves (queries) statistical data and other information about Amazon Web
        Services resources that Amazon Macie monitors and analyzes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.search_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#search_resources)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds or updates one or more tags (keys and values) that are associated with an
        Amazon Macie resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#tag_resource)
        """
    def test_custom_data_identifier(
        self,
        *,
        regex: str,
        sampleText: str,
        ignoreWords: List[str] = None,
        keywords: List[str] = None,
        maximumMatchDistance: int = None
    ) -> TestCustomDataIdentifierResponseTypeDef:
        """
        Tests a custom data identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.test_custom_data_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#test_custom_data_identifier)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags (keys and values) from an Amazon Macie resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#untag_resource)
        """
    def update_allow_list(
        self, *, criteria: "AllowListCriteriaTypeDef", id: str, name: str, description: str = None
    ) -> UpdateAllowListResponseTypeDef:
        """
        Updates the settings for an allow list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_allow_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_allow_list)
        """
    def update_automated_discovery_configuration(
        self, *, status: AutomatedDiscoveryStatusType
    ) -> Dict[str, Any]:
        """
        Enables or disables automated sensitive data discovery for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_automated_discovery_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_automated_discovery_configuration)
        """
    def update_classification_job(self, *, jobId: str, jobStatus: JobStatusType) -> Dict[str, Any]:
        """
        Changes the status of a classification job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_classification_job)
        """
    def update_classification_scope(
        self, *, id: str, s3: "S3ClassificationScopeUpdateTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the classification scope settings for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_classification_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_classification_scope)
        """
    def update_findings_filter(
        self,
        *,
        id: str,
        action: FindingsFilterActionType = None,
        clientToken: str = None,
        description: str = None,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        name: str = None,
        position: int = None
    ) -> UpdateFindingsFilterResponseTypeDef:
        """
        Updates the criteria and other settings for a findings filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_findings_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_findings_filter)
        """
    def update_macie_session(
        self,
        *,
        findingPublishingFrequency: FindingPublishingFrequencyType = None,
        status: MacieStatusType = None
    ) -> Dict[str, Any]:
        """
        Suspends or re-enables Amazon Macie, or updates the configuration settings for a
        Macie account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_macie_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_macie_session)
        """
    def update_member_session(self, *, id: str, status: MacieStatusType) -> Dict[str, Any]:
        """
        Enables an Amazon Macie administrator to suspend or re-enable Macie for a member
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_member_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_member_session)
        """
    def update_organization_configuration(self, *, autoEnable: bool) -> Dict[str, Any]:
        """
        Updates the Amazon Macie configuration settings for an organization in
        Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_organization_configuration)
        """
    def update_resource_profile(
        self, *, resourceArn: str, sensitivityScoreOverride: int = None
    ) -> Dict[str, Any]:
        """
        Updates the sensitivity score for an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_resource_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_resource_profile)
        """
    def update_resource_profile_detections(
        self,
        *,
        resourceArn: str,
        suppressDataIdentifiers: List["SuppressDataIdentifierTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates the sensitivity scoring settings for an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_resource_profile_detections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_resource_profile_detections)
        """
    def update_reveal_configuration(
        self, *, configuration: "RevealConfigurationTypeDef"
    ) -> UpdateRevealConfigurationResponseTypeDef:
        """
        Updates the status and configuration settings for retrieving occurrences of
        sensitive data reported by findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_reveal_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_reveal_configuration)
        """
    def update_sensitivity_inspection_template(
        self,
        *,
        id: str,
        description: str = None,
        excludes: "SensitivityInspectionTemplateExcludesTypeDef" = None,
        includes: "SensitivityInspectionTemplateIncludesTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the settings for the sensitivity inspection template for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Client.update_sensitivity_inspection_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/client.html#update_sensitivity_inspection_template)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_buckets"]
    ) -> DescribeBucketsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.DescribeBuckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#describebucketspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_statistics"]
    ) -> GetUsageStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.GetUsageStatistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#getusagestatisticspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_allow_lists"]) -> ListAllowListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListAllowLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listallowlistspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_classification_jobs"]
    ) -> ListClassificationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListClassificationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listclassificationjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_classification_scopes"]
    ) -> ListClassificationScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListClassificationScopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listclassificationscopespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_data_identifiers"]
    ) -> ListCustomDataIdentifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListCustomDataIdentifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listcustomdataidentifierspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listfindingspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_findings_filters"]
    ) -> ListFindingsFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListFindingsFilters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listfindingsfilterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListInvitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listinvitationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_data_identifiers"]
    ) -> ListManagedDataIdentifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListManagedDataIdentifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listmanageddataidentifierspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListMembers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listmemberspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListOrganizationAdminAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listorganizationadminaccountspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_profile_artifacts"]
    ) -> ListResourceProfileArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListResourceProfileArtifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listresourceprofileartifactspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_profile_detections"]
    ) -> ListResourceProfileDetectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListResourceProfileDetections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listresourceprofiledetectionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sensitivity_inspection_templates"]
    ) -> ListSensitivityInspectionTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.ListSensitivityInspectionTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#listsensitivityinspectiontemplatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_resources"]
    ) -> SearchResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Paginator.SearchResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/paginators.html#searchresourcespaginator)
        """
    def get_waiter(self, waiter_name: Literal["finding_revealed"]) -> FindingRevealedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/macie2.html#Macie2.Waiter.FindingRevealed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/waiters.html#findingrevealedwaiter)
        """
