"""
Main interface for devicefarm service type definitions.

Usage::

    ```python
    from mypy_boto3_devicefarm.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountSettingsTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeviceFilterTypeDef",
    "DeviceInstanceTypeDef",
    "DeviceMinutesTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "DevicePoolTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceTypeDef",
    "IncompatibilityMessageTypeDef",
    "InstanceProfileTypeDef",
    "JobTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "NetworkProfileTypeDef",
    "OfferingPromotionTypeDef",
    "OfferingStatusTypeDef",
    "OfferingTransactionTypeDef",
    "OfferingTypeDef",
    "ProblemDetailTypeDef",
    "ProblemTypeDef",
    "ProjectTypeDef",
    "RadiosTypeDef",
    "RecurringChargeTypeDef",
    "RemoteAccessSessionTypeDef",
    "ResolutionTypeDef",
    "RuleTypeDef",
    "RunTypeDef",
    "SampleTypeDef",
    "SuiteTypeDef",
    "TagTypeDef",
    "TestGridProjectTypeDef",
    "TestGridSessionActionTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TestGridSessionTypeDef",
    "TestTypeDef",
    "TrialMinutesTypeDef",
    "UniqueProblemTypeDef",
    "UploadTypeDef",
    "VPCEConfigurationTypeDef",
    "CreateDevicePoolResultTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "CreateProjectResultTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "CreateUploadResultTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetAccountSettingsResultTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetDevicePoolResultTypeDef",
    "GetDeviceResultTypeDef",
    "GetInstanceProfileResultTypeDef",
    "GetJobResultTypeDef",
    "GetNetworkProfileResultTypeDef",
    "GetOfferingStatusResultTypeDef",
    "GetProjectResultTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "GetRunResultTypeDef",
    "GetSuiteResultTypeDef",
    "GetTestGridProjectResultTypeDef",
    "GetTestGridSessionResultTypeDef",
    "GetTestResultTypeDef",
    "GetUploadResultTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "ListArtifactsResultTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "ListDevicePoolsResultTypeDef",
    "ListDevicesResultTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "ListJobsResultTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "ListOfferingsResultTypeDef",
    "ListProjectsResultTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "ListRunsResultTypeDef",
    "ListSamplesResultTypeDef",
    "ListSuitesResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListTestsResultTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListUploadsResultTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RenewOfferingResultTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "ScheduleRunResultTypeDef",
    "ScheduleRunTestTypeDef",
    "StopJobResultTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "StopRunResultTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "UpdateProjectResultTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "UpdateUploadResultTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": str,
        "unmeteredDevices": Dict[Literal["ANDROID", "IOS"], int],
        "unmeteredRemoteAccessDevices": Dict[Literal["ANDROID", "IOS"], int],
        "maxJobTimeoutMinutes": int,
        "trialMinutes": "TrialMinutesTypeDef",
        "maxSlots": Dict[str, int],
        "defaultJobTimeoutMinutes": int,
        "skipAppResign": bool,
    },
    total=False,
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "UNKNOWN",
            "SCREENSHOT",
            "DEVICE_LOG",
            "MESSAGE_LOG",
            "VIDEO_LOG",
            "RESULT_LOG",
            "SERVICE_LOG",
            "WEBKIT_LOG",
            "INSTRUMENTATION_OUTPUT",
            "EXERCISER_MONKEY_OUTPUT",
            "CALABASH_JSON_OUTPUT",
            "CALABASH_PRETTY_OUTPUT",
            "CALABASH_STANDARD_OUTPUT",
            "CALABASH_JAVA_XML_OUTPUT",
            "AUTOMATION_OUTPUT",
            "APPIUM_SERVER_OUTPUT",
            "APPIUM_JAVA_OUTPUT",
            "APPIUM_JAVA_XML_OUTPUT",
            "APPIUM_PYTHON_OUTPUT",
            "APPIUM_PYTHON_XML_OUTPUT",
            "EXPLORER_EVENT_LOG",
            "EXPLORER_SUMMARY_LOG",
            "APPLICATION_CRASH_REPORT",
            "XCTEST_LOG",
            "VIDEO",
            "CUSTOMER_ARTIFACT",
            "CUSTOMER_ARTIFACT_LOG",
            "TESTSPEC_OUTPUT",
        ],
        "extension": str,
        "url": str,
    },
    total=False,
)

CPUTypeDef = TypedDict(
    "CPUTypeDef", {"frequency": str, "architecture": str, "clock": float}, total=False
)

CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": int,
        "passed": int,
        "failed": int,
        "warned": int,
        "errored": int,
        "stopped": int,
        "skipped": int,
    },
    total=False,
)

CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {"iosPaths": List[str], "androidPaths": List[str], "deviceHostPaths": List[str]},
    total=False,
)

DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "values": List[str],
    },
    total=False,
)

DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": str,
        "deviceArn": str,
        "labels": List[str],
        "status": Literal["IN_USE", "PREPARING", "AVAILABLE", "NOT_AVAILABLE"],
        "udid": str,
        "instanceProfile": "InstanceProfileTypeDef",
    },
    total=False,
)

DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef", {"total": float, "metered": float, "unmetered": float}, total=False
)

DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": "DeviceTypeDef",
        "compatible": bool,
        "incompatibilityMessages": List["IncompatibilityMessageTypeDef"],
    },
    total=False,
)

DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "rules": List["RuleTypeDef"],
        "maxDevices": int,
    },
    total=False,
)

DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {"filters": List["DeviceFilterTypeDef"], "matchedDevicesCount": int, "maxDevices": int},
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": str,
        "name": str,
        "manufacturer": str,
        "model": str,
        "modelId": str,
        "formFactor": Literal["PHONE", "TABLET"],
        "platform": Literal["ANDROID", "IOS"],
        "os": str,
        "cpu": "CPUTypeDef",
        "resolution": "ResolutionTypeDef",
        "heapSize": int,
        "memory": int,
        "image": str,
        "carrier": str,
        "radio": str,
        "remoteAccessEnabled": bool,
        "remoteDebugEnabled": bool,
        "fleetType": str,
        "fleetName": str,
        "instances": List["DeviceInstanceTypeDef"],
        "availability": Literal["TEMPORARY_NOT_AVAILABLE", "BUSY", "AVAILABLE", "HIGHLY_AVAILABLE"],
    },
    total=False,
)

IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": str,
        "type": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
    },
    total=False,
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": str,
        "packageCleanup": bool,
        "excludeAppPackagesFromCleanup": List[str],
        "rebootAfterUse": bool,
        "name": str,
        "description": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
        "videoEndpoint": str,
        "videoCapture": bool,
    },
    total=False,
)

LocationTypeDef = TypedDict("LocationTypeDef", {"latitude": float, "longitude": float})

MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef", {"amount": float, "currencyCode": Literal["USD"]}, total=False
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CURATED", "PRIVATE"],
        "uplinkBandwidthBits": int,
        "downlinkBandwidthBits": int,
        "uplinkDelayMs": int,
        "downlinkDelayMs": int,
        "uplinkJitterMs": int,
        "downlinkJitterMs": int,
        "uplinkLossPercent": int,
        "downlinkLossPercent": int,
    },
    total=False,
)

OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef", {"id": str, "description": str}, total=False
)

OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": Literal["PURCHASE", "RENEW", "SYSTEM"],
        "offering": "OfferingTypeDef",
        "quantity": int,
        "effectiveOn": datetime,
    },
    total=False,
)

OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": "OfferingStatusTypeDef",
        "transactionId": str,
        "offeringPromotionId": str,
        "createdOn": datetime,
        "cost": "MonetaryAmountTypeDef",
    },
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": str,
        "description": str,
        "type": Literal["RECURRING"],
        "platform": Literal["ANDROID", "IOS"],
        "recurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ProblemDetailTypeDef = TypedDict("ProblemDetailTypeDef", {"arn": str, "name": str}, total=False)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": "ProblemDetailTypeDef",
        "job": "ProblemDetailTypeDef",
        "suite": "ProblemDetailTypeDef",
        "test": "ProblemDetailTypeDef",
        "device": "DeviceTypeDef",
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
    },
    total=False,
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {"arn": str, "name": str, "defaultJobTimeoutMinutes": int, "created": datetime},
    total=False,
)

RadiosTypeDef = TypedDict(
    "RadiosTypeDef", {"wifi": bool, "bluetooth": bool, "nfc": bool, "gps": bool}, total=False
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"cost": "MonetaryAmountTypeDef", "frequency": Literal["MONTHLY"]},
    total=False,
)

RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "message": str,
        "started": datetime,
        "stopped": datetime,
        "device": "DeviceTypeDef",
        "instanceArn": str,
        "remoteDebugEnabled": bool,
        "remoteRecordEnabled": bool,
        "remoteRecordAppArn": str,
        "hostAddress": str,
        "clientId": str,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": "DeviceMinutesTypeDef",
        "endpoint": str,
        "deviceUdid": str,
        "interactionMode": Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"],
        "skipAppResign": bool,
    },
    total=False,
)

ResolutionTypeDef = TypedDict("ResolutionTypeDef", {"width": int, "height": int}, total=False)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": Literal[
            "ARN",
            "PLATFORM",
            "FORM_FACTOR",
            "MANUFACTURER",
            "REMOTE_ACCESS_ENABLED",
            "REMOTE_DEBUG_ENABLED",
            "APPIUM_VERSION",
            "INSTANCE_ARN",
            "INSTANCE_LABELS",
            "FLEET_TYPE",
            "OS_VERSION",
            "MODEL",
            "AVAILABILITY",
        ],
        "operator": Literal[
            "EQUALS",
            "LESS_THAN",
            "LESS_THAN_OR_EQUALS",
            "GREATER_THAN",
            "GREATER_THAN_OR_EQUALS",
            "IN",
            "NOT_IN",
            "CONTAINS",
        ],
        "value": str,
    },
    total=False,
)

RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "platform": Literal["ANDROID", "IOS"],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "totalJobs": int,
        "completedJobs": int,
        "billingMethod": Literal["METERED", "UNMETERED"],
        "deviceMinutes": "DeviceMinutesTypeDef",
        "networkProfile": "NetworkProfileTypeDef",
        "parsingResultUrl": str,
        "resultCode": Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"],
        "seed": int,
        "appUpload": str,
        "eventCount": int,
        "jobTimeoutMinutes": int,
        "devicePoolArn": str,
        "locale": str,
        "radios": "RadiosTypeDef",
        "location": "LocationTypeDef",
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "webUrl": str,
        "skipAppResign": bool,
        "testSpecArn": str,
        "deviceSelectionResult": "DeviceSelectionResultTypeDef",
    },
    total=False,
)

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": str,
        "type": Literal[
            "CPU",
            "MEMORY",
            "THREADS",
            "RX_RATE",
            "TX_RATE",
            "RX",
            "TX",
            "NATIVE_FRAMES",
            "NATIVE_FPS",
            "NATIVE_MIN_DRAWTIME",
            "NATIVE_AVG_DRAWTIME",
            "NATIVE_MAX_DRAWTIME",
            "OPENGL_FRAMES",
            "OPENGL_FPS",
            "OPENGL_MIN_DRAWTIME",
            "OPENGL_AVG_DRAWTIME",
            "OPENGL_MAX_DRAWTIME",
        ],
        "url": str,
    },
    total=False,
)

SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {"arn": str, "name": str, "description": str, "created": datetime},
    total=False,
)

TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {"action": str, "started": datetime, "duration": int, "statusCode": str, "requestMethod": str},
    total=False,
)

TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {"filename": str, "type": Literal["UNKNOWN", "VIDEO", "SELENIUM_LOG"], "url": str},
    total=False,
)

TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": str,
        "status": Literal["ACTIVE", "CLOSED", "ERRORED"],
        "created": datetime,
        "ended": datetime,
        "billingMinutes": float,
        "seleniumProperties": str,
    },
    total=False,
)

TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ],
        "created": datetime,
        "status": Literal[
            "PENDING",
            "PENDING_CONCURRENCY",
            "PENDING_DEVICE",
            "PROCESSING",
            "SCHEDULING",
            "PREPARING",
            "RUNNING",
            "COMPLETED",
            "STOPPING",
        ],
        "result": Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
        "started": datetime,
        "stopped": datetime,
        "counters": "CountersTypeDef",
        "message": str,
        "deviceMinutes": "DeviceMinutesTypeDef",
    },
    total=False,
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef", {"total": float, "remaining": float}, total=False
)

UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef", {"message": str, "problems": List["ProblemTypeDef"]}, total=False
)

UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": str,
        "name": str,
        "created": datetime,
        "type": Literal[
            "ANDROID_APP",
            "IOS_APP",
            "WEB_APP",
            "EXTERNAL_DATA",
            "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_PYTHON_TEST_PACKAGE",
            "APPIUM_NODE_TEST_PACKAGE",
            "APPIUM_RUBY_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
            "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
            "APPIUM_WEB_PYTHON_TEST_PACKAGE",
            "APPIUM_WEB_NODE_TEST_PACKAGE",
            "APPIUM_WEB_RUBY_TEST_PACKAGE",
            "CALABASH_TEST_PACKAGE",
            "INSTRUMENTATION_TEST_PACKAGE",
            "UIAUTOMATION_TEST_PACKAGE",
            "UIAUTOMATOR_TEST_PACKAGE",
            "XCTEST_TEST_PACKAGE",
            "XCTEST_UI_TEST_PACKAGE",
            "APPIUM_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_PYTHON_TEST_SPEC",
            "APPIUM_NODE_TEST_SPEC",
            "APPIUM_RUBY_TEST_SPEC",
            "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
            "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
            "APPIUM_WEB_PYTHON_TEST_SPEC",
            "APPIUM_WEB_NODE_TEST_SPEC",
            "APPIUM_WEB_RUBY_TEST_SPEC",
            "INSTRUMENTATION_TEST_SPEC",
            "XCTEST_UI_TEST_SPEC",
        ],
        "status": Literal["INITIALIZED", "PROCESSING", "SUCCEEDED", "FAILED"],
        "url": str,
        "metadata": str,
        "contentType": str,
        "message": str,
        "category": Literal["CURATED", "PRIVATE"],
    },
    total=False,
)

VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": str,
    },
    total=False,
)

CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef", {"devicePool": "DevicePoolTypeDef"}, total=False
)

CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef", {"instanceProfile": "InstanceProfileTypeDef"}, total=False
)

CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef", {"networkProfile": "NetworkProfileTypeDef"}, total=False
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef", {"project": "ProjectTypeDef"}, total=False
)

CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {"billingMethod": Literal["METERED", "UNMETERED"], "vpceConfigurationArns": List[str]},
    total=False,
)

CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {"remoteAccessSession": "RemoteAccessSessionTypeDef"},
    total=False,
)

CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef", {"testGridProject": "TestGridProjectTypeDef"}, total=False
)

CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef", {"url": str, "expires": datetime}, total=False
)

CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef", {"upload": "UploadTypeDef"}, total=False
)

CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {"vpceConfiguration": "VPCEConfigurationTypeDef"},
    total=False,
)

DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {"filters": List["DeviceFilterTypeDef"], "maxDevices": int},
)

ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": int,
        "accountsCleanup": bool,
        "appPackagesCleanup": bool,
        "videoCapture": bool,
        "skipAppResign": bool,
    },
    total=False,
)

GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef", {"accountSettings": "AccountSettingsTypeDef"}, total=False
)

GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef", {"deviceInstance": "DeviceInstanceTypeDef"}, total=False
)

GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
        "incompatibleDevices": List["DevicePoolCompatibilityResultTypeDef"],
    },
    total=False,
)

GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef", {"devicePool": "DevicePoolTypeDef"}, total=False
)

GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef", {"device": "DeviceTypeDef"}, total=False
)

GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef", {"instanceProfile": "InstanceProfileTypeDef"}, total=False
)

GetJobResultTypeDef = TypedDict("GetJobResultTypeDef", {"job": "JobTypeDef"}, total=False)

GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef", {"networkProfile": "NetworkProfileTypeDef"}, total=False
)

GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, "OfferingStatusTypeDef"],
        "nextPeriod": Dict[str, "OfferingStatusTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef", {"project": "ProjectTypeDef"}, total=False
)

GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {"remoteAccessSession": "RemoteAccessSessionTypeDef"},
    total=False,
)

GetRunResultTypeDef = TypedDict("GetRunResultTypeDef", {"run": "RunTypeDef"}, total=False)

GetSuiteResultTypeDef = TypedDict("GetSuiteResultTypeDef", {"suite": "SuiteTypeDef"}, total=False)

GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef", {"testGridProject": "TestGridProjectTypeDef"}, total=False
)

GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef", {"testGridSession": "TestGridSessionTypeDef"}, total=False
)

GetTestResultTypeDef = TypedDict("GetTestResultTypeDef", {"test": "TestTypeDef"}, total=False)

GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef", {"upload": "UploadTypeDef"}, total=False
)

GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {"vpceConfiguration": "VPCEConfigurationTypeDef"},
    total=False,
)

InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef", {"appUpload": "UploadTypeDef"}, total=False
)

ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {"artifacts": List["ArtifactTypeDef"], "nextToken": str},
    total=False,
)

ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {"deviceInstances": List["DeviceInstanceTypeDef"], "nextToken": str},
    total=False,
)

ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {"devicePools": List["DevicePoolTypeDef"], "nextToken": str},
    total=False,
)

ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef", {"devices": List["DeviceTypeDef"], "nextToken": str}, total=False
)

ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {"instanceProfiles": List["InstanceProfileTypeDef"], "nextToken": str},
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef", {"jobs": List["JobTypeDef"], "nextToken": str}, total=False
)

ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {"networkProfiles": List["NetworkProfileTypeDef"], "nextToken": str},
    total=False,
)

ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {"offeringPromotions": List["OfferingPromotionTypeDef"], "nextToken": str},
    total=False,
)

ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {"offeringTransactions": List["OfferingTransactionTypeDef"], "nextToken": str},
    total=False,
)

ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {"offerings": List["OfferingTypeDef"], "nextToken": str},
    total=False,
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef", {"projects": List["ProjectTypeDef"], "nextToken": str}, total=False
)

ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {"remoteAccessSessions": List["RemoteAccessSessionTypeDef"], "nextToken": str},
    total=False,
)

ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef", {"runs": List["RunTypeDef"], "nextToken": str}, total=False
)

ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef", {"samples": List["SampleTypeDef"], "nextToken": str}, total=False
)

ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef", {"suites": List["SuiteTypeDef"], "nextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {"testGridProjects": List["TestGridProjectTypeDef"], "nextToken": str},
    total=False,
)

ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {"actions": List["TestGridSessionActionTypeDef"], "nextToken": str},
    total=False,
)

ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {"artifacts": List["TestGridSessionArtifactTypeDef"], "nextToken": str},
    total=False,
)

ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {"testGridSessions": List["TestGridSessionTypeDef"], "nextToken": str},
    total=False,
)

ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef", {"tests": List["TestTypeDef"], "nextToken": str}, total=False
)

ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[
            Literal["PENDING", "PASSED", "WARNED", "FAILED", "SKIPPED", "ERRORED", "STOPPED"],
            List["UniqueProblemTypeDef"],
        ],
        "nextToken": str,
    },
    total=False,
)

ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef", {"uploads": List["UploadTypeDef"], "nextToken": str}, total=False
)

ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {"vpceConfigurations": List["VPCEConfigurationTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {"offeringTransaction": "OfferingTransactionTypeDef"},
    total=False,
)

RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef", {"offeringTransaction": "OfferingTransactionTypeDef"}, total=False
)

ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": str,
        "networkProfileArn": str,
        "locale": str,
        "location": "LocationTypeDef",
        "vpceConfigurationArns": List[str],
        "customerArtifactPaths": "CustomerArtifactPathsTypeDef",
        "radios": "RadiosTypeDef",
        "auxiliaryApps": List[str],
        "billingMethod": Literal["METERED", "UNMETERED"],
    },
    total=False,
)

ScheduleRunResultTypeDef = TypedDict("ScheduleRunResultTypeDef", {"run": "RunTypeDef"}, total=False)

_RequiredScheduleRunTestTypeDef = TypedDict(
    "_RequiredScheduleRunTestTypeDef",
    {
        "type": Literal[
            "BUILTIN_FUZZ",
            "BUILTIN_EXPLORER",
            "WEB_PERFORMANCE_PROFILE",
            "APPIUM_JAVA_JUNIT",
            "APPIUM_JAVA_TESTNG",
            "APPIUM_PYTHON",
            "APPIUM_NODE",
            "APPIUM_RUBY",
            "APPIUM_WEB_JAVA_JUNIT",
            "APPIUM_WEB_JAVA_TESTNG",
            "APPIUM_WEB_PYTHON",
            "APPIUM_WEB_NODE",
            "APPIUM_WEB_RUBY",
            "CALABASH",
            "INSTRUMENTATION",
            "UIAUTOMATION",
            "UIAUTOMATOR",
            "XCTEST",
            "XCTEST_UI",
            "REMOTE_ACCESS_RECORD",
            "REMOTE_ACCESS_REPLAY",
        ]
    },
)
_OptionalScheduleRunTestTypeDef = TypedDict(
    "_OptionalScheduleRunTestTypeDef",
    {"testPackageArn": str, "testSpecArn": str, "filter": str, "parameters": Dict[str, str]},
    total=False,
)


class ScheduleRunTestTypeDef(_RequiredScheduleRunTestTypeDef, _OptionalScheduleRunTestTypeDef):
    pass


StopJobResultTypeDef = TypedDict("StopJobResultTypeDef", {"job": "JobTypeDef"}, total=False)

StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {"remoteAccessSession": "RemoteAccessSessionTypeDef"},
    total=False,
)

StopRunResultTypeDef = TypedDict("StopRunResultTypeDef", {"run": "RunTypeDef"}, total=False)

UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef", {"deviceInstance": "DeviceInstanceTypeDef"}, total=False
)

UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef", {"devicePool": "DevicePoolTypeDef"}, total=False
)

UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef", {"instanceProfile": "InstanceProfileTypeDef"}, total=False
)

UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef", {"networkProfile": "NetworkProfileTypeDef"}, total=False
)

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef", {"project": "ProjectTypeDef"}, total=False
)

UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef", {"testGridProject": "TestGridProjectTypeDef"}, total=False
)

UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef", {"upload": "UploadTypeDef"}, total=False
)

UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {"vpceConfiguration": "VPCEConfigurationTypeDef"},
    total=False,
)
