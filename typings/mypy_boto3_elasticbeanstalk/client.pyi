# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for elasticbeanstalk service client

Usage::

    ```python
    import boto3
    from mypy_boto3_elasticbeanstalk import ElasticBeanstalkClient

    client: ElasticBeanstalkClient = boto3.client("elasticbeanstalk")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_elasticbeanstalk.paginator import (
    DescribeApplicationVersionsPaginator,
    DescribeEnvironmentManagedActionHistoryPaginator,
    DescribeEnvironmentsPaginator,
    DescribeEventsPaginator,
    ListPlatformVersionsPaginator,
)
from mypy_boto3_elasticbeanstalk.type_defs import (
    ApplicationDescriptionMessageTypeDef,
    ApplicationDescriptionsMessageTypeDef,
    ApplicationResourceLifecycleConfigTypeDef,
    ApplicationResourceLifecycleDescriptionMessageTypeDef,
    ApplicationVersionDescriptionMessageTypeDef,
    ApplicationVersionDescriptionsMessageTypeDef,
    ApplyEnvironmentManagedActionResultTypeDef,
    BuildConfigurationTypeDef,
    CheckDNSAvailabilityResultMessageTypeDef,
    ConfigurationOptionsDescriptionTypeDef,
    ConfigurationOptionSettingTypeDef,
    ConfigurationSettingsDescriptionsTypeDef,
    ConfigurationSettingsDescriptionTypeDef,
    ConfigurationSettingsValidationMessagesTypeDef,
    CreatePlatformVersionResultTypeDef,
    CreateStorageLocationResultMessageTypeDef,
    DeletePlatformVersionResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeEnvironmentHealthResultTypeDef,
    DescribeEnvironmentManagedActionHistoryResultTypeDef,
    DescribeEnvironmentManagedActionsResultTypeDef,
    DescribeInstancesHealthResultTypeDef,
    DescribePlatformVersionResultTypeDef,
    EnvironmentDescriptionsMessageTypeDef,
    EnvironmentDescriptionTypeDef,
    EnvironmentResourceDescriptionsMessageTypeDef,
    EnvironmentTierTypeDef,
    EventDescriptionsMessageTypeDef,
    ListAvailableSolutionStacksResultMessageTypeDef,
    ListPlatformBranchesResultTypeDef,
    ListPlatformVersionsResultTypeDef,
    OptionSpecificationTypeDef,
    PlatformFilterTypeDef,
    ResourceTagsDescriptionMessageTypeDef,
    RetrieveEnvironmentInfoResultMessageTypeDef,
    S3LocationTypeDef,
    SearchFilterTypeDef,
    SourceBuildInformationTypeDef,
    SourceConfigurationTypeDef,
    TagTypeDef,
)
from mypy_boto3_elasticbeanstalk.waiter import (
    EnvironmentExistsWaiter,
    EnvironmentTerminatedWaiter,
    EnvironmentUpdatedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticBeanstalkClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    CodeBuildNotInServiceRegionException: Type[Boto3ClientError]
    ElasticBeanstalkServiceException: Type[Boto3ClientError]
    InsufficientPrivilegesException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    ManagedActionInvalidStateException: Type[Boto3ClientError]
    OperationInProgressException: Type[Boto3ClientError]
    PlatformVersionStillReferencedException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ResourceTypeNotSupportedException: Type[Boto3ClientError]
    S3LocationNotInServiceRegionException: Type[Boto3ClientError]
    S3SubscriptionRequiredException: Type[Boto3ClientError]
    SourceBundleDeletionException: Type[Boto3ClientError]
    TooManyApplicationVersionsException: Type[Boto3ClientError]
    TooManyApplicationsException: Type[Boto3ClientError]
    TooManyBucketsException: Type[Boto3ClientError]
    TooManyConfigurationTemplatesException: Type[Boto3ClientError]
    TooManyEnvironmentsException: Type[Boto3ClientError]
    TooManyPlatformsException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]


class ElasticBeanstalkClient:
    """
    [ElasticBeanstalk.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client)
    """

    exceptions: Exceptions

    def abort_environment_update(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> None:
        """
        [Client.abort_environment_update documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.abort_environment_update)
        """

    def apply_environment_managed_action(
        self, ActionId: str, EnvironmentName: str = None, EnvironmentId: str = None
    ) -> ApplyEnvironmentManagedActionResultTypeDef:
        """
        [Client.apply_environment_managed_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.apply_environment_managed_action)
        """

    def associate_environment_operations_role(
        self, EnvironmentName: str, OperationsRole: str
    ) -> None:
        """
        [Client.associate_environment_operations_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.associate_environment_operations_role)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.can_paginate)
        """

    def check_dns_availability(self, CNAMEPrefix: str) -> CheckDNSAvailabilityResultMessageTypeDef:
        """
        [Client.check_dns_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.check_dns_availability)
        """

    def compose_environments(
        self, ApplicationName: str = None, GroupName: str = None, VersionLabels: List[str] = None
    ) -> EnvironmentDescriptionsMessageTypeDef:
        """
        [Client.compose_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.compose_environments)
        """

    def create_application(
        self,
        ApplicationName: str,
        Description: str = None,
        ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ApplicationDescriptionMessageTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application)
        """

    def create_application_version(
        self,
        ApplicationName: str,
        VersionLabel: str,
        Description: str = None,
        SourceBuildInformation: "SourceBuildInformationTypeDef" = None,
        SourceBundle: "S3LocationTypeDef" = None,
        BuildConfiguration: BuildConfigurationTypeDef = None,
        AutoCreateApplication: bool = None,
        Process: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ApplicationVersionDescriptionMessageTypeDef:
        """
        [Client.create_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_application_version)
        """

    def create_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        SourceConfiguration: SourceConfigurationTypeDef = None,
        EnvironmentId: str = None,
        Description: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> "ConfigurationSettingsDescriptionTypeDef":
        """
        [Client.create_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_configuration_template)
        """

    def create_environment(
        self,
        ApplicationName: str,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        CNAMEPrefix: str = None,
        Tier: "EnvironmentTierTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        OptionsToRemove: List[OptionSpecificationTypeDef] = None,
        OperationsRole: str = None,
    ) -> "EnvironmentDescriptionTypeDef":
        """
        [Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_environment)
        """

    def create_platform_version(
        self,
        PlatformName: str,
        PlatformVersion: str,
        PlatformDefinitionBundle: "S3LocationTypeDef",
        EnvironmentName: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePlatformVersionResultTypeDef:
        """
        [Client.create_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_platform_version)
        """

    def create_storage_location(self) -> CreateStorageLocationResultMessageTypeDef:
        """
        [Client.create_storage_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.create_storage_location)
        """

    def delete_application(self, ApplicationName: str, TerminateEnvByForce: bool = None) -> None:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application)
        """

    def delete_application_version(
        self, ApplicationName: str, VersionLabel: str, DeleteSourceBundle: bool = None
    ) -> None:
        """
        [Client.delete_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_application_version)
        """

    def delete_configuration_template(self, ApplicationName: str, TemplateName: str) -> None:
        """
        [Client.delete_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_configuration_template)
        """

    def delete_environment_configuration(self, ApplicationName: str, EnvironmentName: str) -> None:
        """
        [Client.delete_environment_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_environment_configuration)
        """

    def delete_platform_version(
        self, PlatformArn: str = None
    ) -> DeletePlatformVersionResultTypeDef:
        """
        [Client.delete_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.delete_platform_version)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResultTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_account_attributes)
        """

    def describe_application_versions(
        self,
        ApplicationName: str = None,
        VersionLabels: List[str] = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ApplicationVersionDescriptionsMessageTypeDef:
        """
        [Client.describe_application_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_application_versions)
        """

    def describe_applications(
        self, ApplicationNames: List[str] = None
    ) -> ApplicationDescriptionsMessageTypeDef:
        """
        [Client.describe_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_applications)
        """

    def describe_configuration_options(
        self,
        ApplicationName: str = None,
        TemplateName: str = None,
        EnvironmentName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        Options: List[OptionSpecificationTypeDef] = None,
    ) -> ConfigurationOptionsDescriptionTypeDef:
        """
        [Client.describe_configuration_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_options)
        """

    def describe_configuration_settings(
        self, ApplicationName: str, TemplateName: str = None, EnvironmentName: str = None
    ) -> ConfigurationSettingsDescriptionsTypeDef:
        """
        [Client.describe_configuration_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_configuration_settings)
        """

    def describe_environment_health(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[
            Literal[
                "Status",
                "Color",
                "Causes",
                "ApplicationMetrics",
                "InstancesHealth",
                "All",
                "HealthStatus",
                "RefreshedAt",
            ]
        ] = None,
    ) -> DescribeEnvironmentHealthResultTypeDef:
        """
        [Client.describe_environment_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_health)
        """

    def describe_environment_managed_action_history(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> DescribeEnvironmentManagedActionHistoryResultTypeDef:
        """
        [Client.describe_environment_managed_action_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_action_history)
        """

    def describe_environment_managed_actions(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        Status: Literal["Scheduled", "Pending", "Running", "Unknown"] = None,
    ) -> DescribeEnvironmentManagedActionsResultTypeDef:
        """
        [Client.describe_environment_managed_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_managed_actions)
        """

    def describe_environment_resources(
        self, EnvironmentId: str = None, EnvironmentName: str = None
    ) -> EnvironmentResourceDescriptionsMessageTypeDef:
        """
        [Client.describe_environment_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environment_resources)
        """

    def describe_environments(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        EnvironmentIds: List[str] = None,
        EnvironmentNames: List[str] = None,
        IncludeDeleted: bool = None,
        IncludedDeletedBackTo: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> EnvironmentDescriptionsMessageTypeDef:
        """
        [Client.describe_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_environments)
        """

    def describe_events(
        self,
        ApplicationName: str = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        PlatformArn: str = None,
        RequestId: str = None,
        Severity: Literal["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> EventDescriptionsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_events)
        """

    def describe_instances_health(
        self,
        EnvironmentName: str = None,
        EnvironmentId: str = None,
        AttributeNames: List[
            Literal[
                "HealthStatus",
                "Color",
                "Causes",
                "ApplicationMetrics",
                "RefreshedAt",
                "LaunchedAt",
                "System",
                "Deployment",
                "AvailabilityZone",
                "InstanceType",
                "All",
            ]
        ] = None,
        NextToken: str = None,
    ) -> DescribeInstancesHealthResultTypeDef:
        """
        [Client.describe_instances_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_instances_health)
        """

    def describe_platform_version(
        self, PlatformArn: str = None
    ) -> DescribePlatformVersionResultTypeDef:
        """
        [Client.describe_platform_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.describe_platform_version)
        """

    def disassociate_environment_operations_role(self, EnvironmentName: str) -> None:
        """
        [Client.disassociate_environment_operations_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.disassociate_environment_operations_role)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.generate_presigned_url)
        """

    def list_available_solution_stacks(self) -> ListAvailableSolutionStacksResultMessageTypeDef:
        """
        [Client.list_available_solution_stacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_available_solution_stacks)
        """

    def list_platform_branches(
        self,
        Filters: List[SearchFilterTypeDef] = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ListPlatformBranchesResultTypeDef:
        """
        [Client.list_platform_branches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_branches)
        """

    def list_platform_versions(
        self,
        Filters: List[PlatformFilterTypeDef] = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> ListPlatformVersionsResultTypeDef:
        """
        [Client.list_platform_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_platform_versions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ResourceTagsDescriptionMessageTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.list_tags_for_resource)
        """

    def rebuild_environment(self, EnvironmentId: str = None, EnvironmentName: str = None) -> None:
        """
        [Client.rebuild_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.rebuild_environment)
        """

    def request_environment_info(
        self,
        InfoType: Literal["tail", "bundle"],
        EnvironmentId: str = None,
        EnvironmentName: str = None,
    ) -> None:
        """
        [Client.request_environment_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.request_environment_info)
        """

    def restart_app_server(self, EnvironmentId: str = None, EnvironmentName: str = None) -> None:
        """
        [Client.restart_app_server documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.restart_app_server)
        """

    def retrieve_environment_info(
        self,
        InfoType: Literal["tail", "bundle"],
        EnvironmentId: str = None,
        EnvironmentName: str = None,
    ) -> RetrieveEnvironmentInfoResultMessageTypeDef:
        """
        [Client.retrieve_environment_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.retrieve_environment_info)
        """

    def swap_environment_cnames(
        self,
        SourceEnvironmentId: str = None,
        SourceEnvironmentName: str = None,
        DestinationEnvironmentId: str = None,
        DestinationEnvironmentName: str = None,
    ) -> None:
        """
        [Client.swap_environment_cnames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.swap_environment_cnames)
        """

    def terminate_environment(
        self,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        TerminateResources: bool = None,
        ForceTerminate: bool = None,
    ) -> "EnvironmentDescriptionTypeDef":
        """
        [Client.terminate_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.terminate_environment)
        """

    def update_application(
        self, ApplicationName: str, Description: str = None
    ) -> ApplicationDescriptionMessageTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application)
        """

    def update_application_resource_lifecycle(
        self,
        ApplicationName: str,
        ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef",
    ) -> ApplicationResourceLifecycleDescriptionMessageTypeDef:
        """
        [Client.update_application_resource_lifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_resource_lifecycle)
        """

    def update_application_version(
        self, ApplicationName: str, VersionLabel: str, Description: str = None
    ) -> ApplicationVersionDescriptionMessageTypeDef:
        """
        [Client.update_application_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_application_version)
        """

    def update_configuration_template(
        self,
        ApplicationName: str,
        TemplateName: str,
        Description: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        OptionsToRemove: List[OptionSpecificationTypeDef] = None,
    ) -> "ConfigurationSettingsDescriptionTypeDef":
        """
        [Client.update_configuration_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_configuration_template)
        """

    def update_environment(
        self,
        ApplicationName: str = None,
        EnvironmentId: str = None,
        EnvironmentName: str = None,
        GroupName: str = None,
        Description: str = None,
        Tier: "EnvironmentTierTypeDef" = None,
        VersionLabel: str = None,
        TemplateName: str = None,
        SolutionStackName: str = None,
        PlatformArn: str = None,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"] = None,
        OptionsToRemove: List[OptionSpecificationTypeDef] = None,
    ) -> "EnvironmentDescriptionTypeDef":
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_environment)
        """

    def update_tags_for_resource(
        self, ResourceArn: str, TagsToAdd: List["TagTypeDef"] = None, TagsToRemove: List[str] = None
    ) -> None:
        """
        [Client.update_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.update_tags_for_resource)
        """

    def validate_configuration_settings(
        self,
        ApplicationName: str,
        OptionSettings: List["ConfigurationOptionSettingTypeDef"],
        TemplateName: str = None,
        EnvironmentName: str = None,
    ) -> ConfigurationSettingsValidationMessagesTypeDef:
        """
        [Client.validate_configuration_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Client.validate_configuration_settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_application_versions"]
    ) -> DescribeApplicationVersionsPaginator:
        """
        [Paginator.DescribeApplicationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeApplicationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environment_managed_action_history"]
    ) -> DescribeEnvironmentManagedActionHistoryPaginator:
        """
        [Paginator.DescribeEnvironmentManagedActionHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironmentManagedActionHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_environments"]
    ) -> DescribeEnvironmentsPaginator:
        """
        [Paginator.DescribeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEnvironments)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_platform_versions"]
    ) -> ListPlatformVersionsPaginator:
        """
        [Paginator.ListPlatformVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Paginator.ListPlatformVersions)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["environment_exists"]) -> EnvironmentExistsWaiter:
        """
        [Waiter.EnvironmentExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentExists)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["environment_terminated"]
    ) -> EnvironmentTerminatedWaiter:
        """
        [Waiter.EnvironmentTerminated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentTerminated)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["environment_updated"]) -> EnvironmentUpdatedWaiter:
        """
        [Waiter.EnvironmentUpdated documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elasticbeanstalk.html#ElasticBeanstalk.Waiter.EnvironmentUpdated)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
