"""
Main interface for pinpoint-sms-voice-v2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pinpoint_sms_voice_v2 import (
        Client,
        DescribeAccountAttributesPaginator,
        DescribeAccountLimitsPaginator,
        DescribeConfigurationSetsPaginator,
        DescribeKeywordsPaginator,
        DescribeOptOutListsPaginator,
        DescribeOptedOutNumbersPaginator,
        DescribePhoneNumbersPaginator,
        DescribePoolsPaginator,
        DescribeProtectConfigurationsPaginator,
        DescribeRegistrationAttachmentsPaginator,
        DescribeRegistrationFieldDefinitionsPaginator,
        DescribeRegistrationFieldValuesPaginator,
        DescribeRegistrationSectionDefinitionsPaginator,
        DescribeRegistrationTypeDefinitionsPaginator,
        DescribeRegistrationVersionsPaginator,
        DescribeRegistrationsPaginator,
        DescribeSenderIdsPaginator,
        DescribeSpendLimitsPaginator,
        DescribeVerifiedDestinationNumbersPaginator,
        ListPoolOriginationIdentitiesPaginator,
        ListProtectConfigurationRuleSetNumberOverridesPaginator,
        ListRegistrationAssociationsPaginator,
        PinpointSMSVoiceV2Client,
    )

    session = Session()
    client: PinpointSMSVoiceV2Client = session.client("pinpoint-sms-voice-v2")

    describe_account_attributes_paginator: DescribeAccountAttributesPaginator = client.get_paginator("describe_account_attributes")
    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_configuration_sets_paginator: DescribeConfigurationSetsPaginator = client.get_paginator("describe_configuration_sets")
    describe_keywords_paginator: DescribeKeywordsPaginator = client.get_paginator("describe_keywords")
    describe_opt_out_lists_paginator: DescribeOptOutListsPaginator = client.get_paginator("describe_opt_out_lists")
    describe_opted_out_numbers_paginator: DescribeOptedOutNumbersPaginator = client.get_paginator("describe_opted_out_numbers")
    describe_phone_numbers_paginator: DescribePhoneNumbersPaginator = client.get_paginator("describe_phone_numbers")
    describe_pools_paginator: DescribePoolsPaginator = client.get_paginator("describe_pools")
    describe_protect_configurations_paginator: DescribeProtectConfigurationsPaginator = client.get_paginator("describe_protect_configurations")
    describe_registration_attachments_paginator: DescribeRegistrationAttachmentsPaginator = client.get_paginator("describe_registration_attachments")
    describe_registration_field_definitions_paginator: DescribeRegistrationFieldDefinitionsPaginator = client.get_paginator("describe_registration_field_definitions")
    describe_registration_field_values_paginator: DescribeRegistrationFieldValuesPaginator = client.get_paginator("describe_registration_field_values")
    describe_registration_section_definitions_paginator: DescribeRegistrationSectionDefinitionsPaginator = client.get_paginator("describe_registration_section_definitions")
    describe_registration_type_definitions_paginator: DescribeRegistrationTypeDefinitionsPaginator = client.get_paginator("describe_registration_type_definitions")
    describe_registration_versions_paginator: DescribeRegistrationVersionsPaginator = client.get_paginator("describe_registration_versions")
    describe_registrations_paginator: DescribeRegistrationsPaginator = client.get_paginator("describe_registrations")
    describe_sender_ids_paginator: DescribeSenderIdsPaginator = client.get_paginator("describe_sender_ids")
    describe_spend_limits_paginator: DescribeSpendLimitsPaginator = client.get_paginator("describe_spend_limits")
    describe_verified_destination_numbers_paginator: DescribeVerifiedDestinationNumbersPaginator = client.get_paginator("describe_verified_destination_numbers")
    list_pool_origination_identities_paginator: ListPoolOriginationIdentitiesPaginator = client.get_paginator("list_pool_origination_identities")
    list_protect_configuration_rule_set_number_overrides_paginator: ListProtectConfigurationRuleSetNumberOverridesPaginator = client.get_paginator("list_protect_configuration_rule_set_number_overrides")
    list_registration_associations_paginator: ListRegistrationAssociationsPaginator = client.get_paginator("list_registration_associations")
    ```
"""

from .client import PinpointSMSVoiceV2Client
from .paginator import (
    DescribeAccountAttributesPaginator,
    DescribeAccountLimitsPaginator,
    DescribeConfigurationSetsPaginator,
    DescribeKeywordsPaginator,
    DescribeOptedOutNumbersPaginator,
    DescribeOptOutListsPaginator,
    DescribePhoneNumbersPaginator,
    DescribePoolsPaginator,
    DescribeProtectConfigurationsPaginator,
    DescribeRegistrationAttachmentsPaginator,
    DescribeRegistrationFieldDefinitionsPaginator,
    DescribeRegistrationFieldValuesPaginator,
    DescribeRegistrationSectionDefinitionsPaginator,
    DescribeRegistrationsPaginator,
    DescribeRegistrationTypeDefinitionsPaginator,
    DescribeRegistrationVersionsPaginator,
    DescribeSenderIdsPaginator,
    DescribeSpendLimitsPaginator,
    DescribeVerifiedDestinationNumbersPaginator,
    ListPoolOriginationIdentitiesPaginator,
    ListProtectConfigurationRuleSetNumberOverridesPaginator,
    ListRegistrationAssociationsPaginator,
)

Client = PinpointSMSVoiceV2Client

__all__ = (
    "Client",
    "DescribeAccountAttributesPaginator",
    "DescribeAccountLimitsPaginator",
    "DescribeConfigurationSetsPaginator",
    "DescribeKeywordsPaginator",
    "DescribeOptOutListsPaginator",
    "DescribeOptedOutNumbersPaginator",
    "DescribePhoneNumbersPaginator",
    "DescribePoolsPaginator",
    "DescribeProtectConfigurationsPaginator",
    "DescribeRegistrationAttachmentsPaginator",
    "DescribeRegistrationFieldDefinitionsPaginator",
    "DescribeRegistrationFieldValuesPaginator",
    "DescribeRegistrationSectionDefinitionsPaginator",
    "DescribeRegistrationTypeDefinitionsPaginator",
    "DescribeRegistrationVersionsPaginator",
    "DescribeRegistrationsPaginator",
    "DescribeSenderIdsPaginator",
    "DescribeSpendLimitsPaginator",
    "DescribeVerifiedDestinationNumbersPaginator",
    "ListPoolOriginationIdentitiesPaginator",
    "ListProtectConfigurationRuleSetNumberOverridesPaginator",
    "ListRegistrationAssociationsPaginator",
    "PinpointSMSVoiceV2Client",
)
