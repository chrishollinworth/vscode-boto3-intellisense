"""
Type annotations for license-manager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/literals.html)

Usage::

    ```python
    from mypy_boto3_license_manager.literals import ActivationOverrideBehaviorType

    data: ActivationOverrideBehaviorType = "ALL_GRANTS_PERMITTED_BY_ISSUER"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActivationOverrideBehaviorType",
    "AllowedOperationType",
    "CheckoutTypeType",
    "DigitalSignatureMethodType",
    "EntitlementDataUnitType",
    "EntitlementUnitType",
    "GrantStatusType",
    "InventoryFilterConditionType",
    "LicenseConfigurationStatusType",
    "LicenseConversionTaskStatusType",
    "LicenseCountingTypeType",
    "LicenseDeletionStatusType",
    "LicenseStatusType",
    "ListAssociationsForLicenseConfigurationPaginatorName",
    "ListLicenseConfigurationsPaginatorName",
    "ListLicenseSpecificationsForResourcePaginatorName",
    "ListResourceInventoryPaginatorName",
    "ListUsageForLicenseConfigurationPaginatorName",
    "ReceivedStatusType",
    "RenewTypeType",
    "ReportFrequencyTypeType",
    "ReportTypeType",
    "ResourceTypeType",
    "TokenTypeType",
)

ActivationOverrideBehaviorType = Literal[
    "ALL_GRANTS_PERMITTED_BY_ISSUER", "DISTRIBUTED_GRANTS_ONLY"
]
AllowedOperationType = Literal[
    "CheckInLicense",
    "CheckoutBorrowLicense",
    "CheckoutLicense",
    "CreateGrant",
    "CreateToken",
    "ExtendConsumptionLicense",
    "ListPurchasedLicenses",
]
CheckoutTypeType = Literal["PERPETUAL", "PROVISIONAL"]
DigitalSignatureMethodType = Literal["JWT_PS384"]
EntitlementDataUnitType = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
EntitlementUnitType = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
GrantStatusType = Literal[
    "ACTIVE",
    "DELETED",
    "DISABLED",
    "FAILED_WORKFLOW",
    "PENDING_ACCEPT",
    "PENDING_DELETE",
    "PENDING_WORKFLOW",
    "REJECTED",
    "WORKFLOW_COMPLETED",
]
InventoryFilterConditionType = Literal["BEGINS_WITH", "CONTAINS", "EQUALS", "NOT_EQUALS"]
LicenseConfigurationStatusType = Literal["AVAILABLE", "DISABLED"]
LicenseConversionTaskStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
LicenseCountingTypeType = Literal["Core", "Instance", "Socket", "vCPU"]
LicenseDeletionStatusType = Literal["DELETED", "PENDING_DELETE"]
LicenseStatusType = Literal[
    "AVAILABLE",
    "DEACTIVATED",
    "DELETED",
    "EXPIRED",
    "PENDING_AVAILABLE",
    "PENDING_DELETE",
    "SUSPENDED",
]
ListAssociationsForLicenseConfigurationPaginatorName = Literal[
    "list_associations_for_license_configuration"
]
ListLicenseConfigurationsPaginatorName = Literal["list_license_configurations"]
ListLicenseSpecificationsForResourcePaginatorName = Literal[
    "list_license_specifications_for_resource"
]
ListResourceInventoryPaginatorName = Literal["list_resource_inventory"]
ListUsageForLicenseConfigurationPaginatorName = Literal["list_usage_for_license_configuration"]
ReceivedStatusType = Literal[
    "ACTIVE",
    "DELETED",
    "DISABLED",
    "FAILED_WORKFLOW",
    "PENDING_ACCEPT",
    "PENDING_WORKFLOW",
    "REJECTED",
    "WORKFLOW_COMPLETED",
]
RenewTypeType = Literal["Monthly", "None", "Weekly"]
ReportFrequencyTypeType = Literal["DAY", "MONTH", "WEEK"]
ReportTypeType = Literal["LicenseConfigurationSummaryReport", "LicenseConfigurationUsageReport"]
ResourceTypeType = Literal[
    "EC2_AMI", "EC2_HOST", "EC2_INSTANCE", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
]
TokenTypeType = Literal["REFRESH_TOKEN"]
