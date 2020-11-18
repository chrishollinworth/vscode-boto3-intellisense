"""
Main interface for sagemaker service type definitions.

Usage::

    ```python
    from mypy_boto3_sagemaker.type_defs import AlgorithmSpecificationTypeDef

    data: AlgorithmSpecificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
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
    "AutoMLCandidateStepTypeDef",
    "AutoMLCandidateTypeDef",
    "AutoMLChannelTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "AutoMLDataSourceTypeDef",
    "AutoMLJobArtifactsTypeDef",
    "AutoMLJobCompletionCriteriaTypeDef",
    "AutoMLJobConfigTypeDef",
    "AutoMLJobObjectiveTypeDef",
    "AutoMLJobSummaryTypeDef",
    "AutoMLOutputDataConfigTypeDef",
    "AutoMLS3DataSourceTypeDef",
    "AutoMLSecurityConfigTypeDef",
    "CaptureContentTypeHeaderTypeDef",
    "CaptureOptionTypeDef",
    "CategoricalParameterRangeSpecificationTypeDef",
    "CategoricalParameterRangeTypeDef",
    "ChannelSpecificationTypeDef",
    "ChannelTypeDef",
    "CheckpointConfigTypeDef",
    "CodeRepositorySummaryTypeDef",
    "CognitoConfigTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "CollectionConfigurationTypeDef",
    "CompilationJobSummaryTypeDef",
    "ContainerDefinitionTypeDef",
    "ContinuousParameterRangeSpecificationTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CustomImageTypeDef",
    "DataCaptureConfigSummaryTypeDef",
    "DataCaptureConfigTypeDef",
    "DataProcessingTypeDef",
    "DataSourceTypeDef",
    "DebugHookConfigTypeDef",
    "DebugRuleConfigurationTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "DeployedImageTypeDef",
    "DomainDetailsTypeDef",
    "EndpointConfigSummaryTypeDef",
    "EndpointInputTypeDef",
    "EndpointSummaryTypeDef",
    "ExperimentConfigTypeDef",
    "ExperimentSourceTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTypeDef",
    "FileSystemConfigTypeDef",
    "FileSystemDataSourceTypeDef",
    "FilterTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "FlowDefinitionOutputConfigTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "GitConfigTypeDef",
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
    "HyperParameterTuningJobConfigTypeDef",
    "HyperParameterTuningJobObjectiveTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    "ImageConfigTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "InferenceSpecificationTypeDef",
    "InputConfigTypeDef",
    "IntegerParameterRangeSpecificationTypeDef",
    "IntegerParameterRangeTypeDef",
    "JupyterServerAppSettingsTypeDef",
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
    "MemberDefinitionTypeDef",
    "MetricDataTypeDef",
    "MetricDefinitionTypeDef",
    "ModelArtifactsTypeDef",
    "ModelClientConfigTypeDef",
    "ModelPackageContainerDefinitionTypeDef",
    "ModelPackageStatusDetailsTypeDef",
    "ModelPackageStatusItemTypeDef",
    "ModelPackageSummaryTypeDef",
    "ModelPackageValidationProfileTypeDef",
    "ModelPackageValidationSpecificationTypeDef",
    "ModelSummaryTypeDef",
    "MonitoringAppSpecificationTypeDef",
    "MonitoringBaselineConfigTypeDef",
    "MonitoringClusterConfigTypeDef",
    "MonitoringConstraintsResourceTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "MonitoringInputTypeDef",
    "MonitoringJobDefinitionTypeDef",
    "MonitoringOutputConfigTypeDef",
    "MonitoringOutputTypeDef",
    "MonitoringResourcesTypeDef",
    "MonitoringS3OutputTypeDef",
    "MonitoringScheduleConfigTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "MonitoringStatisticsResourceTypeDef",
    "MonitoringStoppingConditionTypeDef",
    "NestedFiltersTypeDef",
    "NetworkConfigTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "NotebookInstanceLifecycleHookTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "OidcConfigForResponseTypeDef",
    "OidcMemberDefinitionTypeDef",
    "OutputConfigTypeDef",
    "OutputDataConfigTypeDef",
    "ParameterRangeTypeDef",
    "ParameterRangesTypeDef",
    "ParentHyperParameterTuningJobTypeDef",
    "ParentTypeDef",
    "ProcessingClusterConfigTypeDef",
    "ProcessingInputTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ProcessingJobTypeDef",
    "ProcessingOutputConfigTypeDef",
    "ProcessingOutputTypeDef",
    "ProcessingResourcesTypeDef",
    "ProcessingS3InputTypeDef",
    "ProcessingS3OutputTypeDef",
    "ProcessingStoppingConditionTypeDef",
    "ProductionVariantSummaryTypeDef",
    "ProductionVariantTypeDef",
    "PropertyNameQueryTypeDef",
    "PropertyNameSuggestionTypeDef",
    "PublicWorkforceTaskPriceTypeDef",
    "RenderingErrorTypeDef",
    "ResolvedAttributesTypeDef",
    "ResourceConfigTypeDef",
    "ResourceLimitsTypeDef",
    "ResourceSpecTypeDef",
    "ResponseMetadata",
    "S3DataSourceTypeDef",
    "ScheduleConfigTypeDef",
    "SearchRecordTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "SharingSettingsTypeDef",
    "ShuffleConfigTypeDef",
    "SourceAlgorithmSpecificationTypeDef",
    "SourceAlgorithmTypeDef",
    "SourceIpConfigTypeDef",
    "StoppingConditionTypeDef",
    "SubscribedWorkteamTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "TensorBoardAppSettingsTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "TrainingJobDefinitionTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "TrainingJobSummaryTypeDef",
    "TrainingJobTypeDef",
    "TrainingSpecificationTypeDef",
    "TransformDataSourceTypeDef",
    "TransformInputTypeDef",
    "TransformJobDefinitionTypeDef",
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
    "TuningJobCompletionCriteriaTypeDef",
    "USDTypeDef",
    "UiConfigTypeDef",
    "UiTemplateInfoTypeDef",
    "UserContextTypeDef",
    "UserProfileDetailsTypeDef",
    "UserSettingsTypeDef",
    "VpcConfigTypeDef",
    "WorkforceTypeDef",
    "WorkteamTypeDef",
    "AddTagsOutputTypeDef",
    "AssociateTrialComponentResponseTypeDef",
    "CreateAlgorithmOutputTypeDef",
    "CreateAppImageConfigResponseTypeDef",
    "CreateAppResponseTypeDef",
    "CreateAutoMLJobResponseTypeDef",
    "CreateCodeRepositoryOutputTypeDef",
    "CreateCompilationJobResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEndpointConfigOutputTypeDef",
    "CreateEndpointOutputTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFlowDefinitionResponseTypeDef",
    "CreateHumanTaskUiResponseTypeDef",
    "CreateHyperParameterTuningJobResponseTypeDef",
    "CreateImageResponseTypeDef",
    "CreateImageVersionResponseTypeDef",
    "CreateLabelingJobResponseTypeDef",
    "CreateModelOutputTypeDef",
    "CreateModelPackageOutputTypeDef",
    "CreateMonitoringScheduleResponseTypeDef",
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    "CreateNotebookInstanceOutputTypeDef",
    "CreatePresignedDomainUrlResponseTypeDef",
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    "CreateProcessingJobResponseTypeDef",
    "CreateTrainingJobResponseTypeDef",
    "CreateTransformJobResponseTypeDef",
    "CreateTrialComponentResponseTypeDef",
    "CreateTrialResponseTypeDef",
    "CreateUserProfileResponseTypeDef",
    "CreateWorkforceResponseTypeDef",
    "CreateWorkteamResponseTypeDef",
    "DeleteExperimentResponseTypeDef",
    "DeleteTrialComponentResponseTypeDef",
    "DeleteTrialResponseTypeDef",
    "DeleteWorkteamResponseTypeDef",
    "DescribeAlgorithmOutputTypeDef",
    "DescribeAppImageConfigResponseTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeAutoMLJobResponseTypeDef",
    "DescribeCodeRepositoryOutputTypeDef",
    "DescribeCompilationJobResponseTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeEndpointConfigOutputTypeDef",
    "DescribeEndpointOutputTypeDef",
    "DescribeExperimentResponseTypeDef",
    "DescribeFlowDefinitionResponseTypeDef",
    "DescribeHumanTaskUiResponseTypeDef",
    "DescribeHyperParameterTuningJobResponseTypeDef",
    "DescribeImageResponseTypeDef",
    "DescribeImageVersionResponseTypeDef",
    "DescribeLabelingJobResponseTypeDef",
    "DescribeModelOutputTypeDef",
    "DescribeModelPackageOutputTypeDef",
    "DescribeMonitoringScheduleResponseTypeDef",
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    "DescribeNotebookInstanceOutputTypeDef",
    "DescribeProcessingJobResponseTypeDef",
    "DescribeSubscribedWorkteamResponseTypeDef",
    "DescribeTrainingJobResponseTypeDef",
    "DescribeTransformJobResponseTypeDef",
    "DescribeTrialComponentResponseTypeDef",
    "DescribeTrialResponseTypeDef",
    "DescribeUserProfileResponseTypeDef",
    "DescribeWorkforceResponseTypeDef",
    "DescribeWorkteamResponseTypeDef",
    "DesiredWeightAndCapacityTypeDef",
    "SearchExpressionTypeDef",
    "DisassociateTrialComponentResponseTypeDef",
    "GetSearchSuggestionsResponseTypeDef",
    "GitConfigForUpdateTypeDef",
    "ListAlgorithmsOutputTypeDef",
    "ListAppImageConfigsResponseTypeDef",
    "ListAppsResponseTypeDef",
    "ListAutoMLJobsResponseTypeDef",
    "ListCandidatesForAutoMLJobResponseTypeDef",
    "ListCodeRepositoriesOutputTypeDef",
    "ListCompilationJobsResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEndpointConfigsOutputTypeDef",
    "ListEndpointsOutputTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFlowDefinitionsResponseTypeDef",
    "ListHumanTaskUisResponseTypeDef",
    "ListHyperParameterTuningJobsResponseTypeDef",
    "ListImageVersionsResponseTypeDef",
    "ListImagesResponseTypeDef",
    "ListLabelingJobsForWorkteamResponseTypeDef",
    "ListLabelingJobsResponseTypeDef",
    "ListModelPackagesOutputTypeDef",
    "ListModelsOutputTypeDef",
    "ListMonitoringExecutionsResponseTypeDef",
    "ListMonitoringSchedulesResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    "ListNotebookInstancesOutputTypeDef",
    "ListProcessingJobsResponseTypeDef",
    "ListSubscribedWorkteamsResponseTypeDef",
    "ListTagsOutputTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ListTrainingJobsResponseTypeDef",
    "ListTransformJobsResponseTypeDef",
    "ListTrialComponentsResponseTypeDef",
    "ListTrialsResponseTypeDef",
    "ListUserProfilesResponseTypeDef",
    "ListWorkforcesResponseTypeDef",
    "ListWorkteamsResponseTypeDef",
    "OidcConfigTypeDef",
    "PaginatorConfigTypeDef",
    "RenderUiTemplateResponseTypeDef",
    "RenderableTaskTypeDef",
    "RetentionPolicyTypeDef",
    "SearchResponseTypeDef",
    "SuggestionQueryTypeDef",
    "UiTemplateTypeDef",
    "UpdateAppImageConfigResponseTypeDef",
    "UpdateCodeRepositoryOutputTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateEndpointOutputTypeDef",
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateImageResponseTypeDef",
    "UpdateMonitoringScheduleResponseTypeDef",
    "UpdateTrialComponentResponseTypeDef",
    "UpdateTrialResponseTypeDef",
    "UpdateUserProfileResponseTypeDef",
    "UpdateWorkforceResponseTypeDef",
    "UpdateWorkteamResponseTypeDef",
    "VariantPropertyTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredAlgorithmSpecificationTypeDef", {"TrainingInputMode": Literal["Pipe", "File"]}
)
_OptionalAlgorithmSpecificationTypeDef = TypedDict(
    "_OptionalAlgorithmSpecificationTypeDef",
    {
        "TrainingImage": str,
        "AlgorithmName": str,
        "MetricDefinitions": List["MetricDefinitionTypeDef"],
        "EnableSageMakerMetricsTimeSeries": bool,
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
    {"Name": str, "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"]},
)
_OptionalAlgorithmStatusItemTypeDef = TypedDict(
    "_OptionalAlgorithmStatusItemTypeDef", {"FailureReason": str}, total=False
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
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
)
_OptionalAlgorithmSummaryTypeDef = TypedDict(
    "_OptionalAlgorithmSummaryTypeDef", {"AlgorithmDescription": str}, total=False
)


class AlgorithmSummaryTypeDef(_RequiredAlgorithmSummaryTypeDef, _OptionalAlgorithmSummaryTypeDef):
    pass


_RequiredAlgorithmValidationProfileTypeDef = TypedDict(
    "_RequiredAlgorithmValidationProfileTypeDef",
    {"ProfileName": str, "TrainingJobDefinition": "TrainingJobDefinitionTypeDef"},
)
_OptionalAlgorithmValidationProfileTypeDef = TypedDict(
    "_OptionalAlgorithmValidationProfileTypeDef",
    {"TransformJobDefinition": "TransformJobDefinitionTypeDef"},
    total=False,
)


class AlgorithmValidationProfileTypeDef(
    _RequiredAlgorithmValidationProfileTypeDef, _OptionalAlgorithmValidationProfileTypeDef
):
    pass


AlgorithmValidationSpecificationTypeDef = TypedDict(
    "AlgorithmValidationSpecificationTypeDef",
    {"ValidationRole": str, "ValidationProfiles": List["AlgorithmValidationProfileTypeDef"]},
)

AnnotationConsolidationConfigTypeDef = TypedDict(
    "AnnotationConsolidationConfigTypeDef", {"AnnotationConsolidationLambdaArn": str}
)

AppDetailsTypeDef = TypedDict(
    "AppDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "AppType": Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        "AppName": str,
        "Status": Literal["Deleted", "Deleting", "Failed", "InService", "Pending"],
        "CreationTime": datetime,
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

_RequiredAppSpecificationTypeDef = TypedDict("_RequiredAppSpecificationTypeDef", {"ImageUri": str})
_OptionalAppSpecificationTypeDef = TypedDict(
    "_OptionalAppSpecificationTypeDef",
    {"ContainerEntrypoint": List[str], "ContainerArguments": List[str]},
    total=False,
)


class AppSpecificationTypeDef(_RequiredAppSpecificationTypeDef, _OptionalAppSpecificationTypeDef):
    pass


AutoMLCandidateStepTypeDef = TypedDict(
    "AutoMLCandidateStepTypeDef",
    {
        "CandidateStepType": Literal[
            "AWS::SageMaker::TrainingJob",
            "AWS::SageMaker::TransformJob",
            "AWS::SageMaker::ProcessingJob",
        ],
        "CandidateStepArn": str,
        "CandidateStepName": str,
    },
)

_RequiredAutoMLCandidateTypeDef = TypedDict(
    "_RequiredAutoMLCandidateTypeDef",
    {
        "CandidateName": str,
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
        "CandidateSteps": List["AutoMLCandidateStepTypeDef"],
        "CandidateStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
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
    },
    total=False,
)


class AutoMLCandidateTypeDef(_RequiredAutoMLCandidateTypeDef, _OptionalAutoMLCandidateTypeDef):
    pass


_RequiredAutoMLChannelTypeDef = TypedDict(
    "_RequiredAutoMLChannelTypeDef",
    {"DataSource": "AutoMLDataSourceTypeDef", "TargetAttributeName": str},
)
_OptionalAutoMLChannelTypeDef = TypedDict(
    "_OptionalAutoMLChannelTypeDef", {"CompressionType": Literal["None", "Gzip"]}, total=False
)


class AutoMLChannelTypeDef(_RequiredAutoMLChannelTypeDef, _OptionalAutoMLChannelTypeDef):
    pass


_RequiredAutoMLContainerDefinitionTypeDef = TypedDict(
    "_RequiredAutoMLContainerDefinitionTypeDef", {"Image": str, "ModelDataUrl": str}
)
_OptionalAutoMLContainerDefinitionTypeDef = TypedDict(
    "_OptionalAutoMLContainerDefinitionTypeDef", {"Environment": Dict[str, str]}, total=False
)


class AutoMLContainerDefinitionTypeDef(
    _RequiredAutoMLContainerDefinitionTypeDef, _OptionalAutoMLContainerDefinitionTypeDef
):
    pass


AutoMLDataSourceTypeDef = TypedDict(
    "AutoMLDataSourceTypeDef", {"S3DataSource": "AutoMLS3DataSourceTypeDef"}
)

AutoMLJobArtifactsTypeDef = TypedDict(
    "AutoMLJobArtifactsTypeDef",
    {"CandidateDefinitionNotebookLocation": str, "DataExplorationNotebookLocation": str},
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
    },
    total=False,
)

AutoMLJobObjectiveTypeDef = TypedDict(
    "AutoMLJobObjectiveTypeDef", {"MetricName": Literal["Accuracy", "MSE", "F1", "F1macro", "AUC"]}
)

_RequiredAutoMLJobSummaryTypeDef = TypedDict(
    "_RequiredAutoMLJobSummaryTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "AutoMLJobStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "AutoMLJobSecondaryStatus": Literal[
            "Starting",
            "AnalyzingData",
            "FeatureEngineering",
            "ModelTuning",
            "MaxCandidatesReached",
            "Failed",
            "Stopped",
            "MaxAutoMLJobRuntimeReached",
            "Stopping",
            "CandidateDefinitionsGenerated",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalAutoMLJobSummaryTypeDef = TypedDict(
    "_OptionalAutoMLJobSummaryTypeDef", {"EndTime": datetime, "FailureReason": str}, total=False
)


class AutoMLJobSummaryTypeDef(_RequiredAutoMLJobSummaryTypeDef, _OptionalAutoMLJobSummaryTypeDef):
    pass


_RequiredAutoMLOutputDataConfigTypeDef = TypedDict(
    "_RequiredAutoMLOutputDataConfigTypeDef", {"S3OutputPath": str}
)
_OptionalAutoMLOutputDataConfigTypeDef = TypedDict(
    "_OptionalAutoMLOutputDataConfigTypeDef", {"KmsKeyId": str}, total=False
)


class AutoMLOutputDataConfigTypeDef(
    _RequiredAutoMLOutputDataConfigTypeDef, _OptionalAutoMLOutputDataConfigTypeDef
):
    pass


AutoMLS3DataSourceTypeDef = TypedDict(
    "AutoMLS3DataSourceTypeDef", {"S3DataType": Literal["ManifestFile", "S3Prefix"], "S3Uri": str}
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

CaptureContentTypeHeaderTypeDef = TypedDict(
    "CaptureContentTypeHeaderTypeDef",
    {"CsvContentTypes": List[str], "JsonContentTypes": List[str]},
    total=False,
)

CaptureOptionTypeDef = TypedDict(
    "CaptureOptionTypeDef", {"CaptureMode": Literal["Input", "Output"]}
)

CategoricalParameterRangeSpecificationTypeDef = TypedDict(
    "CategoricalParameterRangeSpecificationTypeDef", {"Values": List[str]}
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef", {"Name": str, "Values": List[str]}
)

_RequiredChannelSpecificationTypeDef = TypedDict(
    "_RequiredChannelSpecificationTypeDef",
    {
        "Name": str,
        "SupportedContentTypes": List[str],
        "SupportedInputModes": List[Literal["Pipe", "File"]],
    },
)
_OptionalChannelSpecificationTypeDef = TypedDict(
    "_OptionalChannelSpecificationTypeDef",
    {
        "Description": str,
        "IsRequired": bool,
        "SupportedCompressionTypes": List[Literal["None", "Gzip"]],
    },
    total=False,
)


class ChannelSpecificationTypeDef(
    _RequiredChannelSpecificationTypeDef, _OptionalChannelSpecificationTypeDef
):
    pass


_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef", {"ChannelName": str, "DataSource": "DataSourceTypeDef"}
)
_OptionalChannelTypeDef = TypedDict(
    "_OptionalChannelTypeDef",
    {
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "RecordWrapperType": Literal["None", "RecordIO"],
        "InputMode": Literal["Pipe", "File"],
        "ShuffleConfig": "ShuffleConfigTypeDef",
    },
    total=False,
)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


_RequiredCheckpointConfigTypeDef = TypedDict("_RequiredCheckpointConfigTypeDef", {"S3Uri": str})
_OptionalCheckpointConfigTypeDef = TypedDict(
    "_OptionalCheckpointConfigTypeDef", {"LocalPath": str}, total=False
)


class CheckpointConfigTypeDef(_RequiredCheckpointConfigTypeDef, _OptionalCheckpointConfigTypeDef):
    pass


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
    "_OptionalCodeRepositorySummaryTypeDef", {"GitConfig": "GitConfigTypeDef"}, total=False
)


class CodeRepositorySummaryTypeDef(
    _RequiredCodeRepositorySummaryTypeDef, _OptionalCodeRepositorySummaryTypeDef
):
    pass


CognitoConfigTypeDef = TypedDict("CognitoConfigTypeDef", {"UserPool": str, "ClientId": str})

CognitoMemberDefinitionTypeDef = TypedDict(
    "CognitoMemberDefinitionTypeDef", {"UserPool": str, "UserGroup": str, "ClientId": str}
)

CollectionConfigurationTypeDef = TypedDict(
    "CollectionConfigurationTypeDef",
    {"CollectionName": str, "CollectionParameters": Dict[str, str]},
    total=False,
)

_RequiredCompilationJobSummaryTypeDef = TypedDict(
    "_RequiredCompilationJobSummaryTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CreationTime": datetime,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
    },
)
_OptionalCompilationJobSummaryTypeDef = TypedDict(
    "_OptionalCompilationJobSummaryTypeDef",
    {
        "CompilationStartTime": datetime,
        "CompilationEndTime": datetime,
        "CompilationTargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "ml_g4dn",
            "ml_inf1",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "jetson_xavier",
            "rasp3b",
            "imx8qm",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
            "sitara_am57x",
            "amba_cv22",
            "x86_win32",
            "x86_win64",
            "coreml",
        ],
        "CompilationTargetPlatformOs": Literal["ANDROID", "LINUX"],
        "CompilationTargetPlatformArch": Literal[
            "X86_64", "X86", "ARM64", "ARM_EABI", "ARM_EABIHF"
        ],
        "CompilationTargetPlatformAccelerator": Literal["INTEL_GRAPHICS", "MALI", "NVIDIA"],
        "LastModifiedTime": datetime,
    },
    total=False,
)


class CompilationJobSummaryTypeDef(
    _RequiredCompilationJobSummaryTypeDef, _OptionalCompilationJobSummaryTypeDef
):
    pass


ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "ContainerHostname": str,
        "Image": str,
        "ImageConfig": "ImageConfigTypeDef",
        "Mode": Literal["SingleModel", "MultiModel"],
        "ModelDataUrl": str,
        "Environment": Dict[str, str],
        "ModelPackageName": str,
    },
    total=False,
)

ContinuousParameterRangeSpecificationTypeDef = TypedDict(
    "ContinuousParameterRangeSpecificationTypeDef", {"MinValue": str, "MaxValue": str}
)

_RequiredContinuousParameterRangeTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeTypeDef", {"Name": str, "MinValue": str, "MaxValue": str}
)
_OptionalContinuousParameterRangeTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeTypeDef",
    {"ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]},
    total=False,
)


class ContinuousParameterRangeTypeDef(
    _RequiredContinuousParameterRangeTypeDef, _OptionalContinuousParameterRangeTypeDef
):
    pass


_RequiredCustomImageTypeDef = TypedDict(
    "_RequiredCustomImageTypeDef", {"ImageName": str, "AppImageConfigName": str}
)
_OptionalCustomImageTypeDef = TypedDict(
    "_OptionalCustomImageTypeDef", {"ImageVersionNumber": int}, total=False
)


class CustomImageTypeDef(_RequiredCustomImageTypeDef, _OptionalCustomImageTypeDef):
    pass


DataCaptureConfigSummaryTypeDef = TypedDict(
    "DataCaptureConfigSummaryTypeDef",
    {
        "EnableCapture": bool,
        "CaptureStatus": Literal["Started", "Stopped"],
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


DataProcessingTypeDef = TypedDict(
    "DataProcessingTypeDef",
    {"InputFilter": str, "OutputFilter": str, "JoinSource": Literal["Input", "None"]},
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {"S3DataSource": "S3DataSourceTypeDef", "FileSystemDataSource": "FileSystemDataSourceTypeDef"},
    total=False,
)

_RequiredDebugHookConfigTypeDef = TypedDict(
    "_RequiredDebugHookConfigTypeDef", {"S3OutputPath": str}
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
    {"RuleConfigurationName": str, "RuleEvaluatorImage": str},
)
_OptionalDebugRuleConfigurationTypeDef = TypedDict(
    "_OptionalDebugRuleConfigurationTypeDef",
    {
        "LocalPath": str,
        "S3OutputPath": str,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
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
        "RuleEvaluationStatus": Literal[
            "InProgress", "NoIssuesFound", "IssuesFound", "Error", "Stopping", "Stopped"
        ],
        "StatusDetails": str,
        "LastModifiedTime": datetime,
    },
    total=False,
)

DeployedImageTypeDef = TypedDict(
    "DeployedImageTypeDef",
    {"SpecifiedImage": str, "ResolvedImage": str, "ResolutionTime": datetime},
    total=False,
)

DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "Status": Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Updating",
            "Update_Failed",
            "Delete_Failed",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "Url": str,
    },
    total=False,
)

EndpointConfigSummaryTypeDef = TypedDict(
    "EndpointConfigSummaryTypeDef",
    {"EndpointConfigName": str, "EndpointConfigArn": str, "CreationTime": datetime},
)

_RequiredEndpointInputTypeDef = TypedDict(
    "_RequiredEndpointInputTypeDef", {"EndpointName": str, "LocalPath": str}
)
_OptionalEndpointInputTypeDef = TypedDict(
    "_OptionalEndpointInputTypeDef",
    {
        "S3InputMode": Literal["Pipe", "File"],
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
    },
    total=False,
)


class EndpointInputTypeDef(_RequiredEndpointInputTypeDef, _OptionalEndpointInputTypeDef):
    pass


EndpointSummaryTypeDef = TypedDict(
    "EndpointSummaryTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
    },
)

ExperimentConfigTypeDef = TypedDict(
    "ExperimentConfigTypeDef",
    {"ExperimentName": str, "TrialName": str, "TrialComponentDisplayName": str},
    total=False,
)

_RequiredExperimentSourceTypeDef = TypedDict("_RequiredExperimentSourceTypeDef", {"SourceArn": str})
_OptionalExperimentSourceTypeDef = TypedDict(
    "_OptionalExperimentSourceTypeDef", {"SourceType": str}, total=False
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

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef", {"MountPath": str, "DefaultUid": int, "DefaultGid": int}, total=False
)

FileSystemDataSourceTypeDef = TypedDict(
    "FileSystemDataSourceTypeDef",
    {
        "FileSystemId": str,
        "FileSystemAccessMode": Literal["rw", "ro"],
        "FileSystemType": Literal["EFS", "FSxLustre"],
        "DirectoryPath": str,
    },
)

_RequiredFilterTypeDef = TypedDict("_RequiredFilterTypeDef", {"Name": str})
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "Operator": Literal[
            "Equals",
            "NotEquals",
            "GreaterThan",
            "GreaterThanOrEqualTo",
            "LessThan",
            "LessThanOrEqualTo",
            "Contains",
            "Exists",
            "NotExists",
            "In",
        ],
        "Value": str,
    },
    total=False,
)


class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass


_RequiredFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalAutoMLJobObjectiveMetricTypeDef",
    {"MetricName": Literal["Accuracy", "MSE", "F1", "F1macro", "AUC"], "Value": float},
)
_OptionalFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalAutoMLJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"]},
    total=False,
)


class FinalAutoMLJobObjectiveMetricTypeDef(
    _RequiredFinalAutoMLJobObjectiveMetricTypeDef, _OptionalFinalAutoMLJobObjectiveMetricTypeDef
):
    pass


_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"MetricName": str, "Value": float},
)
_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": Literal["Maximize", "Minimize"]},
    total=False,
)


class FinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef,
    _OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef,
):
    pass


_RequiredFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_RequiredFlowDefinitionOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalFlowDefinitionOutputConfigTypeDef = TypedDict(
    "_OptionalFlowDefinitionOutputConfigTypeDef", {"KmsKeyId": str}, total=False
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
        "FlowDefinitionStatus": Literal["Initializing", "Active", "Failed", "Deleting"],
        "CreationTime": datetime,
    },
)
_OptionalFlowDefinitionSummaryTypeDef = TypedDict(
    "_OptionalFlowDefinitionSummaryTypeDef", {"FailureReason": str}, total=False
)


class FlowDefinitionSummaryTypeDef(
    _RequiredFlowDefinitionSummaryTypeDef, _OptionalFlowDefinitionSummaryTypeDef
):
    pass


_RequiredGitConfigTypeDef = TypedDict("_RequiredGitConfigTypeDef", {"RepositoryUrl": str})
_OptionalGitConfigTypeDef = TypedDict(
    "_OptionalGitConfigTypeDef", {"Branch": str, "SecretArn": str}, total=False
)


class GitConfigTypeDef(_RequiredGitConfigTypeDef, _OptionalGitConfigTypeDef):
    pass


HumanLoopActivationConditionsConfigTypeDef = TypedDict(
    "HumanLoopActivationConditionsConfigTypeDef", {"HumanLoopActivationConditions": str}
)

HumanLoopActivationConfigTypeDef = TypedDict(
    "HumanLoopActivationConfigTypeDef",
    {"HumanLoopActivationConditionsConfig": "HumanLoopActivationConditionsConfigTypeDef"},
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
        "AwsManagedHumanLoopRequestSource": Literal[
            "AWS/Rekognition/DetectModerationLabels/Image/V3",
            "AWS/Textract/AnalyzeDocument/Forms/V1",
        ]
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
    {"HumanTaskUiName": str, "HumanTaskUiArn": str, "CreationTime": datetime},
)

_RequiredHyperParameterAlgorithmSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterAlgorithmSpecificationTypeDef",
    {"TrainingInputMode": Literal["Pipe", "File"]},
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
    {"Name": str, "Type": Literal["Integer", "Continuous", "Categorical", "FreeText"]},
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
        "ResourceConfig": "ResourceConfigTypeDef",
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
        "EnableNetworkIsolation": bool,
        "EnableInterContainerTrafficEncryption": bool,
        "EnableManagedSpotTraining": bool,
        "CheckpointConfig": "CheckpointConfigTypeDef",
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
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
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
        "ObjectiveStatus": Literal["Succeeded", "Pending", "Failed"],
    },
    total=False,
)


class HyperParameterTrainingJobSummaryTypeDef(
    _RequiredHyperParameterTrainingJobSummaryTypeDef,
    _OptionalHyperParameterTrainingJobSummaryTypeDef,
):
    pass


_RequiredHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobConfigTypeDef",
    {"Strategy": Literal["Bayesian", "Random"], "ResourceLimits": "ResourceLimitsTypeDef"},
)
_OptionalHyperParameterTuningJobConfigTypeDef = TypedDict(
    "_OptionalHyperParameterTuningJobConfigTypeDef",
    {
        "HyperParameterTuningJobObjective": "HyperParameterTuningJobObjectiveTypeDef",
        "ParameterRanges": "ParameterRangesTypeDef",
        "TrainingJobEarlyStoppingType": Literal["Off", "Auto"],
        "TuningJobCompletionCriteria": "TuningJobCompletionCriteriaTypeDef",
    },
    total=False,
)


class HyperParameterTuningJobConfigTypeDef(
    _RequiredHyperParameterTuningJobConfigTypeDef, _OptionalHyperParameterTuningJobConfigTypeDef
):
    pass


HyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveTypeDef",
    {"Type": Literal["Maximize", "Minimize"], "MetricName": str},
)

_RequiredHyperParameterTuningJobSummaryTypeDef = TypedDict(
    "_RequiredHyperParameterTuningJobSummaryTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "Strategy": Literal["Bayesian", "Random"],
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
        "WarmStartType": Literal["IdenticalDataAndAlgorithm", "TransferLearning"],
    },
)

ImageConfigTypeDef = TypedDict(
    "ImageConfigTypeDef", {"RepositoryAccessMode": Literal["Platform", "Vpc"]}
)

_RequiredImageTypeDef = TypedDict(
    "_RequiredImageTypeDef",
    {
        "CreationTime": datetime,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": Literal[
            "CREATING",
            "CREATED",
            "CREATE_FAILED",
            "UPDATING",
            "UPDATE_FAILED",
            "DELETING",
            "DELETE_FAILED",
        ],
        "LastModifiedTime": datetime,
    },
)
_OptionalImageTypeDef = TypedDict(
    "_OptionalImageTypeDef",
    {"Description": str, "DisplayName": str, "FailureReason": str},
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
        "ImageVersionStatus": Literal[
            "CREATING", "CREATED", "CREATE_FAILED", "DELETING", "DELETE_FAILED"
        ],
        "LastModifiedTime": datetime,
        "Version": int,
    },
)
_OptionalImageVersionTypeDef = TypedDict(
    "_OptionalImageVersionTypeDef", {"FailureReason": str}, total=False
)


class ImageVersionTypeDef(_RequiredImageVersionTypeDef, _OptionalImageVersionTypeDef):
    pass


InferenceSpecificationTypeDef = TypedDict(
    "InferenceSpecificationTypeDef",
    {
        "Containers": List["ModelPackageContainerDefinitionTypeDef"],
        "SupportedTransformInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
            ]
        ],
        "SupportedRealtimeInferenceInstanceTypes": List[
            Literal[
                "ml.t2.medium",
                "ml.t2.large",
                "ml.t2.xlarge",
                "ml.t2.2xlarge",
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.m5d.large",
                "ml.m5d.xlarge",
                "ml.m5d.2xlarge",
                "ml.m5d.4xlarge",
                "ml.m5d.12xlarge",
                "ml.m5d.24xlarge",
                "ml.c4.large",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.c5.large",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5d.large",
                "ml.c5d.xlarge",
                "ml.c5d.2xlarge",
                "ml.c5d.4xlarge",
                "ml.c5d.9xlarge",
                "ml.c5d.18xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.r5.large",
                "ml.r5.xlarge",
                "ml.r5.2xlarge",
                "ml.r5.4xlarge",
                "ml.r5.12xlarge",
                "ml.r5.24xlarge",
                "ml.r5d.large",
                "ml.r5d.xlarge",
                "ml.r5d.2xlarge",
                "ml.r5d.4xlarge",
                "ml.r5d.12xlarge",
                "ml.r5d.24xlarge",
                "ml.inf1.xlarge",
                "ml.inf1.2xlarge",
                "ml.inf1.6xlarge",
                "ml.inf1.24xlarge",
            ]
        ],
        "SupportedContentTypes": List[str],
        "SupportedResponseMIMETypes": List[str],
    },
)

InputConfigTypeDef = TypedDict(
    "InputConfigTypeDef",
    {
        "S3Uri": str,
        "DataInputConfig": str,
        "Framework": Literal[
            "TENSORFLOW", "KERAS", "MXNET", "ONNX", "PYTORCH", "XGBOOST", "TFLITE", "DARKNET"
        ],
    },
)

IntegerParameterRangeSpecificationTypeDef = TypedDict(
    "IntegerParameterRangeSpecificationTypeDef", {"MinValue": str, "MaxValue": str}
)

_RequiredIntegerParameterRangeTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeTypeDef", {"Name": str, "MinValue": str, "MaxValue": str}
)
_OptionalIntegerParameterRangeTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeTypeDef",
    {"ScalingType": Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]},
    total=False,
)


class IntegerParameterRangeTypeDef(
    _RequiredIntegerParameterRangeTypeDef, _OptionalIntegerParameterRangeTypeDef
):
    pass


JupyterServerAppSettingsTypeDef = TypedDict(
    "JupyterServerAppSettingsTypeDef", {"DefaultResourceSpec": "ResourceSpecTypeDef"}, total=False
)

KernelGatewayAppSettingsTypeDef = TypedDict(
    "KernelGatewayAppSettingsTypeDef",
    {"DefaultResourceSpec": "ResourceSpecTypeDef", "CustomImages": List["CustomImageTypeDef"]},
    total=False,
)

_RequiredKernelGatewayImageConfigTypeDef = TypedDict(
    "_RequiredKernelGatewayImageConfigTypeDef", {"KernelSpecs": List["KernelSpecTypeDef"]}
)
_OptionalKernelGatewayImageConfigTypeDef = TypedDict(
    "_OptionalKernelGatewayImageConfigTypeDef",
    {"FileSystemConfig": "FileSystemConfigTypeDef"},
    total=False,
)


class KernelGatewayImageConfigTypeDef(
    _RequiredKernelGatewayImageConfigTypeDef, _OptionalKernelGatewayImageConfigTypeDef
):
    pass


_RequiredKernelSpecTypeDef = TypedDict("_RequiredKernelSpecTypeDef", {"Name": str})
_OptionalKernelSpecTypeDef = TypedDict(
    "_OptionalKernelSpecTypeDef", {"DisplayName": str}, total=False
)


class KernelSpecTypeDef(_RequiredKernelSpecTypeDef, _OptionalKernelSpecTypeDef):
    pass


LabelCountersForWorkteamTypeDef = TypedDict(
    "LabelCountersForWorkteamTypeDef",
    {"HumanLabeled": int, "PendingHuman": int, "Total": int},
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
    "_RequiredLabelingJobAlgorithmsConfigTypeDef", {"LabelingJobAlgorithmSpecificationArn": str}
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
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
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
    {"JobReferenceCode": str, "WorkRequesterAccountId": str, "CreationTime": datetime},
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
    "_RequiredLabelingJobInputConfigTypeDef", {"DataSource": "LabelingJobDataSourceTypeDef"}
)
_OptionalLabelingJobInputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobInputConfigTypeDef",
    {"DataAttributes": "LabelingJobDataAttributesTypeDef"},
    total=False,
)


class LabelingJobInputConfigTypeDef(
    _RequiredLabelingJobInputConfigTypeDef, _OptionalLabelingJobInputConfigTypeDef
):
    pass


_RequiredLabelingJobOutputConfigTypeDef = TypedDict(
    "_RequiredLabelingJobOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalLabelingJobOutputConfigTypeDef = TypedDict(
    "_OptionalLabelingJobOutputConfigTypeDef", {"KmsKeyId": str, "SnsTopicArn": str}, total=False
)


class LabelingJobOutputConfigTypeDef(
    _RequiredLabelingJobOutputConfigTypeDef, _OptionalLabelingJobOutputConfigTypeDef
):
    pass


_RequiredLabelingJobOutputTypeDef = TypedDict(
    "_RequiredLabelingJobOutputTypeDef", {"OutputDatasetS3Uri": str}
)
_OptionalLabelingJobOutputTypeDef = TypedDict(
    "_OptionalLabelingJobOutputTypeDef",
    {"FinalActiveLearningModelArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class LabelingJobOutputTypeDef(
    _RequiredLabelingJobOutputTypeDef, _OptionalLabelingJobOutputTypeDef
):
    pass


LabelingJobResourceConfigTypeDef = TypedDict(
    "LabelingJobResourceConfigTypeDef", {"VolumeKmsKeyId": str}, total=False
)

LabelingJobS3DataSourceTypeDef = TypedDict("LabelingJobS3DataSourceTypeDef", {"ManifestS3Uri": str})

LabelingJobSnsDataSourceTypeDef = TypedDict("LabelingJobSnsDataSourceTypeDef", {"SnsTopicArn": str})

LabelingJobStoppingConditionsTypeDef = TypedDict(
    "LabelingJobStoppingConditionsTypeDef",
    {"MaxHumanLabeledObjectCount": int, "MaxPercentageOfInputDatasetLabeled": int},
    total=False,
)

_RequiredLabelingJobSummaryTypeDef = TypedDict(
    "_RequiredLabelingJobSummaryTypeDef",
    {
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LabelingJobStatus": Literal[
            "Initializing", "InProgress", "Completed", "Failed", "Stopping", "Stopped"
        ],
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


MemberDefinitionTypeDef = TypedDict(
    "MemberDefinitionTypeDef",
    {
        "CognitoMemberDefinition": "CognitoMemberDefinitionTypeDef",
        "OidcMemberDefinition": "OidcMemberDefinitionTypeDef",
    },
    total=False,
)

MetricDataTypeDef = TypedDict(
    "MetricDataTypeDef", {"MetricName": str, "Value": float, "Timestamp": datetime}, total=False
)

MetricDefinitionTypeDef = TypedDict("MetricDefinitionTypeDef", {"Name": str, "Regex": str})

ModelArtifactsTypeDef = TypedDict("ModelArtifactsTypeDef", {"S3ModelArtifacts": str})

ModelClientConfigTypeDef = TypedDict(
    "ModelClientConfigTypeDef",
    {"InvocationsTimeoutInSeconds": int, "InvocationsMaxRetries": int},
    total=False,
)

_RequiredModelPackageContainerDefinitionTypeDef = TypedDict(
    "_RequiredModelPackageContainerDefinitionTypeDef", {"Image": str}
)
_OptionalModelPackageContainerDefinitionTypeDef = TypedDict(
    "_OptionalModelPackageContainerDefinitionTypeDef",
    {"ContainerHostname": str, "ImageDigest": str, "ModelDataUrl": str, "ProductId": str},
    total=False,
)


class ModelPackageContainerDefinitionTypeDef(
    _RequiredModelPackageContainerDefinitionTypeDef, _OptionalModelPackageContainerDefinitionTypeDef
):
    pass


_RequiredModelPackageStatusDetailsTypeDef = TypedDict(
    "_RequiredModelPackageStatusDetailsTypeDef",
    {"ValidationStatuses": List["ModelPackageStatusItemTypeDef"]},
)
_OptionalModelPackageStatusDetailsTypeDef = TypedDict(
    "_OptionalModelPackageStatusDetailsTypeDef",
    {"ImageScanStatuses": List["ModelPackageStatusItemTypeDef"]},
    total=False,
)


class ModelPackageStatusDetailsTypeDef(
    _RequiredModelPackageStatusDetailsTypeDef, _OptionalModelPackageStatusDetailsTypeDef
):
    pass


_RequiredModelPackageStatusItemTypeDef = TypedDict(
    "_RequiredModelPackageStatusItemTypeDef",
    {"Name": str, "Status": Literal["NotStarted", "InProgress", "Completed", "Failed"]},
)
_OptionalModelPackageStatusItemTypeDef = TypedDict(
    "_OptionalModelPackageStatusItemTypeDef", {"FailureReason": str}, total=False
)


class ModelPackageStatusItemTypeDef(
    _RequiredModelPackageStatusItemTypeDef, _OptionalModelPackageStatusItemTypeDef
):
    pass


_RequiredModelPackageSummaryTypeDef = TypedDict(
    "_RequiredModelPackageSummaryTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
    },
)
_OptionalModelPackageSummaryTypeDef = TypedDict(
    "_OptionalModelPackageSummaryTypeDef", {"ModelPackageDescription": str}, total=False
)


class ModelPackageSummaryTypeDef(
    _RequiredModelPackageSummaryTypeDef, _OptionalModelPackageSummaryTypeDef
):
    pass


ModelPackageValidationProfileTypeDef = TypedDict(
    "ModelPackageValidationProfileTypeDef",
    {"ProfileName": str, "TransformJobDefinition": "TransformJobDefinitionTypeDef"},
)

ModelPackageValidationSpecificationTypeDef = TypedDict(
    "ModelPackageValidationSpecificationTypeDef",
    {"ValidationRole": str, "ValidationProfiles": List["ModelPackageValidationProfileTypeDef"]},
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef", {"ModelName": str, "ModelArn": str, "CreationTime": datetime}
)

_RequiredMonitoringAppSpecificationTypeDef = TypedDict(
    "_RequiredMonitoringAppSpecificationTypeDef", {"ImageUri": str}
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
        "ConstraintsResource": "MonitoringConstraintsResourceTypeDef",
        "StatisticsResource": "MonitoringStatisticsResourceTypeDef",
    },
    total=False,
)

_RequiredMonitoringClusterConfigTypeDef = TypedDict(
    "_RequiredMonitoringClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
    },
)
_OptionalMonitoringClusterConfigTypeDef = TypedDict(
    "_OptionalMonitoringClusterConfigTypeDef", {"VolumeKmsKeyId": str}, total=False
)


class MonitoringClusterConfigTypeDef(
    _RequiredMonitoringClusterConfigTypeDef, _OptionalMonitoringClusterConfigTypeDef
):
    pass


MonitoringConstraintsResourceTypeDef = TypedDict(
    "MonitoringConstraintsResourceTypeDef", {"S3Uri": str}, total=False
)

_RequiredMonitoringExecutionSummaryTypeDef = TypedDict(
    "_RequiredMonitoringExecutionSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "ScheduledTime": datetime,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringExecutionStatus": Literal[
            "Pending",
            "Completed",
            "CompletedWithViolations",
            "InProgress",
            "Failed",
            "Stopping",
            "Stopped",
        ],
    },
)
_OptionalMonitoringExecutionSummaryTypeDef = TypedDict(
    "_OptionalMonitoringExecutionSummaryTypeDef",
    {"ProcessingJobArn": str, "EndpointName": str, "FailureReason": str},
    total=False,
)


class MonitoringExecutionSummaryTypeDef(
    _RequiredMonitoringExecutionSummaryTypeDef, _OptionalMonitoringExecutionSummaryTypeDef
):
    pass


MonitoringInputTypeDef = TypedDict(
    "MonitoringInputTypeDef", {"EndpointInput": "EndpointInputTypeDef"}
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


_RequiredMonitoringOutputConfigTypeDef = TypedDict(
    "_RequiredMonitoringOutputConfigTypeDef", {"MonitoringOutputs": List["MonitoringOutputTypeDef"]}
)
_OptionalMonitoringOutputConfigTypeDef = TypedDict(
    "_OptionalMonitoringOutputConfigTypeDef", {"KmsKeyId": str}, total=False
)


class MonitoringOutputConfigTypeDef(
    _RequiredMonitoringOutputConfigTypeDef, _OptionalMonitoringOutputConfigTypeDef
):
    pass


_RequiredMonitoringOutputTypeDef = TypedDict(
    "_RequiredMonitoringOutputTypeDef", {"S3Output": "MonitoringS3OutputTypeDef"}
)
_OptionalMonitoringOutputTypeDef = TypedDict(
    "_OptionalMonitoringOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class MonitoringOutputTypeDef(_RequiredMonitoringOutputTypeDef, _OptionalMonitoringOutputTypeDef):
    pass


MonitoringResourcesTypeDef = TypedDict(
    "MonitoringResourcesTypeDef", {"ClusterConfig": "MonitoringClusterConfigTypeDef"}
)

_RequiredMonitoringS3OutputTypeDef = TypedDict(
    "_RequiredMonitoringS3OutputTypeDef", {"S3Uri": str, "LocalPath": str}
)
_OptionalMonitoringS3OutputTypeDef = TypedDict(
    "_OptionalMonitoringS3OutputTypeDef",
    {"S3UploadMode": Literal["Continuous", "EndOfJob"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class MonitoringS3OutputTypeDef(
    _RequiredMonitoringS3OutputTypeDef, _OptionalMonitoringS3OutputTypeDef
):
    pass


_RequiredMonitoringScheduleConfigTypeDef = TypedDict(
    "_RequiredMonitoringScheduleConfigTypeDef",
    {"MonitoringJobDefinition": "MonitoringJobDefinitionTypeDef"},
)
_OptionalMonitoringScheduleConfigTypeDef = TypedDict(
    "_OptionalMonitoringScheduleConfigTypeDef",
    {"ScheduleConfig": "ScheduleConfigTypeDef"},
    total=False,
)


class MonitoringScheduleConfigTypeDef(
    _RequiredMonitoringScheduleConfigTypeDef, _OptionalMonitoringScheduleConfigTypeDef
):
    pass


_RequiredMonitoringScheduleSummaryTypeDef = TypedDict(
    "_RequiredMonitoringScheduleSummaryTypeDef",
    {
        "MonitoringScheduleName": str,
        "MonitoringScheduleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleStatus": Literal["Pending", "Failed", "Scheduled", "Stopped"],
    },
)
_OptionalMonitoringScheduleSummaryTypeDef = TypedDict(
    "_OptionalMonitoringScheduleSummaryTypeDef", {"EndpointName": str}, total=False
)


class MonitoringScheduleSummaryTypeDef(
    _RequiredMonitoringScheduleSummaryTypeDef, _OptionalMonitoringScheduleSummaryTypeDef
):
    pass


MonitoringStatisticsResourceTypeDef = TypedDict(
    "MonitoringStatisticsResourceTypeDef", {"S3Uri": str}, total=False
)

MonitoringStoppingConditionTypeDef = TypedDict(
    "MonitoringStoppingConditionTypeDef", {"MaxRuntimeInSeconds": int}
)

NestedFiltersTypeDef = TypedDict(
    "NestedFiltersTypeDef", {"NestedPropertyName": str, "Filters": List["FilterTypeDef"]}
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
    {"NotebookInstanceLifecycleConfigName": str, "NotebookInstanceLifecycleConfigArn": str},
)
_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceLifecycleConfigSummaryTypeDef",
    {"CreationTime": datetime, "LastModifiedTime": datetime},
    total=False,
)


class NotebookInstanceLifecycleConfigSummaryTypeDef(
    _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef,
    _OptionalNotebookInstanceLifecycleConfigSummaryTypeDef,
):
    pass


NotebookInstanceLifecycleHookTypeDef = TypedDict(
    "NotebookInstanceLifecycleHookTypeDef", {"Content": str}, total=False
)

_RequiredNotebookInstanceSummaryTypeDef = TypedDict(
    "_RequiredNotebookInstanceSummaryTypeDef",
    {"NotebookInstanceName": str, "NotebookInstanceArn": str},
)
_OptionalNotebookInstanceSummaryTypeDef = TypedDict(
    "_OptionalNotebookInstanceSummaryTypeDef",
    {
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "Url": str,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
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
    "NotificationConfigurationTypeDef", {"NotificationTopicArn": str}, total=False
)

ObjectiveStatusCountersTypeDef = TypedDict(
    "ObjectiveStatusCountersTypeDef", {"Succeeded": int, "Pending": int, "Failed": int}, total=False
)

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

OidcMemberDefinitionTypeDef = TypedDict("OidcMemberDefinitionTypeDef", {"Groups": List[str]})

_RequiredOutputConfigTypeDef = TypedDict("_RequiredOutputConfigTypeDef", {"S3OutputLocation": str})
_OptionalOutputConfigTypeDef = TypedDict(
    "_OptionalOutputConfigTypeDef",
    {
        "TargetDevice": Literal[
            "lambda",
            "ml_m4",
            "ml_m5",
            "ml_c4",
            "ml_c5",
            "ml_p2",
            "ml_p3",
            "ml_g4dn",
            "ml_inf1",
            "jetson_tx1",
            "jetson_tx2",
            "jetson_nano",
            "jetson_xavier",
            "rasp3b",
            "imx8qm",
            "deeplens",
            "rk3399",
            "rk3288",
            "aisage",
            "sbe_c",
            "qcs605",
            "qcs603",
            "sitara_am57x",
            "amba_cv22",
            "x86_win32",
            "x86_win64",
            "coreml",
        ],
        "TargetPlatform": "TargetPlatformTypeDef",
        "CompilerOptions": str,
    },
    total=False,
)


class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, _OptionalOutputConfigTypeDef):
    pass


_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef", {"S3OutputPath": str}
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef", {"KmsKeyId": str}, total=False
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


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
    },
    total=False,
)

ParentHyperParameterTuningJobTypeDef = TypedDict(
    "ParentHyperParameterTuningJobTypeDef", {"HyperParameterTuningJobName": str}, total=False
)

ParentTypeDef = TypedDict("ParentTypeDef", {"TrialName": str, "ExperimentName": str}, total=False)

_RequiredProcessingClusterConfigTypeDef = TypedDict(
    "_RequiredProcessingClusterConfigTypeDef",
    {
        "InstanceCount": int,
        "InstanceType": Literal[
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.8xlarge",
            "ml.r5.12xlarge",
            "ml.r5.16xlarge",
            "ml.r5.24xlarge",
        ],
        "VolumeSizeInGB": int,
    },
)
_OptionalProcessingClusterConfigTypeDef = TypedDict(
    "_OptionalProcessingClusterConfigTypeDef", {"VolumeKmsKeyId": str}, total=False
)


class ProcessingClusterConfigTypeDef(
    _RequiredProcessingClusterConfigTypeDef, _OptionalProcessingClusterConfigTypeDef
):
    pass


ProcessingInputTypeDef = TypedDict(
    "ProcessingInputTypeDef", {"InputName": str, "S3Input": "ProcessingS3InputTypeDef"}
)

_RequiredProcessingJobSummaryTypeDef = TypedDict(
    "_RequiredProcessingJobSummaryTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingJobArn": str,
        "CreationTime": datetime,
        "ProcessingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
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
        "ProcessingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
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
    "_RequiredProcessingOutputConfigTypeDef", {"Outputs": List["ProcessingOutputTypeDef"]}
)
_OptionalProcessingOutputConfigTypeDef = TypedDict(
    "_OptionalProcessingOutputConfigTypeDef", {"KmsKeyId": str}, total=False
)


class ProcessingOutputConfigTypeDef(
    _RequiredProcessingOutputConfigTypeDef, _OptionalProcessingOutputConfigTypeDef
):
    pass


_RequiredProcessingOutputTypeDef = TypedDict(
    "_RequiredProcessingOutputTypeDef", {"OutputName": str, "S3Output": "ProcessingS3OutputTypeDef"}
)
_OptionalProcessingOutputTypeDef = TypedDict(
    "_OptionalProcessingOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class ProcessingOutputTypeDef(_RequiredProcessingOutputTypeDef, _OptionalProcessingOutputTypeDef):
    pass


ProcessingResourcesTypeDef = TypedDict(
    "ProcessingResourcesTypeDef", {"ClusterConfig": "ProcessingClusterConfigTypeDef"}
)

_RequiredProcessingS3InputTypeDef = TypedDict(
    "_RequiredProcessingS3InputTypeDef",
    {
        "S3Uri": str,
        "LocalPath": str,
        "S3DataType": Literal["ManifestFile", "S3Prefix"],
        "S3InputMode": Literal["Pipe", "File"],
    },
)
_OptionalProcessingS3InputTypeDef = TypedDict(
    "_OptionalProcessingS3InputTypeDef",
    {
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "S3CompressionType": Literal["None", "Gzip"],
    },
    total=False,
)


class ProcessingS3InputTypeDef(
    _RequiredProcessingS3InputTypeDef, _OptionalProcessingS3InputTypeDef
):
    pass


_RequiredProcessingS3OutputTypeDef = TypedDict(
    "_RequiredProcessingS3OutputTypeDef",
    {"S3Uri": str, "LocalPath": str, "S3UploadMode": Literal["Continuous", "EndOfJob"]},
)
_OptionalProcessingS3OutputTypeDef = TypedDict(
    "_OptionalProcessingS3OutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class ProcessingS3OutputTypeDef(
    _RequiredProcessingS3OutputTypeDef, _OptionalProcessingS3OutputTypeDef
):
    pass


ProcessingStoppingConditionTypeDef = TypedDict(
    "ProcessingStoppingConditionTypeDef", {"MaxRuntimeInSeconds": int}
)

_RequiredProductionVariantSummaryTypeDef = TypedDict(
    "_RequiredProductionVariantSummaryTypeDef", {"VariantName": str}
)
_OptionalProductionVariantSummaryTypeDef = TypedDict(
    "_OptionalProductionVariantSummaryTypeDef",
    {
        "DeployedImages": List["DeployedImageTypeDef"],
        "CurrentWeight": float,
        "DesiredWeight": float,
        "CurrentInstanceCount": int,
        "DesiredInstanceCount": int,
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
        "InitialInstanceCount": int,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.m5d.large",
            "ml.m5d.xlarge",
            "ml.m5d.2xlarge",
            "ml.m5d.4xlarge",
            "ml.m5d.12xlarge",
            "ml.m5d.24xlarge",
            "ml.c4.large",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.large",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.r5.large",
            "ml.r5.xlarge",
            "ml.r5.2xlarge",
            "ml.r5.4xlarge",
            "ml.r5.12xlarge",
            "ml.r5.24xlarge",
            "ml.r5d.large",
            "ml.r5d.xlarge",
            "ml.r5d.2xlarge",
            "ml.r5d.4xlarge",
            "ml.r5d.12xlarge",
            "ml.r5d.24xlarge",
            "ml.inf1.xlarge",
            "ml.inf1.2xlarge",
            "ml.inf1.6xlarge",
            "ml.inf1.24xlarge",
        ],
    },
)
_OptionalProductionVariantTypeDef = TypedDict(
    "_OptionalProductionVariantTypeDef",
    {
        "InitialVariantWeight": float,
        "AcceleratorType": Literal[
            "ml.eia1.medium",
            "ml.eia1.large",
            "ml.eia1.xlarge",
            "ml.eia2.medium",
            "ml.eia2.large",
            "ml.eia2.xlarge",
        ],
    },
    total=False,
)


class ProductionVariantTypeDef(
    _RequiredProductionVariantTypeDef, _OptionalProductionVariantTypeDef
):
    pass


PropertyNameQueryTypeDef = TypedDict("PropertyNameQueryTypeDef", {"PropertyNameHint": str})

PropertyNameSuggestionTypeDef = TypedDict(
    "PropertyNameSuggestionTypeDef", {"PropertyName": str}, total=False
)

PublicWorkforceTaskPriceTypeDef = TypedDict(
    "PublicWorkforceTaskPriceTypeDef", {"AmountInUsd": "USDTypeDef"}, total=False
)

RenderingErrorTypeDef = TypedDict("RenderingErrorTypeDef", {"Code": str, "Message": str})

ResolvedAttributesTypeDef = TypedDict(
    "ResolvedAttributesTypeDef",
    {
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": Literal["BinaryClassification", "MulticlassClassification", "Regression"],
        "CompletionCriteria": "AutoMLJobCompletionCriteriaTypeDef",
    },
    total=False,
)

_RequiredResourceConfigTypeDef = TypedDict(
    "_RequiredResourceConfigTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.p3dn.24xlarge",
            "ml.p4d.24xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5n.xlarge",
            "ml.c5n.2xlarge",
            "ml.c5n.4xlarge",
            "ml.c5n.9xlarge",
            "ml.c5n.18xlarge",
        ],
        "InstanceCount": int,
        "VolumeSizeInGB": int,
    },
)
_OptionalResourceConfigTypeDef = TypedDict(
    "_OptionalResourceConfigTypeDef", {"VolumeKmsKeyId": str}, total=False
)


class ResourceConfigTypeDef(_RequiredResourceConfigTypeDef, _OptionalResourceConfigTypeDef):
    pass


ResourceLimitsTypeDef = TypedDict(
    "ResourceLimitsTypeDef", {"MaxNumberOfTrainingJobs": int, "MaxParallelTrainingJobs": int}
)

ResourceSpecTypeDef = TypedDict(
    "ResourceSpecTypeDef",
    {
        "SageMakerImageArn": str,
        "SageMakerImageVersionArn": str,
        "InstanceType": Literal[
            "system",
            "ml.t3.micro",
            "ml.t3.small",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.8xlarge",
            "ml.m5.12xlarge",
            "ml.m5.16xlarge",
            "ml.m5.24xlarge",
            "ml.c5.large",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.12xlarge",
            "ml.c5.18xlarge",
            "ml.c5.24xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.g4dn.xlarge",
            "ml.g4dn.2xlarge",
            "ml.g4dn.4xlarge",
            "ml.g4dn.8xlarge",
            "ml.g4dn.12xlarge",
            "ml.g4dn.16xlarge",
        ],
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3DataSourceTypeDef = TypedDict(
    "_RequiredS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
)
_OptionalS3DataSourceTypeDef = TypedDict(
    "_OptionalS3DataSourceTypeDef",
    {
        "S3DataDistributionType": Literal["FullyReplicated", "ShardedByS3Key"],
        "AttributeNames": List[str],
    },
    total=False,
)


class S3DataSourceTypeDef(_RequiredS3DataSourceTypeDef, _OptionalS3DataSourceTypeDef):
    pass


ScheduleConfigTypeDef = TypedDict("ScheduleConfigTypeDef", {"ScheduleExpression": str})

SearchRecordTypeDef = TypedDict(
    "SearchRecordTypeDef",
    {
        "TrainingJob": "TrainingJobTypeDef",
        "Experiment": "ExperimentTypeDef",
        "Trial": "TrialTypeDef",
        "TrialComponent": "TrialComponentTypeDef",
    },
    total=False,
)

_RequiredSecondaryStatusTransitionTypeDef = TypedDict(
    "_RequiredSecondaryStatusTransitionTypeDef",
    {
        "Status": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "StartTime": datetime,
    },
)
_OptionalSecondaryStatusTransitionTypeDef = TypedDict(
    "_OptionalSecondaryStatusTransitionTypeDef",
    {"EndTime": datetime, "StatusMessage": str},
    total=False,
)


class SecondaryStatusTransitionTypeDef(
    _RequiredSecondaryStatusTransitionTypeDef, _OptionalSecondaryStatusTransitionTypeDef
):
    pass


SharingSettingsTypeDef = TypedDict(
    "SharingSettingsTypeDef",
    {
        "NotebookOutputOption": Literal["Allowed", "Disabled"],
        "S3OutputPath": str,
        "S3KmsKeyId": str,
    },
    total=False,
)

ShuffleConfigTypeDef = TypedDict("ShuffleConfigTypeDef", {"Seed": int})

SourceAlgorithmSpecificationTypeDef = TypedDict(
    "SourceAlgorithmSpecificationTypeDef", {"SourceAlgorithms": List["SourceAlgorithmTypeDef"]}
)

_RequiredSourceAlgorithmTypeDef = TypedDict(
    "_RequiredSourceAlgorithmTypeDef", {"AlgorithmName": str}
)
_OptionalSourceAlgorithmTypeDef = TypedDict(
    "_OptionalSourceAlgorithmTypeDef", {"ModelDataUrl": str}, total=False
)


class SourceAlgorithmTypeDef(_RequiredSourceAlgorithmTypeDef, _OptionalSourceAlgorithmTypeDef):
    pass


SourceIpConfigTypeDef = TypedDict("SourceIpConfigTypeDef", {"Cidrs": List[str]})

StoppingConditionTypeDef = TypedDict(
    "StoppingConditionTypeDef",
    {"MaxRuntimeInSeconds": int, "MaxWaitTimeInSeconds": int},
    total=False,
)

_RequiredSubscribedWorkteamTypeDef = TypedDict(
    "_RequiredSubscribedWorkteamTypeDef", {"WorkteamArn": str}
)
_OptionalSubscribedWorkteamTypeDef = TypedDict(
    "_OptionalSubscribedWorkteamTypeDef",
    {"MarketplaceTitle": str, "SellerName": str, "MarketplaceDescription": str, "ListingId": str},
    total=False,
)


class SubscribedWorkteamTypeDef(
    _RequiredSubscribedWorkteamTypeDef, _OptionalSubscribedWorkteamTypeDef
):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredTargetPlatformTypeDef = TypedDict(
    "_RequiredTargetPlatformTypeDef",
    {
        "Os": Literal["ANDROID", "LINUX"],
        "Arch": Literal["X86_64", "X86", "ARM64", "ARM_EABI", "ARM_EABIHF"],
    },
)
_OptionalTargetPlatformTypeDef = TypedDict(
    "_OptionalTargetPlatformTypeDef",
    {"Accelerator": Literal["INTEL_GRAPHICS", "MALI", "NVIDIA"]},
    total=False,
)


class TargetPlatformTypeDef(_RequiredTargetPlatformTypeDef, _OptionalTargetPlatformTypeDef):
    pass


TensorBoardAppSettingsTypeDef = TypedDict(
    "TensorBoardAppSettingsTypeDef", {"DefaultResourceSpec": "ResourceSpecTypeDef"}, total=False
)

_RequiredTensorBoardOutputConfigTypeDef = TypedDict(
    "_RequiredTensorBoardOutputConfigTypeDef", {"S3OutputPath": str}
)
_OptionalTensorBoardOutputConfigTypeDef = TypedDict(
    "_OptionalTensorBoardOutputConfigTypeDef", {"LocalPath": str}, total=False
)


class TensorBoardOutputConfigTypeDef(
    _RequiredTensorBoardOutputConfigTypeDef, _OptionalTensorBoardOutputConfigTypeDef
):
    pass


_RequiredTrainingJobDefinitionTypeDef = TypedDict(
    "_RequiredTrainingJobDefinitionTypeDef",
    {
        "TrainingInputMode": Literal["Pipe", "File"],
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
    },
)
_OptionalTrainingJobDefinitionTypeDef = TypedDict(
    "_OptionalTrainingJobDefinitionTypeDef", {"HyperParameters": Dict[str, str]}, total=False
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

_RequiredTrainingJobSummaryTypeDef = TypedDict(
    "_RequiredTrainingJobSummaryTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "CreationTime": datetime,
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
)
_OptionalTrainingJobSummaryTypeDef = TypedDict(
    "_OptionalTrainingJobSummaryTypeDef",
    {"TrainingEndTime": datetime, "LastModifiedTime": datetime},
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
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
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
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredTrainingSpecificationTypeDef = TypedDict(
    "_RequiredTrainingSpecificationTypeDef",
    {
        "TrainingImage": str,
        "SupportedTrainingInstanceTypes": List[
            Literal[
                "ml.m4.xlarge",
                "ml.m4.2xlarge",
                "ml.m4.4xlarge",
                "ml.m4.10xlarge",
                "ml.m4.16xlarge",
                "ml.g4dn.xlarge",
                "ml.g4dn.2xlarge",
                "ml.g4dn.4xlarge",
                "ml.g4dn.8xlarge",
                "ml.g4dn.12xlarge",
                "ml.g4dn.16xlarge",
                "ml.m5.large",
                "ml.m5.xlarge",
                "ml.m5.2xlarge",
                "ml.m5.4xlarge",
                "ml.m5.12xlarge",
                "ml.m5.24xlarge",
                "ml.c4.xlarge",
                "ml.c4.2xlarge",
                "ml.c4.4xlarge",
                "ml.c4.8xlarge",
                "ml.p2.xlarge",
                "ml.p2.8xlarge",
                "ml.p2.16xlarge",
                "ml.p3.2xlarge",
                "ml.p3.8xlarge",
                "ml.p3.16xlarge",
                "ml.p3dn.24xlarge",
                "ml.p4d.24xlarge",
                "ml.c5.xlarge",
                "ml.c5.2xlarge",
                "ml.c5.4xlarge",
                "ml.c5.9xlarge",
                "ml.c5.18xlarge",
                "ml.c5n.xlarge",
                "ml.c5n.2xlarge",
                "ml.c5n.4xlarge",
                "ml.c5n.9xlarge",
                "ml.c5n.18xlarge",
            ]
        ],
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
    },
    total=False,
)


class TrainingSpecificationTypeDef(
    _RequiredTrainingSpecificationTypeDef, _OptionalTrainingSpecificationTypeDef
):
    pass


TransformDataSourceTypeDef = TypedDict(
    "TransformDataSourceTypeDef", {"S3DataSource": "TransformS3DataSourceTypeDef"}
)

_RequiredTransformInputTypeDef = TypedDict(
    "_RequiredTransformInputTypeDef", {"DataSource": "TransformDataSourceTypeDef"}
)
_OptionalTransformInputTypeDef = TypedDict(
    "_OptionalTransformInputTypeDef",
    {
        "ContentType": str,
        "CompressionType": Literal["None", "Gzip"],
        "SplitType": Literal["None", "Line", "RecordIO", "TFRecord"],
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
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
    },
    total=False,
)


class TransformJobDefinitionTypeDef(
    _RequiredTransformJobDefinitionTypeDef, _OptionalTransformJobDefinitionTypeDef
):
    pass


_RequiredTransformJobSummaryTypeDef = TypedDict(
    "_RequiredTransformJobSummaryTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "CreationTime": datetime,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
    },
)
_OptionalTransformJobSummaryTypeDef = TypedDict(
    "_OptionalTransformJobSummaryTypeDef",
    {"TransformEndTime": datetime, "LastModifiedTime": datetime, "FailureReason": str},
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
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "FailureReason": str,
        "ModelName": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
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
    },
    total=False,
)

_RequiredTransformOutputTypeDef = TypedDict(
    "_RequiredTransformOutputTypeDef", {"S3OutputPath": str}
)
_OptionalTransformOutputTypeDef = TypedDict(
    "_OptionalTransformOutputTypeDef",
    {
        "Accept": str,
        "AssembleWith": Literal["None", "Line"],
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class TransformOutputTypeDef(_RequiredTransformOutputTypeDef, _OptionalTransformOutputTypeDef):
    pass


_RequiredTransformResourcesTypeDef = TypedDict(
    "_RequiredTransformResourcesTypeDef",
    {
        "InstanceType": Literal[
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.m5.large",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
        ],
        "InstanceCount": int,
    },
)
_OptionalTransformResourcesTypeDef = TypedDict(
    "_OptionalTransformResourcesTypeDef", {"VolumeKmsKeyId": str}, total=False
)


class TransformResourcesTypeDef(
    _RequiredTransformResourcesTypeDef, _OptionalTransformResourcesTypeDef
):
    pass


TransformS3DataSourceTypeDef = TypedDict(
    "TransformS3DataSourceTypeDef",
    {"S3DataType": Literal["ManifestFile", "S3Prefix", "AugmentedManifestFile"], "S3Uri": str},
)

_RequiredTrialComponentArtifactTypeDef = TypedDict(
    "_RequiredTrialComponentArtifactTypeDef", {"Value": str}
)
_OptionalTrialComponentArtifactTypeDef = TypedDict(
    "_OptionalTrialComponentArtifactTypeDef", {"MediaType": str}, total=False
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
    "TrialComponentParameterValueTypeDef", {"StringValue": str, "NumberValue": float}, total=False
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
    "_RequiredTrialComponentSourceTypeDef", {"SourceArn": str}
)
_OptionalTrialComponentSourceTypeDef = TypedDict(
    "_OptionalTrialComponentSourceTypeDef", {"SourceType": str}, total=False
)


class TrialComponentSourceTypeDef(
    _RequiredTrialComponentSourceTypeDef, _OptionalTrialComponentSourceTypeDef
):
    pass


TrialComponentStatusTypeDef = TypedDict(
    "TrialComponentStatusTypeDef",
    {
        "PrimaryStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
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
        "SourceDetail": "TrialComponentSourceDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "Parents": List["ParentTypeDef"],
    },
    total=False,
)

_RequiredTrialSourceTypeDef = TypedDict("_RequiredTrialSourceTypeDef", {"SourceArn": str})
_OptionalTrialSourceTypeDef = TypedDict(
    "_OptionalTrialSourceTypeDef", {"SourceType": str}, total=False
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
        "Tags": List["TagTypeDef"],
        "TrialComponentSummaries": List["TrialComponentSimpleSummaryTypeDef"],
    },
    total=False,
)

TuningJobCompletionCriteriaTypeDef = TypedDict(
    "TuningJobCompletionCriteriaTypeDef", {"TargetObjectiveMetricValue": float}
)

USDTypeDef = TypedDict(
    "USDTypeDef", {"Dollars": int, "Cents": int, "TenthFractionsOfACent": int}, total=False
)

UiConfigTypeDef = TypedDict(
    "UiConfigTypeDef", {"UiTemplateS3Uri": str, "HumanTaskUiArn": str}, total=False
)

UiTemplateInfoTypeDef = TypedDict(
    "UiTemplateInfoTypeDef", {"Url": str, "ContentSha256": str}, total=False
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {"UserProfileArn": str, "UserProfileName": str, "DomainId": str},
    total=False,
)

UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "DomainId": str,
        "UserProfileName": str,
        "Status": Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Updating",
            "Update_Failed",
            "Delete_Failed",
        ],
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
    },
    total=False,
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef", {"SecurityGroupIds": List[str], "Subnets": List[str]}
)

_RequiredWorkforceTypeDef = TypedDict(
    "_RequiredWorkforceTypeDef", {"WorkforceName": str, "WorkforceArn": str}
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
    },
    total=False,
)


class WorkforceTypeDef(_RequiredWorkforceTypeDef, _OptionalWorkforceTypeDef):
    pass


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


AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {"Tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AssociateTrialComponentResponseTypeDef = TypedDict(
    "AssociateTrialComponentResponseTypeDef",
    {"TrialComponentArn": str, "TrialArn": str},
    total=False,
)

_RequiredCreateAlgorithmOutputTypeDef = TypedDict(
    "_RequiredCreateAlgorithmOutputTypeDef", {"AlgorithmArn": str}
)
_OptionalCreateAlgorithmOutputTypeDef = TypedDict(
    "_OptionalCreateAlgorithmOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateAlgorithmOutputTypeDef(
    _RequiredCreateAlgorithmOutputTypeDef, _OptionalCreateAlgorithmOutputTypeDef
):
    pass


CreateAppImageConfigResponseTypeDef = TypedDict(
    "CreateAppImageConfigResponseTypeDef", {"AppImageConfigArn": str}, total=False
)

CreateAppResponseTypeDef = TypedDict("CreateAppResponseTypeDef", {"AppArn": str}, total=False)

CreateAutoMLJobResponseTypeDef = TypedDict("CreateAutoMLJobResponseTypeDef", {"AutoMLJobArn": str})

_RequiredCreateCodeRepositoryOutputTypeDef = TypedDict(
    "_RequiredCreateCodeRepositoryOutputTypeDef", {"CodeRepositoryArn": str}
)
_OptionalCreateCodeRepositoryOutputTypeDef = TypedDict(
    "_OptionalCreateCodeRepositoryOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateCodeRepositoryOutputTypeDef(
    _RequiredCreateCodeRepositoryOutputTypeDef, _OptionalCreateCodeRepositoryOutputTypeDef
):
    pass


CreateCompilationJobResponseTypeDef = TypedDict(
    "CreateCompilationJobResponseTypeDef", {"CompilationJobArn": str}
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef", {"DomainArn": str, "Url": str}, total=False
)

_RequiredCreateEndpointConfigOutputTypeDef = TypedDict(
    "_RequiredCreateEndpointConfigOutputTypeDef", {"EndpointConfigArn": str}
)
_OptionalCreateEndpointConfigOutputTypeDef = TypedDict(
    "_OptionalCreateEndpointConfigOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateEndpointConfigOutputTypeDef(
    _RequiredCreateEndpointConfigOutputTypeDef, _OptionalCreateEndpointConfigOutputTypeDef
):
    pass


_RequiredCreateEndpointOutputTypeDef = TypedDict(
    "_RequiredCreateEndpointOutputTypeDef", {"EndpointArn": str}
)
_OptionalCreateEndpointOutputTypeDef = TypedDict(
    "_OptionalCreateEndpointOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateEndpointOutputTypeDef(
    _RequiredCreateEndpointOutputTypeDef, _OptionalCreateEndpointOutputTypeDef
):
    pass


CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef", {"ExperimentArn": str}, total=False
)

CreateFlowDefinitionResponseTypeDef = TypedDict(
    "CreateFlowDefinitionResponseTypeDef", {"FlowDefinitionArn": str}
)

CreateHumanTaskUiResponseTypeDef = TypedDict(
    "CreateHumanTaskUiResponseTypeDef", {"HumanTaskUiArn": str}
)

CreateHyperParameterTuningJobResponseTypeDef = TypedDict(
    "CreateHyperParameterTuningJobResponseTypeDef", {"HyperParameterTuningJobArn": str}
)

CreateImageResponseTypeDef = TypedDict("CreateImageResponseTypeDef", {"ImageArn": str}, total=False)

CreateImageVersionResponseTypeDef = TypedDict(
    "CreateImageVersionResponseTypeDef", {"ImageVersionArn": str}, total=False
)

CreateLabelingJobResponseTypeDef = TypedDict(
    "CreateLabelingJobResponseTypeDef", {"LabelingJobArn": str}
)

_RequiredCreateModelOutputTypeDef = TypedDict(
    "_RequiredCreateModelOutputTypeDef", {"ModelArn": str}
)
_OptionalCreateModelOutputTypeDef = TypedDict(
    "_OptionalCreateModelOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateModelOutputTypeDef(
    _RequiredCreateModelOutputTypeDef, _OptionalCreateModelOutputTypeDef
):
    pass


_RequiredCreateModelPackageOutputTypeDef = TypedDict(
    "_RequiredCreateModelPackageOutputTypeDef", {"ModelPackageArn": str}
)
_OptionalCreateModelPackageOutputTypeDef = TypedDict(
    "_OptionalCreateModelPackageOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateModelPackageOutputTypeDef(
    _RequiredCreateModelPackageOutputTypeDef, _OptionalCreateModelPackageOutputTypeDef
):
    pass


CreateMonitoringScheduleResponseTypeDef = TypedDict(
    "CreateMonitoringScheduleResponseTypeDef", {"MonitoringScheduleArn": str}
)

CreateNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    {"NotebookInstanceLifecycleConfigArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateNotebookInstanceOutputTypeDef = TypedDict(
    "CreateNotebookInstanceOutputTypeDef",
    {"NotebookInstanceArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreatePresignedDomainUrlResponseTypeDef = TypedDict(
    "CreatePresignedDomainUrlResponseTypeDef", {"AuthorizedUrl": str}, total=False
)

CreatePresignedNotebookInstanceUrlOutputTypeDef = TypedDict(
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    {"AuthorizedUrl": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateProcessingJobResponseTypeDef = TypedDict(
    "CreateProcessingJobResponseTypeDef", {"ProcessingJobArn": str}
)

CreateTrainingJobResponseTypeDef = TypedDict(
    "CreateTrainingJobResponseTypeDef", {"TrainingJobArn": str}
)

CreateTransformJobResponseTypeDef = TypedDict(
    "CreateTransformJobResponseTypeDef", {"TransformJobArn": str}
)

CreateTrialComponentResponseTypeDef = TypedDict(
    "CreateTrialComponentResponseTypeDef", {"TrialComponentArn": str}, total=False
)

CreateTrialResponseTypeDef = TypedDict("CreateTrialResponseTypeDef", {"TrialArn": str}, total=False)

CreateUserProfileResponseTypeDef = TypedDict(
    "CreateUserProfileResponseTypeDef", {"UserProfileArn": str}, total=False
)

CreateWorkforceResponseTypeDef = TypedDict("CreateWorkforceResponseTypeDef", {"WorkforceArn": str})

CreateWorkteamResponseTypeDef = TypedDict(
    "CreateWorkteamResponseTypeDef", {"WorkteamArn": str}, total=False
)

DeleteExperimentResponseTypeDef = TypedDict(
    "DeleteExperimentResponseTypeDef", {"ExperimentArn": str}, total=False
)

DeleteTrialComponentResponseTypeDef = TypedDict(
    "DeleteTrialComponentResponseTypeDef", {"TrialComponentArn": str}, total=False
)

DeleteTrialResponseTypeDef = TypedDict("DeleteTrialResponseTypeDef", {"TrialArn": str}, total=False)

DeleteWorkteamResponseTypeDef = TypedDict("DeleteWorkteamResponseTypeDef", {"Success": bool})

_RequiredDescribeAlgorithmOutputTypeDef = TypedDict(
    "_RequiredDescribeAlgorithmOutputTypeDef",
    {
        "AlgorithmName": str,
        "AlgorithmArn": str,
        "CreationTime": datetime,
        "TrainingSpecification": "TrainingSpecificationTypeDef",
        "AlgorithmStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
        "AlgorithmStatusDetails": "AlgorithmStatusDetailsTypeDef",
    },
)
_OptionalDescribeAlgorithmOutputTypeDef = TypedDict(
    "_OptionalDescribeAlgorithmOutputTypeDef",
    {
        "AlgorithmDescription": str,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "ValidationSpecification": "AlgorithmValidationSpecificationTypeDef",
        "ProductId": str,
        "CertifyForMarketplace": bool,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeAlgorithmOutputTypeDef(
    _RequiredDescribeAlgorithmOutputTypeDef, _OptionalDescribeAlgorithmOutputTypeDef
):
    pass


DescribeAppImageConfigResponseTypeDef = TypedDict(
    "DescribeAppImageConfigResponseTypeDef",
    {
        "AppImageConfigArn": str,
        "AppImageConfigName": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "KernelGatewayImageConfig": "KernelGatewayImageConfigTypeDef",
    },
    total=False,
)

DescribeAppResponseTypeDef = TypedDict(
    "DescribeAppResponseTypeDef",
    {
        "AppArn": str,
        "AppType": Literal["JupyterServer", "KernelGateway", "TensorBoard"],
        "AppName": str,
        "DomainId": str,
        "UserProfileName": str,
        "Status": Literal["Deleted", "Deleting", "Failed", "InService", "Pending"],
        "LastHealthCheckTimestamp": datetime,
        "LastUserActivityTimestamp": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "ResourceSpec": "ResourceSpecTypeDef",
    },
    total=False,
)

_RequiredDescribeAutoMLJobResponseTypeDef = TypedDict(
    "_RequiredDescribeAutoMLJobResponseTypeDef",
    {
        "AutoMLJobName": str,
        "AutoMLJobArn": str,
        "InputDataConfig": List["AutoMLChannelTypeDef"],
        "OutputDataConfig": "AutoMLOutputDataConfigTypeDef",
        "RoleArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "AutoMLJobStatus": Literal["Completed", "InProgress", "Failed", "Stopped", "Stopping"],
        "AutoMLJobSecondaryStatus": Literal[
            "Starting",
            "AnalyzingData",
            "FeatureEngineering",
            "ModelTuning",
            "MaxCandidatesReached",
            "Failed",
            "Stopped",
            "MaxAutoMLJobRuntimeReached",
            "Stopping",
            "CandidateDefinitionsGenerated",
        ],
    },
)
_OptionalDescribeAutoMLJobResponseTypeDef = TypedDict(
    "_OptionalDescribeAutoMLJobResponseTypeDef",
    {
        "AutoMLJobObjective": "AutoMLJobObjectiveTypeDef",
        "ProblemType": Literal["BinaryClassification", "MulticlassClassification", "Regression"],
        "AutoMLJobConfig": "AutoMLJobConfigTypeDef",
        "EndTime": datetime,
        "FailureReason": str,
        "BestCandidate": "AutoMLCandidateTypeDef",
        "GenerateCandidateDefinitionsOnly": bool,
        "AutoMLJobArtifacts": "AutoMLJobArtifactsTypeDef",
        "ResolvedAttributes": "ResolvedAttributesTypeDef",
    },
    total=False,
)


class DescribeAutoMLJobResponseTypeDef(
    _RequiredDescribeAutoMLJobResponseTypeDef, _OptionalDescribeAutoMLJobResponseTypeDef
):
    pass


_RequiredDescribeCodeRepositoryOutputTypeDef = TypedDict(
    "_RequiredDescribeCodeRepositoryOutputTypeDef",
    {
        "CodeRepositoryName": str,
        "CodeRepositoryArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalDescribeCodeRepositoryOutputTypeDef = TypedDict(
    "_OptionalDescribeCodeRepositoryOutputTypeDef",
    {"GitConfig": "GitConfigTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeCodeRepositoryOutputTypeDef(
    _RequiredDescribeCodeRepositoryOutputTypeDef, _OptionalDescribeCodeRepositoryOutputTypeDef
):
    pass


_RequiredDescribeCompilationJobResponseTypeDef = TypedDict(
    "_RequiredDescribeCompilationJobResponseTypeDef",
    {
        "CompilationJobName": str,
        "CompilationJobArn": str,
        "CompilationJobStatus": Literal[
            "INPROGRESS", "COMPLETED", "FAILED", "STARTING", "STOPPING", "STOPPED"
        ],
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "RoleArn": str,
        "InputConfig": "InputConfigTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
    },
)
_OptionalDescribeCompilationJobResponseTypeDef = TypedDict(
    "_OptionalDescribeCompilationJobResponseTypeDef",
    {"CompilationStartTime": datetime, "CompilationEndTime": datetime},
    total=False,
)


class DescribeCompilationJobResponseTypeDef(
    _RequiredDescribeCompilationJobResponseTypeDef, _OptionalDescribeCompilationJobResponseTypeDef
):
    pass


DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainArn": str,
        "DomainId": str,
        "DomainName": str,
        "HomeEfsFileSystemId": str,
        "SingleSignOnManagedApplicationInstanceId": str,
        "Status": Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Updating",
            "Update_Failed",
            "Delete_Failed",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "AuthMode": Literal["SSO", "IAM"],
        "DefaultUserSettings": "UserSettingsTypeDef",
        "AppNetworkAccessType": Literal["PublicInternetOnly", "VpcOnly"],
        "HomeEfsFileSystemKmsKeyId": str,
        "SubnetIds": List[str],
        "Url": str,
        "VpcId": str,
        "KmsKeyId": str,
    },
    total=False,
)

_RequiredDescribeEndpointConfigOutputTypeDef = TypedDict(
    "_RequiredDescribeEndpointConfigOutputTypeDef",
    {
        "EndpointConfigName": str,
        "EndpointConfigArn": str,
        "ProductionVariants": List["ProductionVariantTypeDef"],
        "CreationTime": datetime,
    },
)
_OptionalDescribeEndpointConfigOutputTypeDef = TypedDict(
    "_OptionalDescribeEndpointConfigOutputTypeDef",
    {
        "DataCaptureConfig": "DataCaptureConfigTypeDef",
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeEndpointConfigOutputTypeDef(
    _RequiredDescribeEndpointConfigOutputTypeDef, _OptionalDescribeEndpointConfigOutputTypeDef
):
    pass


_RequiredDescribeEndpointOutputTypeDef = TypedDict(
    "_RequiredDescribeEndpointOutputTypeDef",
    {
        "EndpointName": str,
        "EndpointArn": str,
        "EndpointConfigName": str,
        "EndpointStatus": Literal[
            "OutOfService",
            "Creating",
            "Updating",
            "SystemUpdating",
            "RollingBack",
            "InService",
            "Deleting",
            "Failed",
        ],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
)
_OptionalDescribeEndpointOutputTypeDef = TypedDict(
    "_OptionalDescribeEndpointOutputTypeDef",
    {
        "ProductionVariants": List["ProductionVariantSummaryTypeDef"],
        "DataCaptureConfig": "DataCaptureConfigSummaryTypeDef",
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeEndpointOutputTypeDef(
    _RequiredDescribeEndpointOutputTypeDef, _OptionalDescribeEndpointOutputTypeDef
):
    pass


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
    },
    total=False,
)

_RequiredDescribeFlowDefinitionResponseTypeDef = TypedDict(
    "_RequiredDescribeFlowDefinitionResponseTypeDef",
    {
        "FlowDefinitionArn": str,
        "FlowDefinitionName": str,
        "FlowDefinitionStatus": Literal["Initializing", "Active", "Failed", "Deleting"],
        "CreationTime": datetime,
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "OutputConfig": "FlowDefinitionOutputConfigTypeDef",
        "RoleArn": str,
    },
)
_OptionalDescribeFlowDefinitionResponseTypeDef = TypedDict(
    "_OptionalDescribeFlowDefinitionResponseTypeDef",
    {
        "HumanLoopRequestSource": "HumanLoopRequestSourceTypeDef",
        "HumanLoopActivationConfig": "HumanLoopActivationConfigTypeDef",
        "FailureReason": str,
    },
    total=False,
)


class DescribeFlowDefinitionResponseTypeDef(
    _RequiredDescribeFlowDefinitionResponseTypeDef, _OptionalDescribeFlowDefinitionResponseTypeDef
):
    pass


_RequiredDescribeHumanTaskUiResponseTypeDef = TypedDict(
    "_RequiredDescribeHumanTaskUiResponseTypeDef",
    {
        "HumanTaskUiArn": str,
        "HumanTaskUiName": str,
        "CreationTime": datetime,
        "UiTemplate": "UiTemplateInfoTypeDef",
    },
)
_OptionalDescribeHumanTaskUiResponseTypeDef = TypedDict(
    "_OptionalDescribeHumanTaskUiResponseTypeDef",
    {"HumanTaskUiStatus": Literal["Active", "Deleting"]},
    total=False,
)


class DescribeHumanTaskUiResponseTypeDef(
    _RequiredDescribeHumanTaskUiResponseTypeDef, _OptionalDescribeHumanTaskUiResponseTypeDef
):
    pass


_RequiredDescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_RequiredDescribeHyperParameterTuningJobResponseTypeDef",
    {
        "HyperParameterTuningJobName": str,
        "HyperParameterTuningJobArn": str,
        "HyperParameterTuningJobConfig": "HyperParameterTuningJobConfigTypeDef",
        "HyperParameterTuningJobStatus": Literal[
            "Completed", "InProgress", "Failed", "Stopped", "Stopping"
        ],
        "CreationTime": datetime,
        "TrainingJobStatusCounters": "TrainingJobStatusCountersTypeDef",
        "ObjectiveStatusCounters": "ObjectiveStatusCountersTypeDef",
    },
)
_OptionalDescribeHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_OptionalDescribeHyperParameterTuningJobResponseTypeDef",
    {
        "TrainingJobDefinition": "HyperParameterTrainingJobDefinitionTypeDef",
        "TrainingJobDefinitions": List["HyperParameterTrainingJobDefinitionTypeDef"],
        "HyperParameterTuningEndTime": datetime,
        "LastModifiedTime": datetime,
        "BestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "OverallBestTrainingJob": "HyperParameterTrainingJobSummaryTypeDef",
        "WarmStartConfig": "HyperParameterTuningJobWarmStartConfigTypeDef",
        "FailureReason": str,
    },
    total=False,
)


class DescribeHyperParameterTuningJobResponseTypeDef(
    _RequiredDescribeHyperParameterTuningJobResponseTypeDef,
    _OptionalDescribeHyperParameterTuningJobResponseTypeDef,
):
    pass


DescribeImageResponseTypeDef = TypedDict(
    "DescribeImageResponseTypeDef",
    {
        "CreationTime": datetime,
        "Description": str,
        "DisplayName": str,
        "FailureReason": str,
        "ImageArn": str,
        "ImageName": str,
        "ImageStatus": Literal[
            "CREATING",
            "CREATED",
            "CREATE_FAILED",
            "UPDATING",
            "UPDATE_FAILED",
            "DELETING",
            "DELETE_FAILED",
        ],
        "LastModifiedTime": datetime,
        "RoleArn": str,
    },
    total=False,
)

DescribeImageVersionResponseTypeDef = TypedDict(
    "DescribeImageVersionResponseTypeDef",
    {
        "BaseImage": str,
        "ContainerImage": str,
        "CreationTime": datetime,
        "FailureReason": str,
        "ImageArn": str,
        "ImageVersionArn": str,
        "ImageVersionStatus": Literal[
            "CREATING", "CREATED", "CREATE_FAILED", "DELETING", "DELETE_FAILED"
        ],
        "LastModifiedTime": datetime,
        "Version": int,
    },
    total=False,
)

_RequiredDescribeLabelingJobResponseTypeDef = TypedDict(
    "_RequiredDescribeLabelingJobResponseTypeDef",
    {
        "LabelingJobStatus": Literal[
            "Initializing", "InProgress", "Completed", "Failed", "Stopping", "Stopped"
        ],
        "LabelCounters": "LabelCountersTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "JobReferenceCode": str,
        "LabelingJobName": str,
        "LabelingJobArn": str,
        "InputConfig": "LabelingJobInputConfigTypeDef",
        "OutputConfig": "LabelingJobOutputConfigTypeDef",
        "RoleArn": str,
        "HumanTaskConfig": "HumanTaskConfigTypeDef",
    },
)
_OptionalDescribeLabelingJobResponseTypeDef = TypedDict(
    "_OptionalDescribeLabelingJobResponseTypeDef",
    {
        "FailureReason": str,
        "LabelAttributeName": str,
        "LabelCategoryConfigS3Uri": str,
        "StoppingConditions": "LabelingJobStoppingConditionsTypeDef",
        "LabelingJobAlgorithmsConfig": "LabelingJobAlgorithmsConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "LabelingJobOutput": "LabelingJobOutputTypeDef",
    },
    total=False,
)


class DescribeLabelingJobResponseTypeDef(
    _RequiredDescribeLabelingJobResponseTypeDef, _OptionalDescribeLabelingJobResponseTypeDef
):
    pass


_RequiredDescribeModelOutputTypeDef = TypedDict(
    "_RequiredDescribeModelOutputTypeDef",
    {"ModelName": str, "ExecutionRoleArn": str, "CreationTime": datetime, "ModelArn": str},
)
_OptionalDescribeModelOutputTypeDef = TypedDict(
    "_OptionalDescribeModelOutputTypeDef",
    {
        "PrimaryContainer": "ContainerDefinitionTypeDef",
        "Containers": List["ContainerDefinitionTypeDef"],
        "VpcConfig": "VpcConfigTypeDef",
        "EnableNetworkIsolation": bool,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeModelOutputTypeDef(
    _RequiredDescribeModelOutputTypeDef, _OptionalDescribeModelOutputTypeDef
):
    pass


_RequiredDescribeModelPackageOutputTypeDef = TypedDict(
    "_RequiredDescribeModelPackageOutputTypeDef",
    {
        "ModelPackageName": str,
        "ModelPackageArn": str,
        "CreationTime": datetime,
        "ModelPackageStatus": Literal["Pending", "InProgress", "Completed", "Failed", "Deleting"],
        "ModelPackageStatusDetails": "ModelPackageStatusDetailsTypeDef",
    },
)
_OptionalDescribeModelPackageOutputTypeDef = TypedDict(
    "_OptionalDescribeModelPackageOutputTypeDef",
    {
        "ModelPackageDescription": str,
        "InferenceSpecification": "InferenceSpecificationTypeDef",
        "SourceAlgorithmSpecification": "SourceAlgorithmSpecificationTypeDef",
        "ValidationSpecification": "ModelPackageValidationSpecificationTypeDef",
        "CertifyForMarketplace": bool,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeModelPackageOutputTypeDef(
    _RequiredDescribeModelPackageOutputTypeDef, _OptionalDescribeModelPackageOutputTypeDef
):
    pass


_RequiredDescribeMonitoringScheduleResponseTypeDef = TypedDict(
    "_RequiredDescribeMonitoringScheduleResponseTypeDef",
    {
        "MonitoringScheduleArn": str,
        "MonitoringScheduleName": str,
        "MonitoringScheduleStatus": Literal["Pending", "Failed", "Scheduled", "Stopped"],
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleConfig": "MonitoringScheduleConfigTypeDef",
    },
)
_OptionalDescribeMonitoringScheduleResponseTypeDef = TypedDict(
    "_OptionalDescribeMonitoringScheduleResponseTypeDef",
    {
        "FailureReason": str,
        "EndpointName": str,
        "LastMonitoringExecutionSummary": "MonitoringExecutionSummaryTypeDef",
    },
    total=False,
)


class DescribeMonitoringScheduleResponseTypeDef(
    _RequiredDescribeMonitoringScheduleResponseTypeDef,
    _OptionalDescribeMonitoringScheduleResponseTypeDef,
):
    pass


DescribeNotebookInstanceLifecycleConfigOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    {
        "NotebookInstanceLifecycleConfigArn": str,
        "NotebookInstanceLifecycleConfigName": str,
        "OnCreate": List["NotebookInstanceLifecycleHookTypeDef"],
        "OnStart": List["NotebookInstanceLifecycleHookTypeDef"],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeNotebookInstanceOutputTypeDef = TypedDict(
    "DescribeNotebookInstanceOutputTypeDef",
    {
        "NotebookInstanceArn": str,
        "NotebookInstanceName": str,
        "NotebookInstanceStatus": Literal[
            "Pending", "InService", "Stopping", "Stopped", "Failed", "Deleting", "Updating"
        ],
        "FailureReason": str,
        "Url": str,
        "InstanceType": Literal[
            "ml.t2.medium",
            "ml.t2.large",
            "ml.t2.xlarge",
            "ml.t2.2xlarge",
            "ml.t3.medium",
            "ml.t3.large",
            "ml.t3.xlarge",
            "ml.t3.2xlarge",
            "ml.m4.xlarge",
            "ml.m4.2xlarge",
            "ml.m4.4xlarge",
            "ml.m4.10xlarge",
            "ml.m4.16xlarge",
            "ml.m5.xlarge",
            "ml.m5.2xlarge",
            "ml.m5.4xlarge",
            "ml.m5.12xlarge",
            "ml.m5.24xlarge",
            "ml.c4.xlarge",
            "ml.c4.2xlarge",
            "ml.c4.4xlarge",
            "ml.c4.8xlarge",
            "ml.c5.xlarge",
            "ml.c5.2xlarge",
            "ml.c5.4xlarge",
            "ml.c5.9xlarge",
            "ml.c5.18xlarge",
            "ml.c5d.xlarge",
            "ml.c5d.2xlarge",
            "ml.c5d.4xlarge",
            "ml.c5d.9xlarge",
            "ml.c5d.18xlarge",
            "ml.p2.xlarge",
            "ml.p2.8xlarge",
            "ml.p2.16xlarge",
            "ml.p3.2xlarge",
            "ml.p3.8xlarge",
            "ml.p3.16xlarge",
        ],
        "SubnetId": str,
        "SecurityGroups": List[str],
        "RoleArn": str,
        "KmsKeyId": str,
        "NetworkInterfaceId": str,
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "NotebookInstanceLifecycleConfigName": str,
        "DirectInternetAccess": Literal["Enabled", "Disabled"],
        "VolumeSizeInGB": int,
        "AcceleratorTypes": List[
            Literal[
                "ml.eia1.medium",
                "ml.eia1.large",
                "ml.eia1.xlarge",
                "ml.eia2.medium",
                "ml.eia2.large",
                "ml.eia2.xlarge",
            ]
        ],
        "DefaultCodeRepository": str,
        "AdditionalCodeRepositories": List[str],
        "RootAccess": Literal["Enabled", "Disabled"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredDescribeProcessingJobResponseTypeDef = TypedDict(
    "_RequiredDescribeProcessingJobResponseTypeDef",
    {
        "ProcessingJobName": str,
        "ProcessingResources": "ProcessingResourcesTypeDef",
        "AppSpecification": "AppSpecificationTypeDef",
        "ProcessingJobArn": str,
        "ProcessingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "CreationTime": datetime,
    },
)
_OptionalDescribeProcessingJobResponseTypeDef = TypedDict(
    "_OptionalDescribeProcessingJobResponseTypeDef",
    {
        "ProcessingInputs": List["ProcessingInputTypeDef"],
        "ProcessingOutputConfig": "ProcessingOutputConfigTypeDef",
        "StoppingCondition": "ProcessingStoppingConditionTypeDef",
        "Environment": Dict[str, str],
        "NetworkConfig": "NetworkConfigTypeDef",
        "RoleArn": str,
        "ExperimentConfig": "ExperimentConfigTypeDef",
        "ExitMessage": str,
        "FailureReason": str,
        "ProcessingEndTime": datetime,
        "ProcessingStartTime": datetime,
        "LastModifiedTime": datetime,
        "MonitoringScheduleArn": str,
        "AutoMLJobArn": str,
        "TrainingJobArn": str,
    },
    total=False,
)


class DescribeProcessingJobResponseTypeDef(
    _RequiredDescribeProcessingJobResponseTypeDef, _OptionalDescribeProcessingJobResponseTypeDef
):
    pass


DescribeSubscribedWorkteamResponseTypeDef = TypedDict(
    "DescribeSubscribedWorkteamResponseTypeDef", {"SubscribedWorkteam": "SubscribedWorkteamTypeDef"}
)

_RequiredDescribeTrainingJobResponseTypeDef = TypedDict(
    "_RequiredDescribeTrainingJobResponseTypeDef",
    {
        "TrainingJobName": str,
        "TrainingJobArn": str,
        "ModelArtifacts": "ModelArtifactsTypeDef",
        "TrainingJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "SecondaryStatus": Literal[
            "Starting",
            "LaunchingMLInstances",
            "PreparingTrainingStack",
            "Downloading",
            "DownloadingTrainingImage",
            "Training",
            "Uploading",
            "Stopping",
            "Stopped",
            "MaxRuntimeExceeded",
            "Completed",
            "Failed",
            "Interrupted",
            "MaxWaitTimeExceeded",
        ],
        "AlgorithmSpecification": "AlgorithmSpecificationTypeDef",
        "ResourceConfig": "ResourceConfigTypeDef",
        "StoppingCondition": "StoppingConditionTypeDef",
        "CreationTime": datetime,
    },
)
_OptionalDescribeTrainingJobResponseTypeDef = TypedDict(
    "_OptionalDescribeTrainingJobResponseTypeDef",
    {
        "TuningJobArn": str,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "FailureReason": str,
        "HyperParameters": Dict[str, str],
        "RoleArn": str,
        "InputDataConfig": List["ChannelTypeDef"],
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "VpcConfig": "VpcConfigTypeDef",
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
    },
    total=False,
)


class DescribeTrainingJobResponseTypeDef(
    _RequiredDescribeTrainingJobResponseTypeDef, _OptionalDescribeTrainingJobResponseTypeDef
):
    pass


_RequiredDescribeTransformJobResponseTypeDef = TypedDict(
    "_RequiredDescribeTransformJobResponseTypeDef",
    {
        "TransformJobName": str,
        "TransformJobArn": str,
        "TransformJobStatus": Literal["InProgress", "Completed", "Failed", "Stopping", "Stopped"],
        "ModelName": str,
        "TransformInput": "TransformInputTypeDef",
        "TransformResources": "TransformResourcesTypeDef",
        "CreationTime": datetime,
    },
)
_OptionalDescribeTransformJobResponseTypeDef = TypedDict(
    "_OptionalDescribeTransformJobResponseTypeDef",
    {
        "FailureReason": str,
        "MaxConcurrentTransforms": int,
        "ModelClientConfig": "ModelClientConfigTypeDef",
        "MaxPayloadInMB": int,
        "BatchStrategy": Literal["MultiRecord", "SingleRecord"],
        "Environment": Dict[str, str],
        "TransformOutput": "TransformOutputTypeDef",
        "TransformStartTime": datetime,
        "TransformEndTime": datetime,
        "LabelingJobArn": str,
        "AutoMLJobArn": str,
        "DataProcessing": "DataProcessingTypeDef",
        "ExperimentConfig": "ExperimentConfigTypeDef",
    },
    total=False,
)


class DescribeTransformJobResponseTypeDef(
    _RequiredDescribeTransformJobResponseTypeDef, _OptionalDescribeTransformJobResponseTypeDef
):
    pass


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
        "Metrics": List["TrialComponentMetricSummaryTypeDef"],
    },
    total=False,
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
    },
    total=False,
)

DescribeUserProfileResponseTypeDef = TypedDict(
    "DescribeUserProfileResponseTypeDef",
    {
        "DomainId": str,
        "UserProfileArn": str,
        "UserProfileName": str,
        "HomeEfsFileSystemUid": str,
        "Status": Literal[
            "Deleting",
            "Failed",
            "InService",
            "Pending",
            "Updating",
            "Update_Failed",
            "Delete_Failed",
        ],
        "LastModifiedTime": datetime,
        "CreationTime": datetime,
        "FailureReason": str,
        "SingleSignOnUserIdentifier": str,
        "SingleSignOnUserValue": str,
        "UserSettings": "UserSettingsTypeDef",
    },
    total=False,
)

DescribeWorkforceResponseTypeDef = TypedDict(
    "DescribeWorkforceResponseTypeDef", {"Workforce": "WorkforceTypeDef"}
)

DescribeWorkteamResponseTypeDef = TypedDict(
    "DescribeWorkteamResponseTypeDef", {"Workteam": "WorkteamTypeDef"}
)

_RequiredDesiredWeightAndCapacityTypeDef = TypedDict(
    "_RequiredDesiredWeightAndCapacityTypeDef", {"VariantName": str}
)
_OptionalDesiredWeightAndCapacityTypeDef = TypedDict(
    "_OptionalDesiredWeightAndCapacityTypeDef",
    {"DesiredWeight": float, "DesiredInstanceCount": int},
    total=False,
)


class DesiredWeightAndCapacityTypeDef(
    _RequiredDesiredWeightAndCapacityTypeDef, _OptionalDesiredWeightAndCapacityTypeDef
):
    pass


SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NestedFilters": List["NestedFiltersTypeDef"],
        "SubExpressions": List[Dict[str, Any]],
        "Operator": Literal["And", "Or"],
    },
    total=False,
)

DisassociateTrialComponentResponseTypeDef = TypedDict(
    "DisassociateTrialComponentResponseTypeDef",
    {"TrialComponentArn": str, "TrialArn": str},
    total=False,
)

GetSearchSuggestionsResponseTypeDef = TypedDict(
    "GetSearchSuggestionsResponseTypeDef",
    {"PropertyNameSuggestions": List["PropertyNameSuggestionTypeDef"]},
    total=False,
)

GitConfigForUpdateTypeDef = TypedDict("GitConfigForUpdateTypeDef", {"SecretArn": str}, total=False)

_RequiredListAlgorithmsOutputTypeDef = TypedDict(
    "_RequiredListAlgorithmsOutputTypeDef",
    {"AlgorithmSummaryList": List["AlgorithmSummaryTypeDef"]},
)
_OptionalListAlgorithmsOutputTypeDef = TypedDict(
    "_OptionalListAlgorithmsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListAlgorithmsOutputTypeDef(
    _RequiredListAlgorithmsOutputTypeDef, _OptionalListAlgorithmsOutputTypeDef
):
    pass


ListAppImageConfigsResponseTypeDef = TypedDict(
    "ListAppImageConfigsResponseTypeDef",
    {"NextToken": str, "AppImageConfigs": List["AppImageConfigDetailsTypeDef"]},
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef", {"Apps": List["AppDetailsTypeDef"], "NextToken": str}, total=False
)

_RequiredListAutoMLJobsResponseTypeDef = TypedDict(
    "_RequiredListAutoMLJobsResponseTypeDef",
    {"AutoMLJobSummaries": List["AutoMLJobSummaryTypeDef"]},
)
_OptionalListAutoMLJobsResponseTypeDef = TypedDict(
    "_OptionalListAutoMLJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListAutoMLJobsResponseTypeDef(
    _RequiredListAutoMLJobsResponseTypeDef, _OptionalListAutoMLJobsResponseTypeDef
):
    pass


_RequiredListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "_RequiredListCandidatesForAutoMLJobResponseTypeDef",
    {"Candidates": List["AutoMLCandidateTypeDef"]},
)
_OptionalListCandidatesForAutoMLJobResponseTypeDef = TypedDict(
    "_OptionalListCandidatesForAutoMLJobResponseTypeDef", {"NextToken": str}, total=False
)


class ListCandidatesForAutoMLJobResponseTypeDef(
    _RequiredListCandidatesForAutoMLJobResponseTypeDef,
    _OptionalListCandidatesForAutoMLJobResponseTypeDef,
):
    pass


_RequiredListCodeRepositoriesOutputTypeDef = TypedDict(
    "_RequiredListCodeRepositoriesOutputTypeDef",
    {"CodeRepositorySummaryList": List["CodeRepositorySummaryTypeDef"]},
)
_OptionalListCodeRepositoriesOutputTypeDef = TypedDict(
    "_OptionalListCodeRepositoriesOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListCodeRepositoriesOutputTypeDef(
    _RequiredListCodeRepositoriesOutputTypeDef, _OptionalListCodeRepositoriesOutputTypeDef
):
    pass


_RequiredListCompilationJobsResponseTypeDef = TypedDict(
    "_RequiredListCompilationJobsResponseTypeDef",
    {"CompilationJobSummaries": List["CompilationJobSummaryTypeDef"]},
)
_OptionalListCompilationJobsResponseTypeDef = TypedDict(
    "_OptionalListCompilationJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListCompilationJobsResponseTypeDef(
    _RequiredListCompilationJobsResponseTypeDef, _OptionalListCompilationJobsResponseTypeDef
):
    pass


ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {"Domains": List["DomainDetailsTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListEndpointConfigsOutputTypeDef = TypedDict(
    "_RequiredListEndpointConfigsOutputTypeDef",
    {"EndpointConfigs": List["EndpointConfigSummaryTypeDef"]},
)
_OptionalListEndpointConfigsOutputTypeDef = TypedDict(
    "_OptionalListEndpointConfigsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListEndpointConfigsOutputTypeDef(
    _RequiredListEndpointConfigsOutputTypeDef, _OptionalListEndpointConfigsOutputTypeDef
):
    pass


_RequiredListEndpointsOutputTypeDef = TypedDict(
    "_RequiredListEndpointsOutputTypeDef", {"Endpoints": List["EndpointSummaryTypeDef"]}
)
_OptionalListEndpointsOutputTypeDef = TypedDict(
    "_OptionalListEndpointsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListEndpointsOutputTypeDef(
    _RequiredListEndpointsOutputTypeDef, _OptionalListEndpointsOutputTypeDef
):
    pass


ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {"ExperimentSummaries": List["ExperimentSummaryTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListFlowDefinitionsResponseTypeDef = TypedDict(
    "_RequiredListFlowDefinitionsResponseTypeDef",
    {"FlowDefinitionSummaries": List["FlowDefinitionSummaryTypeDef"]},
)
_OptionalListFlowDefinitionsResponseTypeDef = TypedDict(
    "_OptionalListFlowDefinitionsResponseTypeDef", {"NextToken": str}, total=False
)


class ListFlowDefinitionsResponseTypeDef(
    _RequiredListFlowDefinitionsResponseTypeDef, _OptionalListFlowDefinitionsResponseTypeDef
):
    pass


_RequiredListHumanTaskUisResponseTypeDef = TypedDict(
    "_RequiredListHumanTaskUisResponseTypeDef",
    {"HumanTaskUiSummaries": List["HumanTaskUiSummaryTypeDef"]},
)
_OptionalListHumanTaskUisResponseTypeDef = TypedDict(
    "_OptionalListHumanTaskUisResponseTypeDef", {"NextToken": str}, total=False
)


class ListHumanTaskUisResponseTypeDef(
    _RequiredListHumanTaskUisResponseTypeDef, _OptionalListHumanTaskUisResponseTypeDef
):
    pass


_RequiredListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "_RequiredListHyperParameterTuningJobsResponseTypeDef",
    {"HyperParameterTuningJobSummaries": List["HyperParameterTuningJobSummaryTypeDef"]},
)
_OptionalListHyperParameterTuningJobsResponseTypeDef = TypedDict(
    "_OptionalListHyperParameterTuningJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHyperParameterTuningJobsResponseTypeDef(
    _RequiredListHyperParameterTuningJobsResponseTypeDef,
    _OptionalListHyperParameterTuningJobsResponseTypeDef,
):
    pass


ListImageVersionsResponseTypeDef = TypedDict(
    "ListImageVersionsResponseTypeDef",
    {"ImageVersions": List["ImageVersionTypeDef"], "NextToken": str},
    total=False,
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef", {"Images": List["ImageTypeDef"], "NextToken": str}, total=False
)

_RequiredListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "_RequiredListLabelingJobsForWorkteamResponseTypeDef",
    {"LabelingJobSummaryList": List["LabelingJobForWorkteamSummaryTypeDef"]},
)
_OptionalListLabelingJobsForWorkteamResponseTypeDef = TypedDict(
    "_OptionalListLabelingJobsForWorkteamResponseTypeDef", {"NextToken": str}, total=False
)


class ListLabelingJobsForWorkteamResponseTypeDef(
    _RequiredListLabelingJobsForWorkteamResponseTypeDef,
    _OptionalListLabelingJobsForWorkteamResponseTypeDef,
):
    pass


ListLabelingJobsResponseTypeDef = TypedDict(
    "ListLabelingJobsResponseTypeDef",
    {"LabelingJobSummaryList": List["LabelingJobSummaryTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListModelPackagesOutputTypeDef = TypedDict(
    "_RequiredListModelPackagesOutputTypeDef",
    {"ModelPackageSummaryList": List["ModelPackageSummaryTypeDef"]},
)
_OptionalListModelPackagesOutputTypeDef = TypedDict(
    "_OptionalListModelPackagesOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListModelPackagesOutputTypeDef(
    _RequiredListModelPackagesOutputTypeDef, _OptionalListModelPackagesOutputTypeDef
):
    pass


_RequiredListModelsOutputTypeDef = TypedDict(
    "_RequiredListModelsOutputTypeDef", {"Models": List["ModelSummaryTypeDef"]}
)
_OptionalListModelsOutputTypeDef = TypedDict(
    "_OptionalListModelsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListModelsOutputTypeDef(_RequiredListModelsOutputTypeDef, _OptionalListModelsOutputTypeDef):
    pass


_RequiredListMonitoringExecutionsResponseTypeDef = TypedDict(
    "_RequiredListMonitoringExecutionsResponseTypeDef",
    {"MonitoringExecutionSummaries": List["MonitoringExecutionSummaryTypeDef"]},
)
_OptionalListMonitoringExecutionsResponseTypeDef = TypedDict(
    "_OptionalListMonitoringExecutionsResponseTypeDef", {"NextToken": str}, total=False
)


class ListMonitoringExecutionsResponseTypeDef(
    _RequiredListMonitoringExecutionsResponseTypeDef,
    _OptionalListMonitoringExecutionsResponseTypeDef,
):
    pass


_RequiredListMonitoringSchedulesResponseTypeDef = TypedDict(
    "_RequiredListMonitoringSchedulesResponseTypeDef",
    {"MonitoringScheduleSummaries": List["MonitoringScheduleSummaryTypeDef"]},
)
_OptionalListMonitoringSchedulesResponseTypeDef = TypedDict(
    "_OptionalListMonitoringSchedulesResponseTypeDef", {"NextToken": str}, total=False
)


class ListMonitoringSchedulesResponseTypeDef(
    _RequiredListMonitoringSchedulesResponseTypeDef, _OptionalListMonitoringSchedulesResponseTypeDef
):
    pass


ListNotebookInstanceLifecycleConfigsOutputTypeDef = TypedDict(
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstanceLifecycleConfigs": List["NotebookInstanceLifecycleConfigSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListNotebookInstancesOutputTypeDef = TypedDict(
    "ListNotebookInstancesOutputTypeDef",
    {
        "NextToken": str,
        "NotebookInstances": List["NotebookInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredListProcessingJobsResponseTypeDef = TypedDict(
    "_RequiredListProcessingJobsResponseTypeDef",
    {"ProcessingJobSummaries": List["ProcessingJobSummaryTypeDef"]},
)
_OptionalListProcessingJobsResponseTypeDef = TypedDict(
    "_OptionalListProcessingJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListProcessingJobsResponseTypeDef(
    _RequiredListProcessingJobsResponseTypeDef, _OptionalListProcessingJobsResponseTypeDef
):
    pass


_RequiredListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "_RequiredListSubscribedWorkteamsResponseTypeDef",
    {"SubscribedWorkteams": List["SubscribedWorkteamTypeDef"]},
)
_OptionalListSubscribedWorkteamsResponseTypeDef = TypedDict(
    "_OptionalListSubscribedWorkteamsResponseTypeDef", {"NextToken": str}, total=False
)


class ListSubscribedWorkteamsResponseTypeDef(
    _RequiredListSubscribedWorkteamsResponseTypeDef, _OptionalListSubscribedWorkteamsResponseTypeDef
):
    pass


ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {"TrainingJobSummaries": List["HyperParameterTrainingJobSummaryTypeDef"]},
)
_OptionalListTrainingJobsForHyperParameterTuningJobResponseTypeDef = TypedDict(
    "_OptionalListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    {"NextToken": str},
    total=False,
)


class ListTrainingJobsForHyperParameterTuningJobResponseTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    _OptionalListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
):
    pass


_RequiredListTrainingJobsResponseTypeDef = TypedDict(
    "_RequiredListTrainingJobsResponseTypeDef",
    {"TrainingJobSummaries": List["TrainingJobSummaryTypeDef"]},
)
_OptionalListTrainingJobsResponseTypeDef = TypedDict(
    "_OptionalListTrainingJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListTrainingJobsResponseTypeDef(
    _RequiredListTrainingJobsResponseTypeDef, _OptionalListTrainingJobsResponseTypeDef
):
    pass


_RequiredListTransformJobsResponseTypeDef = TypedDict(
    "_RequiredListTransformJobsResponseTypeDef",
    {"TransformJobSummaries": List["TransformJobSummaryTypeDef"]},
)
_OptionalListTransformJobsResponseTypeDef = TypedDict(
    "_OptionalListTransformJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListTransformJobsResponseTypeDef(
    _RequiredListTransformJobsResponseTypeDef, _OptionalListTransformJobsResponseTypeDef
):
    pass


ListTrialComponentsResponseTypeDef = TypedDict(
    "ListTrialComponentsResponseTypeDef",
    {"TrialComponentSummaries": List["TrialComponentSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTrialsResponseTypeDef = TypedDict(
    "ListTrialsResponseTypeDef",
    {"TrialSummaries": List["TrialSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListUserProfilesResponseTypeDef = TypedDict(
    "ListUserProfilesResponseTypeDef",
    {"UserProfiles": List["UserProfileDetailsTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListWorkforcesResponseTypeDef = TypedDict(
    "_RequiredListWorkforcesResponseTypeDef", {"Workforces": List["WorkforceTypeDef"]}
)
_OptionalListWorkforcesResponseTypeDef = TypedDict(
    "_OptionalListWorkforcesResponseTypeDef", {"NextToken": str}, total=False
)


class ListWorkforcesResponseTypeDef(
    _RequiredListWorkforcesResponseTypeDef, _OptionalListWorkforcesResponseTypeDef
):
    pass


_RequiredListWorkteamsResponseTypeDef = TypedDict(
    "_RequiredListWorkteamsResponseTypeDef", {"Workteams": List["WorkteamTypeDef"]}
)
_OptionalListWorkteamsResponseTypeDef = TypedDict(
    "_OptionalListWorkteamsResponseTypeDef", {"NextToken": str}, total=False
)


class ListWorkteamsResponseTypeDef(
    _RequiredListWorkteamsResponseTypeDef, _OptionalListWorkteamsResponseTypeDef
):
    pass


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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RenderUiTemplateResponseTypeDef = TypedDict(
    "RenderUiTemplateResponseTypeDef",
    {"RenderedContent": str, "Errors": List["RenderingErrorTypeDef"]},
)

RenderableTaskTypeDef = TypedDict("RenderableTaskTypeDef", {"Input": str})

RetentionPolicyTypeDef = TypedDict(
    "RetentionPolicyTypeDef", {"HomeEfsFileSystem": Literal["Retain", "Delete"]}, total=False
)

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef", {"Results": List["SearchRecordTypeDef"], "NextToken": str}, total=False
)

SuggestionQueryTypeDef = TypedDict(
    "SuggestionQueryTypeDef", {"PropertyNameQuery": "PropertyNameQueryTypeDef"}, total=False
)

UiTemplateTypeDef = TypedDict("UiTemplateTypeDef", {"Content": str})

UpdateAppImageConfigResponseTypeDef = TypedDict(
    "UpdateAppImageConfigResponseTypeDef", {"AppImageConfigArn": str}, total=False
)

_RequiredUpdateCodeRepositoryOutputTypeDef = TypedDict(
    "_RequiredUpdateCodeRepositoryOutputTypeDef", {"CodeRepositoryArn": str}
)
_OptionalUpdateCodeRepositoryOutputTypeDef = TypedDict(
    "_OptionalUpdateCodeRepositoryOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateCodeRepositoryOutputTypeDef(
    _RequiredUpdateCodeRepositoryOutputTypeDef, _OptionalUpdateCodeRepositoryOutputTypeDef
):
    pass


UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef", {"DomainArn": str}, total=False
)

_RequiredUpdateEndpointOutputTypeDef = TypedDict(
    "_RequiredUpdateEndpointOutputTypeDef", {"EndpointArn": str}
)
_OptionalUpdateEndpointOutputTypeDef = TypedDict(
    "_OptionalUpdateEndpointOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class UpdateEndpointOutputTypeDef(
    _RequiredUpdateEndpointOutputTypeDef, _OptionalUpdateEndpointOutputTypeDef
):
    pass


_RequiredUpdateEndpointWeightsAndCapacitiesOutputTypeDef = TypedDict(
    "_RequiredUpdateEndpointWeightsAndCapacitiesOutputTypeDef", {"EndpointArn": str}
)
_OptionalUpdateEndpointWeightsAndCapacitiesOutputTypeDef = TypedDict(
    "_OptionalUpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateEndpointWeightsAndCapacitiesOutputTypeDef(
    _RequiredUpdateEndpointWeightsAndCapacitiesOutputTypeDef,
    _OptionalUpdateEndpointWeightsAndCapacitiesOutputTypeDef,
):
    pass


UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef", {"ExperimentArn": str}, total=False
)

UpdateImageResponseTypeDef = TypedDict("UpdateImageResponseTypeDef", {"ImageArn": str}, total=False)

UpdateMonitoringScheduleResponseTypeDef = TypedDict(
    "UpdateMonitoringScheduleResponseTypeDef", {"MonitoringScheduleArn": str}
)

UpdateTrialComponentResponseTypeDef = TypedDict(
    "UpdateTrialComponentResponseTypeDef", {"TrialComponentArn": str}, total=False
)

UpdateTrialResponseTypeDef = TypedDict("UpdateTrialResponseTypeDef", {"TrialArn": str}, total=False)

UpdateUserProfileResponseTypeDef = TypedDict(
    "UpdateUserProfileResponseTypeDef", {"UserProfileArn": str}, total=False
)

UpdateWorkforceResponseTypeDef = TypedDict(
    "UpdateWorkforceResponseTypeDef", {"Workforce": "WorkforceTypeDef"}
)

UpdateWorkteamResponseTypeDef = TypedDict(
    "UpdateWorkteamResponseTypeDef", {"Workteam": "WorkteamTypeDef"}
)

VariantPropertyTypeDef = TypedDict(
    "VariantPropertyTypeDef",
    {"VariantPropertyType": Literal["DesiredInstanceCount", "DesiredWeight", "DataCaptureConfig"]},
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
