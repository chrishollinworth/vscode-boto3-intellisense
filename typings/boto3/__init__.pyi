import sys
from typing import overload, Any, Union
from botocore.config import Config
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
from mypy_boto3.accessanalyzer import AccessAnalyzerClient
from mypy_boto3.acm import ACMClient
from mypy_boto3.acm_pca import ACMPCAClient
from mypy_boto3.alexaforbusiness import AlexaForBusinessClient
from mypy_boto3.amplify import AmplifyClient
from mypy_boto3.amplifybackend import AmplifyBackendClient
from mypy_boto3.apigateway import APIGatewayClient
from mypy_boto3.apigatewaymanagementapi import ApiGatewayManagementApiClient
from mypy_boto3.apigatewayv2 import ApiGatewayV2Client
from mypy_boto3.appconfig import AppConfigClient
from mypy_boto3.appflow import AppflowClient
from mypy_boto3.appintegrations import AppIntegrationsClient
from mypy_boto3.application_autoscaling import ApplicationAutoScalingClient
from mypy_boto3.application_insights import ApplicationInsightsClient
from mypy_boto3.appmesh import AppMeshClient
from mypy_boto3.appstream import AppStreamClient
from mypy_boto3.appsync import AppSyncClient
from mypy_boto3.athena import AthenaClient
from mypy_boto3.autoscaling import AutoScalingClient
from mypy_boto3.autoscaling_plans import AutoScalingPlansClient
from mypy_boto3.backup import BackupClient
from mypy_boto3.batch import BatchClient
from mypy_boto3.braket import BraketClient
from mypy_boto3.budgets import BudgetsClient
from mypy_boto3.ce import CostExplorerClient
from mypy_boto3.chime import ChimeClient
from mypy_boto3.cloud9 import Cloud9Client
from mypy_boto3.clouddirectory import CloudDirectoryClient
from mypy_boto3.cloudformation import CloudFormationClient
from mypy_boto3.cloudformation import CloudFormationServiceResource
from mypy_boto3.cloudfront import CloudFrontClient
from mypy_boto3.cloudhsm import CloudHSMClient
from mypy_boto3.cloudhsmv2 import CloudHSMV2Client
from mypy_boto3.cloudsearch import CloudSearchClient
from mypy_boto3.cloudsearchdomain import CloudSearchDomainClient
from mypy_boto3.cloudtrail import CloudTrailClient
from mypy_boto3.cloudwatch import CloudWatchClient
from mypy_boto3.cloudwatch import CloudWatchServiceResource
from mypy_boto3.codeartifact import CodeArtifactClient
from mypy_boto3.codebuild import CodeBuildClient
from mypy_boto3.codecommit import CodeCommitClient
from mypy_boto3.codedeploy import CodeDeployClient
from mypy_boto3.codeguru_reviewer import CodeGuruReviewerClient
from mypy_boto3.codeguruprofiler import CodeGuruProfilerClient
from mypy_boto3.codepipeline import CodePipelineClient
from mypy_boto3.codestar import CodeStarClient
from mypy_boto3.codestar_connections import CodeStarconnectionsClient
from mypy_boto3.codestar_notifications import CodeStarNotificationsClient
from mypy_boto3.cognito_identity import CognitoIdentityClient
from mypy_boto3.cognito_idp import CognitoIdentityProviderClient
from mypy_boto3.cognito_sync import CognitoSyncClient
from mypy_boto3.comprehend import ComprehendClient
from mypy_boto3.comprehendmedical import ComprehendMedicalClient
from mypy_boto3.compute_optimizer import ComputeOptimizerClient
from mypy_boto3.config import ConfigServiceClient
from mypy_boto3.connect import ConnectClient
from mypy_boto3.connect_contact_lens import ConnectContactLensClient
from mypy_boto3.connectparticipant import ConnectParticipantClient
from mypy_boto3.cur import CostandUsageReportServiceClient
from mypy_boto3.customer_profiles import CustomerProfilesClient
from mypy_boto3.databrew import GlueDataBrewClient
from mypy_boto3.dataexchange import DataExchangeClient
from mypy_boto3.datapipeline import DataPipelineClient
from mypy_boto3.datasync import DataSyncClient
from mypy_boto3.dax import DAXClient
from mypy_boto3.detective import DetectiveClient
from mypy_boto3.devicefarm import DeviceFarmClient
from mypy_boto3.devops_guru import DevOpsGuruClient
from mypy_boto3.directconnect import DirectConnectClient
from mypy_boto3.discovery import ApplicationDiscoveryServiceClient
from mypy_boto3.dlm import DLMClient
from mypy_boto3.dms import DatabaseMigrationServiceClient
from mypy_boto3.docdb import DocDBClient
from mypy_boto3.ds import DirectoryServiceClient
from mypy_boto3.dynamodb import DynamoDBClient
from mypy_boto3.dynamodb import DynamoDBServiceResource
from mypy_boto3.dynamodbstreams import DynamoDBStreamsClient
from mypy_boto3.ebs import EBSClient
from mypy_boto3.ec2 import EC2Client
from mypy_boto3.ec2 import EC2ServiceResource
from mypy_boto3.ec2_instance_connect import EC2InstanceConnectClient
from mypy_boto3.ecr import ECRClient
from mypy_boto3.ecr_public import ECRPublicClient
from mypy_boto3.ecs import ECSClient
from mypy_boto3.efs import EFSClient
from mypy_boto3.eks import EKSClient
from mypy_boto3.elastic_inference import ElasticInferenceClient
from mypy_boto3.elasticache import ElastiCacheClient
from mypy_boto3.elasticbeanstalk import ElasticBeanstalkClient
from mypy_boto3.elastictranscoder import ElasticTranscoderClient
from mypy_boto3.elb import ElasticLoadBalancingClient
from mypy_boto3.elbv2 import ElasticLoadBalancingv2Client
from mypy_boto3.emr import EMRClient
from mypy_boto3.es import ElasticsearchServiceClient
from mypy_boto3.events import EventBridgeClient
from mypy_boto3.firehose import FirehoseClient
from mypy_boto3.fms import FMSClient
from mypy_boto3.forecast import ForecastServiceClient
from mypy_boto3.forecastquery import ForecastQueryServiceClient
from mypy_boto3.frauddetector import FraudDetectorClient
from mypy_boto3.fsx import FSxClient
from mypy_boto3.gamelift import GameLiftClient
from mypy_boto3.glacier import GlacierClient
from mypy_boto3.glacier import GlacierServiceResource
from mypy_boto3.globalaccelerator import GlobalAcceleratorClient
from mypy_boto3.glue import GlueClient
from mypy_boto3.greengrass import GreengrassClient
from mypy_boto3.groundstation import GroundStationClient
from mypy_boto3.guardduty import GuardDutyClient
from mypy_boto3.health import HealthClient
from mypy_boto3.honeycode import HoneycodeClient
from mypy_boto3.iam import IAMClient
from mypy_boto3.iam import IAMServiceResource
from mypy_boto3.identitystore import IdentityStoreClient
from mypy_boto3.imagebuilder import ImagebuilderClient
from mypy_boto3.importexport import ImportExportClient
from mypy_boto3.inspector import InspectorClient
from mypy_boto3.iot import IoTClient
from mypy_boto3.iot_data import IoTDataPlaneClient
from mypy_boto3.iot_jobs_data import IoTJobsDataPlaneClient
from mypy_boto3.iot1click_devices import IoT1ClickDevicesServiceClient
from mypy_boto3.iot1click_projects import IoT1ClickProjectsClient
from mypy_boto3.iotanalytics import IoTAnalyticsClient
from mypy_boto3.iotevents import IoTEventsClient
from mypy_boto3.iotevents_data import IoTEventsDataClient
from mypy_boto3.iotsecuretunneling import IoTSecureTunnelingClient
from mypy_boto3.iotsitewise import IoTSiteWiseClient
from mypy_boto3.iotthingsgraph import IoTThingsGraphClient
from mypy_boto3.ivs import IVSClient
from mypy_boto3.kafka import KafkaClient
from mypy_boto3.kendra import KendraClient
from mypy_boto3.kinesis import KinesisClient
from mypy_boto3.kinesis_video_archived_media import KinesisVideoArchivedMediaClient
from mypy_boto3.kinesis_video_media import KinesisVideoMediaClient
from mypy_boto3.kinesis_video_signaling import KinesisVideoSignalingChannelsClient
from mypy_boto3.kinesisanalytics import KinesisAnalyticsClient
from mypy_boto3.kinesisanalyticsv2 import KinesisAnalyticsV2Client
from mypy_boto3.kinesisvideo import KinesisVideoClient
from mypy_boto3.kms import KMSClient
from mypy_boto3.lakeformation import LakeFormationClient
from mypy_boto3.lambda_ import LambdaClient
from mypy_boto3.lex_models import LexModelBuildingServiceClient
from mypy_boto3.lex_runtime import LexRuntimeServiceClient
from mypy_boto3.license_manager import LicenseManagerClient
from mypy_boto3.lightsail import LightsailClient
from mypy_boto3.logs import CloudWatchLogsClient
from mypy_boto3.lookoutvision import LookoutForVisionClient
from mypy_boto3.machinelearning import MachineLearningClient
from mypy_boto3.macie import MacieClient
from mypy_boto3.macie2 import Macie2Client
from mypy_boto3.managedblockchain import ManagedBlockchainClient
from mypy_boto3.marketplace_catalog import MarketplaceCatalogClient
from mypy_boto3.marketplace_entitlement import MarketplaceEntitlementServiceClient
from mypy_boto3.marketplacecommerceanalytics import MarketplaceCommerceAnalyticsClient
from mypy_boto3.mediaconnect import MediaConnectClient
from mypy_boto3.mediaconvert import MediaConvertClient
from mypy_boto3.medialive import MediaLiveClient
from mypy_boto3.mediapackage import MediaPackageClient
from mypy_boto3.mediapackage_vod import MediaPackageVodClient
from mypy_boto3.mediastore import MediaStoreClient
from mypy_boto3.mediastore_data import MediaStoreDataClient
from mypy_boto3.mediatailor import MediaTailorClient
from mypy_boto3.meteringmarketplace import MarketplaceMeteringClient
from mypy_boto3.mgh import MigrationHubClient
from mypy_boto3.migrationhub_config import MigrationHubConfigClient
from mypy_boto3.mobile import MobileClient
from mypy_boto3.mq import MQClient
from mypy_boto3.mturk import MTurkClient
from mypy_boto3.mwaa import MWAAClient
from mypy_boto3.neptune import NeptuneClient
from mypy_boto3.network_firewall import NetworkFirewallClient
from mypy_boto3.networkmanager import NetworkManagerClient
from mypy_boto3.opsworks import OpsWorksClient
from mypy_boto3.opsworks import OpsWorksServiceResource
from mypy_boto3.opsworkscm import OpsWorksCMClient
from mypy_boto3.organizations import OrganizationsClient
from mypy_boto3.outposts import OutpostsClient
from mypy_boto3.personalize import PersonalizeClient
from mypy_boto3.personalize_events import PersonalizeEventsClient
from mypy_boto3.personalize_runtime import PersonalizeRuntimeClient
from mypy_boto3.pi import PIClient
from mypy_boto3.pinpoint import PinpointClient
from mypy_boto3.pinpoint_email import PinpointEmailClient
from mypy_boto3.pinpoint_sms_voice import PinpointSMSVoiceClient
from mypy_boto3.polly import PollyClient
from mypy_boto3.pricing import PricingClient
from mypy_boto3.qldb import QLDBClient
from mypy_boto3.qldb_session import QLDBSessionClient
from mypy_boto3.quicksight import QuickSightClient
from mypy_boto3.ram import RAMClient
from mypy_boto3.rds import RDSClient
from mypy_boto3.rds_data import RDSDataServiceClient
from mypy_boto3.redshift import RedshiftClient
from mypy_boto3.redshift_data import RedshiftDataAPIServiceClient
from mypy_boto3.rekognition import RekognitionClient
from mypy_boto3.resource_groups import ResourceGroupsClient
from mypy_boto3.resourcegroupstaggingapi import ResourceGroupsTaggingAPIClient
from mypy_boto3.robomaker import RoboMakerClient
from mypy_boto3.route53 import Route53Client
from mypy_boto3.route53domains import Route53DomainsClient
from mypy_boto3.route53resolver import Route53ResolverClient
from mypy_boto3.s3 import S3Client
from mypy_boto3.s3 import S3ServiceResource
from mypy_boto3.s3control import S3ControlClient
from mypy_boto3.s3outposts import S3OutpostsClient
from mypy_boto3.sagemaker import SageMakerClient
from mypy_boto3.sagemaker_a2i_runtime import AugmentedAIRuntimeClient
from mypy_boto3.sagemaker_featurestore_runtime import SageMakerFeatureStoreRuntimeClient
from mypy_boto3.sagemaker_runtime import SageMakerRuntimeClient
from mypy_boto3.savingsplans import SavingsPlansClient
from mypy_boto3.schemas import SchemasClient
from mypy_boto3.sdb import SimpleDBClient
from mypy_boto3.secretsmanager import SecretsManagerClient
from mypy_boto3.securityhub import SecurityHubClient
from mypy_boto3.serverlessrepo import ServerlessApplicationRepositoryClient
from mypy_boto3.service_quotas import ServiceQuotasClient
from mypy_boto3.servicecatalog import ServiceCatalogClient
from mypy_boto3.servicecatalog_appregistry import ServiceCatalogAppRegistryClient
from mypy_boto3.servicediscovery import ServiceDiscoveryClient
from mypy_boto3.ses import SESClient
from mypy_boto3.sesv2 import SESV2Client
from mypy_boto3.shield import ShieldClient
from mypy_boto3.signer import SignerClient
from mypy_boto3.sms import SMSClient
from mypy_boto3.sms_voice import SMSVoiceClient
from mypy_boto3.snowball import SnowballClient
from mypy_boto3.sns import SNSClient
from mypy_boto3.sns import SNSServiceResource
from mypy_boto3.sqs import SQSClient
from mypy_boto3.sqs import SQSServiceResource
from mypy_boto3.ssm import SSMClient
from mypy_boto3.sso import SSOClient
from mypy_boto3.sso_admin import SSOAdminClient
from mypy_boto3.sso_oidc import SSOOIDCClient
from mypy_boto3.stepfunctions import SFNClient
from mypy_boto3.storagegateway import StorageGatewayClient
from mypy_boto3.sts import STSClient
from mypy_boto3.support import SupportClient
from mypy_boto3.swf import SWFClient
from mypy_boto3.synthetics import SyntheticsClient
from mypy_boto3.textract import TextractClient
from mypy_boto3.timestream_query import TimestreamQueryClient
from mypy_boto3.timestream_write import TimestreamWriteClient
from mypy_boto3.transcribe import TranscribeServiceClient
from mypy_boto3.transfer import TransferClient
from mypy_boto3.translate import TranslateClient
from mypy_boto3.waf import WAFClient
from mypy_boto3.waf_regional import WAFRegionalClient
from mypy_boto3.wafv2 import WAFV2Client
from mypy_boto3.workdocs import WorkDocsClient
from mypy_boto3.worklink import WorkLinkClient
from mypy_boto3.workmail import WorkMailClient
from mypy_boto3.workmailmessageflow import WorkMailMessageFlowClient
from mypy_boto3.workspaces import WorkSpacesClient
from mypy_boto3.xray import XRayClient

