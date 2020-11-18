# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for config service client

Usage::

    ```python
    import boto3
    from mypy_boto3_config import ConfigServiceClient

    client: ConfigServiceClient = boto3.client("config")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_config.paginator import (
    DescribeAggregateComplianceByConfigRulesPaginator,
    DescribeAggregationAuthorizationsPaginator,
    DescribeComplianceByConfigRulePaginator,
    DescribeComplianceByResourcePaginator,
    DescribeConfigRuleEvaluationStatusPaginator,
    DescribeConfigRulesPaginator,
    DescribeConfigurationAggregatorSourcesStatusPaginator,
    DescribeConfigurationAggregatorsPaginator,
    DescribePendingAggregationRequestsPaginator,
    DescribeRemediationExecutionStatusPaginator,
    DescribeRetentionConfigurationsPaginator,
    GetAggregateComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByConfigRulePaginator,
    GetComplianceDetailsByResourcePaginator,
    GetResourceConfigHistoryPaginator,
    ListAggregateDiscoveredResourcesPaginator,
    ListDiscoveredResourcesPaginator,
)
from mypy_boto3_config.type_defs import (
    AccountAggregationSourceTypeDef,
    AggregateResourceIdentifierTypeDef,
    BatchGetAggregateResourceConfigResponseTypeDef,
    BatchGetResourceConfigResponseTypeDef,
    ConfigRuleComplianceFiltersTypeDef,
    ConfigRuleComplianceSummaryFiltersTypeDef,
    ConfigRuleTypeDef,
    ConfigurationRecorderTypeDef,
    ConformancePackComplianceFiltersTypeDef,
    ConformancePackEvaluationFiltersTypeDef,
    ConformancePackInputParameterTypeDef,
    DeleteRemediationExceptionsResponseTypeDef,
    DeliverConfigSnapshotResponseTypeDef,
    DeliveryChannelTypeDef,
    DescribeAggregateComplianceByConfigRulesResponseTypeDef,
    DescribeAggregationAuthorizationsResponseTypeDef,
    DescribeComplianceByConfigRuleResponseTypeDef,
    DescribeComplianceByResourceResponseTypeDef,
    DescribeConfigRuleEvaluationStatusResponseTypeDef,
    DescribeConfigRulesResponseTypeDef,
    DescribeConfigurationAggregatorSourcesStatusResponseTypeDef,
    DescribeConfigurationAggregatorsResponseTypeDef,
    DescribeConfigurationRecordersResponseTypeDef,
    DescribeConfigurationRecorderStatusResponseTypeDef,
    DescribeConformancePackComplianceResponseTypeDef,
    DescribeConformancePacksResponseTypeDef,
    DescribeConformancePackStatusResponseTypeDef,
    DescribeDeliveryChannelsResponseTypeDef,
    DescribeDeliveryChannelStatusResponseTypeDef,
    DescribeOrganizationConfigRulesResponseTypeDef,
    DescribeOrganizationConfigRuleStatusesResponseTypeDef,
    DescribeOrganizationConformancePacksResponseTypeDef,
    DescribeOrganizationConformancePackStatusesResponseTypeDef,
    DescribePendingAggregationRequestsResponseTypeDef,
    DescribeRemediationConfigurationsResponseTypeDef,
    DescribeRemediationExceptionsResponseTypeDef,
    DescribeRemediationExecutionStatusResponseTypeDef,
    DescribeRetentionConfigurationsResponseTypeDef,
    EvaluationTypeDef,
    GetAggregateComplianceDetailsByConfigRuleResponseTypeDef,
    GetAggregateConfigRuleComplianceSummaryResponseTypeDef,
    GetAggregateDiscoveredResourceCountsResponseTypeDef,
    GetAggregateResourceConfigResponseTypeDef,
    GetComplianceDetailsByConfigRuleResponseTypeDef,
    GetComplianceDetailsByResourceResponseTypeDef,
    GetComplianceSummaryByConfigRuleResponseTypeDef,
    GetComplianceSummaryByResourceTypeResponseTypeDef,
    GetConformancePackComplianceDetailsResponseTypeDef,
    GetConformancePackComplianceSummaryResponseTypeDef,
    GetDiscoveredResourceCountsResponseTypeDef,
    GetOrganizationConfigRuleDetailedStatusResponseTypeDef,
    GetOrganizationConformancePackDetailedStatusResponseTypeDef,
    GetResourceConfigHistoryResponseTypeDef,
    ListAggregateDiscoveredResourcesResponseTypeDef,
    ListDiscoveredResourcesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OrganizationAggregationSourceTypeDef,
    OrganizationCustomRuleMetadataTypeDef,
    OrganizationManagedRuleMetadataTypeDef,
    OrganizationResourceDetailedStatusFiltersTypeDef,
    PutAggregationAuthorizationResponseTypeDef,
    PutConfigurationAggregatorResponseTypeDef,
    PutConformancePackResponseTypeDef,
    PutEvaluationsResponseTypeDef,
    PutOrganizationConfigRuleResponseTypeDef,
    PutOrganizationConformancePackResponseTypeDef,
    PutRemediationConfigurationsResponseTypeDef,
    PutRemediationExceptionsResponseTypeDef,
    PutRetentionConfigurationResponseTypeDef,
    RemediationConfigurationTypeDef,
    RemediationExceptionResourceKeyTypeDef,
    ResourceCountFiltersTypeDef,
    ResourceFiltersTypeDef,
    ResourceKeyTypeDef,
    SelectAggregateResourceConfigResponseTypeDef,
    SelectResourceConfigResponseTypeDef,
    StartRemediationExecutionResponseTypeDef,
    StatusDetailFiltersTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConfigServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConformancePackTemplateValidationException: Type[BotocoreClientError]
    InsufficientDeliveryPolicyException: Type[BotocoreClientError]
    InsufficientPermissionsException: Type[BotocoreClientError]
    InvalidConfigurationRecorderNameException: Type[BotocoreClientError]
    InvalidDeliveryChannelNameException: Type[BotocoreClientError]
    InvalidExpressionException: Type[BotocoreClientError]
    InvalidLimitException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRecordingGroupException: Type[BotocoreClientError]
    InvalidResultTokenException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    InvalidS3KeyPrefixException: Type[BotocoreClientError]
    InvalidSNSTopicARNException: Type[BotocoreClientError]
    InvalidTimeRangeException: Type[BotocoreClientError]
    LastDeliveryChannelDeleteFailedException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MaxActiveResourcesExceededException: Type[BotocoreClientError]
    MaxNumberOfConfigRulesExceededException: Type[BotocoreClientError]
    MaxNumberOfConfigurationRecordersExceededException: Type[BotocoreClientError]
    MaxNumberOfConformancePacksExceededException: Type[BotocoreClientError]
    MaxNumberOfDeliveryChannelsExceededException: Type[BotocoreClientError]
    MaxNumberOfOrganizationConfigRulesExceededException: Type[BotocoreClientError]
    MaxNumberOfOrganizationConformancePacksExceededException: Type[BotocoreClientError]
    MaxNumberOfRetentionConfigurationsExceededException: Type[BotocoreClientError]
    NoAvailableConfigurationRecorderException: Type[BotocoreClientError]
    NoAvailableDeliveryChannelException: Type[BotocoreClientError]
    NoAvailableOrganizationException: Type[BotocoreClientError]
    NoRunningConfigurationRecorderException: Type[BotocoreClientError]
    NoSuchBucketException: Type[BotocoreClientError]
    NoSuchConfigRuleException: Type[BotocoreClientError]
    NoSuchConfigRuleInConformancePackException: Type[BotocoreClientError]
    NoSuchConfigurationAggregatorException: Type[BotocoreClientError]
    NoSuchConfigurationRecorderException: Type[BotocoreClientError]
    NoSuchConformancePackException: Type[BotocoreClientError]
    NoSuchDeliveryChannelException: Type[BotocoreClientError]
    NoSuchOrganizationConfigRuleException: Type[BotocoreClientError]
    NoSuchOrganizationConformancePackException: Type[BotocoreClientError]
    NoSuchRemediationConfigurationException: Type[BotocoreClientError]
    NoSuchRemediationExceptionException: Type[BotocoreClientError]
    NoSuchRetentionConfigurationException: Type[BotocoreClientError]
    OrganizationAccessDeniedException: Type[BotocoreClientError]
    OrganizationAllFeaturesNotEnabledException: Type[BotocoreClientError]
    OrganizationConformancePackTemplateValidationException: Type[BotocoreClientError]
    OversizedConfigurationItemException: Type[BotocoreClientError]
    RemediationInProgressException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotDiscoveredException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ConfigServiceClient:
    """
    [ConfigService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_aggregate_resource_config(
        self,
        ConfigurationAggregatorName: str,
        ResourceIdentifiers: List["AggregateResourceIdentifierTypeDef"],
    ) -> BatchGetAggregateResourceConfigResponseTypeDef:
        """
        [Client.batch_get_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.batch_get_aggregate_resource_config)
        """

    def batch_get_resource_config(
        self, resourceKeys: List["ResourceKeyTypeDef"]
    ) -> BatchGetResourceConfigResponseTypeDef:
        """
        [Client.batch_get_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.batch_get_resource_config)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.can_paginate)
        """

    def delete_aggregation_authorization(
        self, AuthorizedAccountId: str, AuthorizedAwsRegion: str
    ) -> None:
        """
        [Client.delete_aggregation_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_aggregation_authorization)
        """

    def delete_config_rule(self, ConfigRuleName: str) -> None:
        """
        [Client.delete_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_config_rule)
        """

    def delete_configuration_aggregator(self, ConfigurationAggregatorName: str) -> None:
        """
        [Client.delete_configuration_aggregator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_configuration_aggregator)
        """

    def delete_configuration_recorder(self, ConfigurationRecorderName: str) -> None:
        """
        [Client.delete_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_configuration_recorder)
        """

    def delete_conformance_pack(self, ConformancePackName: str) -> None:
        """
        [Client.delete_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_conformance_pack)
        """

    def delete_delivery_channel(self, DeliveryChannelName: str) -> None:
        """
        [Client.delete_delivery_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_delivery_channel)
        """

    def delete_evaluation_results(self, ConfigRuleName: str) -> Dict[str, Any]:
        """
        [Client.delete_evaluation_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_evaluation_results)
        """

    def delete_organization_config_rule(self, OrganizationConfigRuleName: str) -> None:
        """
        [Client.delete_organization_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_organization_config_rule)
        """

    def delete_organization_conformance_pack(self, OrganizationConformancePackName: str) -> None:
        """
        [Client.delete_organization_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_organization_conformance_pack)
        """

    def delete_pending_aggregation_request(
        self, RequesterAccountId: str, RequesterAwsRegion: str
    ) -> None:
        """
        [Client.delete_pending_aggregation_request documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_pending_aggregation_request)
        """

    def delete_remediation_configuration(
        self, ConfigRuleName: str, ResourceType: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_remediation_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_remediation_configuration)
        """

    def delete_remediation_exceptions(
        self, ConfigRuleName: str, ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"]
    ) -> DeleteRemediationExceptionsResponseTypeDef:
        """
        [Client.delete_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_remediation_exceptions)
        """

    def delete_resource_config(self, ResourceType: str, ResourceId: str) -> None:
        """
        [Client.delete_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_resource_config)
        """

    def delete_retention_configuration(self, RetentionConfigurationName: str) -> None:
        """
        [Client.delete_retention_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.delete_retention_configuration)
        """

    def deliver_config_snapshot(
        self, deliveryChannelName: str
    ) -> DeliverConfigSnapshotResponseTypeDef:
        """
        [Client.deliver_config_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.deliver_config_snapshot)
        """

    def describe_aggregate_compliance_by_config_rules(
        self,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeAggregateComplianceByConfigRulesResponseTypeDef:
        """
        [Client.describe_aggregate_compliance_by_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_aggregate_compliance_by_config_rules)
        """

    def describe_aggregation_authorizations(
        self, Limit: int = None, NextToken: str = None
    ) -> DescribeAggregationAuthorizationsResponseTypeDef:
        """
        [Client.describe_aggregation_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_aggregation_authorizations)
        """

    def describe_compliance_by_config_rule(
        self,
        ConfigRuleNames: List[str] = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        NextToken: str = None,
    ) -> DescribeComplianceByConfigRuleResponseTypeDef:
        """
        [Client.describe_compliance_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_compliance_by_config_rule)
        """

    def describe_compliance_by_resource(
        self,
        ResourceType: str = None,
        ResourceId: str = None,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeComplianceByResourceResponseTypeDef:
        """
        [Client.describe_compliance_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_compliance_by_resource)
        """

    def describe_config_rule_evaluation_status(
        self, ConfigRuleNames: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> DescribeConfigRuleEvaluationStatusResponseTypeDef:
        """
        [Client.describe_config_rule_evaluation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_config_rule_evaluation_status)
        """

    def describe_config_rules(
        self, ConfigRuleNames: List[str] = None, NextToken: str = None
    ) -> DescribeConfigRulesResponseTypeDef:
        """
        [Client.describe_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_config_rules)
        """

    def describe_configuration_aggregator_sources_status(
        self,
        ConfigurationAggregatorName: str,
        UpdateStatus: List[Literal["FAILED", "SUCCEEDED", "OUTDATED"]] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeConfigurationAggregatorSourcesStatusResponseTypeDef:
        """
        [Client.describe_configuration_aggregator_sources_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_configuration_aggregator_sources_status)
        """

    def describe_configuration_aggregators(
        self,
        ConfigurationAggregatorNames: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeConfigurationAggregatorsResponseTypeDef:
        """
        [Client.describe_configuration_aggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_configuration_aggregators)
        """

    def describe_configuration_recorder_status(
        self, ConfigurationRecorderNames: List[str] = None
    ) -> DescribeConfigurationRecorderStatusResponseTypeDef:
        """
        [Client.describe_configuration_recorder_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_configuration_recorder_status)
        """

    def describe_configuration_recorders(
        self, ConfigurationRecorderNames: List[str] = None
    ) -> DescribeConfigurationRecordersResponseTypeDef:
        """
        [Client.describe_configuration_recorders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_configuration_recorders)
        """

    def describe_conformance_pack_compliance(
        self,
        ConformancePackName: str,
        Filters: ConformancePackComplianceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeConformancePackComplianceResponseTypeDef:
        """
        [Client.describe_conformance_pack_compliance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_conformance_pack_compliance)
        """

    def describe_conformance_pack_status(
        self, ConformancePackNames: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeConformancePackStatusResponseTypeDef:
        """
        [Client.describe_conformance_pack_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_conformance_pack_status)
        """

    def describe_conformance_packs(
        self, ConformancePackNames: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeConformancePacksResponseTypeDef:
        """
        [Client.describe_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_conformance_packs)
        """

    def describe_delivery_channel_status(
        self, DeliveryChannelNames: List[str] = None
    ) -> DescribeDeliveryChannelStatusResponseTypeDef:
        """
        [Client.describe_delivery_channel_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_delivery_channel_status)
        """

    def describe_delivery_channels(
        self, DeliveryChannelNames: List[str] = None
    ) -> DescribeDeliveryChannelsResponseTypeDef:
        """
        [Client.describe_delivery_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_delivery_channels)
        """

    def describe_organization_config_rule_statuses(
        self,
        OrganizationConfigRuleNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeOrganizationConfigRuleStatusesResponseTypeDef:
        """
        [Client.describe_organization_config_rule_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_organization_config_rule_statuses)
        """

    def describe_organization_config_rules(
        self,
        OrganizationConfigRuleNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeOrganizationConfigRulesResponseTypeDef:
        """
        [Client.describe_organization_config_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_organization_config_rules)
        """

    def describe_organization_conformance_pack_statuses(
        self,
        OrganizationConformancePackNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeOrganizationConformancePackStatusesResponseTypeDef:
        """
        [Client.describe_organization_conformance_pack_statuses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_organization_conformance_pack_statuses)
        """

    def describe_organization_conformance_packs(
        self,
        OrganizationConformancePackNames: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeOrganizationConformancePacksResponseTypeDef:
        """
        [Client.describe_organization_conformance_packs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_organization_conformance_packs)
        """

    def describe_pending_aggregation_requests(
        self, Limit: int = None, NextToken: str = None
    ) -> DescribePendingAggregationRequestsResponseTypeDef:
        """
        [Client.describe_pending_aggregation_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_pending_aggregation_requests)
        """

    def describe_remediation_configurations(
        self, ConfigRuleNames: List[str]
    ) -> DescribeRemediationConfigurationsResponseTypeDef:
        """
        [Client.describe_remediation_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_remediation_configurations)
        """

    def describe_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeRemediationExceptionsResponseTypeDef:
        """
        [Client.describe_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_remediation_exceptions)
        """

    def describe_remediation_execution_status(
        self,
        ConfigRuleName: str,
        ResourceKeys: List["ResourceKeyTypeDef"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeRemediationExecutionStatusResponseTypeDef:
        """
        [Client.describe_remediation_execution_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_remediation_execution_status)
        """

    def describe_retention_configurations(
        self, RetentionConfigurationNames: List[str] = None, NextToken: str = None
    ) -> DescribeRetentionConfigurationsResponseTypeDef:
        """
        [Client.describe_retention_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.describe_retention_configurations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.generate_presigned_url)
        """

    def get_aggregate_compliance_details_by_config_rule(
        self,
        ConfigurationAggregatorName: str,
        ConfigRuleName: str,
        AccountId: str,
        AwsRegion: str,
        ComplianceType: Literal[
            "COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"
        ] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetAggregateComplianceDetailsByConfigRuleResponseTypeDef:
        """
        [Client.get_aggregate_compliance_details_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_aggregate_compliance_details_by_config_rule)
        """

    def get_aggregate_config_rule_compliance_summary(
        self,
        ConfigurationAggregatorName: str,
        Filters: ConfigRuleComplianceSummaryFiltersTypeDef = None,
        GroupByKey: Literal["ACCOUNT_ID", "AWS_REGION"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetAggregateConfigRuleComplianceSummaryResponseTypeDef:
        """
        [Client.get_aggregate_config_rule_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_aggregate_config_rule_compliance_summary)
        """

    def get_aggregate_discovered_resource_counts(
        self,
        ConfigurationAggregatorName: str,
        Filters: ResourceCountFiltersTypeDef = None,
        GroupByKey: Literal["RESOURCE_TYPE", "ACCOUNT_ID", "AWS_REGION"] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetAggregateDiscoveredResourceCountsResponseTypeDef:
        """
        [Client.get_aggregate_discovered_resource_counts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_aggregate_discovered_resource_counts)
        """

    def get_aggregate_resource_config(
        self,
        ConfigurationAggregatorName: str,
        ResourceIdentifier: "AggregateResourceIdentifierTypeDef",
    ) -> GetAggregateResourceConfigResponseTypeDef:
        """
        [Client.get_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_aggregate_resource_config)
        """

    def get_compliance_details_by_config_rule(
        self,
        ConfigRuleName: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetComplianceDetailsByConfigRuleResponseTypeDef:
        """
        [Client.get_compliance_details_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_compliance_details_by_config_rule)
        """

    def get_compliance_details_by_resource(
        self,
        ResourceType: str,
        ResourceId: str,
        ComplianceTypes: List[
            Literal["COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE", "INSUFFICIENT_DATA"]
        ] = None,
        NextToken: str = None,
    ) -> GetComplianceDetailsByResourceResponseTypeDef:
        """
        [Client.get_compliance_details_by_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_compliance_details_by_resource)
        """

    def get_compliance_summary_by_config_rule(
        self,
    ) -> GetComplianceSummaryByConfigRuleResponseTypeDef:
        """
        [Client.get_compliance_summary_by_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_config_rule)
        """

    def get_compliance_summary_by_resource_type(
        self, ResourceTypes: List[str] = None
    ) -> GetComplianceSummaryByResourceTypeResponseTypeDef:
        """
        [Client.get_compliance_summary_by_resource_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_compliance_summary_by_resource_type)
        """

    def get_conformance_pack_compliance_details(
        self,
        ConformancePackName: str,
        Filters: ConformancePackEvaluationFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetConformancePackComplianceDetailsResponseTypeDef:
        """
        [Client.get_conformance_pack_compliance_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_details)
        """

    def get_conformance_pack_compliance_summary(
        self, ConformancePackNames: List[str], Limit: int = None, NextToken: str = None
    ) -> GetConformancePackComplianceSummaryResponseTypeDef:
        """
        [Client.get_conformance_pack_compliance_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_conformance_pack_compliance_summary)
        """

    def get_discovered_resource_counts(
        self, resourceTypes: List[str] = None, limit: int = None, nextToken: str = None
    ) -> GetDiscoveredResourceCountsResponseTypeDef:
        """
        [Client.get_discovered_resource_counts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_discovered_resource_counts)
        """

    def get_organization_config_rule_detailed_status(
        self,
        OrganizationConfigRuleName: str,
        Filters: StatusDetailFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetOrganizationConfigRuleDetailedStatusResponseTypeDef:
        """
        [Client.get_organization_config_rule_detailed_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_organization_config_rule_detailed_status)
        """

    def get_organization_conformance_pack_detailed_status(
        self,
        OrganizationConformancePackName: str,
        Filters: OrganizationResourceDetailedStatusFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> GetOrganizationConformancePackDetailedStatusResponseTypeDef:
        """
        [Client.get_organization_conformance_pack_detailed_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_organization_conformance_pack_detailed_status)
        """

    def get_resource_config_history(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::Elasticsearch::Domain",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::WAFv2::WebACL",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::SQS::Queue",
            "AWS::KMS::Key",
            "AWS::QLDB::Ledger",
            "AWS::SecretsManager::Secret",
            "AWS::SNS::Topic",
            "AWS::SSM::FileData",
        ],
        resourceId: str,
        laterTime: datetime = None,
        earlierTime: datetime = None,
        chronologicalOrder: Literal["Reverse", "Forward"] = None,
        limit: int = None,
        nextToken: str = None,
    ) -> GetResourceConfigHistoryResponseTypeDef:
        """
        [Client.get_resource_config_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.get_resource_config_history)
        """

    def list_aggregate_discovered_resources(
        self,
        ConfigurationAggregatorName: str,
        ResourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::Elasticsearch::Domain",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::WAFv2::WebACL",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::SQS::Queue",
            "AWS::KMS::Key",
            "AWS::QLDB::Ledger",
            "AWS::SecretsManager::Secret",
            "AWS::SNS::Topic",
            "AWS::SSM::FileData",
        ],
        Filters: ResourceFiltersTypeDef = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ListAggregateDiscoveredResourcesResponseTypeDef:
        """
        [Client.list_aggregate_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.list_aggregate_discovered_resources)
        """

    def list_discovered_resources(
        self,
        resourceType: Literal[
            "AWS::EC2::CustomerGateway",
            "AWS::EC2::EIP",
            "AWS::EC2::Host",
            "AWS::EC2::Instance",
            "AWS::EC2::InternetGateway",
            "AWS::EC2::NetworkAcl",
            "AWS::EC2::NetworkInterface",
            "AWS::EC2::RouteTable",
            "AWS::EC2::SecurityGroup",
            "AWS::EC2::Subnet",
            "AWS::CloudTrail::Trail",
            "AWS::EC2::Volume",
            "AWS::EC2::VPC",
            "AWS::EC2::VPNConnection",
            "AWS::EC2::VPNGateway",
            "AWS::EC2::RegisteredHAInstance",
            "AWS::EC2::NatGateway",
            "AWS::EC2::EgressOnlyInternetGateway",
            "AWS::EC2::VPCEndpoint",
            "AWS::EC2::VPCEndpointService",
            "AWS::EC2::FlowLog",
            "AWS::EC2::VPCPeeringConnection",
            "AWS::Elasticsearch::Domain",
            "AWS::IAM::Group",
            "AWS::IAM::Policy",
            "AWS::IAM::Role",
            "AWS::IAM::User",
            "AWS::ElasticLoadBalancingV2::LoadBalancer",
            "AWS::ACM::Certificate",
            "AWS::RDS::DBInstance",
            "AWS::RDS::DBSubnetGroup",
            "AWS::RDS::DBSecurityGroup",
            "AWS::RDS::DBSnapshot",
            "AWS::RDS::DBCluster",
            "AWS::RDS::DBClusterSnapshot",
            "AWS::RDS::EventSubscription",
            "AWS::S3::Bucket",
            "AWS::S3::AccountPublicAccessBlock",
            "AWS::Redshift::Cluster",
            "AWS::Redshift::ClusterSnapshot",
            "AWS::Redshift::ClusterParameterGroup",
            "AWS::Redshift::ClusterSecurityGroup",
            "AWS::Redshift::ClusterSubnetGroup",
            "AWS::Redshift::EventSubscription",
            "AWS::SSM::ManagedInstanceInventory",
            "AWS::CloudWatch::Alarm",
            "AWS::CloudFormation::Stack",
            "AWS::ElasticLoadBalancing::LoadBalancer",
            "AWS::AutoScaling::AutoScalingGroup",
            "AWS::AutoScaling::LaunchConfiguration",
            "AWS::AutoScaling::ScalingPolicy",
            "AWS::AutoScaling::ScheduledAction",
            "AWS::DynamoDB::Table",
            "AWS::CodeBuild::Project",
            "AWS::WAF::RateBasedRule",
            "AWS::WAF::Rule",
            "AWS::WAF::RuleGroup",
            "AWS::WAF::WebACL",
            "AWS::WAFRegional::RateBasedRule",
            "AWS::WAFRegional::Rule",
            "AWS::WAFRegional::RuleGroup",
            "AWS::WAFRegional::WebACL",
            "AWS::CloudFront::Distribution",
            "AWS::CloudFront::StreamingDistribution",
            "AWS::Lambda::Function",
            "AWS::ElasticBeanstalk::Application",
            "AWS::ElasticBeanstalk::ApplicationVersion",
            "AWS::ElasticBeanstalk::Environment",
            "AWS::WAFv2::WebACL",
            "AWS::WAFv2::RuleGroup",
            "AWS::WAFv2::IPSet",
            "AWS::WAFv2::RegexPatternSet",
            "AWS::WAFv2::ManagedRuleSet",
            "AWS::XRay::EncryptionConfig",
            "AWS::SSM::AssociationCompliance",
            "AWS::SSM::PatchCompliance",
            "AWS::Shield::Protection",
            "AWS::ShieldRegional::Protection",
            "AWS::Config::ResourceCompliance",
            "AWS::ApiGateway::Stage",
            "AWS::ApiGateway::RestApi",
            "AWS::ApiGatewayV2::Stage",
            "AWS::ApiGatewayV2::Api",
            "AWS::CodePipeline::Pipeline",
            "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
            "AWS::ServiceCatalog::CloudFormationProduct",
            "AWS::ServiceCatalog::Portfolio",
            "AWS::SQS::Queue",
            "AWS::KMS::Key",
            "AWS::QLDB::Ledger",
            "AWS::SecretsManager::Secret",
            "AWS::SNS::Topic",
            "AWS::SSM::FileData",
        ],
        resourceIds: List[str] = None,
        resourceName: str = None,
        limit: int = None,
        includeDeletedResources: bool = None,
        nextToken: str = None,
    ) -> ListDiscoveredResourcesResponseTypeDef:
        """
        [Client.list_discovered_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.list_discovered_resources)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, Limit: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.list_tags_for_resource)
        """

    def put_aggregation_authorization(
        self, AuthorizedAccountId: str, AuthorizedAwsRegion: str, Tags: List["TagTypeDef"] = None
    ) -> PutAggregationAuthorizationResponseTypeDef:
        """
        [Client.put_aggregation_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_aggregation_authorization)
        """

    def put_config_rule(
        self, ConfigRule: "ConfigRuleTypeDef", Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        [Client.put_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_config_rule)
        """

    def put_configuration_aggregator(
        self,
        ConfigurationAggregatorName: str,
        AccountAggregationSources: List["AccountAggregationSourceTypeDef"] = None,
        OrganizationAggregationSource: "OrganizationAggregationSourceTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> PutConfigurationAggregatorResponseTypeDef:
        """
        [Client.put_configuration_aggregator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_configuration_aggregator)
        """

    def put_configuration_recorder(
        self, ConfigurationRecorder: "ConfigurationRecorderTypeDef"
    ) -> None:
        """
        [Client.put_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_configuration_recorder)
        """

    def put_conformance_pack(
        self,
        ConformancePackName: str,
        TemplateS3Uri: str = None,
        TemplateBody: str = None,
        DeliveryS3Bucket: str = None,
        DeliveryS3KeyPrefix: str = None,
        ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"] = None,
    ) -> PutConformancePackResponseTypeDef:
        """
        [Client.put_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_conformance_pack)
        """

    def put_delivery_channel(self, DeliveryChannel: "DeliveryChannelTypeDef") -> None:
        """
        [Client.put_delivery_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_delivery_channel)
        """

    def put_evaluations(
        self, ResultToken: str, Evaluations: List["EvaluationTypeDef"] = None, TestMode: bool = None
    ) -> PutEvaluationsResponseTypeDef:
        """
        [Client.put_evaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_evaluations)
        """

    def put_organization_config_rule(
        self,
        OrganizationConfigRuleName: str,
        OrganizationManagedRuleMetadata: "OrganizationManagedRuleMetadataTypeDef" = None,
        OrganizationCustomRuleMetadata: "OrganizationCustomRuleMetadataTypeDef" = None,
        ExcludedAccounts: List[str] = None,
    ) -> PutOrganizationConfigRuleResponseTypeDef:
        """
        [Client.put_organization_config_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_organization_config_rule)
        """

    def put_organization_conformance_pack(
        self,
        OrganizationConformancePackName: str,
        TemplateS3Uri: str = None,
        TemplateBody: str = None,
        DeliveryS3Bucket: str = None,
        DeliveryS3KeyPrefix: str = None,
        ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"] = None,
        ExcludedAccounts: List[str] = None,
    ) -> PutOrganizationConformancePackResponseTypeDef:
        """
        [Client.put_organization_conformance_pack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_organization_conformance_pack)
        """

    def put_remediation_configurations(
        self, RemediationConfigurations: List["RemediationConfigurationTypeDef"]
    ) -> PutRemediationConfigurationsResponseTypeDef:
        """
        [Client.put_remediation_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_remediation_configurations)
        """

    def put_remediation_exceptions(
        self,
        ConfigRuleName: str,
        ResourceKeys: List["RemediationExceptionResourceKeyTypeDef"],
        Message: str = None,
        ExpirationTime: datetime = None,
    ) -> PutRemediationExceptionsResponseTypeDef:
        """
        [Client.put_remediation_exceptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_remediation_exceptions)
        """

    def put_resource_config(
        self,
        ResourceType: str,
        SchemaVersionId: str,
        ResourceId: str,
        Configuration: str,
        ResourceName: str = None,
        Tags: Dict[str, str] = None,
    ) -> None:
        """
        [Client.put_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_resource_config)
        """

    def put_retention_configuration(
        self, RetentionPeriodInDays: int
    ) -> PutRetentionConfigurationResponseTypeDef:
        """
        [Client.put_retention_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.put_retention_configuration)
        """

    def select_aggregate_resource_config(
        self,
        Expression: str,
        ConfigurationAggregatorName: str,
        Limit: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> SelectAggregateResourceConfigResponseTypeDef:
        """
        [Client.select_aggregate_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.select_aggregate_resource_config)
        """

    def select_resource_config(
        self, Expression: str, Limit: int = None, NextToken: str = None
    ) -> SelectResourceConfigResponseTypeDef:
        """
        [Client.select_resource_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.select_resource_config)
        """

    def start_config_rules_evaluation(self, ConfigRuleNames: List[str] = None) -> Dict[str, Any]:
        """
        [Client.start_config_rules_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.start_config_rules_evaluation)
        """

    def start_configuration_recorder(self, ConfigurationRecorderName: str) -> None:
        """
        [Client.start_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.start_configuration_recorder)
        """

    def start_remediation_execution(
        self, ConfigRuleName: str, ResourceKeys: List["ResourceKeyTypeDef"]
    ) -> StartRemediationExecutionResponseTypeDef:
        """
        [Client.start_remediation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.start_remediation_execution)
        """

    def stop_configuration_recorder(self, ConfigurationRecorderName: str) -> None:
        """
        [Client.stop_configuration_recorder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.stop_configuration_recorder)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Client.untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aggregate_compliance_by_config_rules"]
    ) -> DescribeAggregateComplianceByConfigRulesPaginator:
        """
        [Paginator.DescribeAggregateComplianceByConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeAggregateComplianceByConfigRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aggregation_authorizations"]
    ) -> DescribeAggregationAuthorizationsPaginator:
        """
        [Paginator.DescribeAggregationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeAggregationAuthorizations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compliance_by_config_rule"]
    ) -> DescribeComplianceByConfigRulePaginator:
        """
        [Paginator.DescribeComplianceByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByConfigRule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_compliance_by_resource"]
    ) -> DescribeComplianceByResourcePaginator:
        """
        [Paginator.DescribeComplianceByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeComplianceByResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_config_rule_evaluation_status"]
    ) -> DescribeConfigRuleEvaluationStatusPaginator:
        """
        [Paginator.DescribeConfigRuleEvaluationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigRuleEvaluationStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_config_rules"]
    ) -> DescribeConfigRulesPaginator:
        """
        [Paginator.DescribeConfigRules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigRules)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_aggregator_sources_status"]
    ) -> DescribeConfigurationAggregatorSourcesStatusPaginator:
        """
        [Paginator.DescribeConfigurationAggregatorSourcesStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregatorSourcesStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_configuration_aggregators"]
    ) -> DescribeConfigurationAggregatorsPaginator:
        """
        [Paginator.DescribeConfigurationAggregators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeConfigurationAggregators)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_aggregation_requests"]
    ) -> DescribePendingAggregationRequestsPaginator:
        """
        [Paginator.DescribePendingAggregationRequests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribePendingAggregationRequests)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_remediation_execution_status"]
    ) -> DescribeRemediationExecutionStatusPaginator:
        """
        [Paginator.DescribeRemediationExecutionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeRemediationExecutionStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_retention_configurations"]
    ) -> DescribeRetentionConfigurationsPaginator:
        """
        [Paginator.DescribeRetentionConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.DescribeRetentionConfigurations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_aggregate_compliance_details_by_config_rule"]
    ) -> GetAggregateComplianceDetailsByConfigRulePaginator:
        """
        [Paginator.GetAggregateComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetAggregateComplianceDetailsByConfigRule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_details_by_config_rule"]
    ) -> GetComplianceDetailsByConfigRulePaginator:
        """
        [Paginator.GetComplianceDetailsByConfigRule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByConfigRule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_compliance_details_by_resource"]
    ) -> GetComplianceDetailsByResourcePaginator:
        """
        [Paginator.GetComplianceDetailsByResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetComplianceDetailsByResource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_config_history"]
    ) -> GetResourceConfigHistoryPaginator:
        """
        [Paginator.GetResourceConfigHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.GetResourceConfigHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aggregate_discovered_resources"]
    ) -> ListAggregateDiscoveredResourcesPaginator:
        """
        [Paginator.ListAggregateDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.ListAggregateDiscoveredResources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discovered_resources"]
    ) -> ListDiscoveredResourcesPaginator:
        """
        [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/config.html#ConfigService.Paginator.ListDiscoveredResources)
        """
