"""
Type annotations for sagemaker service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker import SageMakerClient

    client: SageMakerClient = boto3.client("sagemaker")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ActionStatusType,
    AlgorithmSortByType,
    AppImageConfigSortKeyType,
    AppNetworkAccessTypeType,
    AppSecurityGroupManagementType,
    AppTypeType,
    AssociationEdgeTypeType,
    AuthModeType,
    AutoMLJobStatusType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    BatchStrategyType,
    CandidateSortByType,
    CandidateStatusType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CompilationJobStatusType,
    CrossAccountFilterOptionType,
    DirectInternetAccessType,
    DirectionType,
    EdgePackagingJobStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionStatusType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    HubContentSortByType,
    HubContentTypeType,
    HubSortByType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    ImageSortByType,
    ImageSortOrderType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    InferenceExperimentStatusType,
    InferenceExperimentStopDesiredStateType,
    InstanceTypeType,
    JobTypeType,
    LabelingJobStatusType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgeDeploymentPlansSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    ModelApprovalStatusType,
    ModelCardExportJobSortByType,
    ModelCardExportJobSortOrderType,
    ModelCardExportJobStatusType,
    ModelCardSortByType,
    ModelCardSortOrderType,
    ModelCardStatusType,
    ModelPackageGroupSortByType,
    ModelPackageSortByType,
    ModelPackageTypeType,
    ModelSortKeyType,
    ModelVariantActionType,
    MonitoringAlertHistorySortKeyType,
    MonitoringAlertStatusType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    OfflineStoreStatusValueType,
    OrderKeyType,
    ProblemTypeType,
    ProcessingJobStatusType,
    ProcessorType,
    ProjectSortByType,
    ProjectSortOrderType,
    RecommendationJobStatusType,
    RecommendationJobTypeType,
    ResourceCatalogSortOrderType,
    ResourceTypeType,
    RootAccessType,
    ScheduleStatusType,
    SearchSortOrderType,
    SkipModelValidationType,
    SortActionsByType,
    SortAssociationsByType,
    SortByType,
    SortContextsByType,
    SortExperimentsByType,
    SortInferenceExperimentsByType,
    SortLineageGroupsByType,
    SortOrderType,
    SortPipelineExecutionsByType,
    SortPipelinesByType,
    SortTrialComponentsByType,
    SortTrialsByType,
    SpaceSortKeyType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TransformJobStatusType,
    UserProfileSortKeyType,
    VendorGuidanceType,
    WarmPoolResourceStatusType,
)
from .paginator import (
    ListActionsPaginator,
    ListAlgorithmsPaginator,
    ListAliasesPaginator,
    ListAppImageConfigsPaginator,
    ListAppsPaginator,
    ListArtifactsPaginator,
    ListAssociationsPaginator,
    ListAutoMLJobsPaginator,
    ListCandidatesForAutoMLJobPaginator,
    ListCodeRepositoriesPaginator,
    ListCompilationJobsPaginator,
    ListContextsPaginator,
    ListDataQualityJobDefinitionsPaginator,
    ListDeviceFleetsPaginator,
    ListDevicesPaginator,
    ListDomainsPaginator,
    ListEdgeDeploymentPlansPaginator,
    ListEdgePackagingJobsPaginator,
    ListEndpointConfigsPaginator,
    ListEndpointsPaginator,
    ListExperimentsPaginator,
    ListFeatureGroupsPaginator,
    ListFlowDefinitionsPaginator,
    ListHumanTaskUisPaginator,
    ListHyperParameterTuningJobsPaginator,
    ListImagesPaginator,
    ListImageVersionsPaginator,
    ListInferenceExperimentsPaginator,
    ListInferenceRecommendationsJobsPaginator,
    ListInferenceRecommendationsJobStepsPaginator,
    ListLabelingJobsForWorkteamPaginator,
    ListLabelingJobsPaginator,
    ListLineageGroupsPaginator,
    ListModelBiasJobDefinitionsPaginator,
    ListModelCardExportJobsPaginator,
    ListModelCardsPaginator,
    ListModelCardVersionsPaginator,
    ListModelExplainabilityJobDefinitionsPaginator,
    ListModelMetadataPaginator,
    ListModelPackageGroupsPaginator,
    ListModelPackagesPaginator,
    ListModelQualityJobDefinitionsPaginator,
    ListModelsPaginator,
    ListMonitoringAlertHistoryPaginator,
    ListMonitoringAlertsPaginator,
    ListMonitoringExecutionsPaginator,
    ListMonitoringSchedulesPaginator,
    ListNotebookInstanceLifecycleConfigsPaginator,
    ListNotebookInstancesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelineExecutionStepsPaginator,
    ListPipelineParametersForExecutionPaginator,
    ListPipelinesPaginator,
    ListProcessingJobsPaginator,
    ListResourceCatalogsPaginator,
    ListSpacesPaginator,
    ListStageDevicesPaginator,
    ListStudioLifecycleConfigsPaginator,
    ListSubscribedWorkteamsPaginator,
    ListTagsPaginator,
    ListTrainingJobsForHyperParameterTuningJobPaginator,
    ListTrainingJobsPaginator,
    ListTransformJobsPaginator,
    ListTrialComponentsPaginator,
    ListTrialsPaginator,
    ListUserProfilesPaginator,
    ListWorkforcesPaginator,
    ListWorkteamsPaginator,
    SearchPaginator,
)
from .type_defs import (
    ActionSourceTypeDef,
    AddAssociationResponseTypeDef,
    AdditionalInferenceSpecificationDefinitionTypeDef,
    AddTagsOutputTypeDef,
    AlgorithmSpecificationTypeDef,
    AlgorithmValidationSpecificationTypeDef,
    AppSpecificationTypeDef,
    ArtifactSourceTypeDef,
    AssociateTrialComponentResponseTypeDef,
    AsyncInferenceConfigTypeDef,
    AutoMLChannelTypeDef,
    AutoMLDataSplitConfigTypeDef,
    AutoMLJobChannelTypeDef,
    AutoMLJobConfigTypeDef,
    AutoMLJobObjectiveTypeDef,
    AutoMLOutputDataConfigTypeDef,
    AutoMLProblemTypeConfigTypeDef,
    AutoMLSecurityConfigTypeDef,
    AutotuneTypeDef,
    BatchDataCaptureConfigTypeDef,
    BatchDescribeModelPackageOutputTypeDef,
    ChannelTypeDef,
    CheckpointConfigTypeDef,
    CognitoConfigTypeDef,
    ContainerDefinitionTypeDef,
    ContextSourceTypeDef,
    CreateActionResponseTypeDef,
    CreateAlgorithmOutputTypeDef,
    CreateAppImageConfigResponseTypeDef,
    CreateAppResponseTypeDef,
    CreateArtifactResponseTypeDef,
    CreateAutoMLJobResponseTypeDef,
    CreateAutoMLJobV2ResponseTypeDef,
    CreateCodeRepositoryOutputTypeDef,
    CreateCompilationJobResponseTypeDef,
    CreateContextResponseTypeDef,
    CreateDataQualityJobDefinitionResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateEdgeDeploymentPlanResponseTypeDef,
    CreateEndpointConfigOutputTypeDef,
    CreateEndpointOutputTypeDef,
    CreateExperimentResponseTypeDef,
    CreateFeatureGroupResponseTypeDef,
    CreateFlowDefinitionResponseTypeDef,
    CreateHubResponseTypeDef,
    CreateHumanTaskUiResponseTypeDef,
    CreateHyperParameterTuningJobResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateImageVersionResponseTypeDef,
    CreateInferenceExperimentResponseTypeDef,
    CreateInferenceRecommendationsJobResponseTypeDef,
    CreateLabelingJobResponseTypeDef,
    CreateModelBiasJobDefinitionResponseTypeDef,
    CreateModelCardExportJobResponseTypeDef,
    CreateModelCardResponseTypeDef,
    CreateModelExplainabilityJobDefinitionResponseTypeDef,
    CreateModelOutputTypeDef,
    CreateModelPackageGroupOutputTypeDef,
    CreateModelPackageOutputTypeDef,
    CreateModelQualityJobDefinitionResponseTypeDef,
    CreateMonitoringScheduleResponseTypeDef,
    CreateNotebookInstanceLifecycleConfigOutputTypeDef,
    CreateNotebookInstanceOutputTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresignedDomainUrlResponseTypeDef,
    CreatePresignedNotebookInstanceUrlOutputTypeDef,
    CreateProcessingJobResponseTypeDef,
    CreateProjectOutputTypeDef,
    CreateSpaceResponseTypeDef,
    CreateStudioLifecycleConfigResponseTypeDef,
    CreateTrainingJobResponseTypeDef,
    CreateTransformJobResponseTypeDef,
    CreateTrialComponentResponseTypeDef,
    CreateTrialResponseTypeDef,
    CreateUserProfileResponseTypeDef,
    CreateWorkforceResponseTypeDef,
    CreateWorkteamResponseTypeDef,
    DataCaptureConfigTypeDef,
    DataProcessingTypeDef,
    DataQualityAppSpecificationTypeDef,
    DataQualityBaselineConfigTypeDef,
    DataQualityJobInputTypeDef,
    DebugHookConfigTypeDef,
    DebugRuleConfigurationTypeDef,
    DefaultSpaceSettingsTypeDef,
    DeleteActionResponseTypeDef,
    DeleteArtifactResponseTypeDef,
    DeleteAssociationResponseTypeDef,
    DeleteContextResponseTypeDef,
    DeleteExperimentResponseTypeDef,
    DeleteInferenceExperimentResponseTypeDef,
    DeletePipelineResponseTypeDef,
    DeleteTrialComponentResponseTypeDef,
    DeleteTrialResponseTypeDef,
    DeleteWorkteamResponseTypeDef,
    DeploymentConfigTypeDef,
    DeploymentStageTypeDef,
    DescribeActionResponseTypeDef,
    DescribeAlgorithmOutputTypeDef,
    DescribeAppImageConfigResponseTypeDef,
    DescribeAppResponseTypeDef,
    DescribeArtifactResponseTypeDef,
    DescribeAutoMLJobResponseTypeDef,
    DescribeAutoMLJobV2ResponseTypeDef,
    DescribeCodeRepositoryOutputTypeDef,
    DescribeCompilationJobResponseTypeDef,
    DescribeContextResponseTypeDef,
    DescribeDataQualityJobDefinitionResponseTypeDef,
    DescribeDeviceFleetResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeEdgeDeploymentPlanResponseTypeDef,
    DescribeEdgePackagingJobResponseTypeDef,
    DescribeEndpointConfigOutputTypeDef,
    DescribeEndpointOutputTypeDef,
    DescribeExperimentResponseTypeDef,
    DescribeFeatureGroupResponseTypeDef,
    DescribeFeatureMetadataResponseTypeDef,
    DescribeFlowDefinitionResponseTypeDef,
    DescribeHubContentResponseTypeDef,
    DescribeHubResponseTypeDef,
    DescribeHumanTaskUiResponseTypeDef,
    DescribeHyperParameterTuningJobResponseTypeDef,
    DescribeImageResponseTypeDef,
    DescribeImageVersionResponseTypeDef,
    DescribeInferenceExperimentResponseTypeDef,
    DescribeInferenceRecommendationsJobResponseTypeDef,
    DescribeLabelingJobResponseTypeDef,
    DescribeLineageGroupResponseTypeDef,
    DescribeModelBiasJobDefinitionResponseTypeDef,
    DescribeModelCardExportJobResponseTypeDef,
    DescribeModelCardResponseTypeDef,
    DescribeModelExplainabilityJobDefinitionResponseTypeDef,
    DescribeModelOutputTypeDef,
    DescribeModelPackageGroupOutputTypeDef,
    DescribeModelPackageOutputTypeDef,
    DescribeModelQualityJobDefinitionResponseTypeDef,
    DescribeMonitoringScheduleResponseTypeDef,
    DescribeNotebookInstanceLifecycleConfigOutputTypeDef,
    DescribeNotebookInstanceOutputTypeDef,
    DescribePipelineDefinitionForExecutionResponseTypeDef,
    DescribePipelineExecutionResponseTypeDef,
    DescribePipelineResponseTypeDef,
    DescribeProcessingJobResponseTypeDef,
    DescribeProjectOutputTypeDef,
    DescribeSpaceResponseTypeDef,
    DescribeStudioLifecycleConfigResponseTypeDef,
    DescribeSubscribedWorkteamResponseTypeDef,
    DescribeTrainingJobResponseTypeDef,
    DescribeTransformJobResponseTypeDef,
    DescribeTrialComponentResponseTypeDef,
    DescribeTrialResponseTypeDef,
    DescribeUserProfileResponseTypeDef,
    DescribeWorkforceResponseTypeDef,
    DescribeWorkteamResponseTypeDef,
    DesiredWeightAndCapacityTypeDef,
    DeviceTypeDef,
    DisassociateTrialComponentResponseTypeDef,
    DomainSettingsForUpdateTypeDef,
    DomainSettingsTypeDef,
    DriftCheckBaselinesTypeDef,
    EdgeDeploymentModelConfigTypeDef,
    EdgeOutputConfigTypeDef,
    ExperimentConfigTypeDef,
    ExplainerConfigTypeDef,
    FeatureDefinitionTypeDef,
    FeatureParameterTypeDef,
    FlowDefinitionOutputConfigTypeDef,
    GetDeviceFleetReportResponseTypeDef,
    GetLineageGroupPolicyResponseTypeDef,
    GetModelPackageGroupPolicyOutputTypeDef,
    GetSagemakerServicecatalogPortfolioStatusOutputTypeDef,
    GetScalingConfigurationRecommendationResponseTypeDef,
    GetSearchSuggestionsResponseTypeDef,
    GitConfigForUpdateTypeDef,
    GitConfigTypeDef,
    HubS3StorageConfigTypeDef,
    HumanLoopActivationConfigTypeDef,
    HumanLoopConfigTypeDef,
    HumanLoopRequestSourceTypeDef,
    HumanTaskConfigTypeDef,
    HyperParameterTrainingJobDefinitionTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    HyperParameterTuningJobWarmStartConfigTypeDef,
    ImportHubContentResponseTypeDef,
    InferenceExecutionConfigTypeDef,
    InferenceExperimentDataStorageConfigTypeDef,
    InferenceExperimentScheduleTypeDef,
    InferenceSpecificationTypeDef,
    InputConfigTypeDef,
    InstanceMetadataServiceConfigurationTypeDef,
    KernelGatewayImageConfigTypeDef,
    LabelingJobAlgorithmsConfigTypeDef,
    LabelingJobInputConfigTypeDef,
    LabelingJobOutputConfigTypeDef,
    LabelingJobStoppingConditionsTypeDef,
    ListActionsResponseTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAliasesResponseTypeDef,
    ListAppImageConfigsResponseTypeDef,
    ListAppsResponseTypeDef,
    ListArtifactsResponseTypeDef,
    ListAssociationsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListContextsResponseTypeDef,
    ListDataQualityJobDefinitionsResponseTypeDef,
    ListDeviceFleetsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEdgeDeploymentPlansResponseTypeDef,
    ListEdgePackagingJobsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeatureGroupsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHubContentsResponseTypeDef,
    ListHubContentVersionsResponseTypeDef,
    ListHubsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListInferenceExperimentsResponseTypeDef,
    ListInferenceRecommendationsJobsResponseTypeDef,
    ListInferenceRecommendationsJobStepsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListLineageGroupsResponseTypeDef,
    ListModelBiasJobDefinitionsResponseTypeDef,
    ListModelCardExportJobsResponseTypeDef,
    ListModelCardsResponseTypeDef,
    ListModelCardVersionsResponseTypeDef,
    ListModelExplainabilityJobDefinitionsResponseTypeDef,
    ListModelMetadataResponseTypeDef,
    ListModelPackageGroupsOutputTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelQualityJobDefinitionsResponseTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringAlertHistoryResponseTypeDef,
    ListMonitoringAlertsResponseTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListPipelineExecutionsResponseTypeDef,
    ListPipelineExecutionStepsResponseTypeDef,
    ListPipelineParametersForExecutionResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListProjectsOutputTypeDef,
    ListResourceCatalogsResponseTypeDef,
    ListSpacesResponseTypeDef,
    ListStageDevicesResponseTypeDef,
    ListStudioLifecycleConfigsResponseTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkforcesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    MemberDefinitionTypeDef,
    MetadataPropertiesTypeDef,
    ModelBiasAppSpecificationTypeDef,
    ModelBiasBaselineConfigTypeDef,
    ModelBiasJobInputTypeDef,
    ModelCardExportOutputConfigTypeDef,
    ModelCardSecurityConfigTypeDef,
    ModelClientConfigTypeDef,
    ModelDeployConfigTypeDef,
    ModelExplainabilityAppSpecificationTypeDef,
    ModelExplainabilityBaselineConfigTypeDef,
    ModelExplainabilityJobInputTypeDef,
    ModelMetadataSearchExpressionTypeDef,
    ModelMetricsTypeDef,
    ModelPackageValidationSpecificationTypeDef,
    ModelQualityAppSpecificationTypeDef,
    ModelQualityBaselineConfigTypeDef,
    ModelQualityJobInputTypeDef,
    ModelVariantConfigTypeDef,
    MonitoringNetworkConfigTypeDef,
    MonitoringOutputConfigTypeDef,
    MonitoringResourcesTypeDef,
    MonitoringScheduleConfigTypeDef,
    MonitoringStoppingConditionTypeDef,
    NeoVpcConfigTypeDef,
    NetworkConfigTypeDef,
    NotebookInstanceLifecycleHookTypeDef,
    NotificationConfigurationTypeDef,
    OfflineStoreConfigTypeDef,
    OidcConfigTypeDef,
    OnlineStoreConfigTypeDef,
    OnlineStoreConfigUpdateTypeDef,
    OutputConfigTypeDef,
    OutputDataConfigTypeDef,
    OutputParameterTypeDef,
    ParallelismConfigurationTypeDef,
    ParameterTypeDef,
    PipelineDefinitionS3LocationTypeDef,
    ProcessingInputTypeDef,
    ProcessingOutputConfigTypeDef,
    ProcessingResourcesTypeDef,
    ProcessingStoppingConditionTypeDef,
    ProductionVariantTypeDef,
    ProfilerConfigForUpdateTypeDef,
    ProfilerConfigTypeDef,
    ProfilerRuleConfigurationTypeDef,
    PutModelPackageGroupPolicyOutputTypeDef,
    QueryFiltersTypeDef,
    QueryLineageResponseTypeDef,
    RecommendationJobInputConfigTypeDef,
    RecommendationJobOutputConfigTypeDef,
    RecommendationJobStoppingConditionsTypeDef,
    RenderableTaskTypeDef,
    RenderUiTemplateResponseTypeDef,
    ResourceConfigForUpdateTypeDef,
    ResourceConfigTypeDef,
    ResourceSpecTypeDef,
    RetentionPolicyTypeDef,
    RetryPipelineExecutionResponseTypeDef,
    RetryStrategyTypeDef,
    ScalingPolicyObjectiveTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
    SelectiveExecutionConfigTypeDef,
    SendPipelineExecutionStepFailureResponseTypeDef,
    SendPipelineExecutionStepSuccessResponseTypeDef,
    ServiceCatalogProvisioningDetailsTypeDef,
    ServiceCatalogProvisioningUpdateDetailsTypeDef,
    ShadowModeConfigTypeDef,
    SourceAlgorithmSpecificationTypeDef,
    SourceIpConfigTypeDef,
    SpaceSettingsTypeDef,
    StartInferenceExperimentResponseTypeDef,
    StartPipelineExecutionResponseTypeDef,
    StopInferenceExperimentResponseTypeDef,
    StoppingConditionTypeDef,
    StopPipelineExecutionResponseTypeDef,
    SuggestionQueryTypeDef,
    TagTypeDef,
    TensorBoardOutputConfigTypeDef,
    TrainingSpecificationTypeDef,
    TransformInputTypeDef,
    TransformOutputTypeDef,
    TransformResourcesTypeDef,
    TrialComponentArtifactTypeDef,
    TrialComponentParameterValueTypeDef,
    TrialComponentStatusTypeDef,
    UiTemplateTypeDef,
    UpdateActionResponseTypeDef,
    UpdateAppImageConfigResponseTypeDef,
    UpdateArtifactResponseTypeDef,
    UpdateCodeRepositoryOutputTypeDef,
    UpdateContextResponseTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateEndpointOutputTypeDef,
    UpdateEndpointWeightsAndCapacitiesOutputTypeDef,
    UpdateExperimentResponseTypeDef,
    UpdateFeatureGroupResponseTypeDef,
    UpdateHubResponseTypeDef,
    UpdateImageResponseTypeDef,
    UpdateImageVersionResponseTypeDef,
    UpdateInferenceExperimentResponseTypeDef,
    UpdateModelCardResponseTypeDef,
    UpdateModelPackageOutputTypeDef,
    UpdateMonitoringAlertResponseTypeDef,
    UpdateMonitoringScheduleResponseTypeDef,
    UpdatePipelineExecutionResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateSpaceResponseTypeDef,
    UpdateTrainingJobResponseTypeDef,
    UpdateTrialComponentResponseTypeDef,
    UpdateTrialResponseTypeDef,
    UpdateUserProfileResponseTypeDef,
    UpdateWorkforceResponseTypeDef,
    UpdateWorkteamResponseTypeDef,
    UserSettingsTypeDef,
    VariantPropertyTypeDef,
    VpcConfigTypeDef,
    WorkforceVpcConfigRequestTypeDef,
)
from .waiter import (
    EndpointDeletedWaiter,
    EndpointInServiceWaiter,
    ImageCreatedWaiter,
    ImageDeletedWaiter,
    ImageUpdatedWaiter,
    ImageVersionCreatedWaiter,
    ImageVersionDeletedWaiter,
    NotebookInstanceDeletedWaiter,
    NotebookInstanceInServiceWaiter,
    NotebookInstanceStoppedWaiter,
    ProcessingJobCompletedOrStoppedWaiter,
    TrainingJobCompletedOrStoppedWaiter,
    TransformJobCompletedOrStoppedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SageMakerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResourceLimitExceeded: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]

class SageMakerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerClient exceptions.
        """
    def add_association(
        self,
        *,
        SourceArn: str,
        DestinationArn: str,
        AssociationType: AssociationEdgeTypeType = None
    ) -> AddAssociationResponseTypeDef:
        """
        Creates an *association* between the source and the destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.add_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#add_association)
        """
    def add_tags(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> AddTagsOutputTypeDef:
        """
        Adds or overwrites one or more tags for the specified SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#add_tags)
        """
    def associate_trial_component(
        self, *, TrialComponentName: str, TrialName: str
    ) -> AssociateTrialComponentResponseTypeDef:
        """
        Associates a trial component with a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#associate_trial_component)
        """
    def batch_describe_model_package(
        self, *, ModelPackageArnList: List[str]
    ) -> BatchDescribeModelPackageOutputTypeDef:
        """
        This action batch describes a list of versioned model packages See also: `AWS
        API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-
        24/BatchDescribeModelPackage>`_ **Request Syntax** response =
        client.batch_describe_model_package( ModelPackageArnList=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.batch_describe_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#batch_describe_model_package)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#close)
        """
    def create_action(
        self,
        *,
        ActionName: str,
        Source: "ActionSourceTypeDef",
        ActionType: str,
        Description: str = None,
        Status: ActionStatusType = None,
        Properties: Dict[str, str] = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateActionResponseTypeDef:
        """
        Creates an *action*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_action)
        """
    def create_algorithm(
        self,
        *,
        AlgorithmName: str,
        TrainingSpecification: "TrainingSpecificationTypeDef",
        AlgorithmDescription: str = None,
        InferenceSpecification: "InferenceSpecificationTypeDef" = None,
        ValidationSpecification: "AlgorithmValidationSpecificationTypeDef" = None,
        CertifyForMarketplace: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAlgorithmOutputTypeDef:
        """
        Create a machine learning algorithm that you can use in SageMaker and list in
        the Amazon Web Services Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_algorithm)
        """
    def create_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = None,
        Tags: List["TagTypeDef"] = None,
        ResourceSpec: "ResourceSpecTypeDef" = None,
        SpaceName: str = None
    ) -> CreateAppResponseTypeDef:
        """
        Creates a running app for the specified UserProfile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_app)
        """
    def create_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        Tags: List["TagTypeDef"] = None,
        KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None
    ) -> CreateAppImageConfigResponseTypeDef:
        """
        Creates a configuration for running a SageMaker image as a KernelGateway app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_app_image_config)
        """
    def create_artifact(
        self,
        *,
        Source: "ArtifactSourceTypeDef",
        ArtifactType: str,
        ArtifactName: str = None,
        Properties: Dict[str, str] = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateArtifactResponseTypeDef:
        """
        Creates an *artifact*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_artifact)
        """
    def create_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        InputDataConfig: List["AutoMLChannelTypeDef"],
        OutputDataConfig: "AutoMLOutputDataConfigTypeDef",
        RoleArn: str,
        ProblemType: ProblemTypeType = None,
        AutoMLJobObjective: "AutoMLJobObjectiveTypeDef" = None,
        AutoMLJobConfig: "AutoMLJobConfigTypeDef" = None,
        GenerateCandidateDefinitionsOnly: bool = None,
        Tags: List["TagTypeDef"] = None,
        ModelDeployConfig: "ModelDeployConfigTypeDef" = None
    ) -> CreateAutoMLJobResponseTypeDef:
        """
        Creates an Autopilot job also referred to as Autopilot experiment or AutoML job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_auto_ml_job)
        """
    def create_auto_ml_job_v2(
        self,
        *,
        AutoMLJobName: str,
        AutoMLJobInputDataConfig: List["AutoMLJobChannelTypeDef"],
        OutputDataConfig: "AutoMLOutputDataConfigTypeDef",
        AutoMLProblemTypeConfig: "AutoMLProblemTypeConfigTypeDef",
        RoleArn: str,
        Tags: List["TagTypeDef"] = None,
        SecurityConfig: "AutoMLSecurityConfigTypeDef" = None,
        AutoMLJobObjective: "AutoMLJobObjectiveTypeDef" = None,
        ModelDeployConfig: "ModelDeployConfigTypeDef" = None,
        DataSplitConfig: "AutoMLDataSplitConfigTypeDef" = None
    ) -> CreateAutoMLJobV2ResponseTypeDef:
        """
        Creates an Autopilot job also referred to as Autopilot experiment or AutoML job
        V2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_auto_ml_job_v2)
        """
    def create_code_repository(
        self,
        *,
        CodeRepositoryName: str,
        GitConfig: "GitConfigTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateCodeRepositoryOutputTypeDef:
        """
        Creates a Git repository as a resource in your SageMaker account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_code_repository)
        """
    def create_compilation_job(
        self,
        *,
        CompilationJobName: str,
        RoleArn: str,
        OutputConfig: "OutputConfigTypeDef",
        StoppingCondition: "StoppingConditionTypeDef",
        ModelPackageVersionArn: str = None,
        InputConfig: "InputConfigTypeDef" = None,
        VpcConfig: "NeoVpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateCompilationJobResponseTypeDef:
        """
        Starts a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_compilation_job)
        """
    def create_context(
        self,
        *,
        ContextName: str,
        Source: "ContextSourceTypeDef",
        ContextType: str,
        Description: str = None,
        Properties: Dict[str, str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateContextResponseTypeDef:
        """
        Creates a *context*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_context)
        """
    def create_data_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        DataQualityAppSpecification: "DataQualityAppSpecificationTypeDef",
        DataQualityJobInput: "DataQualityJobInputTypeDef",
        DataQualityJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        DataQualityBaselineConfig: "DataQualityBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataQualityJobDefinitionResponseTypeDef:
        """
        Creates a definition for a job that monitors data quality and drift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_data_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_data_quality_job_definition)
        """
    def create_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: "EdgeOutputConfigTypeDef",
        RoleArn: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        EnableIotRoleAlias: bool = None
    ) -> None:
        """
        Creates a device fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_device_fleet)
        """
    def create_domain(
        self,
        *,
        DomainName: str,
        AuthMode: AuthModeType,
        DefaultUserSettings: "UserSettingsTypeDef",
        SubnetIds: List[str],
        VpcId: str,
        Tags: List["TagTypeDef"] = None,
        AppNetworkAccessType: AppNetworkAccessTypeType = None,
        HomeEfsFileSystemKmsKeyId: str = None,
        KmsKeyId: str = None,
        AppSecurityGroupManagement: AppSecurityGroupManagementType = None,
        DomainSettings: "DomainSettingsTypeDef" = None,
        DefaultSpaceSettings: "DefaultSpaceSettingsTypeDef" = None
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a `Domain` used by Amazon SageMaker Studio.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_domain)
        """
    def create_edge_deployment_plan(
        self,
        *,
        EdgeDeploymentPlanName: str,
        ModelConfigs: List["EdgeDeploymentModelConfigTypeDef"],
        DeviceFleetName: str,
        Stages: List["DeploymentStageTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateEdgeDeploymentPlanResponseTypeDef:
        """
        Creates an edge deployment plan, consisting of multiple stages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_edge_deployment_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_edge_deployment_plan)
        """
    def create_edge_deployment_stage(
        self, *, EdgeDeploymentPlanName: str, Stages: List["DeploymentStageTypeDef"]
    ) -> None:
        """
        Creates a new stage in an existing edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_edge_deployment_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_edge_deployment_stage)
        """
    def create_edge_packaging_job(
        self,
        *,
        EdgePackagingJobName: str,
        CompilationJobName: str,
        ModelName: str,
        ModelVersion: str,
        RoleArn: str,
        OutputConfig: "EdgeOutputConfigTypeDef",
        ResourceKey: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        Starts a SageMaker Edge Manager model packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_edge_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_edge_packaging_job)
        """
    def create_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        DeploymentConfig: "DeploymentConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateEndpointOutputTypeDef:
        """
        Creates an endpoint using the endpoint configuration specified in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_endpoint)
        """
    def create_endpoint_config(
        self,
        *,
        EndpointConfigName: str,
        ProductionVariants: List["ProductionVariantTypeDef"],
        DataCaptureConfig: "DataCaptureConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        AsyncInferenceConfig: "AsyncInferenceConfigTypeDef" = None,
        ExplainerConfig: "ExplainerConfigTypeDef" = None,
        ShadowProductionVariants: List["ProductionVariantTypeDef"] = None
    ) -> CreateEndpointConfigOutputTypeDef:
        """
        Creates an endpoint configuration that SageMaker hosting services uses to deploy
        models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_endpoint_config)
        """
    def create_experiment(
        self,
        *,
        ExperimentName: str,
        DisplayName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateExperimentResponseTypeDef:
        """
        Creates a SageMaker *experiment*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_experiment)
        """
    def create_feature_group(
        self,
        *,
        FeatureGroupName: str,
        RecordIdentifierFeatureName: str,
        EventTimeFeatureName: str,
        FeatureDefinitions: List["FeatureDefinitionTypeDef"],
        OnlineStoreConfig: "OnlineStoreConfigTypeDef" = None,
        OfflineStoreConfig: "OfflineStoreConfigTypeDef" = None,
        RoleArn: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateFeatureGroupResponseTypeDef:
        """
        Create a new `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_feature_group)
        """
    def create_flow_definition(
        self,
        *,
        FlowDefinitionName: str,
        HumanLoopConfig: "HumanLoopConfigTypeDef",
        OutputConfig: "FlowDefinitionOutputConfigTypeDef",
        RoleArn: str,
        HumanLoopRequestSource: "HumanLoopRequestSourceTypeDef" = None,
        HumanLoopActivationConfig: "HumanLoopActivationConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateFlowDefinitionResponseTypeDef:
        """
        Creates a flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_flow_definition)
        """
    def create_hub(
        self,
        *,
        HubName: str,
        HubDescription: str,
        HubDisplayName: str = None,
        HubSearchKeywords: List[str] = None,
        S3StorageConfig: "HubS3StorageConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateHubResponseTypeDef:
        """
        Create a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_hub)
        """
    def create_human_task_ui(
        self,
        *,
        HumanTaskUiName: str,
        UiTemplate: "UiTemplateTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateHumanTaskUiResponseTypeDef:
        """
        Defines the settings you will use for the human review workflow user interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_human_task_ui)
        """
    def create_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: "HyperParameterTuningJobConfigTypeDef",
        TrainingJobDefinition: "HyperParameterTrainingJobDefinitionTypeDef" = None,
        TrainingJobDefinitions: List["HyperParameterTrainingJobDefinitionTypeDef"] = None,
        WarmStartConfig: "HyperParameterTuningJobWarmStartConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        Autotune: "AutotuneTypeDef" = None
    ) -> CreateHyperParameterTuningJobResponseTypeDef:
        """
        Starts a hyperparameter tuning job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_hyper_parameter_tuning_job)
        """
    def create_image(
        self,
        *,
        ImageName: str,
        RoleArn: str,
        Description: str = None,
        DisplayName: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateImageResponseTypeDef:
        """
        Creates a custom SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_image)
        """
    def create_image_version(
        self,
        *,
        BaseImage: str,
        ClientToken: str,
        ImageName: str,
        Aliases: List[str] = None,
        VendorGuidance: VendorGuidanceType = None,
        JobType: JobTypeType = None,
        MLFramework: str = None,
        ProgrammingLang: str = None,
        Processor: ProcessorType = None,
        Horovod: bool = None,
        ReleaseNotes: str = None
    ) -> CreateImageVersionResponseTypeDef:
        """
        Creates a version of the SageMaker image specified by `ImageName`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_image_version)
        """
    def create_inference_experiment(
        self,
        *,
        Name: str,
        Type: Literal["ShadowMode"],
        RoleArn: str,
        EndpointName: str,
        ModelVariants: List["ModelVariantConfigTypeDef"],
        ShadowModeConfig: "ShadowModeConfigTypeDef",
        Schedule: "InferenceExperimentScheduleTypeDef" = None,
        Description: str = None,
        DataStorageConfig: "InferenceExperimentDataStorageConfigTypeDef" = None,
        KmsKey: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateInferenceExperimentResponseTypeDef:
        """
        Creates an inference experiment using the configurations specified in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_inference_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_inference_experiment)
        """
    def create_inference_recommendations_job(
        self,
        *,
        JobName: str,
        JobType: RecommendationJobTypeType,
        RoleArn: str,
        InputConfig: "RecommendationJobInputConfigTypeDef",
        JobDescription: str = None,
        StoppingConditions: "RecommendationJobStoppingConditionsTypeDef" = None,
        OutputConfig: "RecommendationJobOutputConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateInferenceRecommendationsJobResponseTypeDef:
        """
        Starts a recommendation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_inference_recommendations_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_inference_recommendations_job)
        """
    def create_labeling_job(
        self,
        *,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: "LabelingJobInputConfigTypeDef",
        OutputConfig: "LabelingJobOutputConfigTypeDef",
        RoleArn: str,
        HumanTaskConfig: "HumanTaskConfigTypeDef",
        LabelCategoryConfigS3Uri: str = None,
        StoppingConditions: "LabelingJobStoppingConditionsTypeDef" = None,
        LabelingJobAlgorithmsConfig: "LabelingJobAlgorithmsConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateLabelingJobResponseTypeDef:
        """
        Creates a job that uses workers to label the data objects in your input dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_labeling_job)
        """
    def create_model(
        self,
        *,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: "ContainerDefinitionTypeDef" = None,
        Containers: List["ContainerDefinitionTypeDef"] = None,
        InferenceExecutionConfig: "InferenceExecutionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        EnableNetworkIsolation: bool = None
    ) -> CreateModelOutputTypeDef:
        """
        Creates a model in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model)
        """
    def create_model_bias_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelBiasAppSpecification: "ModelBiasAppSpecificationTypeDef",
        ModelBiasJobInput: "ModelBiasJobInputTypeDef",
        ModelBiasJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        ModelBiasBaselineConfig: "ModelBiasBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateModelBiasJobDefinitionResponseTypeDef:
        """
        Creates the definition for a model bias job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_bias_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_bias_job_definition)
        """
    def create_model_card(
        self,
        *,
        ModelCardName: str,
        Content: str,
        ModelCardStatus: ModelCardStatusType,
        SecurityConfig: "ModelCardSecurityConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateModelCardResponseTypeDef:
        """
        Creates an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_card)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_card)
        """
    def create_model_card_export_job(
        self,
        *,
        ModelCardName: str,
        ModelCardExportJobName: str,
        OutputConfig: "ModelCardExportOutputConfigTypeDef",
        ModelCardVersion: int = None
    ) -> CreateModelCardExportJobResponseTypeDef:
        """
        Creates an Amazon SageMaker Model Card export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_card_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_card_export_job)
        """
    def create_model_explainability_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelExplainabilityAppSpecification: "ModelExplainabilityAppSpecificationTypeDef",
        ModelExplainabilityJobInput: "ModelExplainabilityJobInputTypeDef",
        ModelExplainabilityJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        ModelExplainabilityBaselineConfig: "ModelExplainabilityBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateModelExplainabilityJobDefinitionResponseTypeDef:
        """
        Creates the definition for a model explainability job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_explainability_job_definition)
        """
    def create_model_package(
        self,
        *,
        ModelPackageName: str = None,
        ModelPackageGroupName: str = None,
        ModelPackageDescription: str = None,
        InferenceSpecification: "InferenceSpecificationTypeDef" = None,
        ValidationSpecification: "ModelPackageValidationSpecificationTypeDef" = None,
        SourceAlgorithmSpecification: "SourceAlgorithmSpecificationTypeDef" = None,
        CertifyForMarketplace: bool = None,
        Tags: List["TagTypeDef"] = None,
        ModelApprovalStatus: ModelApprovalStatusType = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        ModelMetrics: "ModelMetricsTypeDef" = None,
        ClientToken: str = None,
        CustomerMetadataProperties: Dict[str, str] = None,
        DriftCheckBaselines: "DriftCheckBaselinesTypeDef" = None,
        Domain: str = None,
        Task: str = None,
        SamplePayloadUrl: str = None,
        AdditionalInferenceSpecifications: List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ] = None,
        SkipModelValidation: SkipModelValidationType = None
    ) -> CreateModelPackageOutputTypeDef:
        """
        Creates a model package that you can use to create SageMaker models or list on
        Amazon Web Services Marketplace, or a versioned model that is part of a model
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_package)
        """
    def create_model_package_group(
        self,
        *,
        ModelPackageGroupName: str,
        ModelPackageGroupDescription: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateModelPackageGroupOutputTypeDef:
        """
        Creates a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_package_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_package_group)
        """
    def create_model_quality_job_definition(
        self,
        *,
        JobDefinitionName: str,
        ModelQualityAppSpecification: "ModelQualityAppSpecificationTypeDef",
        ModelQualityJobInput: "ModelQualityJobInputTypeDef",
        ModelQualityJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        ModelQualityBaselineConfig: "ModelQualityBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateModelQualityJobDefinitionResponseTypeDef:
        """
        Creates a definition for a job that monitors model quality and drift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_model_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_model_quality_job_definition)
        """
    def create_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateMonitoringScheduleResponseTypeDef:
        """
        Creates a schedule that regularly starts Amazon SageMaker Processing Jobs to
        monitor the data captured for an Amazon SageMaker Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_monitoring_schedule)
        """
    def create_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: InstanceTypeType,
        RoleArn: str,
        SubnetId: str = None,
        SecurityGroupIds: List[str] = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        LifecycleConfigName: str = None,
        DirectInternetAccess: DirectInternetAccessType = None,
        VolumeSizeInGB: int = None,
        AcceleratorTypes: List[NotebookInstanceAcceleratorTypeType] = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        RootAccess: RootAccessType = None,
        PlatformIdentifier: str = None,
        InstanceMetadataServiceConfiguration: "InstanceMetadataServiceConfigurationTypeDef" = None
    ) -> CreateNotebookInstanceOutputTypeDef:
        """
        Creates an SageMaker notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_notebook_instance)
        """
    def create_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
        OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None
    ) -> CreateNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        Creates a lifecycle configuration that you can associate with a notebook
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_notebook_instance_lifecycle_config)
        """
    def create_pipeline(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        RoleArn: str,
        PipelineDisplayName: str = None,
        PipelineDefinition: str = None,
        PipelineDefinitionS3Location: "PipelineDefinitionS3LocationTypeDef" = None,
        PipelineDescription: str = None,
        Tags: List["TagTypeDef"] = None,
        ParallelismConfiguration: "ParallelismConfigurationTypeDef" = None
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates a pipeline using a JSON pipeline definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_pipeline)
        """
    def create_presigned_domain_url(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SessionExpirationDurationInSeconds: int = None,
        ExpiresInSeconds: int = None,
        SpaceName: str = None
    ) -> CreatePresignedDomainUrlResponseTypeDef:
        """
        Creates a URL for a specified UserProfile in a Domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_presigned_domain_url)
        """
    def create_presigned_notebook_instance_url(
        self, *, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None
    ) -> CreatePresignedNotebookInstanceUrlOutputTypeDef:
        """
        Returns a URL that you can use to connect to the Jupyter server from a notebook
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_presigned_notebook_instance_url)
        """
    def create_processing_job(
        self,
        *,
        ProcessingJobName: str,
        ProcessingResources: "ProcessingResourcesTypeDef",
        AppSpecification: "AppSpecificationTypeDef",
        RoleArn: str,
        ProcessingInputs: List["ProcessingInputTypeDef"] = None,
        ProcessingOutputConfig: "ProcessingOutputConfigTypeDef" = None,
        StoppingCondition: "ProcessingStoppingConditionTypeDef" = None,
        Environment: Dict[str, str] = None,
        NetworkConfig: "NetworkConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None
    ) -> CreateProcessingJobResponseTypeDef:
        """
        Creates a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_processing_job)
        """
    def create_project(
        self,
        *,
        ProjectName: str,
        ServiceCatalogProvisioningDetails: "ServiceCatalogProvisioningDetailsTypeDef",
        ProjectDescription: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateProjectOutputTypeDef:
        """
        Creates a machine learning (ML) project that can contain one or more templates
        that set up an ML pipeline from training to deploying an approved model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_project)
        """
    def create_space(
        self,
        *,
        DomainId: str,
        SpaceName: str,
        Tags: List["TagTypeDef"] = None,
        SpaceSettings: "SpaceSettingsTypeDef" = None
    ) -> CreateSpaceResponseTypeDef:
        """
        Creates a space used for real time collaboration in a Domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_space)
        """
    def create_studio_lifecycle_config(
        self,
        *,
        StudioLifecycleConfigName: str,
        StudioLifecycleConfigContent: str,
        StudioLifecycleConfigAppType: StudioLifecycleConfigAppTypeType,
        Tags: List["TagTypeDef"] = None
    ) -> CreateStudioLifecycleConfigResponseTypeDef:
        """
        Creates a new Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_studio_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_studio_lifecycle_config)
        """
    def create_training_job(
        self,
        *,
        TrainingJobName: str,
        AlgorithmSpecification: "AlgorithmSpecificationTypeDef",
        RoleArn: str,
        OutputDataConfig: "OutputDataConfigTypeDef",
        ResourceConfig: "ResourceConfigTypeDef",
        StoppingCondition: "StoppingConditionTypeDef",
        HyperParameters: Dict[str, str] = None,
        InputDataConfig: List["ChannelTypeDef"] = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        EnableNetworkIsolation: bool = None,
        EnableInterContainerTrafficEncryption: bool = None,
        EnableManagedSpotTraining: bool = None,
        CheckpointConfig: "CheckpointConfigTypeDef" = None,
        DebugHookConfig: "DebugHookConfigTypeDef" = None,
        DebugRuleConfigurations: List["DebugRuleConfigurationTypeDef"] = None,
        TensorBoardOutputConfig: "TensorBoardOutputConfigTypeDef" = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
        ProfilerConfig: "ProfilerConfigTypeDef" = None,
        ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"] = None,
        Environment: Dict[str, str] = None,
        RetryStrategy: "RetryStrategyTypeDef" = None
    ) -> CreateTrainingJobResponseTypeDef:
        """
        Starts a model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_training_job)
        """
    def create_transform_job(
        self,
        *,
        TransformJobName: str,
        ModelName: str,
        TransformInput: "TransformInputTypeDef",
        TransformOutput: "TransformOutputTypeDef",
        TransformResources: "TransformResourcesTypeDef",
        MaxConcurrentTransforms: int = None,
        ModelClientConfig: "ModelClientConfigTypeDef" = None,
        MaxPayloadInMB: int = None,
        BatchStrategy: BatchStrategyType = None,
        Environment: Dict[str, str] = None,
        DataCaptureConfig: "BatchDataCaptureConfigTypeDef" = None,
        DataProcessing: "DataProcessingTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None
    ) -> CreateTransformJobResponseTypeDef:
        """
        Starts a transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_transform_job)
        """
    def create_trial(
        self,
        *,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTrialResponseTypeDef:
        """
        Creates an SageMaker *trial*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_trial)
        """
    def create_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: "TrialComponentStatusTypeDef" = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
        InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTrialComponentResponseTypeDef:
        """
        Creates a *trial component*, which is a stage of a machine learning *trial*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_trial_component)
        """
    def create_user_profile(
        self,
        *,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str = None,
        SingleSignOnUserValue: str = None,
        Tags: List["TagTypeDef"] = None,
        UserSettings: "UserSettingsTypeDef" = None
    ) -> CreateUserProfileResponseTypeDef:
        """
        Creates a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_user_profile)
        """
    def create_workforce(
        self,
        *,
        WorkforceName: str,
        CognitoConfig: "CognitoConfigTypeDef" = None,
        OidcConfig: "OidcConfigTypeDef" = None,
        SourceIpConfig: "SourceIpConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        WorkforceVpcConfig: "WorkforceVpcConfigRequestTypeDef" = None
    ) -> CreateWorkforceResponseTypeDef:
        """
        Use this operation to create a workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_workforce)
        """
    def create_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: List["MemberDefinitionTypeDef"],
        Description: str,
        WorkforceName: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWorkteamResponseTypeDef:
        """
        Creates a new work team for labeling your data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.create_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create_workteam)
        """
    def delete_action(self, *, ActionName: str) -> DeleteActionResponseTypeDef:
        """
        Deletes an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_action)
        """
    def delete_algorithm(self, *, AlgorithmName: str) -> None:
        """
        Removes the specified algorithm from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_algorithm)
        """
    def delete_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = None,
        SpaceName: str = None
    ) -> None:
        """
        Used to stop and delete an app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_app)
        """
    def delete_app_image_config(self, *, AppImageConfigName: str) -> None:
        """
        Deletes an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_app_image_config)
        """
    def delete_artifact(
        self, *, ArtifactArn: str = None, Source: "ArtifactSourceTypeDef" = None
    ) -> DeleteArtifactResponseTypeDef:
        """
        Deletes an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_artifact)
        """
    def delete_association(
        self, *, SourceArn: str, DestinationArn: str
    ) -> DeleteAssociationResponseTypeDef:
        """
        Deletes an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_association)
        """
    def delete_code_repository(self, *, CodeRepositoryName: str) -> None:
        """
        Deletes the specified Git repository from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_code_repository)
        """
    def delete_context(self, *, ContextName: str) -> DeleteContextResponseTypeDef:
        """
        Deletes an context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_context)
        """
    def delete_data_quality_job_definition(self, *, JobDefinitionName: str) -> None:
        """
        Deletes a data quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_data_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_data_quality_job_definition)
        """
    def delete_device_fleet(self, *, DeviceFleetName: str) -> None:
        """
        Deletes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_device_fleet)
        """
    def delete_domain(
        self, *, DomainId: str, RetentionPolicy: "RetentionPolicyTypeDef" = None
    ) -> None:
        """
        Used to delete a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_domain)
        """
    def delete_edge_deployment_plan(self, *, EdgeDeploymentPlanName: str) -> None:
        """
        Deletes an edge deployment plan if (and only if) all the stages in the plan are
        inactive or there are no stages in the plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_edge_deployment_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_edge_deployment_plan)
        """
    def delete_edge_deployment_stage(self, *, EdgeDeploymentPlanName: str, StageName: str) -> None:
        """
        Delete a stage in an edge deployment plan if (and only if) the stage is
        inactive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_edge_deployment_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_edge_deployment_stage)
        """
    def delete_endpoint(self, *, EndpointName: str) -> None:
        """
        Deletes an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_endpoint)
        """
    def delete_endpoint_config(self, *, EndpointConfigName: str) -> None:
        """
        Deletes an endpoint configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_endpoint_config)
        """
    def delete_experiment(self, *, ExperimentName: str) -> DeleteExperimentResponseTypeDef:
        """
        Deletes an SageMaker experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_experiment)
        """
    def delete_feature_group(self, *, FeatureGroupName: str) -> None:
        """
        Delete the `FeatureGroup` and any data that was written to the `OnlineStore` of
        the `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_feature_group)
        """
    def delete_flow_definition(self, *, FlowDefinitionName: str) -> Dict[str, Any]:
        """
        Deletes the specified flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_flow_definition)
        """
    def delete_hub(self, *, HubName: str) -> None:
        """
        Delete a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_hub)
        """
    def delete_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        HubContentVersion: str
    ) -> None:
        """
        Delete the contents of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_hub_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_hub_content)
        """
    def delete_human_task_ui(self, *, HumanTaskUiName: str) -> Dict[str, Any]:
        """
        Use this operation to delete a human task user interface (worker task template).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_human_task_ui)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_human_task_ui)
        """
    def delete_image(self, *, ImageName: str) -> Dict[str, Any]:
        """
        Deletes a SageMaker image and all versions of the image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_image)
        """
    def delete_image_version(
        self, *, ImageName: str, Version: int = None, Alias: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a version of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_image_version)
        """
    def delete_inference_experiment(self, *, Name: str) -> DeleteInferenceExperimentResponseTypeDef:
        """
        Deletes an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_inference_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_inference_experiment)
        """
    def delete_model(self, *, ModelName: str) -> None:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model)
        """
    def delete_model_bias_job_definition(self, *, JobDefinitionName: str) -> None:
        """
        Deletes an Amazon SageMaker model bias job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_bias_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_bias_job_definition)
        """
    def delete_model_card(self, *, ModelCardName: str) -> None:
        """
        Deletes an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_card)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_card)
        """
    def delete_model_explainability_job_definition(self, *, JobDefinitionName: str) -> None:
        """
        Deletes an Amazon SageMaker model explainability job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_explainability_job_definition)
        """
    def delete_model_package(self, *, ModelPackageName: str) -> None:
        """
        Deletes a model package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_package)
        """
    def delete_model_package_group(self, *, ModelPackageGroupName: str) -> None:
        """
        Deletes the specified model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_package_group)
        """
    def delete_model_package_group_policy(self, *, ModelPackageGroupName: str) -> None:
        """
        Deletes a model group resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_package_group_policy)
        """
    def delete_model_quality_job_definition(self, *, JobDefinitionName: str) -> None:
        """
        Deletes the secified model quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_model_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_model_quality_job_definition)
        """
    def delete_monitoring_schedule(self, *, MonitoringScheduleName: str) -> None:
        """
        Deletes a monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_monitoring_schedule)
        """
    def delete_notebook_instance(self, *, NotebookInstanceName: str) -> None:
        """
        Deletes an SageMaker notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_notebook_instance)
        """
    def delete_notebook_instance_lifecycle_config(
        self, *, NotebookInstanceLifecycleConfigName: str
    ) -> None:
        """
        Deletes a notebook instance lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_notebook_instance_lifecycle_config)
        """
    def delete_pipeline(
        self, *, PipelineName: str, ClientRequestToken: str
    ) -> DeletePipelineResponseTypeDef:
        """
        Deletes a pipeline if there are no running instances of the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_pipeline)
        """
    def delete_project(self, *, ProjectName: str) -> None:
        """
        Delete the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_project)
        """
    def delete_space(self, *, DomainId: str, SpaceName: str) -> None:
        """
        Used to delete a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_space)
        """
    def delete_studio_lifecycle_config(self, *, StudioLifecycleConfigName: str) -> None:
        """
        Deletes the Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_studio_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_studio_lifecycle_config)
        """
    def delete_tags(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from an SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_tags)
        """
    def delete_trial(self, *, TrialName: str) -> DeleteTrialResponseTypeDef:
        """
        Deletes the specified trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_trial)
        """
    def delete_trial_component(
        self, *, TrialComponentName: str
    ) -> DeleteTrialComponentResponseTypeDef:
        """
        Deletes the specified trial component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_trial_component)
        """
    def delete_user_profile(self, *, DomainId: str, UserProfileName: str) -> None:
        """
        Deletes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_user_profile)
        """
    def delete_workforce(self, *, WorkforceName: str) -> Dict[str, Any]:
        """
        Use this operation to delete a workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_workforce)
        """
    def delete_workteam(self, *, WorkteamName: str) -> DeleteWorkteamResponseTypeDef:
        """
        Deletes an existing work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete_workteam)
        """
    def deregister_devices(self, *, DeviceFleetName: str, DeviceNames: List[str]) -> None:
        """
        Deregisters the specified devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.deregister_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#deregister_devices)
        """
    def describe_action(self, *, ActionName: str) -> DescribeActionResponseTypeDef:
        """
        Describes an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_action)
        """
    def describe_algorithm(self, *, AlgorithmName: str) -> DescribeAlgorithmOutputTypeDef:
        """
        Returns a description of the specified algorithm that is in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_algorithm)
        """
    def describe_app(
        self,
        *,
        DomainId: str,
        AppType: AppTypeType,
        AppName: str,
        UserProfileName: str = None,
        SpaceName: str = None
    ) -> DescribeAppResponseTypeDef:
        """
        Describes the app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_app)
        """
    def describe_app_image_config(
        self, *, AppImageConfigName: str
    ) -> DescribeAppImageConfigResponseTypeDef:
        """
        Describes an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_app_image_config)
        """
    def describe_artifact(self, *, ArtifactArn: str) -> DescribeArtifactResponseTypeDef:
        """
        Describes an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_artifact)
        """
    def describe_auto_ml_job(self, *, AutoMLJobName: str) -> DescribeAutoMLJobResponseTypeDef:
        """
        Returns information about an AutoML job created by calling `CreateAutoMLJob <htt
        ps://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html>
        `__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_auto_ml_job)
        """
    def describe_auto_ml_job_v2(self, *, AutoMLJobName: str) -> DescribeAutoMLJobV2ResponseTypeDef:
        """
        Returns information about an AutoML job created by calling `CreateAutoMLJobV2 <h
        ttps://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.h
        tml>`__ or `CreateAutoMLJob <https://docs.aws.amazon.com/sagemaker/latest/APIRef
        erence/API_CreateAutoMLJob.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job_v2)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_auto_ml_job_v2)
        """
    def describe_code_repository(
        self, *, CodeRepositoryName: str
    ) -> DescribeCodeRepositoryOutputTypeDef:
        """
        Gets details about the specified Git repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_code_repository)
        """
    def describe_compilation_job(
        self, *, CompilationJobName: str
    ) -> DescribeCompilationJobResponseTypeDef:
        """
        Returns information about a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_compilation_job)
        """
    def describe_context(self, *, ContextName: str) -> DescribeContextResponseTypeDef:
        """
        Describes a context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_context)
        """
    def describe_data_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeDataQualityJobDefinitionResponseTypeDef:
        """
        Gets the details of a data quality monitoring job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_data_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_data_quality_job_definition)
        """
    def describe_device(
        self, *, DeviceName: str, DeviceFleetName: str, NextToken: str = None
    ) -> DescribeDeviceResponseTypeDef:
        """
        Describes the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_device)
        """
    def describe_device_fleet(self, *, DeviceFleetName: str) -> DescribeDeviceFleetResponseTypeDef:
        """
        A description of the fleet the device belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_device_fleet)
        """
    def describe_domain(self, *, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        The description of the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_domain)
        """
    def describe_edge_deployment_plan(
        self, *, EdgeDeploymentPlanName: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeEdgeDeploymentPlanResponseTypeDef:
        """
        Describes an edge deployment plan with deployment status per stage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_edge_deployment_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_edge_deployment_plan)
        """
    def describe_edge_packaging_job(
        self, *, EdgePackagingJobName: str
    ) -> DescribeEdgePackagingJobResponseTypeDef:
        """
        A description of edge packaging jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_edge_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_edge_packaging_job)
        """
    def describe_endpoint(self, *, EndpointName: str) -> DescribeEndpointOutputTypeDef:
        """
        Returns the description of an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_endpoint)
        """
    def describe_endpoint_config(
        self, *, EndpointConfigName: str
    ) -> DescribeEndpointConfigOutputTypeDef:
        """
        Returns the description of an endpoint configuration created using the
        `CreateEndpointConfig` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_endpoint_config)
        """
    def describe_experiment(self, *, ExperimentName: str) -> DescribeExperimentResponseTypeDef:
        """
        Provides a list of an experiment's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_experiment)
        """
    def describe_feature_group(
        self, *, FeatureGroupName: str, NextToken: str = None
    ) -> DescribeFeatureGroupResponseTypeDef:
        """
        Use this operation to describe a `FeatureGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_feature_group)
        """
    def describe_feature_metadata(
        self, *, FeatureGroupName: str, FeatureName: str
    ) -> DescribeFeatureMetadataResponseTypeDef:
        """
        Shows the metadata for a feature within a feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_feature_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_feature_metadata)
        """
    def describe_flow_definition(
        self, *, FlowDefinitionName: str
    ) -> DescribeFlowDefinitionResponseTypeDef:
        """
        Returns information about the specified flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_flow_definition)
        """
    def describe_hub(self, *, HubName: str) -> DescribeHubResponseTypeDef:
        """
        Describe a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_hub)
        """
    def describe_hub_content(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        HubContentVersion: str = None
    ) -> DescribeHubContentResponseTypeDef:
        """
        Describe the content of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_hub_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_hub_content)
        """
    def describe_human_task_ui(self, *, HumanTaskUiName: str) -> DescribeHumanTaskUiResponseTypeDef:
        """
        Returns information about the requested human task user interface (worker task
        template).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_human_task_ui)
        """
    def describe_hyper_parameter_tuning_job(
        self, *, HyperParameterTuningJobName: str
    ) -> DescribeHyperParameterTuningJobResponseTypeDef:
        """
        Returns a description of a hyperparameter tuning job, depending on the fields
        selected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_hyper_parameter_tuning_job)
        """
    def describe_image(self, *, ImageName: str) -> DescribeImageResponseTypeDef:
        """
        Describes a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_image)
        """
    def describe_image_version(
        self, *, ImageName: str, Version: int = None, Alias: str = None
    ) -> DescribeImageVersionResponseTypeDef:
        """
        Describes a version of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_image_version)
        """
    def describe_inference_experiment(
        self, *, Name: str
    ) -> DescribeInferenceExperimentResponseTypeDef:
        """
        Returns details about an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_inference_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_inference_experiment)
        """
    def describe_inference_recommendations_job(
        self, *, JobName: str
    ) -> DescribeInferenceRecommendationsJobResponseTypeDef:
        """
        Provides the results of the Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_inference_recommendations_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_inference_recommendations_job)
        """
    def describe_labeling_job(self, *, LabelingJobName: str) -> DescribeLabelingJobResponseTypeDef:
        """
        Gets information about a labeling job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_labeling_job)
        """
    def describe_lineage_group(
        self, *, LineageGroupName: str
    ) -> DescribeLineageGroupResponseTypeDef:
        """
        Provides a list of properties for the requested lineage group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_lineage_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_lineage_group)
        """
    def describe_model(self, *, ModelName: str) -> DescribeModelOutputTypeDef:
        """
        Describes a model that you created using the `CreateModel` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model)
        """
    def describe_model_bias_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelBiasJobDefinitionResponseTypeDef:
        """
        Returns a description of a model bias job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_bias_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_bias_job_definition)
        """
    def describe_model_card(
        self, *, ModelCardName: str, ModelCardVersion: int = None
    ) -> DescribeModelCardResponseTypeDef:
        """
        Describes the content, creation time, and security configuration of an Amazon
        SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_card)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_card)
        """
    def describe_model_card_export_job(
        self, *, ModelCardExportJobArn: str
    ) -> DescribeModelCardExportJobResponseTypeDef:
        """
        Describes an Amazon SageMaker Model Card export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_card_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_card_export_job)
        """
    def describe_model_explainability_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelExplainabilityJobDefinitionResponseTypeDef:
        """
        Returns a description of a model explainability job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_explainability_job_definition)
        """
    def describe_model_package(self, *, ModelPackageName: str) -> DescribeModelPackageOutputTypeDef:
        """
        Returns a description of the specified model package, which is used to create
        SageMaker models or list them on Amazon Web Services Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_package)
        """
    def describe_model_package_group(
        self, *, ModelPackageGroupName: str
    ) -> DescribeModelPackageGroupOutputTypeDef:
        """
        Gets a description for the specified model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_package_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_package_group)
        """
    def describe_model_quality_job_definition(
        self, *, JobDefinitionName: str
    ) -> DescribeModelQualityJobDefinitionResponseTypeDef:
        """
        Returns a description of a model quality job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_model_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_model_quality_job_definition)
        """
    def describe_monitoring_schedule(
        self, *, MonitoringScheduleName: str
    ) -> DescribeMonitoringScheduleResponseTypeDef:
        """
        Describes the schedule for a monitoring job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_monitoring_schedule)
        """
    def describe_notebook_instance(
        self, *, NotebookInstanceName: str
    ) -> DescribeNotebookInstanceOutputTypeDef:
        """
        Returns information about a notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_notebook_instance)
        """
    def describe_notebook_instance_lifecycle_config(
        self, *, NotebookInstanceLifecycleConfigName: str
    ) -> DescribeNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        Returns a description of a notebook instance lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_notebook_instance_lifecycle_config)
        """
    def describe_pipeline(self, *, PipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        Describes the details of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_pipeline)
        """
    def describe_pipeline_definition_for_execution(
        self, *, PipelineExecutionArn: str
    ) -> DescribePipelineDefinitionForExecutionResponseTypeDef:
        """
        Describes the details of an execution's pipeline definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_definition_for_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_pipeline_definition_for_execution)
        """
    def describe_pipeline_execution(
        self, *, PipelineExecutionArn: str
    ) -> DescribePipelineExecutionResponseTypeDef:
        """
        Describes the details of a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_pipeline_execution)
        """
    def describe_processing_job(
        self, *, ProcessingJobName: str
    ) -> DescribeProcessingJobResponseTypeDef:
        """
        Returns a description of a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_processing_job)
        """
    def describe_project(self, *, ProjectName: str) -> DescribeProjectOutputTypeDef:
        """
        Describes the details of a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_project)
        """
    def describe_space(self, *, DomainId: str, SpaceName: str) -> DescribeSpaceResponseTypeDef:
        """
        Describes the space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_space)
        """
    def describe_studio_lifecycle_config(
        self, *, StudioLifecycleConfigName: str
    ) -> DescribeStudioLifecycleConfigResponseTypeDef:
        """
        Describes the Studio Lifecycle Configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_studio_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_studio_lifecycle_config)
        """
    def describe_subscribed_workteam(
        self, *, WorkteamArn: str
    ) -> DescribeSubscribedWorkteamResponseTypeDef:
        """
        Gets information about a work team provided by a vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_subscribed_workteam)
        """
    def describe_training_job(self, *, TrainingJobName: str) -> DescribeTrainingJobResponseTypeDef:
        """
        Returns information about a training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_training_job)
        """
    def describe_transform_job(
        self, *, TransformJobName: str
    ) -> DescribeTransformJobResponseTypeDef:
        """
        Returns information about a transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_transform_job)
        """
    def describe_trial(self, *, TrialName: str) -> DescribeTrialResponseTypeDef:
        """
        Provides a list of a trial's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_trial)
        """
    def describe_trial_component(
        self, *, TrialComponentName: str
    ) -> DescribeTrialComponentResponseTypeDef:
        """
        Provides a list of a trials component's properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_trial_component)
        """
    def describe_user_profile(
        self, *, DomainId: str, UserProfileName: str
    ) -> DescribeUserProfileResponseTypeDef:
        """
        Describes a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_user_profile)
        """
    def describe_workforce(self, *, WorkforceName: str) -> DescribeWorkforceResponseTypeDef:
        """
        Lists private workforce information, including workforce name, Amazon Resource
        Name (ARN), and, if applicable, allowed IP address ranges ( `CIDRs
        <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html>`__).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_workforce)
        """
    def describe_workteam(self, *, WorkteamName: str) -> DescribeWorkteamResponseTypeDef:
        """
        Gets information about a specific work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe_workteam)
        """
    def disable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        Disables using Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.disable_sagemaker_servicecatalog_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#disable_sagemaker_servicecatalog_portfolio)
        """
    def disassociate_trial_component(
        self, *, TrialComponentName: str, TrialName: str
    ) -> DisassociateTrialComponentResponseTypeDef:
        """
        Disassociates a trial component from a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#disassociate_trial_component)
        """
    def enable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        Enables using Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.enable_sagemaker_servicecatalog_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#enable_sagemaker_servicecatalog_portfolio)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#generate_presigned_url)
        """
    def get_device_fleet_report(
        self, *, DeviceFleetName: str
    ) -> GetDeviceFleetReportResponseTypeDef:
        """
        Describes a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.get_device_fleet_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get_device_fleet_report)
        """
    def get_lineage_group_policy(
        self, *, LineageGroupName: str
    ) -> GetLineageGroupPolicyResponseTypeDef:
        """
        The resource policy for the lineage group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.get_lineage_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get_lineage_group_policy)
        """
    def get_model_package_group_policy(
        self, *, ModelPackageGroupName: str
    ) -> GetModelPackageGroupPolicyOutputTypeDef:
        """
        Gets a resource policy that manages access for a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.get_model_package_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get_model_package_group_policy)
        """
    def get_sagemaker_servicecatalog_portfolio_status(
        self,
    ) -> GetSagemakerServicecatalogPortfolioStatusOutputTypeDef:
        """
        Gets the status of Service Catalog in SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.get_sagemaker_servicecatalog_portfolio_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get_sagemaker_servicecatalog_portfolio_status)
        """
    def get_scaling_configuration_recommendation(
        self,
        *,
        InferenceRecommendationsJobName: str,
        RecommendationId: str = None,
        EndpointName: str = None,
        TargetCpuUtilizationPerCore: int = None,
        ScalingPolicyObjective: "ScalingPolicyObjectiveTypeDef" = None
    ) -> GetScalingConfigurationRecommendationResponseTypeDef:
        """
        Starts an Amazon SageMaker Inference Recommender autoscaling recommendation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.get_scaling_configuration_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get_scaling_configuration_recommendation)
        """
    def get_search_suggestions(
        self, *, Resource: ResourceTypeType, SuggestionQuery: "SuggestionQueryTypeDef" = None
    ) -> GetSearchSuggestionsResponseTypeDef:
        """
        An auto-complete API for the search functionality in the SageMaker console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get_search_suggestions)
        """
    def import_hub_content(
        self,
        *,
        HubContentName: str,
        HubContentType: HubContentTypeType,
        DocumentSchemaVersion: str,
        HubName: str,
        HubContentDocument: str,
        HubContentVersion: str = None,
        HubContentDisplayName: str = None,
        HubContentDescription: str = None,
        HubContentMarkdown: str = None,
        HubContentSearchKeywords: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportHubContentResponseTypeDef:
        """
        Import hub content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.import_hub_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#import_hub_content)
        """
    def list_actions(
        self,
        *,
        SourceUri: str = None,
        ActionType: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortActionsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListActionsResponseTypeDef:
        """
        Lists the actions in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_actions)
        """
    def list_algorithms(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: AlgorithmSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListAlgorithmsOutputTypeDef:
        """
        Lists the machine learning algorithms that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_algorithms)
        """
    def list_aliases(
        self,
        *,
        ImageName: str,
        Alias: str = None,
        Version: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAliasesResponseTypeDef:
        """
        Lists the aliases of a specified image or image version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_aliases)
        """
    def list_app_image_configs(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        ModifiedTimeBefore: Union[datetime, str] = None,
        ModifiedTimeAfter: Union[datetime, str] = None,
        SortBy: AppImageConfigSortKeyType = None,
        SortOrder: SortOrderType = None
    ) -> ListAppImageConfigsResponseTypeDef:
        """
        Lists the AppImageConfigs in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_app_image_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_app_image_configs)
        """
    def list_apps(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrderType = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        SpaceNameEquals: str = None
    ) -> ListAppsResponseTypeDef:
        """
        Lists apps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_apps)
        """
    def list_artifacts(
        self,
        *,
        SourceUri: str = None,
        ArtifactType: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListArtifactsResponseTypeDef:
        """
        Lists the artifacts in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_artifacts)
        """
    def list_associations(
        self,
        *,
        SourceArn: str = None,
        DestinationArn: str = None,
        SourceType: str = None,
        DestinationType: str = None,
        AssociationType: AssociationEdgeTypeType = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortAssociationsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAssociationsResponseTypeDef:
        """
        Lists the associations in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_associations)
        """
    def list_auto_ml_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: AutoMLJobStatusType = None,
        SortOrder: AutoMLSortOrderType = None,
        SortBy: AutoMLSortByType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAutoMLJobsResponseTypeDef:
        """
        Request a list of jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_auto_ml_jobs)
        """
    def list_candidates_for_auto_ml_job(
        self,
        *,
        AutoMLJobName: str,
        StatusEquals: CandidateStatusType = None,
        CandidateNameEquals: str = None,
        SortOrder: AutoMLSortOrderType = None,
        SortBy: CandidateSortByType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCandidatesForAutoMLJobResponseTypeDef:
        """
        List the candidates created for the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_candidates_for_auto_ml_job)
        """
    def list_code_repositories(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: CodeRepositorySortByType = None,
        SortOrder: CodeRepositorySortOrderType = None
    ) -> ListCodeRepositoriesOutputTypeDef:
        """
        Gets a list of the Git repositories in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_code_repositories)
        """
    def list_compilation_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: CompilationJobStatusType = None,
        SortBy: ListCompilationJobsSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListCompilationJobsResponseTypeDef:
        """
        Lists model compilation jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_compilation_jobs)
        """
    def list_contexts(
        self,
        *,
        SourceUri: str = None,
        ContextType: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortContextsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListContextsResponseTypeDef:
        """
        Lists the contexts in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_contexts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_contexts)
        """
    def list_data_quality_job_definitions(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None
    ) -> ListDataQualityJobDefinitionsResponseTypeDef:
        """
        Lists the data quality job definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_data_quality_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_data_quality_job_definitions)
        """
    def list_device_fleets(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        SortBy: ListDeviceFleetsSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListDeviceFleetsResponseTypeDef:
        """
        Returns a list of devices in the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_device_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_device_fleets)
        """
    def list_devices(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        LatestHeartbeatAfter: Union[datetime, str] = None,
        ModelName: str = None,
        DeviceFleetName: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        A list of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_devices)
        """
    def list_domains(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        Lists the domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_domains)
        """
    def list_edge_deployment_plans(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        DeviceFleetNameContains: str = None,
        SortBy: ListEdgeDeploymentPlansSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListEdgeDeploymentPlansResponseTypeDef:
        """
        Lists all edge deployment plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_edge_deployment_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_edge_deployment_plans)
        """
    def list_edge_packaging_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        ModelNameContains: str = None,
        StatusEquals: EdgePackagingJobStatusType = None,
        SortBy: ListEdgePackagingJobsSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListEdgePackagingJobsResponseTypeDef:
        """
        Returns a list of edge packaging jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_edge_packaging_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_edge_packaging_jobs)
        """
    def list_endpoint_configs(
        self,
        *,
        SortBy: EndpointConfigSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None
    ) -> ListEndpointConfigsOutputTypeDef:
        """
        Lists endpoint configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_endpoint_configs)
        """
    def list_endpoints(
        self,
        *,
        SortBy: EndpointSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: EndpointStatusType = None
    ) -> ListEndpointsOutputTypeDef:
        """
        Lists endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_endpoints)
        """
    def list_experiments(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortExperimentsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListExperimentsResponseTypeDef:
        """
        Lists all the experiments in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_experiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_experiments)
        """
    def list_feature_groups(
        self,
        *,
        NameContains: str = None,
        FeatureGroupStatusEquals: FeatureGroupStatusType = None,
        OfflineStoreStatusEquals: OfflineStoreStatusValueType = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: FeatureGroupSortOrderType = None,
        SortBy: FeatureGroupSortByType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListFeatureGroupsResponseTypeDef:
        """
        List `FeatureGroup`s based on given filter and order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_feature_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_feature_groups)
        """
    def list_flow_definitions(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListFlowDefinitionsResponseTypeDef:
        """
        Returns information about the flow definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_flow_definitions)
        """
    def list_hub_content_versions(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        HubContentName: str,
        MinVersion: str = None,
        MaxSchemaVersion: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        SortBy: HubContentSortByType = None,
        SortOrder: SortOrderType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListHubContentVersionsResponseTypeDef:
        """
        List hub content versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_hub_content_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_hub_content_versions)
        """
    def list_hub_contents(
        self,
        *,
        HubName: str,
        HubContentType: HubContentTypeType,
        NameContains: str = None,
        MaxSchemaVersion: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        SortBy: HubContentSortByType = None,
        SortOrder: SortOrderType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListHubContentsResponseTypeDef:
        """
        List the contents of a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_hub_contents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_hub_contents)
        """
    def list_hubs(
        self,
        *,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        SortBy: HubSortByType = None,
        SortOrder: SortOrderType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListHubsResponseTypeDef:
        """
        List all existing hubs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_hubs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_hubs)
        """
    def list_human_task_uis(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListHumanTaskUisResponseTypeDef:
        """
        Returns information about the human task user interfaces in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_human_task_uis)
        """
    def list_hyper_parameter_tuning_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: HyperParameterTuningJobSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        StatusEquals: HyperParameterTuningJobStatusType = None
    ) -> ListHyperParameterTuningJobsResponseTypeDef:
        """
        Gets a list of `HyperParameterTuningJobSummary <https://docs.aws.amazon.com/sage
        maker/latest/APIReference/API_HyperParameterTuningJobSummary.html>`__ objects
        that describe the hyperparameter tuning jobs launched in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_hyper_parameter_tuning_jobs)
        """
    def list_image_versions(
        self,
        *,
        ImageName: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: ImageVersionSortByType = None,
        SortOrder: ImageVersionSortOrderType = None
    ) -> ListImageVersionsResponseTypeDef:
        """
        Lists the versions of a specified image and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_image_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_image_versions)
        """
    def list_images(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: ImageSortByType = None,
        SortOrder: ImageSortOrderType = None
    ) -> ListImagesResponseTypeDef:
        """
        Lists the images in your account and their properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_images)
        """
    def list_inference_experiments(
        self,
        *,
        NameContains: str = None,
        Type: Literal["ShadowMode"] = None,
        StatusEquals: InferenceExperimentStatusType = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        SortBy: SortInferenceExperimentsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListInferenceExperimentsResponseTypeDef:
        """
        Returns the list of all inference experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_inference_experiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_inference_experiments)
        """
    def list_inference_recommendations_job_steps(
        self,
        *,
        JobName: str,
        Status: RecommendationJobStatusType = None,
        StepType: Literal["BENCHMARK"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListInferenceRecommendationsJobStepsResponseTypeDef:
        """
        Returns a list of the subtasks for an Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_inference_recommendations_job_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_inference_recommendations_job_steps)
        """
    def list_inference_recommendations_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: RecommendationJobStatusType = None,
        SortBy: ListInferenceRecommendationsJobsSortByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        ModelNameEquals: str = None,
        ModelPackageVersionArnEquals: str = None
    ) -> ListInferenceRecommendationsJobsResponseTypeDef:
        """
        Lists recommendation jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_inference_recommendations_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_inference_recommendations_jobs)
        """
    def list_labeling_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        StatusEquals: LabelingJobStatusType = None
    ) -> ListLabelingJobsResponseTypeDef:
        """
        Gets a list of labeling jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_labeling_jobs)
        """
    def list_labeling_jobs_for_workteam(
        self,
        *,
        WorkteamArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrderType = None
    ) -> ListLabelingJobsForWorkteamResponseTypeDef:
        """
        Gets a list of labeling jobs assigned to a specified work team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_labeling_jobs_for_workteam)
        """
    def list_lineage_groups(
        self,
        *,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortLineageGroupsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLineageGroupsResponseTypeDef:
        """
        A list of lineage groups shared with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_lineage_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_lineage_groups)
        """
    def list_model_bias_job_definitions(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None
    ) -> ListModelBiasJobDefinitionsResponseTypeDef:
        """
        Lists model bias jobs definitions that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_bias_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_bias_job_definitions)
        """
    def list_model_card_export_jobs(
        self,
        *,
        ModelCardName: str,
        ModelCardVersion: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        ModelCardExportJobNameContains: str = None,
        StatusEquals: ModelCardExportJobStatusType = None,
        SortBy: ModelCardExportJobSortByType = None,
        SortOrder: ModelCardExportJobSortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListModelCardExportJobsResponseTypeDef:
        """
        List the export jobs for the Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_card_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_card_export_jobs)
        """
    def list_model_card_versions(
        self,
        *,
        ModelCardName: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        ModelCardStatus: ModelCardStatusType = None,
        NextToken: str = None,
        SortBy: Literal["Version"] = None,
        SortOrder: ModelCardSortOrderType = None
    ) -> ListModelCardVersionsResponseTypeDef:
        """
        List existing versions of an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_card_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_card_versions)
        """
    def list_model_cards(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        ModelCardStatus: ModelCardStatusType = None,
        NextToken: str = None,
        SortBy: ModelCardSortByType = None,
        SortOrder: ModelCardSortOrderType = None
    ) -> ListModelCardsResponseTypeDef:
        """
        List existing model cards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_cards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_cards)
        """
    def list_model_explainability_job_definitions(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None
    ) -> ListModelExplainabilityJobDefinitionsResponseTypeDef:
        """
        Lists model explainability job definitions that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_explainability_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_explainability_job_definitions)
        """
    def list_model_metadata(
        self,
        *,
        SearchExpression: "ModelMetadataSearchExpressionTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListModelMetadataResponseTypeDef:
        """
        Lists the domain, framework, task, and model name of standard machine learning
        models found in common model zoos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_metadata)
        """
    def list_model_package_groups(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: ModelPackageGroupSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListModelPackageGroupsOutputTypeDef:
        """
        Gets a list of the model groups in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_package_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_package_groups)
        """
    def list_model_packages(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        ModelApprovalStatus: ModelApprovalStatusType = None,
        ModelPackageGroupName: str = None,
        ModelPackageType: ModelPackageTypeType = None,
        NextToken: str = None,
        SortBy: ModelPackageSortByType = None,
        SortOrder: SortOrderType = None
    ) -> ListModelPackagesOutputTypeDef:
        """
        Lists the model packages that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_packages)
        """
    def list_model_quality_job_definitions(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None
    ) -> ListModelQualityJobDefinitionsResponseTypeDef:
        """
        Gets a list of model quality monitoring job definitions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_model_quality_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_model_quality_job_definitions)
        """
    def list_models(
        self,
        *,
        SortBy: ModelSortKeyType = None,
        SortOrder: OrderKeyType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None
    ) -> ListModelsOutputTypeDef:
        """
        Lists models created with the `CreateModel` API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_models)
        """
    def list_monitoring_alert_history(
        self,
        *,
        MonitoringScheduleName: str = None,
        MonitoringAlertName: str = None,
        SortBy: MonitoringAlertHistorySortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        StatusEquals: MonitoringAlertStatusType = None
    ) -> ListMonitoringAlertHistoryResponseTypeDef:
        """
        Gets a list of past alerts in a model monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_alert_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_monitoring_alert_history)
        """
    def list_monitoring_alerts(
        self, *, MonitoringScheduleName: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMonitoringAlertsResponseTypeDef:
        """
        Gets the alerts for a single monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_alerts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_monitoring_alerts)
        """
    def list_monitoring_executions(
        self,
        *,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: MonitoringExecutionSortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        ScheduledTimeBefore: Union[datetime, str] = None,
        ScheduledTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: ExecutionStatusType = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringTypeType = None
    ) -> ListMonitoringExecutionsResponseTypeDef:
        """
        Returns list of all monitoring job executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_monitoring_executions)
        """
    def list_monitoring_schedules(
        self,
        *,
        EndpointName: str = None,
        SortBy: MonitoringScheduleSortKeyType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: ScheduleStatusType = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringTypeType = None
    ) -> ListMonitoringSchedulesResponseTypeDef:
        """
        Returns list of all monitoring schedules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_monitoring_schedules)
        """
    def list_notebook_instance_lifecycle_configs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: NotebookInstanceLifecycleConfigSortKeyType = None,
        SortOrder: NotebookInstanceLifecycleConfigSortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None
    ) -> ListNotebookInstanceLifecycleConfigsOutputTypeDef:
        """
        Lists notebook instance lifestyle configurations created with the
        `CreateNotebookInstanceLifecycleConfig <https://docs.aws.amazon.com/sagemaker/la
        test/APIReference/API_CreateNotebookInstanceLifecycleConfig.html>`__ API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_notebook_instance_lifecycle_configs)
        """
    def list_notebook_instances(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: NotebookInstanceSortKeyType = None,
        SortOrder: NotebookInstanceSortOrderType = None,
        NameContains: str = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        StatusEquals: NotebookInstanceStatusType = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None
    ) -> ListNotebookInstancesOutputTypeDef:
        """
        Returns a list of the SageMaker notebook instances in the requester's account in
        an Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_notebook_instances)
        """
    def list_pipeline_execution_steps(
        self,
        *,
        PipelineExecutionArn: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrderType = None
    ) -> ListPipelineExecutionStepsResponseTypeDef:
        """
        Gets a list of `PipeLineExecutionStep` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_execution_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_pipeline_execution_steps)
        """
    def list_pipeline_executions(
        self,
        *,
        PipelineName: str,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortPipelineExecutionsByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPipelineExecutionsResponseTypeDef:
        """
        Gets a list of the pipeline executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_pipeline_executions)
        """
    def list_pipeline_parameters_for_execution(
        self, *, PipelineExecutionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPipelineParametersForExecutionResponseTypeDef:
        """
        Gets a list of parameters for a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_parameters_for_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_pipeline_parameters_for_execution)
        """
    def list_pipelines(
        self,
        *,
        PipelineNamePrefix: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortPipelinesByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPipelinesResponseTypeDef:
        """
        Gets a list of pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_pipelines)
        """
    def list_processing_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: ProcessingJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListProcessingJobsResponseTypeDef:
        """
        Lists processing jobs that satisfy various filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_processing_jobs)
        """
    def list_projects(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: ProjectSortByType = None,
        SortOrder: ProjectSortOrderType = None
    ) -> ListProjectsOutputTypeDef:
        """
        Gets a list of the projects in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_projects)
        """
    def list_resource_catalogs(
        self,
        *,
        NameContains: str = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: ResourceCatalogSortOrderType = None,
        SortBy: Literal["CreationTime"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListResourceCatalogsResponseTypeDef:
        """
        Lists Amazon SageMaker Catalogs based on given filters and orders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_resource_catalogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_resource_catalogs)
        """
    def list_spaces(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrderType = None,
        SortBy: SpaceSortKeyType = None,
        DomainIdEquals: str = None,
        SpaceNameContains: str = None
    ) -> ListSpacesResponseTypeDef:
        """
        Lists spaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_spaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_spaces)
        """
    def list_stage_devices(
        self,
        *,
        EdgeDeploymentPlanName: str,
        StageName: str,
        NextToken: str = None,
        MaxResults: int = None,
        ExcludeDevicesDeployedInOtherStage: bool = None
    ) -> ListStageDevicesResponseTypeDef:
        """
        Lists devices allocated to the stage, containing detailed device information and
        deployment status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_stage_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_stage_devices)
        """
    def list_studio_lifecycle_configs(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        AppTypeEquals: StudioLifecycleConfigAppTypeType = None,
        CreationTimeBefore: Union[datetime, str] = None,
        CreationTimeAfter: Union[datetime, str] = None,
        ModifiedTimeBefore: Union[datetime, str] = None,
        ModifiedTimeAfter: Union[datetime, str] = None,
        SortBy: StudioLifecycleConfigSortKeyType = None,
        SortOrder: SortOrderType = None
    ) -> ListStudioLifecycleConfigsResponseTypeDef:
        """
        Lists the Studio Lifecycle Configurations in your Amazon Web Services Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_studio_lifecycle_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_studio_lifecycle_configs)
        """
    def list_subscribed_workteams(
        self, *, NameContains: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListSubscribedWorkteamsResponseTypeDef:
        """
        Gets a list of the work teams that you are subscribed to in the Amazon Web
        Services Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_subscribed_workteams)
        """
    def list_tags(
        self, *, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        Returns the tags for the specified SageMaker resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_tags)
        """
    def list_training_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: TrainingJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        WarmPoolStatusEquals: WarmPoolResourceStatusType = None
    ) -> ListTrainingJobsResponseTypeDef:
        """
        Lists training jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_training_jobs)
        """
    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        *,
        HyperParameterTuningJobName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StatusEquals: TrainingJobStatusType = None,
        SortBy: TrainingJobSortByOptionsType = None,
        SortOrder: SortOrderType = None
    ) -> ListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
        """
        Gets a list of `TrainingJobSummary <https://docs.aws.amazon.com/sagemaker/latest
        /APIReference/API_TrainingJobSummary.html>`__ objects that describe the training
        jobs that a hyperparameter tuning job launched.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_training_jobs_for_hyper_parameter_tuning_job)
        """
    def list_transform_jobs(
        self,
        *,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        LastModifiedTimeAfter: Union[datetime, str] = None,
        LastModifiedTimeBefore: Union[datetime, str] = None,
        NameContains: str = None,
        StatusEquals: TransformJobStatusType = None,
        SortBy: SortByType = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTransformJobsResponseTypeDef:
        """
        Lists transform jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_transform_jobs)
        """
    def list_trial_components(
        self,
        *,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortTrialComponentsByType = None,
        SortOrder: SortOrderType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListTrialComponentsResponseTypeDef:
        """
        Lists the trial components in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_trial_components)
        """
    def list_trials(
        self,
        *,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: Union[datetime, str] = None,
        CreatedBefore: Union[datetime, str] = None,
        SortBy: SortTrialsByType = None,
        SortOrder: SortOrderType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListTrialsResponseTypeDef:
        """
        Lists the trials in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_trials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_trials)
        """
    def list_user_profiles(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrderType = None,
        SortBy: UserProfileSortKeyType = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None
    ) -> ListUserProfilesResponseTypeDef:
        """
        Lists user profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_user_profiles)
        """
    def list_workforces(
        self,
        *,
        SortBy: ListWorkforcesSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListWorkforcesResponseTypeDef:
        """
        Use this operation to list all private and vendor workforces in an Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_workforces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_workforces)
        """
    def list_workteams(
        self,
        *,
        SortBy: ListWorkteamsSortByOptionsType = None,
        SortOrder: SortOrderType = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListWorkteamsResponseTypeDef:
        """
        Gets a list of private work teams that you have defined in a region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.list_workteams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list_workteams)
        """
    def put_model_package_group_policy(
        self, *, ModelPackageGroupName: str, ResourcePolicy: str
    ) -> PutModelPackageGroupPolicyOutputTypeDef:
        """
        Adds a resouce policy to control access to a model group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.put_model_package_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#put_model_package_group_policy)
        """
    def query_lineage(
        self,
        *,
        StartArns: List[str] = None,
        Direction: DirectionType = None,
        IncludeEdges: bool = None,
        Filters: "QueryFiltersTypeDef" = None,
        MaxDepth: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> QueryLineageResponseTypeDef:
        """
        Use this action to inspect your lineage and discover relationships between
        entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.query_lineage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#query_lineage)
        """
    def register_devices(
        self,
        *,
        DeviceFleetName: str,
        Devices: List["DeviceTypeDef"],
        Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        Register devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.register_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#register_devices)
        """
    def render_ui_template(
        self,
        *,
        Task: "RenderableTaskTypeDef",
        RoleArn: str,
        UiTemplate: "UiTemplateTypeDef" = None,
        HumanTaskUiArn: str = None
    ) -> RenderUiTemplateResponseTypeDef:
        """
        Renders the UI template so that you can preview the worker's experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#render_ui_template)
        """
    def retry_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        ClientRequestToken: str,
        ParallelismConfiguration: "ParallelismConfigurationTypeDef" = None
    ) -> RetryPipelineExecutionResponseTypeDef:
        """
        Retry the execution of the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.retry_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#retry_pipeline_execution)
        """
    def search(
        self,
        *,
        Resource: ResourceTypeType,
        SearchExpression: "SearchExpressionTypeDef" = None,
        SortBy: str = None,
        SortOrder: SearchSortOrderType = None,
        NextToken: str = None,
        MaxResults: int = None,
        CrossAccountFilterOption: CrossAccountFilterOptionType = None
    ) -> SearchResponseTypeDef:
        """
        Finds SageMaker resources that match a search query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#search)
        """
    def send_pipeline_execution_step_failure(
        self, *, CallbackToken: str, FailureReason: str = None, ClientRequestToken: str = None
    ) -> SendPipelineExecutionStepFailureResponseTypeDef:
        """
        Notifies the pipeline that the execution of a callback step failed, along with a
        message describing why.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.send_pipeline_execution_step_failure)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#send_pipeline_execution_step_failure)
        """
    def send_pipeline_execution_step_success(
        self,
        *,
        CallbackToken: str,
        OutputParameters: List["OutputParameterTypeDef"] = None,
        ClientRequestToken: str = None
    ) -> SendPipelineExecutionStepSuccessResponseTypeDef:
        """
        Notifies the pipeline that the execution of a callback step succeeded and
        provides a list of the step's output parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.send_pipeline_execution_step_success)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#send_pipeline_execution_step_success)
        """
    def start_edge_deployment_stage(self, *, EdgeDeploymentPlanName: str, StageName: str) -> None:
        """
        Starts a stage in an edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.start_edge_deployment_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start_edge_deployment_stage)
        """
    def start_inference_experiment(self, *, Name: str) -> StartInferenceExperimentResponseTypeDef:
        """
        Starts an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.start_inference_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start_inference_experiment)
        """
    def start_monitoring_schedule(self, *, MonitoringScheduleName: str) -> None:
        """
        Starts a previously stopped monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start_monitoring_schedule)
        """
    def start_notebook_instance(self, *, NotebookInstanceName: str) -> None:
        """
        Launches an ML compute instance with the latest version of the libraries and
        attaches your ML storage volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start_notebook_instance)
        """
    def start_pipeline_execution(
        self,
        *,
        PipelineName: str,
        ClientRequestToken: str,
        PipelineExecutionDisplayName: str = None,
        PipelineParameters: List["ParameterTypeDef"] = None,
        PipelineExecutionDescription: str = None,
        ParallelismConfiguration: "ParallelismConfigurationTypeDef" = None,
        SelectiveExecutionConfig: "SelectiveExecutionConfigTypeDef" = None
    ) -> StartPipelineExecutionResponseTypeDef:
        """
        Starts a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.start_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start_pipeline_execution)
        """
    def stop_auto_ml_job(self, *, AutoMLJobName: str) -> None:
        """
        A method for forcing a running job to shut down.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_auto_ml_job)
        """
    def stop_compilation_job(self, *, CompilationJobName: str) -> None:
        """
        Stops a model compilation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_compilation_job)
        """
    def stop_edge_deployment_stage(self, *, EdgeDeploymentPlanName: str, StageName: str) -> None:
        """
        Stops a stage in an edge deployment plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_edge_deployment_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_edge_deployment_stage)
        """
    def stop_edge_packaging_job(self, *, EdgePackagingJobName: str) -> None:
        """
        Request to stop an edge packaging job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_edge_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_edge_packaging_job)
        """
    def stop_hyper_parameter_tuning_job(self, *, HyperParameterTuningJobName: str) -> None:
        """
        Stops a running hyperparameter tuning job and all running training jobs that the
        tuning job launched.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_hyper_parameter_tuning_job)
        """
    def stop_inference_experiment(
        self,
        *,
        Name: str,
        ModelVariantActions: Dict[str, ModelVariantActionType],
        DesiredModelVariants: List["ModelVariantConfigTypeDef"] = None,
        DesiredState: InferenceExperimentStopDesiredStateType = None,
        Reason: str = None
    ) -> StopInferenceExperimentResponseTypeDef:
        """
        Stops an inference experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_inference_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_inference_experiment)
        """
    def stop_inference_recommendations_job(self, *, JobName: str) -> None:
        """
        Stops an Inference Recommender job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_inference_recommendations_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_inference_recommendations_job)
        """
    def stop_labeling_job(self, *, LabelingJobName: str) -> None:
        """
        Stops a running labeling job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_labeling_job)
        """
    def stop_monitoring_schedule(self, *, MonitoringScheduleName: str) -> None:
        """
        Stops a previously started monitoring schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_monitoring_schedule)
        """
    def stop_notebook_instance(self, *, NotebookInstanceName: str) -> None:
        """
        Terminates the ML compute instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_notebook_instance)
        """
    def stop_pipeline_execution(
        self, *, PipelineExecutionArn: str, ClientRequestToken: str
    ) -> StopPipelineExecutionResponseTypeDef:
        """
        Stops a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_pipeline_execution)
        """
    def stop_processing_job(self, *, ProcessingJobName: str) -> None:
        """
        Stops a processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_processing_job)
        """
    def stop_training_job(self, *, TrainingJobName: str) -> None:
        """
        Stops a training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_training_job)
        """
    def stop_transform_job(self, *, TransformJobName: str) -> None:
        """
        Stops a batch transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop_transform_job)
        """
    def update_action(
        self,
        *,
        ActionName: str,
        Description: str = None,
        Status: ActionStatusType = None,
        Properties: Dict[str, str] = None,
        PropertiesToRemove: List[str] = None
    ) -> UpdateActionResponseTypeDef:
        """
        Updates an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_action)
        """
    def update_app_image_config(
        self,
        *,
        AppImageConfigName: str,
        KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None
    ) -> UpdateAppImageConfigResponseTypeDef:
        """
        Updates the properties of an AppImageConfig.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_app_image_config)
        """
    def update_artifact(
        self,
        *,
        ArtifactArn: str,
        ArtifactName: str = None,
        Properties: Dict[str, str] = None,
        PropertiesToRemove: List[str] = None
    ) -> UpdateArtifactResponseTypeDef:
        """
        Updates an artifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_artifact)
        """
    def update_code_repository(
        self, *, CodeRepositoryName: str, GitConfig: "GitConfigForUpdateTypeDef" = None
    ) -> UpdateCodeRepositoryOutputTypeDef:
        """
        Updates the specified Git repository with the specified values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_code_repository)
        """
    def update_context(
        self,
        *,
        ContextName: str,
        Description: str = None,
        Properties: Dict[str, str] = None,
        PropertiesToRemove: List[str] = None
    ) -> UpdateContextResponseTypeDef:
        """
        Updates a context.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_context)
        """
    def update_device_fleet(
        self,
        *,
        DeviceFleetName: str,
        OutputConfig: "EdgeOutputConfigTypeDef",
        RoleArn: str = None,
        Description: str = None,
        EnableIotRoleAlias: bool = None
    ) -> None:
        """
        Updates a fleet of devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_device_fleet)
        """
    def update_devices(self, *, DeviceFleetName: str, Devices: List["DeviceTypeDef"]) -> None:
        """
        Updates one or more devices in a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_devices)
        """
    def update_domain(
        self,
        *,
        DomainId: str,
        DefaultUserSettings: "UserSettingsTypeDef" = None,
        DomainSettingsForUpdate: "DomainSettingsForUpdateTypeDef" = None,
        DefaultSpaceSettings: "DefaultSpaceSettingsTypeDef" = None,
        AppSecurityGroupManagement: AppSecurityGroupManagementType = None
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the default settings for new user profiles in the domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_domain)
        """
    def update_endpoint(
        self,
        *,
        EndpointName: str,
        EndpointConfigName: str,
        RetainAllVariantProperties: bool = None,
        ExcludeRetainedVariantProperties: List["VariantPropertyTypeDef"] = None,
        DeploymentConfig: "DeploymentConfigTypeDef" = None,
        RetainDeploymentConfig: bool = None
    ) -> UpdateEndpointOutputTypeDef:
        """
        Deploys the new `EndpointConfig` specified in the request, switches to using
        newly created endpoint, and then deletes resources provisioned for the endpoint
        using the previous `EndpointConfig` (there is no availability loss).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_endpoint)
        """
    def update_endpoint_weights_and_capacities(
        self,
        *,
        EndpointName: str,
        DesiredWeightsAndCapacities: List["DesiredWeightAndCapacityTypeDef"]
    ) -> UpdateEndpointWeightsAndCapacitiesOutputTypeDef:
        """
        Updates variant weight of one or more variants associated with an existing
        endpoint, or capacity of one variant associated with an existing endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_endpoint_weights_and_capacities)
        """
    def update_experiment(
        self, *, ExperimentName: str, DisplayName: str = None, Description: str = None
    ) -> UpdateExperimentResponseTypeDef:
        """
        Adds, updates, or removes the description of an experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_experiment)
        """
    def update_feature_group(
        self,
        *,
        FeatureGroupName: str,
        FeatureAdditions: List["FeatureDefinitionTypeDef"] = None,
        OnlineStoreConfig: "OnlineStoreConfigUpdateTypeDef" = None
    ) -> UpdateFeatureGroupResponseTypeDef:
        """
        Updates the feature group by either adding features or updating the online store
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_feature_group)
        """
    def update_feature_metadata(
        self,
        *,
        FeatureGroupName: str,
        FeatureName: str,
        Description: str = None,
        ParameterAdditions: List["FeatureParameterTypeDef"] = None,
        ParameterRemovals: List[str] = None
    ) -> None:
        """
        Updates the description and parameters of the feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_feature_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_feature_metadata)
        """
    def update_hub(
        self,
        *,
        HubName: str,
        HubDescription: str = None,
        HubDisplayName: str = None,
        HubSearchKeywords: List[str] = None
    ) -> UpdateHubResponseTypeDef:
        """
        Update a hub.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_hub)
        """
    def update_image(
        self,
        *,
        ImageName: str,
        DeleteProperties: List[str] = None,
        Description: str = None,
        DisplayName: str = None,
        RoleArn: str = None
    ) -> UpdateImageResponseTypeDef:
        """
        Updates the properties of a SageMaker image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_image)
        """
    def update_image_version(
        self,
        *,
        ImageName: str,
        Alias: str = None,
        Version: int = None,
        AliasesToAdd: List[str] = None,
        AliasesToDelete: List[str] = None,
        VendorGuidance: VendorGuidanceType = None,
        JobType: JobTypeType = None,
        MLFramework: str = None,
        ProgrammingLang: str = None,
        Processor: ProcessorType = None,
        Horovod: bool = None,
        ReleaseNotes: str = None
    ) -> UpdateImageVersionResponseTypeDef:
        """
        Updates the properties of a SageMaker image version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_image_version)
        """
    def update_inference_experiment(
        self,
        *,
        Name: str,
        Schedule: "InferenceExperimentScheduleTypeDef" = None,
        Description: str = None,
        ModelVariants: List["ModelVariantConfigTypeDef"] = None,
        DataStorageConfig: "InferenceExperimentDataStorageConfigTypeDef" = None,
        ShadowModeConfig: "ShadowModeConfigTypeDef" = None
    ) -> UpdateInferenceExperimentResponseTypeDef:
        """
        Updates an inference experiment that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_inference_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_inference_experiment)
        """
    def update_model_card(
        self,
        *,
        ModelCardName: str,
        Content: str = None,
        ModelCardStatus: ModelCardStatusType = None
    ) -> UpdateModelCardResponseTypeDef:
        """
        Update an Amazon SageMaker Model Card.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_model_card)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_model_card)
        """
    def update_model_package(
        self,
        *,
        ModelPackageArn: str,
        ModelApprovalStatus: ModelApprovalStatusType = None,
        ApprovalDescription: str = None,
        CustomerMetadataProperties: Dict[str, str] = None,
        CustomerMetadataPropertiesToRemove: List[str] = None,
        AdditionalInferenceSpecificationsToAdd: List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ] = None
    ) -> UpdateModelPackageOutputTypeDef:
        """
        Updates a versioned model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_model_package)
        """
    def update_monitoring_alert(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringAlertName: str,
        DatapointsToAlert: int,
        EvaluationPeriod: int
    ) -> UpdateMonitoringAlertResponseTypeDef:
        """
        Update the parameters of a model monitor alert.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_alert)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_monitoring_alert)
        """
    def update_monitoring_schedule(
        self,
        *,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef"
    ) -> UpdateMonitoringScheduleResponseTypeDef:
        """
        Updates a previously created schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_monitoring_schedule)
        """
    def update_notebook_instance(
        self,
        *,
        NotebookInstanceName: str,
        InstanceType: InstanceTypeType = None,
        RoleArn: str = None,
        LifecycleConfigName: str = None,
        DisassociateLifecycleConfig: bool = None,
        VolumeSizeInGB: int = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        AcceleratorTypes: List[NotebookInstanceAcceleratorTypeType] = None,
        DisassociateAcceleratorTypes: bool = None,
        DisassociateDefaultCodeRepository: bool = None,
        DisassociateAdditionalCodeRepositories: bool = None,
        RootAccess: RootAccessType = None,
        InstanceMetadataServiceConfiguration: "InstanceMetadataServiceConfigurationTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates a notebook instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_notebook_instance)
        """
    def update_notebook_instance_lifecycle_config(
        self,
        *,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
        OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates a notebook instance lifecycle configuration created with the
        `CreateNotebookInstanceLifecycleConfig <https://docs.aws.amazon.com/sagemaker/la
        test/APIReference/API_CreateNotebookInstanceLifecycleConfig.html>`__ API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_notebook_instance_lifecycle_config)
        """
    def update_pipeline(
        self,
        *,
        PipelineName: str,
        PipelineDisplayName: str = None,
        PipelineDefinition: str = None,
        PipelineDefinitionS3Location: "PipelineDefinitionS3LocationTypeDef" = None,
        PipelineDescription: str = None,
        RoleArn: str = None,
        ParallelismConfiguration: "ParallelismConfigurationTypeDef" = None
    ) -> UpdatePipelineResponseTypeDef:
        """
        Updates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_pipeline)
        """
    def update_pipeline_execution(
        self,
        *,
        PipelineExecutionArn: str,
        PipelineExecutionDescription: str = None,
        PipelineExecutionDisplayName: str = None,
        ParallelismConfiguration: "ParallelismConfigurationTypeDef" = None
    ) -> UpdatePipelineExecutionResponseTypeDef:
        """
        Updates a pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_pipeline_execution)
        """
    def update_project(
        self,
        *,
        ProjectName: str,
        ProjectDescription: str = None,
        ServiceCatalogProvisioningUpdateDetails: "ServiceCatalogProvisioningUpdateDetailsTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates a machine learning (ML) project that is created from a template that
        sets up an ML pipeline from training to deploying an approved model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_project)
        """
    def update_space(
        self, *, DomainId: str, SpaceName: str, SpaceSettings: "SpaceSettingsTypeDef" = None
    ) -> UpdateSpaceResponseTypeDef:
        """
        Updates the settings of a space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_space)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_space)
        """
    def update_training_job(
        self,
        *,
        TrainingJobName: str,
        ProfilerConfig: "ProfilerConfigForUpdateTypeDef" = None,
        ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"] = None,
        ResourceConfig: "ResourceConfigForUpdateTypeDef" = None
    ) -> UpdateTrainingJobResponseTypeDef:
        """
        Update a model training job to request a new Debugger profiling configuration or
        to change warm pool retention length.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_training_job)
        """
    def update_trial(
        self, *, TrialName: str, DisplayName: str = None
    ) -> UpdateTrialResponseTypeDef:
        """
        Updates the display name of a trial.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_trial)
        """
    def update_trial_component(
        self,
        *,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: "TrialComponentStatusTypeDef" = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
        ParametersToRemove: List[str] = None,
        InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        InputArtifactsToRemove: List[str] = None,
        OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        OutputArtifactsToRemove: List[str] = None
    ) -> UpdateTrialComponentResponseTypeDef:
        """
        Updates one or more properties of a trial component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_trial_component)
        """
    def update_user_profile(
        self, *, DomainId: str, UserProfileName: str, UserSettings: "UserSettingsTypeDef" = None
    ) -> UpdateUserProfileResponseTypeDef:
        """
        Updates a user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_user_profile)
        """
    def update_workforce(
        self,
        *,
        WorkforceName: str,
        SourceIpConfig: "SourceIpConfigTypeDef" = None,
        OidcConfig: "OidcConfigTypeDef" = None,
        WorkforceVpcConfig: "WorkforceVpcConfigRequestTypeDef" = None
    ) -> UpdateWorkforceResponseTypeDef:
        """
        Use this operation to update your workforce.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_workforce)
        """
    def update_workteam(
        self,
        *,
        WorkteamName: str,
        MemberDefinitions: List["MemberDefinitionTypeDef"] = None,
        Description: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None
    ) -> UpdateWorkteamResponseTypeDef:
        """
        Updates an existing work team with new member definitions or description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Client.update_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update_workteam)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_actions"]) -> ListActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListActions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listactionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_algorithms"]) -> ListAlgorithmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listalgorithmspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListAliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listaliasespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_image_configs"]
    ) -> ListAppImageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappimageconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listartifactspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_auto_ml_jobs"]
    ) -> ListAutoMLJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listautomljobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_candidates_for_auto_ml_job"]
    ) -> ListCandidatesForAutoMLJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcandidatesforautomljobpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_repositories"]
    ) -> ListCodeRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcoderepositoriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_compilation_jobs"]
    ) -> ListCompilationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcompilationjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_contexts"]) -> ListContextsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcontextspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_quality_job_definitions"]
    ) -> ListDataQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdataqualityjobdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_fleets"]
    ) -> ListDeviceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicefleetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdomainspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_deployment_plans"]
    ) -> ListEdgeDeploymentPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgeDeploymentPlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgedeploymentplanspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_packaging_jobs"]
    ) -> ListEdgePackagingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgepackagingjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_configs"]
    ) -> ListEndpointConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointconfigspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listexperimentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_feature_groups"]
    ) -> ListFeatureGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listfeaturegroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_definitions"]
    ) -> ListFlowDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listflowdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_human_task_uis"]
    ) -> ListHumanTaskUisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhumantaskuispaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_hyper_parameter_tuning_jobs"]
    ) -> ListHyperParameterTuningJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhyperparametertuningjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_versions"]
    ) -> ListImageVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimageversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimagespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_experiments"]
    ) -> ListInferenceExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceExperiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferenceexperimentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_recommendations_job_steps"]
    ) -> ListInferenceRecommendationsJobStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceRecommendationsJobSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencerecommendationsjobstepspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_inference_recommendations_jobs"]
    ) -> ListInferenceRecommendationsJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListInferenceRecommendationsJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listinferencerecommendationsjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs"]
    ) -> ListLabelingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs_for_workteam"]
    ) -> ListLabelingJobsForWorkteamPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobsforworkteampaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_lineage_groups"]
    ) -> ListLineageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListLineageGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlineagegroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_bias_job_definitions"]
    ) -> ListModelBiasJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelbiasjobdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_card_export_jobs"]
    ) -> ListModelCardExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCardExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardexportjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_card_versions"]
    ) -> ListModelCardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCardVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_model_cards"]) -> ListModelCardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelCards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelcardspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_explainability_job_definitions"]
    ) -> ListModelExplainabilityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelexplainabilityjobdefinitionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_metadata"]
    ) -> ListModelMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelMetadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelmetadatapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_package_groups"]
    ) -> ListModelPackageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagegroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packages"]
    ) -> ListModelPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_quality_job_definitions"]
    ) -> ListModelQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelqualityjobdefinitionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_alert_history"]
    ) -> ListMonitoringAlertHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringAlertHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringalerthistorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_alerts"]
    ) -> ListMonitoringAlertsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringAlerts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringalertspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_executions"]
    ) -> ListMonitoringExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_schedules"]
    ) -> ListMonitoringSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringschedulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instance_lifecycle_configs"]
    ) -> ListNotebookInstanceLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancelifecycleconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instances"]
    ) -> ListNotebookInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_execution_steps"]
    ) -> ListPipelineExecutionStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionstepspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_parameters_for_execution"]
    ) -> ListPipelineParametersForExecutionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineparametersforexecutionpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelinespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_processing_jobs"]
    ) -> ListProcessingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listprocessingjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_catalogs"]
    ) -> ListResourceCatalogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListResourceCatalogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listresourcecatalogspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_spaces"]) -> ListSpacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListSpaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listspacespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stage_devices"]
    ) -> ListStageDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListStageDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#liststagedevicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_lifecycle_configs"]
    ) -> ListStudioLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListStudioLifecycleConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#liststudiolifecycleconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_workteams"]
    ) -> ListSubscribedWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listsubscribedworkteamspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtagspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs"]
    ) -> ListTrainingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs_for_hyper_parameter_tuning_job"]
    ) -> ListTrainingJobsForHyperParameterTuningJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobsforhyperparametertuningjobpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_transform_jobs"]
    ) -> ListTransformJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtransformjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_trial_components"]
    ) -> ListTrialComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialcomponentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_trials"]) -> ListTrialsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listuserprofilespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workforces"]) -> ListWorkforcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkforcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workteams"]) -> ListWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkteamspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Paginator.Search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#searchpaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.EndpointDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#endpointdeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_in_service"]) -> EndpointInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.EndpointInService)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#endpointinservicewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["image_created"]) -> ImageCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.ImageCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#imagecreatedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["image_deleted"]) -> ImageDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.ImageDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#imagedeletedwaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["image_updated"]) -> ImageUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.ImageUpdated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#imageupdatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["image_version_created"]
    ) -> ImageVersionCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.ImageVersionCreated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#imageversioncreatedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["image_version_deleted"]
    ) -> ImageVersionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.ImageVersionDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#imageversiondeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_deleted"]
    ) -> NotebookInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#notebookinstancedeletedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_in_service"]
    ) -> NotebookInstanceInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceInService)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#notebookinstanceinservicewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_stopped"]
    ) -> NotebookInstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.NotebookInstanceStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#notebookinstancestoppedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["processing_job_completed_or_stopped"]
    ) -> ProcessingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.ProcessingJobCompletedOrStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#processingjobcompletedorstoppedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["training_job_completed_or_stopped"]
    ) -> TrainingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.TrainingJobCompletedOrStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#trainingjobcompletedorstoppedwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["transform_job_completed_or_stopped"]
    ) -> TransformJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/sagemaker.html#SageMaker.Waiter.TransformJobCompletedOrStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#transformjobcompletedorstoppedwaiter)
        """
