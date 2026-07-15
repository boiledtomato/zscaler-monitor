# ZIA リリースノート

> 最終更新: 2026-07-15 23:31 UTC  
> ソース: https://help.zscaler.com/zia/release-notes

---

# ZIA Release Notes Index


## Internet & SaaS (ZIA) Release Notes

### Internet & SaaS Service Release Notes
- [Release Upgrade Summary (2026)](/zia/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](/zia/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](/zia/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](/zia/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](/zia/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](/zia/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](/zia/release-upgrade-summary-2020)
- [Release Upgrade Summary (2019)](/zia/release-upgrade-summary-2019)

### Zscaler Endpoint DLP Release Notes
- [Zscaler Endpoint DLP Release Summary (2026)](/zia/zscaler-endpoint-dlp-release-summary-2026)

## Private Access (ZPA) Release Notes

### ZPA Service Release Notes
- [Release Upgrade Summary (2026)](/zpa/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](/zpa/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](/zpa/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](/zpa/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](/zpa/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](/zpa/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](/zpa/release-upgrade-summary-2020)
- [Release Upgrade Summary (2019)](/zpa/release-upgrade-summary-2019)

### ZPA App Connector Release Notes
- [App Connector Release Summary (2026)](/zpa/app-connector-release-summary-2026)
- [App Connector Release Summary (2025)](/zpa/app-connector-release-summary-2025)
- [App Connector Release Summary (2024)](/zpa/app-connector-release-summary-2024)
- [App Connector Release Summary (2023)](/zpa/app-connector-release-summary-2023)
- [App Connector Release Summary (2022)](/zpa/app-connector-release-summary-2022)
- [App Connector Release Summary (2021)](/zpa/app-connector-release-summary-2021)
- [App Connector Release Summary (2020)](/zpa/app-connector-release-summary-2020)

### ZPA Private Service Edge Release Notes
- [ZPA Private Service Edge Release Summary (2026)](/zpa/zpa-private-service-edge-release-summary-2026)
- [ZPA Private Service Edge Release Summary (2025)](/zpa/zpa-private-service-edge-release-summary-2025)
- [ZPA Private Service Edge Release Summary (2024)](/zpa/zpa-private-service-edge-release-summary-2024)
- [ZPA Private Service Edge Release Summary (2023)](/zpa/zpa-private-service-edge-release-summary-2023)
- [ZPA Private Service Edge Release Summary (2022)](/zpa/zpa-private-service-edge-release-summary-2022)
- [ZPA Private Service Edge Release Summary (2021)](/zpa/zpa-private-service-edge-release-summary-2021)
- [ZPA Private Service Edge Release Summary (2020)](/zpa/zpa-private-service-edge-release-summary-2020)

## Digital Experience Monitoring (ZDX) Release Notes

## Workflow Automation Release Notes

## Data Security Posture Management (DSPM) Release Notes


# ZIA 2026 Release Upgrade Summary

This article provides a summary of all new features and enhancements per Zscaler cloud for Zscaler Internet Access (ZIA). Zscaler will email a notification to your organization's registered support contacts approximately one week before your cloud is upgraded. To see scheduled maintenance updates for your cloud, visit the [Trust Portal](https://trust.zscaler.com).

## July 06, 2026

### Feature Available

#### New Cloud Applications
New cloud applications are added to the cloud application categories. You can download the list of newly added cloud applications to the respective categories: [Download](/sites/default/files/downloads/zia/documentation-knowledgebase/policies/cloud-apps/cloud-app-control-policies/cloud-app-categories/New_Cloud_Apps_April-2026.xlsx)

