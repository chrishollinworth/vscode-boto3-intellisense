"""
Type annotations for sagemaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker.type_defs import ActionSourceTypeDef

    data: ActionSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionStatusType,
    AggregationTransformationValueType,
    AlgorithmSortByType,
    AlgorithmStatusType,
    AppImageConfigSortKeyType,
    AppInstanceTypeType,
    AppNetworkAccessTypeType,
    AppSecurityGroupManagementType,
    AppStatusType,
    AppTypeType,
    ArtifactSourceIdTypeType,
    AssemblyTypeType,
    AssociationEdgeTypeType,
    AsyncNotificationTopicTypesType,
    AthenaResultCompressionTypeType,
    AthenaResultFormatType,
    AuthModeType,
    AutoMLAlgorithmType,
    AutoMLChannelTypeType,
    AutoMLJobObjectiveTypeType,
    AutoMLJobSecondaryStatusType,
    AutoMLJobStatusType,
    AutoMLMetricEnumType,
    AutoMLMetricExtendedEnumType,
    AutoMLModeType,
    AutoMLProblemTypeConfigNameType,
    AutoMLProcessingUnitType,
    AutoMLS3DataTypeType,
    AutoMLSortByType,
    AutoMLSortOrderType,
    AwsManagedHumanLoopRequestSourceType,
    BatchStrategyType,
    BooleanOperatorType,
    CandidateSortByType,
    CandidateStatusType,
    CandidateStepTypeType,
    CapacitySizeTypeType,
    CaptureModeType,
    CaptureStatusType,
    ClarifyFeatureTypeType,
    ClarifyTextGranularityType,
    ClarifyTextLanguageType,
    CodeRepositorySortByType,
    CodeRepositorySortOrderType,
    CollectionTypeType,
    CompilationJobStatusType,
    CompleteOnConvergenceType,
    CompressionTypeType,
    ConditionOutcomeType,
    ContainerModeType,
    ContentClassifierType,
    CrossAccountFilterOptionType,
    DataDistributionTypeType,
    DataSourceNameType,
    DetailedAlgorithmStatusType,
    DetailedModelPackageStatusType,
    DeviceDeploymentStatusType,
    DeviceSubsetTypeType,
    DirectInternetAccessType,
    DirectionType,
    DomainStatusType,
    EdgePackagingJobStatusType,
    EdgePresetDeploymentStatusType,
    EndpointConfigSortKeyType,
    EndpointSortKeyType,
    EndpointStatusType,
    ExecutionRoleIdentityConfigType,
    ExecutionStatusType,
    FailureHandlingPolicyType,
    FeatureGroupSortByType,
    FeatureGroupSortOrderType,
    FeatureGroupStatusType,
    FeatureStatusType,
    FeatureTypeType,
    FileSystemAccessModeType,
    FileSystemTypeType,
    FillingTypeType,
    FlatInvocationsType,
    FlowDefinitionStatusType,
    FrameworkType,
    HubContentSortByType,
    HubContentStatusType,
    HubContentTypeType,
    HubSortByType,
    HubStatusType,
    HumanTaskUiStatusType,
    HyperParameterScalingTypeType,
    HyperParameterTuningJobObjectiveTypeType,
    HyperParameterTuningJobSortByOptionsType,
    HyperParameterTuningJobStatusType,
    HyperParameterTuningJobStrategyTypeType,
    HyperParameterTuningJobWarmStartTypeType,
    ImageSortByType,
    ImageSortOrderType,
    ImageStatusType,
    ImageVersionSortByType,
    ImageVersionSortOrderType,
    ImageVersionStatusType,
    InferenceExecutionModeType,
    InferenceExperimentStatusType,
    InferenceExperimentStopDesiredStateType,
    InputModeType,
    InstanceTypeType,
    JobTypeType,
    JoinSourceType,
    LabelingJobStatusType,
    LastUpdateStatusValueType,
    LineageTypeType,
    ListCompilationJobsSortByType,
    ListDeviceFleetsSortByType,
    ListEdgeDeploymentPlansSortByType,
    ListEdgePackagingJobsSortByType,
    ListInferenceRecommendationsJobsSortByType,
    ListWorkforcesSortByOptionsType,
    ListWorkteamsSortByOptionsType,
    MetricSetSourceType,
    ModelApprovalStatusType,
    ModelCacheSettingType,
    ModelCardExportJobSortByType,
    ModelCardExportJobSortOrderType,
    ModelCardExportJobStatusType,
    ModelCardProcessingStatusType,
    ModelCardSortByType,
    ModelCardSortOrderType,
    ModelCardStatusType,
    ModelCompressionTypeType,
    ModelMetadataFilterTypeType,
    ModelPackageGroupSortByType,
    ModelPackageGroupStatusType,
    ModelPackageSortByType,
    ModelPackageStatusType,
    ModelPackageTypeType,
    ModelSortKeyType,
    ModelVariantActionType,
    ModelVariantStatusType,
    MonitoringAlertHistorySortKeyType,
    MonitoringAlertStatusType,
    MonitoringExecutionSortKeyType,
    MonitoringJobDefinitionSortKeyType,
    MonitoringProblemTypeType,
    MonitoringScheduleSortKeyType,
    MonitoringTypeType,
    NotebookInstanceAcceleratorTypeType,
    NotebookInstanceLifecycleConfigSortKeyType,
    NotebookInstanceLifecycleConfigSortOrderType,
    NotebookInstanceSortKeyType,
    NotebookInstanceSortOrderType,
    NotebookInstanceStatusType,
    NotebookOutputOptionType,
    ObjectiveStatusType,
    OfflineStoreStatusValueType,
    OperatorType,
    OrderKeyType,
    OutputCompressionTypeType,
    ParameterTypeType,
    PipelineExecutionStatusType,
    ProblemTypeType,
    ProcessingInstanceTypeType,
    ProcessingJobStatusType,
    ProcessingS3CompressionTypeType,
    ProcessingS3DataDistributionTypeType,
    ProcessingS3DataTypeType,
    ProcessingS3InputModeType,
    ProcessingS3UploadModeType,
    ProcessorType,
    ProductionVariantAcceleratorTypeType,
    ProductionVariantInstanceTypeType,
    ProfilingStatusType,
    ProjectSortByType,
    ProjectSortOrderType,
    ProjectStatusType,
    RecommendationJobStatusType,
    RecommendationJobSupportedEndpointTypeType,
    RecommendationJobTypeType,
    RecommendationStatusType,
    RecordWrapperType,
    RedshiftResultCompressionTypeType,
    RedshiftResultFormatType,
    RepositoryAccessModeType,
    ResourceCatalogSortOrderType,
    ResourceTypeType,
    RetentionTypeType,
    RootAccessType,
    RStudioServerProAccessStatusType,
    RStudioServerProUserGroupType,
    RuleEvaluationStatusType,
    S3DataDistributionType,
    S3DataTypeType,
    S3ModelDataTypeType,
    SagemakerServicecatalogStatusType,
    ScheduleStatusType,
    SearchSortOrderType,
    SecondaryStatusType,
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
    SpaceStatusType,
    SplitTypeType,
    StageStatusType,
    StatisticType,
    StepStatusType,
    StorageTypeType,
    StudioLifecycleConfigAppTypeType,
    StudioLifecycleConfigSortKeyType,
    TableFormatType,
    TargetDeviceType,
    TargetPlatformAcceleratorType,
    TargetPlatformArchType,
    TargetPlatformOsType,
    TrafficRoutingConfigTypeType,
    TrafficTypeType,
    TrainingInputModeType,
    TrainingInstanceTypeType,
    TrainingJobEarlyStoppingTypeType,
    TrainingJobSortByOptionsType,
    TrainingJobStatusType,
    TrainingRepositoryAccessModeType,
    TransformInstanceTypeType,
    TransformJobStatusType,
    TrialComponentPrimaryStatusType,
    TtlDurationUnitType,
    UserProfileSortKeyType,
    UserProfileStatusType,
    VariantPropertyTypeType,
    VariantStatusType,
    VendorGuidanceType,
    WarmPoolResourceStatusType,
    WorkforceStatusType,
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
    "ActionSourceTypeDef",
    "ActionSummaryTypeDef",
    "AddAssociationRequestRequestTypeDef",
    "AddAssociationResponseTypeDef",
    "AddTagsInputRequestTypeDef",
    "AddTagsOutputTypeDef",
    "AdditionalInferenceSpecificationDefinitionTypeDef",
    "AdditionalS3DataSourceTypeDef",
    "AgentVersionTypeDef",
    "AlarmTypeDef",
    "AlgorithmSpecificationTypeDef",
    "AlgorithmStatusDetailsTypeDef",
    "AlgorithmStatusItemTypeDef",
    "AlgorithmSummaryTypeDef",
    "AlgorithmValidationProfileTypeDef",
    "AlgorithmValidationSpecificationTypeDef",
    "AnnotationConsolidationConfigTypeDef",
    "AppDetailsTypeDef",
    "AppImageConfigDetailsTypeDef",
    "AppSpecificationTypeDef",
    "ArtifactSourceTypeDef",
    "ArtifactSourceTypeTypeDef",
    "ArtifactSummaryTypeDef",
    "AssociateTrialComponentRequestRequestTypeDef",
    "AssociateTrialComponentResponseTypeDef",
    "AssociationSummaryTypeDef",
    "AsyncInferenceClientConfigTypeDef",
    "AsyncInferenceConfigTypeDef",
    "AsyncInferenceNotificationConfigTypeDef",
    "AsyncInferenceOutputConfigTypeDef",
    "AthenaDatasetDefinitionTypeDef",
    "AutoMLAlgorithmConfigTypeDef",
    "AutoMLCandidateGenerationConfigTypeDef",
    "AutoMLCandidateStepTypeDef",
    "AutoMLCandidateTypeDef",
    "AutoMLChannelTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "AutoMLDataSourceTypeDef",
    "AutoMLDataSplitConfigTypeDef",
    "AutoMLJobArtifactsTypeDef",
    "AutoMLJobChannelTypeDef",
    "AutoMLJobCompletionCriteriaTypeDef",
    "AutoMLJobConfigTypeDef",
    "AutoMLJobObjectiveTypeDef",
    "AutoMLJobStepMetadataTypeDef",
    "AutoMLJobSummaryTypeDef",
    "AutoMLOutputDataConfigTypeDef",
    "AutoMLPartialFailureReasonTypeDef",
    "AutoMLProblemTypeConfigTypeDef",
    "AutoMLProblemTypeResolvedAttributesTypeDef",
    "AutoMLResolvedAttributesTypeDef",
    "AutoMLS3DataSourceTypeDef",
    "AutoMLSecurityConfigTypeDef",
    "AutoParameterTypeDef",
    "AutoRollbackConfigTypeDef",
    "AutotuneTypeDef",
    "BatchDataCaptureConfigTypeDef",
    "BatchDescribeModelPackageErrorTypeDef",
    "BatchDescribeModelPackageInputRequestTypeDef",
    "BatchDescribeModelPackageOutputTypeDef",
    "BatchDescribeModelPackageSummaryTypeDef",
    "BatchTransformInputTypeDef",
    "BestObjectiveNotImprovingTypeDef",
    "BiasTypeDef",
    "BlueGreenUpdatePolicyTypeDef",
    "CacheHitResultTypeDef",
    "CallbackStepMetadataTypeDef",
    "CandidateArtifactLocationsTypeDef",
    "CandidateGenerationConfigTypeDef",
    "CandidatePropertiesTypeDef",
    "CanvasAppSettingsTypeDef",
    "CapacitySizeTypeDef",
    "CaptureContentTypeHeaderTypeDef",
    "CaptureOptionTypeDef",
    "CategoricalParameterRangeSpecificationTypeDef",
    "CategoricalParameterRangeTypeDef",
    "CategoricalParameterTypeDef",
    "ChannelSpecificationTypeDef",
    "ChannelTypeDef",
    "CheckpointConfigTypeDef",
    "ClarifyCheckStepMetadataTypeDef",
    "ClarifyExplainerConfigTypeDef",
    "ClarifyInferenceConfigTypeDef",
    "ClarifyShapBaselineConfigTypeDef",
    "ClarifyShapConfigTypeDef",
    "ClarifyTextConfigTypeDef",
    "CodeRepositorySummaryTypeDef",
    "CodeRepositoryTypeDef",
    "CognitoConfigTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "CollectionConfigTypeDef",
    "CollectionConfigurationTypeDef",
    "CompilationJobSummaryTypeDef",
    "ConditionStepMetadataTypeDef",
    "ContainerDefinitionTypeDef",
    "ContextSourceTypeDef",
    "ContextSummaryTypeDef",
    "ContinuousParameterRangeSpecificationTypeDef",
    "ContinuousParameterRangeTypeDef",
    "ConvergenceDetectedTypeDef",
    "CreateActionRequestRequestTypeDef",
    "CreateActionResponseTypeDef",
    "CreateAlgorithmInputRequestTypeDef",
    "CreateAlgorithmOutputTypeDef",
    "CreateAppImageConfigRequestRequestTypeDef",
    "CreateAppImageConfigResponseTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateArtifactRequestRequestTypeDef",
    "CreateArtifactResponseTypeDef",
    "CreateAutoMLJobRequestRequestTypeDef",
    "CreateAutoMLJobResponseTypeDef",
    "CreateAutoMLJobV2RequestRequestTypeDef",
    "CreateAutoMLJobV2ResponseTypeDef",
    "CreateCodeRepositoryInputRequestTypeDef",
    "CreateCodeRepositoryOutputTypeDef",
    "CreateCompilationJobRequestRequestTypeDef",
    "CreateCompilationJobResponseTypeDef",
    "CreateContextRequestRequestTypeDef",
    "CreateContextResponseTypeDef",
    "CreateDataQualityJobDefinitionRequestRequestTypeDef",
    "CreateDataQualityJobDefinitionResponseTypeDef",
    "CreateDeviceFleetRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEdgeDeploymentPlanRequestRequestTypeDef",
    "CreateEdgeDeploymentPlanResponseTypeDef",
    "CreateEdgeDeploymentStageRequestRequestTypeDef",
    "CreateEdgePackagingJobRequestRequestTypeDef",
    "CreateEndpointConfigInputRequestTypeDef",
    "CreateEndpointConfigOutputTypeDef",
    "CreateEndpointInputRequestTypeDef",
    "CreateEndpointOutputTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFeatureGroupRequestRequestTypeDef",
    "CreateFeatureGroupResponseTypeDef",
    "CreateFlowDefinitionRequestRequestTypeDef",
    "CreateFlowDefinitionResponseTypeDef",
    "CreateHubRequestRequestTypeDef",
    "CreateHubResponseTypeDef",
    "CreateHumanTaskUiRequestRequestTypeDef",
    "CreateHumanTaskUiResponseTypeDef",
    "CreateHyperParameterTuningJobRequestRequestTypeDef",
    "CreateHyperParameterTuningJobResponseTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateImageResponseTypeDef",
    "CreateImageVersionRequestRequestTypeDef",
    "CreateImageVersionResponseTypeDef",
    "CreateInferenceExperimentRequestRequestTypeDef",
    "CreateInferenceExperimentResponseTypeDef",
    "CreateInferenceRecommendationsJobRequestRequestTypeDef",
    "CreateInferenceRecommendationsJobResponseTypeDef",
    "CreateLabelingJobRequestRequestTypeDef",
    "CreateLabelingJobResponseTypeDef",
    "CreateModelBiasJobDefinitionRequestRequestTypeDef",
    "CreateModelBiasJobDefinitionResponseTypeDef",
    "CreateModelCardExportJobRequestRequestTypeDef",
    "CreateModelCardExportJobResponseTypeDef",
    "CreateModelCardRequestRequestTypeDef",
    "CreateModelCardResponseTypeDef",
    "CreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    "CreateModelInputRequestTypeDef",
    "CreateModelOutputTypeDef",
    "CreateModelPackageGroupInputRequestTypeDef",
    "CreateModelPackageGroupOutputTypeDef",
    "CreateModelPackageInputRequestTypeDef",
    "CreateModelPackageOutputTypeDef",
    "CreateModelQualityJobDefinitionRequestRequestTypeDef",
    "CreateModelQualityJobDefinitionResponseTypeDef",
    "CreateMonitoringScheduleRequestRequestTypeDef",
    "CreateMonitoringScheduleResponseTypeDef",
    "CreateNotebookInstanceInputRequestTypeDef",
    "CreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    "CreateNotebookInstanceOutputTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "CreatePresignedDomainUrlRequestRequestTypeDef",
    "CreatePresignedDomainUrlResponseTypeDef",
    "CreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    "CreateProcessingJobRequestRequestTypeDef",
    "CreateProcessingJobResponseTypeDef",
    "CreateProjectInputRequestTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateSpaceRequestRequestTypeDef",
    "CreateSpaceResponseTypeDef",
    "CreateStudioLifecycleConfigRequestRequestTypeDef",
    "CreateStudioLifecycleConfigResponseTypeDef",
    "CreateTrainingJobRequestRequestTypeDef",
    "CreateTrainingJobResponseTypeDef",
    "CreateTransformJobRequestRequestTypeDef",
    "CreateTransformJobResponseTypeDef",
    "CreateTrialComponentRequestRequestTypeDef",
    "CreateTrialComponentResponseTypeDef",
    "CreateTrialRequestRequestTypeDef",
    "CreateTrialResponseTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "CreateUserProfileResponseTypeDef",
    "CreateWorkforceRequestRequestTypeDef",
    "CreateWorkforceResponseTypeDef",
    "CreateWorkteamRequestRequestTypeDef",
    "CreateWorkteamResponseTypeDef",
    "CustomImageTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DataCaptureConfigSummaryTypeDef",
    "DataCaptureConfigTypeDef",
    "DataCatalogConfigTypeDef",
    "DataProcessingTypeDef",
    "DataQualityAppSpecificationTypeDef",
    "DataQualityBaselineConfigTypeDef",
    "DataQualityJobInputTypeDef",
    "DataSourceTypeDef",
    "DatasetDefinitionTypeDef",
    "DebugHookConfigTypeDef",
    "DebugRuleConfigurationTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "DefaultSpaceSettingsTypeDef",
    "DeleteActionRequestRequestTypeDef",
    "DeleteActionResponseTypeDef",
    "DeleteAlgorithmInputRequestTypeDef",
    "DeleteAppImageConfigRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteArtifactRequestRequestTypeDef",
    "DeleteArtifactResponseTypeDef",
    "DeleteAssociationRequestRequestTypeDef",
    "DeleteAssociationResponseTypeDef",
    "DeleteCodeRepositoryInputRequestTypeDef",
    "DeleteContextRequestRequestTypeDef",
    "DeleteContextResponseTypeDef",
    "DeleteDataQualityJobDefinitionRequestRequestTypeDef",
    "DeleteDeviceFleetRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteEdgeDeploymentPlanRequestRequestTypeDef",
    "DeleteEdgeDeploymentStageRequestRequestTypeDef",
    "DeleteEndpointConfigInputRequestTypeDef",
    "DeleteEndpointInputRequestTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteExperimentResponseTypeDef",
    "DeleteFeatureGroupRequestRequestTypeDef",
    "DeleteFlowDefinitionRequestRequestTypeDef",
    "DeleteHubContentRequestRequestTypeDef",
    "DeleteHubRequestRequestTypeDef",
    "DeleteHumanTaskUiRequestRequestTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageVersionRequestRequestTypeDef",
    "DeleteInferenceExperimentRequestRequestTypeDef",
    "DeleteInferenceExperimentResponseTypeDef",
    "DeleteModelBiasJobDefinitionRequestRequestTypeDef",
    "DeleteModelCardRequestRequestTypeDef",
    "DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "DeleteModelInputRequestTypeDef",
    "DeleteModelPackageGroupInputRequestTypeDef",
    "DeleteModelPackageGroupPolicyInputRequestTypeDef",
    "DeleteModelPackageInputRequestTypeDef",
    "DeleteModelQualityJobDefinitionRequestRequestTypeDef",
    "DeleteMonitoringScheduleRequestRequestTypeDef",
    "DeleteNotebookInstanceInputRequestTypeDef",
    "DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeletePipelineResponseTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteSpaceRequestRequestTypeDef",
    "DeleteStudioLifecycleConfigRequestRequestTypeDef",
    "DeleteTagsInputRequestTypeDef",
    "DeleteTrialComponentRequestRequestTypeDef",
    "DeleteTrialComponentResponseTypeDef",
    "DeleteTrialRequestRequestTypeDef",
    "DeleteTrialResponseTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeleteWorkforceRequestRequestTypeDef",
    "DeleteWorkteamRequestRequestTypeDef",
    "DeleteWorkteamResponseTypeDef",
    "DeployedImageTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentRecommendationTypeDef",
    "DeploymentStageStatusSummaryTypeDef",
    "DeploymentStageTypeDef",
    "DeregisterDevicesRequestRequestTypeDef",
    "DerivedInformationTypeDef",
    "DescribeActionRequestRequestTypeDef",
    "DescribeActionResponseTypeDef",
    "DescribeAlgorithmInputRequestTypeDef",
    "DescribeAlgorithmOutputTypeDef",
    "DescribeAppImageConfigRequestRequestTypeDef",
    "DescribeAppImageConfigResponseTypeDef",
    "DescribeAppRequestRequestTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeArtifactRequestRequestTypeDef",
    "DescribeArtifactResponseTypeDef",
    "DescribeAutoMLJobRequestRequestTypeDef",
    "DescribeAutoMLJobResponseTypeDef",
    "DescribeAutoMLJobV2RequestRequestTypeDef",
    "DescribeAutoMLJobV2ResponseTypeDef",
    "DescribeCodeRepositoryInputRequestTypeDef",
    "DescribeCodeRepositoryOutputTypeDef",
    "DescribeCompilationJobRequestRequestTypeDef",
    "DescribeCompilationJobResponseTypeDef",
    "DescribeContextRequestRequestTypeDef",
    "DescribeContextResponseTypeDef",
    "DescribeDataQualityJobDefinitionRequestRequestTypeDef",
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    "DescribeDeviceFleetRequestRequestTypeDef",
    "DescribeDeviceFleetResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeEdgeDeploymentPlanRequestRequestTypeDef",
    "DescribeEdgeDeploymentPlanResponseTypeDef",
    "DescribeEdgePackagingJobRequestRequestTypeDef",
    "DescribeEdgePackagingJobResponseTypeDef",
    "DescribeEndpointConfigInputRequestTypeDef",
    "DescribeEndpointConfigOutputTypeDef",
    "DescribeEndpointInputRequestTypeDef",
    "DescribeEndpointOutputTypeDef",
    "DescribeExperimentRequestRequestTypeDef",
    "DescribeExperimentResponseTypeDef",
    "DescribeFeatureGroupRequestRequestTypeDef",
    "DescribeFeatureGroupResponseTypeDef",
    "DescribeFeatureMetadataRequestRequestTypeDef",
    "DescribeFeatureMetadataResponseTypeDef",
    "DescribeFlowDefinitionRequestRequestTypeDef",
    "DescribeFlowDefinitionResponseTypeDef",
    "DescribeHubContentRequestRequestTypeDef",
    "DescribeHubContentResponseTypeDef",
    "DescribeHubRequestRequestTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeHumanTaskUiRequestRequestTypeDef",
    "DescribeHumanTaskUiResponseTypeDef",
    "DescribeHyperParameterTuningJobRequestRequestTypeDef",
    "DescribeHyperParameterTuningJobResponseTypeDef",
    "DescribeImageRequestRequestTypeDef",
    "DescribeImageResponseTypeDef",
    "DescribeImageVersionRequestRequestTypeDef",
    "DescribeImageVersionResponseTypeDef",
    "DescribeInferenceExperimentRequestRequestTypeDef",
    "DescribeInferenceExperimentResponseTypeDef",
    "DescribeInferenceRecommendationsJobRequestRequestTypeDef",
    "DescribeInferenceRecommendationsJobResponseTypeDef",
    "DescribeLabelingJobRequestRequestTypeDef",
    "DescribeLabelingJobResponseTypeDef",
    "DescribeLineageGroupRequestRequestTypeDef",
    "DescribeLineageGroupResponseTypeDef",
    "DescribeModelBiasJobDefinitionRequestRequestTypeDef",
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    "DescribeModelCardExportJobRequestRequestTypeDef",
    "DescribeModelCardExportJobResponseTypeDef",
    "DescribeModelCardRequestRequestTypeDef",
    "DescribeModelCardResponseTypeDef",
    "DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef",
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    "DescribeModelInputRequestTypeDef",
    "DescribeModelOutputTypeDef",
    "DescribeModelPackageGroupInputRequestTypeDef",
    "DescribeModelPackageGroupOutputTypeDef",
    "DescribeModelPackageInputRequestTypeDef",
    "DescribeModelPackageOutputTypeDef",
    "DescribeModelQualityJobDefinitionRequestRequestTypeDef",
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    "DescribeMonitoringScheduleRequestRequestTypeDef",
    "DescribeMonitoringScheduleResponseTypeDef",
    "DescribeNotebookInstanceInputRequestTypeDef",
    "DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    "DescribeNotebookInstanceOutputTypeDef",
    "DescribePipelineDefinitionForExecutionRequestRequestTypeDef",
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    "DescribePipelineExecutionRequestRequestTypeDef",
    "DescribePipelineExecutionResponseTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DescribePipelineResponseTypeDef",
    "DescribeProcessingJobRequestRequestTypeDef",
    "DescribeProcessingJobResponseTypeDef",
    "DescribeProjectInputRequestTypeDef",
    "DescribeProjectOutputTypeDef",
    "DescribeSpaceRequestRequestTypeDef",
    "DescribeSpaceResponseTypeDef",
    "DescribeStudioLifecycleConfigRequestRequestTypeDef",
    "DescribeStudioLifecycleConfigResponseTypeDef",
    "DescribeSubscribedWorkteamRequestRequestTypeDef",
    "DescribeSubscribedWorkteamResponseTypeDef",
    "DescribeTrainingJobRequestRequestTypeDef",
    "DescribeTrainingJobResponseTypeDef",
    "DescribeTransformJobRequestRequestTypeDef",
    "DescribeTransformJobResponseTypeDef",
    "DescribeTrialComponentRequestRequestTypeDef",
    "DescribeTrialComponentResponseTypeDef",
    "DescribeTrialRequestRequestTypeDef",
    "DescribeTrialResponseTypeDef",
    "DescribeUserProfileRequestRequestTypeDef",
    "DescribeUserProfileResponseTypeDef",
    "DescribeWorkforceRequestRequestTypeDef",
    "DescribeWorkforceResponseTypeDef",
    "DescribeWorkteamRequestRequestTypeDef",
    "DescribeWorkteamResponseTypeDef",
    "DesiredWeightAndCapacityTypeDef",
    "DeviceDeploymentSummaryTypeDef",
    "DeviceFleetSummaryTypeDef",
    "DeviceSelectionConfigTypeDef",
    "DeviceStatsTypeDef",
    "DeviceSummaryTypeDef",
    "DeviceTypeDef",
    "DirectDeploySettingsTypeDef",
    "DisassociateTrialComponentRequestRequestTypeDef",
    "DisassociateTrialComponentResponseTypeDef",
    "DomainDetailsTypeDef",
    "DomainSettingsForUpdateTypeDef",
    "DomainSettingsTypeDef",
    "DriftCheckBaselinesTypeDef",
    "DriftCheckBiasTypeDef",
    "DriftCheckExplainabilityTypeDef",
    "DriftCheckModelDataQualityTypeDef",
    "DriftCheckModelQualityTypeDef",
    "DynamicScalingConfigurationTypeDef",
    "EMRStepMetadataTypeDef",
    "EdgeDeploymentConfigTypeDef",
    "EdgeDeploymentModelConfigTypeDef",
    "EdgeDeploymentPlanSummaryTypeDef",
    "EdgeDeploymentStatusTypeDef",
    "EdgeModelStatTypeDef",
    "EdgeModelSummaryTypeDef",
    "EdgeModelTypeDef",
    "EdgeOutputConfigTypeDef",
    "EdgePackagingJobSummaryTypeDef",
    "EdgePresetDeploymentOutputTypeDef",
    "EdgeTypeDef",
    "EndpointConfigSummaryTypeDef",
    "EndpointInfoTypeDef",
    "EndpointInputConfigurationTypeDef",
    "EndpointInputTypeDef",
    "EndpointMetadataTypeDef",
    "EndpointOutputConfigurationTypeDef",
    "EndpointPerformanceTypeDef",
    "EndpointSummaryTypeDef",
    "EndpointTypeDef",
    "EnvironmentParameterRangesTypeDef",
    "EnvironmentParameterTypeDef",
    "ExperimentConfigTypeDef",
    "ExperimentSourceTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTypeDef",
    "ExplainabilityTypeDef",
    "ExplainerConfigTypeDef",
    "FailStepMetadataTypeDef",
    "FeatureDefinitionTypeDef",
    "FeatureGroupSummaryTypeDef",
    "FeatureGroupTypeDef",
    "FeatureMetadataTypeDef",
    "FeatureParameterTypeDef",
    "FileSourceTypeDef",
    "FileSystemConfigTypeDef",
    "FileSystemDataSourceTypeDef",
    "FilterTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "FlowDefinitionOutputConfigTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "GetDeviceFleetReportRequestRequestTypeDef",
    "GetDeviceFleetReportResponseTypeDef",
    "GetLineageGroupPolicyRequestRequestTypeDef",
    "GetLineageGroupPolicyResponseTypeDef",
    "GetModelPackageGroupPolicyInputRequestTypeDef",
    "GetModelPackageGroupPolicyOutputTypeDef",
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    "GetScalingConfigurationRecommendationRequestRequestTypeDef",
    "GetScalingConfigurationRecommendationResponseTypeDef",
    "GetSearchSuggestionsRequestRequestTypeDef",
    "GetSearchSuggestionsResponseTypeDef",
    "GitConfigForUpdateTypeDef",
    "GitConfigTypeDef",
    "HolidayConfigAttributesTypeDef",
    "HubContentDependencyTypeDef",
    "HubContentInfoTypeDef",
    "HubInfoTypeDef",
    "HubS3StorageConfigTypeDef",
    "HumanLoopActivationConditionsConfigTypeDef",
    "HumanLoopActivationConfigTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopRequestSourceTypeDef",
    "HumanTaskConfigTypeDef",
    "HumanTaskUiSummaryTypeDef",
    "HyperParameterAlgorithmSpecificationTypeDef",
    "HyperParameterSpecificationTypeDef",
    "HyperParameterTrainingJobDefinitionTypeDef",
    "HyperParameterTrainingJobSummaryTypeDef",
    "HyperParameterTuningInstanceConfigTypeDef",
    "HyperParameterTuningJobCompletionDetailsTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "HyperParameterTuningJobConsumedResourcesTypeDef",
    "HyperParameterTuningJobObjectiveTypeDef",
    "HyperParameterTuningJobSearchEntityTypeDef",
    "HyperParameterTuningJobStrategyConfigTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    "HyperParameterTuningResourceConfigTypeDef",
    "HyperbandStrategyConfigTypeDef",
    "IamIdentityTypeDef",
    "IdentityProviderOAuthSettingTypeDef",
    "ImageClassificationJobConfigTypeDef",
    "ImageConfigTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "ImportHubContentRequestRequestTypeDef",
    "ImportHubContentResponseTypeDef",
    "InferenceExecutionConfigTypeDef",
    "InferenceExperimentDataStorageConfigTypeDef",
    "InferenceExperimentScheduleTypeDef",
    "InferenceExperimentSummaryTypeDef",
    "InferenceMetricsTypeDef",
    "InferenceRecommendationTypeDef",
    "InferenceRecommendationsJobStepTypeDef",
    "InferenceRecommendationsJobTypeDef",
    "InferenceSpecificationTypeDef",
    "InputConfigTypeDef",
    "InstanceGroupTypeDef",
    "InstanceMetadataServiceConfigurationTypeDef",
    "IntegerParameterRangeSpecificationTypeDef",
    "IntegerParameterRangeTypeDef",
    "JupyterServerAppSettingsTypeDef",
    "KendraSettingsTypeDef",
    "KernelGatewayAppSettingsTypeDef",
    "KernelGatewayImageConfigTypeDef",
    "KernelSpecTypeDef",
    "LabelCountersForWorkteamTypeDef",
    "LabelCountersTypeDef",
    "LabelingJobAlgorithmsConfigTypeDef",
    "LabelingJobDataAttributesTypeDef",
    "LabelingJobDataSourceTypeDef",
    "LabelingJobForWorkteamSummaryTypeDef",
    "LabelingJobInputConfigTypeDef",
    "LabelingJobOutputConfigTypeDef",
    "LabelingJobOutputTypeDef",
    "LabelingJobResourceConfigTypeDef",
    "LabelingJobS3DataSourceTypeDef",
    "LabelingJobSnsDataSourceTypeDef",
    "LabelingJobStoppingConditionsTypeDef",
    "LabelingJobSummaryTypeDef",
    "LambdaStepMetadataTypeDef",
    "LastUpdateStatusTypeDef",
    "LineageGroupSummaryTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListActionsResponseTypeDef",
    "ListAlgorithmsInputRequestTypeDef",
    "ListAlgorithmsOutputTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListAppImageConfigsRequestRequestTypeDef",
    "ListAppImageConfigsResponseTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResponseTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListArtifactsResponseTypeDef",
    "ListAssociationsRequestRequestTypeDef",
    "ListAssociationsResponseTypeDef",
    "ListAutoMLJobsRequestRequestTypeDef",
    "ListAutoMLJobsResponseTypeDef",
    "ListCandidatesForAutoMLJobRequestRequestTypeDef",
    "ListCandidatesForAutoMLJobResponseTypeDef",
    "ListCodeRepositoriesInputRequestTypeDef",
    "ListCodeRepositoriesOutputTypeDef",
    "ListCompilationJobsRequestRequestTypeDef",
    "ListCompilationJobsResponseTypeDef",
    "ListContextsRequestRequestTypeDef",
    "ListContextsResponseTypeDef",
    "ListDataQualityJobDefinitionsRequestRequestTypeDef",
    "ListDataQualityJobDefinitionsResponseTypeDef",
    "ListDeviceFleetsRequestRequestTypeDef",
    "ListDeviceFleetsResponseTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEdgeDeploymentPlansRequestRequestTypeDef",
    "ListEdgeDeploymentPlansResponseTypeDef",
    "ListEdgePackagingJobsRequestRequestTypeDef",
    "ListEdgePackagingJobsResponseTypeDef",
    "ListEndpointConfigsInputRequestTypeDef",
    "ListEndpointConfigsOutputTypeDef",
    "ListEndpointsInputRequestTypeDef",
    "ListEndpointsOutputTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFeatureGroupsRequestRequestTypeDef",
    "ListFeatureGroupsResponseTypeDef",
    "ListFlowDefinitionsRequestRequestTypeDef",
    "ListFlowDefinitionsResponseTypeDef",
    "ListHubContentVersionsRequestRequestTypeDef",
    "ListHubContentVersionsResponseTypeDef",
    "ListHubContentsRequestRequestTypeDef",
    "ListHubContentsResponseTypeDef",
    "ListHubsRequestRequestTypeDef",
    "ListHubsResponseTypeDef",
    "ListHumanTaskUisRequestRequestTypeDef",
    "ListHumanTaskUisResponseTypeDef",
    "ListHyperParameterTuningJobsRequestRequestTypeDef",
    "ListHyperParameterTuningJobsResponseTypeDef",
    "ListImageVersionsRequestRequestTypeDef",
    "ListImageVersionsResponseTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInferenceExperimentsRequestRequestTypeDef",
    "ListInferenceExperimentsResponseTypeDef",
    "ListInferenceRecommendationsJobStepsRequestRequestTypeDef",
    "ListInferenceRecommendationsJobStepsResponseTypeDef",
    "ListInferenceRecommendationsJobsRequestRequestTypeDef",
    "ListInferenceRecommendationsJobsResponseTypeDef",
    "ListLabelingJobsForWorkteamRequestRequestTypeDef",
    "ListLabelingJobsForWorkteamResponseTypeDef",
    "ListLabelingJobsRequestRequestTypeDef",
    "ListLabelingJobsResponseTypeDef",
    "ListLineageGroupsRequestRequestTypeDef",
    "ListLineageGroupsResponseTypeDef",
    "ListModelBiasJobDefinitionsRequestRequestTypeDef",
    "ListModelBiasJobDefinitionsResponseTypeDef",
    "ListModelCardExportJobsRequestRequestTypeDef",
    "ListModelCardExportJobsResponseTypeDef",
    "ListModelCardVersionsRequestRequestTypeDef",
    "ListModelCardVersionsResponseTypeDef",
    "ListModelCardsRequestRequestTypeDef",
    "ListModelCardsResponseTypeDef",
    "ListModelExplainabilityJobDefinitionsRequestRequestTypeDef",
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    "ListModelMetadataRequestRequestTypeDef",
    "ListModelMetadataResponseTypeDef",
    "ListModelPackageGroupsInputRequestTypeDef",
    "ListModelPackageGroupsOutputTypeDef",
    "ListModelPackagesInputRequestTypeDef",
    "ListModelPackagesOutputTypeDef",
    "ListModelQualityJobDefinitionsRequestRequestTypeDef",
    "ListModelQualityJobDefinitionsResponseTypeDef",
    "ListModelsInputRequestTypeDef",
    "ListModelsOutputTypeDef",
    "ListMonitoringAlertHistoryRequestRequestTypeDef",
    "ListMonitoringAlertHistoryResponseTypeDef",
    "ListMonitoringAlertsRequestRequestTypeDef",
    "ListMonitoringAlertsResponseTypeDef",
    "ListMonitoringExecutionsRequestRequestTypeDef",
    "ListMonitoringExecutionsResponseTypeDef",
    "ListMonitoringSchedulesRequestRequestTypeDef",
    "ListMonitoringSchedulesResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsInputRequestTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    "ListNotebookInstancesInputRequestTypeDef",
    "ListNotebookInstancesOutputTypeDef",
    "ListPipelineExecutionStepsRequestRequestTypeDef",
    "ListPipelineExecutionStepsResponseTypeDef",
    "ListPipelineExecutionsRequestRequestTypeDef",
    "ListPipelineExecutionsResponseTypeDef",
    "ListPipelineParametersForExecutionRequestRequestTypeDef",
    "ListPipelineParametersForExecutionResponseTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListProcessingJobsRequestRequestTypeDef",
    "ListProcessingJobsResponseTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListProjectsOutputTypeDef",
    "ListResourceCatalogsRequestRequestTypeDef",
    "ListResourceCatalogsResponseTypeDef",
    "ListSpacesRequestRequestTypeDef",
    "ListSpacesResponseTypeDef",
    "ListStageDevicesRequestRequestTypeDef",
    "ListStageDevicesResponseTypeDef",
    "ListStudioLifecycleConfigsRequestRequestTypeDef",
    "ListStudioLifecycleConfigsResponseTypeDef",
    "ListSubscribedWorkteamsRequestRequestTypeDef",
    "ListSubscribedWorkteamsResponseTypeDef",
    "ListTagsInputRequestTypeDef",
    "ListTagsOutputTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ListTrainingJobsRequestRequestTypeDef",
    "ListTrainingJobsResponseTypeDef",
    "ListTransformJobsRequestRequestTypeDef",
    "ListTransformJobsResponseTypeDef",
    "ListTrialComponentsRequestRequestTypeDef",
    "ListTrialComponentsResponseTypeDef",
    "ListTrialsRequestRequestTypeDef",
    "ListTrialsResponseTypeDef",
    "ListUserProfilesRequestRequestTypeDef",
    "ListUserProfilesResponseTypeDef",
    "ListWorkforcesRequestRequestTypeDef",
    "ListWorkforcesResponseTypeDef",
    "ListWorkteamsRequestRequestTypeDef",
    "ListWorkteamsResponseTypeDef",
    "MemberDefinitionTypeDef",
    "MetadataPropertiesTypeDef",
    "MetricDataTypeDef",
    "MetricDatumTypeDef",
    "MetricDefinitionTypeDef",
    "MetricSpecificationTypeDef",
    "MetricsSourceTypeDef",
    "ModelAccessConfigTypeDef",
    "ModelArtifactsTypeDef",
    "ModelBiasAppSpecificationTypeDef",
    "ModelBiasBaselineConfigTypeDef",
    "ModelBiasJobInputTypeDef",
    "ModelCardExportArtifactsTypeDef",
    "ModelCardExportJobSummaryTypeDef",
    "ModelCardExportOutputConfigTypeDef",
    "ModelCardSecurityConfigTypeDef",
    "ModelCardSummaryTypeDef",
    "ModelCardTypeDef",
    "ModelCardVersionSummaryTypeDef",
    "ModelClientConfigTypeDef",
    "ModelConfigurationTypeDef",
    "ModelDashboardEndpointTypeDef",
    "ModelDashboardIndicatorActionTypeDef",
    "ModelDashboardModelCardTypeDef",
    "ModelDashboardModelTypeDef",
    "ModelDashboardMonitoringScheduleTypeDef",
    "ModelDataQualityTypeDef",
    "ModelDataSourceTypeDef",
    "ModelDeployConfigTypeDef",
    "ModelDeployResultTypeDef",
    "ModelDigestsTypeDef",
    "ModelExplainabilityAppSpecificationTypeDef",
    "ModelExplainabilityBaselineConfigTypeDef",
    "ModelExplainabilityJobInputTypeDef",
    "ModelInfrastructureConfigTypeDef",
    "ModelInputTypeDef",
    "ModelLatencyThresholdTypeDef",
    "ModelMetadataFilterTypeDef",
    "ModelMetadataSearchExpressionTypeDef",
    "ModelMetadataSummaryTypeDef",
    "ModelMetricsTypeDef",
    "ModelPackageContainerDefinitionTypeDef",
    "ModelPackageGroupSummaryTypeDef",
    "ModelPackageGroupTypeDef",
    "ModelPackageStatusDetailsTypeDef",
    "ModelPackageStatusItemTypeDef",
    "ModelPackageSummaryTypeDef",
    "ModelPackageTypeDef",
    "ModelPackageValidationProfileTypeDef",
    "ModelPackageValidationSpecificationTypeDef",
    "ModelQualityAppSpecificationTypeDef",
    "ModelQualityBaselineConfigTypeDef",
    "ModelQualityJobInputTypeDef",
    "ModelQualityTypeDef",
    "ModelRegisterSettingsTypeDef",
    "ModelStepMetadataTypeDef",
    "ModelSummaryTypeDef",
    "ModelTypeDef",
    "ModelVariantConfigSummaryTypeDef",
    "ModelVariantConfigTypeDef",
    "MonitoringAlertActionsTypeDef",
    "MonitoringAlertHistorySummaryTypeDef",
    "MonitoringAlertSummaryTypeDef",
    "MonitoringAppSpecificationTypeDef",
    "MonitoringBaselineConfigTypeDef",
    "MonitoringClusterConfigTypeDef",
    "MonitoringConstraintsResourceTypeDef",
    "MonitoringCsvDatasetFormatTypeDef",
    "MonitoringDatasetFormatTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "MonitoringGroundTruthS3InputTypeDef",
    "MonitoringInputTypeDef",
    "MonitoringJobDefinitionSummaryTypeDef",
    "MonitoringJobDefinitionTypeDef",
    "MonitoringJsonDatasetFormatTypeDef",
    "MonitoringNetworkConfigTypeDef",
    "MonitoringOutputConfigTypeDef",
    "MonitoringOutputTypeDef",
    "MonitoringResourcesTypeDef",
    "MonitoringS3OutputTypeDef",
    "MonitoringScheduleConfigTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "MonitoringScheduleTypeDef",
    "MonitoringStatisticsResourceTypeDef",
    "MonitoringStoppingConditionTypeDef",
    "MultiModelConfigTypeDef",
    "NeoVpcConfigTypeDef",
    "NestedFiltersTypeDef",
    "NetworkConfigTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "NotebookInstanceLifecycleHookTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "OfflineStoreConfigTypeDef",
    "OfflineStoreStatusTypeDef",
    "OidcConfigForResponseTypeDef",
    "OidcConfigTypeDef",
    "OidcMemberDefinitionTypeDef",
    "OnlineStoreConfigTypeDef",
    "OnlineStoreConfigUpdateTypeDef",
    "OnlineStoreSecurityConfigTypeDef",
    "OutputConfigTypeDef",
    "OutputDataConfigTypeDef",
    "OutputParameterTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParameterRangeTypeDef",
    "ParameterRangesTypeDef",
    "ParameterTypeDef",
    "ParentHyperParameterTuningJobTypeDef",
    "ParentTypeDef",
    "PendingDeploymentSummaryTypeDef",
    "PendingProductionVariantSummaryTypeDef",
    "PhaseTypeDef",
    "PipelineDefinitionS3LocationTypeDef",
    "PipelineExecutionStepMetadataTypeDef",
    "PipelineExecutionStepTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineExperimentConfigTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "ProcessingClusterConfigTypeDef",
    "ProcessingFeatureStoreOutputTypeDef",
    "ProcessingInputTypeDef",
    "ProcessingJobStepMetadataTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ProcessingJobTypeDef",
    "ProcessingOutputConfigTypeDef",
    "ProcessingOutputTypeDef",
    "ProcessingResourcesTypeDef",
    "ProcessingS3InputTypeDef",
    "ProcessingS3OutputTypeDef",
    "ProcessingStoppingConditionTypeDef",
    "ProductionVariantCoreDumpConfigTypeDef",
    "ProductionVariantServerlessConfigTypeDef",
    "ProductionVariantServerlessUpdateConfigTypeDef",
    "ProductionVariantStatusTypeDef",
    "ProductionVariantSummaryTypeDef",
    "ProductionVariantTypeDef",
    "ProfilerConfigForUpdateTypeDef",
    "ProfilerConfigTypeDef",
    "ProfilerRuleConfigurationTypeDef",
    "ProfilerRuleEvaluationStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ProjectTypeDef",
    "PropertyNameQueryTypeDef",
    "PropertyNameSuggestionTypeDef",
    "ProvisioningParameterTypeDef",
    "PublicWorkforceTaskPriceTypeDef",
    "PutModelPackageGroupPolicyInputRequestTypeDef",
    "PutModelPackageGroupPolicyOutputTypeDef",
    "QualityCheckStepMetadataTypeDef",
    "QueryFiltersTypeDef",
    "QueryLineageRequestRequestTypeDef",
    "QueryLineageResponseTypeDef",
    "RSessionAppSettingsTypeDef",
    "RStudioServerProAppSettingsTypeDef",
    "RStudioServerProDomainSettingsForUpdateTypeDef",
    "RStudioServerProDomainSettingsTypeDef",
    "RealTimeInferenceConfigTypeDef",
    "RealTimeInferenceRecommendationTypeDef",
    "RecommendationJobCompiledOutputConfigTypeDef",
    "RecommendationJobContainerConfigTypeDef",
    "RecommendationJobInferenceBenchmarkTypeDef",
    "RecommendationJobInputConfigTypeDef",
    "RecommendationJobOutputConfigTypeDef",
    "RecommendationJobPayloadConfigTypeDef",
    "RecommendationJobResourceLimitTypeDef",
    "RecommendationJobStoppingConditionsTypeDef",
    "RecommendationJobVpcConfigTypeDef",
    "RecommendationMetricsTypeDef",
    "RedshiftDatasetDefinitionTypeDef",
    "RegisterDevicesRequestRequestTypeDef",
    "RegisterModelStepMetadataTypeDef",
    "RenderUiTemplateRequestRequestTypeDef",
    "RenderUiTemplateResponseTypeDef",
    "RenderableTaskTypeDef",
    "RenderingErrorTypeDef",
    "RepositoryAuthConfigTypeDef",
    "ResolvedAttributesTypeDef",
    "ResourceCatalogTypeDef",
    "ResourceConfigForUpdateTypeDef",
    "ResourceConfigTypeDef",
    "ResourceLimitsTypeDef",
    "ResourceSpecTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPolicyTypeDef",
    "RetryPipelineExecutionRequestRequestTypeDef",
    "RetryPipelineExecutionResponseTypeDef",
    "RetryStrategyTypeDef",
    "RollingUpdatePolicyTypeDef",
    "S3DataSourceTypeDef",
    "S3ModelDataSourceTypeDef",
    "S3StorageConfigTypeDef",
    "ScalingPolicyMetricTypeDef",
    "ScalingPolicyObjectiveTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduleConfigTypeDef",
    "SearchExpressionTypeDef",
    "SearchRecordTypeDef",
    "SearchRequestRequestTypeDef",
    "SearchResponseTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "SelectedStepTypeDef",
    "SelectiveExecutionConfigTypeDef",
    "SelectiveExecutionResultTypeDef",
    "SendPipelineExecutionStepFailureRequestRequestTypeDef",
    "SendPipelineExecutionStepFailureResponseTypeDef",
    "SendPipelineExecutionStepSuccessRequestRequestTypeDef",
    "SendPipelineExecutionStepSuccessResponseTypeDef",
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    "ServiceCatalogProvisioningDetailsTypeDef",
    "ServiceCatalogProvisioningUpdateDetailsTypeDef",
    "ShadowModeConfigTypeDef",
    "ShadowModelVariantConfigTypeDef",
    "SharingSettingsTypeDef",
    "ShuffleConfigTypeDef",
    "SourceAlgorithmSpecificationTypeDef",
    "SourceAlgorithmTypeDef",
    "SourceIpConfigTypeDef",
    "SpaceDetailsTypeDef",
    "SpaceSettingsTypeDef",
    "StairsTypeDef",
    "StartEdgeDeploymentStageRequestRequestTypeDef",
    "StartInferenceExperimentRequestRequestTypeDef",
    "StartInferenceExperimentResponseTypeDef",
    "StartMonitoringScheduleRequestRequestTypeDef",
    "StartNotebookInstanceInputRequestTypeDef",
    "StartPipelineExecutionRequestRequestTypeDef",
    "StartPipelineExecutionResponseTypeDef",
    "StopAutoMLJobRequestRequestTypeDef",
    "StopCompilationJobRequestRequestTypeDef",
    "StopEdgeDeploymentStageRequestRequestTypeDef",
    "StopEdgePackagingJobRequestRequestTypeDef",
    "StopHyperParameterTuningJobRequestRequestTypeDef",
    "StopInferenceExperimentRequestRequestTypeDef",
    "StopInferenceExperimentResponseTypeDef",
    "StopInferenceRecommendationsJobRequestRequestTypeDef",
    "StopLabelingJobRequestRequestTypeDef",
    "StopMonitoringScheduleRequestRequestTypeDef",
    "StopNotebookInstanceInputRequestTypeDef",
    "StopPipelineExecutionRequestRequestTypeDef",
    "StopPipelineExecutionResponseTypeDef",
    "StopProcessingJobRequestRequestTypeDef",
    "StopTrainingJobRequestRequestTypeDef",
    "StopTransformJobRequestRequestTypeDef",
    "StoppingConditionTypeDef",
    "StudioLifecycleConfigDetailsTypeDef",
    "SubscribedWorkteamTypeDef",
    "SuggestionQueryTypeDef",
    "TabularJobConfigTypeDef",
    "TabularResolvedAttributesTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "TensorBoardAppSettingsTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "TextClassificationJobConfigTypeDef",
    "TextGenerationJobConfigTypeDef",
    "TextGenerationResolvedAttributesTypeDef",
    "TimeSeriesConfigTypeDef",
    "TimeSeriesForecastingJobConfigTypeDef",
    "TimeSeriesForecastingSettingsTypeDef",
    "TimeSeriesTransformationsTypeDef",
    "TrafficPatternTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TrainingImageConfigTypeDef",
    "TrainingJobDefinitionTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "TrainingJobStepMetadataTypeDef",
    "TrainingJobSummaryTypeDef",
    "TrainingJobTypeDef",
    "TrainingRepositoryAuthConfigTypeDef",
    "TrainingSpecificationTypeDef",
    "TransformDataSourceTypeDef",
    "TransformInputTypeDef",
    "TransformJobDefinitionTypeDef",
    "TransformJobStepMetadataTypeDef",
    "TransformJobSummaryTypeDef",
    "TransformJobTypeDef",
    "TransformOutputTypeDef",
    "TransformResourcesTypeDef",
    "TransformS3DataSourceTypeDef",
    "TrialComponentArtifactTypeDef",
    "TrialComponentMetricSummaryTypeDef",
    "TrialComponentParameterValueTypeDef",
    "TrialComponentSimpleSummaryTypeDef",
    "TrialComponentSourceDetailTypeDef",
    "TrialComponentSourceTypeDef",
    "TrialComponentStatusTypeDef",
    "TrialComponentSummaryTypeDef",
    "TrialComponentTypeDef",
    "TrialSourceTypeDef",
    "TrialSummaryTypeDef",
    "TrialTypeDef",
    "TtlDurationTypeDef",
    "TuningJobCompletionCriteriaTypeDef",
    "TuningJobStepMetaDataTypeDef",
    "USDTypeDef",
    "UiConfigTypeDef",
    "UiTemplateInfoTypeDef",
    "UiTemplateTypeDef",
    "UpdateActionRequestRequestTypeDef",
    "UpdateActionResponseTypeDef",
    "UpdateAppImageConfigRequestRequestTypeDef",
    "UpdateAppImageConfigResponseTypeDef",
    "UpdateArtifactRequestRequestTypeDef",
    "UpdateArtifactResponseTypeDef",
    "UpdateCodeRepositoryInputRequestTypeDef",
    "UpdateCodeRepositoryOutputTypeDef",
    "UpdateContextRequestRequestTypeDef",
    "UpdateContextResponseTypeDef",
    "UpdateDeviceFleetRequestRequestTypeDef",
    "UpdateDevicesRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateEndpointInputRequestTypeDef",
    "UpdateEndpointOutputTypeDef",
    "UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef",
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateFeatureGroupRequestRequestTypeDef",
    "UpdateFeatureGroupResponseTypeDef",
    "UpdateFeatureMetadataRequestRequestTypeDef",
    "UpdateHubRequestRequestTypeDef",
    "UpdateHubResponseTypeDef",
    "UpdateImageRequestRequestTypeDef",
    "UpdateImageResponseTypeDef",
    "UpdateImageVersionRequestRequestTypeDef",
    "UpdateImageVersionResponseTypeDef",
    "UpdateInferenceExperimentRequestRequestTypeDef",
    "UpdateInferenceExperimentResponseTypeDef",
    "UpdateModelCardRequestRequestTypeDef",
    "UpdateModelCardResponseTypeDef",
    "UpdateModelPackageInputRequestTypeDef",
    "UpdateModelPackageOutputTypeDef",
    "UpdateMonitoringAlertRequestRequestTypeDef",
    "UpdateMonitoringAlertResponseTypeDef",
    "UpdateMonitoringScheduleRequestRequestTypeDef",
    "UpdateMonitoringScheduleResponseTypeDef",
    "UpdateNotebookInstanceInputRequestTypeDef",
    "UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    "UpdatePipelineExecutionRequestRequestTypeDef",
    "UpdatePipelineExecutionResponseTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateSpaceRequestRequestTypeDef",
    "UpdateSpaceResponseTypeDef",
    "UpdateTrainingJobRequestRequestTypeDef",
    "UpdateTrainingJobResponseTypeDef",
    "UpdateTrialComponentRequestRequestTypeDef",
    "UpdateTrialComponentResponseTypeDef",
    "UpdateTrialRequestRequestTypeDef",
    "UpdateTrialResponseTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "UpdateUserProfileResponseTypeDef",
    "UpdateWorkforceRequestRequestTypeDef",
    "UpdateWorkforceResponseTypeDef",
    "UpdateWorkteamRequestRequestTypeDef",
    "UpdateWorkteamResponseTypeDef",
    "UserContextTypeDef",
    "UserProfileDetailsTypeDef",
    "UserSettingsTypeDef",
    "VariantPropertyTypeDef",
    "VectorConfigTypeDef",
    "VertexTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
    "WarmPoolStatusTypeDef",
    "WorkforceTypeDef",
    "WorkforceVpcConfigRequestTypeDef",
    "WorkforceVpcConfigResponseTypeDef",
    "WorkspaceSettingsTypeDef",
    "WorkteamTypeDef",
)

_RequiredActionSourceTypeDef = TypedDict(
    "_RequiredActionSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalActionSourceTypeDef = TypedDict(
    "_OptionalActionSourceTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)

class ActionSourceTypeDef(_RequiredActionSourceTypeDef, _OptionalActionSourceTypeDef):
    pass

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "ActionArn": str,
        "ActionName": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
        "Status": ActionStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredAddAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredAddAssociationRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)
_OptionalAddAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalAddAssociationRequestRequestTypeDef",
    {
        "AssociationType": AssociationEdgeTypeType,
    },
    total=False,
)

class AddAssociationRequestRequestTypeDef(
    _RequiredAddAssociationRequestRequestTypeDef, _OptionalAddAssociationRequestRequestTypeDef
):
    pass

AddAssociationResponseTypeDef = TypedDict(
    "AddAssociationResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdditionalInferenceSpecificationDefinitionTypeDef = TypedDict(
    "_RequiredAdditionalInferenceSpecificationDefinitionTypeDef",
    {
        "Name": str,
        "Containers": List["ModelPackageContainerDefinitionTypeDef"],
    },
)
_OptionalAdditionalInferenceSpecificationDefinitionTypeDef = TypedDict(
    "_OptionalAdditionalInferenceSpecificationDefinitionTypeDef",
    {
        "Description": str,
        "SupportedTransformInstanceTypes": List[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": List[ProductionVariantInstanceTypeType],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)

class AdditionalInferenceSpecificationDefinitionTypeDef(
    _RequiredAdditionalInferenceSpecificationDefinitionTypeDef,
    _OptionalAdditionalInferenceSpecificationDefinitionTypeDef,
):
    pass

_RequiredAdditionalS3DataSourceTypeDef = TypedDict(
    "_RequiredAdditionalS3DataSourceTypeDef",
    {
        "S3DataType": Literal["S3Object"],
        "S3Uri": str,
    },
)
_OptionalAdditionalS3DataSourceTypeDef = TypedDict(
    "_OptionalAdditionalS3DataSourceTypeDef",
    {
        "CompressionType": CompressionTypeType,
    },
    total=False,
)

class AdditionalS3DataSourceTypeDef(
    _RequiredAdditionalS3DataSourceTypeDef, _OptionalAdditionalS3DataSourceTypeDef
):
    pass

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": str,
        "AgentCount": int,
    },
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
    },
    total=False,
)

_RequiredAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "EnableSageMakerMetricsTimeSeries": bool,
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "TrainingImageConfig": "TrainingImageConfigTypeDef",
    },
    total=False,
)

class AlgorithmSpecificationTypeDef(
    _RequiredAlgorithmSpecificationTypeDef, _OptionalAlgorithmSpecificationTypeDef
):
    pass

AlgorithmStatusDetailsTypeDef = TypedDict(
    "AlgorithmStatusDetailsTypeDef",
    {
        "ValidationStatuses": List["AlgorithmStatusItemTypeDef"],
        "ImageScanStatuses": List["AlgorithmStatusItemTypeDef"],
    },
    total=False,
)

_RequiredAlgorithmStatusItemTypeDef = TypedDict(
    "_RequiredAlgorithmStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedAlgorithmStatusType,
    },
)
_OptionalAlgorithmStatusItemTypeDef = TypedDict(
    "_OptionalAlgorithmStatusItemTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)

class AlgorithmStatusItemTypeDef(
    _RequiredAlgorithmStatusItemTypeDef, _OptionalAlgorithmStatusItemTypeDef
):
    pass

_RequiredAlgorithmSummaryTypeDef = TypedDict(
    "_RequiredAlgorithmSummaryTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "CreationTime": datetime,
        "AlgorithmStatus": AlgorithmStatusType,
    },
)
_OptionalAlgorithmSummaryTypeDef = TypedDict(
    "_OptionalAlgorithmSummaryTypeDef",
    {
        "AlgorithmDescription": str,
    },
    total=False,
)

class AlgorithmSummaryTypeDef(_RequiredAlgorithmSummaryTypeDef, _OptionalAlgorithmSummaryTypeDef):
    pass

_RequiredAlgorithmValidationProfileTypeDef = TypedDict(
    "_RequiredAlgorithmValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TrainingJobDefinition": "TrainingJobDefinitionTypeDef",
    },
)
_OptionalAlgorithmValidationProfileTypeDef = TypedDict(
    "_OptionalAlgorithmValidationProfileTypeDef",
    {
        "TransformJobDefinition": "TransformJobDefinitionTypeDef",
    },
    total=False,
)

class AlgorithmValidationProfileTypeDef(
    _RequiredAlgorithmValidationProfileTypeDef, _OptionalAlgorithmValidationProfileTypeDef
):
    pass

AlgorithmValidationSpecificationTypeDef = TypedDict(
    "AlgorithmValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List["AlgorithmValidationProfileTypeDef"],
    },
)

AnnotationConsolidationConfigTypeDef = TypedDict(
    "AnnotationConsolidationConfigTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
    },
)

AppDetailsTypeDef = TypedDict(
    "AppDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": AppTypeType,
        "AppName": str,
        "Status": AppStatusType,
        "CreationTime": datetime,
        "SpaceName": str,
    },
    total=False,
)

AppImageConfigDetailsTypeDef = TypedDict(
    "AppImageConfigDetailsTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)

_RequiredAppSpecificationTypeDef = TypedDict(
    "_RequiredAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalAppSpecificationTypeDef = TypedDict(
    "_OptionalAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
    },
    total=False,
)

class AppSpecificationTypeDef(_RequiredAppSpecificationTypeDef, _OptionalAppSpecificationTypeDef):
    pass

_RequiredArtifactSourceTypeDef = TypedDict(
    "_RequiredArtifactSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalArtifactSourceTypeDef = TypedDict(
    "_OptionalArtifactSourceTypeDef",
    {
        "SourceTypes": List["ArtifactSourceTypeTypeDef"],
    },
    total=False,
)

class ArtifactSourceTypeDef(_RequiredArtifactSourceTypeDef, _OptionalArtifactSourceTypeDef):
    pass

ArtifactSourceTypeTypeDef = TypedDict(
    "ArtifactSourceTypeTypeDef",
    {
        "SourceIdType": ArtifactSourceIdTypeType,
        "Value": str,
    },
)

ArtifactSummaryTypeDef = TypedDict(
    "ArtifactSummaryTypeDef",
    {
        "ArtifactArn": str,
        "ArtifactName": str,
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

AssociateTrialComponentRequestRequestTypeDef = TypedDict(
    "AssociateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

AssociateTrialComponentResponseTypeDef = TypedDict(
    "AssociateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociationSummaryTypeDef = TypedDict(
    "AssociationSummaryTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "SourceName": str,
        "DestinationName": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
    },
    total=False,
)

AsyncInferenceClientConfigTypeDef = TypedDict(
    "AsyncInferenceClientConfigTypeDef",
    {
        "MaxConcurrentInvocationsPerInstance": int,
    },
    total=False,
)

_RequiredAsyncInferenceConfigTypeDef = TypedDict(
    "_RequiredAsyncInferenceConfigTypeDef",
    {
        "OutputConfig": "AsyncInferenceOutputConfigTypeDef",
    },
)
_OptionalAsyncInferenceConfigTypeDef = TypedDict(
    "_OptionalAsyncInferenceConfigTypeDef",
    {
        "ClientConfig": "AsyncInferenceClientConfigTypeDef",
    },
    total=False,
)

class AsyncInferenceConfigTypeDef(
    _RequiredAsyncInferenceConfigTypeDef, _OptionalAsyncInferenceConfigTypeDef
):
    pass

AsyncInferenceNotificationConfigTypeDef = TypedDict(
    "AsyncInferenceNotificationConfigTypeDef",
    {
        "SuccessTopic": str,
        "ErrorTopic": str,
        "IncludeInferenceResponseIn": List[AsyncNotificationTopicTypesType],
    },
    total=False,
)

AsyncInferenceOutputConfigTypeDef = TypedDict(
    "AsyncInferenceOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "S3OutputPath": str,
        "NotificationConfig": "AsyncInferenceNotificationConfigTypeDef",
        "S3FailurePath": str,
    },
    total=False,
)

_RequiredAthenaDatasetDefinitionTypeDef = TypedDict(
    "_RequiredAthenaDatasetDefinitionTypeDef",
    {
        "Catalog": str,
        "Database": str,
        "QueryString": str,
        "OutputS3Uri": str,
        "OutputFormat": AthenaResultFormatType,
    },
)
_OptionalAthenaDatasetDefinitionTypeDef = TypedDict(
    "_OptionalAthenaDatasetDefinitionTypeDef",
    {
        "WorkGroup": str,
        "KmsKeyId": str,
        "OutputCompression": AthenaResultCompressionTypeType,
    },
    total=False,
)

class AthenaDatasetDefinitionTypeDef(
    _RequiredAthenaDatasetDefinitionTypeDef, _OptionalAthenaDatasetDefinitionTypeDef
):
    pass

AutoMLAlgorithmConfigTypeDef = TypedDict(
    "AutoMLAlgorithmConfigTypeDef",
    {
        "AutoMLAlgorithms": List[AutoMLAlgorithmType],
    },
)

AutoMLCandidateGenerationConfigTypeDef = TypedDict(
    "AutoMLCandidateGenerationConfigTypeDef",
    {
        "FeatureSpecificationS3Uri": str,
        "AlgorithmsConfig": List["AutoMLAlgorithmConfigTypeDef"],
    },
    total=False,
)

AutoMLCandidateStepTypeDef = TypedDict(
    "AutoMLCandidateStepTypeDef",
    {
        "CandidateStepType": CandidateStepTypeType,
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
)

_RequiredAutoMLCandidateTypeDef = TypedDict(
    "_RequiredAutoMLCandidateTypeDef",
    {
        "CandidateName": str,
        "ObjectiveStatus": ObjectiveStatusType,
        "CandidateSteps": List["AutoMLCandidateStepTypeDef"],
        "CandidateStatus": CandidateStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLCandidateTypeDef = TypedDict(
    "_OptionalAutoMLCandidateTypeDef",
    {
        "FinalAutoMLJobObjectiveMetric": "FinalAutoMLJobObjectiveMetricTypeDef",
        "InferenceContainers": List["AutoMLContainerDefinitionTypeDef"],
        "EndTime": datetime,
        "FailureReason": str,
        "CandidateProperties": "CandidatePropertiesTypeDef",
        "InferenceContainerDefinitions": Dict[
            AutoMLProcessingUnitType, List["AutoMLContainerDefinitionTypeDef"]
        ],
    },
    total=False,
)

class AutoMLCandidateTypeDef(_RequiredAutoMLCandidateTypeDef, _OptionalAutoMLCandidateTypeDef):
    pass

_RequiredAutoMLChannelTypeDef = TypedDict(
    "_RequiredAutoMLChannelTypeDef",
    {
        "DataSource": "AutoMLDataSourceTypeDef",
        "TargetAttributeName": str,
    },
)
_OptionalAutoMLChannelTypeDef = TypedDict(
    "_OptionalAutoMLChannelTypeDef",
    {
        "CompressionType": CompressionTypeType,
        "ContentType": str,
        "ChannelType": AutoMLChannelTypeType,
        "SampleWeightAttributeName": str,
    },
    total=False,
)

class AutoMLChannelTypeDef(_RequiredAutoMLChannelTypeDef, _OptionalAutoMLChannelTypeDef):
    pass

_RequiredAutoMLContainerDefinitionTypeDef = TypedDict(
    "_RequiredAutoMLContainerDefinitionTypeDef",
    {
        "Image": str,
        "ModelDataUrl": str,
    },
)
_OptionalAutoMLContainerDefinitionTypeDef = TypedDict(
    "_OptionalAutoMLContainerDefinitionTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)

class AutoMLContainerDefinitionTypeDef(
    _RequiredAutoMLContainerDefinitionTypeDef, _OptionalAutoMLContainerDefinitionTypeDef
):
    pass

AutoMLDataSourceTypeDef = TypedDict(
    "AutoMLDataSourceTypeDef",
    {
        "S3DataSource": "AutoMLS3DataSourceTypeDef",
    },
)

AutoMLDataSplitConfigTypeDef = TypedDict(
    "AutoMLDataSplitConfigTypeDef",
    {
        "ValidationFraction": float,
    },
    total=False,
)

AutoMLJobArtifactsTypeDef = TypedDict(
    "AutoMLJobArtifactsTypeDef",
    {
        "CandidateDefinitionNotebookLocation": str,
        "DataExplorationNotebookLocation": str,
    },
    total=False,
)

AutoMLJobChannelTypeDef = TypedDict(
    "AutoMLJobChannelTypeDef",
    {
        "ChannelType": AutoMLChannelTypeType,
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "DataSource": "AutoMLDataSourceTypeDef",
    },
    total=False,
)

AutoMLJobCompletionCriteriaTypeDef = TypedDict(
    "AutoMLJobCompletionCriteriaTypeDef",
    {
        "MaxCandidates": int,
        "MaxRuntimePerTrainingJobInSeconds": int,
        "MaxAutoMLJobRuntimeInSeconds": int,
    },
    total=False,
)

AutoMLJobConfigTypeDef = TypedDict(
    "AutoMLJobConfigTypeDef",
    {
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
        "SecurityConfig": "AutoMLSecurityConfigTypeDef",
        "DataSplitConfig": "AutoMLDataSplitConfigTypeDef",
        "CandidateGenerationConfig": "AutoMLCandidateGenerationConfigTypeDef",
        "Mode": AutoMLModeType,
    },
    total=False,
)

AutoMLJobObjectiveTypeDef = TypedDict(
    "AutoMLJobObjectiveTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
    },
)

AutoMLJobStepMetadataTypeDef = TypedDict(
    "AutoMLJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredAutoMLJobSummaryTypeDef = TypedDict(
    "_RequiredAutoMLJobSummaryTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLJobSummaryTypeDef = TypedDict(
    "_OptionalAutoMLJobSummaryTypeDef",
    {
        "EndTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List["AutoMLPartialFailureReasonTypeDef"],
    },
    total=False,
)

class AutoMLJobSummaryTypeDef(_RequiredAutoMLJobSummaryTypeDef, _OptionalAutoMLJobSummaryTypeDef):
    pass

_RequiredAutoMLOutputDataConfigTypeDef = TypedDict(
    "_RequiredAutoMLOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalAutoMLOutputDataConfigTypeDef = TypedDict(
    "_OptionalAutoMLOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class AutoMLOutputDataConfigTypeDef(
    _RequiredAutoMLOutputDataConfigTypeDef, _OptionalAutoMLOutputDataConfigTypeDef
):
    pass

AutoMLPartialFailureReasonTypeDef = TypedDict(
    "AutoMLPartialFailureReasonTypeDef",
    {
        "PartialFailureMessage": str,
    },
    total=False,
)

AutoMLProblemTypeConfigTypeDef = TypedDict(
    "AutoMLProblemTypeConfigTypeDef",
    {
        "ImageClassificationJobConfig": "ImageClassificationJobConfigTypeDef",
        "TextClassificationJobConfig": "TextClassificationJobConfigTypeDef",
        "TabularJobConfig": "TabularJobConfigTypeDef",
        "TimeSeriesForecastingJobConfig": "TimeSeriesForecastingJobConfigTypeDef",
        "TextGenerationJobConfig": "TextGenerationJobConfigTypeDef",
    },
    total=False,
)

AutoMLProblemTypeResolvedAttributesTypeDef = TypedDict(
    "AutoMLProblemTypeResolvedAttributesTypeDef",
    {
        "TabularResolvedAttributes": "TabularResolvedAttributesTypeDef",
        "TextGenerationResolvedAttributes": "TextGenerationResolvedAttributesTypeDef",
    },
    total=False,
)

AutoMLResolvedAttributesTypeDef = TypedDict(
    "AutoMLResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
        "AutoMLProblemTypeResolvedAttributes": "AutoMLProblemTypeResolvedAttributesTypeDef",
    },
    total=False,
)

AutoMLS3DataSourceTypeDef = TypedDict(
    "AutoMLS3DataSourceTypeDef",
    {
        "S3DataType": AutoMLS3DataTypeType,
        "S3Uri": str,
    },
)

AutoMLSecurityConfigTypeDef = TypedDict(
    "AutoMLSecurityConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "EnableInterContainerTrafficEncryption": bool,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

AutoParameterTypeDef = TypedDict(
    "AutoParameterTypeDef",
    {
        "Name": str,
        "ValueHint": str,
    },
)

AutoRollbackConfigTypeDef = TypedDict(
    "AutoRollbackConfigTypeDef",
    {
        "Alarms": List["AlarmTypeDef"],
    },
    total=False,
)

AutotuneTypeDef = TypedDict(
    "AutotuneTypeDef",
    {
        "Mode": Literal["Enabled"],
    },
)

_RequiredBatchDataCaptureConfigTypeDef = TypedDict(
    "_RequiredBatchDataCaptureConfigTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalBatchDataCaptureConfigTypeDef = TypedDict(
    "_OptionalBatchDataCaptureConfigTypeDef",
    {
        "KmsKeyId": str,
        "GenerateInferenceId": bool,
    },
    total=False,
)

class BatchDataCaptureConfigTypeDef(
    _RequiredBatchDataCaptureConfigTypeDef, _OptionalBatchDataCaptureConfigTypeDef
):
    pass

BatchDescribeModelPackageErrorTypeDef = TypedDict(
    "BatchDescribeModelPackageErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorResponse": str,
    },
)

BatchDescribeModelPackageInputRequestTypeDef = TypedDict(
    "BatchDescribeModelPackageInputRequestTypeDef",
    {
        "ModelPackageArnList": List[str],
    },
)

BatchDescribeModelPackageOutputTypeDef = TypedDict(
    "BatchDescribeModelPackageOutputTypeDef",
    {
        "ModelPackageSummaries": Dict[str, "BatchDescribeModelPackageSummaryTypeDef"],
        "BatchDescribeModelPackageErrorMap": Dict[str, "BatchDescribeModelPackageErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDescribeModelPackageSummaryTypeDef = TypedDict(
    "_RequiredBatchDescribeModelPackageSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
    },
)
_OptionalBatchDescribeModelPackageSummaryTypeDef = TypedDict(
    "_OptionalBatchDescribeModelPackageSummaryTypeDef",
    {
        "ModelPackageVersion": int,
        "ModelPackageDescription": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
    },
    total=False,
)

class BatchDescribeModelPackageSummaryTypeDef(
    _RequiredBatchDescribeModelPackageSummaryTypeDef,
    _OptionalBatchDescribeModelPackageSummaryTypeDef,
):
    pass

_RequiredBatchTransformInputTypeDef = TypedDict(
    "_RequiredBatchTransformInputTypeDef",
    {
        "DataCapturedDestinationS3Uri": str,
        "DatasetFormat": "MonitoringDatasetFormatTypeDef",
        "LocalPath": str,
    },
)
_OptionalBatchTransformInputTypeDef = TypedDict(
    "_OptionalBatchTransformInputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
        "ExcludeFeaturesAttribute": str,
    },
    total=False,
)

class BatchTransformInputTypeDef(
    _RequiredBatchTransformInputTypeDef, _OptionalBatchTransformInputTypeDef
):
    pass

BestObjectiveNotImprovingTypeDef = TypedDict(
    "BestObjectiveNotImprovingTypeDef",
    {
        "MaxNumberOfTrainingJobsNotImproving": int,
    },
    total=False,
)

BiasTypeDef = TypedDict(
    "BiasTypeDef",
    {
        "Report": "MetricsSourceTypeDef",
        "PreTrainingReport": "MetricsSourceTypeDef",
        "PostTrainingReport": "MetricsSourceTypeDef",
    },
    total=False,
)

_RequiredBlueGreenUpdatePolicyTypeDef = TypedDict(
    "_RequiredBlueGreenUpdatePolicyTypeDef",
    {
        "TrafficRoutingConfiguration": "TrafficRoutingConfigTypeDef",
    },
)
_OptionalBlueGreenUpdatePolicyTypeDef = TypedDict(
    "_OptionalBlueGreenUpdatePolicyTypeDef",
    {
        "TerminationWaitInSeconds": int,
        "MaximumExecutionTimeoutInSeconds": int,
    },
    total=False,
)

class BlueGreenUpdatePolicyTypeDef(
    _RequiredBlueGreenUpdatePolicyTypeDef, _OptionalBlueGreenUpdatePolicyTypeDef
):
    pass

CacheHitResultTypeDef = TypedDict(
    "CacheHitResultTypeDef",
    {
        "SourcePipelineExecutionArn": str,
    },
    total=False,
)

CallbackStepMetadataTypeDef = TypedDict(
    "CallbackStepMetadataTypeDef",
    {
        "CallbackToken": str,
        "SqsQueueUrl": str,
        "OutputParameters": List["OutputParameterTypeDef"],
    },
    total=False,
)

_RequiredCandidateArtifactLocationsTypeDef = TypedDict(
    "_RequiredCandidateArtifactLocationsTypeDef",
    {
        "Explainability": str,
    },
)
_OptionalCandidateArtifactLocationsTypeDef = TypedDict(
    "_OptionalCandidateArtifactLocationsTypeDef",
    {
        "ModelInsights": str,
        "BacktestResults": str,
    },
    total=False,
)

class CandidateArtifactLocationsTypeDef(
    _RequiredCandidateArtifactLocationsTypeDef, _OptionalCandidateArtifactLocationsTypeDef
):
    pass

CandidateGenerationConfigTypeDef = TypedDict(
    "CandidateGenerationConfigTypeDef",
    {
        "AlgorithmsConfig": List["AutoMLAlgorithmConfigTypeDef"],
    },
    total=False,
)

CandidatePropertiesTypeDef = TypedDict(
    "CandidatePropertiesTypeDef",
    {
        "CandidateArtifactLocations": "CandidateArtifactLocationsTypeDef",
        "CandidateMetrics": List["MetricDatumTypeDef"],
    },
    total=False,
)

CanvasAppSettingsTypeDef = TypedDict(
    "CanvasAppSettingsTypeDef",
    {
        "TimeSeriesForecastingSettings": "TimeSeriesForecastingSettingsTypeDef",
        "ModelRegisterSettings": "ModelRegisterSettingsTypeDef",
        "WorkspaceSettings": "WorkspaceSettingsTypeDef",
        "IdentityProviderOAuthSettings": List["IdentityProviderOAuthSettingTypeDef"],
        "KendraSettings": "KendraSettingsTypeDef",
        "DirectDeploySettings": "DirectDeploySettingsTypeDef",
    },
    total=False,
)

CapacitySizeTypeDef = TypedDict(
    "CapacitySizeTypeDef",
    {
        "Type": CapacitySizeTypeType,
        "Value": int,
    },
)

CaptureContentTypeHeaderTypeDef = TypedDict(
    "CaptureContentTypeHeaderTypeDef",
    {
        "CsvContentTypes": List[str],
        "JsonContentTypes": List[str],
    },
    total=False,
)

CaptureOptionTypeDef = TypedDict(
    "CaptureOptionTypeDef",
    {
        "CaptureMode": CaptureModeType,
    },
)

CategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "CategoricalParameterRangeSpecificationTypeDef",
    {
        "Values": List[str],
    },
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

CategoricalParameterTypeDef = TypedDict(
    "CategoricalParameterTypeDef",
    {
        "Name": str,
        "Value": List[str],
    },
)

_RequiredChannelSpecificationTypeDef = TypedDict(
    "_RequiredChannelSpecificationTypeDef",
    {
        "Name": str,
        "SupportedContentTypes": List[str],
        "SupportedInputModes": List[TrainingInputModeType],
    },
)
_OptionalChannelSpecificationTypeDef = TypedDict(
    "_OptionalChannelSpecificationTypeDef",
    {
        "Description": str,
        "IsRequired": bool,
        "SupportedCompressionTypes": List[CompressionTypeType],
    },
    total=False,
)

class ChannelSpecificationTypeDef(
    _RequiredChannelSpecificationTypeDef, _OptionalChannelSpecificationTypeDef
):
    pass

_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef",
    {
        "ChannelName": str,
        "DataSource": "DataSourceTypeDef",
    },
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "RecordWrapperType": RecordWrapperType,
        "InputMode": TrainingInputModeType,
        "ShuffleConfig": "ShuffleConfigTypeDef",
    },
    total=False,
)

class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass

_RequiredCheckpointConfigTypeDef = TypedDict(
    "_RequiredCheckpointConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalCheckpointConfigTypeDef = TypedDict(
    "_OptionalCheckpointConfigTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)

class CheckpointConfigTypeDef(_RequiredCheckpointConfigTypeDef, _OptionalCheckpointConfigTypeDef):
    pass

ClarifyCheckStepMetadataTypeDef = TypedDict(
    "ClarifyCheckStepMetadataTypeDef",
    {
        "CheckType": str,
        "BaselineUsedForDriftCheckConstraints": str,
        "CalculatedBaselineConstraints": str,
        "ModelPackageGroupName": str,
        "ViolationReport": str,
        "CheckJobArn": str,
        "SkipCheck": bool,
        "RegisterNewBaseline": bool,
    },
    total=False,
)

_RequiredClarifyExplainerConfigTypeDef = TypedDict(
    "_RequiredClarifyExplainerConfigTypeDef",
    {
        "ShapConfig": "ClarifyShapConfigTypeDef",
    },
)
_OptionalClarifyExplainerConfigTypeDef = TypedDict(
    "_OptionalClarifyExplainerConfigTypeDef",
    {
        "EnableExplanations": str,
        "InferenceConfig": "ClarifyInferenceConfigTypeDef",
    },
    total=False,
)

class ClarifyExplainerConfigTypeDef(
    _RequiredClarifyExplainerConfigTypeDef, _OptionalClarifyExplainerConfigTypeDef
):
    pass

ClarifyInferenceConfigTypeDef = TypedDict(
    "ClarifyInferenceConfigTypeDef",
    {
        "FeaturesAttribute": str,
        "ContentTemplate": str,
        "MaxRecordCount": int,
        "MaxPayloadInMB": int,
        "ProbabilityIndex": int,
        "LabelIndex": int,
        "ProbabilityAttribute": str,
        "LabelAttribute": str,
        "LabelHeaders": List[str],
        "FeatureHeaders": List[str],
        "FeatureTypes": List[ClarifyFeatureTypeType],
    },
    total=False,
)

ClarifyShapBaselineConfigTypeDef = TypedDict(
    "ClarifyShapBaselineConfigTypeDef",
    {
        "MimeType": str,
        "ShapBaseline": str,
        "ShapBaselineUri": str,
    },
    total=False,
)

_RequiredClarifyShapConfigTypeDef = TypedDict(
    "_RequiredClarifyShapConfigTypeDef",
    {
        "ShapBaselineConfig": "ClarifyShapBaselineConfigTypeDef",
    },
)
_OptionalClarifyShapConfigTypeDef = TypedDict(
    "_OptionalClarifyShapConfigTypeDef",
    {
        "NumberOfSamples": int,
        "UseLogit": bool,
        "Seed": int,
        "TextConfig": "ClarifyTextConfigTypeDef",
    },
    total=False,
)

class ClarifyShapConfigTypeDef(
    _RequiredClarifyShapConfigTypeDef, _OptionalClarifyShapConfigTypeDef
):
    pass

ClarifyTextConfigTypeDef = TypedDict(
    "ClarifyTextConfigTypeDef",
    {
        "Language": ClarifyTextLanguageType,
        "Granularity": ClarifyTextGranularityType,
    },
)

_RequiredCodeRepositorySummaryTypeDef = TypedDict(
    "_RequiredCodeRepositorySummaryTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalCodeRepositorySummaryTypeDef = TypedDict(
    "_OptionalCodeRepositorySummaryTypeDef",
    {
        "GitConfig": "GitConfigTypeDef",
    },
    total=False,
)

class CodeRepositorySummaryTypeDef(
    _RequiredCodeRepositorySummaryTypeDef, _OptionalCodeRepositorySummaryTypeDef
):
    pass

CodeRepositoryTypeDef = TypedDict(
    "CodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
    },
)

CognitoConfigTypeDef = TypedDict(
    "CognitoConfigTypeDef",
    {
        "UserPool": str,
        "ClientId": str,
    },
)

CognitoMemberDefinitionTypeDef = TypedDict(
    "CognitoMemberDefinitionTypeDef",
    {
        "UserPool": str,
        "UserGroup": str,
        "ClientId": str,
    },
)

CollectionConfigTypeDef = TypedDict(
    "CollectionConfigTypeDef",
    {
        "VectorConfig": "VectorConfigTypeDef",
    },
    total=False,
)

CollectionConfigurationTypeDef = TypedDict(
    "CollectionConfigurationTypeDef",
    {
        "CollectionName": str,
        "CollectionParameters": Dict[str, str],
    },
    total=False,
)

_RequiredCompilationJobSummaryTypeDef = TypedDict(
    "_RequiredCompilationJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationJobStatus": CompilationJobStatusType,
    },
)
_OptionalCompilationJobSummaryTypeDef = TypedDict(
    "_OptionalCompilationJobSummaryTypeDef",
    {
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": TargetDeviceType,
        "CompilationTargetPlatformOs": TargetPlatformOsType,
        "CompilationTargetPlatformArch": TargetPlatformArchType,
        "CompilationTargetPlatformAccelerator": TargetPlatformAcceleratorType,
        "LastModifiedTime": datetime,
    },
    total=False,
)

class CompilationJobSummaryTypeDef(
    _RequiredCompilationJobSummaryTypeDef, _OptionalCompilationJobSummaryTypeDef
):
    pass

ConditionStepMetadataTypeDef = TypedDict(
    "ConditionStepMetadataTypeDef",
    {
        "Outcome": ConditionOutcomeType,
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageConfig": "ImageConfigTypeDef",
        "Mode": ContainerModeType,
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
        "InferenceSpecificationName": str,
        "MultiModelConfig": "MultiModelConfigTypeDef",
        "ModelDataSource": "ModelDataSourceTypeDef",
    },
    total=False,
)

_RequiredContextSourceTypeDef = TypedDict(
    "_RequiredContextSourceTypeDef",
    {
        "SourceUri": str,
    },
)
_OptionalContextSourceTypeDef = TypedDict(
    "_OptionalContextSourceTypeDef",
    {
        "SourceType": str,
        "SourceId": str,
    },
    total=False,
)

class ContextSourceTypeDef(_RequiredContextSourceTypeDef, _OptionalContextSourceTypeDef):
    pass

ContextSummaryTypeDef = TypedDict(
    "ContextSummaryTypeDef",
    {
        "ContextArn": str,
        "ContextName": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ContinuousParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

_RequiredContinuousParameterRangeTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalContinuousParameterRangeTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)

class ContinuousParameterRangeTypeDef(
    _RequiredContinuousParameterRangeTypeDef, _OptionalContinuousParameterRangeTypeDef
):
    pass

ConvergenceDetectedTypeDef = TypedDict(
    "ConvergenceDetectedTypeDef",
    {
        "CompleteOnConvergence": CompleteOnConvergenceType,
    },
    total=False,
)

_RequiredCreateActionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateActionRequestRequestTypeDef",
    {
        "ActionName": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
    },
)
_OptionalCreateActionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateActionRequestRequestTypeDef",
    {
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateActionRequestRequestTypeDef(
    _RequiredCreateActionRequestRequestTypeDef, _OptionalCreateActionRequestRequestTypeDef
):
    pass

CreateActionResponseTypeDef = TypedDict(
    "CreateActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAlgorithmInputRequestTypeDef = TypedDict(
    "_RequiredCreateAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
    },
)
_OptionalCreateAlgorithmInputRequestTypeDef = TypedDict(
    "_OptionalCreateAlgorithmInputRequestTypeDef",
    {
        "AlgorithmDescription": str,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "AlgorithmValidationSpecificationTypeDef",
        "CertifyForMarketplace": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAlgorithmInputRequestTypeDef(
    _RequiredCreateAlgorithmInputRequestTypeDef, _OptionalCreateAlgorithmInputRequestTypeDef
):
    pass

CreateAlgorithmOutputTypeDef = TypedDict(
    "CreateAlgorithmOutputTypeDef",
    {
        "AlgorithmArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)
_OptionalCreateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppImageConfigRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)

class CreateAppImageConfigRequestRequestTypeDef(
    _RequiredCreateAppImageConfigRequestRequestTypeDef,
    _OptionalCreateAppImageConfigRequestRequestTypeDef,
):
    pass

CreateAppImageConfigResponseTypeDef = TypedDict(
    "CreateAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalCreateAppRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppRequestRequestTypeDef",
    {
        "UserProfileName": str,
        "Tags": List["TagTypeDef"],
        "ResourceSpec": "ResourceSpecTypeDef",
        "SpaceName": str,
    },
    total=False,
)

class CreateAppRequestRequestTypeDef(
    _RequiredCreateAppRequestRequestTypeDef, _OptionalCreateAppRequestRequestTypeDef
):
    pass

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "AppArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArtifactRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArtifactRequestRequestTypeDef",
    {
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
    },
)
_OptionalCreateArtifactRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArtifactRequestRequestTypeDef",
    {
        "ArtifactName": str,
        "Properties": Dict[str, str],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateArtifactRequestRequestTypeDef(
    _RequiredCreateArtifactRequestRequestTypeDef, _OptionalCreateArtifactRequestRequestTypeDef
):
    pass

CreateArtifactResponseTypeDef = TypedDict(
    "CreateArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAutoMLJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
        "InputDataConfig": List["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateAutoMLJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoMLJobRequestRequestTypeDef",
    {
        "ProblemType": ProblemTypeType,
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "AutoMLJobConfig": "AutoMLJobConfigTypeDef",
        "GenerateCandidateDefinitionsOnly": bool,
        "Tags": List["TagTypeDef"],
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
    },
    total=False,
)

class CreateAutoMLJobRequestRequestTypeDef(
    _RequiredCreateAutoMLJobRequestRequestTypeDef, _OptionalCreateAutoMLJobRequestRequestTypeDef
):
    pass

CreateAutoMLJobResponseTypeDef = TypedDict(
    "CreateAutoMLJobResponseTypeDef",
    {
        "AutoMLJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAutoMLJobV2RequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoMLJobV2RequestRequestTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobInputDataConfig": List["AutoMLJobChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "AutoMLProblemTypeConfig": "AutoMLProblemTypeConfigTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateAutoMLJobV2RequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoMLJobV2RequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "SecurityConfig": "AutoMLSecurityConfigTypeDef",
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
        "DataSplitConfig": "AutoMLDataSplitConfigTypeDef",
    },
    total=False,
)

class CreateAutoMLJobV2RequestRequestTypeDef(
    _RequiredCreateAutoMLJobV2RequestRequestTypeDef, _OptionalCreateAutoMLJobV2RequestRequestTypeDef
):
    pass

CreateAutoMLJobV2ResponseTypeDef = TypedDict(
    "CreateAutoMLJobV2ResponseTypeDef",
    {
        "AutoMLJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredCreateCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
        "GitConfig": "GitConfigTypeDef",
    },
)
_OptionalCreateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalCreateCodeRepositoryInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCodeRepositoryInputRequestTypeDef(
    _RequiredCreateCodeRepositoryInputRequestTypeDef,
    _OptionalCreateCodeRepositoryInputRequestTypeDef,
):
    pass

CreateCodeRepositoryOutputTypeDef = TypedDict(
    "CreateCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCompilationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
        "RoleArn": str,
        "OutputConfig": "OutputConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalCreateCompilationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCompilationJobRequestRequestTypeDef",
    {
        "ModelPackageVersionArn": str,
        "InputConfig": "InputConfigTypeDef",
        "VpcConfig": "NeoVpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCompilationJobRequestRequestTypeDef(
    _RequiredCreateCompilationJobRequestRequestTypeDef,
    _OptionalCreateCompilationJobRequestRequestTypeDef,
):
    pass

CreateCompilationJobResponseTypeDef = TypedDict(
    "CreateCompilationJobResponseTypeDef",
    {
        "CompilationJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContextRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContextRequestRequestTypeDef",
    {
        "ContextName": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
    },
)
_OptionalCreateContextRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContextRequestRequestTypeDef",
    {
        "Description": str,
        "Properties": Dict[str, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateContextRequestRequestTypeDef(
    _RequiredCreateContextRequestRequestTypeDef, _OptionalCreateContextRequestRequestTypeDef
):
    pass

CreateContextResponseTypeDef = TypedDict(
    "CreateContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "DataQualityAppSpecification": "DataQualityAppSpecificationTypeDef",
        "DataQualityJobInput": "DataQualityJobInputTypeDef",
        "DataQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "DataQualityBaselineConfig": "DataQualityBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataQualityJobDefinitionRequestRequestTypeDef(
    _RequiredCreateDataQualityJobDefinitionRequestRequestTypeDef,
    _OptionalCreateDataQualityJobDefinitionRequestRequestTypeDef,
):
    pass

CreateDataQualityJobDefinitionResponseTypeDef = TypedDict(
    "CreateDataQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
    },
)
_OptionalCreateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceFleetRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "EnableIotRoleAlias": bool,
    },
    total=False,
)

class CreateDeviceFleetRequestRequestTypeDef(
    _RequiredCreateDeviceFleetRequestRequestTypeDef, _OptionalCreateDeviceFleetRequestRequestTypeDef
):
    pass

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": "UserSettingsTypeDef",
        "SubnetIds": List[str],
        "VpcId": str,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "KmsKeyId": str,
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
        "DomainSettings": "DomainSettingsTypeDef",
        "DefaultSpaceSettings": "DefaultSpaceSettingsTypeDef",
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainArn": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "ModelConfigs": List["EdgeDeploymentModelConfigTypeDef"],
        "DeviceFleetName": str,
    },
)
_OptionalCreateEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "Stages": List["DeploymentStageTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEdgeDeploymentPlanRequestRequestTypeDef(
    _RequiredCreateEdgeDeploymentPlanRequestRequestTypeDef,
    _OptionalCreateEdgeDeploymentPlanRequestRequestTypeDef,
):
    pass

CreateEdgeDeploymentPlanResponseTypeDef = TypedDict(
    "CreateEdgeDeploymentPlanResponseTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "CreateEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "Stages": List["DeploymentStageTypeDef"],
    },
)

_RequiredCreateEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
    },
)
_OptionalCreateEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEdgePackagingJobRequestRequestTypeDef",
    {
        "ResourceKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEdgePackagingJobRequestRequestTypeDef(
    _RequiredCreateEdgePackagingJobRequestRequestTypeDef,
    _OptionalCreateEdgePackagingJobRequestRequestTypeDef,
):
    pass

_RequiredCreateEndpointConfigInputRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
        "ProductionVariants": List["ProductionVariantTypeDef"],
    },
)
_OptionalCreateEndpointConfigInputRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointConfigInputRequestTypeDef",
    {
        "DataCaptureConfig": "DataCaptureConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "AsyncInferenceConfig": "AsyncInferenceConfigTypeDef",
        "ExplainerConfig": "ExplainerConfigTypeDef",
        "ShadowProductionVariants": List["ProductionVariantTypeDef"],
    },
    total=False,
)

class CreateEndpointConfigInputRequestTypeDef(
    _RequiredCreateEndpointConfigInputRequestTypeDef,
    _OptionalCreateEndpointConfigInputRequestTypeDef,
):
    pass

CreateEndpointConfigOutputTypeDef = TypedDict(
    "CreateEndpointConfigOutputTypeDef",
    {
        "EndpointConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointInputRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
    },
)
_OptionalCreateEndpointInputRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointInputRequestTypeDef",
    {
        "DeploymentConfig": "DeploymentConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEndpointInputRequestTypeDef(
    _RequiredCreateEndpointInputRequestTypeDef, _OptionalCreateEndpointInputRequestTypeDef
):
    pass

CreateEndpointOutputTypeDef = TypedDict(
    "CreateEndpointOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)
_OptionalCreateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateExperimentRequestRequestTypeDef(
    _RequiredCreateExperimentRequestRequestTypeDef, _OptionalCreateExperimentRequestRequestTypeDef
):
    pass

CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
    },
)
_OptionalCreateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFeatureGroupRequestRequestTypeDef",
    {
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFeatureGroupRequestRequestTypeDef(
    _RequiredCreateFeatureGroupRequestRequestTypeDef,
    _OptionalCreateFeatureGroupRequestRequestTypeDef,
):
    pass

CreateFeatureGroupResponseTypeDef = TypedDict(
    "CreateFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateFlowDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowDefinitionRequestRequestTypeDef",
    {
        "HumanLoopRequestSource": "HumanLoopRequestSourceTypeDef",
        "HumanLoopActivationConfig": "HumanLoopActivationConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFlowDefinitionRequestRequestTypeDef(
    _RequiredCreateFlowDefinitionRequestRequestTypeDef,
    _OptionalCreateFlowDefinitionRequestRequestTypeDef,
):
    pass

CreateFlowDefinitionResponseTypeDef = TypedDict(
    "CreateFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHubRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHubRequestRequestTypeDef",
    {
        "HubName": str,
        "HubDescription": str,
    },
)
_OptionalCreateHubRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHubRequestRequestTypeDef",
    {
        "HubDisplayName": str,
        "HubSearchKeywords": List[str],
        "S3StorageConfig": "HubS3StorageConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHubRequestRequestTypeDef(
    _RequiredCreateHubRequestRequestTypeDef, _OptionalCreateHubRequestRequestTypeDef
):
    pass

CreateHubResponseTypeDef = TypedDict(
    "CreateHubResponseTypeDef",
    {
        "HubArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHumanTaskUiRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
        "UiTemplate": "UiTemplateTypeDef",
    },
)
_OptionalCreateHumanTaskUiRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHumanTaskUiRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHumanTaskUiRequestRequestTypeDef(
    _RequiredCreateHumanTaskUiRequestRequestTypeDef, _OptionalCreateHumanTaskUiRequestRequestTypeDef
):
    pass

CreateHumanTaskUiResponseTypeDef = TypedDict(
    "CreateHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
    },
)
_OptionalCreateHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHyperParameterTuningJobRequestRequestTypeDef",
    {
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "Autotune": "AutotuneTypeDef",
    },
    total=False,
)

class CreateHyperParameterTuningJobRequestRequestTypeDef(
    _RequiredCreateHyperParameterTuningJobRequestRequestTypeDef,
    _OptionalCreateHyperParameterTuningJobRequestRequestTypeDef,
):
    pass

CreateHyperParameterTuningJobResponseTypeDef = TypedDict(
    "CreateHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestRequestTypeDef",
    {
        "ImageName": str,
        "RoleArn": str,
    },
)
_OptionalCreateImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestRequestTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateImageRequestRequestTypeDef(
    _RequiredCreateImageRequestRequestTypeDef, _OptionalCreateImageRequestRequestTypeDef
):
    pass

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageVersionRequestRequestTypeDef",
    {
        "BaseImage": str,
        "ClientToken": str,
        "ImageName": str,
    },
)
_OptionalCreateImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageVersionRequestRequestTypeDef",
    {
        "Aliases": List[str],
        "VendorGuidance": VendorGuidanceType,
        "JobType": JobTypeType,
        "MLFramework": str,
        "ProgrammingLang": str,
        "Processor": ProcessorType,
        "Horovod": bool,
        "ReleaseNotes": str,
    },
    total=False,
)

class CreateImageVersionRequestRequestTypeDef(
    _RequiredCreateImageVersionRequestRequestTypeDef,
    _OptionalCreateImageVersionRequestRequestTypeDef,
):
    pass

CreateImageVersionResponseTypeDef = TypedDict(
    "CreateImageVersionResponseTypeDef",
    {
        "ImageVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
        "Type": Literal["ShadowMode"],
        "RoleArn": str,
        "EndpointName": str,
        "ModelVariants": List["ModelVariantConfigTypeDef"],
        "ShadowModeConfig": "ShadowModeConfigTypeDef",
    },
)
_OptionalCreateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceExperimentRequestRequestTypeDef",
    {
        "Schedule": "InferenceExperimentScheduleTypeDef",
        "Description": str,
        "DataStorageConfig": "InferenceExperimentDataStorageConfigTypeDef",
        "KmsKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateInferenceExperimentRequestRequestTypeDef(
    _RequiredCreateInferenceExperimentRequestRequestTypeDef,
    _OptionalCreateInferenceExperimentRequestRequestTypeDef,
):
    pass

CreateInferenceExperimentResponseTypeDef = TypedDict(
    "CreateInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
        "JobType": RecommendationJobTypeType,
        "RoleArn": str,
        "InputConfig": "RecommendationJobInputConfigTypeDef",
    },
)
_OptionalCreateInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobDescription": str,
        "StoppingConditions": "RecommendationJobStoppingConditionsTypeDef",
        "OutputConfig": "RecommendationJobOutputConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateInferenceRecommendationsJobRequestRequestTypeDef(
    _RequiredCreateInferenceRecommendationsJobRequestRequestTypeDef,
    _OptionalCreateInferenceRecommendationsJobRequestRequestTypeDef,
):
    pass

CreateInferenceRecommendationsJobResponseTypeDef = TypedDict(
    "CreateInferenceRecommendationsJobResponseTypeDef",
    {
        "JobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLabelingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
        "LabelAttributeName": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
    },
)
_OptionalCreateLabelingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLabelingJobRequestRequestTypeDef",
    {
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": "LabelingJobStoppingConditionsTypeDef",
        "LabelingJobAlgorithmsConfig": "LabelingJobAlgorithmsConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateLabelingJobRequestRequestTypeDef(
    _RequiredCreateLabelingJobRequestRequestTypeDef, _OptionalCreateLabelingJobRequestRequestTypeDef
):
    pass

CreateLabelingJobResponseTypeDef = TypedDict(
    "CreateLabelingJobResponseTypeDef",
    {
        "LabelingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelBiasAppSpecification": "ModelBiasAppSpecificationTypeDef",
        "ModelBiasJobInput": "ModelBiasJobInputTypeDef",
        "ModelBiasJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "ModelBiasBaselineConfig": "ModelBiasBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelBiasJobDefinitionRequestRequestTypeDef(
    _RequiredCreateModelBiasJobDefinitionRequestRequestTypeDef,
    _OptionalCreateModelBiasJobDefinitionRequestRequestTypeDef,
):
    pass

CreateModelBiasJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelBiasJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelCardExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelCardExportJobRequestRequestTypeDef",
    {
        "ModelCardName": str,
        "ModelCardExportJobName": str,
        "OutputConfig": "ModelCardExportOutputConfigTypeDef",
    },
)
_OptionalCreateModelCardExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelCardExportJobRequestRequestTypeDef",
    {
        "ModelCardVersion": int,
    },
    total=False,
)

class CreateModelCardExportJobRequestRequestTypeDef(
    _RequiredCreateModelCardExportJobRequestRequestTypeDef,
    _OptionalCreateModelCardExportJobRequestRequestTypeDef,
):
    pass

CreateModelCardExportJobResponseTypeDef = TypedDict(
    "CreateModelCardExportJobResponseTypeDef",
    {
        "ModelCardExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelCardRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
    },
)
_OptionalCreateModelCardRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelCardRequestRequestTypeDef",
    {
        "SecurityConfig": "ModelCardSecurityConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelCardRequestRequestTypeDef(
    _RequiredCreateModelCardRequestRequestTypeDef, _OptionalCreateModelCardRequestRequestTypeDef
):
    pass

CreateModelCardResponseTypeDef = TypedDict(
    "CreateModelCardResponseTypeDef",
    {
        "ModelCardArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelExplainabilityAppSpecification": "ModelExplainabilityAppSpecificationTypeDef",
        "ModelExplainabilityJobInput": "ModelExplainabilityJobInputTypeDef",
        "ModelExplainabilityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "ModelExplainabilityBaselineConfig": "ModelExplainabilityBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelExplainabilityJobDefinitionRequestRequestTypeDef(
    _RequiredCreateModelExplainabilityJobDefinitionRequestRequestTypeDef,
    _OptionalCreateModelExplainabilityJobDefinitionRequestRequestTypeDef,
):
    pass

CreateModelExplainabilityJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelInputRequestTypeDef = TypedDict(
    "_RequiredCreateModelInputRequestTypeDef",
    {
        "ModelName": str,
        "ExecutionRoleArn": str,
    },
)
_OptionalCreateModelInputRequestTypeDef = TypedDict(
    "_OptionalCreateModelInputRequestTypeDef",
    {
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "InferenceExecutionConfig": "InferenceExecutionConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "EnableNetworkIsolation": bool,
    },
    total=False,
)

class CreateModelInputRequestTypeDef(
    _RequiredCreateModelInputRequestTypeDef, _OptionalCreateModelInputRequestTypeDef
):
    pass

CreateModelOutputTypeDef = TypedDict(
    "CreateModelOutputTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelPackageGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)
_OptionalCreateModelPackageGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupDescription": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelPackageGroupInputRequestTypeDef(
    _RequiredCreateModelPackageGroupInputRequestTypeDef,
    _OptionalCreateModelPackageGroupInputRequestTypeDef,
):
    pass

CreateModelPackageGroupOutputTypeDef = TypedDict(
    "CreateModelPackageGroupOutputTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelPackageInputRequestTypeDef = TypedDict(
    "CreateModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageDescription": str,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "CertifyForMarketplace": bool,
        "Tags": List["TagTypeDef"],
        "ModelApprovalStatus": ModelApprovalStatusType,
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "ClientToken": str,
        "CustomerMetadataProperties": Dict[str, str],
        "DriftCheckBaselines": "DriftCheckBaselinesTypeDef",
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ],
        "SkipModelValidation": SkipModelValidationType,
    },
    total=False,
)

CreateModelPackageOutputTypeDef = TypedDict(
    "CreateModelPackageOutputTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
        "ModelQualityAppSpecification": "ModelQualityAppSpecificationTypeDef",
        "ModelQualityJobInput": "ModelQualityJobInputTypeDef",
        "ModelQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "ModelQualityBaselineConfig": "ModelQualityBaselineConfigTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelQualityJobDefinitionRequestRequestTypeDef(
    _RequiredCreateModelQualityJobDefinitionRequestRequestTypeDef,
    _OptionalCreateModelQualityJobDefinitionRequestRequestTypeDef,
):
    pass

CreateModelQualityJobDefinitionResponseTypeDef = TypedDict(
    "CreateModelQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
    },
)
_OptionalCreateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMonitoringScheduleRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMonitoringScheduleRequestRequestTypeDef(
    _RequiredCreateMonitoringScheduleRequestRequestTypeDef,
    _OptionalCreateMonitoringScheduleRequestRequestTypeDef,
):
    pass

CreateMonitoringScheduleResponseTypeDef = TypedDict(
    "CreateMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_RequiredCreateNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
    },
)
_OptionalCreateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_OptionalCreateNotebookInstanceInputRequestTypeDef",
    {
        "SubnetId": str,
        "SecurityGroupIds": List[str],
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "LifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": RootAccessType,
        "PlatformIdentifier": str,
        "InstanceMetadataServiceConfiguration": "InstanceMetadataServiceConfigurationTypeDef",
    },
    total=False,
)

class CreateNotebookInstanceInputRequestTypeDef(
    _RequiredCreateNotebookInstanceInputRequestTypeDef,
    _OptionalCreateNotebookInstanceInputRequestTypeDef,
):
    pass

_RequiredCreateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_RequiredCreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)
_OptionalCreateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_OptionalCreateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
    },
    total=False,
)

class CreateNotebookInstanceLifecycleConfigInputRequestTypeDef(
    _RequiredCreateNotebookInstanceLifecycleConfigInputRequestTypeDef,
    _OptionalCreateNotebookInstanceLifecycleConfigInputRequestTypeDef,
):
    pass

CreateNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNotebookInstanceOutputTypeDef = TypedDict(
    "CreateNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
        "RoleArn": str,
    },
)
_OptionalCreatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineRequestRequestTypeDef",
    {
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDefinitionS3Location": "PipelineDefinitionS3LocationTypeDef",
        "PipelineDescription": str,
        "Tags": List["TagTypeDef"],
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
    },
    total=False,
)

class CreatePipelineRequestRequestTypeDef(
    _RequiredCreatePipelineRequestRequestTypeDef, _OptionalCreatePipelineRequestRequestTypeDef
):
    pass

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePresignedDomainUrlRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePresignedDomainUrlRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalCreatePresignedDomainUrlRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePresignedDomainUrlRequestRequestTypeDef",
    {
        "SessionExpirationDurationInSeconds": int,
        "ExpiresInSeconds": int,
        "SpaceName": str,
    },
    total=False,
)

class CreatePresignedDomainUrlRequestRequestTypeDef(
    _RequiredCreatePresignedDomainUrlRequestRequestTypeDef,
    _OptionalCreatePresignedDomainUrlRequestRequestTypeDef,
):
    pass

CreatePresignedDomainUrlResponseTypeDef = TypedDict(
    "CreatePresignedDomainUrlResponseTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePresignedNotebookInstanceUrlInputRequestTypeDef = TypedDict(
    "_RequiredCreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalCreatePresignedNotebookInstanceUrlInputRequestTypeDef = TypedDict(
    "_OptionalCreatePresignedNotebookInstanceUrlInputRequestTypeDef",
    {
        "SessionExpirationDurationInSeconds": int,
    },
    total=False,
)

class CreatePresignedNotebookInstanceUrlInputRequestTypeDef(
    _RequiredCreatePresignedNotebookInstanceUrlInputRequestTypeDef,
    _OptionalCreatePresignedNotebookInstanceUrlInputRequestTypeDef,
):
    pass

CreatePresignedNotebookInstanceUrlOutputTypeDef = TypedDict(
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    {
        "AuthorizedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProcessingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateProcessingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProcessingJobRequestRequestTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "ExperimentConfig": "ExperimentConfigTypeDef",
    },
    total=False,
)

class CreateProcessingJobRequestRequestTypeDef(
    _RequiredCreateProcessingJobRequestRequestTypeDef,
    _OptionalCreateProcessingJobRequestRequestTypeDef,
):
    pass

CreateProcessingJobResponseTypeDef = TypedDict(
    "CreateProcessingJobResponseTypeDef",
    {
        "ProcessingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectInputRequestTypeDef = TypedDict(
    "_RequiredCreateProjectInputRequestTypeDef",
    {
        "ProjectName": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
    },
)
_OptionalCreateProjectInputRequestTypeDef = TypedDict(
    "_OptionalCreateProjectInputRequestTypeDef",
    {
        "ProjectDescription": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProjectInputRequestTypeDef(
    _RequiredCreateProjectInputRequestTypeDef, _OptionalCreateProjectInputRequestTypeDef
):
    pass

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ProjectId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSpaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)
_OptionalCreateSpaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSpaceRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "SpaceSettings": "SpaceSettingsTypeDef",
    },
    total=False,
)

class CreateSpaceRequestRequestTypeDef(
    _RequiredCreateSpaceRequestRequestTypeDef, _OptionalCreateSpaceRequestRequestTypeDef
):
    pass

CreateSpaceResponseTypeDef = TypedDict(
    "CreateSpaceResponseTypeDef",
    {
        "SpaceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
        "StudioLifecycleConfigContent": str,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
    },
)
_OptionalCreateStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStudioLifecycleConfigRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateStudioLifecycleConfigRequestRequestTypeDef(
    _RequiredCreateStudioLifecycleConfigRequestRequestTypeDef,
    _OptionalCreateStudioLifecycleConfigRequestRequestTypeDef,
):
    pass

CreateStudioLifecycleConfigResponseTypeDef = TypedDict(
    "CreateStudioLifecycleConfigResponseTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrainingJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalCreateTrainingJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrainingJobRequestRequestTypeDef",
    {
        "HyperParameters": Dict[str, str],
        "InputDataConfig": List["ChannelTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProfilerConfig": "ProfilerConfigTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
        "Environment": Dict[str, str],
        "RetryStrategy": "RetryStrategyTypeDef",
    },
    total=False,
)

class CreateTrainingJobRequestRequestTypeDef(
    _RequiredCreateTrainingJobRequestRequestTypeDef, _OptionalCreateTrainingJobRequestRequestTypeDef
):
    pass

CreateTrainingJobResponseTypeDef = TypedDict(
    "CreateTrainingJobResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransformJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
        "ModelName": str,
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
    },
)
_OptionalCreateTransformJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransformJobRequestRequestTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "DataCaptureConfig": "BatchDataCaptureConfigTypeDef",
        "DataProcessing": "DataProcessingTypeDef",
        "Tags": List["TagTypeDef"],
        "ExperimentConfig": "ExperimentConfigTypeDef",
    },
    total=False,
)

class CreateTransformJobRequestRequestTypeDef(
    _RequiredCreateTransformJobRequestRequestTypeDef,
    _OptionalCreateTransformJobRequestRequestTypeDef,
):
    pass

CreateTransformJobResponseTypeDef = TypedDict(
    "CreateTransformJobResponseTypeDef",
    {
        "TransformJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrialComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)
_OptionalCreateTrialComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrialComponentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrialComponentRequestRequestTypeDef(
    _RequiredCreateTrialComponentRequestRequestTypeDef,
    _OptionalCreateTrialComponentRequestRequestTypeDef,
):
    pass

CreateTrialComponentResponseTypeDef = TypedDict(
    "CreateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrialRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrialRequestRequestTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
    },
)
_OptionalCreateTrialRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrialRequestRequestTypeDef",
    {
        "DisplayName": str,
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrialRequestRequestTypeDef(
    _RequiredCreateTrialRequestRequestTypeDef, _OptionalCreateTrialRequestRequestTypeDef
):
    pass

CreateTrialResponseTypeDef = TypedDict(
    "CreateTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalCreateUserProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserProfileRequestRequestTypeDef",
    {
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "Tags": List["TagTypeDef"],
        "UserSettings": "UserSettingsTypeDef",
    },
    total=False,
)

class CreateUserProfileRequestRequestTypeDef(
    _RequiredCreateUserProfileRequestRequestTypeDef, _OptionalCreateUserProfileRequestRequestTypeDef
):
    pass

CreateUserProfileResponseTypeDef = TypedDict(
    "CreateUserProfileResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkforceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)
_OptionalCreateWorkforceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkforceRequestRequestTypeDef",
    {
        "CognitoConfig": "CognitoConfigTypeDef",
        "OidcConfig": "OidcConfigTypeDef",
        "SourceIpConfig": "SourceIpConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "WorkforceVpcConfig": "WorkforceVpcConfigRequestTypeDef",
    },
    total=False,
)

class CreateWorkforceRequestRequestTypeDef(
    _RequiredCreateWorkforceRequestRequestTypeDef, _OptionalCreateWorkforceRequestRequestTypeDef
):
    pass

CreateWorkforceResponseTypeDef = TypedDict(
    "CreateWorkforceResponseTypeDef",
    {
        "WorkforceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkteamRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "Description": str,
    },
)
_OptionalCreateWorkteamRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkteamRequestRequestTypeDef",
    {
        "WorkforceName": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkteamRequestRequestTypeDef(
    _RequiredCreateWorkteamRequestRequestTypeDef, _OptionalCreateWorkteamRequestRequestTypeDef
):
    pass

CreateWorkteamResponseTypeDef = TypedDict(
    "CreateWorkteamResponseTypeDef",
    {
        "WorkteamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomImageTypeDef = TypedDict(
    "_RequiredCustomImageTypeDef",
    {
        "ImageName": str,
        "AppImageConfigName": str,
    },
)
_OptionalCustomImageTypeDef = TypedDict(
    "_OptionalCustomImageTypeDef",
    {
        "ImageVersionNumber": int,
    },
    total=False,
)

class CustomImageTypeDef(_RequiredCustomImageTypeDef, _OptionalCustomImageTypeDef):
    pass

CustomizedMetricSpecificationTypeDef = TypedDict(
    "CustomizedMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
    },
    total=False,
)

DataCaptureConfigSummaryTypeDef = TypedDict(
    "DataCaptureConfigSummaryTypeDef",
    {
        "EnableCapture": bool,
        "CaptureStatus": CaptureStatusType,
        "CurrentSamplingPercentage": int,
        "DestinationS3Uri": str,
        "KmsKeyId": str,
    },
)

_RequiredDataCaptureConfigTypeDef = TypedDict(
    "_RequiredDataCaptureConfigTypeDef",
    {
        "InitialSamplingPercentage": int,
        "DestinationS3Uri": str,
        "CaptureOptions": List["CaptureOptionTypeDef"],
    },
)
_OptionalDataCaptureConfigTypeDef = TypedDict(
    "_OptionalDataCaptureConfigTypeDef",
    {
        "EnableCapture": bool,
        "KmsKeyId": str,
        "CaptureContentTypeHeader": "CaptureContentTypeHeaderTypeDef",
    },
    total=False,
)

class DataCaptureConfigTypeDef(
    _RequiredDataCaptureConfigTypeDef, _OptionalDataCaptureConfigTypeDef
):
    pass

DataCatalogConfigTypeDef = TypedDict(
    "DataCatalogConfigTypeDef",
    {
        "TableName": str,
        "Catalog": str,
        "Database": str,
    },
)

DataProcessingTypeDef = TypedDict(
    "DataProcessingTypeDef",
    {
        "InputFilter": str,
        "OutputFilter": str,
        "JoinSource": JoinSourceType,
    },
    total=False,
)

_RequiredDataQualityAppSpecificationTypeDef = TypedDict(
    "_RequiredDataQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalDataQualityAppSpecificationTypeDef = TypedDict(
    "_OptionalDataQualityAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "Environment": Dict[str, str],
    },
    total=False,
)

class DataQualityAppSpecificationTypeDef(
    _RequiredDataQualityAppSpecificationTypeDef, _OptionalDataQualityAppSpecificationTypeDef
):
    pass

DataQualityBaselineConfigTypeDef = TypedDict(
    "DataQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
        "StatisticsResource": "MonitoringStatisticsResourceTypeDef",
    },
    total=False,
)

DataQualityJobInputTypeDef = TypedDict(
    "DataQualityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "BatchTransformInput": "BatchTransformInputTypeDef",
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3DataSource": "S3DataSourceTypeDef",
        "FileSystemDataSource": "FileSystemDataSourceTypeDef",
    },
    total=False,
)

DatasetDefinitionTypeDef = TypedDict(
    "DatasetDefinitionTypeDef",
    {
        "AthenaDatasetDefinition": "AthenaDatasetDefinitionTypeDef",
        "RedshiftDatasetDefinition": "RedshiftDatasetDefinitionTypeDef",
        "LocalPath": str,
        "DataDistributionType": DataDistributionTypeType,
        "InputMode": InputModeType,
    },
    total=False,
)

_RequiredDebugHookConfigTypeDef = TypedDict(
    "_RequiredDebugHookConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalDebugHookConfigTypeDef = TypedDict(
    "_OptionalDebugHookConfigTypeDef",
    {
        "LocalPath": str,
        "HookParameters": Dict[str, str],
        "CollectionConfigurations": List["CollectionConfigurationTypeDef"],
    },
    total=False,
)

class DebugHookConfigTypeDef(_RequiredDebugHookConfigTypeDef, _OptionalDebugHookConfigTypeDef):
    pass

_RequiredDebugRuleConfigurationTypeDef = TypedDict(
    "_RequiredDebugRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalDebugRuleConfigurationTypeDef = TypedDict(
    "_OptionalDebugRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)

class DebugRuleConfigurationTypeDef(
    _RequiredDebugRuleConfigurationTypeDef, _OptionalDebugRuleConfigurationTypeDef
):
    pass

DebugRuleEvaluationStatusTypeDef = TypedDict(
    "DebugRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": RuleEvaluationStatusType,
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

DefaultSpaceSettingsTypeDef = TypedDict(
    "DefaultSpaceSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "JupyterServerAppSettings": "JupyterServerAppSettingsTypeDef",
        "KernelGatewayAppSettings": "KernelGatewayAppSettingsTypeDef",
    },
    total=False,
)

DeleteActionRequestRequestTypeDef = TypedDict(
    "DeleteActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)

DeleteActionResponseTypeDef = TypedDict(
    "DeleteActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlgorithmInputRequestTypeDef = TypedDict(
    "DeleteAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
    },
)

DeleteAppImageConfigRequestRequestTypeDef = TypedDict(
    "DeleteAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

_RequiredDeleteAppRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalDeleteAppRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppRequestRequestTypeDef",
    {
        "UserProfileName": str,
        "SpaceName": str,
    },
    total=False,
)

class DeleteAppRequestRequestTypeDef(
    _RequiredDeleteAppRequestRequestTypeDef, _OptionalDeleteAppRequestRequestTypeDef
):
    pass

DeleteArtifactRequestRequestTypeDef = TypedDict(
    "DeleteArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
        "Source": "ArtifactSourceTypeDef",
    },
    total=False,
)

DeleteArtifactResponseTypeDef = TypedDict(
    "DeleteArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssociationRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
    },
)

DeleteAssociationResponseTypeDef = TypedDict(
    "DeleteAssociationResponseTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCodeRepositoryInputRequestTypeDef = TypedDict(
    "DeleteCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DeleteContextRequestRequestTypeDef = TypedDict(
    "DeleteContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)

DeleteContextResponseTypeDef = TypedDict(
    "DeleteContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteDeviceFleetRequestRequestTypeDef = TypedDict(
    "DeleteDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

_RequiredDeleteDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalDeleteDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainRequestRequestTypeDef",
    {
        "RetentionPolicy": "RetentionPolicyTypeDef",
    },
    total=False,
)

class DeleteDomainRequestRequestTypeDef(
    _RequiredDeleteDomainRequestRequestTypeDef, _OptionalDeleteDomainRequestRequestTypeDef
):
    pass

DeleteEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "DeleteEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
    },
)

DeleteEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "DeleteEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)

DeleteEndpointConfigInputRequestTypeDef = TypedDict(
    "DeleteEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DeleteEndpointInputRequestTypeDef = TypedDict(
    "DeleteEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DeleteExperimentResponseTypeDef = TypedDict(
    "DeleteExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFeatureGroupRequestRequestTypeDef = TypedDict(
    "DeleteFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)

DeleteFlowDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DeleteHubContentRequestRequestTypeDef = TypedDict(
    "DeleteHubContentRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
        "HubContentName": str,
        "HubContentVersion": str,
    },
)

DeleteHubRequestRequestTypeDef = TypedDict(
    "DeleteHubRequestRequestTypeDef",
    {
        "HubName": str,
    },
)

DeleteHumanTaskUiRequestRequestTypeDef = TypedDict(
    "DeleteHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)

_RequiredDeleteImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDeleteImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteImageVersionRequestRequestTypeDef",
    {
        "Version": int,
        "Alias": str,
    },
    total=False,
)

class DeleteImageVersionRequestRequestTypeDef(
    _RequiredDeleteImageVersionRequestRequestTypeDef,
    _OptionalDeleteImageVersionRequestRequestTypeDef,
):
    pass

DeleteInferenceExperimentRequestRequestTypeDef = TypedDict(
    "DeleteInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteInferenceExperimentResponseTypeDef = TypedDict(
    "DeleteInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelCardRequestRequestTypeDef = TypedDict(
    "DeleteModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)

DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteModelInputRequestTypeDef = TypedDict(
    "DeleteModelInputRequestTypeDef",
    {
        "ModelName": str,
    },
)

DeleteModelPackageGroupInputRequestTypeDef = TypedDict(
    "DeleteModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "DeleteModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DeleteModelPackageInputRequestTypeDef = TypedDict(
    "DeleteModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
    },
)

DeleteModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DeleteMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "DeleteMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DeleteNotebookInstanceInputRequestTypeDef = TypedDict(
    "DeleteNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "DeleteNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)

DeletePipelineResponseTypeDef = TypedDict(
    "DeletePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DeleteSpaceRequestRequestTypeDef = TypedDict(
    "DeleteSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)

DeleteStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "DeleteStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
    },
)

DeleteTagsInputRequestTypeDef = TypedDict(
    "DeleteTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DeleteTrialComponentRequestRequestTypeDef = TypedDict(
    "DeleteTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DeleteTrialComponentResponseTypeDef = TypedDict(
    "DeleteTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTrialRequestRequestTypeDef = TypedDict(
    "DeleteTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)

DeleteTrialResponseTypeDef = TypedDict(
    "DeleteTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DeleteWorkforceRequestRequestTypeDef = TypedDict(
    "DeleteWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DeleteWorkteamRequestRequestTypeDef = TypedDict(
    "DeleteWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DeleteWorkteamResponseTypeDef = TypedDict(
    "DeleteWorkteamResponseTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeployedImageTypeDef = TypedDict(
    "DeployedImageTypeDef",
    {
        "SpecifiedImage": str,
        "ResolvedImage": str,
        "ResolutionTime": datetime,
    },
    total=False,
)

DeploymentConfigTypeDef = TypedDict(
    "DeploymentConfigTypeDef",
    {
        "BlueGreenUpdatePolicy": "BlueGreenUpdatePolicyTypeDef",
        "AutoRollbackConfiguration": "AutoRollbackConfigTypeDef",
        "RollingUpdatePolicy": "RollingUpdatePolicyTypeDef",
    },
    total=False,
)

_RequiredDeploymentRecommendationTypeDef = TypedDict(
    "_RequiredDeploymentRecommendationTypeDef",
    {
        "RecommendationStatus": RecommendationStatusType,
    },
)
_OptionalDeploymentRecommendationTypeDef = TypedDict(
    "_OptionalDeploymentRecommendationTypeDef",
    {
        "RealTimeInferenceRecommendations": List["RealTimeInferenceRecommendationTypeDef"],
    },
    total=False,
)

class DeploymentRecommendationTypeDef(
    _RequiredDeploymentRecommendationTypeDef, _OptionalDeploymentRecommendationTypeDef
):
    pass

DeploymentStageStatusSummaryTypeDef = TypedDict(
    "DeploymentStageStatusSummaryTypeDef",
    {
        "StageName": str,
        "DeviceSelectionConfig": "DeviceSelectionConfigTypeDef",
        "DeploymentConfig": "EdgeDeploymentConfigTypeDef",
        "DeploymentStatus": "EdgeDeploymentStatusTypeDef",
    },
)

_RequiredDeploymentStageTypeDef = TypedDict(
    "_RequiredDeploymentStageTypeDef",
    {
        "StageName": str,
        "DeviceSelectionConfig": "DeviceSelectionConfigTypeDef",
    },
)
_OptionalDeploymentStageTypeDef = TypedDict(
    "_OptionalDeploymentStageTypeDef",
    {
        "DeploymentConfig": "EdgeDeploymentConfigTypeDef",
    },
    total=False,
)

class DeploymentStageTypeDef(_RequiredDeploymentStageTypeDef, _OptionalDeploymentStageTypeDef):
    pass

DeregisterDevicesRequestRequestTypeDef = TypedDict(
    "DeregisterDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceNames": List[str],
    },
)

DerivedInformationTypeDef = TypedDict(
    "DerivedInformationTypeDef",
    {
        "DerivedDataInputConfig": str,
    },
    total=False,
)

DescribeActionRequestRequestTypeDef = TypedDict(
    "DescribeActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)

DescribeActionResponseTypeDef = TypedDict(
    "DescribeActionResponseTypeDef",
    {
        "ActionName": str,
        "ActionArn": str,
        "Source": "ActionSourceTypeDef",
        "ActionType": str,
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlgorithmInputRequestTypeDef = TypedDict(
    "DescribeAlgorithmInputRequestTypeDef",
    {
        "AlgorithmName": str,
    },
)

DescribeAlgorithmOutputTypeDef = TypedDict(
    "DescribeAlgorithmOutputTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "AlgorithmDescription": str,
        "CreationTime": datetime,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "AlgorithmValidationSpecificationTypeDef",
        "AlgorithmStatus": AlgorithmStatusType,
        "AlgorithmStatusDetails": "AlgorithmStatusDetailsTypeDef",
        "ProductId": str,
        "CertifyForMarketplace": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppImageConfigRequestRequestTypeDef = TypedDict(
    "DescribeAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)

DescribeAppImageConfigResponseTypeDef = TypedDict(
    "DescribeAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAppRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAppRequestRequestTypeDef",
    {
        "DomainId": str,
        "AppType": AppTypeType,
        "AppName": str,
    },
)
_OptionalDescribeAppRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAppRequestRequestTypeDef",
    {
        "UserProfileName": str,
        "SpaceName": str,
    },
    total=False,
)

class DescribeAppRequestRequestTypeDef(
    _RequiredDescribeAppRequestRequestTypeDef, _OptionalDescribeAppRequestRequestTypeDef
):
    pass

DescribeAppResponseTypeDef = TypedDict(
    "DescribeAppResponseTypeDef",
    {
        "AppArn": str,
        "AppType": AppTypeType,
        "AppName": str,
        "DomainId": str,
        "UserProfileName": str,
        "Status": AppStatusType,
        "LastHealthCheckTimestamp": datetime,
        "LastUserActivityTimestamp": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "ResourceSpec": "ResourceSpecTypeDef",
        "SpaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArtifactRequestRequestTypeDef = TypedDict(
    "DescribeArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)

DescribeArtifactResponseTypeDef = TypedDict(
    "DescribeArtifactResponseTypeDef",
    {
        "ArtifactName": str,
        "ArtifactArn": str,
        "Source": "ArtifactSourceTypeDef",
        "ArtifactType": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoMLJobRequestRequestTypeDef = TypedDict(
    "DescribeAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

DescribeAutoMLJobResponseTypeDef = TypedDict(
    "DescribeAutoMLJobResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "InputDataConfig": List["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": ProblemTypeType,
        "AutoMLJobConfig": "AutoMLJobConfigTypeDef",
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List["AutoMLPartialFailureReasonTypeDef"],
        "BestCandidate": "AutoMLCandidateTypeDef",
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "GenerateCandidateDefinitionsOnly": bool,
        "AutoMLJobArtifacts": "AutoMLJobArtifactsTypeDef",
        "ResolvedAttributes": "ResolvedAttributesTypeDef",
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
        "ModelDeployResult": "ModelDeployResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutoMLJobV2RequestRequestTypeDef = TypedDict(
    "DescribeAutoMLJobV2RequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

DescribeAutoMLJobV2ResponseTypeDef = TypedDict(
    "DescribeAutoMLJobV2ResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobInputDataConfig": List["AutoMLJobChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "AutoMLProblemTypeConfig": "AutoMLProblemTypeConfigTypeDef",
        "CreationTime": datetime,
        "EndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "PartialFailureReasons": List["AutoMLPartialFailureReasonTypeDef"],
        "BestCandidate": "AutoMLCandidateTypeDef",
        "AutoMLJobStatus": AutoMLJobStatusType,
        "AutoMLJobSecondaryStatus": AutoMLJobSecondaryStatusType,
        "ModelDeployConfig": "ModelDeployConfigTypeDef",
        "ModelDeployResult": "ModelDeployResultTypeDef",
        "DataSplitConfig": "AutoMLDataSplitConfigTypeDef",
        "SecurityConfig": "AutoMLSecurityConfigTypeDef",
        "AutoMLJobArtifacts": "AutoMLJobArtifactsTypeDef",
        "ResolvedAttributes": "AutoMLResolvedAttributesTypeDef",
        "AutoMLProblemTypeConfigName": AutoMLProblemTypeConfigNameType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeRepositoryInputRequestTypeDef = TypedDict(
    "DescribeCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)

DescribeCodeRepositoryOutputTypeDef = TypedDict(
    "DescribeCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "GitConfig": "GitConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCompilationJobRequestRequestTypeDef = TypedDict(
    "DescribeCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

DescribeCompilationJobResponseTypeDef = TypedDict(
    "DescribeCompilationJobResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": CompilationJobStatusType,
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "StoppingCondition": "StoppingConditionTypeDef",
        "InferenceImage": str,
        "ModelPackageVersionArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "ModelDigests": "ModelDigestsTypeDef",
        "RoleArn": str,
        "InputConfig": "InputConfigTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "VpcConfig": "NeoVpcConfigTypeDef",
        "DerivedInformation": "DerivedInformationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContextRequestRequestTypeDef = TypedDict(
    "DescribeContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)

DescribeContextResponseTypeDef = TypedDict(
    "DescribeContextResponseTypeDef",
    {
        "ContextName": str,
        "ContextArn": str,
        "Source": "ContextSourceTypeDef",
        "ContextType": str,
        "Description": str,
        "Properties": Dict[str, str],
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "LineageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeDataQualityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "DataQualityBaselineConfig": "DataQualityBaselineConfigTypeDef",
        "DataQualityAppSpecification": "DataQualityAppSpecificationTypeDef",
        "DataQualityJobInput": "DataQualityJobInputTypeDef",
        "DataQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceFleetRequestRequestTypeDef = TypedDict(
    "DescribeDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

DescribeDeviceFleetResponseTypeDef = TypedDict(
    "DescribeDeviceFleetResponseTypeDef",
    {
        "DeviceFleetName": str,
        "DeviceFleetArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "IotRoleAlias": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDeviceRequestRequestTypeDef",
    {
        "DeviceName": str,
        "DeviceFleetName": str,
    },
)
_OptionalDescribeDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDeviceRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class DescribeDeviceRequestRequestTypeDef(
    _RequiredDescribeDeviceRequestRequestTypeDef, _OptionalDescribeDeviceRequestRequestTypeDef
):
    pass

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceArn": str,
        "DeviceName": str,
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List["EdgeModelTypeDef"],
        "MaxModels": int,
        "NextToken": str,
        "AgentVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "HomeEfsFileSystemId": str,
        "SingleSignOnManagedApplicationInstanceId": str,
        "SingleSignOnApplicationArn": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "AuthMode": AuthModeType,
        "DefaultUserSettings": "UserSettingsTypeDef",
        "AppNetworkAccessType": AppNetworkAccessTypeType,
        "HomeEfsFileSystemKmsKeyId": str,
        "SubnetIds": List[str],
        "Url": str,
        "VpcId": str,
        "KmsKeyId": str,
        "DomainSettings": "DomainSettingsTypeDef",
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
        "SecurityGroupIdForDomainBoundary": str,
        "DefaultSpaceSettings": "DefaultSpaceSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
    },
)
_OptionalDescribeEdgeDeploymentPlanRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEdgeDeploymentPlanRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeEdgeDeploymentPlanRequestRequestTypeDef(
    _RequiredDescribeEdgeDeploymentPlanRequestRequestTypeDef,
    _OptionalDescribeEdgeDeploymentPlanRequestRequestTypeDef,
):
    pass

DescribeEdgeDeploymentPlanResponseTypeDef = TypedDict(
    "DescribeEdgeDeploymentPlanResponseTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "EdgeDeploymentPlanName": str,
        "ModelConfigs": List["EdgeDeploymentModelConfigTypeDef"],
        "DeviceFleetName": str,
        "EdgeDeploymentSuccess": int,
        "EdgeDeploymentPending": int,
        "EdgeDeploymentFailed": int,
        "Stages": List["DeploymentStageStatusSummaryTypeDef"],
        "NextToken": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "DescribeEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

DescribeEdgePackagingJobResponseTypeDef = TypedDict(
    "DescribeEdgePackagingJobResponseTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "RoleArn": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "ResourceKey": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
        "EdgePackagingJobStatusMessage": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ModelArtifact": str,
        "ModelSignature": str,
        "PresetDeploymentOutput": "EdgePresetDeploymentOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointConfigInputRequestTypeDef = TypedDict(
    "DescribeEndpointConfigInputRequestTypeDef",
    {
        "EndpointConfigName": str,
    },
)

DescribeEndpointConfigOutputTypeDef = TypedDict(
    "DescribeEndpointConfigOutputTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List["ProductionVariantTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigTypeDef",
        "KmsKeyId": str,
        "CreationTime": datetime,
        "AsyncInferenceConfig": "AsyncInferenceConfigTypeDef",
        "ExplainerConfig": "ExplainerConfigTypeDef",
        "ShadowProductionVariants": List["ProductionVariantTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointInputRequestTypeDef = TypedDict(
    "DescribeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DescribeEndpointOutputTypeDef = TypedDict(
    "DescribeEndpointOutputTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "ProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigSummaryTypeDef",
        "EndpointStatus": EndpointStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastDeploymentConfig": "DeploymentConfigTypeDef",
        "AsyncInferenceConfig": "AsyncInferenceConfigTypeDef",
        "PendingDeploymentSummary": "PendingDeploymentSummaryTypeDef",
        "ExplainerConfig": "ExplainerConfigTypeDef",
        "ShadowProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExperimentRequestRequestTypeDef = TypedDict(
    "DescribeExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)

DescribeExperimentResponseTypeDef = TypedDict(
    "DescribeExperimentResponseTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": "ExperimentSourceTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFeatureGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)
_OptionalDescribeFeatureGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFeatureGroupRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class DescribeFeatureGroupRequestRequestTypeDef(
    _RequiredDescribeFeatureGroupRequestRequestTypeDef,
    _OptionalDescribeFeatureGroupRequestRequestTypeDef,
):
    pass

DescribeFeatureGroupResponseTypeDef = TypedDict(
    "DescribeFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
        "LastUpdateStatus": "LastUpdateStatusTypeDef",
        "FailureReason": str,
        "Description": str,
        "NextToken": str,
        "OnlineStoreTotalSizeBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeatureMetadataRequestRequestTypeDef = TypedDict(
    "DescribeFeatureMetadataRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureName": str,
    },
)

DescribeFeatureMetadataResponseTypeDef = TypedDict(
    "DescribeFeatureMetadataResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Description": str,
        "Parameters": List["FeatureParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeFlowDefinitionRequestRequestTypeDef",
    {
        "FlowDefinitionName": str,
    },
)

DescribeFlowDefinitionResponseTypeDef = TypedDict(
    "DescribeFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "FlowDefinitionName": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
        "HumanLoopRequestSource": "HumanLoopRequestSourceTypeDef",
        "HumanLoopActivationConfig": "HumanLoopActivationConfigTypeDef",
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeHubContentRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeHubContentRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
        "HubContentName": str,
    },
)
_OptionalDescribeHubContentRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeHubContentRequestRequestTypeDef",
    {
        "HubContentVersion": str,
    },
    total=False,
)

class DescribeHubContentRequestRequestTypeDef(
    _RequiredDescribeHubContentRequestRequestTypeDef,
    _OptionalDescribeHubContentRequestRequestTypeDef,
):
    pass

DescribeHubContentResponseTypeDef = TypedDict(
    "DescribeHubContentResponseTypeDef",
    {
        "HubContentName": str,
        "HubContentArn": str,
        "HubContentVersion": str,
        "HubContentType": HubContentTypeType,
        "DocumentSchemaVersion": str,
        "HubName": str,
        "HubArn": str,
        "HubContentDisplayName": str,
        "HubContentDescription": str,
        "HubContentMarkdown": str,
        "HubContentDocument": str,
        "HubContentSearchKeywords": List[str],
        "HubContentDependencies": List["HubContentDependencyTypeDef"],
        "HubContentStatus": HubContentStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHubRequestRequestTypeDef = TypedDict(
    "DescribeHubRequestRequestTypeDef",
    {
        "HubName": str,
    },
)

DescribeHubResponseTypeDef = TypedDict(
    "DescribeHubResponseTypeDef",
    {
        "HubName": str,
        "HubArn": str,
        "HubDisplayName": str,
        "HubDescription": str,
        "HubSearchKeywords": List[str],
        "S3StorageConfig": "HubS3StorageConfigTypeDef",
        "HubStatus": HubStatusType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHumanTaskUiRequestRequestTypeDef = TypedDict(
    "DescribeHumanTaskUiRequestRequestTypeDef",
    {
        "HumanTaskUiName": str,
    },
)

DescribeHumanTaskUiResponseTypeDef = TypedDict(
    "DescribeHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "HumanTaskUiName": str,
        "HumanTaskUiStatus": HumanTaskUiStatusType,
        "CreationTime": datetime,
        "UiTemplate": "UiTemplateInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

DescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "DescribeHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
        "BestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "OverallBestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "FailureReason": str,
        "TuningJobCompletionDetails": "HyperParameterTuningJobCompletionDetailsTypeDef",
        "ConsumedResources": "HyperParameterTuningJobConsumedResourcesTypeDef",
        "Autotune": "AutotuneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageRequestRequestTypeDef = TypedDict(
    "DescribeImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)

DescribeImageResponseTypeDef = TypedDict(
    "DescribeImageResponseTypeDef",
    {
        "CreationTime": datetime,
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalDescribeImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageVersionRequestRequestTypeDef",
    {
        "Version": int,
        "Alias": str,
    },
    total=False,
)

class DescribeImageVersionRequestRequestTypeDef(
    _RequiredDescribeImageVersionRequestRequestTypeDef,
    _OptionalDescribeImageVersionRequestRequestTypeDef,
):
    pass

DescribeImageVersionResponseTypeDef = TypedDict(
    "DescribeImageVersionResponseTypeDef",
    {
        "BaseImage": str,
        "ContainerImage": str,
        "CreationTime": datetime,
        "FailureReason": str,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
        "VendorGuidance": VendorGuidanceType,
        "JobType": JobTypeType,
        "MLFramework": str,
        "ProgrammingLang": str,
        "Processor": ProcessorType,
        "Horovod": bool,
        "ReleaseNotes": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInferenceExperimentRequestRequestTypeDef = TypedDict(
    "DescribeInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeInferenceExperimentResponseTypeDef = TypedDict(
    "DescribeInferenceExperimentResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": Literal["ShadowMode"],
        "Schedule": "InferenceExperimentScheduleTypeDef",
        "Status": InferenceExperimentStatusType,
        "StatusReason": str,
        "Description": str,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LastModifiedTime": datetime,
        "RoleArn": str,
        "EndpointMetadata": "EndpointMetadataTypeDef",
        "ModelVariants": List["ModelVariantConfigSummaryTypeDef"],
        "DataStorageConfig": "InferenceExperimentDataStorageConfigTypeDef",
        "ShadowModeConfig": "ShadowModeConfigTypeDef",
        "KmsKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "DescribeInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

DescribeInferenceRecommendationsJobResponseTypeDef = TypedDict(
    "DescribeInferenceRecommendationsJobResponseTypeDef",
    {
        "JobName": str,
        "JobDescription": str,
        "JobType": RecommendationJobTypeType,
        "JobArn": str,
        "RoleArn": str,
        "Status": RecommendationJobStatusType,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "InputConfig": "RecommendationJobInputConfigTypeDef",
        "StoppingConditions": "RecommendationJobStoppingConditionsTypeDef",
        "InferenceRecommendations": List["InferenceRecommendationTypeDef"],
        "EndpointPerformances": List["EndpointPerformanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLabelingJobRequestRequestTypeDef = TypedDict(
    "DescribeLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

DescribeLabelingJobResponseTypeDef = TypedDict(
    "DescribeLabelingJobResponseTypeDef",
    {
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": "LabelCountersTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "LabelAttributeName": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": "LabelingJobStoppingConditionsTypeDef",
        "LabelingJobAlgorithmsConfig": "LabelingJobAlgorithmsConfigTypeDef",
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "LabelingJobOutput": "LabelingJobOutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLineageGroupRequestRequestTypeDef = TypedDict(
    "DescribeLineageGroupRequestRequestTypeDef",
    {
        "LineageGroupName": str,
    },
)

DescribeLineageGroupResponseTypeDef = TypedDict(
    "DescribeLineageGroupResponseTypeDef",
    {
        "LineageGroupName": str,
        "LineageGroupArn": str,
        "DisplayName": str,
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelBiasJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelBiasJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelBiasBaselineConfig": "ModelBiasBaselineConfigTypeDef",
        "ModelBiasAppSpecification": "ModelBiasAppSpecificationTypeDef",
        "ModelBiasJobInput": "ModelBiasJobInputTypeDef",
        "ModelBiasJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelCardExportJobRequestRequestTypeDef = TypedDict(
    "DescribeModelCardExportJobRequestRequestTypeDef",
    {
        "ModelCardExportJobArn": str,
    },
)

DescribeModelCardExportJobResponseTypeDef = TypedDict(
    "DescribeModelCardExportJobResponseTypeDef",
    {
        "ModelCardExportJobName": str,
        "ModelCardExportJobArn": str,
        "Status": ModelCardExportJobStatusType,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "OutputConfig": "ModelCardExportOutputConfigTypeDef",
        "CreatedAt": datetime,
        "LastModifiedAt": datetime,
        "FailureReason": str,
        "ExportArtifacts": "ModelCardExportArtifactsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeModelCardRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalDescribeModelCardRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeModelCardRequestRequestTypeDef",
    {
        "ModelCardVersion": int,
    },
    total=False,
)

class DescribeModelCardRequestRequestTypeDef(
    _RequiredDescribeModelCardRequestRequestTypeDef, _OptionalDescribeModelCardRequestRequestTypeDef
):
    pass

DescribeModelCardResponseTypeDef = TypedDict(
    "DescribeModelCardResponseTypeDef",
    {
        "ModelCardArn": str,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
        "SecurityConfig": "ModelCardSecurityConfigTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ModelCardProcessingStatus": ModelCardProcessingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelExplainabilityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelExplainabilityBaselineConfig": "ModelExplainabilityBaselineConfigTypeDef",
        "ModelExplainabilityAppSpecification": "ModelExplainabilityAppSpecificationTypeDef",
        "ModelExplainabilityJobInput": "ModelExplainabilityJobInputTypeDef",
        "ModelExplainabilityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelInputRequestTypeDef = TypedDict(
    "DescribeModelInputRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeModelOutputTypeDef = TypedDict(
    "DescribeModelOutputTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "InferenceExecutionConfig": "InferenceExecutionConfigTypeDef",
        "ExecutionRoleArn": str,
        "VpcConfig": "VpcConfigTypeDef",
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
        "DeploymentRecommendation": "DeploymentRecommendationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackageGroupInputRequestTypeDef = TypedDict(
    "DescribeModelPackageGroupInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

DescribeModelPackageGroupOutputTypeDef = TypedDict(
    "DescribeModelPackageGroupOutputTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackageInputRequestTypeDef = TypedDict(
    "DescribeModelPackageInputRequestTypeDef",
    {
        "ModelPackageName": str,
    },
)

DescribeModelPackageOutputTypeDef = TypedDict(
    "DescribeModelPackageOutputTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": "ModelPackageStatusDetailsTypeDef",
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ApprovalDescription": str,
        "CustomerMetadataProperties": Dict[str, str],
        "DriftCheckBaselines": "DriftCheckBaselinesTypeDef",
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ],
        "SkipModelValidation": SkipModelValidationType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelQualityJobDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionRequestRequestTypeDef",
    {
        "JobDefinitionName": str,
    },
)

DescribeModelQualityJobDefinitionResponseTypeDef = TypedDict(
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    {
        "JobDefinitionArn": str,
        "JobDefinitionName": str,
        "CreationTime": datetime,
        "ModelQualityBaselineConfig": "ModelQualityBaselineConfigTypeDef",
        "ModelQualityAppSpecification": "ModelQualityAppSpecificationTypeDef",
        "ModelQualityJobInput": "ModelQualityJobInputTypeDef",
        "ModelQualityJobOutputConfig": "MonitoringOutputConfigTypeDef",
        "JobResources": "MonitoringResourcesTypeDef",
        "NetworkConfig": "MonitoringNetworkConfigTypeDef",
        "RoleArn": str,
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "DescribeMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

DescribeMonitoringScheduleResponseTypeDef = TypedDict(
    "DescribeMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "EndpointName": str,
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookInstanceInputRequestTypeDef = TypedDict(
    "DescribeNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)

DescribeNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookInstanceOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "FailureReason": str,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": DirectInternetAccessType,
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": RootAccessType,
        "PlatformIdentifier": str,
        "InstanceMetadataServiceConfiguration": "InstanceMetadataServiceConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineDefinitionForExecutionRequestRequestTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineDefinitionForExecutionResponseTypeDef = TypedDict(
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    {
        "PipelineDefinition": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineExecutionRequestRequestTypeDef = TypedDict(
    "DescribePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)

DescribePipelineExecutionResponseTypeDef = TypedDict(
    "DescribePipelineExecutionResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": "PipelineExperimentConfigTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "SelectiveExecutionConfig": "SelectiveExecutionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)

DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProcessingJobRequestRequestTypeDef = TypedDict(
    "DescribeProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

DescribeProcessingJobResponseTypeDef = TypedDict(
    "DescribeProcessingJobResponseTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "RoleArn": str,
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectInputRequestTypeDef = TypedDict(
    "DescribeProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DescribeProjectOutputTypeDef = TypedDict(
    "DescribeProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "ProjectId": str,
        "ProjectDescription": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
        "ServiceCatalogProvisionedProductDetails": "ServiceCatalogProvisionedProductDetailsTypeDef",
        "ProjectStatus": ProjectStatusType,
        "CreatedBy": "UserContextTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpaceRequestRequestTypeDef = TypedDict(
    "DescribeSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)

DescribeSpaceResponseTypeDef = TypedDict(
    "DescribeSpaceResponseTypeDef",
    {
        "DomainId": str,
        "SpaceArn": str,
        "SpaceName": str,
        "HomeEfsFileSystemUid": str,
        "Status": SpaceStatusType,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SpaceSettings": "SpaceSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStudioLifecycleConfigRequestRequestTypeDef = TypedDict(
    "DescribeStudioLifecycleConfigRequestRequestTypeDef",
    {
        "StudioLifecycleConfigName": str,
    },
)

DescribeStudioLifecycleConfigResponseTypeDef = TypedDict(
    "DescribeStudioLifecycleConfigResponseTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "StudioLifecycleConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "StudioLifecycleConfigContent": str,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscribedWorkteamRequestRequestTypeDef = TypedDict(
    "DescribeSubscribedWorkteamRequestRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)

DescribeSubscribedWorkteamResponseTypeDef = TypedDict(
    "DescribeSubscribedWorkteamResponseTypeDef",
    {
        "SubscribedWorkteam": "SubscribedWorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrainingJobRequestRequestTypeDef = TypedDict(
    "DescribeTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

DescribeTrainingJobResponseTypeDef = TypedDict(
    "DescribeTrainingJobResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List["SecondaryStatusTransitionTypeDef"],
        "FinalMetricDataList": List["MetricDataTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "DebugRuleEvaluationStatuses": List["DebugRuleEvaluationStatusTypeDef"],
        "ProfilerConfig": "ProfilerConfigTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
        "ProfilerRuleEvaluationStatuses": List["ProfilerRuleEvaluationStatusTypeDef"],
        "ProfilingStatus": ProfilingStatusType,
        "RetryStrategy": "RetryStrategyTypeDef",
        "Environment": Dict[str, str],
        "WarmPoolStatus": "WarmPoolStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransformJobRequestRequestTypeDef = TypedDict(
    "DescribeTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

DescribeTransformJobResponseTypeDef = TypedDict(
    "DescribeTransformJobResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "DataCaptureConfig": "BatchDataCaptureConfigTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": "DataProcessingTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrialComponentRequestRequestTypeDef = TypedDict(
    "DescribeTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)

DescribeTrialComponentResponseTypeDef = TypedDict(
    "DescribeTrialComponentResponseTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "Source": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Metrics": List["TrialComponentMetricSummaryTypeDef"],
        "LineageGroupArn": str,
        "Sources": List["TrialComponentSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrialRequestRequestTypeDef = TypedDict(
    "DescribeTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)

DescribeTrialResponseTypeDef = TypedDict(
    "DescribeTrialResponseTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfileRequestRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)

DescribeUserProfileResponseTypeDef = TypedDict(
    "DescribeUserProfileResponseTypeDef",
    {
        "DomainId": str,
        "UserProfileArn": str,
        "UserProfileName": str,
        "HomeEfsFileSystemUid": str,
        "Status": UserProfileStatusType,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "UserSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkforceRequestRequestTypeDef = TypedDict(
    "DescribeWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)

DescribeWorkforceResponseTypeDef = TypedDict(
    "DescribeWorkforceResponseTypeDef",
    {
        "Workforce": "WorkforceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkteamRequestRequestTypeDef = TypedDict(
    "DescribeWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)

DescribeWorkteamResponseTypeDef = TypedDict(
    "DescribeWorkteamResponseTypeDef",
    {
        "Workteam": "WorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDesiredWeightAndCapacityTypeDef = TypedDict(
    "_RequiredDesiredWeightAndCapacityTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalDesiredWeightAndCapacityTypeDef = TypedDict(
    "_OptionalDesiredWeightAndCapacityTypeDef",
    {
        "DesiredWeight": float,
        "DesiredInstanceCount": int,
        "ServerlessUpdateConfig": "ProductionVariantServerlessUpdateConfigTypeDef",
    },
    total=False,
)

class DesiredWeightAndCapacityTypeDef(
    _RequiredDesiredWeightAndCapacityTypeDef, _OptionalDesiredWeightAndCapacityTypeDef
):
    pass

_RequiredDeviceDeploymentSummaryTypeDef = TypedDict(
    "_RequiredDeviceDeploymentSummaryTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "EdgeDeploymentPlanName": str,
        "StageName": str,
        "DeviceName": str,
        "DeviceArn": str,
    },
)
_OptionalDeviceDeploymentSummaryTypeDef = TypedDict(
    "_OptionalDeviceDeploymentSummaryTypeDef",
    {
        "DeployedStageName": str,
        "DeviceFleetName": str,
        "DeviceDeploymentStatus": DeviceDeploymentStatusType,
        "DeviceDeploymentStatusMessage": str,
        "Description": str,
        "DeploymentStartTime": datetime,
    },
    total=False,
)

class DeviceDeploymentSummaryTypeDef(
    _RequiredDeviceDeploymentSummaryTypeDef, _OptionalDeviceDeploymentSummaryTypeDef
):
    pass

_RequiredDeviceFleetSummaryTypeDef = TypedDict(
    "_RequiredDeviceFleetSummaryTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
    },
)
_OptionalDeviceFleetSummaryTypeDef = TypedDict(
    "_OptionalDeviceFleetSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

class DeviceFleetSummaryTypeDef(
    _RequiredDeviceFleetSummaryTypeDef, _OptionalDeviceFleetSummaryTypeDef
):
    pass

_RequiredDeviceSelectionConfigTypeDef = TypedDict(
    "_RequiredDeviceSelectionConfigTypeDef",
    {
        "DeviceSubsetType": DeviceSubsetTypeType,
    },
)
_OptionalDeviceSelectionConfigTypeDef = TypedDict(
    "_OptionalDeviceSelectionConfigTypeDef",
    {
        "Percentage": int,
        "DeviceNames": List[str],
        "DeviceNameContains": str,
    },
    total=False,
)

class DeviceSelectionConfigTypeDef(
    _RequiredDeviceSelectionConfigTypeDef, _OptionalDeviceSelectionConfigTypeDef
):
    pass

DeviceStatsTypeDef = TypedDict(
    "DeviceStatsTypeDef",
    {
        "ConnectedDeviceCount": int,
        "RegisteredDeviceCount": int,
    },
)

_RequiredDeviceSummaryTypeDef = TypedDict(
    "_RequiredDeviceSummaryTypeDef",
    {
        "DeviceName": str,
        "DeviceArn": str,
    },
)
_OptionalDeviceSummaryTypeDef = TypedDict(
    "_OptionalDeviceSummaryTypeDef",
    {
        "Description": str,
        "DeviceFleetName": str,
        "IotThingName": str,
        "RegistrationTime": datetime,
        "LatestHeartbeat": datetime,
        "Models": List["EdgeModelSummaryTypeDef"],
        "AgentVersion": str,
    },
    total=False,
)

class DeviceSummaryTypeDef(_RequiredDeviceSummaryTypeDef, _OptionalDeviceSummaryTypeDef):
    pass

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "DeviceName": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "Description": str,
        "IotThingName": str,
    },
    total=False,
)

class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass

DirectDeploySettingsTypeDef = TypedDict(
    "DirectDeploySettingsTypeDef",
    {
        "Status": FeatureStatusType,
    },
    total=False,
)

DisassociateTrialComponentRequestRequestTypeDef = TypedDict(
    "DisassociateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "TrialName": str,
    },
)

DisassociateTrialComponentResponseTypeDef = TypedDict(
    "DisassociateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "Status": DomainStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Url": str,
    },
    total=False,
)

DomainSettingsForUpdateTypeDef = TypedDict(
    "DomainSettingsForUpdateTypeDef",
    {
        "RStudioServerProDomainSettingsForUpdate": "RStudioServerProDomainSettingsForUpdateTypeDef",
        "ExecutionRoleIdentityConfig": ExecutionRoleIdentityConfigType,
        "SecurityGroupIds": List[str],
    },
    total=False,
)

DomainSettingsTypeDef = TypedDict(
    "DomainSettingsTypeDef",
    {
        "SecurityGroupIds": List[str],
        "RStudioServerProDomainSettings": "RStudioServerProDomainSettingsTypeDef",
        "ExecutionRoleIdentityConfig": ExecutionRoleIdentityConfigType,
    },
    total=False,
)

DriftCheckBaselinesTypeDef = TypedDict(
    "DriftCheckBaselinesTypeDef",
    {
        "Bias": "DriftCheckBiasTypeDef",
        "Explainability": "DriftCheckExplainabilityTypeDef",
        "ModelQuality": "DriftCheckModelQualityTypeDef",
        "ModelDataQuality": "DriftCheckModelDataQualityTypeDef",
    },
    total=False,
)

DriftCheckBiasTypeDef = TypedDict(
    "DriftCheckBiasTypeDef",
    {
        "ConfigFile": "FileSourceTypeDef",
        "PreTrainingConstraints": "MetricsSourceTypeDef",
        "PostTrainingConstraints": "MetricsSourceTypeDef",
    },
    total=False,
)

DriftCheckExplainabilityTypeDef = TypedDict(
    "DriftCheckExplainabilityTypeDef",
    {
        "Constraints": "MetricsSourceTypeDef",
        "ConfigFile": "FileSourceTypeDef",
    },
    total=False,
)

DriftCheckModelDataQualityTypeDef = TypedDict(
    "DriftCheckModelDataQualityTypeDef",
    {
        "Statistics": "MetricsSourceTypeDef",
        "Constraints": "MetricsSourceTypeDef",
    },
    total=False,
)

DriftCheckModelQualityTypeDef = TypedDict(
    "DriftCheckModelQualityTypeDef",
    {
        "Statistics": "MetricsSourceTypeDef",
        "Constraints": "MetricsSourceTypeDef",
    },
    total=False,
)

DynamicScalingConfigurationTypeDef = TypedDict(
    "DynamicScalingConfigurationTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
        "ScaleInCooldown": int,
        "ScaleOutCooldown": int,
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
    },
    total=False,
)

EMRStepMetadataTypeDef = TypedDict(
    "EMRStepMetadataTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
        "StepName": str,
        "LogFilePath": str,
    },
    total=False,
)

EdgeDeploymentConfigTypeDef = TypedDict(
    "EdgeDeploymentConfigTypeDef",
    {
        "FailureHandlingPolicy": FailureHandlingPolicyType,
    },
)

EdgeDeploymentModelConfigTypeDef = TypedDict(
    "EdgeDeploymentModelConfigTypeDef",
    {
        "ModelHandle": str,
        "EdgePackagingJobName": str,
    },
)

_RequiredEdgeDeploymentPlanSummaryTypeDef = TypedDict(
    "_RequiredEdgeDeploymentPlanSummaryTypeDef",
    {
        "EdgeDeploymentPlanArn": str,
        "EdgeDeploymentPlanName": str,
        "DeviceFleetName": str,
        "EdgeDeploymentSuccess": int,
        "EdgeDeploymentPending": int,
        "EdgeDeploymentFailed": int,
    },
)
_OptionalEdgeDeploymentPlanSummaryTypeDef = TypedDict(
    "_OptionalEdgeDeploymentPlanSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

class EdgeDeploymentPlanSummaryTypeDef(
    _RequiredEdgeDeploymentPlanSummaryTypeDef, _OptionalEdgeDeploymentPlanSummaryTypeDef
):
    pass

_RequiredEdgeDeploymentStatusTypeDef = TypedDict(
    "_RequiredEdgeDeploymentStatusTypeDef",
    {
        "StageStatus": StageStatusType,
        "EdgeDeploymentSuccessInStage": int,
        "EdgeDeploymentPendingInStage": int,
        "EdgeDeploymentFailedInStage": int,
    },
)
_OptionalEdgeDeploymentStatusTypeDef = TypedDict(
    "_OptionalEdgeDeploymentStatusTypeDef",
    {
        "EdgeDeploymentStatusMessage": str,
        "EdgeDeploymentStageStartTime": datetime,
    },
    total=False,
)

class EdgeDeploymentStatusTypeDef(
    _RequiredEdgeDeploymentStatusTypeDef, _OptionalEdgeDeploymentStatusTypeDef
):
    pass

EdgeModelStatTypeDef = TypedDict(
    "EdgeModelStatTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
        "OfflineDeviceCount": int,
        "ConnectedDeviceCount": int,
        "ActiveDeviceCount": int,
        "SamplingDeviceCount": int,
    },
)

EdgeModelSummaryTypeDef = TypedDict(
    "EdgeModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)

_RequiredEdgeModelTypeDef = TypedDict(
    "_RequiredEdgeModelTypeDef",
    {
        "ModelName": str,
        "ModelVersion": str,
    },
)
_OptionalEdgeModelTypeDef = TypedDict(
    "_OptionalEdgeModelTypeDef",
    {
        "LatestSampleTime": datetime,
        "LatestInference": datetime,
    },
    total=False,
)

class EdgeModelTypeDef(_RequiredEdgeModelTypeDef, _OptionalEdgeModelTypeDef):
    pass

_RequiredEdgeOutputConfigTypeDef = TypedDict(
    "_RequiredEdgeOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalEdgeOutputConfigTypeDef = TypedDict(
    "_OptionalEdgeOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "PresetDeploymentType": Literal["GreengrassV2Component"],
        "PresetDeploymentConfig": str,
    },
    total=False,
)

class EdgeOutputConfigTypeDef(_RequiredEdgeOutputConfigTypeDef, _OptionalEdgeOutputConfigTypeDef):
    pass

_RequiredEdgePackagingJobSummaryTypeDef = TypedDict(
    "_RequiredEdgePackagingJobSummaryTypeDef",
    {
        "EdgePackagingJobArn": str,
        "EdgePackagingJobName": str,
        "EdgePackagingJobStatus": EdgePackagingJobStatusType,
    },
)
_OptionalEdgePackagingJobSummaryTypeDef = TypedDict(
    "_OptionalEdgePackagingJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "ModelName": str,
        "ModelVersion": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

class EdgePackagingJobSummaryTypeDef(
    _RequiredEdgePackagingJobSummaryTypeDef, _OptionalEdgePackagingJobSummaryTypeDef
):
    pass

_RequiredEdgePresetDeploymentOutputTypeDef = TypedDict(
    "_RequiredEdgePresetDeploymentOutputTypeDef",
    {
        "Type": Literal["GreengrassV2Component"],
    },
)
_OptionalEdgePresetDeploymentOutputTypeDef = TypedDict(
    "_OptionalEdgePresetDeploymentOutputTypeDef",
    {
        "Artifact": str,
        "Status": EdgePresetDeploymentStatusType,
        "StatusMessage": str,
    },
    total=False,
)

class EdgePresetDeploymentOutputTypeDef(
    _RequiredEdgePresetDeploymentOutputTypeDef, _OptionalEdgePresetDeploymentOutputTypeDef
):
    pass

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "AssociationType": AssociationEdgeTypeType,
    },
    total=False,
)

EndpointConfigSummaryTypeDef = TypedDict(
    "EndpointConfigSummaryTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "CreationTime": datetime,
    },
)

EndpointInfoTypeDef = TypedDict(
    "EndpointInfoTypeDef",
    {
        "EndpointName": str,
    },
)

EndpointInputConfigurationTypeDef = TypedDict(
    "EndpointInputConfigurationTypeDef",
    {
        "InstanceType": ProductionVariantInstanceTypeType,
        "InferenceSpecificationName": str,
        "EnvironmentParameterRanges": "EnvironmentParameterRangesTypeDef",
        "ServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
    },
    total=False,
)

_RequiredEndpointInputTypeDef = TypedDict(
    "_RequiredEndpointInputTypeDef",
    {
        "EndpointName": str,
        "LocalPath": str,
    },
)
_OptionalEndpointInputTypeDef = TypedDict(
    "_OptionalEndpointInputTypeDef",
    {
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "FeaturesAttribute": str,
        "InferenceAttribute": str,
        "ProbabilityAttribute": str,
        "ProbabilityThresholdAttribute": float,
        "StartTimeOffset": str,
        "EndTimeOffset": str,
        "ExcludeFeaturesAttribute": str,
    },
    total=False,
)

class EndpointInputTypeDef(_RequiredEndpointInputTypeDef, _OptionalEndpointInputTypeDef):
    pass

_RequiredEndpointMetadataTypeDef = TypedDict(
    "_RequiredEndpointMetadataTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalEndpointMetadataTypeDef = TypedDict(
    "_OptionalEndpointMetadataTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointStatus": EndpointStatusType,
        "FailureReason": str,
    },
    total=False,
)

class EndpointMetadataTypeDef(_RequiredEndpointMetadataTypeDef, _OptionalEndpointMetadataTypeDef):
    pass

_RequiredEndpointOutputConfigurationTypeDef = TypedDict(
    "_RequiredEndpointOutputConfigurationTypeDef",
    {
        "EndpointName": str,
        "VariantName": str,
    },
)
_OptionalEndpointOutputConfigurationTypeDef = TypedDict(
    "_OptionalEndpointOutputConfigurationTypeDef",
    {
        "InstanceType": ProductionVariantInstanceTypeType,
        "InitialInstanceCount": int,
        "ServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
    },
    total=False,
)

class EndpointOutputConfigurationTypeDef(
    _RequiredEndpointOutputConfigurationTypeDef, _OptionalEndpointOutputConfigurationTypeDef
):
    pass

EndpointPerformanceTypeDef = TypedDict(
    "EndpointPerformanceTypeDef",
    {
        "Metrics": "InferenceMetricsTypeDef",
        "EndpointInfo": "EndpointInfoTypeDef",
    },
)

EndpointSummaryTypeDef = TypedDict(
    "EndpointSummaryTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": EndpointStatusType,
    },
)

_RequiredEndpointTypeDef = TypedDict(
    "_RequiredEndpointTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "EndpointStatus": EndpointStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalEndpointTypeDef = TypedDict(
    "_OptionalEndpointTypeDef",
    {
        "ProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigSummaryTypeDef",
        "FailureReason": str,
        "MonitoringSchedules": List["MonitoringScheduleTypeDef"],
        "Tags": List["TagTypeDef"],
        "ShadowProductionVariants": List["ProductionVariantSummaryTypeDef"],
    },
    total=False,
)

class EndpointTypeDef(_RequiredEndpointTypeDef, _OptionalEndpointTypeDef):
    pass

EnvironmentParameterRangesTypeDef = TypedDict(
    "EnvironmentParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": List["CategoricalParameterTypeDef"],
    },
    total=False,
)

EnvironmentParameterTypeDef = TypedDict(
    "EnvironmentParameterTypeDef",
    {
        "Key": str,
        "ValueType": str,
        "Value": str,
    },
)

ExperimentConfigTypeDef = TypedDict(
    "ExperimentConfigTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "TrialComponentDisplayName": str,
        "RunName": str,
    },
    total=False,
)

_RequiredExperimentSourceTypeDef = TypedDict(
    "_RequiredExperimentSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalExperimentSourceTypeDef = TypedDict(
    "_OptionalExperimentSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)

class ExperimentSourceTypeDef(_RequiredExperimentSourceTypeDef, _OptionalExperimentSourceTypeDef):
    pass

ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "ExperimentArn": str,
        "ExperimentName": str,
        "DisplayName": str,
        "ExperimentSource": "ExperimentSourceTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "ExperimentName": str,
        "ExperimentArn": str,
        "DisplayName": str,
        "Source": "ExperimentSourceTypeDef",
        "Description": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ExplainabilityTypeDef = TypedDict(
    "ExplainabilityTypeDef",
    {
        "Report": "MetricsSourceTypeDef",
    },
    total=False,
)

ExplainerConfigTypeDef = TypedDict(
    "ExplainerConfigTypeDef",
    {
        "ClarifyExplainerConfig": "ClarifyExplainerConfigTypeDef",
    },
    total=False,
)

FailStepMetadataTypeDef = TypedDict(
    "FailStepMetadataTypeDef",
    {
        "ErrorMessage": str,
    },
    total=False,
)

FeatureDefinitionTypeDef = TypedDict(
    "FeatureDefinitionTypeDef",
    {
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
        "CollectionType": CollectionTypeType,
        "CollectionConfig": "CollectionConfigTypeDef",
    },
    total=False,
)

_RequiredFeatureGroupSummaryTypeDef = TypedDict(
    "_RequiredFeatureGroupSummaryTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureGroupArn": str,
        "CreationTime": datetime,
    },
)
_OptionalFeatureGroupSummaryTypeDef = TypedDict(
    "_OptionalFeatureGroupSummaryTypeDef",
    {
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
    },
    total=False,
)

class FeatureGroupSummaryTypeDef(
    _RequiredFeatureGroupSummaryTypeDef, _OptionalFeatureGroupSummaryTypeDef
):
    pass

FeatureGroupTypeDef = TypedDict(
    "FeatureGroupTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "RecordIdentifierFeatureName": str,
        "EventTimeFeatureName": str,
        "FeatureDefinitions": List["FeatureDefinitionTypeDef"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "OnlineStoreConfig": "OnlineStoreConfigTypeDef",
        "OfflineStoreConfig": "OfflineStoreConfigTypeDef",
        "RoleArn": str,
        "FeatureGroupStatus": FeatureGroupStatusType,
        "OfflineStoreStatus": "OfflineStoreStatusTypeDef",
        "LastUpdateStatus": "LastUpdateStatusTypeDef",
        "FailureReason": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

FeatureMetadataTypeDef = TypedDict(
    "FeatureMetadataTypeDef",
    {
        "FeatureGroupArn": str,
        "FeatureGroupName": str,
        "FeatureName": str,
        "FeatureType": FeatureTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Description": str,
        "Parameters": List["FeatureParameterTypeDef"],
    },
    total=False,
)

FeatureParameterTypeDef = TypedDict(
    "FeatureParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredFileSourceTypeDef = TypedDict(
    "_RequiredFileSourceTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalFileSourceTypeDef = TypedDict(
    "_OptionalFileSourceTypeDef",
    {
        "ContentType": str,
        "ContentDigest": str,
    },
    total=False,
)

class FileSourceTypeDef(_RequiredFileSourceTypeDef, _OptionalFileSourceTypeDef):
    pass

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "MountPath": str,
        "DefaultUid": int,
        "DefaultGid": int,
    },
    total=False,
)

FileSystemDataSourceTypeDef = TypedDict(
    "FileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": FileSystemAccessModeType,
        "FileSystemType": FileSystemTypeType,
        "DirectoryPath": str,
    },
)

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "Name": str,
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Operator": OperatorType,
        "Value": str,
    },
    total=False,
)

class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass

_RequiredFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
        "Value": float,
    },
)
_OptionalFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalAutoMLJobObjectiveMetricTypeDef",
    {
        "Type": AutoMLJobObjectiveTypeType,
        "StandardMetricName": AutoMLMetricEnumType,
    },
    total=False,
)

class FinalAutoMLJobObjectiveMetricTypeDef(
    _RequiredFinalAutoMLJobObjectiveMetricTypeDef, _OptionalFinalAutoMLJobObjectiveMetricTypeDef
):
    pass

_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "MetricName": str,
        "Value": float,
    },
)
_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
    },
    total=False,
)

class FinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef,
    _OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef,
):
    pass

_RequiredFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_RequiredFlowDefinitionOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_OptionalFlowDefinitionOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class FlowDefinitionOutputConfigTypeDef(
    _RequiredFlowDefinitionOutputConfigTypeDef, _OptionalFlowDefinitionOutputConfigTypeDef
):
    pass

_RequiredFlowDefinitionSummaryTypeDef = TypedDict(
    "_RequiredFlowDefinitionSummaryTypeDef",
    {
        "FlowDefinitionName": str,
        "FlowDefinitionArn": str,
        "FlowDefinitionStatus": FlowDefinitionStatusType,
        "CreationTime": datetime,
    },
)
_OptionalFlowDefinitionSummaryTypeDef = TypedDict(
    "_OptionalFlowDefinitionSummaryTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)

class FlowDefinitionSummaryTypeDef(
    _RequiredFlowDefinitionSummaryTypeDef, _OptionalFlowDefinitionSummaryTypeDef
):
    pass

GetDeviceFleetReportRequestRequestTypeDef = TypedDict(
    "GetDeviceFleetReportRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
    },
)

GetDeviceFleetReportResponseTypeDef = TypedDict(
    "GetDeviceFleetReportResponseTypeDef",
    {
        "DeviceFleetArn": str,
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
        "Description": str,
        "ReportGenerated": datetime,
        "DeviceStats": "DeviceStatsTypeDef",
        "AgentVersions": List["AgentVersionTypeDef"],
        "ModelStats": List["EdgeModelStatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLineageGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetLineageGroupPolicyRequestRequestTypeDef",
    {
        "LineageGroupName": str,
    },
)

GetLineageGroupPolicyResponseTypeDef = TypedDict(
    "GetLineageGroupPolicyResponseTypeDef",
    {
        "LineageGroupArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "GetModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
    },
)

GetModelPackageGroupPolicyOutputTypeDef = TypedDict(
    "GetModelPackageGroupPolicyOutputTypeDef",
    {
        "ResourcePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSagemakerServicecatalogPortfolioStatusOutputTypeDef = TypedDict(
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    {
        "Status": SagemakerServicecatalogStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetScalingConfigurationRecommendationRequestRequestTypeDef = TypedDict(
    "_RequiredGetScalingConfigurationRecommendationRequestRequestTypeDef",
    {
        "InferenceRecommendationsJobName": str,
    },
)
_OptionalGetScalingConfigurationRecommendationRequestRequestTypeDef = TypedDict(
    "_OptionalGetScalingConfigurationRecommendationRequestRequestTypeDef",
    {
        "RecommendationId": str,
        "EndpointName": str,
        "TargetCpuUtilizationPerCore": int,
        "ScalingPolicyObjective": "ScalingPolicyObjectiveTypeDef",
    },
    total=False,
)

class GetScalingConfigurationRecommendationRequestRequestTypeDef(
    _RequiredGetScalingConfigurationRecommendationRequestRequestTypeDef,
    _OptionalGetScalingConfigurationRecommendationRequestRequestTypeDef,
):
    pass

GetScalingConfigurationRecommendationResponseTypeDef = TypedDict(
    "GetScalingConfigurationRecommendationResponseTypeDef",
    {
        "InferenceRecommendationsJobName": str,
        "RecommendationId": str,
        "EndpointName": str,
        "TargetCpuUtilizationPerCore": int,
        "ScalingPolicyObjective": "ScalingPolicyObjectiveTypeDef",
        "Metric": "ScalingPolicyMetricTypeDef",
        "DynamicScalingConfiguration": "DynamicScalingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSearchSuggestionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSearchSuggestionsRequestRequestTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalGetSearchSuggestionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSearchSuggestionsRequestRequestTypeDef",
    {
        "SuggestionQuery": "SuggestionQueryTypeDef",
    },
    total=False,
)

class GetSearchSuggestionsRequestRequestTypeDef(
    _RequiredGetSearchSuggestionsRequestRequestTypeDef,
    _OptionalGetSearchSuggestionsRequestRequestTypeDef,
):
    pass

GetSearchSuggestionsResponseTypeDef = TypedDict(
    "GetSearchSuggestionsResponseTypeDef",
    {
        "PropertyNameSuggestions": List["PropertyNameSuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GitConfigForUpdateTypeDef = TypedDict(
    "GitConfigForUpdateTypeDef",
    {
        "SecretArn": str,
    },
    total=False,
)

_RequiredGitConfigTypeDef = TypedDict(
    "_RequiredGitConfigTypeDef",
    {
        "RepositoryUrl": str,
    },
)
_OptionalGitConfigTypeDef = TypedDict(
    "_OptionalGitConfigTypeDef",
    {
        "Branch": str,
        "SecretArn": str,
    },
    total=False,
)

class GitConfigTypeDef(_RequiredGitConfigTypeDef, _OptionalGitConfigTypeDef):
    pass

HolidayConfigAttributesTypeDef = TypedDict(
    "HolidayConfigAttributesTypeDef",
    {
        "CountryCode": str,
    },
    total=False,
)

HubContentDependencyTypeDef = TypedDict(
    "HubContentDependencyTypeDef",
    {
        "DependencyOriginPath": str,
        "DependencyCopyPath": str,
    },
    total=False,
)

_RequiredHubContentInfoTypeDef = TypedDict(
    "_RequiredHubContentInfoTypeDef",
    {
        "HubContentName": str,
        "HubContentArn": str,
        "HubContentVersion": str,
        "HubContentType": HubContentTypeType,
        "DocumentSchemaVersion": str,
        "HubContentStatus": HubContentStatusType,
        "CreationTime": datetime,
    },
)
_OptionalHubContentInfoTypeDef = TypedDict(
    "_OptionalHubContentInfoTypeDef",
    {
        "HubContentDisplayName": str,
        "HubContentDescription": str,
        "HubContentSearchKeywords": List[str],
    },
    total=False,
)

class HubContentInfoTypeDef(_RequiredHubContentInfoTypeDef, _OptionalHubContentInfoTypeDef):
    pass

_RequiredHubInfoTypeDef = TypedDict(
    "_RequiredHubInfoTypeDef",
    {
        "HubName": str,
        "HubArn": str,
        "HubStatus": HubStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalHubInfoTypeDef = TypedDict(
    "_OptionalHubInfoTypeDef",
    {
        "HubDisplayName": str,
        "HubDescription": str,
        "HubSearchKeywords": List[str],
    },
    total=False,
)

class HubInfoTypeDef(_RequiredHubInfoTypeDef, _OptionalHubInfoTypeDef):
    pass

HubS3StorageConfigTypeDef = TypedDict(
    "HubS3StorageConfigTypeDef",
    {
        "S3OutputPath": str,
    },
    total=False,
)

HumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "HumanLoopActivationConditionsConfigTypeDef",
    {
        "HumanLoopActivationConditions": str,
    },
)

HumanLoopActivationConfigTypeDef = TypedDict(
    "HumanLoopActivationConfigTypeDef",
    {
        "HumanLoopActivationConditionsConfig": "HumanLoopActivationConditionsConfigTypeDef",
    },
)

_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef",
    {
        "WorkteamArn": str,
        "HumanTaskUiArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "TaskCount": int,
    },
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {
        "TaskAvailabilityLifetimeInSeconds": int,
        "TaskTimeLimitInSeconds": int,
        "TaskKeywords": List[str],
        "PublicWorkforceTaskPrice": "PublicWorkforceTaskPriceTypeDef",
    },
    total=False,
)

class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass

HumanLoopRequestSourceTypeDef = TypedDict(
    "HumanLoopRequestSourceTypeDef",
    {
        "AwsManagedHumanLoopRequestSource": AwsManagedHumanLoopRequestSourceType,
    },
)

_RequiredHumanTaskConfigTypeDef = TypedDict(
    "_RequiredHumanTaskConfigTypeDef",
    {
        "WorkteamArn": str,
        "UiConfig": "UiConfigTypeDef",
        "PreHumanTaskLambdaArn": str,
        "TaskTitle": str,
        "TaskDescription": str,
        "NumberOfHumanWorkersPerDataObject": int,
        "TaskTimeLimitInSeconds": int,
        "AnnotationConsolidationConfig": "AnnotationConsolidationConfigTypeDef",
    },
)
_OptionalHumanTaskConfigTypeDef = TypedDict(
    "_OptionalHumanTaskConfigTypeDef",
    {
        "TaskKeywords": List[str],
        "TaskAvailabilityLifetimeInSeconds": int,
        "MaxConcurrentTaskCount": int,
        "PublicWorkforceTaskPrice": "PublicWorkforceTaskPriceTypeDef",
    },
    total=False,
)

class HumanTaskConfigTypeDef(_RequiredHumanTaskConfigTypeDef, _OptionalHumanTaskConfigTypeDef):
    pass

HumanTaskUiSummaryTypeDef = TypedDict(
    "HumanTaskUiSummaryTypeDef",
    {
        "HumanTaskUiName": str,
        "HumanTaskUiArn": str,
        "CreationTime": datetime,
    },
)

_RequiredHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
    },
)
_OptionalHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
    },
    total=False,
)

class HyperParameterAlgorithmSpecificationTypeDef(
    _RequiredHyperParameterAlgorithmSpecificationTypeDef,
    _OptionalHyperParameterAlgorithmSpecificationTypeDef,
):
    pass

_RequiredHyperParameterSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterSpecificationTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
    },
)
_OptionalHyperParameterSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterSpecificationTypeDef",
    {
        "Description": str,
        "Range": "ParameterRangeTypeDef",
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)

class HyperParameterSpecificationTypeDef(
    _RequiredHyperParameterSpecificationTypeDef, _OptionalHyperParameterSpecificationTypeDef
):
    pass

_RequiredHyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobDefinitionTypeDef",
    {
        "AlgorithmSpecification": "HyperParameterAlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalHyperParameterTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobDefinitionTypeDef",
    {
        "DefinitionName": str,
        "TuningObjective": "HyperParameterTuningJobObjectiveTypeDef",
        "HyperParameterRanges": "ParameterRangesTypeDef",
        "StaticHyperParameters": Dict[str, str],
        "InputDataConfig": List["ChannelTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "RetryStrategy": "RetryStrategyTypeDef",
        "HyperParameterTuningResourceConfig": "HyperParameterTuningResourceConfigTypeDef",
        "Environment": Dict[str, str],
    },
    total=False,
)

class HyperParameterTrainingJobDefinitionTypeDef(
    _RequiredHyperParameterTrainingJobDefinitionTypeDef,
    _OptionalHyperParameterTrainingJobDefinitionTypeDef,
):
    pass

_RequiredHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
        "TunedHyperParameters": Dict[str, str],
    },
)
_OptionalHyperParameterTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTrainingJobSummaryTypeDef",
    {
        "TrainingJobDefinitionName": str,
        "TuningJobName": str,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "FailureReason": str,
        "FinalHyperParameterTuningJobObjectiveMetric": "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
        "ObjectiveStatus": ObjectiveStatusType,
    },
    total=False,
)

class HyperParameterTrainingJobSummaryTypeDef(
    _RequiredHyperParameterTrainingJobSummaryTypeDef,
    _OptionalHyperParameterTrainingJobSummaryTypeDef,
):
    pass

HyperParameterTuningInstanceConfigTypeDef = TypedDict(
    "HyperParameterTuningInstanceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
    },
)

HyperParameterTuningJobCompletionDetailsTypeDef = TypedDict(
    "HyperParameterTuningJobCompletionDetailsTypeDef",
    {
        "NumberOfTrainingJobsObjectiveNotImproving": int,
        "ConvergenceDetectedTime": datetime,
    },
    total=False,
)

_RequiredHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobConfigTypeDef",
    {
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "ResourceLimits": "ResourceLimitsTypeDef",
    },
)
_OptionalHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobConfigTypeDef",
    {
        "StrategyConfig": "HyperParameterTuningJobStrategyConfigTypeDef",
        "HyperParameterTuningJobObjective": "HyperParameterTuningJobObjectiveTypeDef",
        "ParameterRanges": "ParameterRangesTypeDef",
        "TrainingJobEarlyStoppingType": TrainingJobEarlyStoppingTypeType,
        "TuningJobCompletionCriteria": "TuningJobCompletionCriteriaTypeDef",
        "RandomSeed": int,
    },
    total=False,
)

class HyperParameterTuningJobConfigTypeDef(
    _RequiredHyperParameterTuningJobConfigTypeDef, _OptionalHyperParameterTuningJobConfigTypeDef
):
    pass

HyperParameterTuningJobConsumedResourcesTypeDef = TypedDict(
    "HyperParameterTuningJobConsumedResourcesTypeDef",
    {
        "RuntimeInSeconds": int,
    },
    total=False,
)

HyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveTypeDef",
    {
        "Type": HyperParameterTuningJobObjectiveTypeType,
        "MetricName": str,
    },
)

HyperParameterTuningJobSearchEntityTypeDef = TypedDict(
    "HyperParameterTuningJobSearchEntityTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "CreationTime": datetime,
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
        "BestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "OverallBestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "FailureReason": str,
        "Tags": List["TagTypeDef"],
        "TuningJobCompletionDetails": "HyperParameterTuningJobCompletionDetailsTypeDef",
        "ConsumedResources": "HyperParameterTuningJobConsumedResourcesTypeDef",
    },
    total=False,
)

HyperParameterTuningJobStrategyConfigTypeDef = TypedDict(
    "HyperParameterTuningJobStrategyConfigTypeDef",
    {
        "HyperbandStrategyConfig": "HyperbandStrategyConfigTypeDef",
    },
    total=False,
)

_RequiredHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": HyperParameterTuningJobStatusType,
        "Strategy": HyperParameterTuningJobStrategyTypeType,
        "CreationTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
    },
)
_OptionalHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "ResourceLimits": "ResourceLimitsTypeDef",
    },
    total=False,
)

class HyperParameterTuningJobSummaryTypeDef(
    _RequiredHyperParameterTuningJobSummaryTypeDef, _OptionalHyperParameterTuningJobSummaryTypeDef
):
    pass

HyperParameterTuningJobWarmStartConfigTypeDef = TypedDict(
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    {
        "ParentHyperParameterTuningJobs": List["ParentHyperParameterTuningJobTypeDef"],
        "WarmStartType": HyperParameterTuningJobWarmStartTypeType,
    },
)

HyperParameterTuningResourceConfigTypeDef = TypedDict(
    "HyperParameterTuningResourceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeSizeInGB": int,
        "VolumeKmsKeyId": str,
        "AllocationStrategy": Literal["Prioritized"],
        "InstanceConfigs": List["HyperParameterTuningInstanceConfigTypeDef"],
    },
    total=False,
)

HyperbandStrategyConfigTypeDef = TypedDict(
    "HyperbandStrategyConfigTypeDef",
    {
        "MinResource": int,
        "MaxResource": int,
    },
    total=False,
)

IamIdentityTypeDef = TypedDict(
    "IamIdentityTypeDef",
    {
        "Arn": str,
        "PrincipalId": str,
        "SourceIdentity": str,
    },
    total=False,
)

IdentityProviderOAuthSettingTypeDef = TypedDict(
    "IdentityProviderOAuthSettingTypeDef",
    {
        "DataSourceName": DataSourceNameType,
        "Status": FeatureStatusType,
        "SecretArn": str,
    },
    total=False,
)

ImageClassificationJobConfigTypeDef = TypedDict(
    "ImageClassificationJobConfigTypeDef",
    {
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
    },
    total=False,
)

_RequiredImageConfigTypeDef = TypedDict(
    "_RequiredImageConfigTypeDef",
    {
        "RepositoryAccessMode": RepositoryAccessModeType,
    },
)
_OptionalImageConfigTypeDef = TypedDict(
    "_OptionalImageConfigTypeDef",
    {
        "RepositoryAuthConfig": "RepositoryAuthConfigTypeDef",
    },
    total=False,
)

class ImageConfigTypeDef(_RequiredImageConfigTypeDef, _OptionalImageConfigTypeDef):
    pass

_RequiredImageTypeDef = TypedDict(
    "_RequiredImageTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": ImageStatusType,
        "LastModifiedTime": datetime,
    },
)
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
    },
    total=False,
)

class ImageTypeDef(_RequiredImageTypeDef, _OptionalImageTypeDef):
    pass

_RequiredImageVersionTypeDef = TypedDict(
    "_RequiredImageVersionTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": ImageVersionStatusType,
        "LastModifiedTime": datetime,
        "Version": int,
    },
)
_OptionalImageVersionTypeDef = TypedDict(
    "_OptionalImageVersionTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)

class ImageVersionTypeDef(_RequiredImageVersionTypeDef, _OptionalImageVersionTypeDef):
    pass

_RequiredImportHubContentRequestRequestTypeDef = TypedDict(
    "_RequiredImportHubContentRequestRequestTypeDef",
    {
        "HubContentName": str,
        "HubContentType": HubContentTypeType,
        "DocumentSchemaVersion": str,
        "HubName": str,
        "HubContentDocument": str,
    },
)
_OptionalImportHubContentRequestRequestTypeDef = TypedDict(
    "_OptionalImportHubContentRequestRequestTypeDef",
    {
        "HubContentVersion": str,
        "HubContentDisplayName": str,
        "HubContentDescription": str,
        "HubContentMarkdown": str,
        "HubContentSearchKeywords": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportHubContentRequestRequestTypeDef(
    _RequiredImportHubContentRequestRequestTypeDef, _OptionalImportHubContentRequestRequestTypeDef
):
    pass

ImportHubContentResponseTypeDef = TypedDict(
    "ImportHubContentResponseTypeDef",
    {
        "HubArn": str,
        "HubContentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InferenceExecutionConfigTypeDef = TypedDict(
    "InferenceExecutionConfigTypeDef",
    {
        "Mode": InferenceExecutionModeType,
    },
)

_RequiredInferenceExperimentDataStorageConfigTypeDef = TypedDict(
    "_RequiredInferenceExperimentDataStorageConfigTypeDef",
    {
        "Destination": str,
    },
)
_OptionalInferenceExperimentDataStorageConfigTypeDef = TypedDict(
    "_OptionalInferenceExperimentDataStorageConfigTypeDef",
    {
        "KmsKey": str,
        "ContentType": "CaptureContentTypeHeaderTypeDef",
    },
    total=False,
)

class InferenceExperimentDataStorageConfigTypeDef(
    _RequiredInferenceExperimentDataStorageConfigTypeDef,
    _OptionalInferenceExperimentDataStorageConfigTypeDef,
):
    pass

InferenceExperimentScheduleTypeDef = TypedDict(
    "InferenceExperimentScheduleTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

_RequiredInferenceExperimentSummaryTypeDef = TypedDict(
    "_RequiredInferenceExperimentSummaryTypeDef",
    {
        "Name": str,
        "Type": Literal["ShadowMode"],
        "Status": InferenceExperimentStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalInferenceExperimentSummaryTypeDef = TypedDict(
    "_OptionalInferenceExperimentSummaryTypeDef",
    {
        "Schedule": "InferenceExperimentScheduleTypeDef",
        "StatusReason": str,
        "Description": str,
        "CompletionTime": datetime,
        "RoleArn": str,
    },
    total=False,
)

class InferenceExperimentSummaryTypeDef(
    _RequiredInferenceExperimentSummaryTypeDef, _OptionalInferenceExperimentSummaryTypeDef
):
    pass

InferenceMetricsTypeDef = TypedDict(
    "InferenceMetricsTypeDef",
    {
        "MaxInvocations": int,
        "ModelLatency": int,
    },
)

_RequiredInferenceRecommendationTypeDef = TypedDict(
    "_RequiredInferenceRecommendationTypeDef",
    {
        "Metrics": "RecommendationMetricsTypeDef",
        "EndpointConfiguration": "EndpointOutputConfigurationTypeDef",
        "ModelConfiguration": "ModelConfigurationTypeDef",
    },
)
_OptionalInferenceRecommendationTypeDef = TypedDict(
    "_OptionalInferenceRecommendationTypeDef",
    {
        "RecommendationId": str,
        "InvocationEndTime": datetime,
        "InvocationStartTime": datetime,
    },
    total=False,
)

class InferenceRecommendationTypeDef(
    _RequiredInferenceRecommendationTypeDef, _OptionalInferenceRecommendationTypeDef
):
    pass

_RequiredInferenceRecommendationsJobStepTypeDef = TypedDict(
    "_RequiredInferenceRecommendationsJobStepTypeDef",
    {
        "StepType": Literal["BENCHMARK"],
        "JobName": str,
        "Status": RecommendationJobStatusType,
    },
)
_OptionalInferenceRecommendationsJobStepTypeDef = TypedDict(
    "_OptionalInferenceRecommendationsJobStepTypeDef",
    {
        "InferenceBenchmark": "RecommendationJobInferenceBenchmarkTypeDef",
    },
    total=False,
)

class InferenceRecommendationsJobStepTypeDef(
    _RequiredInferenceRecommendationsJobStepTypeDef, _OptionalInferenceRecommendationsJobStepTypeDef
):
    pass

_RequiredInferenceRecommendationsJobTypeDef = TypedDict(
    "_RequiredInferenceRecommendationsJobTypeDef",
    {
        "JobName": str,
        "JobDescription": str,
        "JobType": RecommendationJobTypeType,
        "JobArn": str,
        "Status": RecommendationJobStatusType,
        "CreationTime": datetime,
        "RoleArn": str,
        "LastModifiedTime": datetime,
    },
)
_OptionalInferenceRecommendationsJobTypeDef = TypedDict(
    "_OptionalInferenceRecommendationsJobTypeDef",
    {
        "CompletionTime": datetime,
        "FailureReason": str,
        "ModelName": str,
        "SamplePayloadUrl": str,
        "ModelPackageVersionArn": str,
    },
    total=False,
)

class InferenceRecommendationsJobTypeDef(
    _RequiredInferenceRecommendationsJobTypeDef, _OptionalInferenceRecommendationsJobTypeDef
):
    pass

_RequiredInferenceSpecificationTypeDef = TypedDict(
    "_RequiredInferenceSpecificationTypeDef",
    {
        "Containers": List["ModelPackageContainerDefinitionTypeDef"],
    },
)
_OptionalInferenceSpecificationTypeDef = TypedDict(
    "_OptionalInferenceSpecificationTypeDef",
    {
        "SupportedTransformInstanceTypes": List[TransformInstanceTypeType],
        "SupportedRealtimeInferenceInstanceTypes": List[ProductionVariantInstanceTypeType],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)

class InferenceSpecificationTypeDef(
    _RequiredInferenceSpecificationTypeDef, _OptionalInferenceSpecificationTypeDef
):
    pass

_RequiredInputConfigTypeDef = TypedDict(
    "_RequiredInputConfigTypeDef",
    {
        "S3Uri": str,
        "Framework": FrameworkType,
    },
)
_OptionalInputConfigTypeDef = TypedDict(
    "_OptionalInputConfigTypeDef",
    {
        "DataInputConfig": str,
        "FrameworkVersion": str,
    },
    total=False,
)

class InputConfigTypeDef(_RequiredInputConfigTypeDef, _OptionalInputConfigTypeDef):
    pass

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "InstanceGroupName": str,
    },
)

InstanceMetadataServiceConfigurationTypeDef = TypedDict(
    "InstanceMetadataServiceConfigurationTypeDef",
    {
        "MinimumInstanceMetadataServiceVersion": str,
    },
)

IntegerParameterRangeSpecificationTypeDef = TypedDict(
    "IntegerParameterRangeSpecificationTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
    },
)

_RequiredIntegerParameterRangeTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MinValue": str,
        "MaxValue": str,
    },
)
_OptionalIntegerParameterRangeTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeTypeDef",
    {
        "ScalingType": HyperParameterScalingTypeType,
    },
    total=False,
)

class IntegerParameterRangeTypeDef(
    _RequiredIntegerParameterRangeTypeDef, _OptionalIntegerParameterRangeTypeDef
):
    pass

JupyterServerAppSettingsTypeDef = TypedDict(
    "JupyterServerAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
        "LifecycleConfigArns": List[str],
        "CodeRepositories": List["CodeRepositoryTypeDef"],
    },
    total=False,
)

KendraSettingsTypeDef = TypedDict(
    "KendraSettingsTypeDef",
    {
        "Status": FeatureStatusType,
    },
    total=False,
)

KernelGatewayAppSettingsTypeDef = TypedDict(
    "KernelGatewayAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
        "CustomImages": List["CustomImageTypeDef"],
        "LifecycleConfigArns": List[str],
    },
    total=False,
)

_RequiredKernelGatewayImageConfigTypeDef = TypedDict(
    "_RequiredKernelGatewayImageConfigTypeDef",
    {
        "KernelSpecs": List["KernelSpecTypeDef"],
    },
)
_OptionalKernelGatewayImageConfigTypeDef = TypedDict(
    "_OptionalKernelGatewayImageConfigTypeDef",
    {
        "FileSystemConfig": "FileSystemConfigTypeDef",
    },
    total=False,
)

class KernelGatewayImageConfigTypeDef(
    _RequiredKernelGatewayImageConfigTypeDef, _OptionalKernelGatewayImageConfigTypeDef
):
    pass

_RequiredKernelSpecTypeDef = TypedDict(
    "_RequiredKernelSpecTypeDef",
    {
        "Name": str,
    },
)
_OptionalKernelSpecTypeDef = TypedDict(
    "_OptionalKernelSpecTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class KernelSpecTypeDef(_RequiredKernelSpecTypeDef, _OptionalKernelSpecTypeDef):
    pass

LabelCountersForWorkteamTypeDef = TypedDict(
    "LabelCountersForWorkteamTypeDef",
    {
        "HumanLabeled": int,
        "PendingHuman": int,
        "Total": int,
    },
    total=False,
)

LabelCountersTypeDef = TypedDict(
    "LabelCountersTypeDef",
    {
        "TotalLabeled": int,
        "HumanLabeled": int,
        "MachineLabeled": int,
        "FailedNonRetryableError": int,
        "Unlabeled": int,
    },
    total=False,
)

_RequiredLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_RequiredLabelingJobAlgorithmsConfigTypeDef",
    {
        "LabelingJobAlgorithmSpecificationArn": str,
    },
)
_OptionalLabelingJobAlgorithmsConfigTypeDef = TypedDict(
    "_OptionalLabelingJobAlgorithmsConfigTypeDef",
    {
        "InitialActiveLearningModelArn": str,
        "LabelingJobResourceConfig": "LabelingJobResourceConfigTypeDef",
    },
    total=False,
)

class LabelingJobAlgorithmsConfigTypeDef(
    _RequiredLabelingJobAlgorithmsConfigTypeDef, _OptionalLabelingJobAlgorithmsConfigTypeDef
):
    pass

LabelingJobDataAttributesTypeDef = TypedDict(
    "LabelingJobDataAttributesTypeDef",
    {
        "ContentClassifiers": List[ContentClassifierType],
    },
    total=False,
)

LabelingJobDataSourceTypeDef = TypedDict(
    "LabelingJobDataSourceTypeDef",
    {
        "S3DataSource": "LabelingJobS3DataSourceTypeDef",
        "SnsDataSource": "LabelingJobSnsDataSourceTypeDef",
    },
    total=False,
)

_RequiredLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobForWorkteamSummaryTypeDef",
    {
        "JobReferenceCode": str,
        "WorkRequesterAccountId": str,
        "CreationTime": datetime,
    },
)
_OptionalLabelingJobForWorkteamSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobForWorkteamSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelCounters": "LabelCountersForWorkteamTypeDef",
        "NumberOfHumanWorkersPerDataObject": int,
    },
    total=False,
)

class LabelingJobForWorkteamSummaryTypeDef(
    _RequiredLabelingJobForWorkteamSummaryTypeDef, _OptionalLabelingJobForWorkteamSummaryTypeDef
):
    pass

_RequiredLabelingJobInputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobInputConfigTypeDef",
    {
        "DataSource": "LabelingJobDataSourceTypeDef",
    },
)
_OptionalLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobInputConfigTypeDef",
    {
        "DataAttributes": "LabelingJobDataAttributesTypeDef",
    },
    total=False,
)

class LabelingJobInputConfigTypeDef(
    _RequiredLabelingJobInputConfigTypeDef, _OptionalLabelingJobInputConfigTypeDef
):
    pass

_RequiredLabelingJobOutputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalLabelingJobOutputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "SnsTopicArn": str,
    },
    total=False,
)

class LabelingJobOutputConfigTypeDef(
    _RequiredLabelingJobOutputConfigTypeDef, _OptionalLabelingJobOutputConfigTypeDef
):
    pass

_RequiredLabelingJobOutputTypeDef = TypedDict(
    "_RequiredLabelingJobOutputTypeDef",
    {
        "OutputDatasetS3Uri": str,
    },
)
_OptionalLabelingJobOutputTypeDef = TypedDict(
    "_OptionalLabelingJobOutputTypeDef",
    {
        "FinalActiveLearningModelArn": str,
    },
    total=False,
)

class LabelingJobOutputTypeDef(
    _RequiredLabelingJobOutputTypeDef, _OptionalLabelingJobOutputTypeDef
):
    pass

LabelingJobResourceConfigTypeDef = TypedDict(
    "LabelingJobResourceConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

LabelingJobS3DataSourceTypeDef = TypedDict(
    "LabelingJobS3DataSourceTypeDef",
    {
        "ManifestS3Uri": str,
    },
)

LabelingJobSnsDataSourceTypeDef = TypedDict(
    "LabelingJobSnsDataSourceTypeDef",
    {
        "SnsTopicArn": str,
    },
)

LabelingJobStoppingConditionsTypeDef = TypedDict(
    "LabelingJobStoppingConditionsTypeDef",
    {
        "MaxHumanLabeledObjectCount": int,
        "MaxPercentageOfInputDatasetLabeled": int,
    },
    total=False,
)

_RequiredLabelingJobSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": LabelingJobStatusType,
        "LabelCounters": "LabelCountersTypeDef",
        "WorkteamArn": str,
        "PreHumanTaskLambdaArn": str,
    },
)
_OptionalLabelingJobSummaryTypeDef = TypedDict(
    "_OptionalLabelingJobSummaryTypeDef",
    {
        "AnnotationConsolidationLambdaArn": str,
        "FailureReason": str,
        "LabelingJobOutput": "LabelingJobOutputTypeDef",
        "InputConfig": "LabelingJobInputConfigTypeDef",
    },
    total=False,
)

class LabelingJobSummaryTypeDef(
    _RequiredLabelingJobSummaryTypeDef, _OptionalLabelingJobSummaryTypeDef
):
    pass

LambdaStepMetadataTypeDef = TypedDict(
    "LambdaStepMetadataTypeDef",
    {
        "Arn": str,
        "OutputParameters": List["OutputParameterTypeDef"],
    },
    total=False,
)

_RequiredLastUpdateStatusTypeDef = TypedDict(
    "_RequiredLastUpdateStatusTypeDef",
    {
        "Status": LastUpdateStatusValueType,
    },
)
_OptionalLastUpdateStatusTypeDef = TypedDict(
    "_OptionalLastUpdateStatusTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)

class LastUpdateStatusTypeDef(_RequiredLastUpdateStatusTypeDef, _OptionalLastUpdateStatusTypeDef):
    pass

LineageGroupSummaryTypeDef = TypedDict(
    "LineageGroupSummaryTypeDef",
    {
        "LineageGroupArn": str,
        "LineageGroupName": str,
        "DisplayName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "SourceUri": str,
        "ActionType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortActionsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "ActionSummaries": List["ActionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAlgorithmsInputRequestTypeDef = TypedDict(
    "ListAlgorithmsInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": AlgorithmSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListAlgorithmsOutputTypeDef = TypedDict(
    "ListAlgorithmsOutputTypeDef",
    {
        "AlgorithmSummaryList": List["AlgorithmSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListAliasesRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListAliasesRequestRequestTypeDef",
    {
        "Alias": str,
        "Version": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAliasesRequestRequestTypeDef(
    _RequiredListAliasesRequestRequestTypeDef, _OptionalListAliasesRequestRequestTypeDef
):
    pass

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "SageMakerImageVersionAliases": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppImageConfigsRequestRequestTypeDef = TypedDict(
    "ListAppImageConfigsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": AppImageConfigSortKeyType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListAppImageConfigsResponseTypeDef = TypedDict(
    "ListAppImageConfigsResponseTypeDef",
    {
        "NextToken": str,
        "AppImageConfigs": List["AppImageConfigDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": Literal["CreationTime"],
        "DomainIdEquals": str,
        "UserProfileNameEquals": str,
        "SpaceNameEquals": str,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "Apps": List["AppDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "SourceUri": str,
        "ArtifactType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListArtifactsResponseTypeDef = TypedDict(
    "ListArtifactsResponseTypeDef",
    {
        "ArtifactSummaries": List["ArtifactSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssociationsRequestRequestTypeDef",
    {
        "SourceArn": str,
        "DestinationArn": str,
        "SourceType": str,
        "DestinationType": str,
        "AssociationType": AssociationEdgeTypeType,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortAssociationsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAssociationsResponseTypeDef = TypedDict(
    "ListAssociationsResponseTypeDef",
    {
        "AssociationSummaries": List["AssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutoMLJobsRequestRequestTypeDef = TypedDict(
    "ListAutoMLJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": AutoMLJobStatusType,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": AutoMLSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAutoMLJobsResponseTypeDef = TypedDict(
    "ListAutoMLJobsResponseTypeDef",
    {
        "AutoMLJobSummaries": List["AutoMLJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCandidatesForAutoMLJobRequestRequestTypeDef = TypedDict(
    "_RequiredListCandidatesForAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)
_OptionalListCandidatesForAutoMLJobRequestRequestTypeDef = TypedDict(
    "_OptionalListCandidatesForAutoMLJobRequestRequestTypeDef",
    {
        "StatusEquals": CandidateStatusType,
        "CandidateNameEquals": str,
        "SortOrder": AutoMLSortOrderType,
        "SortBy": CandidateSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCandidatesForAutoMLJobRequestRequestTypeDef(
    _RequiredListCandidatesForAutoMLJobRequestRequestTypeDef,
    _OptionalListCandidatesForAutoMLJobRequestRequestTypeDef,
):
    pass

ListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "ListCandidatesForAutoMLJobResponseTypeDef",
    {
        "Candidates": List["AutoMLCandidateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCodeRepositoriesInputRequestTypeDef = TypedDict(
    "ListCodeRepositoriesInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": CodeRepositorySortByType,
        "SortOrder": CodeRepositorySortOrderType,
    },
    total=False,
)

ListCodeRepositoriesOutputTypeDef = TypedDict(
    "ListCodeRepositoriesOutputTypeDef",
    {
        "CodeRepositorySummaryList": List["CodeRepositorySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCompilationJobsRequestRequestTypeDef = TypedDict(
    "ListCompilationJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": CompilationJobStatusType,
        "SortBy": ListCompilationJobsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListCompilationJobsResponseTypeDef = TypedDict(
    "ListCompilationJobsResponseTypeDef",
    {
        "CompilationJobSummaries": List["CompilationJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContextsRequestRequestTypeDef = TypedDict(
    "ListContextsRequestRequestTypeDef",
    {
        "SourceUri": str,
        "ContextType": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortContextsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListContextsResponseTypeDef = TypedDict(
    "ListContextsResponseTypeDef",
    {
        "ContextSummaries": List["ContextSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListDataQualityJobDefinitionsResponseTypeDef = TypedDict(
    "ListDataQualityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceFleetsRequestRequestTypeDef = TypedDict(
    "ListDeviceFleetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "SortBy": ListDeviceFleetsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListDeviceFleetsResponseTypeDef = TypedDict(
    "ListDeviceFleetsResponseTypeDef",
    {
        "DeviceFleetSummaries": List["DeviceFleetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LatestHeartbeatAfter": Union[datetime, str],
        "ModelName": str,
        "DeviceFleetName": str,
    },
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "DeviceSummaries": List["DeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List["DomainDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEdgeDeploymentPlansRequestRequestTypeDef = TypedDict(
    "ListEdgeDeploymentPlansRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "DeviceFleetNameContains": str,
        "SortBy": ListEdgeDeploymentPlansSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListEdgeDeploymentPlansResponseTypeDef = TypedDict(
    "ListEdgeDeploymentPlansResponseTypeDef",
    {
        "EdgeDeploymentPlanSummaries": List["EdgeDeploymentPlanSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEdgePackagingJobsRequestRequestTypeDef = TypedDict(
    "ListEdgePackagingJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "ModelNameContains": str,
        "StatusEquals": EdgePackagingJobStatusType,
        "SortBy": ListEdgePackagingJobsSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListEdgePackagingJobsResponseTypeDef = TypedDict(
    "ListEdgePackagingJobsResponseTypeDef",
    {
        "EdgePackagingJobSummaries": List["EdgePackagingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointConfigsInputRequestTypeDef = TypedDict(
    "ListEndpointConfigsInputRequestTypeDef",
    {
        "SortBy": EndpointConfigSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListEndpointConfigsOutputTypeDef = TypedDict(
    "ListEndpointConfigsOutputTypeDef",
    {
        "EndpointConfigs": List["EndpointConfigSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsInputRequestTypeDef = TypedDict(
    "ListEndpointsInputRequestTypeDef",
    {
        "SortBy": EndpointSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": EndpointStatusType,
    },
    total=False,
)

ListEndpointsOutputTypeDef = TypedDict(
    "ListEndpointsOutputTypeDef",
    {
        "Endpoints": List["EndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortExperimentsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "ExperimentSummaries": List["ExperimentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFeatureGroupsRequestRequestTypeDef = TypedDict(
    "ListFeatureGroupsRequestRequestTypeDef",
    {
        "NameContains": str,
        "FeatureGroupStatusEquals": FeatureGroupStatusType,
        "OfflineStoreStatusEquals": OfflineStoreStatusValueType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": FeatureGroupSortOrderType,
        "SortBy": FeatureGroupSortByType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListFeatureGroupsResponseTypeDef = TypedDict(
    "ListFeatureGroupsResponseTypeDef",
    {
        "FeatureGroupSummaries": List["FeatureGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowDefinitionsRequestRequestTypeDef = TypedDict(
    "ListFlowDefinitionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFlowDefinitionsResponseTypeDef = TypedDict(
    "ListFlowDefinitionsResponseTypeDef",
    {
        "FlowDefinitionSummaries": List["FlowDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHubContentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListHubContentVersionsRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
        "HubContentName": str,
    },
)
_OptionalListHubContentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListHubContentVersionsRequestRequestTypeDef",
    {
        "MinVersion": str,
        "MaxSchemaVersion": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "SortBy": HubContentSortByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListHubContentVersionsRequestRequestTypeDef(
    _RequiredListHubContentVersionsRequestRequestTypeDef,
    _OptionalListHubContentVersionsRequestRequestTypeDef,
):
    pass

ListHubContentVersionsResponseTypeDef = TypedDict(
    "ListHubContentVersionsResponseTypeDef",
    {
        "HubContentSummaries": List["HubContentInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHubContentsRequestRequestTypeDef = TypedDict(
    "_RequiredListHubContentsRequestRequestTypeDef",
    {
        "HubName": str,
        "HubContentType": HubContentTypeType,
    },
)
_OptionalListHubContentsRequestRequestTypeDef = TypedDict(
    "_OptionalListHubContentsRequestRequestTypeDef",
    {
        "NameContains": str,
        "MaxSchemaVersion": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "SortBy": HubContentSortByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListHubContentsRequestRequestTypeDef(
    _RequiredListHubContentsRequestRequestTypeDef, _OptionalListHubContentsRequestRequestTypeDef
):
    pass

ListHubContentsResponseTypeDef = TypedDict(
    "ListHubContentsResponseTypeDef",
    {
        "HubContentSummaries": List["HubContentInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHubsRequestRequestTypeDef = TypedDict(
    "ListHubsRequestRequestTypeDef",
    {
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "SortBy": HubSortByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListHubsResponseTypeDef = TypedDict(
    "ListHubsResponseTypeDef",
    {
        "HubSummaries": List["HubInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHumanTaskUisRequestRequestTypeDef = TypedDict(
    "ListHumanTaskUisRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListHumanTaskUisResponseTypeDef = TypedDict(
    "ListHumanTaskUisResponseTypeDef",
    {
        "HumanTaskUiSummaries": List["HumanTaskUiSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHyperParameterTuningJobsRequestRequestTypeDef = TypedDict(
    "ListHyperParameterTuningJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": HyperParameterTuningJobSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "StatusEquals": HyperParameterTuningJobStatusType,
    },
    total=False,
)

ListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "ListHyperParameterTuningJobsResponseTypeDef",
    {
        "HyperParameterTuningJobSummaries": List["HyperParameterTuningJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListImageVersionsRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalListImageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListImageVersionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "SortBy": ImageVersionSortByType,
        "SortOrder": ImageVersionSortOrderType,
    },
    total=False,
)

class ListImageVersionsRequestRequestTypeDef(
    _RequiredListImageVersionsRequestRequestTypeDef, _OptionalListImageVersionsRequestRequestTypeDef
):
    pass

ListImageVersionsResponseTypeDef = TypedDict(
    "ListImageVersionsResponseTypeDef",
    {
        "ImageVersions": List["ImageVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ImageSortByType,
        "SortOrder": ImageSortOrderType,
    },
    total=False,
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInferenceExperimentsRequestRequestTypeDef = TypedDict(
    "ListInferenceExperimentsRequestRequestTypeDef",
    {
        "NameContains": str,
        "Type": Literal["ShadowMode"],
        "StatusEquals": InferenceExperimentStatusType,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "SortBy": SortInferenceExperimentsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListInferenceExperimentsResponseTypeDef = TypedDict(
    "ListInferenceExperimentsResponseTypeDef",
    {
        "InferenceExperiments": List["InferenceExperimentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInferenceRecommendationsJobStepsRequestRequestTypeDef = TypedDict(
    "_RequiredListInferenceRecommendationsJobStepsRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalListInferenceRecommendationsJobStepsRequestRequestTypeDef = TypedDict(
    "_OptionalListInferenceRecommendationsJobStepsRequestRequestTypeDef",
    {
        "Status": RecommendationJobStatusType,
        "StepType": Literal["BENCHMARK"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListInferenceRecommendationsJobStepsRequestRequestTypeDef(
    _RequiredListInferenceRecommendationsJobStepsRequestRequestTypeDef,
    _OptionalListInferenceRecommendationsJobStepsRequestRequestTypeDef,
):
    pass

ListInferenceRecommendationsJobStepsResponseTypeDef = TypedDict(
    "ListInferenceRecommendationsJobStepsResponseTypeDef",
    {
        "Steps": List["InferenceRecommendationsJobStepTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInferenceRecommendationsJobsRequestRequestTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": RecommendationJobStatusType,
        "SortBy": ListInferenceRecommendationsJobsSortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "ModelNameEquals": str,
        "ModelPackageVersionArnEquals": str,
    },
    total=False,
)

ListInferenceRecommendationsJobsResponseTypeDef = TypedDict(
    "ListInferenceRecommendationsJobsResponseTypeDef",
    {
        "InferenceRecommendationsJobs": List["InferenceRecommendationsJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLabelingJobsForWorkteamRequestRequestTypeDef = TypedDict(
    "_RequiredListLabelingJobsForWorkteamRequestRequestTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalListLabelingJobsForWorkteamRequestRequestTypeDef = TypedDict(
    "_OptionalListLabelingJobsForWorkteamRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "JobReferenceCodeContains": str,
        "SortBy": Literal["CreationTime"],
        "SortOrder": SortOrderType,
    },
    total=False,
)

class ListLabelingJobsForWorkteamRequestRequestTypeDef(
    _RequiredListLabelingJobsForWorkteamRequestRequestTypeDef,
    _OptionalListLabelingJobsForWorkteamRequestRequestTypeDef,
):
    pass

ListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "ListLabelingJobsForWorkteamResponseTypeDef",
    {
        "LabelingJobSummaryList": List["LabelingJobForWorkteamSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLabelingJobsRequestRequestTypeDef = TypedDict(
    "ListLabelingJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "StatusEquals": LabelingJobStatusType,
    },
    total=False,
)

ListLabelingJobsResponseTypeDef = TypedDict(
    "ListLabelingJobsResponseTypeDef",
    {
        "LabelingJobSummaryList": List["LabelingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLineageGroupsRequestRequestTypeDef = TypedDict(
    "ListLineageGroupsRequestRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortLineageGroupsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLineageGroupsResponseTypeDef = TypedDict(
    "ListLineageGroupsResponseTypeDef",
    {
        "LineageGroupSummaries": List["LineageGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelBiasJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelBiasJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelBiasJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListModelCardExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListModelCardExportJobsRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalListModelCardExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListModelCardExportJobsRequestRequestTypeDef",
    {
        "ModelCardVersion": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "ModelCardExportJobNameContains": str,
        "StatusEquals": ModelCardExportJobStatusType,
        "SortBy": ModelCardExportJobSortByType,
        "SortOrder": ModelCardExportJobSortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListModelCardExportJobsRequestRequestTypeDef(
    _RequiredListModelCardExportJobsRequestRequestTypeDef,
    _OptionalListModelCardExportJobsRequestRequestTypeDef,
):
    pass

ListModelCardExportJobsResponseTypeDef = TypedDict(
    "ListModelCardExportJobsResponseTypeDef",
    {
        "ModelCardExportJobSummaries": List["ModelCardExportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListModelCardVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListModelCardVersionsRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalListModelCardVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListModelCardVersionsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "ModelCardStatus": ModelCardStatusType,
        "NextToken": str,
        "SortBy": Literal["Version"],
        "SortOrder": ModelCardSortOrderType,
    },
    total=False,
)

class ListModelCardVersionsRequestRequestTypeDef(
    _RequiredListModelCardVersionsRequestRequestTypeDef,
    _OptionalListModelCardVersionsRequestRequestTypeDef,
):
    pass

ListModelCardVersionsResponseTypeDef = TypedDict(
    "ListModelCardVersionsResponseTypeDef",
    {
        "ModelCardVersionSummaryList": List["ModelCardVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelCardsRequestRequestTypeDef = TypedDict(
    "ListModelCardsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "ModelCardStatus": ModelCardStatusType,
        "NextToken": str,
        "SortBy": ModelCardSortByType,
        "SortOrder": ModelCardSortOrderType,
    },
    total=False,
)

ListModelCardsResponseTypeDef = TypedDict(
    "ListModelCardsResponseTypeDef",
    {
        "ModelCardSummaries": List["ModelCardSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelExplainabilityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelExplainabilityJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelMetadataRequestRequestTypeDef = TypedDict(
    "ListModelMetadataRequestRequestTypeDef",
    {
        "SearchExpression": "ModelMetadataSearchExpressionTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListModelMetadataResponseTypeDef = TypedDict(
    "ListModelMetadataResponseTypeDef",
    {
        "ModelMetadataSummaries": List["ModelMetadataSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackageGroupsInputRequestTypeDef = TypedDict(
    "ListModelPackageGroupsInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ModelPackageGroupSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListModelPackageGroupsOutputTypeDef = TypedDict(
    "ListModelPackageGroupsOutputTypeDef",
    {
        "ModelPackageGroupSummaryList": List["ModelPackageGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackagesInputRequestTypeDef = TypedDict(
    "ListModelPackagesInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "ModelPackageGroupName": str,
        "ModelPackageType": ModelPackageTypeType,
        "NextToken": str,
        "SortBy": ModelPackageSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListModelPackagesOutputTypeDef = TypedDict(
    "ListModelPackagesOutputTypeDef",
    {
        "ModelPackageSummaryList": List["ModelPackageSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelQualityJobDefinitionsRequestRequestTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringJobDefinitionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelQualityJobDefinitionsResponseTypeDef = TypedDict(
    "ListModelQualityJobDefinitionsResponseTypeDef",
    {
        "JobDefinitionSummaries": List["MonitoringJobDefinitionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelsInputRequestTypeDef = TypedDict(
    "ListModelsInputRequestTypeDef",
    {
        "SortBy": ModelSortKeyType,
        "SortOrder": OrderKeyType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListModelsOutputTypeDef = TypedDict(
    "ListModelsOutputTypeDef",
    {
        "Models": List["ModelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringAlertHistoryRequestRequestTypeDef = TypedDict(
    "ListMonitoringAlertHistoryRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "SortBy": MonitoringAlertHistorySortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "StatusEquals": MonitoringAlertStatusType,
    },
    total=False,
)

ListMonitoringAlertHistoryResponseTypeDef = TypedDict(
    "ListMonitoringAlertHistoryResponseTypeDef",
    {
        "MonitoringAlertHistory": List["MonitoringAlertHistorySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMonitoringAlertsRequestRequestTypeDef = TypedDict(
    "_RequiredListMonitoringAlertsRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)
_OptionalListMonitoringAlertsRequestRequestTypeDef = TypedDict(
    "_OptionalListMonitoringAlertsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListMonitoringAlertsRequestRequestTypeDef(
    _RequiredListMonitoringAlertsRequestRequestTypeDef,
    _OptionalListMonitoringAlertsRequestRequestTypeDef,
):
    pass

ListMonitoringAlertsResponseTypeDef = TypedDict(
    "ListMonitoringAlertsResponseTypeDef",
    {
        "MonitoringAlertSummaries": List["MonitoringAlertSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringExecutionsRequestRequestTypeDef = TypedDict(
    "ListMonitoringExecutionsRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "EndpointName": str,
        "SortBy": MonitoringExecutionSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "ScheduledTimeBefore": Union[datetime, str],
        "ScheduledTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ExecutionStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
    },
    total=False,
)

ListMonitoringExecutionsResponseTypeDef = TypedDict(
    "ListMonitoringExecutionsResponseTypeDef",
    {
        "MonitoringExecutionSummaries": List["MonitoringExecutionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitoringSchedulesRequestRequestTypeDef = TypedDict(
    "ListMonitoringSchedulesRequestRequestTypeDef",
    {
        "EndpointName": str,
        "SortBy": MonitoringScheduleSortKeyType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": ScheduleStatusType,
        "MonitoringJobDefinitionName": str,
        "MonitoringTypeEquals": MonitoringTypeType,
    },
    total=False,
)

ListMonitoringSchedulesResponseTypeDef = TypedDict(
    "ListMonitoringSchedulesResponseTypeDef",
    {
        "MonitoringScheduleSummaries": List["MonitoringScheduleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookInstanceLifecycleConfigsInputRequestTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": NotebookInstanceLifecycleConfigSortKeyType,
        "SortOrder": NotebookInstanceLifecycleConfigSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
    },
    total=False,
)

ListNotebookInstanceLifecycleConfigsOutputTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List["NotebookInstanceLifecycleConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookInstancesInputRequestTypeDef = TypedDict(
    "ListNotebookInstancesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortBy": NotebookInstanceSortKeyType,
        "SortOrder": NotebookInstanceSortOrderType,
        "NameContains": str,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "StatusEquals": NotebookInstanceStatusType,
        "NotebookInstanceLifecycleConfigNameContains": str,
        "DefaultCodeRepositoryContains": str,
        "AdditionalCodeRepositoryEquals": str,
    },
    total=False,
)

ListNotebookInstancesOutputTypeDef = TypedDict(
    "ListNotebookInstancesOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List["NotebookInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelineExecutionStepsRequestRequestTypeDef = TypedDict(
    "ListPipelineExecutionStepsRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListPipelineExecutionStepsResponseTypeDef = TypedDict(
    "ListPipelineExecutionStepsResponseTypeDef",
    {
        "PipelineExecutionSteps": List["PipelineExecutionStepTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPipelineExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalListPipelineExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsRequestRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelineExecutionsByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPipelineExecutionsRequestRequestTypeDef(
    _RequiredListPipelineExecutionsRequestRequestTypeDef,
    _OptionalListPipelineExecutionsRequestRequestTypeDef,
):
    pass

ListPipelineExecutionsResponseTypeDef = TypedDict(
    "ListPipelineExecutionsResponseTypeDef",
    {
        "PipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPipelineParametersForExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredListPipelineParametersForExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalListPipelineParametersForExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalListPipelineParametersForExecutionRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPipelineParametersForExecutionRequestRequestTypeDef(
    _RequiredListPipelineParametersForExecutionRequestRequestTypeDef,
    _OptionalListPipelineParametersForExecutionRequestRequestTypeDef,
):
    pass

ListPipelineParametersForExecutionResponseTypeDef = TypedDict(
    "ListPipelineParametersForExecutionResponseTypeDef",
    {
        "PipelineParameters": List["ParameterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "PipelineNamePrefix": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortPipelinesByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "PipelineSummaries": List["PipelineSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProcessingJobsRequestRequestTypeDef = TypedDict(
    "ListProcessingJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": ProcessingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProcessingJobsResponseTypeDef = TypedDict(
    "ListProcessingJobsResponseTypeDef",
    {
        "ProcessingJobSummaries": List["ProcessingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "MaxResults": int,
        "NameContains": str,
        "NextToken": str,
        "SortBy": ProjectSortByType,
        "SortOrder": ProjectSortOrderType,
    },
    total=False,
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "ProjectSummaryList": List["ProjectSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceCatalogsRequestRequestTypeDef = TypedDict(
    "ListResourceCatalogsRequestRequestTypeDef",
    {
        "NameContains": str,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "SortOrder": ResourceCatalogSortOrderType,
        "SortBy": Literal["CreationTime"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListResourceCatalogsResponseTypeDef = TypedDict(
    "ListResourceCatalogsResponseTypeDef",
    {
        "ResourceCatalogs": List["ResourceCatalogTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpacesRequestRequestTypeDef = TypedDict(
    "ListSpacesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": SpaceSortKeyType,
        "DomainIdEquals": str,
        "SpaceNameContains": str,
    },
    total=False,
)

ListSpacesResponseTypeDef = TypedDict(
    "ListSpacesResponseTypeDef",
    {
        "Spaces": List["SpaceDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStageDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredListStageDevicesRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)
_OptionalListStageDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalListStageDevicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ExcludeDevicesDeployedInOtherStage": bool,
    },
    total=False,
)

class ListStageDevicesRequestRequestTypeDef(
    _RequiredListStageDevicesRequestRequestTypeDef, _OptionalListStageDevicesRequestRequestTypeDef
):
    pass

ListStageDevicesResponseTypeDef = TypedDict(
    "ListStageDevicesResponseTypeDef",
    {
        "DeviceDeploymentSummaries": List["DeviceDeploymentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioLifecycleConfigsRequestRequestTypeDef = TypedDict(
    "ListStudioLifecycleConfigsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "NameContains": str,
        "AppTypeEquals": StudioLifecycleConfigAppTypeType,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
        "ModifiedTimeBefore": Union[datetime, str],
        "ModifiedTimeAfter": Union[datetime, str],
        "SortBy": StudioLifecycleConfigSortKeyType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ListStudioLifecycleConfigsResponseTypeDef = TypedDict(
    "ListStudioLifecycleConfigsResponseTypeDef",
    {
        "NextToken": str,
        "StudioLifecycleConfigs": List["StudioLifecycleConfigDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribedWorkteamsRequestRequestTypeDef = TypedDict(
    "ListSubscribedWorkteamsRequestRequestTypeDef",
    {
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "ListSubscribedWorkteamsResponseTypeDef",
    {
        "SubscribedWorkteams": List["SubscribedWorkteamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsInputRequestTypeDef = TypedDict(
    "_RequiredListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsInputRequestTypeDef = TypedDict(
    "_OptionalListTagsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsInputRequestTypeDef(
    _RequiredListTagsInputRequestTypeDef, _OptionalListTagsInputRequestTypeDef
):
    pass

ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_RequiredListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)
_OptionalListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "_OptionalListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": TrainingJobSortByOptionsType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

class ListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef,
    _OptionalListTrainingJobsForHyperParameterTuningJobRequestRequestTypeDef,
):
    pass

ListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {
        "TrainingJobSummaries": List["HyperParameterTrainingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrainingJobsRequestRequestTypeDef = TypedDict(
    "ListTrainingJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TrainingJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "WarmPoolStatusEquals": WarmPoolResourceStatusType,
    },
    total=False,
)

ListTrainingJobsResponseTypeDef = TypedDict(
    "ListTrainingJobsResponseTypeDef",
    {
        "TrainingJobSummaries": List["TrainingJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransformJobsRequestRequestTypeDef = TypedDict(
    "ListTransformJobsRequestRequestTypeDef",
    {
        "CreationTimeAfter": Union[datetime, str],
        "CreationTimeBefore": Union[datetime, str],
        "LastModifiedTimeAfter": Union[datetime, str],
        "LastModifiedTimeBefore": Union[datetime, str],
        "NameContains": str,
        "StatusEquals": TransformJobStatusType,
        "SortBy": SortByType,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTransformJobsResponseTypeDef = TypedDict(
    "ListTransformJobsResponseTypeDef",
    {
        "TransformJobSummaries": List["TransformJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrialComponentsRequestRequestTypeDef = TypedDict(
    "ListTrialComponentsRequestRequestTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
        "SourceArn": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialComponentsByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTrialComponentsResponseTypeDef = TypedDict(
    "ListTrialComponentsResponseTypeDef",
    {
        "TrialComponentSummaries": List["TrialComponentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrialsRequestRequestTypeDef = TypedDict(
    "ListTrialsRequestRequestTypeDef",
    {
        "ExperimentName": str,
        "TrialComponentName": str,
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "SortBy": SortTrialsByType,
        "SortOrder": SortOrderType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListTrialsResponseTypeDef = TypedDict(
    "ListTrialsResponseTypeDef",
    {
        "TrialSummaries": List["TrialSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserProfilesRequestRequestTypeDef = TypedDict(
    "ListUserProfilesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "SortOrder": SortOrderType,
        "SortBy": UserProfileSortKeyType,
        "DomainIdEquals": str,
        "UserProfileNameContains": str,
    },
    total=False,
)

ListUserProfilesResponseTypeDef = TypedDict(
    "ListUserProfilesResponseTypeDef",
    {
        "UserProfiles": List["UserProfileDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkforcesRequestRequestTypeDef = TypedDict(
    "ListWorkforcesRequestRequestTypeDef",
    {
        "SortBy": ListWorkforcesSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkforcesResponseTypeDef = TypedDict(
    "ListWorkforcesResponseTypeDef",
    {
        "Workforces": List["WorkforceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkteamsRequestRequestTypeDef = TypedDict(
    "ListWorkteamsRequestRequestTypeDef",
    {
        "SortBy": ListWorkteamsSortByOptionsType,
        "SortOrder": SortOrderType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkteamsResponseTypeDef = TypedDict(
    "ListWorkteamsResponseTypeDef",
    {
        "Workteams": List["WorkteamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberDefinitionTypeDef = TypedDict(
    "MemberDefinitionTypeDef",
    {
        "CognitoMemberDefinition": "CognitoMemberDefinitionTypeDef",
        "OidcMemberDefinition": "OidcMemberDefinitionTypeDef",
    },
    total=False,
)

MetadataPropertiesTypeDef = TypedDict(
    "MetadataPropertiesTypeDef",
    {
        "CommitId": str,
        "Repository": str,
        "GeneratedBy": str,
        "ProjectId": str,
    },
    total=False,
)

MetricDataTypeDef = TypedDict(
    "MetricDataTypeDef",
    {
        "MetricName": str,
        "Value": float,
        "Timestamp": datetime,
    },
    total=False,
)

MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": AutoMLMetricEnumType,
        "Value": float,
        "Set": MetricSetSourceType,
        "StandardMetricName": AutoMLMetricExtendedEnumType,
    },
    total=False,
)

MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "Name": str,
        "Regex": str,
    },
)

MetricSpecificationTypeDef = TypedDict(
    "MetricSpecificationTypeDef",
    {
        "Predefined": "PredefinedMetricSpecificationTypeDef",
        "Customized": "CustomizedMetricSpecificationTypeDef",
    },
    total=False,
)

_RequiredMetricsSourceTypeDef = TypedDict(
    "_RequiredMetricsSourceTypeDef",
    {
        "ContentType": str,
        "S3Uri": str,
    },
)
_OptionalMetricsSourceTypeDef = TypedDict(
    "_OptionalMetricsSourceTypeDef",
    {
        "ContentDigest": str,
    },
    total=False,
)

class MetricsSourceTypeDef(_RequiredMetricsSourceTypeDef, _OptionalMetricsSourceTypeDef):
    pass

ModelAccessConfigTypeDef = TypedDict(
    "ModelAccessConfigTypeDef",
    {
        "AcceptEula": bool,
    },
)

ModelArtifactsTypeDef = TypedDict(
    "ModelArtifactsTypeDef",
    {
        "S3ModelArtifacts": str,
    },
)

_RequiredModelBiasAppSpecificationTypeDef = TypedDict(
    "_RequiredModelBiasAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelBiasAppSpecificationTypeDef = TypedDict(
    "_OptionalModelBiasAppSpecificationTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)

class ModelBiasAppSpecificationTypeDef(
    _RequiredModelBiasAppSpecificationTypeDef, _OptionalModelBiasAppSpecificationTypeDef
):
    pass

ModelBiasBaselineConfigTypeDef = TypedDict(
    "ModelBiasBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
    },
    total=False,
)

_RequiredModelBiasJobInputTypeDef = TypedDict(
    "_RequiredModelBiasJobInputTypeDef",
    {
        "GroundTruthS3Input": "MonitoringGroundTruthS3InputTypeDef",
    },
)
_OptionalModelBiasJobInputTypeDef = TypedDict(
    "_OptionalModelBiasJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "BatchTransformInput": "BatchTransformInputTypeDef",
    },
    total=False,
)

class ModelBiasJobInputTypeDef(
    _RequiredModelBiasJobInputTypeDef, _OptionalModelBiasJobInputTypeDef
):
    pass

ModelCardExportArtifactsTypeDef = TypedDict(
    "ModelCardExportArtifactsTypeDef",
    {
        "S3ExportArtifacts": str,
    },
)

ModelCardExportJobSummaryTypeDef = TypedDict(
    "ModelCardExportJobSummaryTypeDef",
    {
        "ModelCardExportJobName": str,
        "ModelCardExportJobArn": str,
        "Status": ModelCardExportJobStatusType,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "CreatedAt": datetime,
        "LastModifiedAt": datetime,
    },
)

ModelCardExportOutputConfigTypeDef = TypedDict(
    "ModelCardExportOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)

ModelCardSecurityConfigTypeDef = TypedDict(
    "ModelCardSecurityConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredModelCardSummaryTypeDef = TypedDict(
    "_RequiredModelCardSummaryTypeDef",
    {
        "ModelCardName": str,
        "ModelCardArn": str,
        "ModelCardStatus": ModelCardStatusType,
        "CreationTime": datetime,
    },
)
_OptionalModelCardSummaryTypeDef = TypedDict(
    "_OptionalModelCardSummaryTypeDef",
    {
        "LastModifiedTime": datetime,
    },
    total=False,
)

class ModelCardSummaryTypeDef(_RequiredModelCardSummaryTypeDef, _OptionalModelCardSummaryTypeDef):
    pass

ModelCardTypeDef = TypedDict(
    "ModelCardTypeDef",
    {
        "ModelCardArn": str,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
        "SecurityConfig": "ModelCardSecurityConfigTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Tags": List["TagTypeDef"],
        "ModelId": str,
        "RiskRating": str,
        "ModelPackageGroupName": str,
    },
    total=False,
)

_RequiredModelCardVersionSummaryTypeDef = TypedDict(
    "_RequiredModelCardVersionSummaryTypeDef",
    {
        "ModelCardName": str,
        "ModelCardArn": str,
        "ModelCardStatus": ModelCardStatusType,
        "ModelCardVersion": int,
        "CreationTime": datetime,
    },
)
_OptionalModelCardVersionSummaryTypeDef = TypedDict(
    "_OptionalModelCardVersionSummaryTypeDef",
    {
        "LastModifiedTime": datetime,
    },
    total=False,
)

class ModelCardVersionSummaryTypeDef(
    _RequiredModelCardVersionSummaryTypeDef, _OptionalModelCardVersionSummaryTypeDef
):
    pass

ModelClientConfigTypeDef = TypedDict(
    "ModelClientConfigTypeDef",
    {
        "InvocationsTimeoutInSeconds": int,
        "InvocationsMaxRetries": int,
    },
    total=False,
)

ModelConfigurationTypeDef = TypedDict(
    "ModelConfigurationTypeDef",
    {
        "InferenceSpecificationName": str,
        "EnvironmentParameters": List["EnvironmentParameterTypeDef"],
        "CompilationJobName": str,
    },
    total=False,
)

ModelDashboardEndpointTypeDef = TypedDict(
    "ModelDashboardEndpointTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": EndpointStatusType,
    },
)

ModelDashboardIndicatorActionTypeDef = TypedDict(
    "ModelDashboardIndicatorActionTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ModelDashboardModelCardTypeDef = TypedDict(
    "ModelDashboardModelCardTypeDef",
    {
        "ModelCardArn": str,
        "ModelCardName": str,
        "ModelCardVersion": int,
        "ModelCardStatus": ModelCardStatusType,
        "SecurityConfig": "ModelCardSecurityConfigTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Tags": List["TagTypeDef"],
        "ModelId": str,
        "RiskRating": str,
    },
    total=False,
)

ModelDashboardModelTypeDef = TypedDict(
    "ModelDashboardModelTypeDef",
    {
        "Model": "ModelTypeDef",
        "Endpoints": List["ModelDashboardEndpointTypeDef"],
        "LastBatchTransformJob": "TransformJobTypeDef",
        "MonitoringSchedules": List["ModelDashboardMonitoringScheduleTypeDef"],
        "ModelCard": "ModelDashboardModelCardTypeDef",
    },
    total=False,
)

ModelDashboardMonitoringScheduleTypeDef = TypedDict(
    "ModelDashboardMonitoringScheduleTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "EndpointName": str,
        "MonitoringAlertSummaries": List["MonitoringAlertSummaryTypeDef"],
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
        "BatchTransformInput": "BatchTransformInputTypeDef",
    },
    total=False,
)

ModelDataQualityTypeDef = TypedDict(
    "ModelDataQualityTypeDef",
    {
        "Statistics": "MetricsSourceTypeDef",
        "Constraints": "MetricsSourceTypeDef",
    },
    total=False,
)

ModelDataSourceTypeDef = TypedDict(
    "ModelDataSourceTypeDef",
    {
        "S3DataSource": "S3ModelDataSourceTypeDef",
    },
)

ModelDeployConfigTypeDef = TypedDict(
    "ModelDeployConfigTypeDef",
    {
        "AutoGenerateEndpointName": bool,
        "EndpointName": str,
    },
    total=False,
)

ModelDeployResultTypeDef = TypedDict(
    "ModelDeployResultTypeDef",
    {
        "EndpointName": str,
    },
    total=False,
)

ModelDigestsTypeDef = TypedDict(
    "ModelDigestsTypeDef",
    {
        "ArtifactDigest": str,
    },
    total=False,
)

_RequiredModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "_RequiredModelExplainabilityAppSpecificationTypeDef",
    {
        "ImageUri": str,
        "ConfigUri": str,
    },
)
_OptionalModelExplainabilityAppSpecificationTypeDef = TypedDict(
    "_OptionalModelExplainabilityAppSpecificationTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)

class ModelExplainabilityAppSpecificationTypeDef(
    _RequiredModelExplainabilityAppSpecificationTypeDef,
    _OptionalModelExplainabilityAppSpecificationTypeDef,
):
    pass

ModelExplainabilityBaselineConfigTypeDef = TypedDict(
    "ModelExplainabilityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
    },
    total=False,
)

ModelExplainabilityJobInputTypeDef = TypedDict(
    "ModelExplainabilityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "BatchTransformInput": "BatchTransformInputTypeDef",
    },
    total=False,
)

ModelInfrastructureConfigTypeDef = TypedDict(
    "ModelInfrastructureConfigTypeDef",
    {
        "InfrastructureType": Literal["RealTimeInference"],
        "RealTimeInferenceConfig": "RealTimeInferenceConfigTypeDef",
    },
)

ModelInputTypeDef = TypedDict(
    "ModelInputTypeDef",
    {
        "DataInputConfig": str,
    },
)

ModelLatencyThresholdTypeDef = TypedDict(
    "ModelLatencyThresholdTypeDef",
    {
        "Percentile": str,
        "ValueInMilliseconds": int,
    },
    total=False,
)

ModelMetadataFilterTypeDef = TypedDict(
    "ModelMetadataFilterTypeDef",
    {
        "Name": ModelMetadataFilterTypeType,
        "Value": str,
    },
)

ModelMetadataSearchExpressionTypeDef = TypedDict(
    "ModelMetadataSearchExpressionTypeDef",
    {
        "Filters": List["ModelMetadataFilterTypeDef"],
    },
    total=False,
)

ModelMetadataSummaryTypeDef = TypedDict(
    "ModelMetadataSummaryTypeDef",
    {
        "Domain": str,
        "Framework": str,
        "Task": str,
        "Model": str,
        "FrameworkVersion": str,
    },
)

ModelMetricsTypeDef = TypedDict(
    "ModelMetricsTypeDef",
    {
        "ModelQuality": "ModelQualityTypeDef",
        "ModelDataQuality": "ModelDataQualityTypeDef",
        "Bias": "BiasTypeDef",
        "Explainability": "ExplainabilityTypeDef",
    },
    total=False,
)

_RequiredModelPackageContainerDefinitionTypeDef = TypedDict(
    "_RequiredModelPackageContainerDefinitionTypeDef",
    {
        "Image": str,
    },
)
_OptionalModelPackageContainerDefinitionTypeDef = TypedDict(
    "_OptionalModelPackageContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "ImageDigest": str,
        "ModelDataUrl": str,
        "ProductId": str,
        "Environment": Dict[str, str],
        "ModelInput": "ModelInputTypeDef",
        "Framework": str,
        "FrameworkVersion": str,
        "NearestModelName": str,
        "AdditionalS3DataSource": "AdditionalS3DataSourceTypeDef",
    },
    total=False,
)

class ModelPackageContainerDefinitionTypeDef(
    _RequiredModelPackageContainerDefinitionTypeDef, _OptionalModelPackageContainerDefinitionTypeDef
):
    pass

_RequiredModelPackageGroupSummaryTypeDef = TypedDict(
    "_RequiredModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "CreationTime": datetime,
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
    },
)
_OptionalModelPackageGroupSummaryTypeDef = TypedDict(
    "_OptionalModelPackageGroupSummaryTypeDef",
    {
        "ModelPackageGroupDescription": str,
    },
    total=False,
)

class ModelPackageGroupSummaryTypeDef(
    _RequiredModelPackageGroupSummaryTypeDef, _OptionalModelPackageGroupSummaryTypeDef
):
    pass

ModelPackageGroupTypeDef = TypedDict(
    "ModelPackageGroupTypeDef",
    {
        "ModelPackageGroupName": str,
        "ModelPackageGroupArn": str,
        "ModelPackageGroupDescription": str,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "ModelPackageGroupStatus": ModelPackageGroupStatusType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredModelPackageStatusDetailsTypeDef = TypedDict(
    "_RequiredModelPackageStatusDetailsTypeDef",
    {
        "ValidationStatuses": List["ModelPackageStatusItemTypeDef"],
    },
)
_OptionalModelPackageStatusDetailsTypeDef = TypedDict(
    "_OptionalModelPackageStatusDetailsTypeDef",
    {
        "ImageScanStatuses": List["ModelPackageStatusItemTypeDef"],
    },
    total=False,
)

class ModelPackageStatusDetailsTypeDef(
    _RequiredModelPackageStatusDetailsTypeDef, _OptionalModelPackageStatusDetailsTypeDef
):
    pass

_RequiredModelPackageStatusItemTypeDef = TypedDict(
    "_RequiredModelPackageStatusItemTypeDef",
    {
        "Name": str,
        "Status": DetailedModelPackageStatusType,
    },
)
_OptionalModelPackageStatusItemTypeDef = TypedDict(
    "_OptionalModelPackageStatusItemTypeDef",
    {
        "FailureReason": str,
    },
    total=False,
)

class ModelPackageStatusItemTypeDef(
    _RequiredModelPackageStatusItemTypeDef, _OptionalModelPackageStatusItemTypeDef
):
    pass

_RequiredModelPackageSummaryTypeDef = TypedDict(
    "_RequiredModelPackageSummaryTypeDef",
    {
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": ModelPackageStatusType,
    },
)
_OptionalModelPackageSummaryTypeDef = TypedDict(
    "_OptionalModelPackageSummaryTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageDescription": str,
        "ModelApprovalStatus": ModelApprovalStatusType,
    },
    total=False,
)

class ModelPackageSummaryTypeDef(
    _RequiredModelPackageSummaryTypeDef, _OptionalModelPackageSummaryTypeDef
):
    pass

ModelPackageTypeDef = TypedDict(
    "ModelPackageTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageGroupName": str,
        "ModelPackageVersion": int,
        "ModelPackageArn": str,
        "ModelPackageDescription": str,
        "CreationTime": datetime,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "ModelPackageStatus": ModelPackageStatusType,
        "ModelPackageStatusDetails": "ModelPackageStatusDetailsTypeDef",
        "CertifyForMarketplace": bool,
        "ModelApprovalStatus": ModelApprovalStatusType,
        "CreatedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "ModelMetrics": "ModelMetricsTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "ApprovalDescription": str,
        "Domain": str,
        "Task": str,
        "SamplePayloadUrl": str,
        "AdditionalInferenceSpecifications": List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ],
        "Tags": List["TagTypeDef"],
        "CustomerMetadataProperties": Dict[str, str],
        "DriftCheckBaselines": "DriftCheckBaselinesTypeDef",
        "SkipModelValidation": SkipModelValidationType,
    },
    total=False,
)

ModelPackageValidationProfileTypeDef = TypedDict(
    "ModelPackageValidationProfileTypeDef",
    {
        "ProfileName": str,
        "TransformJobDefinition": "TransformJobDefinitionTypeDef",
    },
)

ModelPackageValidationSpecificationTypeDef = TypedDict(
    "ModelPackageValidationSpecificationTypeDef",
    {
        "ValidationRole": str,
        "ValidationProfiles": List["ModelPackageValidationProfileTypeDef"],
    },
)

_RequiredModelQualityAppSpecificationTypeDef = TypedDict(
    "_RequiredModelQualityAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalModelQualityAppSpecificationTypeDef = TypedDict(
    "_OptionalModelQualityAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
        "ProblemType": MonitoringProblemTypeType,
        "Environment": Dict[str, str],
    },
    total=False,
)

class ModelQualityAppSpecificationTypeDef(
    _RequiredModelQualityAppSpecificationTypeDef, _OptionalModelQualityAppSpecificationTypeDef
):
    pass

ModelQualityBaselineConfigTypeDef = TypedDict(
    "ModelQualityBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
    },
    total=False,
)

_RequiredModelQualityJobInputTypeDef = TypedDict(
    "_RequiredModelQualityJobInputTypeDef",
    {
        "GroundTruthS3Input": "MonitoringGroundTruthS3InputTypeDef",
    },
)
_OptionalModelQualityJobInputTypeDef = TypedDict(
    "_OptionalModelQualityJobInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "BatchTransformInput": "BatchTransformInputTypeDef",
    },
    total=False,
)

class ModelQualityJobInputTypeDef(
    _RequiredModelQualityJobInputTypeDef, _OptionalModelQualityJobInputTypeDef
):
    pass

ModelQualityTypeDef = TypedDict(
    "ModelQualityTypeDef",
    {
        "Statistics": "MetricsSourceTypeDef",
        "Constraints": "MetricsSourceTypeDef",
    },
    total=False,
)

ModelRegisterSettingsTypeDef = TypedDict(
    "ModelRegisterSettingsTypeDef",
    {
        "Status": FeatureStatusType,
        "CrossAccountModelRegisterRoleArn": str,
    },
    total=False,
)

ModelStepMetadataTypeDef = TypedDict(
    "ModelStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "CreationTime": datetime,
    },
)

ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "ModelName": str,
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "InferenceExecutionConfig": "InferenceExecutionConfigTypeDef",
        "ExecutionRoleArn": str,
        "VpcConfig": "VpcConfigTypeDef",
        "CreationTime": datetime,
        "ModelArn": str,
        "EnableNetworkIsolation": bool,
        "Tags": List["TagTypeDef"],
        "DeploymentRecommendation": "DeploymentRecommendationTypeDef",
    },
    total=False,
)

ModelVariantConfigSummaryTypeDef = TypedDict(
    "ModelVariantConfigSummaryTypeDef",
    {
        "ModelName": str,
        "VariantName": str,
        "InfrastructureConfig": "ModelInfrastructureConfigTypeDef",
        "Status": ModelVariantStatusType,
    },
)

ModelVariantConfigTypeDef = TypedDict(
    "ModelVariantConfigTypeDef",
    {
        "ModelName": str,
        "VariantName": str,
        "InfrastructureConfig": "ModelInfrastructureConfigTypeDef",
    },
)

MonitoringAlertActionsTypeDef = TypedDict(
    "MonitoringAlertActionsTypeDef",
    {
        "ModelDashboardIndicator": "ModelDashboardIndicatorActionTypeDef",
    },
    total=False,
)

MonitoringAlertHistorySummaryTypeDef = TypedDict(
    "MonitoringAlertHistorySummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "CreationTime": datetime,
        "AlertStatus": MonitoringAlertStatusType,
    },
)

MonitoringAlertSummaryTypeDef = TypedDict(
    "MonitoringAlertSummaryTypeDef",
    {
        "MonitoringAlertName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "AlertStatus": MonitoringAlertStatusType,
        "DatapointsToAlert": int,
        "EvaluationPeriod": int,
        "Actions": "MonitoringAlertActionsTypeDef",
    },
)

_RequiredMonitoringAppSpecificationTypeDef = TypedDict(
    "_RequiredMonitoringAppSpecificationTypeDef",
    {
        "ImageUri": str,
    },
)
_OptionalMonitoringAppSpecificationTypeDef = TypedDict(
    "_OptionalMonitoringAppSpecificationTypeDef",
    {
        "ContainerEntrypoint": List[str],
        "ContainerArguments": List[str],
        "RecordPreprocessorSourceUri": str,
        "PostAnalyticsProcessorSourceUri": str,
    },
    total=False,
)

class MonitoringAppSpecificationTypeDef(
    _RequiredMonitoringAppSpecificationTypeDef, _OptionalMonitoringAppSpecificationTypeDef
):
    pass

MonitoringBaselineConfigTypeDef = TypedDict(
    "MonitoringBaselineConfigTypeDef",
    {
        "BaseliningJobName": str,
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
        "StatisticsResource": "MonitoringStatisticsResourceTypeDef",
    },
    total=False,
)

_RequiredMonitoringClusterConfigTypeDef = TypedDict(
    "_RequiredMonitoringClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalMonitoringClusterConfigTypeDef = TypedDict(
    "_OptionalMonitoringClusterConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)

class MonitoringClusterConfigTypeDef(
    _RequiredMonitoringClusterConfigTypeDef, _OptionalMonitoringClusterConfigTypeDef
):
    pass

MonitoringConstraintsResourceTypeDef = TypedDict(
    "MonitoringConstraintsResourceTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringCsvDatasetFormatTypeDef = TypedDict(
    "MonitoringCsvDatasetFormatTypeDef",
    {
        "Header": bool,
    },
    total=False,
)

MonitoringDatasetFormatTypeDef = TypedDict(
    "MonitoringDatasetFormatTypeDef",
    {
        "Csv": "MonitoringCsvDatasetFormatTypeDef",
        "Json": "MonitoringJsonDatasetFormatTypeDef",
        "Parquet": Dict[str, Any],
    },
    total=False,
)

_RequiredMonitoringExecutionSummaryTypeDef = TypedDict(
    "_RequiredMonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": ExecutionStatusType,
    },
)
_OptionalMonitoringExecutionSummaryTypeDef = TypedDict(
    "_OptionalMonitoringExecutionSummaryTypeDef",
    {
        "ProcessingJobArn": str,
        "EndpointName": str,
        "FailureReason": str,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)

class MonitoringExecutionSummaryTypeDef(
    _RequiredMonitoringExecutionSummaryTypeDef, _OptionalMonitoringExecutionSummaryTypeDef
):
    pass

MonitoringGroundTruthS3InputTypeDef = TypedDict(
    "MonitoringGroundTruthS3InputTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringInputTypeDef = TypedDict(
    "MonitoringInputTypeDef",
    {
        "EndpointInput": "EndpointInputTypeDef",
        "BatchTransformInput": "BatchTransformInputTypeDef",
    },
    total=False,
)

MonitoringJobDefinitionSummaryTypeDef = TypedDict(
    "MonitoringJobDefinitionSummaryTypeDef",
    {
        "MonitoringJobDefinitionName": str,
        "MonitoringJobDefinitionArn": str,
        "CreationTime": datetime,
        "EndpointName": str,
    },
)

_RequiredMonitoringJobDefinitionTypeDef = TypedDict(
    "_RequiredMonitoringJobDefinitionTypeDef",
    {
        "MonitoringInputs": List["MonitoringInputTypeDef"],
        "MonitoringOutputConfig": "MonitoringOutputConfigTypeDef",
        "MonitoringResources": "MonitoringResourcesTypeDef",
        "MonitoringAppSpecification": "MonitoringAppSpecificationTypeDef",
        "RoleArn": str,
    },
)
_OptionalMonitoringJobDefinitionTypeDef = TypedDict(
    "_OptionalMonitoringJobDefinitionTypeDef",
    {
        "BaselineConfig": "MonitoringBaselineConfigTypeDef",
        "StoppingCondition": "MonitoringStoppingConditionTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
    },
    total=False,
)

class MonitoringJobDefinitionTypeDef(
    _RequiredMonitoringJobDefinitionTypeDef, _OptionalMonitoringJobDefinitionTypeDef
):
    pass

MonitoringJsonDatasetFormatTypeDef = TypedDict(
    "MonitoringJsonDatasetFormatTypeDef",
    {
        "Line": bool,
    },
    total=False,
)

MonitoringNetworkConfigTypeDef = TypedDict(
    "MonitoringNetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

_RequiredMonitoringOutputConfigTypeDef = TypedDict(
    "_RequiredMonitoringOutputConfigTypeDef",
    {
        "MonitoringOutputs": List["MonitoringOutputTypeDef"],
    },
)
_OptionalMonitoringOutputConfigTypeDef = TypedDict(
    "_OptionalMonitoringOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class MonitoringOutputConfigTypeDef(
    _RequiredMonitoringOutputConfigTypeDef, _OptionalMonitoringOutputConfigTypeDef
):
    pass

MonitoringOutputTypeDef = TypedDict(
    "MonitoringOutputTypeDef",
    {
        "S3Output": "MonitoringS3OutputTypeDef",
    },
)

MonitoringResourcesTypeDef = TypedDict(
    "MonitoringResourcesTypeDef",
    {
        "ClusterConfig": "MonitoringClusterConfigTypeDef",
    },
)

_RequiredMonitoringS3OutputTypeDef = TypedDict(
    "_RequiredMonitoringS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
    },
)
_OptionalMonitoringS3OutputTypeDef = TypedDict(
    "_OptionalMonitoringS3OutputTypeDef",
    {
        "S3UploadMode": ProcessingS3UploadModeType,
    },
    total=False,
)

class MonitoringS3OutputTypeDef(
    _RequiredMonitoringS3OutputTypeDef, _OptionalMonitoringS3OutputTypeDef
):
    pass

MonitoringScheduleConfigTypeDef = TypedDict(
    "MonitoringScheduleConfigTypeDef",
    {
        "ScheduleConfig": "ScheduleConfigTypeDef",
        "MonitoringJobDefinition": "MonitoringJobDefinitionTypeDef",
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)

_RequiredMonitoringScheduleSummaryTypeDef = TypedDict(
    "_RequiredMonitoringScheduleSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": ScheduleStatusType,
    },
)
_OptionalMonitoringScheduleSummaryTypeDef = TypedDict(
    "_OptionalMonitoringScheduleSummaryTypeDef",
    {
        "EndpointName": str,
        "MonitoringJobDefinitionName": str,
        "MonitoringType": MonitoringTypeType,
    },
    total=False,
)

class MonitoringScheduleSummaryTypeDef(
    _RequiredMonitoringScheduleSummaryTypeDef, _OptionalMonitoringScheduleSummaryTypeDef
):
    pass

MonitoringScheduleTypeDef = TypedDict(
    "MonitoringScheduleTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": ScheduleStatusType,
        "MonitoringType": MonitoringTypeType,
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
        "EndpointName": str,
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

MonitoringStatisticsResourceTypeDef = TypedDict(
    "MonitoringStatisticsResourceTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

MonitoringStoppingConditionTypeDef = TypedDict(
    "MonitoringStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

MultiModelConfigTypeDef = TypedDict(
    "MultiModelConfigTypeDef",
    {
        "ModelCacheSetting": ModelCacheSettingType,
    },
    total=False,
)

NeoVpcConfigTypeDef = TypedDict(
    "NeoVpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

NestedFiltersTypeDef = TypedDict(
    "NestedFiltersTypeDef",
    {
        "NestedPropertyName": str,
        "Filters": List["FilterTypeDef"],
    },
)

NetworkConfigTypeDef = TypedDict(
    "NetworkConfigTypeDef",
    {
        "EnableInterContainerTrafficEncryption": bool,
        "EnableNetworkIsolation": bool,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
        "NotebookInstanceLifecycleConfigArn": str,
    },
)
_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef",
    {
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

class NotebookInstanceLifecycleConfigSummaryTypeDef(
    _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef,
    _OptionalNotebookInstanceLifecycleConfigSummaryTypeDef,
):
    pass

NotebookInstanceLifecycleHookTypeDef = TypedDict(
    "NotebookInstanceLifecycleHookTypeDef",
    {
        "Content": str,
    },
    total=False,
)

_RequiredNotebookInstanceSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceName": str,
        "NotebookInstanceArn": str,
    },
)
_OptionalNotebookInstanceSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceStatus": NotebookInstanceStatusType,
        "Url": str,
        "InstanceType": InstanceTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
    },
    total=False,
)

class NotebookInstanceSummaryTypeDef(
    _RequiredNotebookInstanceSummaryTypeDef, _OptionalNotebookInstanceSummaryTypeDef
):
    pass

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "NotificationTopicArn": str,
    },
    total=False,
)

ObjectiveStatusCountersTypeDef = TypedDict(
    "ObjectiveStatusCountersTypeDef",
    {
        "Succeeded": int,
        "Pending": int,
        "Failed": int,
    },
    total=False,
)

_RequiredOfflineStoreConfigTypeDef = TypedDict(
    "_RequiredOfflineStoreConfigTypeDef",
    {
        "S3StorageConfig": "S3StorageConfigTypeDef",
    },
)
_OptionalOfflineStoreConfigTypeDef = TypedDict(
    "_OptionalOfflineStoreConfigTypeDef",
    {
        "DisableGlueTableCreation": bool,
        "DataCatalogConfig": "DataCatalogConfigTypeDef",
        "TableFormat": TableFormatType,
    },
    total=False,
)

class OfflineStoreConfigTypeDef(
    _RequiredOfflineStoreConfigTypeDef, _OptionalOfflineStoreConfigTypeDef
):
    pass

_RequiredOfflineStoreStatusTypeDef = TypedDict(
    "_RequiredOfflineStoreStatusTypeDef",
    {
        "Status": OfflineStoreStatusValueType,
    },
)
_OptionalOfflineStoreStatusTypeDef = TypedDict(
    "_OptionalOfflineStoreStatusTypeDef",
    {
        "BlockedReason": str,
    },
    total=False,
)

class OfflineStoreStatusTypeDef(
    _RequiredOfflineStoreStatusTypeDef, _OptionalOfflineStoreStatusTypeDef
):
    pass

OidcConfigForResponseTypeDef = TypedDict(
    "OidcConfigForResponseTypeDef",
    {
        "ClientId": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
    total=False,
)

OidcConfigTypeDef = TypedDict(
    "OidcConfigTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "LogoutEndpoint": str,
        "JwksUri": str,
    },
)

OidcMemberDefinitionTypeDef = TypedDict(
    "OidcMemberDefinitionTypeDef",
    {
        "Groups": List[str],
    },
)

OnlineStoreConfigTypeDef = TypedDict(
    "OnlineStoreConfigTypeDef",
    {
        "SecurityConfig": "OnlineStoreSecurityConfigTypeDef",
        "EnableOnlineStore": bool,
        "TtlDuration": "TtlDurationTypeDef",
        "StorageType": StorageTypeType,
    },
    total=False,
)

OnlineStoreConfigUpdateTypeDef = TypedDict(
    "OnlineStoreConfigUpdateTypeDef",
    {
        "TtlDuration": "TtlDurationTypeDef",
    },
    total=False,
)

OnlineStoreSecurityConfigTypeDef = TypedDict(
    "OnlineStoreSecurityConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredOutputConfigTypeDef = TypedDict(
    "_RequiredOutputConfigTypeDef",
    {
        "S3OutputLocation": str,
    },
)
_OptionalOutputConfigTypeDef = TypedDict(
    "_OptionalOutputConfigTypeDef",
    {
        "TargetDevice": TargetDeviceType,
        "TargetPlatform": "TargetPlatformTypeDef",
        "CompilerOptions": str,
        "KmsKeyId": str,
    },
    total=False,
)

class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, _OptionalOutputConfigTypeDef):
    pass

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
        "CompressionType": OutputCompressionTypeType,
    },
    total=False,
)

class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass

OutputParameterTypeDef = TypedDict(
    "OutputParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParallelismConfigurationTypeDef = TypedDict(
    "ParallelismConfigurationTypeDef",
    {
        "MaxParallelExecutionSteps": int,
    },
)

ParameterRangeTypeDef = TypedDict(
    "ParameterRangeTypeDef",
    {
        "IntegerParameterRangeSpecification": "IntegerParameterRangeSpecificationTypeDef",
        "ContinuousParameterRangeSpecification": "ContinuousParameterRangeSpecificationTypeDef",
        "CategoricalParameterRangeSpecification": "CategoricalParameterRangeSpecificationTypeDef",
    },
    total=False,
)

ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "IntegerParameterRanges": List["IntegerParameterRangeTypeDef"],
        "ContinuousParameterRanges": List["ContinuousParameterRangeTypeDef"],
        "CategoricalParameterRanges": List["CategoricalParameterRangeTypeDef"],
        "AutoParameters": List["AutoParameterTypeDef"],
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

ParentHyperParameterTuningJobTypeDef = TypedDict(
    "ParentHyperParameterTuningJobTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
    total=False,
)

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "TrialName": str,
        "ExperimentName": str,
    },
    total=False,
)

_RequiredPendingDeploymentSummaryTypeDef = TypedDict(
    "_RequiredPendingDeploymentSummaryTypeDef",
    {
        "EndpointConfigName": str,
    },
)
_OptionalPendingDeploymentSummaryTypeDef = TypedDict(
    "_OptionalPendingDeploymentSummaryTypeDef",
    {
        "ProductionVariants": List["PendingProductionVariantSummaryTypeDef"],
        "StartTime": datetime,
        "ShadowProductionVariants": List["PendingProductionVariantSummaryTypeDef"],
    },
    total=False,
)

class PendingDeploymentSummaryTypeDef(
    _RequiredPendingDeploymentSummaryTypeDef, _OptionalPendingDeploymentSummaryTypeDef
):
    pass

_RequiredPendingProductionVariantSummaryTypeDef = TypedDict(
    "_RequiredPendingProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalPendingProductionVariantSummaryTypeDef = TypedDict(
    "_OptionalPendingProductionVariantSummaryTypeDef",
    {
        "DeployedImages": List["DeployedImageTypeDef"],
        "CurrentWeight": float,
        "DesiredWeight": float,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
        "InstanceType": ProductionVariantInstanceTypeType,
        "AcceleratorType": ProductionVariantAcceleratorTypeType,
        "VariantStatus": List["ProductionVariantStatusTypeDef"],
        "CurrentServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
        "DesiredServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
    },
    total=False,
)

class PendingProductionVariantSummaryTypeDef(
    _RequiredPendingProductionVariantSummaryTypeDef, _OptionalPendingProductionVariantSummaryTypeDef
):
    pass

PhaseTypeDef = TypedDict(
    "PhaseTypeDef",
    {
        "InitialNumberOfUsers": int,
        "SpawnRate": int,
        "DurationInSeconds": int,
    },
    total=False,
)

_RequiredPipelineDefinitionS3LocationTypeDef = TypedDict(
    "_RequiredPipelineDefinitionS3LocationTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
    },
)
_OptionalPipelineDefinitionS3LocationTypeDef = TypedDict(
    "_OptionalPipelineDefinitionS3LocationTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)

class PipelineDefinitionS3LocationTypeDef(
    _RequiredPipelineDefinitionS3LocationTypeDef, _OptionalPipelineDefinitionS3LocationTypeDef
):
    pass

PipelineExecutionStepMetadataTypeDef = TypedDict(
    "PipelineExecutionStepMetadataTypeDef",
    {
        "TrainingJob": "TrainingJobStepMetadataTypeDef",
        "ProcessingJob": "ProcessingJobStepMetadataTypeDef",
        "TransformJob": "TransformJobStepMetadataTypeDef",
        "TuningJob": "TuningJobStepMetaDataTypeDef",
        "Model": "ModelStepMetadataTypeDef",
        "RegisterModel": "RegisterModelStepMetadataTypeDef",
        "Condition": "ConditionStepMetadataTypeDef",
        "Callback": "CallbackStepMetadataTypeDef",
        "Lambda": "LambdaStepMetadataTypeDef",
        "QualityCheck": "QualityCheckStepMetadataTypeDef",
        "ClarifyCheck": "ClarifyCheckStepMetadataTypeDef",
        "EMR": "EMRStepMetadataTypeDef",
        "Fail": "FailStepMetadataTypeDef",
        "AutoMLJob": "AutoMLJobStepMetadataTypeDef",
    },
    total=False,
)

PipelineExecutionStepTypeDef = TypedDict(
    "PipelineExecutionStepTypeDef",
    {
        "StepName": str,
        "StepDisplayName": str,
        "StepDescription": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "StepStatus": StepStatusType,
        "CacheHitResult": "CacheHitResultTypeDef",
        "AttemptCount": int,
        "FailureReason": str,
        "Metadata": "PipelineExecutionStepMetadataTypeDef",
        "SelectiveExecutionResult": "SelectiveExecutionResultTypeDef",
    },
    total=False,
)

PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "PipelineExecutionArn": str,
        "StartTime": datetime,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionFailureReason": str,
    },
    total=False,
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "PipelineArn": str,
        "PipelineExecutionArn": str,
        "PipelineExecutionDisplayName": str,
        "PipelineExecutionStatus": PipelineExecutionStatusType,
        "PipelineExecutionDescription": str,
        "PipelineExperimentConfig": "PipelineExperimentConfigTypeDef",
        "FailureReason": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "PipelineParameters": List["ParameterTypeDef"],
        "SelectiveExecutionConfig": "SelectiveExecutionConfigTypeDef",
    },
    total=False,
)

PipelineExperimentConfigTypeDef = TypedDict(
    "PipelineExperimentConfigTypeDef",
    {
        "ExperimentName": str,
        "TrialName": str,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastExecutionTime": datetime,
    },
    total=False,
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "PipelineArn": str,
        "PipelineName": str,
        "PipelineDisplayName": str,
        "PipelineDescription": str,
        "RoleArn": str,
        "PipelineStatus": Literal["Active"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastRunTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedBy": "UserContextTypeDef",
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

PredefinedMetricSpecificationTypeDef = TypedDict(
    "PredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": str,
    },
    total=False,
)

_RequiredProcessingClusterConfigTypeDef = TypedDict(
    "_RequiredProcessingClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
    },
)
_OptionalProcessingClusterConfigTypeDef = TypedDict(
    "_OptionalProcessingClusterConfigTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)

class ProcessingClusterConfigTypeDef(
    _RequiredProcessingClusterConfigTypeDef, _OptionalProcessingClusterConfigTypeDef
):
    pass

ProcessingFeatureStoreOutputTypeDef = TypedDict(
    "ProcessingFeatureStoreOutputTypeDef",
    {
        "FeatureGroupName": str,
    },
)

_RequiredProcessingInputTypeDef = TypedDict(
    "_RequiredProcessingInputTypeDef",
    {
        "InputName": str,
    },
)
_OptionalProcessingInputTypeDef = TypedDict(
    "_OptionalProcessingInputTypeDef",
    {
        "AppManaged": bool,
        "S3Input": "ProcessingS3InputTypeDef",
        "DatasetDefinition": "DatasetDefinitionTypeDef",
    },
    total=False,
)

class ProcessingInputTypeDef(_RequiredProcessingInputTypeDef, _OptionalProcessingInputTypeDef):
    pass

ProcessingJobStepMetadataTypeDef = TypedDict(
    "ProcessingJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredProcessingJobSummaryTypeDef = TypedDict(
    "_RequiredProcessingJobSummaryTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingJobStatus": ProcessingJobStatusType,
    },
)
_OptionalProcessingJobSummaryTypeDef = TypedDict(
    "_OptionalProcessingJobSummaryTypeDef",
    {
        "ProcessingEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ExitMessage": str,
    },
    total=False,
)

class ProcessingJobSummaryTypeDef(
    _RequiredProcessingJobSummaryTypeDef, _OptionalProcessingJobSummaryTypeDef
):
    pass

ProcessingJobTypeDef = TypedDict(
    "ProcessingJobTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "RoleArn": str,
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ProcessingJobArn": str,
        "ProcessingJobStatus": ProcessingJobStatusType,
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredProcessingOutputConfigTypeDef = TypedDict(
    "_RequiredProcessingOutputConfigTypeDef",
    {
        "Outputs": List["ProcessingOutputTypeDef"],
    },
)
_OptionalProcessingOutputConfigTypeDef = TypedDict(
    "_OptionalProcessingOutputConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class ProcessingOutputConfigTypeDef(
    _RequiredProcessingOutputConfigTypeDef, _OptionalProcessingOutputConfigTypeDef
):
    pass

_RequiredProcessingOutputTypeDef = TypedDict(
    "_RequiredProcessingOutputTypeDef",
    {
        "OutputName": str,
    },
)
_OptionalProcessingOutputTypeDef = TypedDict(
    "_OptionalProcessingOutputTypeDef",
    {
        "S3Output": "ProcessingS3OutputTypeDef",
        "FeatureStoreOutput": "ProcessingFeatureStoreOutputTypeDef",
        "AppManaged": bool,
    },
    total=False,
)

class ProcessingOutputTypeDef(_RequiredProcessingOutputTypeDef, _OptionalProcessingOutputTypeDef):
    pass

ProcessingResourcesTypeDef = TypedDict(
    "ProcessingResourcesTypeDef",
    {
        "ClusterConfig": "ProcessingClusterConfigTypeDef",
    },
)

_RequiredProcessingS3InputTypeDef = TypedDict(
    "_RequiredProcessingS3InputTypeDef",
    {
        "S3Uri": str,
        "S3DataType": ProcessingS3DataTypeType,
    },
)
_OptionalProcessingS3InputTypeDef = TypedDict(
    "_OptionalProcessingS3InputTypeDef",
    {
        "LocalPath": str,
        "S3InputMode": ProcessingS3InputModeType,
        "S3DataDistributionType": ProcessingS3DataDistributionTypeType,
        "S3CompressionType": ProcessingS3CompressionTypeType,
    },
    total=False,
)

class ProcessingS3InputTypeDef(
    _RequiredProcessingS3InputTypeDef, _OptionalProcessingS3InputTypeDef
):
    pass

ProcessingS3OutputTypeDef = TypedDict(
    "ProcessingS3OutputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3UploadMode": ProcessingS3UploadModeType,
    },
)

ProcessingStoppingConditionTypeDef = TypedDict(
    "ProcessingStoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
    },
)

_RequiredProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "_RequiredProductionVariantCoreDumpConfigTypeDef",
    {
        "DestinationS3Uri": str,
    },
)
_OptionalProductionVariantCoreDumpConfigTypeDef = TypedDict(
    "_OptionalProductionVariantCoreDumpConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class ProductionVariantCoreDumpConfigTypeDef(
    _RequiredProductionVariantCoreDumpConfigTypeDef, _OptionalProductionVariantCoreDumpConfigTypeDef
):
    pass

_RequiredProductionVariantServerlessConfigTypeDef = TypedDict(
    "_RequiredProductionVariantServerlessConfigTypeDef",
    {
        "MemorySizeInMB": int,
        "MaxConcurrency": int,
    },
)
_OptionalProductionVariantServerlessConfigTypeDef = TypedDict(
    "_OptionalProductionVariantServerlessConfigTypeDef",
    {
        "ProvisionedConcurrency": int,
    },
    total=False,
)

class ProductionVariantServerlessConfigTypeDef(
    _RequiredProductionVariantServerlessConfigTypeDef,
    _OptionalProductionVariantServerlessConfigTypeDef,
):
    pass

ProductionVariantServerlessUpdateConfigTypeDef = TypedDict(
    "ProductionVariantServerlessUpdateConfigTypeDef",
    {
        "MaxConcurrency": int,
        "ProvisionedConcurrency": int,
    },
    total=False,
)

_RequiredProductionVariantStatusTypeDef = TypedDict(
    "_RequiredProductionVariantStatusTypeDef",
    {
        "Status": VariantStatusType,
    },
)
_OptionalProductionVariantStatusTypeDef = TypedDict(
    "_OptionalProductionVariantStatusTypeDef",
    {
        "StatusMessage": str,
        "StartTime": datetime,
    },
    total=False,
)

class ProductionVariantStatusTypeDef(
    _RequiredProductionVariantStatusTypeDef, _OptionalProductionVariantStatusTypeDef
):
    pass

_RequiredProductionVariantSummaryTypeDef = TypedDict(
    "_RequiredProductionVariantSummaryTypeDef",
    {
        "VariantName": str,
    },
)
_OptionalProductionVariantSummaryTypeDef = TypedDict(
    "_OptionalProductionVariantSummaryTypeDef",
    {
        "DeployedImages": List["DeployedImageTypeDef"],
        "CurrentWeight": float,
        "DesiredWeight": float,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
        "VariantStatus": List["ProductionVariantStatusTypeDef"],
        "CurrentServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
        "DesiredServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
    },
    total=False,
)

class ProductionVariantSummaryTypeDef(
    _RequiredProductionVariantSummaryTypeDef, _OptionalProductionVariantSummaryTypeDef
):
    pass

_RequiredProductionVariantTypeDef = TypedDict(
    "_RequiredProductionVariantTypeDef",
    {
        "VariantName": str,
        "ModelName": str,
    },
)
_OptionalProductionVariantTypeDef = TypedDict(
    "_OptionalProductionVariantTypeDef",
    {
        "InitialInstanceCount": int,
        "InstanceType": ProductionVariantInstanceTypeType,
        "InitialVariantWeight": float,
        "AcceleratorType": ProductionVariantAcceleratorTypeType,
        "CoreDumpConfig": "ProductionVariantCoreDumpConfigTypeDef",
        "ServerlessConfig": "ProductionVariantServerlessConfigTypeDef",
        "VolumeSizeInGB": int,
        "ModelDataDownloadTimeoutInSeconds": int,
        "ContainerStartupHealthCheckTimeoutInSeconds": int,
        "EnableSSMAccess": bool,
    },
    total=False,
)

class ProductionVariantTypeDef(
    _RequiredProductionVariantTypeDef, _OptionalProductionVariantTypeDef
):
    pass

ProfilerConfigForUpdateTypeDef = TypedDict(
    "ProfilerConfigForUpdateTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Dict[str, str],
        "DisableProfiler": bool,
    },
    total=False,
)

ProfilerConfigTypeDef = TypedDict(
    "ProfilerConfigTypeDef",
    {
        "S3OutputPath": str,
        "ProfilingIntervalInMilliseconds": int,
        "ProfilingParameters": Dict[str, str],
        "DisableProfiler": bool,
    },
    total=False,
)

_RequiredProfilerRuleConfigurationTypeDef = TypedDict(
    "_RequiredProfilerRuleConfigurationTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluatorImage": str,
    },
)
_OptionalProfilerRuleConfigurationTypeDef = TypedDict(
    "_OptionalProfilerRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": ProcessingInstanceTypeType,
        "VolumeSizeInGB": int,
        "RuleParameters": Dict[str, str],
    },
    total=False,
)

class ProfilerRuleConfigurationTypeDef(
    _RequiredProfilerRuleConfigurationTypeDef, _OptionalProfilerRuleConfigurationTypeDef
):
    pass

ProfilerRuleEvaluationStatusTypeDef = TypedDict(
    "ProfilerRuleEvaluationStatusTypeDef",
    {
        "RuleConfigurationName": str,
        "RuleEvaluationJobArn": str,
        "RuleEvaluationStatus": RuleEvaluationStatusType,
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "ProjectName": str,
        "ProjectArn": str,
        "ProjectId": str,
        "CreationTime": datetime,
        "ProjectStatus": ProjectStatusType,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "ProjectDescription": str,
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "ProjectId": str,
        "ProjectDescription": str,
        "ServiceCatalogProvisioningDetails": "ServiceCatalogProvisioningDetailsTypeDef",
        "ServiceCatalogProvisionedProductDetails": "ServiceCatalogProvisionedProductDetailsTypeDef",
        "ProjectStatus": ProjectStatusType,
        "CreatedBy": "UserContextTypeDef",
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
    },
    total=False,
)

PropertyNameQueryTypeDef = TypedDict(
    "PropertyNameQueryTypeDef",
    {
        "PropertyNameHint": str,
    },
)

PropertyNameSuggestionTypeDef = TypedDict(
    "PropertyNameSuggestionTypeDef",
    {
        "PropertyName": str,
    },
    total=False,
)

ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

PublicWorkforceTaskPriceTypeDef = TypedDict(
    "PublicWorkforceTaskPriceTypeDef",
    {
        "AmountInUsd": "USDTypeDef",
    },
    total=False,
)

PutModelPackageGroupPolicyInputRequestTypeDef = TypedDict(
    "PutModelPackageGroupPolicyInputRequestTypeDef",
    {
        "ModelPackageGroupName": str,
        "ResourcePolicy": str,
    },
)

PutModelPackageGroupPolicyOutputTypeDef = TypedDict(
    "PutModelPackageGroupPolicyOutputTypeDef",
    {
        "ModelPackageGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QualityCheckStepMetadataTypeDef = TypedDict(
    "QualityCheckStepMetadataTypeDef",
    {
        "CheckType": str,
        "BaselineUsedForDriftCheckStatistics": str,
        "BaselineUsedForDriftCheckConstraints": str,
        "CalculatedBaselineStatistics": str,
        "CalculatedBaselineConstraints": str,
        "ModelPackageGroupName": str,
        "ViolationReport": str,
        "CheckJobArn": str,
        "SkipCheck": bool,
        "RegisterNewBaseline": bool,
    },
    total=False,
)

QueryFiltersTypeDef = TypedDict(
    "QueryFiltersTypeDef",
    {
        "Types": List[str],
        "LineageTypes": List[LineageTypeType],
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
        "ModifiedBefore": Union[datetime, str],
        "ModifiedAfter": Union[datetime, str],
        "Properties": Dict[str, str],
    },
    total=False,
)

QueryLineageRequestRequestTypeDef = TypedDict(
    "QueryLineageRequestRequestTypeDef",
    {
        "StartArns": List[str],
        "Direction": DirectionType,
        "IncludeEdges": bool,
        "Filters": "QueryFiltersTypeDef",
        "MaxDepth": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

QueryLineageResponseTypeDef = TypedDict(
    "QueryLineageResponseTypeDef",
    {
        "Vertices": List["VertexTypeDef"],
        "Edges": List["EdgeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RSessionAppSettingsTypeDef = TypedDict(
    "RSessionAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
        "CustomImages": List["CustomImageTypeDef"],
    },
    total=False,
)

RStudioServerProAppSettingsTypeDef = TypedDict(
    "RStudioServerProAppSettingsTypeDef",
    {
        "AccessStatus": RStudioServerProAccessStatusType,
        "UserGroup": RStudioServerProUserGroupType,
    },
    total=False,
)

_RequiredRStudioServerProDomainSettingsForUpdateTypeDef = TypedDict(
    "_RequiredRStudioServerProDomainSettingsForUpdateTypeDef",
    {
        "DomainExecutionRoleArn": str,
    },
)
_OptionalRStudioServerProDomainSettingsForUpdateTypeDef = TypedDict(
    "_OptionalRStudioServerProDomainSettingsForUpdateTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
        "RStudioConnectUrl": str,
        "RStudioPackageManagerUrl": str,
    },
    total=False,
)

class RStudioServerProDomainSettingsForUpdateTypeDef(
    _RequiredRStudioServerProDomainSettingsForUpdateTypeDef,
    _OptionalRStudioServerProDomainSettingsForUpdateTypeDef,
):
    pass

_RequiredRStudioServerProDomainSettingsTypeDef = TypedDict(
    "_RequiredRStudioServerProDomainSettingsTypeDef",
    {
        "DomainExecutionRoleArn": str,
    },
)
_OptionalRStudioServerProDomainSettingsTypeDef = TypedDict(
    "_OptionalRStudioServerProDomainSettingsTypeDef",
    {
        "RStudioConnectUrl": str,
        "RStudioPackageManagerUrl": str,
        "DefaultResourceSpec": "ResourceSpecTypeDef",
    },
    total=False,
)

class RStudioServerProDomainSettingsTypeDef(
    _RequiredRStudioServerProDomainSettingsTypeDef, _OptionalRStudioServerProDomainSettingsTypeDef
):
    pass

RealTimeInferenceConfigTypeDef = TypedDict(
    "RealTimeInferenceConfigTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "InstanceCount": int,
    },
)

_RequiredRealTimeInferenceRecommendationTypeDef = TypedDict(
    "_RequiredRealTimeInferenceRecommendationTypeDef",
    {
        "RecommendationId": str,
        "InstanceType": ProductionVariantInstanceTypeType,
    },
)
_OptionalRealTimeInferenceRecommendationTypeDef = TypedDict(
    "_OptionalRealTimeInferenceRecommendationTypeDef",
    {
        "Environment": Dict[str, str],
    },
    total=False,
)

class RealTimeInferenceRecommendationTypeDef(
    _RequiredRealTimeInferenceRecommendationTypeDef, _OptionalRealTimeInferenceRecommendationTypeDef
):
    pass

RecommendationJobCompiledOutputConfigTypeDef = TypedDict(
    "RecommendationJobCompiledOutputConfigTypeDef",
    {
        "S3OutputUri": str,
    },
    total=False,
)

RecommendationJobContainerConfigTypeDef = TypedDict(
    "RecommendationJobContainerConfigTypeDef",
    {
        "Domain": str,
        "Task": str,
        "Framework": str,
        "FrameworkVersion": str,
        "PayloadConfig": "RecommendationJobPayloadConfigTypeDef",
        "NearestModelName": str,
        "SupportedInstanceTypes": List[str],
        "DataInputConfig": str,
        "SupportedEndpointType": RecommendationJobSupportedEndpointTypeType,
        "SupportedResponseMIMETypes": List[str],
    },
    total=False,
)

_RequiredRecommendationJobInferenceBenchmarkTypeDef = TypedDict(
    "_RequiredRecommendationJobInferenceBenchmarkTypeDef",
    {
        "ModelConfiguration": "ModelConfigurationTypeDef",
    },
)
_OptionalRecommendationJobInferenceBenchmarkTypeDef = TypedDict(
    "_OptionalRecommendationJobInferenceBenchmarkTypeDef",
    {
        "Metrics": "RecommendationMetricsTypeDef",
        "EndpointConfiguration": "EndpointOutputConfigurationTypeDef",
        "FailureReason": str,
        "EndpointMetrics": "InferenceMetricsTypeDef",
        "InvocationEndTime": datetime,
        "InvocationStartTime": datetime,
    },
    total=False,
)

class RecommendationJobInferenceBenchmarkTypeDef(
    _RequiredRecommendationJobInferenceBenchmarkTypeDef,
    _OptionalRecommendationJobInferenceBenchmarkTypeDef,
):
    pass

RecommendationJobInputConfigTypeDef = TypedDict(
    "RecommendationJobInputConfigTypeDef",
    {
        "ModelPackageVersionArn": str,
        "JobDurationInSeconds": int,
        "TrafficPattern": "TrafficPatternTypeDef",
        "ResourceLimit": "RecommendationJobResourceLimitTypeDef",
        "EndpointConfigurations": List["EndpointInputConfigurationTypeDef"],
        "VolumeKmsKeyId": str,
        "ContainerConfig": "RecommendationJobContainerConfigTypeDef",
        "Endpoints": List["EndpointInfoTypeDef"],
        "VpcConfig": "RecommendationJobVpcConfigTypeDef",
        "ModelName": str,
    },
    total=False,
)

RecommendationJobOutputConfigTypeDef = TypedDict(
    "RecommendationJobOutputConfigTypeDef",
    {
        "KmsKeyId": str,
        "CompiledOutputConfig": "RecommendationJobCompiledOutputConfigTypeDef",
    },
    total=False,
)

RecommendationJobPayloadConfigTypeDef = TypedDict(
    "RecommendationJobPayloadConfigTypeDef",
    {
        "SamplePayloadUrl": str,
        "SupportedContentTypes": List[str],
    },
    total=False,
)

RecommendationJobResourceLimitTypeDef = TypedDict(
    "RecommendationJobResourceLimitTypeDef",
    {
        "MaxNumberOfTests": int,
        "MaxParallelOfTests": int,
    },
    total=False,
)

RecommendationJobStoppingConditionsTypeDef = TypedDict(
    "RecommendationJobStoppingConditionsTypeDef",
    {
        "MaxInvocations": int,
        "ModelLatencyThresholds": List["ModelLatencyThresholdTypeDef"],
        "FlatInvocations": FlatInvocationsType,
    },
    total=False,
)

RecommendationJobVpcConfigTypeDef = TypedDict(
    "RecommendationJobVpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

_RequiredRecommendationMetricsTypeDef = TypedDict(
    "_RequiredRecommendationMetricsTypeDef",
    {
        "CostPerHour": float,
        "CostPerInference": float,
        "MaxInvocations": int,
        "ModelLatency": int,
    },
)
_OptionalRecommendationMetricsTypeDef = TypedDict(
    "_OptionalRecommendationMetricsTypeDef",
    {
        "CpuUtilization": float,
        "MemoryUtilization": float,
        "ModelSetupTime": int,
    },
    total=False,
)

class RecommendationMetricsTypeDef(
    _RequiredRecommendationMetricsTypeDef, _OptionalRecommendationMetricsTypeDef
):
    pass

_RequiredRedshiftDatasetDefinitionTypeDef = TypedDict(
    "_RequiredRedshiftDatasetDefinitionTypeDef",
    {
        "ClusterId": str,
        "Database": str,
        "DbUser": str,
        "QueryString": str,
        "ClusterRoleArn": str,
        "OutputS3Uri": str,
        "OutputFormat": RedshiftResultFormatType,
    },
)
_OptionalRedshiftDatasetDefinitionTypeDef = TypedDict(
    "_OptionalRedshiftDatasetDefinitionTypeDef",
    {
        "KmsKeyId": str,
        "OutputCompression": RedshiftResultCompressionTypeType,
    },
    total=False,
)

class RedshiftDatasetDefinitionTypeDef(
    _RequiredRedshiftDatasetDefinitionTypeDef, _OptionalRedshiftDatasetDefinitionTypeDef
):
    pass

_RequiredRegisterDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": List["DeviceTypeDef"],
    },
)
_OptionalRegisterDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterDevicesRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class RegisterDevicesRequestRequestTypeDef(
    _RequiredRegisterDevicesRequestRequestTypeDef, _OptionalRegisterDevicesRequestRequestTypeDef
):
    pass

RegisterModelStepMetadataTypeDef = TypedDict(
    "RegisterModelStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredRenderUiTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredRenderUiTemplateRequestRequestTypeDef",
    {
        "Task": "RenderableTaskTypeDef",
        "RoleArn": str,
    },
)
_OptionalRenderUiTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalRenderUiTemplateRequestRequestTypeDef",
    {
        "UiTemplate": "UiTemplateTypeDef",
        "HumanTaskUiArn": str,
    },
    total=False,
)

class RenderUiTemplateRequestRequestTypeDef(
    _RequiredRenderUiTemplateRequestRequestTypeDef, _OptionalRenderUiTemplateRequestRequestTypeDef
):
    pass

RenderUiTemplateResponseTypeDef = TypedDict(
    "RenderUiTemplateResponseTypeDef",
    {
        "RenderedContent": str,
        "Errors": List["RenderingErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenderableTaskTypeDef = TypedDict(
    "RenderableTaskTypeDef",
    {
        "Input": str,
    },
)

RenderingErrorTypeDef = TypedDict(
    "RenderingErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
)

RepositoryAuthConfigTypeDef = TypedDict(
    "RepositoryAuthConfigTypeDef",
    {
        "RepositoryCredentialsProviderArn": str,
    },
)

ResolvedAttributesTypeDef = TypedDict(
    "ResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": ProblemTypeType,
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
    },
    total=False,
)

ResourceCatalogTypeDef = TypedDict(
    "ResourceCatalogTypeDef",
    {
        "ResourceCatalogArn": str,
        "ResourceCatalogName": str,
        "Description": str,
        "CreationTime": datetime,
    },
)

ResourceConfigForUpdateTypeDef = TypedDict(
    "ResourceConfigForUpdateTypeDef",
    {
        "KeepAlivePeriodInSeconds": int,
    },
)

_RequiredResourceConfigTypeDef = TypedDict(
    "_RequiredResourceConfigTypeDef",
    {
        "VolumeSizeInGB": int,
    },
)
_OptionalResourceConfigTypeDef = TypedDict(
    "_OptionalResourceConfigTypeDef",
    {
        "InstanceType": TrainingInstanceTypeType,
        "InstanceCount": int,
        "VolumeKmsKeyId": str,
        "InstanceGroups": List["InstanceGroupTypeDef"],
        "KeepAlivePeriodInSeconds": int,
    },
    total=False,
)

class ResourceConfigTypeDef(_RequiredResourceConfigTypeDef, _OptionalResourceConfigTypeDef):
    pass

_RequiredResourceLimitsTypeDef = TypedDict(
    "_RequiredResourceLimitsTypeDef",
    {
        "MaxParallelTrainingJobs": int,
    },
)
_OptionalResourceLimitsTypeDef = TypedDict(
    "_OptionalResourceLimitsTypeDef",
    {
        "MaxNumberOfTrainingJobs": int,
        "MaxRuntimeInSeconds": int,
    },
    total=False,
)

class ResourceLimitsTypeDef(_RequiredResourceLimitsTypeDef, _OptionalResourceLimitsTypeDef):
    pass

ResourceSpecTypeDef = TypedDict(
    "ResourceSpecTypeDef",
    {
        "SageMakerImageArn": str,
        "SageMakerImageVersionArn": str,
        "InstanceType": AppInstanceTypeType,
        "LifecycleConfigArn": str,
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

RetentionPolicyTypeDef = TypedDict(
    "RetentionPolicyTypeDef",
    {
        "HomeEfsFileSystem": RetentionTypeType,
    },
    total=False,
)

_RequiredRetryPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredRetryPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
    },
)
_OptionalRetryPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalRetryPipelineExecutionRequestRequestTypeDef",
    {
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
    },
    total=False,
)

class RetryPipelineExecutionRequestRequestTypeDef(
    _RequiredRetryPipelineExecutionRequestRequestTypeDef,
    _OptionalRetryPipelineExecutionRequestRequestTypeDef,
):
    pass

RetryPipelineExecutionResponseTypeDef = TypedDict(
    "RetryPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetryStrategyTypeDef = TypedDict(
    "RetryStrategyTypeDef",
    {
        "MaximumRetryAttempts": int,
    },
)

_RequiredRollingUpdatePolicyTypeDef = TypedDict(
    "_RequiredRollingUpdatePolicyTypeDef",
    {
        "MaximumBatchSize": "CapacitySizeTypeDef",
        "WaitIntervalInSeconds": int,
    },
)
_OptionalRollingUpdatePolicyTypeDef = TypedDict(
    "_OptionalRollingUpdatePolicyTypeDef",
    {
        "MaximumExecutionTimeoutInSeconds": int,
        "RollbackMaximumBatchSize": "CapacitySizeTypeDef",
    },
    total=False,
)

class RollingUpdatePolicyTypeDef(
    _RequiredRollingUpdatePolicyTypeDef, _OptionalRollingUpdatePolicyTypeDef
):
    pass

_RequiredS3DataSourceTypeDef = TypedDict(
    "_RequiredS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)
_OptionalS3DataSourceTypeDef = TypedDict(
    "_OptionalS3DataSourceTypeDef",
    {
        "S3DataDistributionType": S3DataDistributionType,
        "AttributeNames": List[str],
        "InstanceGroupNames": List[str],
    },
    total=False,
)

class S3DataSourceTypeDef(_RequiredS3DataSourceTypeDef, _OptionalS3DataSourceTypeDef):
    pass

_RequiredS3ModelDataSourceTypeDef = TypedDict(
    "_RequiredS3ModelDataSourceTypeDef",
    {
        "S3Uri": str,
        "S3DataType": S3ModelDataTypeType,
        "CompressionType": ModelCompressionTypeType,
    },
)
_OptionalS3ModelDataSourceTypeDef = TypedDict(
    "_OptionalS3ModelDataSourceTypeDef",
    {
        "ModelAccessConfig": "ModelAccessConfigTypeDef",
    },
    total=False,
)

class S3ModelDataSourceTypeDef(
    _RequiredS3ModelDataSourceTypeDef, _OptionalS3ModelDataSourceTypeDef
):
    pass

_RequiredS3StorageConfigTypeDef = TypedDict(
    "_RequiredS3StorageConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalS3StorageConfigTypeDef = TypedDict(
    "_OptionalS3StorageConfigTypeDef",
    {
        "KmsKeyId": str,
        "ResolvedOutputS3Uri": str,
    },
    total=False,
)

class S3StorageConfigTypeDef(_RequiredS3StorageConfigTypeDef, _OptionalS3StorageConfigTypeDef):
    pass

ScalingPolicyMetricTypeDef = TypedDict(
    "ScalingPolicyMetricTypeDef",
    {
        "InvocationsPerInstance": int,
        "ModelLatency": int,
    },
    total=False,
)

ScalingPolicyObjectiveTypeDef = TypedDict(
    "ScalingPolicyObjectiveTypeDef",
    {
        "MinInvocationsPerMinute": int,
        "MaxInvocationsPerMinute": int,
    },
    total=False,
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "TargetTracking": "TargetTrackingScalingPolicyConfigurationTypeDef",
    },
    total=False,
)

_RequiredScheduleConfigTypeDef = TypedDict(
    "_RequiredScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
    },
)
_OptionalScheduleConfigTypeDef = TypedDict(
    "_OptionalScheduleConfigTypeDef",
    {
        "DataAnalysisStartTime": str,
        "DataAnalysisEndTime": str,
    },
    total=False,
)

class ScheduleConfigTypeDef(_RequiredScheduleConfigTypeDef, _OptionalScheduleConfigTypeDef):
    pass

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NestedFilters": List["NestedFiltersTypeDef"],
        "SubExpressions": List[Dict[str, Any]],
        "Operator": BooleanOperatorType,
    },
    total=False,
)

SearchRecordTypeDef = TypedDict(
    "SearchRecordTypeDef",
    {
        "TrainingJob": "TrainingJobTypeDef",
        "Experiment": "ExperimentTypeDef",
        "Trial": "TrialTypeDef",
        "TrialComponent": "TrialComponentTypeDef",
        "Endpoint": "EndpointTypeDef",
        "ModelPackage": "ModelPackageTypeDef",
        "ModelPackageGroup": "ModelPackageGroupTypeDef",
        "Pipeline": "PipelineTypeDef",
        "PipelineExecution": "PipelineExecutionTypeDef",
        "FeatureGroup": "FeatureGroupTypeDef",
        "Project": "ProjectTypeDef",
        "FeatureMetadata": "FeatureMetadataTypeDef",
        "HyperParameterTuningJob": "HyperParameterTuningJobSearchEntityTypeDef",
        "Model": "ModelDashboardModelTypeDef",
        "ModelCard": "ModelCardTypeDef",
    },
    total=False,
)

_RequiredSearchRequestRequestTypeDef = TypedDict(
    "_RequiredSearchRequestRequestTypeDef",
    {
        "Resource": ResourceTypeType,
    },
)
_OptionalSearchRequestRequestTypeDef = TypedDict(
    "_OptionalSearchRequestRequestTypeDef",
    {
        "SearchExpression": "SearchExpressionTypeDef",
        "SortBy": str,
        "SortOrder": SearchSortOrderType,
        "NextToken": str,
        "MaxResults": int,
        "CrossAccountFilterOption": CrossAccountFilterOptionType,
    },
    total=False,
)

class SearchRequestRequestTypeDef(
    _RequiredSearchRequestRequestTypeDef, _OptionalSearchRequestRequestTypeDef
):
    pass

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "Results": List["SearchRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSecondaryStatusTransitionTypeDef = TypedDict(
    "_RequiredSecondaryStatusTransitionTypeDef",
    {
        "Status": SecondaryStatusType,
        "StartTime": datetime,
    },
)
_OptionalSecondaryStatusTransitionTypeDef = TypedDict(
    "_OptionalSecondaryStatusTransitionTypeDef",
    {
        "EndTime": datetime,
        "StatusMessage": str,
    },
    total=False,
)

class SecondaryStatusTransitionTypeDef(
    _RequiredSecondaryStatusTransitionTypeDef, _OptionalSecondaryStatusTransitionTypeDef
):
    pass

SelectedStepTypeDef = TypedDict(
    "SelectedStepTypeDef",
    {
        "StepName": str,
    },
)

_RequiredSelectiveExecutionConfigTypeDef = TypedDict(
    "_RequiredSelectiveExecutionConfigTypeDef",
    {
        "SelectedSteps": List["SelectedStepTypeDef"],
    },
)
_OptionalSelectiveExecutionConfigTypeDef = TypedDict(
    "_OptionalSelectiveExecutionConfigTypeDef",
    {
        "SourcePipelineExecutionArn": str,
    },
    total=False,
)

class SelectiveExecutionConfigTypeDef(
    _RequiredSelectiveExecutionConfigTypeDef, _OptionalSelectiveExecutionConfigTypeDef
):
    pass

SelectiveExecutionResultTypeDef = TypedDict(
    "SelectiveExecutionResultTypeDef",
    {
        "SourcePipelineExecutionArn": str,
    },
    total=False,
)

_RequiredSendPipelineExecutionStepFailureRequestRequestTypeDef = TypedDict(
    "_RequiredSendPipelineExecutionStepFailureRequestRequestTypeDef",
    {
        "CallbackToken": str,
    },
)
_OptionalSendPipelineExecutionStepFailureRequestRequestTypeDef = TypedDict(
    "_OptionalSendPipelineExecutionStepFailureRequestRequestTypeDef",
    {
        "FailureReason": str,
        "ClientRequestToken": str,
    },
    total=False,
)

class SendPipelineExecutionStepFailureRequestRequestTypeDef(
    _RequiredSendPipelineExecutionStepFailureRequestRequestTypeDef,
    _OptionalSendPipelineExecutionStepFailureRequestRequestTypeDef,
):
    pass

SendPipelineExecutionStepFailureResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepFailureResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendPipelineExecutionStepSuccessRequestRequestTypeDef = TypedDict(
    "_RequiredSendPipelineExecutionStepSuccessRequestRequestTypeDef",
    {
        "CallbackToken": str,
    },
)
_OptionalSendPipelineExecutionStepSuccessRequestRequestTypeDef = TypedDict(
    "_OptionalSendPipelineExecutionStepSuccessRequestRequestTypeDef",
    {
        "OutputParameters": List["OutputParameterTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class SendPipelineExecutionStepSuccessRequestRequestTypeDef(
    _RequiredSendPipelineExecutionStepSuccessRequestRequestTypeDef,
    _OptionalSendPipelineExecutionStepSuccessRequestRequestTypeDef,
):
    pass

SendPipelineExecutionStepSuccessResponseTypeDef = TypedDict(
    "SendPipelineExecutionStepSuccessResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceCatalogProvisionedProductDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductStatusMessage": str,
    },
    total=False,
)

_RequiredServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "_RequiredServiceCatalogProvisioningDetailsTypeDef",
    {
        "ProductId": str,
    },
)
_OptionalServiceCatalogProvisioningDetailsTypeDef = TypedDict(
    "_OptionalServiceCatalogProvisioningDetailsTypeDef",
    {
        "ProvisioningArtifactId": str,
        "PathId": str,
        "ProvisioningParameters": List["ProvisioningParameterTypeDef"],
    },
    total=False,
)

class ServiceCatalogProvisioningDetailsTypeDef(
    _RequiredServiceCatalogProvisioningDetailsTypeDef,
    _OptionalServiceCatalogProvisioningDetailsTypeDef,
):
    pass

ServiceCatalogProvisioningUpdateDetailsTypeDef = TypedDict(
    "ServiceCatalogProvisioningUpdateDetailsTypeDef",
    {
        "ProvisioningArtifactId": str,
        "ProvisioningParameters": List["ProvisioningParameterTypeDef"],
    },
    total=False,
)

ShadowModeConfigTypeDef = TypedDict(
    "ShadowModeConfigTypeDef",
    {
        "SourceModelVariantName": str,
        "ShadowModelVariants": List["ShadowModelVariantConfigTypeDef"],
    },
)

ShadowModelVariantConfigTypeDef = TypedDict(
    "ShadowModelVariantConfigTypeDef",
    {
        "ShadowModelVariantName": str,
        "SamplingPercentage": int,
    },
)

SharingSettingsTypeDef = TypedDict(
    "SharingSettingsTypeDef",
    {
        "NotebookOutputOption": NotebookOutputOptionType,
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ShuffleConfigTypeDef = TypedDict(
    "ShuffleConfigTypeDef",
    {
        "Seed": int,
    },
)

SourceAlgorithmSpecificationTypeDef = TypedDict(
    "SourceAlgorithmSpecificationTypeDef",
    {
        "SourceAlgorithms": List["SourceAlgorithmTypeDef"],
    },
)

_RequiredSourceAlgorithmTypeDef = TypedDict(
    "_RequiredSourceAlgorithmTypeDef",
    {
        "AlgorithmName": str,
    },
)
_OptionalSourceAlgorithmTypeDef = TypedDict(
    "_OptionalSourceAlgorithmTypeDef",
    {
        "ModelDataUrl": str,
    },
    total=False,
)

class SourceAlgorithmTypeDef(_RequiredSourceAlgorithmTypeDef, _OptionalSourceAlgorithmTypeDef):
    pass

SourceIpConfigTypeDef = TypedDict(
    "SourceIpConfigTypeDef",
    {
        "Cidrs": List[str],
    },
)

SpaceDetailsTypeDef = TypedDict(
    "SpaceDetailsTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
        "Status": SpaceStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

SpaceSettingsTypeDef = TypedDict(
    "SpaceSettingsTypeDef",
    {
        "JupyterServerAppSettings": "JupyterServerAppSettingsTypeDef",
        "KernelGatewayAppSettings": "KernelGatewayAppSettingsTypeDef",
    },
    total=False,
)

StairsTypeDef = TypedDict(
    "StairsTypeDef",
    {
        "DurationInSeconds": int,
        "NumberOfSteps": int,
        "UsersPerStep": int,
    },
    total=False,
)

StartEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "StartEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)

StartInferenceExperimentRequestRequestTypeDef = TypedDict(
    "StartInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartInferenceExperimentResponseTypeDef = TypedDict(
    "StartInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "StartMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StartNotebookInstanceInputRequestTypeDef = TypedDict(
    "StartNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

_RequiredStartPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineName": str,
        "ClientRequestToken": str,
    },
)
_OptionalStartPipelineExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionDisplayName": str,
        "PipelineParameters": List["ParameterTypeDef"],
        "PipelineExecutionDescription": str,
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
        "SelectiveExecutionConfig": "SelectiveExecutionConfigTypeDef",
    },
    total=False,
)

class StartPipelineExecutionRequestRequestTypeDef(
    _RequiredStartPipelineExecutionRequestRequestTypeDef,
    _OptionalStartPipelineExecutionRequestRequestTypeDef,
):
    pass

StartPipelineExecutionResponseTypeDef = TypedDict(
    "StartPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAutoMLJobRequestRequestTypeDef = TypedDict(
    "StopAutoMLJobRequestRequestTypeDef",
    {
        "AutoMLJobName": str,
    },
)

StopCompilationJobRequestRequestTypeDef = TypedDict(
    "StopCompilationJobRequestRequestTypeDef",
    {
        "CompilationJobName": str,
    },
)

StopEdgeDeploymentStageRequestRequestTypeDef = TypedDict(
    "StopEdgeDeploymentStageRequestRequestTypeDef",
    {
        "EdgeDeploymentPlanName": str,
        "StageName": str,
    },
)

StopEdgePackagingJobRequestRequestTypeDef = TypedDict(
    "StopEdgePackagingJobRequestRequestTypeDef",
    {
        "EdgePackagingJobName": str,
    },
)

StopHyperParameterTuningJobRequestRequestTypeDef = TypedDict(
    "StopHyperParameterTuningJobRequestRequestTypeDef",
    {
        "HyperParameterTuningJobName": str,
    },
)

_RequiredStopInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredStopInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
        "ModelVariantActions": Dict[str, ModelVariantActionType],
    },
)
_OptionalStopInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalStopInferenceExperimentRequestRequestTypeDef",
    {
        "DesiredModelVariants": List["ModelVariantConfigTypeDef"],
        "DesiredState": InferenceExperimentStopDesiredStateType,
        "Reason": str,
    },
    total=False,
)

class StopInferenceExperimentRequestRequestTypeDef(
    _RequiredStopInferenceExperimentRequestRequestTypeDef,
    _OptionalStopInferenceExperimentRequestRequestTypeDef,
):
    pass

StopInferenceExperimentResponseTypeDef = TypedDict(
    "StopInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopInferenceRecommendationsJobRequestRequestTypeDef = TypedDict(
    "StopInferenceRecommendationsJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

StopLabelingJobRequestRequestTypeDef = TypedDict(
    "StopLabelingJobRequestRequestTypeDef",
    {
        "LabelingJobName": str,
    },
)

StopMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "StopMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
    },
)

StopNotebookInstanceInputRequestTypeDef = TypedDict(
    "StopNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)

StopPipelineExecutionRequestRequestTypeDef = TypedDict(
    "StopPipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
        "ClientRequestToken": str,
    },
)

StopPipelineExecutionResponseTypeDef = TypedDict(
    "StopPipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProcessingJobRequestRequestTypeDef = TypedDict(
    "StopProcessingJobRequestRequestTypeDef",
    {
        "ProcessingJobName": str,
    },
)

StopTrainingJobRequestRequestTypeDef = TypedDict(
    "StopTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)

StopTransformJobRequestRequestTypeDef = TypedDict(
    "StopTransformJobRequestRequestTypeDef",
    {
        "TransformJobName": str,
    },
)

StoppingConditionTypeDef = TypedDict(
    "StoppingConditionTypeDef",
    {
        "MaxRuntimeInSeconds": int,
        "MaxWaitTimeInSeconds": int,
        "MaxPendingTimeInSeconds": int,
    },
    total=False,
)

StudioLifecycleConfigDetailsTypeDef = TypedDict(
    "StudioLifecycleConfigDetailsTypeDef",
    {
        "StudioLifecycleConfigArn": str,
        "StudioLifecycleConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "StudioLifecycleConfigAppType": StudioLifecycleConfigAppTypeType,
    },
    total=False,
)

_RequiredSubscribedWorkteamTypeDef = TypedDict(
    "_RequiredSubscribedWorkteamTypeDef",
    {
        "WorkteamArn": str,
    },
)
_OptionalSubscribedWorkteamTypeDef = TypedDict(
    "_OptionalSubscribedWorkteamTypeDef",
    {
        "MarketplaceTitle": str,
        "SellerName": str,
        "MarketplaceDescription": str,
        "ListingId": str,
    },
    total=False,
)

class SubscribedWorkteamTypeDef(
    _RequiredSubscribedWorkteamTypeDef, _OptionalSubscribedWorkteamTypeDef
):
    pass

SuggestionQueryTypeDef = TypedDict(
    "SuggestionQueryTypeDef",
    {
        "PropertyNameQuery": "PropertyNameQueryTypeDef",
    },
    total=False,
)

_RequiredTabularJobConfigTypeDef = TypedDict(
    "_RequiredTabularJobConfigTypeDef",
    {
        "TargetAttributeName": str,
    },
)
_OptionalTabularJobConfigTypeDef = TypedDict(
    "_OptionalTabularJobConfigTypeDef",
    {
        "CandidateGenerationConfig": "CandidateGenerationConfigTypeDef",
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
        "FeatureSpecificationS3Uri": str,
        "Mode": AutoMLModeType,
        "GenerateCandidateDefinitionsOnly": bool,
        "ProblemType": ProblemTypeType,
        "SampleWeightAttributeName": str,
    },
    total=False,
)

class TabularJobConfigTypeDef(_RequiredTabularJobConfigTypeDef, _OptionalTabularJobConfigTypeDef):
    pass

TabularResolvedAttributesTypeDef = TypedDict(
    "TabularResolvedAttributesTypeDef",
    {
        "ProblemType": ProblemTypeType,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

_RequiredTargetPlatformTypeDef = TypedDict(
    "_RequiredTargetPlatformTypeDef",
    {
        "Os": TargetPlatformOsType,
        "Arch": TargetPlatformArchType,
    },
)
_OptionalTargetPlatformTypeDef = TypedDict(
    "_OptionalTargetPlatformTypeDef",
    {
        "Accelerator": TargetPlatformAcceleratorType,
    },
    total=False,
)

class TargetPlatformTypeDef(_RequiredTargetPlatformTypeDef, _OptionalTargetPlatformTypeDef):
    pass

TargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "MetricSpecification": "MetricSpecificationTypeDef",
        "TargetValue": float,
    },
    total=False,
)

TensorBoardAppSettingsTypeDef = TypedDict(
    "TensorBoardAppSettingsTypeDef",
    {
        "DefaultResourceSpec": "ResourceSpecTypeDef",
    },
    total=False,
)

_RequiredTensorBoardOutputConfigTypeDef = TypedDict(
    "_RequiredTensorBoardOutputConfigTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTensorBoardOutputConfigTypeDef = TypedDict(
    "_OptionalTensorBoardOutputConfigTypeDef",
    {
        "LocalPath": str,
    },
    total=False,
)

class TensorBoardOutputConfigTypeDef(
    _RequiredTensorBoardOutputConfigTypeDef, _OptionalTensorBoardOutputConfigTypeDef
):
    pass

_RequiredTextClassificationJobConfigTypeDef = TypedDict(
    "_RequiredTextClassificationJobConfigTypeDef",
    {
        "ContentColumn": str,
        "TargetLabelColumn": str,
    },
)
_OptionalTextClassificationJobConfigTypeDef = TypedDict(
    "_OptionalTextClassificationJobConfigTypeDef",
    {
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
    },
    total=False,
)

class TextClassificationJobConfigTypeDef(
    _RequiredTextClassificationJobConfigTypeDef, _OptionalTextClassificationJobConfigTypeDef
):
    pass

TextGenerationJobConfigTypeDef = TypedDict(
    "TextGenerationJobConfigTypeDef",
    {
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
        "BaseModelName": str,
    },
    total=False,
)

TextGenerationResolvedAttributesTypeDef = TypedDict(
    "TextGenerationResolvedAttributesTypeDef",
    {
        "BaseModelName": str,
    },
    total=False,
)

_RequiredTimeSeriesConfigTypeDef = TypedDict(
    "_RequiredTimeSeriesConfigTypeDef",
    {
        "TargetAttributeName": str,
        "TimestampAttributeName": str,
        "ItemIdentifierAttributeName": str,
    },
)
_OptionalTimeSeriesConfigTypeDef = TypedDict(
    "_OptionalTimeSeriesConfigTypeDef",
    {
        "GroupingAttributeNames": List[str],
    },
    total=False,
)

class TimeSeriesConfigTypeDef(_RequiredTimeSeriesConfigTypeDef, _OptionalTimeSeriesConfigTypeDef):
    pass

_RequiredTimeSeriesForecastingJobConfigTypeDef = TypedDict(
    "_RequiredTimeSeriesForecastingJobConfigTypeDef",
    {
        "ForecastFrequency": str,
        "ForecastHorizon": int,
        "TimeSeriesConfig": "TimeSeriesConfigTypeDef",
    },
)
_OptionalTimeSeriesForecastingJobConfigTypeDef = TypedDict(
    "_OptionalTimeSeriesForecastingJobConfigTypeDef",
    {
        "FeatureSpecificationS3Uri": str,
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
        "ForecastQuantiles": List[str],
        "Transformations": "TimeSeriesTransformationsTypeDef",
        "HolidayConfig": List["HolidayConfigAttributesTypeDef"],
    },
    total=False,
)

class TimeSeriesForecastingJobConfigTypeDef(
    _RequiredTimeSeriesForecastingJobConfigTypeDef, _OptionalTimeSeriesForecastingJobConfigTypeDef
):
    pass

TimeSeriesForecastingSettingsTypeDef = TypedDict(
    "TimeSeriesForecastingSettingsTypeDef",
    {
        "Status": FeatureStatusType,
        "AmazonForecastRoleArn": str,
    },
    total=False,
)

TimeSeriesTransformationsTypeDef = TypedDict(
    "TimeSeriesTransformationsTypeDef",
    {
        "Filling": Dict[str, Dict[FillingTypeType, str]],
        "Aggregation": Dict[str, AggregationTransformationValueType],
    },
    total=False,
)

TrafficPatternTypeDef = TypedDict(
    "TrafficPatternTypeDef",
    {
        "TrafficType": TrafficTypeType,
        "Phases": List["PhaseTypeDef"],
        "Stairs": "StairsTypeDef",
    },
    total=False,
)

_RequiredTrafficRoutingConfigTypeDef = TypedDict(
    "_RequiredTrafficRoutingConfigTypeDef",
    {
        "Type": TrafficRoutingConfigTypeType,
        "WaitIntervalInSeconds": int,
    },
)
_OptionalTrafficRoutingConfigTypeDef = TypedDict(
    "_OptionalTrafficRoutingConfigTypeDef",
    {
        "CanarySize": "CapacitySizeTypeDef",
        "LinearStepSize": "CapacitySizeTypeDef",
    },
    total=False,
)

class TrafficRoutingConfigTypeDef(
    _RequiredTrafficRoutingConfigTypeDef, _OptionalTrafficRoutingConfigTypeDef
):
    pass

_RequiredTrainingImageConfigTypeDef = TypedDict(
    "_RequiredTrainingImageConfigTypeDef",
    {
        "TrainingRepositoryAccessMode": TrainingRepositoryAccessModeType,
    },
)
_OptionalTrainingImageConfigTypeDef = TypedDict(
    "_OptionalTrainingImageConfigTypeDef",
    {
        "TrainingRepositoryAuthConfig": "TrainingRepositoryAuthConfigTypeDef",
    },
    total=False,
)

class TrainingImageConfigTypeDef(
    _RequiredTrainingImageConfigTypeDef, _OptionalTrainingImageConfigTypeDef
):
    pass

_RequiredTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": TrainingInputModeType,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalTrainingJobDefinitionTypeDef",
    {
        "HyperParameters": Dict[str, str],
    },
    total=False,
)

class TrainingJobDefinitionTypeDef(
    _RequiredTrainingJobDefinitionTypeDef, _OptionalTrainingJobDefinitionTypeDef
):
    pass

TrainingJobStatusCountersTypeDef = TypedDict(
    "TrainingJobStatusCountersTypeDef",
    {
        "Completed": int,
        "InProgress": int,
        "RetryableError": int,
        "NonRetryableError": int,
        "Stopped": int,
    },
    total=False,
)

TrainingJobStepMetadataTypeDef = TypedDict(
    "TrainingJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": TrainingJobStatusType,
    },
)
_OptionalTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalTrainingJobSummaryTypeDef",
    {
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "WarmPoolStatus": "WarmPoolStatusTypeDef",
    },
    total=False,
)

class TrainingJobSummaryTypeDef(
    _RequiredTrainingJobSummaryTypeDef, _OptionalTrainingJobSummaryTypeDef
):
    pass

TrainingJobTypeDef = TypedDict(
    "TrainingJobTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "TrainingJobStatus": TrainingJobStatusType,
        "SecondaryStatus": SecondaryStatusType,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "RoleArn": str,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "LastModifiedTime": datetime,
        "SecondaryStatusTransitions": List["SecondaryStatusTransitionTypeDef"],
        "FinalMetricDataList": List["MetricDataTypeDef"],
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
        "TrainingTimeInSeconds": int,
        "BillableTimeInSeconds": int,
        "DebugHookConfig": "DebugHookConfigTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "DebugRuleConfigurations": List["DebugRuleConfigurationTypeDef"],
        "TensorBoardOutputConfig": "TensorBoardOutputConfigTypeDef",
        "DebugRuleEvaluationStatuses": List["DebugRuleEvaluationStatusTypeDef"],
        "ProfilerConfig": "ProfilerConfigTypeDef",
        "Environment": Dict[str, str],
        "RetryStrategy": "RetryStrategyTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrainingRepositoryAuthConfigTypeDef = TypedDict(
    "TrainingRepositoryAuthConfigTypeDef",
    {
        "TrainingRepositoryCredentialsProviderArn": str,
    },
)

_RequiredTrainingSpecificationTypeDef = TypedDict(
    "_RequiredTrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "SupportedTrainingInstanceTypes": List[TrainingInstanceTypeType],
        "TrainingChannels": List["ChannelSpecificationTypeDef"],
    },
)
_OptionalTrainingSpecificationTypeDef = TypedDict(
    "_OptionalTrainingSpecificationTypeDef",
    {
        "TrainingImageDigest": str,
        "SupportedHyperParameters": List["HyperParameterSpecificationTypeDef"],
        "SupportsDistributedTraining": bool,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "SupportedTuningJobObjectiveMetrics": List["HyperParameterTuningJobObjectiveTypeDef"],
        "AdditionalS3DataSource": "AdditionalS3DataSourceTypeDef",
    },
    total=False,
)

class TrainingSpecificationTypeDef(
    _RequiredTrainingSpecificationTypeDef, _OptionalTrainingSpecificationTypeDef
):
    pass

TransformDataSourceTypeDef = TypedDict(
    "TransformDataSourceTypeDef",
    {
        "S3DataSource": "TransformS3DataSourceTypeDef",
    },
)

_RequiredTransformInputTypeDef = TypedDict(
    "_RequiredTransformInputTypeDef",
    {
        "DataSource": "TransformDataSourceTypeDef",
    },
)
_OptionalTransformInputTypeDef = TypedDict(
    "_OptionalTransformInputTypeDef",
    {
        "ContentType": str,
        "CompressionType": CompressionTypeType,
        "SplitType": SplitTypeType,
    },
    total=False,
)

class TransformInputTypeDef(_RequiredTransformInputTypeDef, _OptionalTransformInputTypeDef):
    pass

_RequiredTransformJobDefinitionTypeDef = TypedDict(
    "_RequiredTransformJobDefinitionTypeDef",
    {
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
    },
)
_OptionalTransformJobDefinitionTypeDef = TypedDict(
    "_OptionalTransformJobDefinitionTypeDef",
    {
        "MaxConcurrentTransforms": int,
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
    },
    total=False,
)

class TransformJobDefinitionTypeDef(
    _RequiredTransformJobDefinitionTypeDef, _OptionalTransformJobDefinitionTypeDef
):
    pass

TransformJobStepMetadataTypeDef = TypedDict(
    "TransformJobStepMetadataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredTransformJobSummaryTypeDef = TypedDict(
    "_RequiredTransformJobSummaryTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformJobStatus": TransformJobStatusType,
    },
)
_OptionalTransformJobSummaryTypeDef = TypedDict(
    "_OptionalTransformJobSummaryTypeDef",
    {
        "TransformEndTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

class TransformJobSummaryTypeDef(
    _RequiredTransformJobSummaryTypeDef, _OptionalTransformJobSummaryTypeDef
):
    pass

TransformJobTypeDef = TypedDict(
    "TransformJobTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": TransformJobStatusType,
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": BatchStrategyType,
        "Environment": Dict[str, str],
        "TransformInput": "TransformInputTypeDef",
        "TransformOutput": "TransformOutputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "CreationTime": datetime,
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": "DataProcessingTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "DataCaptureConfig": "BatchDataCaptureConfigTypeDef",
    },
    total=False,
)

_RequiredTransformOutputTypeDef = TypedDict(
    "_RequiredTransformOutputTypeDef",
    {
        "S3OutputPath": str,
    },
)
_OptionalTransformOutputTypeDef = TypedDict(
    "_OptionalTransformOutputTypeDef",
    {
        "Accept": str,
        "AssembleWith": AssemblyTypeType,
        "KmsKeyId": str,
    },
    total=False,
)

class TransformOutputTypeDef(_RequiredTransformOutputTypeDef, _OptionalTransformOutputTypeDef):
    pass

_RequiredTransformResourcesTypeDef = TypedDict(
    "_RequiredTransformResourcesTypeDef",
    {
        "InstanceType": TransformInstanceTypeType,
        "InstanceCount": int,
    },
)
_OptionalTransformResourcesTypeDef = TypedDict(
    "_OptionalTransformResourcesTypeDef",
    {
        "VolumeKmsKeyId": str,
    },
    total=False,
)

class TransformResourcesTypeDef(
    _RequiredTransformResourcesTypeDef, _OptionalTransformResourcesTypeDef
):
    pass

TransformS3DataSourceTypeDef = TypedDict(
    "TransformS3DataSourceTypeDef",
    {
        "S3DataType": S3DataTypeType,
        "S3Uri": str,
    },
)

_RequiredTrialComponentArtifactTypeDef = TypedDict(
    "_RequiredTrialComponentArtifactTypeDef",
    {
        "Value": str,
    },
)
_OptionalTrialComponentArtifactTypeDef = TypedDict(
    "_OptionalTrialComponentArtifactTypeDef",
    {
        "MediaType": str,
    },
    total=False,
)

class TrialComponentArtifactTypeDef(
    _RequiredTrialComponentArtifactTypeDef, _OptionalTrialComponentArtifactTypeDef
):
    pass

TrialComponentMetricSummaryTypeDef = TypedDict(
    "TrialComponentMetricSummaryTypeDef",
    {
        "MetricName": str,
        "SourceArn": str,
        "TimeStamp": datetime,
        "Max": float,
        "Min": float,
        "Last": float,
        "Count": int,
        "Avg": float,
        "StdDev": float,
    },
    total=False,
)

TrialComponentParameterValueTypeDef = TypedDict(
    "TrialComponentParameterValueTypeDef",
    {
        "StringValue": str,
        "NumberValue": float,
    },
    total=False,
)

TrialComponentSimpleSummaryTypeDef = TypedDict(
    "TrialComponentSimpleSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "TrialComponentSource": "TrialComponentSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
    },
    total=False,
)

TrialComponentSourceDetailTypeDef = TypedDict(
    "TrialComponentSourceDetailTypeDef",
    {
        "SourceArn": str,
        "TrainingJob": "TrainingJobTypeDef",
        "ProcessingJob": "ProcessingJobTypeDef",
        "TransformJob": "TransformJobTypeDef",
    },
    total=False,
)

_RequiredTrialComponentSourceTypeDef = TypedDict(
    "_RequiredTrialComponentSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalTrialComponentSourceTypeDef = TypedDict(
    "_OptionalTrialComponentSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)

class TrialComponentSourceTypeDef(
    _RequiredTrialComponentSourceTypeDef, _OptionalTrialComponentSourceTypeDef
):
    pass

TrialComponentStatusTypeDef = TypedDict(
    "TrialComponentStatusTypeDef",
    {
        "PrimaryStatus": TrialComponentPrimaryStatusType,
        "Message": str,
    },
    total=False,
)

TrialComponentSummaryTypeDef = TypedDict(
    "TrialComponentSummaryTypeDef",
    {
        "TrialComponentName": str,
        "TrialComponentArn": str,
        "DisplayName": str,
        "TrialComponentSource": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
    },
    total=False,
)

TrialComponentTypeDef = TypedDict(
    "TrialComponentTypeDef",
    {
        "TrialComponentName": str,
        "DisplayName": str,
        "TrialComponentArn": str,
        "Source": "TrialComponentSourceTypeDef",
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": datetime,
        "EndTime": datetime,
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "Metrics": List["TrialComponentMetricSummaryTypeDef"],
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "SourceDetail": "TrialComponentSourceDetailTypeDef",
        "LineageGroupArn": str,
        "Tags": List["TagTypeDef"],
        "Parents": List["ParentTypeDef"],
        "RunName": str,
    },
    total=False,
)

_RequiredTrialSourceTypeDef = TypedDict(
    "_RequiredTrialSourceTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalTrialSourceTypeDef = TypedDict(
    "_OptionalTrialSourceTypeDef",
    {
        "SourceType": str,
    },
    total=False,
)

class TrialSourceTypeDef(_RequiredTrialSourceTypeDef, _OptionalTrialSourceTypeDef):
    pass

TrialSummaryTypeDef = TypedDict(
    "TrialSummaryTypeDef",
    {
        "TrialArn": str,
        "TrialName": str,
        "DisplayName": str,
        "TrialSource": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

TrialTypeDef = TypedDict(
    "TrialTypeDef",
    {
        "TrialName": str,
        "TrialArn": str,
        "DisplayName": str,
        "ExperimentName": str,
        "Source": "TrialSourceTypeDef",
        "CreationTime": datetime,
        "CreatedBy": "UserContextTypeDef",
        "LastModifiedTime": datetime,
        "LastModifiedBy": "UserContextTypeDef",
        "MetadataProperties": "MetadataPropertiesTypeDef",
        "Tags": List["TagTypeDef"],
        "TrialComponentSummaries": List["TrialComponentSimpleSummaryTypeDef"],
    },
    total=False,
)

TtlDurationTypeDef = TypedDict(
    "TtlDurationTypeDef",
    {
        "Unit": TtlDurationUnitType,
        "Value": int,
    },
    total=False,
)

TuningJobCompletionCriteriaTypeDef = TypedDict(
    "TuningJobCompletionCriteriaTypeDef",
    {
        "TargetObjectiveMetricValue": float,
        "BestObjectiveNotImproving": "BestObjectiveNotImprovingTypeDef",
        "ConvergenceDetected": "ConvergenceDetectedTypeDef",
    },
    total=False,
)

TuningJobStepMetaDataTypeDef = TypedDict(
    "TuningJobStepMetaDataTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

USDTypeDef = TypedDict(
    "USDTypeDef",
    {
        "Dollars": int,
        "Cents": int,
        "TenthFractionsOfACent": int,
    },
    total=False,
)

UiConfigTypeDef = TypedDict(
    "UiConfigTypeDef",
    {
        "UiTemplateS3Uri": str,
        "HumanTaskUiArn": str,
    },
    total=False,
)

UiTemplateInfoTypeDef = TypedDict(
    "UiTemplateInfoTypeDef",
    {
        "Url": str,
        "ContentSha256": str,
    },
    total=False,
)

UiTemplateTypeDef = TypedDict(
    "UiTemplateTypeDef",
    {
        "Content": str,
    },
)

_RequiredUpdateActionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateActionRequestRequestTypeDef",
    {
        "ActionName": str,
    },
)
_OptionalUpdateActionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateActionRequestRequestTypeDef",
    {
        "Description": str,
        "Status": ActionStatusType,
        "Properties": Dict[str, str],
        "PropertiesToRemove": List[str],
    },
    total=False,
)

class UpdateActionRequestRequestTypeDef(
    _RequiredUpdateActionRequestRequestTypeDef, _OptionalUpdateActionRequestRequestTypeDef
):
    pass

UpdateActionResponseTypeDef = TypedDict(
    "UpdateActionResponseTypeDef",
    {
        "ActionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppImageConfigRequestRequestTypeDef",
    {
        "AppImageConfigName": str,
    },
)
_OptionalUpdateAppImageConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppImageConfigRequestRequestTypeDef",
    {
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)

class UpdateAppImageConfigRequestRequestTypeDef(
    _RequiredUpdateAppImageConfigRequestRequestTypeDef,
    _OptionalUpdateAppImageConfigRequestRequestTypeDef,
):
    pass

UpdateAppImageConfigResponseTypeDef = TypedDict(
    "UpdateAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateArtifactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArtifactRequestRequestTypeDef",
    {
        "ArtifactArn": str,
    },
)
_OptionalUpdateArtifactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArtifactRequestRequestTypeDef",
    {
        "ArtifactName": str,
        "Properties": Dict[str, str],
        "PropertiesToRemove": List[str],
    },
    total=False,
)

class UpdateArtifactRequestRequestTypeDef(
    _RequiredUpdateArtifactRequestRequestTypeDef, _OptionalUpdateArtifactRequestRequestTypeDef
):
    pass

UpdateArtifactResponseTypeDef = TypedDict(
    "UpdateArtifactResponseTypeDef",
    {
        "ArtifactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredUpdateCodeRepositoryInputRequestTypeDef",
    {
        "CodeRepositoryName": str,
    },
)
_OptionalUpdateCodeRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalUpdateCodeRepositoryInputRequestTypeDef",
    {
        "GitConfig": "GitConfigForUpdateTypeDef",
    },
    total=False,
)

class UpdateCodeRepositoryInputRequestTypeDef(
    _RequiredUpdateCodeRepositoryInputRequestTypeDef,
    _OptionalUpdateCodeRepositoryInputRequestTypeDef,
):
    pass

UpdateCodeRepositoryOutputTypeDef = TypedDict(
    "UpdateCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContextRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContextRequestRequestTypeDef",
    {
        "ContextName": str,
    },
)
_OptionalUpdateContextRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContextRequestRequestTypeDef",
    {
        "Description": str,
        "Properties": Dict[str, str],
        "PropertiesToRemove": List[str],
    },
    total=False,
)

class UpdateContextRequestRequestTypeDef(
    _RequiredUpdateContextRequestRequestTypeDef, _OptionalUpdateContextRequestRequestTypeDef
):
    pass

UpdateContextResponseTypeDef = TypedDict(
    "UpdateContextResponseTypeDef",
    {
        "ContextArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceFleetRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "OutputConfig": "EdgeOutputConfigTypeDef",
    },
)
_OptionalUpdateDeviceFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceFleetRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Description": str,
        "EnableIotRoleAlias": bool,
    },
    total=False,
)

class UpdateDeviceFleetRequestRequestTypeDef(
    _RequiredUpdateDeviceFleetRequestRequestTypeDef, _OptionalUpdateDeviceFleetRequestRequestTypeDef
):
    pass

UpdateDevicesRequestRequestTypeDef = TypedDict(
    "UpdateDevicesRequestRequestTypeDef",
    {
        "DeviceFleetName": str,
        "Devices": List["DeviceTypeDef"],
    },
)

_RequiredUpdateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
_OptionalUpdateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDomainRequestRequestTypeDef",
    {
        "DefaultUserSettings": "UserSettingsTypeDef",
        "DomainSettingsForUpdate": "DomainSettingsForUpdateTypeDef",
        "DefaultSpaceSettings": "DefaultSpaceSettingsTypeDef",
        "AppSecurityGroupManagement": AppSecurityGroupManagementType,
    },
    total=False,
)

class UpdateDomainRequestRequestTypeDef(
    _RequiredUpdateDomainRequestRequestTypeDef, _OptionalUpdateDomainRequestRequestTypeDef
):
    pass

UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEndpointInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "EndpointConfigName": str,
    },
)
_OptionalUpdateEndpointInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointInputRequestTypeDef",
    {
        "RetainAllVariantProperties": bool,
        "ExcludeRetainedVariantProperties": List["VariantPropertyTypeDef"],
        "DeploymentConfig": "DeploymentConfigTypeDef",
        "RetainDeploymentConfig": bool,
    },
    total=False,
)

class UpdateEndpointInputRequestTypeDef(
    _RequiredUpdateEndpointInputRequestTypeDef, _OptionalUpdateEndpointInputRequestTypeDef
):
    pass

UpdateEndpointOutputTypeDef = TypedDict(
    "UpdateEndpointOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesInputRequestTypeDef",
    {
        "EndpointName": str,
        "DesiredWeightsAndCapacities": List["DesiredWeightAndCapacityTypeDef"],
    },
)

UpdateEndpointWeightsAndCapacitiesOutputTypeDef = TypedDict(
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentRequestRequestTypeDef",
    {
        "ExperimentName": str,
    },
)
_OptionalUpdateExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
    },
    total=False,
)

class UpdateExperimentRequestRequestTypeDef(
    _RequiredUpdateExperimentRequestRequestTypeDef, _OptionalUpdateExperimentRequestRequestTypeDef
):
    pass

UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "ExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
    },
)
_OptionalUpdateFeatureGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeatureGroupRequestRequestTypeDef",
    {
        "FeatureAdditions": List["FeatureDefinitionTypeDef"],
        "OnlineStoreConfig": "OnlineStoreConfigUpdateTypeDef",
    },
    total=False,
)

class UpdateFeatureGroupRequestRequestTypeDef(
    _RequiredUpdateFeatureGroupRequestRequestTypeDef,
    _OptionalUpdateFeatureGroupRequestRequestTypeDef,
):
    pass

UpdateFeatureGroupResponseTypeDef = TypedDict(
    "UpdateFeatureGroupResponseTypeDef",
    {
        "FeatureGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFeatureMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFeatureMetadataRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "FeatureName": str,
    },
)
_OptionalUpdateFeatureMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFeatureMetadataRequestRequestTypeDef",
    {
        "Description": str,
        "ParameterAdditions": List["FeatureParameterTypeDef"],
        "ParameterRemovals": List[str],
    },
    total=False,
)

class UpdateFeatureMetadataRequestRequestTypeDef(
    _RequiredUpdateFeatureMetadataRequestRequestTypeDef,
    _OptionalUpdateFeatureMetadataRequestRequestTypeDef,
):
    pass

_RequiredUpdateHubRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHubRequestRequestTypeDef",
    {
        "HubName": str,
    },
)
_OptionalUpdateHubRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHubRequestRequestTypeDef",
    {
        "HubDescription": str,
        "HubDisplayName": str,
        "HubSearchKeywords": List[str],
    },
    total=False,
)

class UpdateHubRequestRequestTypeDef(
    _RequiredUpdateHubRequestRequestTypeDef, _OptionalUpdateHubRequestRequestTypeDef
):
    pass

UpdateHubResponseTypeDef = TypedDict(
    "UpdateHubResponseTypeDef",
    {
        "HubArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateImageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateImageRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalUpdateImageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateImageRequestRequestTypeDef",
    {
        "DeleteProperties": List[str],
        "Description": str,
        "DisplayName": str,
        "RoleArn": str,
    },
    total=False,
)

class UpdateImageRequestRequestTypeDef(
    _RequiredUpdateImageRequestRequestTypeDef, _OptionalUpdateImageRequestRequestTypeDef
):
    pass

UpdateImageResponseTypeDef = TypedDict(
    "UpdateImageResponseTypeDef",
    {
        "ImageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateImageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateImageVersionRequestRequestTypeDef",
    {
        "ImageName": str,
    },
)
_OptionalUpdateImageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateImageVersionRequestRequestTypeDef",
    {
        "Alias": str,
        "Version": int,
        "AliasesToAdd": List[str],
        "AliasesToDelete": List[str],
        "VendorGuidance": VendorGuidanceType,
        "JobType": JobTypeType,
        "MLFramework": str,
        "ProgrammingLang": str,
        "Processor": ProcessorType,
        "Horovod": bool,
        "ReleaseNotes": str,
    },
    total=False,
)

class UpdateImageVersionRequestRequestTypeDef(
    _RequiredUpdateImageVersionRequestRequestTypeDef,
    _OptionalUpdateImageVersionRequestRequestTypeDef,
):
    pass

UpdateImageVersionResponseTypeDef = TypedDict(
    "UpdateImageVersionResponseTypeDef",
    {
        "ImageVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInferenceExperimentRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateInferenceExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInferenceExperimentRequestRequestTypeDef",
    {
        "Schedule": "InferenceExperimentScheduleTypeDef",
        "Description": str,
        "ModelVariants": List["ModelVariantConfigTypeDef"],
        "DataStorageConfig": "InferenceExperimentDataStorageConfigTypeDef",
        "ShadowModeConfig": "ShadowModeConfigTypeDef",
    },
    total=False,
)

class UpdateInferenceExperimentRequestRequestTypeDef(
    _RequiredUpdateInferenceExperimentRequestRequestTypeDef,
    _OptionalUpdateInferenceExperimentRequestRequestTypeDef,
):
    pass

UpdateInferenceExperimentResponseTypeDef = TypedDict(
    "UpdateInferenceExperimentResponseTypeDef",
    {
        "InferenceExperimentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelCardRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelCardRequestRequestTypeDef",
    {
        "ModelCardName": str,
    },
)
_OptionalUpdateModelCardRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelCardRequestRequestTypeDef",
    {
        "Content": str,
        "ModelCardStatus": ModelCardStatusType,
    },
    total=False,
)

class UpdateModelCardRequestRequestTypeDef(
    _RequiredUpdateModelCardRequestRequestTypeDef, _OptionalUpdateModelCardRequestRequestTypeDef
):
    pass

UpdateModelCardResponseTypeDef = TypedDict(
    "UpdateModelCardResponseTypeDef",
    {
        "ModelCardArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelPackageInputRequestTypeDef = TypedDict(
    "_RequiredUpdateModelPackageInputRequestTypeDef",
    {
        "ModelPackageArn": str,
    },
)
_OptionalUpdateModelPackageInputRequestTypeDef = TypedDict(
    "_OptionalUpdateModelPackageInputRequestTypeDef",
    {
        "ModelApprovalStatus": ModelApprovalStatusType,
        "ApprovalDescription": str,
        "CustomerMetadataProperties": Dict[str, str],
        "CustomerMetadataPropertiesToRemove": List[str],
        "AdditionalInferenceSpecificationsToAdd": List[
            "AdditionalInferenceSpecificationDefinitionTypeDef"
        ],
    },
    total=False,
)

class UpdateModelPackageInputRequestTypeDef(
    _RequiredUpdateModelPackageInputRequestTypeDef, _OptionalUpdateModelPackageInputRequestTypeDef
):
    pass

UpdateModelPackageOutputTypeDef = TypedDict(
    "UpdateModelPackageOutputTypeDef",
    {
        "ModelPackageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMonitoringAlertRequestRequestTypeDef = TypedDict(
    "UpdateMonitoringAlertRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringAlertName": str,
        "DatapointsToAlert": int,
        "EvaluationPeriod": int,
    },
)

UpdateMonitoringAlertResponseTypeDef = TypedDict(
    "UpdateMonitoringAlertResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringAlertName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMonitoringScheduleRequestRequestTypeDef = TypedDict(
    "UpdateMonitoringScheduleRequestRequestTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
    },
)

UpdateMonitoringScheduleResponseTypeDef = TypedDict(
    "UpdateMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNotebookInstanceInputRequestTypeDef",
    {
        "NotebookInstanceName": str,
    },
)
_OptionalUpdateNotebookInstanceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNotebookInstanceInputRequestTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "RoleArn": str,
        "LifecycleConfigName": str,
        "DisassociateLifecycleConfig": bool,
        "VolumeSizeInGB": int,
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "AcceleratorTypes": List[NotebookInstanceAcceleratorTypeType],
        "DisassociateAcceleratorTypes": bool,
        "DisassociateDefaultCodeRepository": bool,
        "DisassociateAdditionalCodeRepositories": bool,
        "RootAccess": RootAccessType,
        "InstanceMetadataServiceConfiguration": "InstanceMetadataServiceConfigurationTypeDef",
    },
    total=False,
)

class UpdateNotebookInstanceInputRequestTypeDef(
    _RequiredUpdateNotebookInstanceInputRequestTypeDef,
    _OptionalUpdateNotebookInstanceInputRequestTypeDef,
):
    pass

_RequiredUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "NotebookInstanceLifecycleConfigName": str,
    },
)
_OptionalUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef",
    {
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
    },
    total=False,
)

class UpdateNotebookInstanceLifecycleConfigInputRequestTypeDef(
    _RequiredUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef,
    _OptionalUpdateNotebookInstanceLifecycleConfigInputRequestTypeDef,
):
    pass

_RequiredUpdatePipelineExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionArn": str,
    },
)
_OptionalUpdatePipelineExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineExecutionRequestRequestTypeDef",
    {
        "PipelineExecutionDescription": str,
        "PipelineExecutionDisplayName": str,
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
    },
    total=False,
)

class UpdatePipelineExecutionRequestRequestTypeDef(
    _RequiredUpdatePipelineExecutionRequestRequestTypeDef,
    _OptionalUpdatePipelineExecutionRequestRequestTypeDef,
):
    pass

UpdatePipelineExecutionResponseTypeDef = TypedDict(
    "UpdatePipelineExecutionResponseTypeDef",
    {
        "PipelineExecutionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePipelineRequestRequestTypeDef",
    {
        "PipelineName": str,
    },
)
_OptionalUpdatePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePipelineRequestRequestTypeDef",
    {
        "PipelineDisplayName": str,
        "PipelineDefinition": str,
        "PipelineDefinitionS3Location": "PipelineDefinitionS3LocationTypeDef",
        "PipelineDescription": str,
        "RoleArn": str,
        "ParallelismConfiguration": "ParallelismConfigurationTypeDef",
    },
    total=False,
)

class UpdatePipelineRequestRequestTypeDef(
    _RequiredUpdatePipelineRequestRequestTypeDef, _OptionalUpdatePipelineRequestRequestTypeDef
):
    pass

UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "PipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectInputRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalUpdateProjectInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectInputRequestTypeDef",
    {
        "ProjectDescription": str,
        "ServiceCatalogProvisioningUpdateDetails": "ServiceCatalogProvisioningUpdateDetailsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UpdateProjectInputRequestTypeDef(
    _RequiredUpdateProjectInputRequestTypeDef, _OptionalUpdateProjectInputRequestTypeDef
):
    pass

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSpaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSpaceRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpaceName": str,
    },
)
_OptionalUpdateSpaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSpaceRequestRequestTypeDef",
    {
        "SpaceSettings": "SpaceSettingsTypeDef",
    },
    total=False,
)

class UpdateSpaceRequestRequestTypeDef(
    _RequiredUpdateSpaceRequestRequestTypeDef, _OptionalUpdateSpaceRequestRequestTypeDef
):
    pass

UpdateSpaceResponseTypeDef = TypedDict(
    "UpdateSpaceResponseTypeDef",
    {
        "SpaceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrainingJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrainingJobRequestRequestTypeDef",
    {
        "TrainingJobName": str,
    },
)
_OptionalUpdateTrainingJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrainingJobRequestRequestTypeDef",
    {
        "ProfilerConfig": "ProfilerConfigForUpdateTypeDef",
        "ProfilerRuleConfigurations": List["ProfilerRuleConfigurationTypeDef"],
        "ResourceConfig": "ResourceConfigForUpdateTypeDef",
    },
    total=False,
)

class UpdateTrainingJobRequestRequestTypeDef(
    _RequiredUpdateTrainingJobRequestRequestTypeDef, _OptionalUpdateTrainingJobRequestRequestTypeDef
):
    pass

UpdateTrainingJobResponseTypeDef = TypedDict(
    "UpdateTrainingJobResponseTypeDef",
    {
        "TrainingJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrialComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrialComponentRequestRequestTypeDef",
    {
        "TrialComponentName": str,
    },
)
_OptionalUpdateTrialComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrialComponentRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Status": "TrialComponentStatusTypeDef",
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Parameters": Dict[str, "TrialComponentParameterValueTypeDef"],
        "ParametersToRemove": List[str],
        "InputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "InputArtifactsToRemove": List[str],
        "OutputArtifacts": Dict[str, "TrialComponentArtifactTypeDef"],
        "OutputArtifactsToRemove": List[str],
    },
    total=False,
)

class UpdateTrialComponentRequestRequestTypeDef(
    _RequiredUpdateTrialComponentRequestRequestTypeDef,
    _OptionalUpdateTrialComponentRequestRequestTypeDef,
):
    pass

UpdateTrialComponentResponseTypeDef = TypedDict(
    "UpdateTrialComponentResponseTypeDef",
    {
        "TrialComponentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTrialRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTrialRequestRequestTypeDef",
    {
        "TrialName": str,
    },
)
_OptionalUpdateTrialRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTrialRequestRequestTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class UpdateTrialRequestRequestTypeDef(
    _RequiredUpdateTrialRequestRequestTypeDef, _OptionalUpdateTrialRequestRequestTypeDef
):
    pass

UpdateTrialResponseTypeDef = TypedDict(
    "UpdateTrialResponseTypeDef",
    {
        "TrialArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserProfileRequestRequestTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
    },
)
_OptionalUpdateUserProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserProfileRequestRequestTypeDef",
    {
        "UserSettings": "UserSettingsTypeDef",
    },
    total=False,
)

class UpdateUserProfileRequestRequestTypeDef(
    _RequiredUpdateUserProfileRequestRequestTypeDef, _OptionalUpdateUserProfileRequestRequestTypeDef
):
    pass

UpdateUserProfileResponseTypeDef = TypedDict(
    "UpdateUserProfileResponseTypeDef",
    {
        "UserProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkforceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkforceRequestRequestTypeDef",
    {
        "WorkforceName": str,
    },
)
_OptionalUpdateWorkforceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkforceRequestRequestTypeDef",
    {
        "SourceIpConfig": "SourceIpConfigTypeDef",
        "OidcConfig": "OidcConfigTypeDef",
        "WorkforceVpcConfig": "WorkforceVpcConfigRequestTypeDef",
    },
    total=False,
)

class UpdateWorkforceRequestRequestTypeDef(
    _RequiredUpdateWorkforceRequestRequestTypeDef, _OptionalUpdateWorkforceRequestRequestTypeDef
):
    pass

UpdateWorkforceResponseTypeDef = TypedDict(
    "UpdateWorkforceResponseTypeDef",
    {
        "Workforce": "WorkforceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkteamRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkteamRequestRequestTypeDef",
    {
        "WorkteamName": str,
    },
)
_OptionalUpdateWorkteamRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkteamRequestRequestTypeDef",
    {
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "Description": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
    total=False,
)

class UpdateWorkteamRequestRequestTypeDef(
    _RequiredUpdateWorkteamRequestRequestTypeDef, _OptionalUpdateWorkteamRequestRequestTypeDef
):
    pass

UpdateWorkteamResponseTypeDef = TypedDict(
    "UpdateWorkteamResponseTypeDef",
    {
        "Workteam": "WorkteamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "UserProfileArn": str,
        "UserProfileName": str,
        "DomainId": str,
        "IamIdentity": "IamIdentityTypeDef",
    },
    total=False,
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "Status": UserProfileStatusType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "ExecutionRole": str,
        "SecurityGroups": List[str],
        "SharingSettings": "SharingSettingsTypeDef",
        "JupyterServerAppSettings": "JupyterServerAppSettingsTypeDef",
        "KernelGatewayAppSettings": "KernelGatewayAppSettingsTypeDef",
        "TensorBoardAppSettings": "TensorBoardAppSettingsTypeDef",
        "RStudioServerProAppSettings": "RStudioServerProAppSettingsTypeDef",
        "RSessionAppSettings": "RSessionAppSettingsTypeDef",
        "CanvasAppSettings": "CanvasAppSettingsTypeDef",
    },
    total=False,
)

VariantPropertyTypeDef = TypedDict(
    "VariantPropertyTypeDef",
    {
        "VariantPropertyType": VariantPropertyTypeType,
    },
)

VectorConfigTypeDef = TypedDict(
    "VectorConfigTypeDef",
    {
        "Dimension": int,
    },
)

VertexTypeDef = TypedDict(
    "VertexTypeDef",
    {
        "Arn": str,
        "Type": str,
        "LineageType": LineageTypeType,
    },
    total=False,
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWarmPoolStatusTypeDef = TypedDict(
    "_RequiredWarmPoolStatusTypeDef",
    {
        "Status": WarmPoolResourceStatusType,
    },
)
_OptionalWarmPoolStatusTypeDef = TypedDict(
    "_OptionalWarmPoolStatusTypeDef",
    {
        "ResourceRetainedBillableTimeInSeconds": int,
        "ReusedByJob": str,
    },
    total=False,
)

class WarmPoolStatusTypeDef(_RequiredWarmPoolStatusTypeDef, _OptionalWarmPoolStatusTypeDef):
    pass

_RequiredWorkforceTypeDef = TypedDict(
    "_RequiredWorkforceTypeDef",
    {
        "WorkforceName": str,
        "WorkforceArn": str,
    },
)
_OptionalWorkforceTypeDef = TypedDict(
    "_OptionalWorkforceTypeDef",
    {
        "LastUpdatedDate": datetime,
        "SourceIpConfig": "SourceIpConfigTypeDef",
        "SubDomain": str,
        "CognitoConfig": "CognitoConfigTypeDef",
        "OidcConfig": "OidcConfigForResponseTypeDef",
        "CreateDate": datetime,
        "WorkforceVpcConfig": "WorkforceVpcConfigResponseTypeDef",
        "Status": WorkforceStatusType,
        "FailureReason": str,
    },
    total=False,
)

class WorkforceTypeDef(_RequiredWorkforceTypeDef, _OptionalWorkforceTypeDef):
    pass

WorkforceVpcConfigRequestTypeDef = TypedDict(
    "WorkforceVpcConfigRequestTypeDef",
    {
        "VpcId": str,
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
    total=False,
)

_RequiredWorkforceVpcConfigResponseTypeDef = TypedDict(
    "_RequiredWorkforceVpcConfigResponseTypeDef",
    {
        "VpcId": str,
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)
_OptionalWorkforceVpcConfigResponseTypeDef = TypedDict(
    "_OptionalWorkforceVpcConfigResponseTypeDef",
    {
        "VpcEndpointId": str,
    },
    total=False,
)

class WorkforceVpcConfigResponseTypeDef(
    _RequiredWorkforceVpcConfigResponseTypeDef, _OptionalWorkforceVpcConfigResponseTypeDef
):
    pass

WorkspaceSettingsTypeDef = TypedDict(
    "WorkspaceSettingsTypeDef",
    {
        "S3ArtifactPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

_RequiredWorkteamTypeDef = TypedDict(
    "_RequiredWorkteamTypeDef",
    {
        "WorkteamName": str,
        "MemberDefinitions": List["MemberDefinitionTypeDef"],
        "WorkteamArn": str,
        "Description": str,
    },
)
_OptionalWorkteamTypeDef = TypedDict(
    "_OptionalWorkteamTypeDef",
    {
        "WorkforceArn": str,
        "ProductListingIds": List[str],
        "SubDomain": str,
        "CreateDate": datetime,
        "LastUpdatedDate": datetime,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
    total=False,
)

class WorkteamTypeDef(_RequiredWorkteamTypeDef, _OptionalWorkteamTypeDef):
    pass