@overload
def client(
    service_name: Literal["accessanalyzer"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AccessAnalyzerClient:
    pass
@overload
def client(
    service_name: Literal["acm"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ACMClient:
    pass
@overload
def client(
    service_name: Literal["acm-pca"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ACMPCAClient:
    pass
@overload
def client(
    service_name: Literal["alexaforbusiness"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AlexaForBusinessClient:
    pass
@overload
def client(
    service_name: Literal["amplify"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AmplifyClient:
    pass
@overload
def client(
    service_name: Literal["amplifybackend"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AmplifyBackendClient:
    pass
@overload
def client(
    service_name: Literal["apigateway"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> APIGatewayClient:
    pass
@overload
def client(
    service_name: Literal["apigatewaymanagementapi"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ApiGatewayManagementApiClient:
    pass
@overload
def client(
    service_name: Literal["apigatewayv2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ApiGatewayV2Client:
    pass
@overload
def client(
    service_name: Literal["appconfig"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AppConfigClient:
    pass
@overload
def client(
    service_name: Literal["appflow"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AppflowClient:
    pass
@overload
def client(
    service_name: Literal["appintegrations"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AppIntegrationsClient:
    pass
@overload
def client(
    service_name: Literal["application-autoscaling"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ApplicationAutoScalingClient:
    pass
@overload
def client(
    service_name: Literal["application-insights"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ApplicationInsightsClient:
    pass
@overload
def client(
    service_name: Literal["appmesh"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AppMeshClient:
    pass
@overload
def client(
    service_name: Literal["appstream"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AppStreamClient:
    pass
@overload
def client(
    service_name: Literal["appsync"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AppSyncClient:
    pass
@overload
def client(
    service_name: Literal["athena"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AthenaClient:
    pass
@overload
def client(
    service_name: Literal["autoscaling"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AutoScalingClient:
    pass
@overload
def client(
    service_name: Literal["autoscaling-plans"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AutoScalingPlansClient:
    pass
@overload
def client(
    service_name: Literal["backup"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> BackupClient:
    pass
@overload
def client(
    service_name: Literal["batch"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> BatchClient:
    pass
@overload
def client(
    service_name: Literal["braket"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> BraketClient:
    pass
@overload
def client(
    service_name: Literal["budgets"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> BudgetsClient:
    pass
@overload
def client(
    service_name: Literal["ce"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CostExplorerClient:
    pass
@overload
def client(
    service_name: Literal["chime"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ChimeClient:
    pass
@overload
def client(
    service_name: Literal["cloud9"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Cloud9Client:
    pass
@overload
def client(
    service_name: Literal["clouddirectory"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudDirectoryClient:
    pass
@overload
def client(
    service_name: Literal["cloudformation"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudFormationClient:
    pass
@overload
def client(
    service_name: Literal["cloudfront"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudFrontClient:
    pass
@overload
def client(
    service_name: Literal["cloudhsm"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudHSMClient:
    pass
@overload
def client(
    service_name: Literal["cloudhsmv2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudHSMV2Client:
    pass
@overload
def client(
    service_name: Literal["cloudsearch"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudSearchClient:
    pass
@overload
def client(
    service_name: Literal["cloudsearchdomain"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudSearchDomainClient:
    pass
@overload
def client(
    service_name: Literal["cloudtrail"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudTrailClient:
    pass
@overload
def client(
    service_name: Literal["cloudwatch"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudWatchClient:
    pass
@overload
def client(
    service_name: Literal["codeartifact"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeArtifactClient:
    pass
@overload
def client(
    service_name: Literal["codebuild"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeBuildClient:
    pass
@overload
def client(
    service_name: Literal["codecommit"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeCommitClient:
    pass
@overload
def client(
    service_name: Literal["codedeploy"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeDeployClient:
    pass
@overload
def client(
    service_name: Literal["codeguru-reviewer"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeGuruReviewerClient:
    pass
@overload
def client(
    service_name: Literal["codeguruprofiler"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeGuruProfilerClient:
    pass
@overload
def client(
    service_name: Literal["codepipeline"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodePipelineClient:
    pass
@overload
def client(
    service_name: Literal["codestar"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeStarClient:
    pass
@overload
def client(
    service_name: Literal["codestar-connections"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeStarconnectionsClient:
    pass
@overload
def client(
    service_name: Literal["codestar-notifications"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CodeStarNotificationsClient:
    pass
@overload
def client(
    service_name: Literal["cognito-identity"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CognitoIdentityClient:
    pass
@overload
def client(
    service_name: Literal["cognito-idp"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CognitoIdentityProviderClient:
    pass
@overload
def client(
    service_name: Literal["cognito-sync"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CognitoSyncClient:
    pass
@overload
def client(
    service_name: Literal["comprehend"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ComprehendClient:
    pass
@overload
def client(
    service_name: Literal["comprehendmedical"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ComprehendMedicalClient:
    pass
@overload
def client(
    service_name: Literal["compute-optimizer"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ComputeOptimizerClient:
    pass
@overload
def client(
    service_name: Literal["config"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ConfigServiceClient:
    pass
@overload
def client(
    service_name: Literal["connect"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ConnectClient:
    pass
@overload
def client(
    service_name: Literal["connect-contact-lens"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ConnectContactLensClient:
    pass
@overload
def client(
    service_name: Literal["connectparticipant"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ConnectParticipantClient:
    pass
@overload
def client(
    service_name: Literal["cur"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CostandUsageReportServiceClient:
    pass
@overload
def client(
    service_name: Literal["customer-profiles"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CustomerProfilesClient:
    pass
@overload
def client(
    service_name: Literal["databrew"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GlueDataBrewClient:
    pass
@overload
def client(
    service_name: Literal["dataexchange"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DataExchangeClient:
    pass
@overload
def client(
    service_name: Literal["datapipeline"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DataPipelineClient:
    pass
@overload
def client(
    service_name: Literal["datasync"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DataSyncClient:
    pass
@overload
def client(
    service_name: Literal["dax"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DAXClient:
    pass
@overload
def client(
    service_name: Literal["detective"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DetectiveClient:
    pass
@overload
def client(
    service_name: Literal["devicefarm"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DeviceFarmClient:
    pass
@overload
def client(
    service_name: Literal["devops-guru"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DevOpsGuruClient:
    pass
@overload
def client(
    service_name: Literal["directconnect"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DirectConnectClient:
    pass
@overload
def client(
    service_name: Literal["discovery"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ApplicationDiscoveryServiceClient:
    pass
@overload
def client(
    service_name: Literal["dlm"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DLMClient:
    pass
@overload
def client(
    service_name: Literal["dms"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DatabaseMigrationServiceClient:
    pass
@overload
def client(
    service_name: Literal["docdb"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DocDBClient:
    pass
@overload
def client(
    service_name: Literal["ds"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DirectoryServiceClient:
    pass
@overload
def client(
    service_name: Literal["dynamodb"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DynamoDBClient:
    pass
@overload
def client(
    service_name: Literal["dynamodbstreams"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DynamoDBStreamsClient:
    pass
@overload
def client(
    service_name: Literal["ebs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EBSClient:
    pass
@overload
def client(
    service_name: Literal["ec2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EC2Client:
    pass
@overload
def client(
    service_name: Literal["ec2-instance-connect"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EC2InstanceConnectClient:
    pass
@overload
def client(
    service_name: Literal["ecr"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ECRClient:
    pass
@overload
def client(
    service_name: Literal["ecr-public"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ECRPublicClient:
    pass
@overload
def client(
    service_name: Literal["ecs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ECSClient:
    pass
@overload
def client(
    service_name: Literal["efs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EFSClient:
    pass
@overload
def client(
    service_name: Literal["eks"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EKSClient:
    pass
@overload
def client(
    service_name: Literal["elastic-inference"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElasticInferenceClient:
    pass
@overload
def client(
    service_name: Literal["elasticache"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElastiCacheClient:
    pass
@overload
def client(
    service_name: Literal["elasticbeanstalk"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElasticBeanstalkClient:
    pass
@overload
def client(
    service_name: Literal["elastictranscoder"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElasticTranscoderClient:
    pass
@overload
def client(
    service_name: Literal["elb"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElasticLoadBalancingClient:
    pass
@overload
def client(
    service_name: Literal["elbv2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElasticLoadBalancingv2Client:
    pass
@overload
def client(
    service_name: Literal["emr"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EMRClient:
    pass
@overload
def client(
    service_name: Literal["es"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ElasticsearchServiceClient:
    pass
@overload
def client(
    service_name: Literal["events"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EventBridgeClient:
    pass
@overload
def client(
    service_name: Literal["firehose"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> FirehoseClient:
    pass
@overload
def client(
    service_name: Literal["fms"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> FMSClient:
    pass
@overload
def client(
    service_name: Literal["forecast"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ForecastServiceClient:
    pass
@overload
def client(
    service_name: Literal["forecastquery"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ForecastQueryServiceClient:
    pass
@overload
def client(
    service_name: Literal["frauddetector"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> FraudDetectorClient:
    pass
@overload
def client(
    service_name: Literal["fsx"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> FSxClient:
    pass
@overload
def client(
    service_name: Literal["gamelift"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GameLiftClient:
    pass
@overload
def client(
    service_name: Literal["glacier"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GlacierClient:
    pass
@overload
def client(
    service_name: Literal["globalaccelerator"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GlobalAcceleratorClient:
    pass
@overload
def client(
    service_name: Literal["glue"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GlueClient:
    pass
@overload
def client(
    service_name: Literal["greengrass"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GreengrassClient:
    pass
@overload
def client(
    service_name: Literal["groundstation"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GroundStationClient:
    pass
@overload
def client(
    service_name: Literal["guardduty"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GuardDutyClient:
    pass
@overload
def client(
    service_name: Literal["health"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> HealthClient:
    pass
@overload
def client(
    service_name: Literal["honeycode"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> HoneycodeClient:
    pass
@overload
def client(
    service_name: Literal["iam"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IAMClient:
    pass
@overload
def client(
    service_name: Literal["identitystore"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IdentityStoreClient:
    pass
@overload
def client(
    service_name: Literal["imagebuilder"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ImagebuilderClient:
    pass
@overload
def client(
    service_name: Literal["importexport"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ImportExportClient:
    pass
@overload
def client(
    service_name: Literal["inspector"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> InspectorClient:
    pass
@overload
def client(
    service_name: Literal["iot"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTClient:
    pass
@overload
def client(
    service_name: Literal["iot-data"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTDataPlaneClient:
    pass
@overload
def client(
    service_name: Literal["iot-jobs-data"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTJobsDataPlaneClient:
    pass
@overload
def client(
    service_name: Literal["iot1click-devices"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoT1ClickDevicesServiceClient:
    pass
@overload
def client(
    service_name: Literal["iot1click-projects"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoT1ClickProjectsClient:
    pass
@overload
def client(
    service_name: Literal["iotanalytics"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTAnalyticsClient:
    pass
@overload
def client(
    service_name: Literal["iotevents"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTEventsClient:
    pass
@overload
def client(
    service_name: Literal["iotevents-data"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTEventsDataClient:
    pass
@overload
def client(
    service_name: Literal["iotsecuretunneling"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTSecureTunnelingClient:
    pass
@overload
def client(
    service_name: Literal["iotsitewise"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTSiteWiseClient:
    pass
@overload
def client(
    service_name: Literal["iotthingsgraph"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IoTThingsGraphClient:
    pass
@overload
def client(
    service_name: Literal["ivs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IVSClient:
    pass
@overload
def client(
    service_name: Literal["kafka"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KafkaClient:
    pass
@overload
def client(
    service_name: Literal["kendra"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KendraClient:
    pass
@overload
def client(
    service_name: Literal["kinesis"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisClient:
    pass
@overload
def client(
    service_name: Literal["kinesis-video-archived-media"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisVideoArchivedMediaClient:
    pass
@overload
def client(
    service_name: Literal["kinesis-video-media"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisVideoMediaClient:
    pass
@overload
def client(
    service_name: Literal["kinesis-video-signaling"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisVideoSignalingChannelsClient:
    pass
@overload
def client(
    service_name: Literal["kinesisanalytics"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisAnalyticsClient:
    pass
@overload
def client(
    service_name: Literal["kinesisanalyticsv2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisAnalyticsV2Client:
    pass
@overload
def client(
    service_name: Literal["kinesisvideo"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KinesisVideoClient:
    pass
@overload
def client(
    service_name: Literal["kms"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> KMSClient:
    pass
@overload
def client(
    service_name: Literal["lakeformation"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LakeFormationClient:
    pass
@overload
def client(
    service_name: Literal["lambda"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LambdaClient:
    pass
@overload
def client(
    service_name: Literal["lex-models"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LexModelBuildingServiceClient:
    pass
@overload
def client(
    service_name: Literal["lex-runtime"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LexRuntimeServiceClient:
    pass
@overload
def client(
    service_name: Literal["license-manager"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LicenseManagerClient:
    pass
@overload
def client(
    service_name: Literal["lightsail"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LightsailClient:
    pass
@overload
def client(
    service_name: Literal["logs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudWatchLogsClient:
    pass
@overload
def client(
    service_name: Literal["lookoutvision"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> LookoutForVisionClient:
    pass
@overload
def client(
    service_name: Literal["machinelearning"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MachineLearningClient:
    pass
@overload
def client(
    service_name: Literal["macie"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MacieClient:
    pass
@overload
def client(
    service_name: Literal["macie2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Macie2Client:
    pass
@overload
def client(
    service_name: Literal["managedblockchain"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ManagedBlockchainClient:
    pass
@overload
def client(
    service_name: Literal["marketplace-catalog"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MarketplaceCatalogClient:
    pass
@overload
def client(
    service_name: Literal["marketplace-entitlement"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MarketplaceEntitlementServiceClient:
    pass
@overload
def client(
    service_name: Literal["marketplacecommerceanalytics"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MarketplaceCommerceAnalyticsClient:
    pass
@overload
def client(
    service_name: Literal["mediaconnect"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaConnectClient:
    pass
@overload
def client(
    service_name: Literal["mediaconvert"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaConvertClient:
    pass
@overload
def client(
    service_name: Literal["medialive"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaLiveClient:
    pass
@overload
def client(
    service_name: Literal["mediapackage"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaPackageClient:
    pass
@overload
def client(
    service_name: Literal["mediapackage-vod"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaPackageVodClient:
    pass
@overload
def client(
    service_name: Literal["mediastore"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaStoreClient:
    pass
@overload
def client(
    service_name: Literal["mediastore-data"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaStoreDataClient:
    pass
@overload
def client(
    service_name: Literal["mediatailor"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MediaTailorClient:
    pass
@overload
def client(
    service_name: Literal["meteringmarketplace"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MarketplaceMeteringClient:
    pass
@overload
def client(
    service_name: Literal["mgh"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MigrationHubClient:
    pass
@overload
def client(
    service_name: Literal["migrationhub-config"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MigrationHubConfigClient:
    pass
@overload
def client(
    service_name: Literal["mobile"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MobileClient:
    pass
@overload
def client(
    service_name: Literal["mq"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MQClient:
    pass
@overload
def client(
    service_name: Literal["mturk"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MTurkClient:
    pass
@overload
def client(
    service_name: Literal["mwaa"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> MWAAClient:
    pass
@overload
def client(
    service_name: Literal["neptune"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> NeptuneClient:
    pass
@overload
def client(
    service_name: Literal["network-firewall"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> NetworkFirewallClient:
    pass
@overload
def client(
    service_name: Literal["networkmanager"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> NetworkManagerClient:
    pass
@overload
def client(
    service_name: Literal["opsworks"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> OpsWorksClient:
    pass
@overload
def client(
    service_name: Literal["opsworkscm"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> OpsWorksCMClient:
    pass
@overload
def client(
    service_name: Literal["organizations"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> OrganizationsClient:
    pass
@overload
def client(
    service_name: Literal["outposts"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> OutpostsClient:
    pass
@overload
def client(
    service_name: Literal["personalize"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PersonalizeClient:
    pass
@overload
def client(
    service_name: Literal["personalize-events"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PersonalizeEventsClient:
    pass
@overload
def client(
    service_name: Literal["personalize-runtime"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PersonalizeRuntimeClient:
    pass
@overload
def client(
    service_name: Literal["pi"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PIClient:
    pass
@overload
def client(
    service_name: Literal["pinpoint"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PinpointClient:
    pass
@overload
def client(
    service_name: Literal["pinpoint-email"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PinpointEmailClient:
    pass
@overload
def client(
    service_name: Literal["pinpoint-sms-voice"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PinpointSMSVoiceClient:
    pass
@overload
def client(
    service_name: Literal["polly"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PollyClient:
    pass
@overload
def client(
    service_name: Literal["pricing"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> PricingClient:
    pass
@overload
def client(
    service_name: Literal["qldb"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> QLDBClient:
    pass
@overload
def client(
    service_name: Literal["qldb-session"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> QLDBSessionClient:
    pass
@overload
def client(
    service_name: Literal["quicksight"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> QuickSightClient:
    pass
@overload
def client(
    service_name: Literal["ram"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RAMClient:
    pass
@overload
def client(
    service_name: Literal["rds"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RDSClient:
    pass
@overload
def client(
    service_name: Literal["rds-data"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RDSDataServiceClient:
    pass
@overload
def client(
    service_name: Literal["redshift"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RedshiftClient:
    pass
@overload
def client(
    service_name: Literal["redshift-data"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RedshiftDataAPIServiceClient:
    pass
@overload
def client(
    service_name: Literal["rekognition"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RekognitionClient:
    pass
@overload
def client(
    service_name: Literal["resource-groups"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ResourceGroupsClient:
    pass
@overload
def client(
    service_name: Literal["resourcegroupstaggingapi"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ResourceGroupsTaggingAPIClient:
    pass
@overload
def client(
    service_name: Literal["robomaker"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> RoboMakerClient:
    pass
@overload
def client(
    service_name: Literal["route53"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Route53Client:
    pass
@overload
def client(
    service_name: Literal["route53domains"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Route53DomainsClient:
    pass
@overload
def client(
    service_name: Literal["route53resolver"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Route53ResolverClient:
    pass
@overload
def client(
    service_name: Literal["s3"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> S3Client:
    pass
@overload
def client(
    service_name: Literal["s3control"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> S3ControlClient:
    pass
@overload
def client(
    service_name: Literal["s3outposts"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> S3OutpostsClient:
    pass
@overload
def client(
    service_name: Literal["sagemaker"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SageMakerClient:
    pass
@overload
def client(
    service_name: Literal["sagemaker-a2i-runtime"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> AugmentedAIRuntimeClient:
    pass
@overload
def client(
    service_name: Literal["sagemaker-featurestore-runtime"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SageMakerFeatureStoreRuntimeClient:
    pass
@overload
def client(
    service_name: Literal["sagemaker-runtime"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SageMakerRuntimeClient:
    pass
@overload
def client(
    service_name: Literal["savingsplans"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SavingsPlansClient:
    pass
@overload
def client(
    service_name: Literal["schemas"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SchemasClient:
    pass
@overload
def client(
    service_name: Literal["sdb"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SimpleDBClient:
    pass
@overload
def client(
    service_name: Literal["secretsmanager"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SecretsManagerClient:
    pass
@overload
def client(
    service_name: Literal["securityhub"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SecurityHubClient:
    pass
@overload
def client(
    service_name: Literal["serverlessrepo"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ServerlessApplicationRepositoryClient:
    pass
@overload
def client(
    service_name: Literal["service-quotas"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ServiceQuotasClient:
    pass
@overload
def client(
    service_name: Literal["servicecatalog"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ServiceCatalogClient:
    pass
@overload
def client(
    service_name: Literal["servicecatalog-appregistry"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ServiceCatalogAppRegistryClient:
    pass
@overload
def client(
    service_name: Literal["servicediscovery"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ServiceDiscoveryClient:
    pass
@overload
def client(
    service_name: Literal["ses"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SESClient:
    pass
@overload
def client(
    service_name: Literal["sesv2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SESV2Client:
    pass
@overload
def client(
    service_name: Literal["shield"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> ShieldClient:
    pass
@overload
def client(
    service_name: Literal["signer"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SignerClient:
    pass
@overload
def client(
    service_name: Literal["sms"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SMSClient:
    pass
@overload
def client(
    service_name: Literal["sms-voice"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SMSVoiceClient:
    pass
@overload
def client(
    service_name: Literal["snowball"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SnowballClient:
    pass
@overload
def client(
    service_name: Literal["sns"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SNSClient:
    pass
@overload
def client(
    service_name: Literal["sqs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SQSClient:
    pass
@overload
def client(
    service_name: Literal["ssm"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SSMClient:
    pass
@overload
def client(
    service_name: Literal["sso"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SSOClient:
    pass
@overload
def client(
    service_name: Literal["sso-admin"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SSOAdminClient:
    pass
@overload
def client(
    service_name: Literal["sso-oidc"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SSOOIDCClient:
    pass
@overload
def client(
    service_name: Literal["stepfunctions"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SFNClient:
    pass
@overload
def client(
    service_name: Literal["storagegateway"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> StorageGatewayClient:
    pass
@overload
def client(
    service_name: Literal["sts"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> STSClient:
    pass
@overload
def client(
    service_name: Literal["support"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SupportClient:
    pass
@overload
def client(
    service_name: Literal["swf"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SWFClient:
    pass
@overload
def client(
    service_name: Literal["synthetics"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SyntheticsClient:
    pass
@overload
def client(
    service_name: Literal["textract"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> TextractClient:
    pass
@overload
def client(
    service_name: Literal["timestream-query"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> TimestreamQueryClient:
    pass
@overload
def client(
    service_name: Literal["timestream-write"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> TimestreamWriteClient:
    pass
@overload
def client(
    service_name: Literal["transcribe"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> TranscribeServiceClient:
    pass
@overload
def client(
    service_name: Literal["transfer"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> TransferClient:
    pass
@overload
def client(
    service_name: Literal["translate"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> TranslateClient:
    pass
@overload
def client(
    service_name: Literal["waf"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WAFClient:
    pass
@overload
def client(
    service_name: Literal["waf-regional"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WAFRegionalClient:
    pass
@overload
def client(
    service_name: Literal["wafv2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WAFV2Client:
    pass
@overload
def client(
    service_name: Literal["workdocs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WorkDocsClient:
    pass
@overload
def client(
    service_name: Literal["worklink"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WorkLinkClient:
    pass
@overload
def client(
    service_name: Literal["workmail"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WorkMailClient:
    pass
@overload
def client(
    service_name: Literal["workmailmessageflow"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WorkMailMessageFlowClient:
    pass
@overload
def client(
    service_name: Literal["workspaces"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> WorkSpacesClient:
    pass
@overload
def client(
    service_name: Literal["xray"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> XRayClient:
    pass
@overload
def resource(
    service_name: Literal["cloudformation"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudFormationServiceResource:
    pass
@overload
def resource(
    service_name: Literal["cloudwatch"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> CloudWatchServiceResource:
    pass
@overload
def resource(
    service_name: Literal["dynamodb"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> DynamoDBServiceResource:
    pass
@overload
def resource(
    service_name: Literal["ec2"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> EC2ServiceResource:
    pass
@overload
def resource(
    service_name: Literal["glacier"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> GlacierServiceResource:
    pass
@overload
def resource(
    service_name: Literal["iam"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> IAMServiceResource:
    pass
@overload
def resource(
    service_name: Literal["opsworks"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> OpsWorksServiceResource:
    pass
@overload
def resource(
    service_name: Literal["s3"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> S3ServiceResource:
    pass
@overload
def resource(
    service_name: Literal["sns"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SNSServiceResource:
    pass
@overload
def resource(
    service_name: Literal["sqs"],
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> SQSServiceResource:
    pass