The risk index and risk attribute values for these new applications are visible only after they are available on all the clouds. Refer to the [trust post](https://trust.zscaler.com/zscalerthree.net/notification/452301) for details.

### Feature Available

#### NSS Support for 3rd-Party App Governance and Posture Management Logs
Logs for Zscaler 3rd-Party App Governance and Posture Management are supported by Zscaler's Nanolog Streaming Service (NSS). You can configure NSS and Cloud NSS feeds for both log types to stream their respective data to your security information and event management (SIEM) system, providing a unified view of your organization’s security posture for effective threat management.

Access to these log types requires a subscription to [Advanced SaaS Security Posture Management (SSPM)](/zia/what-advanced-posture-management). To subscribe to Advanced SSPM, contact your Zscaler Account team.

[See image.](#img-app-governance-posture-log-types)

When creating a policy in 3rd-Party App Governance, you can select the Zscaler Nanolog Streaming Service option to receive alerts for the policy through NSS every time the policy is triggered.

[See image.](#Set-Policy-Window)

![Set Policy Window showing NSS option](/sites/default/files/downloads/tech-pubs-drafts/zia-draft-articles/3rd-party-app-governance-policies-draft-doc-62153/Set_Policy_NSSRN.png "Set Policy Window")

To learn more, see:

* [Adding NSS Feeds for 3rd-Party App Governance Logs](/zia/adding-nss-feeds-3rd-party-app-governance-logs)
* [Adding Cloud NSS Feeds for 3rd-Party App Governance Logs](/zia/adding-cloud-nss-feeds-3rd-party-app-governance-logs)
* [NSS Feed Output Format: 3rd-Party App Governance Logs](/zia/nss-feed-output-format-3rd-party-app-governance-logs)
* [Adding NSS Feeds for Posture Management Logs](/zia/adding-nss-feeds-posture-management-logs)
* [Adding Cloud NSS Feeds for Posture Management Logs](/zia/adding-cloud-nss-feeds-posture-management-logs)
* [NSS Feed Output Format: Posture Management Logs](/zia/nss-feed-output-format-posture-management-logs)
* [3rd-Party App Governance Policies](/zia/3rd-party-app-governance-policies)

![App Governance and Posture log types in the Add Cloud NSS Feed window](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/nss-app-governance-posture-log-type.png "App Governance and Posture log types in the Add Cloud NSS Feed window")

# Enhancement to Cloud Nanolog Streaming Service (NSS) API

Two new enum values, `POSTURE_CONTROL` and `APP_GOVERNANCE` are added to the `nssLogType` field in the `ZmanageNssFeed` model referenced by the `/nssFeeds` APIs

To learn more, go to the `ZmanageNssFeed` model from [Cloud Nanolog Streaming Service (NSS)](/zia/cloud-nanolog-streaming-service-nss).

### Feature Available

#### Updates to Cloud Applications
As part of a continuous review, Zscaler has updated cloud applications across various cloud application categories. To obtain the list of cloud applications that have been updated, download the list: [Download](/sites/default/files/downloads/zia/documentation-knowledgebase/policies/cloud-apps/cloud-app-control-policies/cloud-app-categories/Updated-Cloud-Apps-April-2026.xlsx)

Cloud applications are updated in phases. Refer to the [trust post](https://trust.zscaler.com/zscaler.net/notification/458921) for details.

## July 01, 2026

## June 29, 2026

### Feature Available

#### Additional Support for Microsoft 365 Apps in Advanced SSPM
Advanced SaaS Security Posture Management (SSPM) supports new posture controls as part of the Microsoft 365 connector for the following apps:

* Microsoft Power Apps
* Microsoft Power BI
* Microsoft Purview
* Microsoft Viva Engage

Existing tenants must grant additional permissions and reauthenticate the connector for these additional posture controls.

Select the SSPM Scan checkbox when onboarding a Microsoft 365 tenant to enable the Advanced SSPM scan capability for the specific tenant.

[See image.](#Microsoft-Power-Apps-Onboarding)

The SSPM Scan checkbox is enabled only when you have Advanced SSPM enabled for your tenant.

To learn more, see [What Is Advanced Posture Management?](/zia/what-advanced-posture-management), [Adding SaaS Application Tenants](/zia/adding-saas-application-tenants), and [Authorizing a Custom Zscaler Connector for Microsoft Applications](/zia/authorizing-custom-zscaler-connector-microsoft-applications).

![SSPM Scan Checkbox](/sites/default/files/downloads/SSPM_Scan_Checkbox.png "Onboard SaaS Application")

## June 26, 2026

### Feature Available

#### Block Domain Fronting Enhancement
In Advanced Settings (Policies > Common Configuration > Advanced > Advanced Settings > Domain Fronting), there are two new options available under Block Domain Fronting:

* URL Category Exemptions for Block Domain Fronting: Select the URL categories you want to exempt from domain fronting.
* Exempted Cloud Applications for Block Domain Fronting: Select the cloud app categories or cloud apps you want to exempt from domain fronting.

[See image.](#domain-fronting-image)

To learn more, see [Configuring Advanced Settings](/zia/configuring-advanced-settings#domain-fronting).

![Domain Fronting Page showing two new drop-downs for Block Domain fronting under Advanced Settings](/sites/default/files/downloads/zia/policies/configuring-advanced-settings/Block%20Domain%20Fronting.png "Domain Fronting Page")

### Feature Available

#### Enhanced Web Logs: Added Support for DLP Policy Actions and Justification Messages
You can filter and view logs for DLP policy actions and DLP confirmation messages. As part of the update, the following changes are available in the Zscaler Admin Console:

# Insights Logs

Filters and columns, DLP Policy Action and DLP Confirmation Message, are added to Web Insights Logs and Endpoint DLP Insights Logs.

[See image.](#dlp-filters)

To learn more, see [Web Insights Logs: Columns](/zia/web-insights-logs-columns), [Web Insights Logs: Filters](/zia/web-insights-logs-filters), [Endpoint DLP Insights Logs: Columns](/zia/endpoint-dlp-insights-logs-columns), and [Endpoint DLP Insights Logs: Filters](/zia/endpoint-dlp-insights-logs-filters).

# NSS Feeds

The fields `%s{dlp_policy_action}` and `%s{dlp_confirm_justification_msg}` can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for web logs. Additionally, the field `%s{dlp_confirm_justification_msg}` is available for NSS and Cloud NSS feeds for Endpoint DLP logs.

To learn more, see [NSS Feed Output Format: Web Logs](/zia/nss-feed-output-format-web-logs) and [NSS Feed Output Format: Endpoint DLP Logs](/zia/nss-feed-output-format-endpoint-dlp-logs).

![DLP filters in the Insights Logs page](/sites/default/files/downloads/zia/documentation-knowledgebase/analytics/dashboards-reports-and-logs/logs/about-saas-security-insights-logs/ZIA-DLP-filters.png "DLP Policy Action and DLP Confirmation Message Filter")

## June 24, 2026

### Feature Available

#### New Labels and Values in SaaS Security Report
Instead of classifying all new applications as Unsanctioned, you can use new Application Status labels Unclassified and Under Review, to classify applications more appropriately. The label Unclassified means the applications haven't been evaluated for risks yet, and Under Review means they are undergoing due diligence.

[See image.](#labels)

Moreover, the SaaS Security Report for each cloud application now displays detailed information about security attributes including their certificate validity, WAF name, CVE ID, breach URL, and so on. More information appears in brackets next to the Yes and No signals.

[See image.](#sec-info)

To learn more, see [About the SaaS Security Report](/zia/about-saas-security-report) and [About the Application Information](/zia/about-application-information).

![New labels for Application Status in the SaaS Security Report](/sites/default/files/downloads/tech-pubs-drafts/miscellaneous-draft-articles/about-policy-templates-draft-doc-64063/saas-sec-new-labels-annotated.png "Application Status new labels")

![The Security Information for each cloud app in the SaaS Security Report](/sites/default/files/downloads/zia/dashboard-analytics/reports/saas-security/understanding-assets-report-assets-with-incidents/sec-info-shadow-it.png "Security information in SaaS Security Report")

## June 23, 2026

### Feature Available

#### Enhancement to Application Service Groups
The Application Services page has been enhanced to allow you to define your own application service groups. This page contains the following enhancements:

* You can add custom application service groups.
* The Definition column is added.
* You can view, edit, and filter the application service groups under a new column.

The Custom Application Service Group is available if Advanced Firewall is enabled for your organization.

[See image.](#application-group)

To learn more, see [Configuring Application Service Groups](/zia/configuring-application-service-groups) and [About Application Service Groups](/zia/about-application-service-groups).

# Update to Forwarding Policy, IPS Control Policy, and Firewall Filtering Policy

The Forwarding policy, IPS Control policy, and Firewall Filtering policy allow you to select predefined (AU) and custom (CU) application service groups while configuring these policies.

[See image.](#ips-firewall)

To learn more, see [Configuring Forwarding Policy](/zia/configuring-forwarding-policy), [Configuring IPS Control Policy](/zia/configuring-ips-control-policy), and [Configuring the Firewall Filtering Policy](/zia/configuring-firewall-filtering-policy).

# Update to Cloud Service API

The cloud service API includes the following new endpoints to create, update, and delete custom application service groups, and retrieve configurations for all custom application service groups (predefined and custom):

* `GET /apps-services`
* `POST /apps-services`
* `GET /apps-services/{appServiceId}`
* `PUT /apps-services/{appServiceId}`
* `DELETE /apps-services/{appServiceId}`

To learn more, see the [API Reference](/zia/zia-api).

![Application Services Page with Add Application Service Group option](/sites/default/files/downloads/zia/policies/firewall/firewall-policy-resources/configuring-application-service-groups/Application%20Services.png "Application Services Page")

![IPS Rule Control Rule with Application Service Groups showing predefined and custom application services](/sites/default/files/downloads/zia/policies/firewall/firewall-policy-resources/configuring-application-service-groups/Add%20IPS%20Control%20Rule.png "Predefined and Custom Application Service Groups")

## June 19, 2026

### Feature Available

#### Support for Snowflake as an API-Based Platform in Advanced SSPM
Advanced SaaS Security Posture Management (SSPM) supports Snowflake as an API-based platform to provide visibility into posture misconfigurations. You can configure Advanced SSPM for Snowflake tenants. Select the SSPM Scan checkbox when onboarding a tenant to enable the Advanced SSPM scan capability for the specific tenant.

[See image.](#Snowflake-Onboarding)

The SSPM Scan checkbox is enabled only when you have Advanced SSPM enabled for your tenant.

To learn more, see [What Is Advanced Posture Management?](/zia/what-advanced-posture-management) and [Adding SaaS Application Tenants](/zia/adding-saas-application-tenants).

![SSPM Checkbox for Snowflake](/sites/default/files/downloads/zia/release-notes/internet-saas-service-release-notes/release-upgrade-summary-2026/SSPM_Scan_Checkbox.png "Snowflake Onboarding")

## June 18, 2026

### Feature Available

#### Enhancement to Browser EUN Template
You can set a caution interval per browser EUN template, which allows you to configure different caution intervals for different browser EUNs. As part of this change, in the Administration > End User Notifications > Browser > EUN Templates > Add Custom Message window, the Caution Interval drop-down menu is added.

[See image.](#add-custom-message-caution-interval)

To learn more, see [Configuring Browser EUN Template](/zia/configuring-browser-eun-template).

![ZIA Add Custom Message with Custom Interval](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2025/ZIA-Add-Custom-Message-Caution-Interval-RN.png "ZIA Add Custom Message with Custom Interval")

## June 16, 2026

### Feature Available

#### Advanced SSPM Support for Databricks
Advanced SSPM supports a new platform, Databricks. You can onboard a Databricks tenant from the 3rd-Party App Governance Admin Portal.

[See image.](#Connect-Drop-Down-Menu)

To learn more, see [Integrating with Databricks](/zia/integrating-databricks) and [Connecting Your Platforms to Advanced SSPM](/zia/connecting-your-platforms-advanced-sspm).

![Connect Drop-Down Menu showing Databricks option](/sites/default/files/downloads/zia/policies/saas-security/posture-management/posture-management-advanced/integrating-databricks/Databricks_Connect.png "Connect Drop-Down Menu")

### Feature Available

#### Advanced SSPM Support for OpenAI
Advanced SSPM supports a new platform, OpenAI. You can onboard an OpenAI tenant from the 3rd-Party App Governance Admin Portal.

[See image.](#Connect-Drop-Down-Menu)

To learn more, see [Integrating with OpenAI](/zia/integrating-openai) and [Connecting Your Platforms to Advanced SSPM](/zia/connecting-your-platforms-advanced-sspm).

![Connect Drop-Down Menu showing OpenAI option](/sites/default/files/downloads/zia/policies/saas-security/posture-management/posture-management-advanced/integrating-openai/OpenAI_Connect.png "Connect Drop-Down Menu")

## June 08, 2026

### Feature Available

#### Expanded SSPM Controls for Box
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Box with 4 new SSPM controls, providing deeper visibility and stronger security posture assessment.

## June 05, 2026

### Feature Available

#### Ability to Select Channels for DLP Engines
You can define custom and predefined DLP engines to apply only to specific channels (e.g., Endpoint DLP, DSPM) to reduce the extra noise that can come from engines being on particular channels unnecessarily. This functionality is available when you create, edit, or clone a DLP engine on the DLP Engines page (Policies > Data Protection > Common Resources > DLP Dictionaries & Engines > DLP Engines):

[See image.](#dlp-engine-channel-rn-2604)

To learn more, see [Editing Predefined DLP Engines](/zia/editing-predefined-dlp-engines), [Adding Custom DLP Engines](/zia/adding-custom-dlp-engine), and [Cloning DLP Engines](/zia/cloning-dlp-engines).

![Channels available for editing a DLP engine](/sites/default/files/downloads/zpa/release-notes/release-upgrade-summary-2026/Edit-DLP-Engine-Select-Channels.png "Editing a DLP engine with channels available")

## June 04, 2026

## June 01, 2026

## May 26, 2026

### Feature Available

#### Secure Message Processing Center (SMPC) Instance Endpoints
You can update the data center and the Secure Message Processing Center (SMPC) instance details based on a specific data center ID and retrieve the status of all SMPC instances grouped by a data center using the following endpoints:

* `GET /smpcInstance`
* `PUT /smpcInstance/dc`

A new Enum value, `ZS_BUSINESS_CONTINUITY` is available in the `permissions` field of the `AdminRole` model used by the `/adminRoles` APIs. This enum allows administrators to grant permission to update or view the SMPC instance isolation.

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

## May 22, 2026

### Feature Available

#### Enhancements for Isolation User Experience Loading Page
The following updates have been made to the isolation experience for Zero Trust Browser:

* As you enter an isolated session, a static, temporary message appears in the middle of the web page as it loads to confirm you are entering an isolated session. Additionally, an animated green outline appears around the website border as the page loads.  
  [See image.](#Entering-Zero-Trust-Mode)
* When the page has completely rendered, a [temporary notification banner](/zero-trust-browser/profiles/profile-notifications) appears in the upper-right corner that displays a customized notification title. You can click the Show More link in the banner to view a message customized by the admin.  
  [See image.](#Zero-Trust-Mode-Icon-and-Notification-Banner-condensed)
* A floating checkmark icon also appears when the page has completely rendered, and stays visible after the temporary notification banner disappears. This is a visual indicator that the isolation session is persisting and has not expired.  
  [See image.](#Zero-Trust-Mode-icon-and-expanded-message)

To learn more, see [Adding a Banner Theme for the Isolation End User Notification in ZIA](/zero-trust-browser/adding-banner-theme-isolation-end-user-notification-zia).

![A view of a web page entering Zero Trust Mode. ](/sites/default/files/downloads/zero-trust-browser/profiles/profile-notifications/adding-banner-theme-isolation-end-user-notification-zia/Entering-Zero-Trust-Mode_message_green-outline.png "A green outline appears around the web page as a notification message temporarily loads.")

![A view of a web page after it has completely loaded while in an isolated session.](/sites/default/files/downloads/zero-trust-browser/end-user-isolation-experience/user-experience-modes-isolation/UX-Phase-0_Notification-Banner-Show-More_squircles.png "The web page shows the temporary notification banner that appears when the user is in Zero Trust Mode and the active session icon at the bottom of the page.")

![A view of a web page after it has completely loaded while in an isolated session.](/sites/default/files/downloads/zero-trust-browser/end-user-isolation-experience/user-experience-modes-isolation/UX-Phase-0_Notification-Banner_Expanded_squircles.png "The web page shows the fully expanded temporary notification banner that appears when the user is in Zero Trust Mode and the active session icon at the bottom of the page.")

### Feature Available

#### Updates to Devices Endpoints
You can retrieve information about devices registered with Zscaler using the following endpoints:

* `GET /devices`
* `GET /devices/{id}`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to Partner Integrations APIs
You can retrieve a list of partners and services integrated with the Zscaler service, a list of configured CrowdStrike endpoints or device IDs, and detailed endpoint or device data based on the IDs using the following integration endpoints:

* `GET /integrationPartners`
* `GET /integrationPartners/crowdStrike/endpoints`
* `POST /integrationPartners/crowdStrike/endpoints`
* `GET /integrationPartners/crowdStrike/whitelistedBaseUrls`

You can configure the integration of Microsoft Defender for Endpoint APIs with Zscaler and retrieve the MD5 hash of the file required to view the Sandbox Detail Report using the following endpoints:

* `POST /integrationPartners/microsoftDefender/endpoints`
* `GET /integrationPartners/sandbox/report/{md5}`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

## May 18, 2026

### Feature Available

#### Zscaler URL Category Test
The [Zscaler URL category test](https://www.zscaler.com/url-categorization) provides a set of standardized, immutable test URLs specifically designed for HTTPS URL policy validation testing. These Zscaler-managed sites maintain persistent categorization, allowing administrators to consistently verify that URL Filtering rules and SSL/TLS Inspection policies are being applied as intended.

Because these URLs are immutable, they provide a baseline for confirming HTTPS URLs and SSL/TLS policy actions without the risk of external site changes.

[See image.](#zscaler-url-category-test)

To learn more, see [About URL Categories](/zia/about-url-categories).

![Zscaler URL category test page](/sites/default/files/downloads/zia/release-notes/internet-saas-service-release-notes/release-upgrade-summary-2026/Zscaler-URL-Categorization.png "Zscaler URL category test page")

## May 15, 2026

### Feature Available

#### Increased File Size Support for Advanced Detections
With the Advanced Detections package for Advanced Sandbox, you can analyze EXE and DLL files with sizes up to 200 MB.

To learn more, see [About Sandbox](/zia/about-sandbox).

### Feature Available

#### Sandbox for Private Access Assets
Organizations with Advanced Sandbox that use Internet & SaaS (ZIA) to inspect Private Access (ZPA) traffic can sandbox unknown files uploaded to Private Access assets.

To learn more, see [About Sandbox](/zia/about-sandbox).

### Feature Available

#### Support for AI/ML Detection Source
The Zscaler Admin Console is enhanced with the ability to view the AI/ML detection source for your Internet & SaaS (ZIA) traffic. The following updates are available:

# Web Insights Logs

The AI/ML Detection Source filter and column are added to the Web Insights Logs page.

[See image.](#detection-web-logs)

To learn more, see [Web Insights Logs: Columns](/zia/web-insights-logs-columns) and [Web Insights Logs: Filters](/zia/web-insights-logs-filters).

# Analytics

The Top AI/ML Detection Source by Security Incidents widget and the AI/ML Detection Source field are added to the Threat Incidents table and Details tab.

[See image.](#detection-cybersecurity-insights)

To learn more, see [About Cybersecurity Insights](/zia/about-cybersecurity-insights).

# Nanolog Streaming Service (NSS)

You can use the filter AI/ML Detection Source when configuring an NSS or Cloud NSS feed for web logs.

[See image.](#nss-filter)

Additionally, you can add the field `%s{ai_ml_detection_src}` to the Feed Output Format.

To learn more, see:

* [Adding NSS Feeds for Web Logs](/zia/adding-nss-feeds-web-logs#Security)
* [Adding Cloud NSS Feeds for Web Logs](/zia/adding-cloud-nss-feeds-web-logs#Security)
* [NSS Feed Output Format: Web Logs](/zia/nss-feed-output-format-web-logs)

![AI/ML Dectection Source field in Web Insights Logs](/sites/default/files/downloads/zia/dashboard-analytics/reports/about-cybersecurity-insights/ZIA-Web%20Insights-AI-MLDetection%20Source%20Column%20and%20Filter.png "AI/ML Dectection Source Filter and Column")

![AI/ML Detection Source field in Cybersecurity Insights ](/sites/default/files/downloads/zia/dashboard-analytics/reports/about-cybersecurity-insights/zia-Cybersecurity%20Insights%20Dashboard-AI-ML%20Detection%20Source.png "AI/ML Detection Source Field")

![AI/ML Detection Source filter in NSS for web logs](/sites/default/files/downloads/zia/release-notes/ai-ml-detection-source-filter-nss-web.png "AI/ML Detection Source filter in NSS for web logs")

### Feature Available

#### Support for Display of Site Type for SharePoint Tenants
When creating a site on SharePoint, you can define the site type as Public, Private, or Communication. These site types are displayed on the Manage SaaS Application Tenants > Components page.

[See image.](#sharepoint-site-type)

To learn more, see [Manage SaaS Application Components](/zia/manage-saas-application-components).

![The site type that is displayed under the Components tab of Manage SaaS Application Components page.](/sites/default/files/downloads/tech-pubs-drafts/zia-draft-articles/draft-manage-saas-application-components-doc-61981/Site%20Type.png "SharePoint Site Type")

### Feature Available

#### Support for DLP Scan Timeout Identifiers in Web Insights Logs
You can filter and view logs for specific DLP identifiers of transactions that were exempted from policy enforcement due to a scan timeout.

As part of the update, the following changes are available in the Zscaler Admin Console:

# Web Insights Logs

The filter and column Exempted DLP Identifier is added to the Web Insights Logs.

[See image.](#exempted-dlp-identifier-field)

To learn more, see [Web Insights Logs: Filters](/zia/web-insights-logs-filters) and [Web Insights Logs: Columns](/zia/web-insights-logs-columns).

# NSS Feeds

The field `%d{exempt_dlpidentifier}` can be added to the Feed Output Format when configuring NSS or Cloud NSS feeds for web logs.

To learn more, see [NSS Feed Output Format: Web Logs](/zia/nss-feed-output-format-web-logs).

![Exempted DLP Identifier filter and column in the Web Insights Logs page](/sites/default/files/downloads/ZIA-Exempted-dlp-identifier-field.png "Exempted DLP Identifier Filter and Column")

### Feature Available

#### Support for Restoring Quarantined Files in Salesforce
You can now restore quarantined Salesforce files to their original location with the Restore remediation action on the SaaS Security Assets page.

[See image.](#restore-action)

This action is available only for files initially quarantined using the Quarantine Malware action within the DLP Malware policy.

All files quarantined before this feature update are restored to the Salesforce user folder, specifically within Files > Owned by me.

To learn more, see [Understanding the Assets Report: Assets with Incidents](/zia/understanding-assets-report-assets-with-incidents).

![Restore remediation Action on SaaS Security Assets page](/sites/default/files/downloads/tech-pubs-drafts/zia-draft-articles/release-note-xc-zia-2026/restore-action-salesforce.png "Restore Action on SaaS Security Assets page")

### Feature Available

#### Third-Party Proxies and Gateways Limits
You can add up to 255 proxies and proxy gateways for third-party proxy services (Infrastructure > Internet & SaaS > Network Policies > Proxies & Gateways) in the Zscaler Admin Console.

To learn more, see [Ranges & Limitations](/unified/ranges-limitations).

# Update to Cloud Service API

You can add a maximum of up to 255 proxies using the `POST /proxies` API. To increase the limit to a desired value, contact Zscaler Support to request a configuration change for your tenant.

## May 08, 2026

### Feature Available

#### Additional Support for Predefined DLP Dictionaries in Endpoint DLP
The following predefined Data Loss Prevention (DLP) dictionaries are now supported for use in Endpoint DLP policy rules:

* Addresses (Japan)
* First Names (Japan)
* Full Names (Japan)
* Last Names (Japan)

To learn more, see [Understanding Predefined DLP Dictionaries](/zia/understanding-predefined-dlp-dictionaries).

### Feature Available

#### Enhancement to Cloud Application Instances
The cloud application instances feature is extended to new cloud applications. You can create cloud application instances for the following cloud applications:

* Google Gemini
* Microsoft Copilot

[See image.](#add-cloud-app-instance)

To learn more, see [About Cloud Application Instances](/zia/about-cloud-application-instances).

![Zscaler Add Cloud Application Instance window with Google Gemini and Microsoft Copilot](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/Zscaler-Add-Cloud-Application-Instance-Window-RN.png "Zscaler Add Cloud Application Instance window")

### Feature Available

#### Instance Discovery Report Support for Azure
You can view the Instance Discovery Report for Microsoft Azure; this application supports three levels of discovery:

1. Domain
2. Tenant
3. Resource

[See image.](#data-discovery-report-azure)

To learn more, see [About the Instance Discovery Report](/zia/about-instance-discovery-report) and [Viewing the Resource Discovery Report](/zia/viewing-resource-discovery-report).

![Instance Discovery Report for Microsoft Azure](/sites/default/files/downloads/tech-pubs-drafts/zia-draft-articles/viewing-resource-discovery-report/ZIA-Instance-Discovery-Report-Azure-RN.png "Instance Discovery Report for Microsoft Azure")

### Feature Available

#### Updates to Malware Protection Policy Endpoints
You can update the Malware Protection policy and retrieve the Malware Protection policy for an organization using the following endpoints:

* `GET /malwarePolicy`
* `PUT /malwarePolicy`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to NSS Collector Server Endpoints
You can add, update, and delete NSS Collector servers and retrieve a list of all configured NSS Collector servers for an organization using the following endpoints:

* `GET /nssCollectors`
* `POST /nssCollectors`
* `PUT /nssCollectors/{id}`
* `DELETE /nssCollectors/{id}`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to Secure Browsing and Votiro CDR Endpoints
You can retrieve a list of all supported browsers and their versions and update the Smart Browser Isolation policy settings using the following endpoints:

* `GET /browserControlSettings/supportedBrowserVersions`
* `PUT /browserControlSettings/smartIsolation`

You can update, delete, and retrieve the Votiro CDR authentication credentials and retrieve the Votiro CDR policies configured for a tenant using the following endpoints:

* `GET /isolationVotiroCdr/policies`
* `GET /isolationVotiroCdr/tokenConfig`
* `PUT /isolationVotiroCdr/tokenConfig`
* `DELETE /isolationVotiroCdr/tokenConfig`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to the IPS Control Policy Endpoints
You can create, update, delete, and retrieve custom IPS signature rules using the following endpoints:

* `GET /ipsSignatureRules`
* `POST /ipsSignatureRules`
* `GET /ipsSignatureRules/{id}`
* `PUT /ipsSignatureRules/{id}`
* `DELETE /ipsSignatureRules/{id}`

You can export and import custom IPS signature rules, and validate the rule text for a new custom signature rule using the following endpoints:

* `GET /ipsSignatureRules/export`
* `GET /ipsSignatureRules/import`
* `POST /ipsSignatureRules/import`
* `POST /ipsSignatureRules/validateRuleText`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

## May 07, 2026

### Feature Available

#### Expanded SSPM Controls for Bitbucket
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Bitbucket with 9 new SSPM controls, providing deeper visibility and stronger security posture assessment.

### Feature Available

#### Expanded SSPM Controls for Confluence
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Confluence with 5 new SSPM controls, providing deeper visibility and stronger security posture assessment.

### Feature Available

#### Expanded SSPM Controls for Jira
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Jira with 5 new SSPM controls, providing deeper visibility and stronger security posture assessment.

### Feature Available

#### Support for New Workday Filters and Prompts
You can use a new filter Last Functionally Updated to easily identify recently modified records when creating custom reports in Workday. Additionally, the prompts Starting Prompt and Ending Prompt fields provide greater control and precision when defining report parameters.

[See image.](#wd_filter)

To learn more, see [Adding SaaS Application Tenants](/zia/adding-saas-application-tenants).

![Workday filters and prompts](/sites/default/files/downloads/tech-pubs-drafts/zia-draft-articles/adding-saas-application-tenants-draft-doc-63745/wd_filter_rn.png "Workday filters and prompts")

## May 05, 2026

### Feature Available

#### Increased Virtual Service Edge Instance Memory for Internet & SaaS on Amazon Web Services
Configuring Virtual Service Edge for Internet & SaaS (ZIA) on Amazon Web Services (AWS) requires 64 GB of instance memory.

Zscaler recommends the r7i.2xlarge instance size.

To learn more, see [Configuring Virtual Service Edge for Internet & SaaS: Amazon Web Services](/zia/configuring-virtual-service-edge-internet-saas-amazon-web-services) and [Configuring Virtual Service Edge for Internet & SaaS: Amazon Web Services with GWLB](/zia/configuring-virtual-service-edge-internet-saas-amazon-web-services-gwlb).

## May 01, 2026

### Feature Available

#### Expanded SSPM Controls for Google Workspace
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Google Workspace with 24 new SSPM controls, providing deeper visibility and stronger security posture assessment. The Cloud Identity license must be assigned to the Google Workspace Admin onboarding the account. This is critical to ensure appropriate license and compliance with Google Cloud Identity and Workspace policies. Additional API scopes are required for existing tenants to view the new Cloud Identity policies.

To learn more, see [Adding SaaS Application Tenants](/zia/adding-saas-application-tenants).

### Feature Available

#### Gen AI Prompt Configuration for QuillBot and Google AI
Zscaler's Gen AI prompt configuration is extended to the QuillBot and Google AI generative AI applications. You can enable prompts for these generative AI applications to categorize and store the prompts for the respective applications.

[See image.](#gen-ai-quillbot-googleAI)

To learn more, see [Configuring Advanced Policy Settings](/zia/configuring-advanced-policy-settings#gen-AI-prompt).

![ZIA Advanced Policy Settings Page with QuillBot and Google AI Gen AI Applications](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/ZIA-Advanced-Policy-Settings_Gen-AI-Prompt-Configuration-RN.png "ZIA Advanced Policy Settings Page with QuillBot and Google AI Gen AI Applications")

# Added QuillBot and Google AI Capabilities to URL & Cloud App Control Policy Settings Endpoint

Two new Boolean fields, `enableQuillbotAIPrompt` and `enableGoogleAIPrompt`, are available for the `AdvancedUrlFilteringCloudAppOptions` model in the `/advancedUrlFilterAndCloudAppSettings` APIs. These fields allow users to use generative AI prompts with QuillBot and Google AI.

To learn more, see [URL & Cloud App Control Policy Settings](/zia/url-cloud-app-control-policy-settings).

### Feature Available

#### Policy Level Gen AI Prompt Configuration
You can capture end user prompts for generative AI applications from the Cloud Application Control policy. This allows granular control of Gen AI prompt configuration. As part of this update, the Capture Prompts option is added to the Add/Edit AI & ML Rule window (Policies > Access Control > Internet & SaaS > Policies > Cloud App Control Policy > Add > AI & ML Applications).

This is applicable for Gen AI applications that are supported in the [Gen AI Prompt Configuration](/zia/configuring-advanced-policy-settings#gen-AI-prompt) section of the Advanced Policy Settings page.

[See image.](#ai-ml-rule-capture-prompts)

To learn more, see [Adding an AI & ML Applications Rule for Cloud App Control](/zia/adding-ai-ml-applications-rule-cloud-app-control).

![The Capture Prompts option in the Add/Edit AI & ML Rule window](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/ZIA-Add-Edit-AI-ML-Rule-Window-Action-RN.png "The Add/Edit AI & ML Rule window with the Capture Prompts option")

# Update to the Cloud App Control Policy Endpoint

A new Boolean field, `promptCaptureEnabled`, is available for the `WebApplicationRule` model in the `/webApplicationRules` APIs. This field enables users to allow or block the capture of end user prompts for generative AI applications.

To learn more, go to the `WebApplicationRule` model from [Cloud App Control Policy](/zia/cloud-app-control-policy).

## April 17, 2026

### Feature Available

#### Adaptive Access Profiles Endpoints
You can retrieve a list of Adaptive Access profiles and information about an Adaptive Access profile using the following endpoints:

* `GET /adaptiveAccessProfiles`
* `GET /adaptiveAccessProfiles/profiles/rules`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Enabling Incident Forwarding for Slack Chats
Zscaler is now forwarding Slack chat-based DLP policy incidents to the Zscaler Incident Response and Zscaler Workflow Automation along with already supported file-based violations. These incidents are also sent to Web Insights and Logs and to the respective DLP policy's auditor.

To learn more, see [Understanding SaaS Security API Supported Capabilities](/zia/understanding-saas-security-apis), [Configuring the Data at Rest Scanning DLP Policy with Content Inspection](/zia/configuring-data-rest-scanning-dlp-policy-content-inspection) and [Configuring the Data at Rest Scanning DLP Policy without Content Inspection](/zia/configuring-data-rest-scanning-dlp-policy-without-content-inspection).

### Feature Available

#### Updates to Azure Integration Endpoints
You can retrieve the progress summary of the VPN connection refresh process and start a new asynchronous process to refresh the VPN connection status using the following endpoints:

* `GET /azure/refreshConnectionStatus`
* `POST azure/refreshConnectionStatus`

You can retrieve the tunnel configuration status, start the tunnel configuration process, remove the tunnel configuration, and retrieve the status of the tunnel configuration removal process for a specified Azure hub using the following endpoints:

* `GET /azure/tunnelConfiguration`
* `POST /azure/tunnelConfiguration`
* `DELETE /azure/unConfigureTunnel/{hubId}`
* `GET /azure/unConfigureTunnelStatus`

You can retrieve the Azure hub sync process details and start a process to sync the hubs using the following endpoints:

* `GET /azure/virtualHubs`
* `GET /azure/virtualHubSync`
* `POST azure/virtualHubSync`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to Security & UEBA Alerts Endpoints
You can create, update, and delete alert definitions, and retrieve a list of all configured alert definitions for an organization using the following endpoints:

* `GET /alertDefinitions`
* `POST /alertDefinitions`
* `GET /alertDefinitions/{alertDefinitionId}`
* `PUT /alertDefinitions/{alertDefinitionId}`
* `DELETE /alertDefinitions/{alertDefinitionId}`

You can create, update, and delete Security alert rules, and retrieve a list of all configured Security alert rules for an organization and their statuses using the following endpoints:

* `GET /alertRuleConfiguration/rules`
* `POST /alertRuleConfiguration/rules`
* `GET /alertRuleConfiguration/rules/{ruleId}`
* `PUT /alertRuleConfiguration/rules/{id}`
* `DELETE /alertRuleConfiguration/rules/{id}`
* `GET /alertRuleConfiguration/rules/rulestatus`

You can create, update, and delete User and Entity Behavior Analytics (UEBA) alert rules, and retrieve a list of all configured UEBA alert rules using the following endpoints:

* `GET /alertRuleConfiguration/uebaRules`
* `POST /alertRuleConfiguration/uebaRules`
* `GET /alertRuleConfiguration/uebaRules/{ruleId}`
* `PUT /alertRuleConfiguration/uebaRules/{id}`
* `DELETE /alertRuleConfiguration/uebaRules/{id}`

You can create, update, and delete webhooks, retrieve a list of all configured webhooks for an organization, and test a webhook configuration using the following endpoints:

* `GET /alertRuleConfiguration/webhooks`
* `POST /alertRuleConfiguration/webhooks`
* `PUT /alertRuleConfiguration/webhooks/{id}`
* `DELETE /alertRuleConfiguration/webhooks/{id}`
* `POST /alertRuleConfiguration/webhooks/test`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

## April 15, 2026

### Feature Available

#### DLP Support for New PII Dictionaries
The following are new predefined DLP dictionaries:

* Argentina Uniform Bank Code: Detect Leakage of CBU
* Cambodian National ID: Detect Leakage of Khmer Identification Code (KIdC)
* Mexico Business Tax ID: Detect Leakage of BRFC
* Mexico Individual Tax ID: Detect Leakage of IRFC
* Mexico Social Security Number: Detect Leakage of NSS

To learn more, see [Understanding Predefined DLP Dictionaries](/zia/understanding-predefined-dlp-dictionaries).

### Feature Available

#### Support for Collaboration Scope for Microsoft Teams
When creating a DLP rule for Microsoft Teams, you can define the collaboration scope as External, Internal, or Any to scan messages and attachments in channels containing external, internal, or any (internal or external) members.

[See image.](#collab-scope-dlp)

On the SaaS Security Analytics page, files from MS Teams that violate the DLP policy now show their collaboration scope, among other details.

[See image.](#collab-scope)

To learn more, see [Configuring the Data at Rest Scanning DLP Policy with Content Inspection](/zia/configuring-data-rest-scanning-dlp-policy-content-inspection) and [Configuring the Data at Rest Scanning DLP Policy without Content Inspection](/zia/configuring-data-rest-scanning-dlp-policy-without-content-inspection).

![Collaboration Scope on SaaS Security Analytics page](/sites/default/files/downloads/zia/dashboard-analytics/reports/saas-security/understanding-assets-report-assets-with-incidents/ms-teams-collab-scope-analytics-cropped.png "Collaboration Scope on SaaS Security Analytics page")

![Collaboration Scope in SaaS Security Data Protection Policy](/sites/default/files/downloads/zia/dashboard-analytics/reports/saas-security/understanding-assets-report-assets-with-incidents/image%20(4).png "Collaboration Scope in SaaS Security Data Protection Policy")

### Feature Available

#### Support for Smartsheet as an API-Based Platform in Advanced SSPM
Advanced SSPM supports Smartsheet as an API-based platform to provide visibility into posture misconfigurations. You can onboard a Smartsheet tenant from the 3rd-Party App Governance Admin Portal.

[See image.](#Connect-Drop-Down-Menu)

To learn more, see [Integrating with Smartsheet](/zia/integrating-smartsheet) and [Connecting Your Platforms to Advanced SSPM](/zia/connecting-your-platforms-advanced-sspm).

![Connect Drop-Down Menu showing the Smartsheet option](/sites/default/files/downloads/zia/release-notes/Smartsheet_Connect_Dropdown.png "Connect Drop-Down Menu")

## April 14, 2026

### Feature Available

#### Enhancement to Atlassian Integration in 3rd-Party App Governance
The Add Integration window for Atlassian in 3rd-Party App Governance is enhanced to allow you to enter the Atlassian subdomain and API token while adding the integration. This reduces the number of steps and simplifies the integration process to improve the user experience.

[See image.](#Add-Integration-Window)

To learn more, see [Integrating with Atlassian.](/zia/integrating-with-atlassian)

![Atlassian Integration Window showing API token](/sites/default/files/downloads/tech-pubs-drafts/zia-draft-articles/integrating-atlassian-draft-doc-63584/Atlassian_AddIntegration_Window_New.png "Add Integration Window")

## April 10, 2026

### Feature Available

#### Add or Remove NTP Servers Using CLI
You can add or remove custom NTP servers from the configuration files using CLI commands. This prevents syntax errors and duplicate entries in the configuration files.

To learn more, see [Configuring Virtual Service Edge for Internet & SaaS and NTP Server Synchronization](/zia/configuring-virtual-service-edge-internet-saas-ntp-server-synchronization).

### Feature Available

#### Default Rules for Advanced Sandbox
If your organization is subscribed to the Advanced Sandbox package, the following default rules are available:

* [Sandbox\_Docs\_Trusted](#trusted)
* [Sandbox\_Docs\_Archives](#archives)
* [Sandbox\_Exes\_Web](#exes-web)

These rules are disabled by default and can be enabled and updated to suit your organization's needs.

To learn more, see [About Sandbox](/zia/about-sandbox).

* Rule Order: 1
* Admin Rank: 7
* Rule Name: Sandbox\_Docs\_Trusted
* Rule Status: Disabled
* File Types: Microsoft Office (group) & PDF
* Sandbox Categories: All
* Protocols: FTP over HTTP, HTTP, HTTPS, Native FTP
* First-Time Action: Allow & Scan
* AI Instant Verdict: Enabled
* Action for Subsequent Downloads: Block
* Description: Advanced Sandbox Documents rule created during company creation. This policy rule is intended to be used with a custom user-defined URL Category Trusted Sites (or other applicable name), which after creation needs to be added to the policy via the URL Category control. This policy rule intentionally does not subject documents coming from Trusted Sites to the same level of inspection as untrusted sites.

* Rule Order: 2
* Admin Rank: 7
* Rule Name: Sandbox\_Docs\_Archives
* Rule Status: Disabled
* File Types: Microsoft Office (group), PDF, and Archives (group)
* Sandbox Categories: All
* Protocols: FTP over HTTP, HTTP, HTTPS, Native FTP
* First-Time Action: Quarantine
* AI Instant Verdict: Enabled
* Action for Subsequent Downloads: Block
* Description: Advanced Sandbox Documents and Archives rule created during company creation. This rule must apply to all URL categories other than the custom user-defined URL Category Trusted Sites.

* Rule Order: 3
* Admin Rank: 7
* Rule Name: Sandbox\_Exes\_Web
* Rule Status: Disabled
* File Types: Executable (group), Web Content (group)
* Sandbox Categories: All
* Protocols: FTP over HTTP, HTTP, HTTPS, Native FTP
* First-Time Action: Quarantine
* AI Instant Verdict: Enabled
* Action for Subsequent Downloads: Block
* Description: Advanced Sandbox Executables and Web Content rule created during company creation.

### Feature Available

#### DLP Rule Name Support for Web DLP Reports and Insights
Users can schedule Web DLP incident reports by DLP Rule Name to improve visibility and monitor incident counts in the Zscaler Admin Console:

Data Type DLP Rule Name is introduced in the Interactive Reports widgets and Web Insights.

[See image.](#dlp-rule-name)

To learn more, see [Web Data Types and Filters](/zia/web-data-types-and-filters).

![DLP Rule Name filter in the Data Type field](/sites/default/files/downloads/unified/getting-started-experience-center/zscaler-admin-console-access-navigation/signing-zscaler-admin-console/image-2026-03-11-12-12-32-666.png "DLP Rule Name filter")

### Feature Available

#### Document Classification and Logging for Email DLP Insights
AI or machine language classification is extended to support around 200 new document types across 10 common document categories.

As part of this extended support, Email DLP Insights Logs and the Nanolog Streaming Service (NSS) are enhanced to provide enriched auto-classification of documents that are uploaded or downloaded during transactions.

The following enhancements are available in the Zscaler Admin Console:

# Updates to Email DLP Insights Logs

A new filter and column, Subdocument Type, is added to the Email DLP Insights Logs to capture, categorize, and log document subtypes related to administrative documents, invoices, expense reports, and more.

[See image.](#subdocument_type)

To learn more, see [Email DLP Insights Logs: Columns](/unified/email-dlp-insights-logs-columns) and [Email DLP Insights Logs: Filters](/unified/email-dlp-insights-logs-filters).

# Updates to NSS Feeds

The field `%s{ac_doc_subtypes}` can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for Email DLP logs.

To learn more, see [NSS Feed Output Format: Email DLP Logs](/zia/nss-feed-output-format-email-dlp-logs).

![You can filter by Subdocument Type in the Email DLP Insights Logs page.](/sites/default/files/downloads/zia/dashboard-analytics/reports/about-microsoft-copilot-readiness-assessment/subdocument_type_email_logs.png "Subdocument Type Filter in Email DLP Insights Logs")

### Feature Available

#### Enhancements to Predefined O365 One Click rule in SSL/TLS Inspection Policy
You can choose Evaluate Other Policies or Bypass Other Policies under the Do Not Inspect action in the O365 One Click predefined rule in the SSL/TLS Inspection Policy. This allows you to configure the predefined O365 One Click rule to either evaluate other policies (i.e., URL Filtering and Cloud App Control) or bypass them.

[See image.](#configurable-predefined-o365-one-click)

To learn more, see [Configuring SSL/TLS Inspection Policy](/zia/about-ssltls-inspection-policy).

![Edit SSL Inspection Rule window for the Predefined Office 365 One Click](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/Zscaler-Edit-SSL-Inspection-Policy-RN.png "Edit SSL Inspection Rule window for the Predefined Office 365 One Click")

### Feature Available

#### Exclude Selected URL Classes & Categories from NSS Feeds
Filters to include or exclude selected URL classes, URL categories, and URL super categories have been added to NSS and Cloud NSS feeds for web logs. When configuring a feed, you can select the respective URL classes and categories and include them in the logs by default or choose to exclude them from the logs.

[See image.](#img-nss-url-categories-include-exclude-filter)

To learn more, see [Adding NSS Feeds for Web Logs](/zia/adding-nss-feeds-web-logs#Twhere) and [Adding Cloud NSS Feeds for Web Logs](/zia/adding-cloud-nss-feeds-web-logs#Twhere).

![URL Categories filter with Include/Exclude functionality](/sites/default/files/downloads/release-notes-drafts/URL%20Category%20Exclude%20Filter.png "URL Categories Include and Exclude Options")

# Enhancement to the Cloud Nanolog Streaming Service (NSS) API

New fields `urlCategoriesExclude`, `urlClassesExclude`, and `urlSuperCategoriesExclude` are available for the `ZmanageNssFeed` model in the `/nssFeeds` APIs.

To learn more, go to the `ZmanageNssFeed` model from [Cloud Nanolog Streaming Service (NSS)](/zia/cloud-nanolog-streaming-service-nss).

### Feature Available

#### New Network Applications in Firewall Control
The Zscaler service extends support to identify two new network applications, namely Kafka (Application Service category) and Zalo (Instant Messaging category). You can view these apps on the Network Applications page and configure them in Firewall Filtering rules to identify and manage associated traffic.

[See image.](#new-network-apps-kafka-zalo)

To learn more, see [About Network Applications](/zia/about-network-applications).

![Kafka and Zalo network apps supported in Firewall Filtering rule conditions](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/Firewall-filtering-kafka-zalo-network-apps.png "Kafka and Zalo Network Apps in Firewall Filtering Rules")

### Feature Available

#### Support for Cloud NSS Feeds for Alerts
You can configure a separate Cloud NSS feed for alerts, enabling you to monitor your Cloud NSS feeds for data lag, data loss, and the connection to your cloud-based security information and event management (SIEM) system.

[See image.](#img-cloud-nss-alert-feed)

To learn more, see [Adding Cloud NSS Feeds for Alerts](/zia/adding-cloud-nss-feeds-alerts).

![Add Cloud NSS feed for Alerts ](/sites/default/files/downloads/zia/release-notes/internet-saas-service-release-notes/release-upgrade-summary-2026/cloud-nss-alert-feed.png "Add Cloud NSS feed for Alerts ")

## April 03, 2026

### Feature Available

#### API Session Timeout
When configuring advanced settings (Policies > Common Configuration > Advanced > Advanced Settings), you can specify how long API-initiated sessions can be inactive before they are forced to reauthenticate. The timeout duration can range from 5 to 20 minutes.

[See image.](#api-timeout)

To learn more, see [Configuring Advanced Settings](/zia/configuring-advanced-settings#auth-exemption).

![API Session Timeout Duration in the Advanced Settings](/sites/default/files/downloads/zia/release-notes/release-upgrade-summary-2026/API-session-timeout.png "API Session Timeout Duration in the Advanced Settings")

# Enhancement to the Advanced Settings API

A new field, `apiSessionTimeout`, is available for the `AdvancedSettings` model in the `/advancedSettings` APIs.

To learn more, go to the `AdvancedSettings` model from [Advanced Settings](/zia/advanced-settings).

### Feature Available

#### Subdocument Type Support in Data Discovery Report
The Data Discovery Report is enhanced to include subdocument type support, providing enhanced visibility via an interactive bubble chart for ML categories. This chart utilizes nested bubbles to represent granular subdocument types, such as tax forms and legal contracts. By drilling down, users can access an expanded 4-column view where a new Subcategory column displays these specific subdocument classifications.

[See image.](#data_discovery_rn)

To learn more see, [About the Data Discovery Report](/zia/about-data-discovery-report) and [Viewing Data Discovery Details](/zia/viewing-data-discovery-details).

![The Data Discovery Report shows interactive bubble chart for various content types.](/sites/default/files/downloads/tech-pubs-drafts/miscellaneous-draft-articles/about-probe-overview/Subdocument_Type_Data_Discovery_RN.png "Data Discovery Report")

### Feature Available

#### Update to Workload Groups Endpoints
You can delete a list of workload groups for an organization using the `DELETE /workloadGroups` endpoint. To learn more, go to `DELETE /workloadGroups` from [Workload Groups](/zia/workload-groups).

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

## April 02, 2026

## March 31, 2026

### Feature Available

#### Enhancement to Advanced Threat Protection Policy
Advanced Threat Protection now enables users to allow the Web Proxy Auto-Discovery (WPAD) protocol from external sources to automatically discover proxy settings by locating PAC files via DHCP or DNS queries. To learn more, see [Configuring the Advanced Threat Protection Policy](/zia/configuring-advanced-threat-protection-policy).

## March 26, 2026

### Feature Available

#### Memory Requirement for Standalone Deployment of Virtual Service Edge for Internet & SaaS
A stand-alone deployment of Virtual Service Edges for Internet & SaaS (ZIA) on all platforms (i.e., VMware ESXi, Microsoft Azure, AWS EC2, Microsoft Hyper-V, and GCP) requires a minimum of 48 GB of memory.

To learn more, see [About Virtual Service Edges for Internet & SaaS](/zia/about-virtual-service-edges).

## March 20, 2026

### Feature Available

#### Updates to Data Loss Prevention Endpoints
You can update and retrieve information about the DLP Advanced Settings using the following endpoints:

* `GET /webDlpGlobalOptions`
* `PUT /webDlpGlobalOptions`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to HTTP Header Control Endpoints
You can create, update, and delete HTTP header profiles, and retrieve a list of all HTTP header profiles using the following endpoints:

* `GET /httpHeaderProfile`
* `POST /httpHeaderProfile`
* `PUT /httpHeaderProfile/{id}`
* `DELETE /httpHeaderProfile/{id}`

You can create, update, and delete HTTP header insertion profiles, and retrieve a list of all HTTP header insertion profiles using the following endpoints:

* `GET /httpHeaderActionProfile`
* `POST /httpHeaderActionProfile`
* `PUT /httpHeaderActionProfile/{id}`
* `DELETE /httpHeaderActionProfile/{id}`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).

### Feature Available

#### Updates to Root Certificates and Intermediate CA Certificates Endpoints
You can create, update, and delete root certificates and retrieve information about the root certificates for third-party proxy-chaining services or isolation profiles using the following endpoints:

* `GET /rootCertificates`
* `POST /rootCertificates`
* `GET /rootCertificates/{rootCertId}`
* `PUT /rootCertificates/{rootCertId}`
* `DELETE /rootCertificates/{rootCertId}`

You can delete an intermediate Certificate Authority (CA) certificate, retrieve a list of all intermediate CA certificates for SSL Inspection, and download an intermediate CA certificate using the following endpoints:

* `GET /sslCertificates`
* `GET /sslCertificates/certDetail/{certId}`
* `DELETE /sslCertificates/{certId}`
* `GET /sslCertificates/download/{certId}`

To learn more about each endpoint, see the [API Reference](/zia/about-api) and [API Rate Limit Summary](/zia/api-rate-limit-summary).