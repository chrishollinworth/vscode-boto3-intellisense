"""
Main interface for waf service.

Usage::

    ```python
    import boto3
    from mypy_boto3_waf import (
        Client,
        GetRateBasedRuleManagedKeysPaginator,
        ListActivatedRulesInRuleGroupPaginator,
        ListByteMatchSetsPaginator,
        ListGeoMatchSetsPaginator,
        ListIPSetsPaginator,
        ListLoggingConfigurationsPaginator,
        ListRateBasedRulesPaginator,
        ListRegexMatchSetsPaginator,
        ListRegexPatternSetsPaginator,
        ListRuleGroupsPaginator,
        ListRulesPaginator,
        ListSizeConstraintSetsPaginator,
        ListSqlInjectionMatchSetsPaginator,
        ListSubscribedRuleGroupsPaginator,
        ListWebACLsPaginator,
        ListXssMatchSetsPaginator,
        WAFClient,
    )

    session = boto3.Session()

    client: WAFClient = boto3.client("waf")
    session_client: WAFClient = session.client("waf")

    get_rate_based_rule_managed_keys_paginator: GetRateBasedRuleManagedKeysPaginator = client.get_paginator("get_rate_based_rule_managed_keys")
    list_activated_rules_in_rule_group_paginator: ListActivatedRulesInRuleGroupPaginator = client.get_paginator("list_activated_rules_in_rule_group")
    list_byte_match_sets_paginator: ListByteMatchSetsPaginator = client.get_paginator("list_byte_match_sets")
    list_geo_match_sets_paginator: ListGeoMatchSetsPaginator = client.get_paginator("list_geo_match_sets")
    list_ip_sets_paginator: ListIPSetsPaginator = client.get_paginator("list_ip_sets")
    list_logging_configurations_paginator: ListLoggingConfigurationsPaginator = client.get_paginator("list_logging_configurations")
    list_rate_based_rules_paginator: ListRateBasedRulesPaginator = client.get_paginator("list_rate_based_rules")
    list_regex_match_sets_paginator: ListRegexMatchSetsPaginator = client.get_paginator("list_regex_match_sets")
    list_regex_pattern_sets_paginator: ListRegexPatternSetsPaginator = client.get_paginator("list_regex_pattern_sets")
    list_rule_groups_paginator: ListRuleGroupsPaginator = client.get_paginator("list_rule_groups")
    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    list_size_constraint_sets_paginator: ListSizeConstraintSetsPaginator = client.get_paginator("list_size_constraint_sets")
    list_sql_injection_match_sets_paginator: ListSqlInjectionMatchSetsPaginator = client.get_paginator("list_sql_injection_match_sets")
    list_subscribed_rule_groups_paginator: ListSubscribedRuleGroupsPaginator = client.get_paginator("list_subscribed_rule_groups")
    list_web_acls_paginator: ListWebACLsPaginator = client.get_paginator("list_web_acls")
    list_xss_match_sets_paginator: ListXssMatchSetsPaginator = client.get_paginator("list_xss_match_sets")
    ```
"""
from mypy_boto3_waf.client import WAFClient
from mypy_boto3_waf.paginator import (
    GetRateBasedRuleManagedKeysPaginator,
    ListActivatedRulesInRuleGroupPaginator,
    ListByteMatchSetsPaginator,
    ListGeoMatchSetsPaginator,
    ListIPSetsPaginator,
    ListLoggingConfigurationsPaginator,
    ListRateBasedRulesPaginator,
    ListRegexMatchSetsPaginator,
    ListRegexPatternSetsPaginator,
    ListRuleGroupsPaginator,
    ListRulesPaginator,
    ListSizeConstraintSetsPaginator,
    ListSqlInjectionMatchSetsPaginator,
    ListSubscribedRuleGroupsPaginator,
    ListWebACLsPaginator,
    ListXssMatchSetsPaginator,
)

Client = WAFClient


__all__ = (
    "Client",
    "GetRateBasedRuleManagedKeysPaginator",
    "ListActivatedRulesInRuleGroupPaginator",
    "ListByteMatchSetsPaginator",
    "ListGeoMatchSetsPaginator",
    "ListIPSetsPaginator",
    "ListLoggingConfigurationsPaginator",
    "ListRateBasedRulesPaginator",
    "ListRegexMatchSetsPaginator",
    "ListRegexPatternSetsPaginator",
    "ListRuleGroupsPaginator",
    "ListRulesPaginator",
    "ListSizeConstraintSetsPaginator",
    "ListSqlInjectionMatchSetsPaginator",
    "ListSubscribedRuleGroupsPaginator",
    "ListWebACLsPaginator",
    "ListXssMatchSetsPaginator",
    "WAFClient",
)
