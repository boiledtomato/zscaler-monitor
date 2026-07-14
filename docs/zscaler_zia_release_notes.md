# ZIA リリースノート

> 最終更新: 2026-07-14 23:20 UTC
> ソース: https://help.zscaler.com/zia/release-notes

---

## Release Upgrade Summary (2026)

This article provides a summary of all new features and enhancements per Zscaler cloud for Zscaler Internet Access (ZIA). Zscaler will email a notification to your organization's registered support contacts approximately one week before your cloud is upgraded. To see scheduled maintenance updates for your cloud, visit the Trust Portal .

### 関連記事（他年度）
- [Release Upgrade Summary (2026)](https://help.zscaler.com/zia/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](https://help.zscaler.com/zia/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](https://help.zscaler.com/zia/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](https://help.zscaler.com/zia/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](https://help.zscaler.com/zia/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](https://help.zscaler.com/zia/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](https://help.zscaler.com/zia/release-upgrade-summary-2020)
- [Release Upgrade Summary (2019)](https://help.zscaler.com/zia/release-upgrade-summary-2019)

## 2026年 リリースノート一覧

Zscalerクラウド: zscaler.net


### July 06, 2026

#### New Cloud Applications
New cloud applications are added to the cloud application categories. You can download the list of newly added cloud applications to the respective categories: Download 

The risk index and risk attribute values for these new applications are visible only after they are available on all the clouds. Refer to the trust post for details.

#### NSS Support for 3rd-Party App Governance and Posture Management Logs
Logs for Zscaler 3rd-Party App Governance and Posture Management are supported by Zscaler's Nanolog Streaming Service (NSS). You can configure NSS and Cloud NSS feeds for both log types to stream their respective data to your security information and event management (SIEM) system, providing a unified view of your organization's security posture for effective threat management.

Access to these log types requires a subscription to Advanced SaaS Security Posture Management (SSPM) . To subscribe to Advanced SSPM, contact your Zscaler Account team.

 See image. 
 
When creating a policy in 3rd-Party App Governance, you can select the Zscaler Nanolog Streaming Service option to receive alerts for the policy through NSS every time the policy is triggered.

 See image. 

To learn more, see:
 
- Adding NSS Feeds for 3rd-Party App Governance Logs
- Adding Cloud NSS Feeds for 3rd-Party App Governance Logs
- NSS Feed Output Format: 3rd-Party App Governance Logs
- Adding NSS Feeds for Posture Management Logs
- Adding Cloud NSS Feeds for Posture Management Logs
- NSS Feed Output Format: Posture Management Logs
- 3rd-Party App Governance Policies 
# Enhancement to Cloud Nanolog Streaming Service (NSS) API

Two new enum values, POSTURE_CONTROL and APP_GOVERNANCE are added to the nssLogType field in the ZmanageNssFeed model referenced by the /nssFeeds APIs

To learn more, go to the ZmanageNssFeed model from Cloud Nanolog Streaming Service (NSS) .

#### Updates to Cloud Applications
As part of a continuous review, Zscaler has updated cloud applications across various cloud application categories. To obtain the list of cloud applications that have been updated, download the list: Download 

Cloud applications are updated in phases. Refer to the trust post for details.


### July 01, 2026

#### Enterprise Browser for Zero Trust Browser
The Enterprise Browser feature for Zero Trust Browser is a way to protect users from everyday browser-based threats. Users can access private applications for their organization while utilizing browser protection for daily operations such as file transfer, data sharing, and cloud service authentication.

To learn more, see Understanding Enterprise Browser .


### June 29, 2026

#### Additional Support for Microsoft 365 Apps in Advanced SSPM
Advanced SaaS Security Posture Management (SSPM) supports new posture controls as part of the Microsoft 365 connector for the following apps:
 
- Microsoft Power Apps
- Microsoft Power BI
- Microsoft Purview
- Microsoft Viva Engage 
Existing tenants must grant additional permissions and reauthenticate the connector for these additional posture controls.

Select the SSPM Scan checkbox when onboarding a Microsoft 365 tenant to enable the Advanced SSPM scan capability for the specific tenant.

 See image. 

The SSPM Scan checkbox is enabled only when you have Advanced SSPM enabled for your tenant.

To learn more, see What Is Advanced Posture Management? , Adding SaaS Application Tenants , and Authorizing a Custom Zscaler Connector for Microsoft Applications .


### June 26, 2026

#### Block Domain Fronting Enhancement
In Advanced Settings (Policies > Common Configuration > Advanced > Advanced Settings > Domain Fronting), there are two new options available under Block Domain Fronting:
 
- URL Category Exemptions for Block Domain Fronting: Select the URL categories you want to exempt from domain fronting.
- Exempted Cloud Applications for Block Domain Fronting: Select the cloud app categories or cloud apps you want to exempt from domain fronting. 
 See image. 

To learn more, see Configuring Advanced Settings .

#### Enhanced Web Logs: Added Support for DLP Policy Actions and Justification Messages
You can filter and view logs for DLP policy actions and DLP confirmation messages. As part of the update, the following changes are available in the Zscaler Admin Console:

# Insights Logs

Filters and columns, DLP Policy Action and DLP Confirmation Message, are added to Web Insights Logs and Endpoint DLP Insights Logs.

 See image. 

To learn more, see Web Insights Logs: Columns , Web Insights Logs: Filters , Endpoint DLP Insights Logs: Columns , and Endpoint DLP Insights Logs: Filters .

# NSS Feeds

The fields %s{dlp_policy_action} and %s{dlp_confirm_justification_msg} can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for web logs. Additionally, the field %s{dlp_confirm_justification_msg} is available for NSS and Cloud NSS feeds for Endpoint DLP logs.

To learn more, see NSS Feed Output Format: Web Logs and NSS Feed Output Format: Endpoint DLP Logs .


### June 24, 2026

#### New Labels and Values in SaaS Security Report
Instead of classifying all new applications as Unsanctioned, you can use new Application Status labels Unclassified and Under Review, to classify applications more appropriately. The label Unclassified means the applications haven't been evaluated for risks yet, and Under Review means they are undergoing due diligence.

 See image. 

Moreover, the SaaS Security Report for each cloud application now displays detailed information about security attributes including their certificate validity, WAF name, CVE ID, breach URL, and so on. More information appears in brackets next to the Yes and No signals.

 See image. 

To learn more, see About the SaaS Security Report and About the Application Information .


### June 23, 2026

#### Enhancement to Application Service Groups
The Application Services page has been enhanced to allow you to define your own application service groups. This page contains the following enhancements:
 
- You can add custom application service groups.
- The Definition column is added.
- You can view, edit, and filter the application service groups under a new column. 
The Custom Application Service Group is available if Advanced Firewall is enabled for your organization.

 See image. 

To learn more, see Configuring Application Service Groups and About Application Service Groups .

# Update to Forwarding Policy, IPS Control Policy, and Firewall Filtering Policy

The Forwarding policy, IPS Control policy, and Firewall Filtering policy allow you to select predefined (AU) and custom (CU) application service groups while configuring these policies.

 See image. 

To learn more, see Configuring Forwarding Policy , Configuring IPS Control Policy , and Configuring the Firewall Filtering Policy .

# Update to Cloud Service API

The cloud service API includes the following new endpoints to create, update, and delete custom application service groups, and retrieve configurations for all custom application service groups (predefined and custom):
 
- GET /apps-services
- POST /apps-services
- GET /apps-services/{appServiceId}
- PUT /apps-services/{appServiceId}
- DELETE /apps-services/{appServiceId} 
To learn more, see the API Reference .


### June 19, 2026

#### Support for Snowflake as an API-Based Platform in Advanced SSPM
Advanced SaaS Security Posture Management (SSPM) supports Snowflake as an API-based platform to provide visibility into posture misconfigurations. You can configure Advanced SSPM for Snowflake tenants. Select the SSPM Scan checkbox when onboarding a tenant to enable the Advanced SSPM scan capability for the specific tenant.

 See image. 

The SSPM Scan checkbox is enabled only when you have Advanced SSPM enabled for your tenant.

To learn more, see What Is Advanced Posture Management? and Adding SaaS Application Tenants .


### June 18, 2026

#### Enhancement to Browser EUN Template
You can set a caution interval per browser EUN template, which allows you to configure different caution intervals for different browser EUNs. As part of this change, in the Administration > End User Notifications > Browser > EUN Templates > Add Custom Message window, the Caution Interval drop-down menu is added.

 See image. 

To learn more, see Configuring Browser EUN Template .


### June 16, 2026

#### Advanced SSPM Support for Databricks
Advanced SSPM supports a new platform, Databricks. You can onboard a Databricks tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with Databricks and Connecting Your Platforms to Advanced SSPM .

#### Advanced SSPM Support for OpenAI
Advanced SSPM supports a new platform, OpenAI. You can onboard an OpenAI tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with OpenAI and Connecting Your Platforms to Advanced SSPM .


### June 08, 2026

#### Expanded SSPM Controls for Box
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Box with 4 new SSPM controls, providing deeper visibility and stronger security posture assessment.


### June 05, 2026

#### Ability to Select Channels for DLP Engines
You can define custom and predefined DLP engines to apply only to specific channels (e.g., Endpoint DLP, DSPM) to reduce the extra noise that can come from engines being on particular channels unnecessarily. This functionality is available when you create, edit, or clone a DLP engine on the DLP Engines page (Policies > Data Protection > Common Resources > DLP Dictionaries & Engines > DLP Engines):

 See image. 

To learn more, see Editing Predefined DLP Engines , Adding Custom DLP Engines , and Cloning DLP Engines .


### June 04, 2026

#### Endpoint Context Limited Availability
To enable Endpoint Context for your organization, contact Zscaler Support.

Zscaler Endpoint Context extends the Zero Trust Exchange (ZTE) to provide unified cloud-to-endpoint visibility, detection, and dynamic risk-based policy enforcement. This functionality integrates real-time endpoint application data with industry-leading cloud intelligence to help your Security Operations Center (SOC) teams defend your organization from modern, sophisticated, AI-accelerated attacks that often bypass traditional siloed security tools.

Endpoint Context takes advantage of extensive data available from Zscaler Client Connector to provide an inventory of commonly abused applications that reside on each endpoint, both actively running and at rest, and enumerates a rich data set related to each application, including application name, publisher, total instances of an application, install path, etc.

The Application Investigation page (Policies > Cybersecurity > Endpoint Context > Application Investigation) provides a dashboard with useful information about the applications installed on endpoints across your organization. From the Application Investigation page, you can see the Overview page (Policies > Cybersecurity > Endpoint Context > Application Investigation > Overview), which contains useful tables and charts that categorize information about all applications:

 See image. 

On the Inventory page (Policies > Cybersecurity > Endpoint Context > Application Investigation > Inventory), you can use various criteria (e.g., OS, certificate status, threat type, vulnerabilities) to review the application information most important to your SOC teams:

 See image. 

You can click any of the applications in the list to drill down to more granular detail:

 See image. 

Additionally, when you license Endpoint Context for your organization, you have the ability to specify application details for both Windows and macOS endpoints on the DLP & Endpoint Resources page (Policies > Data Protection > Endpoint DLP Resources > Applications):

 See image. 

You can also add Endpoint Application Tags so that you can group applications by category or theme (e.g., browsers or compression utilities):

 See image. 

If you have also licensed Endpoint Data Loss Prevention (DLP) for your organization, any resource groups that you have already configured are automatically converted to resource tag groups. All policies that previously used resource groups are automatically updated to use the converted resource tag groups.

With applications configured, you can apply your custom application configurations, or use the default configurations provided by the Zscaler service, to various policies in the Zscaler Admin Console (e.g., Advanced Firewall, DNS Control, SSL/TLS Inspection):

 See image. 

# Update to Cloud Service API

The cloud service API includes new endpoints to create and manage endpoint application resources and updates to existing policy APIs to configure endpoint application-based conditions in policy rules.
 
- Endpoint Application Resources
- Endpoint Application Tags
- Policy Rules 
 Using the following API endpoints, you can create, update, and delete custom endpoint applications and update and retrieve information about all endpoint applications, including well-known, discovered, and custom applications. You can also retrieve the count of applications available within a specific category and the list of policy rules associated with a specific application.
 
- GET /endPointApplications/customApps
- POST /endPointApplications/customApp
- PUT /endPointApplications/customApp/{id}
- DELETE /endPointApplications/customApp/{id}
- GET /endPointApplications/customApps/{id}
- GET /endPointApplications/customApps/lite
- GET /endPointApplications
- GET /endPointApplications/lite
- PUT /endPointApplications/{id}
- GET /endPointApplications/cloudApps
- GET /endPointApplications/policies
- GET /endPointApplications/getCategoriesWithNonEmptyApps
- GET /endPointApplications/count
- GET /endPointApplications/cloudApps/count 
To learn more, see the API Reference and API Rate Limit Summary .
 
 The following API endpoints allow you to create and manage endpoint application tag groups. You can create, update, and delete endpoint application tags and retrieve information about the application tags. You can also manage endpoint applications associated with a tag and retrieve the list of policy rules associated with a tag.
 
- GET /endPointApplicationGroups
- POST /endPointApplicationGroups
- GET /endPointApplicationGroups/{id}
- PUT /endPointApplicationGroups/{groupId}
- DELETE /endPointApplicationGroups/{id}
- PUT /endPointApplicationGroups/resources/{groupId}
- GET /endPointApplicationGroups/policies 
To learn more, see the API Reference and API Rate Limit Summary .
 
 The SSLInspectionRule , FirewallFilteringRule , and FirewallDnsRule models include the following attributes to configure policy rule conditions based on endpoint applications, endpoint application tags, and endpoint application threat levels:
 
- endPointApplications
- endPointApplicationGroups
- endPointApplicationThreatLevels
- excludeContextShieldEndPoint (supported only in FirewallFilteringRule and FirewallDnsRule models)

#### Logs for JA4 Network Fingerprinting
Enhancements to Insights Logs and the Nanolog Streaming Service (NSS) provide real-time visibility into the TLS/SSL server communication by capturing JA4 network fingerprints at the connection level and logging them within the Internet & SaaS (ZIA) web logs. The enhancements enable network security teams to monitor, analyze, and respond to encrypted traffic without waiting for sessions to complete.

To enable this feature, contact Zscaler Support.

As part of the update, the following changes are available in the Zscaler Admin Console:

# Web Insights Logs

The following filters and columns are added to Web Insights Logs:
 
- JA4 Fingerprint
- JA4 Fingerprint A
- JA4 Fingerprint B
- JA4 Fingerprint C 
 See image. 

To learn more, see Web Insights Logs: Columns and Web Insights Logs: Filters .

# NSS Feeds for Web Logs

The field %s{ja4_str} can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for web logs.

To learn more, see NSS Feed Output Format: Web Logs .


### June 01, 2026

#### Redactive Sensitive Text for Isolation in Internet & SaaS
Zero Trust Browser allows admins to enable the redaction of sensitive text data for configured Data Loss Prevention (DLP) engines and dictionaries based on the DLP configuration in an isolation profile.

 See image. 

To learn more, see Using Redactive Sensitive Text for Isolation and Creating Isolation Profiles for Internet & SaaS .


### May 26, 2026

#### Secure Message Processing Center (SMPC) Instance Endpoints
You can update the data center and the Secure Message Processing Center (SMPC) instance details based on a specific data center ID and retrieve the status of all SMPC instances grouped by a data center using the following endpoints:
 
- GET /smpcInstance
- PUT /smpcInstance/dc 
A new Enum value, ZS_BUSINESS_CONTINUITY is available in the permissions field of the AdminRole model used by the /adminRoles APIs. This enum allows administrators to grant permission to update or view the SMPC instance isolation.

To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### May 22, 2026

#### Enhancements for Isolation User Experience Loading Page
The following updates have been made to the isolation experience for Zero Trust Browser:
 
- As you enter an isolated session, a static, temporary message appears in the middle of the web page as it loads to confirm you are entering an isolated session. Additionally, an animated green outline appears around the website border as the page loads.
See image.
- When the page has completely rendered, a temporary notification banner appears in the upper-right corner that displays a customized notification title. You can click the Show More link in the banner to view a message customized by the admin.
See image.
- A floating checkmark icon also appears when the page has completely rendered, and stays visible after the temporary notification banner disappears. This is a visual indicator that the isolation session is persisting and has not expired.
See image. 
To learn more, see Adding a Banner Theme for the Isolation End User Notification in ZIA .

#### Updates to Devices Endpoints
You can retrieve information about devices registered with Zscaler using the following endpoints:
 
- GET /devices
- GET /devices/{id} 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to Partner Integrations APIs
You can retrieve a list of partners and services integrated with the Zscaler service, a list of configured CrowdStrike endpoints or device IDs, and detailed endpoint or device data based on the IDs using the following integration endpoints:
 
- GET /integrationPartners
- GET /integrationPartners/crowdStrike/endpoints
- POST /integrationPartners/crowdStrike/endpoints
- GET /integrationPartners/crowdStrike/whitelistedBaseUrls 
You can configure the integration of Microsoft Defender for Endpoint APIs with Zscaler and retrieve the MD5 hash of the file required to view the Sandbox Detail Report using the following endpoints:
 
- POST /integrationPartners/microsoftDefender/endpoints
- GET /integrationPartners/sandbox/report/{md5} 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### May 18, 2026

#### Zscaler URL Category Test
The Zscaler URL category test provides a set of standardized, immutable test URLs specifically designed for HTTPS URL policy validation testing. These Zscaler-managed sites maintain persistent categorization, allowing administrators to consistently verify that URL Filtering rules and SSL/TLS Inspection policies are being applied as intended.

Because these URLs are immutable, they provide a baseline for confirming HTTPS URLs and SSL/TLS policy actions without the risk of external site changes.

 See image. 

To learn more, see About URL Categories .


### May 15, 2026

#### Increased File Size Support for Advanced Detections
With the Advanced Detections package for Advanced Sandbox, you can analyze EXE and DLL files with sizes up to 200 MB.

To learn more, see About Sandbox .

#### Sandbox for Private Access Assets
Organizations with Advanced Sandbox that use Internet & SaaS (ZIA) to inspect Private Access (ZPA) traffic can sandbox unknown files uploaded to Private Access assets.

To learn more, see About Sandbox .

#### Support for AI/ML Detection Source
The Zscaler Admin Console is enhanced with the ability to view the AI/ML detection source for your Internet & SaaS (ZIA) traffic. The following updates are available:

# Web Insights Logs

The AI/ML Detection Source filter and column are added to the Web Insights Logs page.

 See image. 

To learn more, see Web Insights Logs: Columns and Web Insights Logs: Filters .

# Analytics

The Top AI/ML Detection Source by Security Incidents widget and the AI/ML Detection Source field are added to the Threat Incidents table and Details tab.

 See image. 

To learn more, see About Cybersecurity Insights .

# Nanolog Streaming Service (NSS)

You can use the filter AI/ML Detection Source when configuring an NSS or Cloud NSS feed for web logs.

 See image. 

Additionally, you can add the field %s{ai_ml_detection_src} to the Feed Output Format.

To learn more, see:
 
- Adding NSS Feeds for Web Logs
- Adding Cloud NSS Feeds for Web Logs
- NSS Feed Output Format: Web Logs

#### Support for Display of Site Type for SharePoint Tenants
When creating a site on SharePoint, you can define the site type as Public, Private, or Communication. These site types are displayed on the Manage SaaS Application Tenants > Components page.

 See image. 

To learn more, see Manage SaaS Application Components .

#### Support for DLP Scan Timeout Identifiers in Web Insights Logs
You can filter and view logs for specific DLP identifiers of transactions that were exempted from policy enforcement due to a scan timeout.

As part of the update, the following changes are available in the Zscaler Admin Console:

# Web Insights Logs

The filter and column Exempted DLP Identifier is added to the Web Insights Logs.

 See image. 

To learn more, see Web Insights Logs: Filters and Web Insights Logs: Columns .

# NSS Feeds

The field %d{exempt_dlpidentifier} can be added to the Feed Output Format when configuring NSS or Cloud NSS feeds for web logs.

To learn more, see NSS Feed Output Format: Web Logs .

#### Support for Restoring Quarantined Files in Salesforce
You can now restore quarantined Salesforce files to their original location with the Restore remediation action on the SaaS Security Assets page.

 See image. 

This action is available only for files initially quarantined using the Quarantine Malware action within the DLP Malware policy.

All files quarantined before this feature update are restored to the Salesforce user folder, specifically within Files > Owned by me.

To learn more, see Understanding the Assets Report: Assets with Incidents .

#### Third-Party Proxies and Gateways Limits
You can add up to 255 proxies and proxy gateways for third-party proxy services (Infrastructure > Internet & SaaS > Network Policies > Proxies & Gateways) in the Zscaler Admin Console.

To learn more, see Ranges & Limitations .

# Update to Cloud Service API

You can add a maximum of up to 255 proxies using the POST /proxies API. To increase the limit to a desired value, contact Zscaler Support to request a configuration change for your tenant.


### May 08, 2026

#### Additional Support for Predefined DLP Dictionaries in Endpoint DLP
The following predefined Data Loss Prevention (DLP) dictionaries are now supported for use in Endpoint DLP policy rules:
 
- Addresses (Japan)
- First Names (Japan)
- Full Names (Japan)
- Last Names (Japan) 
To learn more, see Understanding Predefined DLP Dictionaries .

#### Enhancement to Cloud Application Instances
The cloud application instances feature is extended to new cloud applications. You can create cloud application instances for the following cloud applications:
 
- Google Gemini
- Microsoft Copilot 
 See image. 

To learn more, see About Cloud Application Instances .

#### Instance Discovery Report Support for Azure
You can view the Instance Discovery Report for Microsoft Azure; this application supports three levels of discovery:
 
- Domain
- Tenant
- Resource 
 See image. 

To learn more, see About the Instance Discovery Report and Viewing the Resource Discovery Report .

#### Updates to Malware Protection Policy Endpoints
You can update the Malware Protection policy and retrieve the Malware Protection policy for an organization using the following endpoints:
 
- GET /malwarePolicy
- PUT /malwarePolicy 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to NSS Collector Server Endpoints
You can add, update, and delete NSS Collector servers and retrieve a list of all configured NSS Collector servers for an organization using the following endpoints:
 
- GET /nssCollectors
- POST /nssCollectors
- PUT /nssCollectors/{id}
- DELETE /nssCollectors/{id} 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to Secure Browsing and Votiro CDR Endpoints
You can retrieve a list of all supported browsers and their versions and update the Smart Browser Isolation policy settings using the following endpoints:
 
- GET /browserControlSettings/supportedBrowserVersions
- PUT /browserControlSettings/smartIsolation 
You can update, delete, and retrieve the Votiro CDR authentication credentials and retrieve the Votiro CDR policies configured for a tenant using the following endpoints:
 
- GET /isolationVotiroCdr/policies
- GET /isolationVotiroCdr/tokenConfig
- PUT /isolationVotiroCdr/tokenConfig
- DELETE /isolationVotiroCdr/tokenConfig 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to the IPS Control Policy Endpoints
You can create, update, delete, and retrieve custom IPS signature rules using the following endpoints:
 
- GET /ipsSignatureRules
- POST /ipsSignatureRules
- GET /ipsSignatureRules/{id}
- PUT /ipsSignatureRules/{id}
- DELETE /ipsSignatureRules/{id} 
You can export and import custom IPS signature rules, and validate the rule text for a new custom signature rule using the following endpoints:
 
- GET /ipsSignatureRules/export
- GET /ipsSignatureRules/import
- POST /ipsSignatureRules/import
- POST /ipsSignatureRules/validateRuleText 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### May 07, 2026

#### Expanded SSPM Controls for Bitbucket
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Bitbucket with 9 new SSPM controls, providing deeper visibility and stronger security posture assessment.

#### Expanded SSPM Controls for Confluence
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Confluence with 5 new SSPM controls, providing deeper visibility and stronger security posture assessment.

#### Expanded SSPM Controls for Jira
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Jira with 5 new SSPM controls, providing deeper visibility and stronger security posture assessment.

#### Support for New Workday Filters and Prompts
You can use a new filter Last Functionally Updated to easily identify recently modified records when creating custom reports in Workday. Additionally, the prompts Starting Prompt and Ending Prompt fields provide greater control and precision when defining report parameters.

 See image. 

To learn more, see Adding SaaS Application Tenants .


### May 05, 2026

#### Increased Virtual Service Edge Instance Memory for Internet & SaaS on Amazon Web Services
Configuring Virtual Service Edge for Internet & SaaS (ZIA) on Amazon Web Services (AWS) requires 64 GB of instance memory.

Zscaler recommends the r7i.2xlarge instance size.

To learn more, see Configuring Virtual Service Edge for Internet & SaaS: Amazon Web Services and Configuring Virtual Service Edge for Internet & SaaS: Amazon Web Services with GWLB .


### May 01, 2026

#### Expanded SSPM Controls for Google Workspace
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Google Workspace with 24 new SSPM controls, providing deeper visibility and stronger security posture assessment. The Cloud Identity license must be assigned to the Google Workspace Admin onboarding the account. This is critical to ensure appropriate license and compliance with Google Cloud Identity and Workspace policies. Additional API scopes are required for existing tenants to view the new Cloud Identity policies.

To learn more, see Adding SaaS Application Tenants .

#### Gen AI Prompt Configuration for QuillBot and Google AI
Zscaler's Gen AI prompt configuration is extended to the QuillBot and Google AI generative AI applications. You can enable prompts for these generative AI applications to categorize and store the prompts for the respective applications.

 See image. 

To learn more, see Configuring Advanced Policy Settings .

# Added QuillBot and Google AI Capabilities to URL & Cloud App Control Policy Settings Endpoint

Two new Boolean fields, enableQuillbotAIPrompt and enableGoogleAIPrompt , are available for the AdvancedUrlFilteringCloudAppOptions model in the /advancedUrlFilterAndCloudAppSettings APIs. These fields allow users to use generative AI prompts with QuillBot and Google AI.

To learn more, see URL & Cloud App Control Policy Settings .

#### Policy Level Gen AI Prompt Configuration
You can capture end user prompts for generative AI applications from the Cloud Application Control policy. This allows granular control of Gen AI prompt configuration. As part of this update, the Capture Prompts option is added to the Add/Edit AI & ML Rule window (Policies > Access Control > Internet & SaaS > Policies > Cloud App Control Policy > Add > AI & ML Applications).

This is applicable for Gen AI applications that are supported in the Gen AI Prompt Configuration section of the Advanced Policy Settings page.

 See image. 

To learn more, see Adding an AI & ML Applications Rule for Cloud App Control .

# Update to the Cloud App Control Policy Endpoint

A new Boolean field, promptCaptureEnabled , is available for the WebApplicationRule model in the /webApplicationRules APIs. This field enables users to allow or block the capture of end user prompts for generative AI applications.

To learn more, go to the WebApplicationRule model from Cloud App Control Policy .


### April 17, 2026

#### Adaptive Access Profiles Endpoints
You can retrieve a list of Adaptive Access profiles and information about an Adaptive Access profile using the following endpoints:
 
- GET /adaptiveAccessProfiles
- GET /adaptiveAccessProfiles/profiles/rules 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Enabling Incident Forwarding for Slack Chats
Zscaler is now forwarding Slack chat-based DLP policy incidents to the Zscaler Incident Response and Zscaler Workflow Automation along with already supported file-based violations. These incidents are also sent to Web Insights and Logs and to the respective DLP policy's auditor.

To learn more, see Understanding SaaS Security API Supported Capabilities , Configuring the Data at Rest Scanning DLP Policy with Content Inspection and Configuring the Data at Rest Scanning DLP Policy without Content Inspection .

#### Updates to Azure Integration Endpoints
You can retrieve the progress summary of the VPN connection refresh process and start a new asynchronous process to refresh the VPN connection status using the following endpoints:
 
- GET /azure/refreshConnectionStatus
- POST azure/refreshConnectionStatus 
You can retrieve the tunnel configuration status, start the tunnel configuration process, remove the tunnel configuration, and retrieve the status of the tunnel configuration removal process for a specified Azure hub using the following endpoints:
 
- GET /azure/tunnelConfiguration
- POST /azure/tunnelConfiguration
- DELETE /azure/unConfigureTunnel/{hubId}
- GET /azure/unConfigureTunnelStatus 
You can retrieve the Azure hub sync process details and start a process to sync the hubs using the following endpoints:
 
- GET /azure/virtualHubs
- GET /azure/virtualHubSync
- POST azure/virtualHubSync 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to Security & UEBA Alerts Endpoints
You can create, update, and delete alert definitions, and retrieve a list of all configured alert definitions for an organization using the following endpoints:
 
- GET /alertDefinitions
- POST /alertDefinitions
- GET /alertDefinitions/{alertDefinitionId}
- PUT /alertDefinitions/{alertDefinitionId}
- DELETE /alertDefinitions/{alertDefinitionId} 
You can create, update, and delete Security alert rules, and retrieve a list of all configured Security alert rules for an organization and their statuses using the following endpoints:
 
- GET /alertRuleConfiguration/rules
- POST /alertRuleConfiguration/rules
- GET /alertRuleConfiguration/rules/{ruleId}
- PUT /alertRuleConfiguration/rules/{id}
- DELETE /alertRuleConfiguration/rules/{id}
- GET /alertRuleConfiguration/rules/rulestatus 
You can create, update, and delete User and Entity Behavior Analytics (UEBA) alert rules, and retrieve a list of all configured UEBA alert rules using the following endpoints:
 
- GET /alertRuleConfiguration/uebaRules
- POST /alertRuleConfiguration/uebaRules
- GET /alertRuleConfiguration/uebaRules/{ruleId}
- PUT /alertRuleConfiguration/uebaRules/{id}
- DELETE /alertRuleConfiguration/uebaRules/{id} 
You can create, update, and delete webhooks, retrieve a list of all configured webhooks for an organization, and test a webhook configuration using the following endpoints:
 
- GET /alertRuleConfiguration/webhooks
- POST /alertRuleConfiguration/webhooks
- PUT /alertRuleConfiguration/webhooks/{id}
- DELETE /alertRuleConfiguration/webhooks/{id}
- POST /alertRuleConfiguration/webhooks/test 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### NSS Support for Admin Audit, Authentication Service Authentication, and Authentication Service SCIM Logs
The following enhancements are available for the NSS Feeds and Cloud NSS Feeds:
 
- New log types, Authentication Service Authentication and Authentication Service SCIM, are added to the NSS for Web type. These log types provide support for the Authentication Service Authentication and Authentication Service SCIM audit log reports.
- A new application filter, Authentication Service Admin Audit Log, is added to the Admin Audit Logs. 
To enable these NSS Feeds and Cloud NSS Feeds enhancements, contact Zscaler Support .

To learn more, see:
 
- Adding NSS Feeds for Authentication Service Authentication Logs
- Adding Cloud NSS Feeds for Authentication Service Authentication Logs
- Adding NSS Feeds for Authentication Service SCIM Logs
- Adding Cloud NSS Feeds for Authentication Service SCIM Logs
- Adding NSS Feeds for Admin Audit Logs
- Adding Cloud NSS Feeds for Admin Audit Logs


### April 15, 2026

#### DLP Support for New PII Dictionaries
The following are new predefined DLP dictionaries:
 
- Argentina Uniform Bank Code: Detect Leakage of CBU
- Cambodian National ID: Detect Leakage of Khmer Identification Code (KIdC)
- Mexico Business Tax ID: Detect Leakage of BRFC
- Mexico Individual Tax ID: Detect Leakage of IRFC
- Mexico Social Security Number: Detect Leakage of NSS 
To learn more, see Understanding Predefined DLP Dictionaries .

#### Support for Collaboration Scope for Microsoft Teams
When creating a DLP rule for Microsoft Teams, you can define the collaboration scope as External, Internal, or Any to scan messages and attachments in channels containing external, internal, or any (internal or external) members.

 See image. 

On the SaaS Security Analytics page, files from MS Teams that violate the DLP policy now show their collaboration scope, among other details.

 See image. 

To learn more, see Configuring the Data at Rest Scanning DLP Policy with Content Inspection and Configuring the Data at Rest Scanning DLP Policy without Content Inspection .

#### Support for Smartsheet as an API-Based Platform in Advanced SSPM
Advanced SSPM supports Smartsheet as an API-based platform to provide visibility into posture misconfigurations. You can onboard a Smartsheet tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with Smartsheet and Connecting Your Platforms to Advanced SSPM .


### April 14, 2026

#### Enhancement to Atlassian Integration in 3rd-Party App Governance
The Add Integration window for Atlassian in 3rd-Party App Governance is enhanced to allow you to enter the Atlassian subdomain and API token while adding the integration. This reduces the number of steps and simplifies the integration process to improve the user experience.

 See image. 

To learn more, see Integrating with Atlassian.


### April 10, 2026

#### Add or Remove NTP Servers Using CLI
You can add or remove custom NTP servers from the configuration files using CLI commands. This prevents syntax errors and duplicate entries in the configuration files.

To learn more, see Configuring Virtual Service Edge for Internet & SaaS and NTP Server Synchronization .

#### Default Rules for Advanced Sandbox
If your organization is subscribed to the Advanced Sandbox package, the following default rules are available:
 
- Sandbox_Docs_Trusted
- Sandbox_Docs_Archives
- Sandbox_Exes_Web 
These rules are disabled by default and can be enabled and updated to suit your organization's needs.

To learn more, see About Sandbox .
 
- Rule Order: 1
- Admin Rank: 7
- Rule Name: Sandbox_Docs_Trusted
- Rule Status: Disabled
- File Types: Microsoft Office (group) & PDF
- Sandbox Categories: All
- Protocols: FTP over HTTP, HTTP, HTTPS, Native FTP
- First-Time Action: Allow & Scan
- AI Instant Verdict: Enabled
- Action for Subsequent Downloads: Block
- Description: Advanced Sandbox Documents rule created during company creation. This policy rule is intended to be used with a custom user-defined URL Category Trusted Sites (or other applicable name), which after creation needs to be added to the policy via the URL Category control. This policy rule intentionally does not subject documents coming from Trusted Sites to the same level of inspection as untrusted sites. 
- Rule Order: 2
- Admin Rank: 7
- Rule Name: Sandbox_Docs_Archives
- Rule Status: Disabled
- File Types: Microsoft Office (group), PDF, and Archives (group)
- Sandbox Categories: All
- Protocols: FTP over HTTP, HTTP, HTTPS, Native FTP
- First-Time Action: Quarantine
- AI Instant Verdict: Enabled
- Action for Subsequent Downloads: Block
- Description: Advanced Sandbox Documents and Archives rule created during company creation. This rule must apply to all URL categories other than the custom user-defined URL Category Trusted Sites. 
- Rule Order: 3
- Admin Rank: 7
- Rule Name: Sandbox_Exes_Web
- Rule Status: Disabled
- File Types: Executable (group), Web Content (group)
- Sandbox Categories: All
- Protocols: FTP over HTTP, HTTP, HTTPS, Native FTP
- First-Time Action: Quarantine
- AI Instant Verdict: Enabled
- Action for Subsequent Downloads: Block
- Description: Advanced Sandbox Executables and Web Content rule created during company creation.

#### DLP Rule Name Support for Web DLP Reports and Insights
Users can schedule Web DLP incident reports by DLP Rule Name to improve visibility and monitor incident counts in the Zscaler Admin Console:

Data Type DLP Rule Name is introduced in the Interactive Reports widgets and Web Insights.

 See image. 

To learn more, see Web Data Types and Filters .

#### Document Classification and Logging for Email DLP Insights
AI or machine language classification is extended to support around 200 new document types across 10 common document categories.

As part of this extended support, Email DLP Insights Logs and the Nanolog Streaming Service (NSS) are enhanced to provide enriched auto-classification of documents that are uploaded or downloaded during transactions.

The following enhancements are available in the Zscaler Admin Console:

# Updates to Email DLP Insights Logs

A new filter and column, Subdocument Type, is added to the Email DLP Insights Logs to capture, categorize, and log document subtypes related to administrative documents, invoices, expense reports, and more.

 See image. 

To learn more, see Email DLP Insights Logs: Columns and Email DLP Insights Logs: Filters .

# Updates to NSS Feeds

The field %s{ac_doc_subtypes} can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for Email DLP logs.

To learn more, see NSS Feed Output Format: Email DLP Logs .

#### Enhancements to Predefined O365 One Click rule in SSL/TLS Inspection Policy
You can choose Evaluate Other Policies or Bypass Other Policies under the Do Not Inspect action in the O365 One Click predefined rule in the SSL/TLS Inspection Policy. This allows you to configure the predefined O365 One Click rule to either evaluate other policies (i.e., URL Filtering and Cloud App Control) or bypass them.

 See image. 

To learn more, see Configuring SSL/TLS Inspection Policy .

#### Exclude Selected URL Classes & Categories from NSS Feeds
Filters to include or exclude selected URL classes, URL categories, and URL super categories have been added to NSS and Cloud NSS feeds for web logs. When configuring a feed, you can select the respective URL classes and categories and include them in the logs by default or choose to exclude them from the logs.

 See image. 

To learn more, see Adding NSS Feeds for Web Logs and Adding Cloud NSS Feeds for Web Logs .

# Enhancement to the Cloud Nanolog Streaming Service (NSS) API

New fields urlCategoriesExclude , urlClassesExclude , and urlSuperCategoriesExclude are available for the ZmanageNssFeed model in the /nssFeeds APIs.

To learn more, go to the ZmanageNssFeed model from Cloud Nanolog Streaming Service (NSS) .

#### New Network Applications in Firewall Control
The Zscaler service extends support to identify two new network applications, namely Kafka (Application Service category) and Zalo (Instant Messaging category). You can view these apps on the Network Applications page and configure them in Firewall Filtering rules to identify and manage associated traffic.

 See image. 

To learn more, see About Network Applications .

#### Support for Cloud NSS Feeds for Alerts
You can configure a separate Cloud NSS feed for alerts, enabling you to monitor your Cloud NSS feeds for data lag, data loss, and the connection to your cloud-based security information and event management (SIEM) system.

 See image. 

To learn more, see Adding Cloud NSS Feeds for Alerts .


### April 03, 2026

#### API Session Timeout
When configuring advanced settings (Policies > Common Configuration > Advanced > Advanced Settings), you can specify how long API-initiated sessions can be inactive before they are forced to reauthenticate. The timeout duration can range from 5 to 20 minutes.

 See image. 

To learn more, see Configuring Advanced Settings .

# Enhancement to the Advanced Settings API

A new field, apiSessionTimeout , is available for the AdvancedSettings model in the /advancedSettings APIs.

To learn more, go to the AdvancedSettings model from Advanced Settings .

#### Subdocument Type Support in Data Discovery Report
The Data Discovery Report is enhanced to include subdocument type support, providing enhanced visibility via an interactive bubble chart for ML categories. This chart utilizes nested bubbles to represent granular subdocument types, such as tax forms and legal contracts. By drilling down, users can access an expanded 4-column view where a new Subcategory column displays these specific subdocument classifications.

 See image. 

To learn more see, About the Data Discovery Report and Viewing Data Discovery Details .

#### Update to Workload Groups Endpoints
You can delete a list of workload groups for an organization using the DELETE /workloadGroups endpoint. To learn more, go to DELETE /workloadGroups from Workload Groups .

To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### April 02, 2026

#### Client Browser for Zero Trust Browser
Zero Trust Browser has been updated with several significant changes to provide seamless and secure enterprise access from any browser. The solution consists of three primary components: a browser extension that handles web-based security and access, a lightweight agent that enforces device posture controls and advanced data protection during the session, and a cloud browser for accessing private applications in an isolated session.

Zero Trust Browser implements the following security features through the combined extension and agent:
 
- Adaptive App Access: Enforcement of device posture controls to ensure that only compliant devices can access sensitive business applications.
- Browser-Based Threat Protection: Robust defense against malicious extensions, identity-based attacks, and emerging web threats.
- Data Exfiltration Prevention: Advanced security controls, including screenshot protection and keystroke logger prevention.


### March 31, 2026

#### Enhancement to Advanced Threat Protection Policy
Advanced Threat Protection now enables users to allow the Web Proxy Auto-Discovery (WPAD) protocol from external sources to automatically discover proxy settings by locating PAC files via DHCP or DNS queries. To learn more, see Configuring the Advanced Threat Protection Policy .


### March 26, 2026

#### Memory Requirement for Standalone Deployment of Virtual Service Edge for Internet & SaaS
A stand-alone deployment of Virtual Service Edges for Internet & SaaS (ZIA) on all platforms (i.e., VMware ESXi, Microsoft Azure, AWS EC2, Microsoft Hyper-V, and GCP) requires a minimum of 48 GB of memory.

To learn more, see About Virtual Service Edges for Internet & SaaS .


### March 20, 2026

#### Updates to Data Loss Prevention Endpoints
You can update and retrieve information about the DLP Advanced Settings using the following endpoints:
 
- GET /webDlpGlobalOptions
- PUT /webDlpGlobalOptions 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to HTTP Header Control Endpoints
You can create, update, and delete HTTP header profiles, and retrieve a list of all HTTP header profiles using the following endpoints:
 
- GET /httpHeaderProfile
- POST /httpHeaderProfile
- PUT /httpHeaderProfile/{id}
- DELETE /httpHeaderProfile/{id} 
You can create, update, and delete HTTP header insertion profiles, and retrieve a list of all HTTP header insertion profiles using the following endpoints:
 
- GET /httpHeaderActionProfile
- POST /httpHeaderActionProfile
- PUT /httpHeaderActionProfile/{id}
- DELETE /httpHeaderActionProfile/{id} 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Updates to Root Certificates and Intermediate CA Certificates Endpoints
You can create, update, and delete root certificates and retrieve information about the root certificates for third-party proxy-chaining services or isolation profiles using the following endpoints:
 
- GET /rootCertificates
- POST /rootCertificates
- GET /rootCertificates/{rootCertId}
- PUT /rootCertificates/{rootCertId}
- DELETE /rootCertificates/{rootCertId} 
You can delete an intermediate Certificate Authority (CA) certificate, retrieve a list of all intermediate CA certificates for SSL Inspection, and download an intermediate CA certificate using the following endpoints:
 
- GET /sslCertificates
- GET /sslCertificates/certDetail/{certId}
- DELETE /sslCertificates/{certId}
- GET /sslCertificates/download/{certId} 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### March 17, 2026

#### Outbound Email DLP Quarantine with Release or Delete Emails in Workflow Automation
Zscaler now supports the Quarantine action when configuring Outbound Email DLP policies for Microsoft Exchange. When Quarantine is selected, emails that match policy criteria are quarantined directly in Microsoft Exchange. To use the Quarantine feature, go to Policy > Email DLP and then select Quarantine under Action in the applicable policy rule.

 See image. 

Email Data Loss Prevention (DLP) incidents that Microsoft has quarantined are displayed in Workflow Automation. In Workflow Automation, you can release or delete the email to one or more of its recipients using one of the following methods:
 
- On the Incident Details page, an admin can select the Release Email Quarantine action from the Actions drop-down menu and select the recipients to release the email to or delete the email.

See image.
- When an end user responds to a user notification or escalation notification that is associated with a quarantined email incident, the notifications are enhanced to include a new Release Email to Recipients section that includes release quarantine options. 
To enable this feature for Workflow Automation, contact Zscaler Support.

To learn more, see:
 
- About Outbound Email Policy
- Configuring Outbound Email Policy Rules
- Step-by-Step Configuration Guide for Zscaler Outbound Email DLP
- Configuring Microsoft Exchange for Zscaler Outbound Email DLP
- Adding Email Tenants
- Managing Incidents
- Viewing & Managing Incident Details


### March 16, 2026

#### Advanced SSPM Support for Lucidchart
Advanced SSPM supports a new platform, Lucidchart. You can onboard a Lucidchart tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Connecting Your Platforms to Advanced SSPM .

#### Support for Zendesk as an API-Based Platform in Advanced SSPM
Advanced SSPM supports Zendesk as an API-based platform. You can onboard a Zendesk tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Connecting Your Platforms to Advanced SSPM .


### March 13, 2026

#### Document Classification and Logging for SaaS Security API, Email, and Endpoint DLP
AI or machine language classification is extended to support around 200 new document types across 10 common document categories.

As part of this extended support, Insights Logs and the Nanolog Streaming Service (NSS) are enhanced to provide enriched auto-classification of documents that are uploaded or downloaded during transactions.

The following enhancements are available in the ZIA Admin Portal:

# Updates to Insights Logs

A new filter and column, Subdocument Type, is added to the Endpoint DLP Insights Logs and SaaS Security Insights Logs pages for email applications (e.g., Gmail) to capture, categorize, and log document subtypes related to administrative documents, invoices, expense reports, and more.

 See image. 

To learn more, see Endpoint DLP Insights Logs: Filters , Endpoint DLP Insights Logs: Columns , and About SaaS Security Insights Logs .

# Updates to NSS Feeds

The field %s{doc_subtype} can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for Endpoint DLP logs. Additionally, the field %s{upload_doc_subtype} is available for SaaS Security feeds configured for email applications (e.g., Gmail). Both fields log the subtype (e.g., Financial Statements: Income Statements (Profit and Loss Statements)) of uploaded or downloaded documents.

To learn more, see NSS Feed Output Format: Endpoint DLP Logs &#8203;&#8203;&#8203;&#8203;&#8203;&#8203;and NSS Feed Output Format: SaaS Security Logs .

#### Enhancement to Gen AI Prompt Configuration
The generative AI prompt configuration is extended to the Grammarly application . As part of this change, the Grammarly option is added to the Policy > URL & Cloud App Control > Advanced Policy Settings page.

 See image. 

To learn more, see Configuring Advanced Policy Settings .

# Added Grammarly Capability to URL & Cloud App Control Policy Settings Endpoint

A new Boolean field, enableGrammarlyPrompt , is available for the AdvancedUrlFilteringCloudAppOptions model in the /advancedUrlFilterAndCloudAppSettings APIs. This field allows users to use generative AI prompts with Grammarly.

To learn more, go to AdvancedUrlFilteringCloudAppOptions from URL & Cloud App Control Policy Settings .

#### Expanded SSPM Controls for Microsoft Copilot
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Microsoft Copilot with 15 new SSPM controls, providing deeper visibility and stronger security posture assessment.

#### HTTP Feed Support for NSS
The Nanolog Streaming Service (NSS) supports streaming encrypted and load-balanced NSS feeds over an HTTP connection between the NSS and your SIEM. The HTTP NSS feed uses the HTTP API to stream logs from the Zscaler nanolog cluster to your SIEM. You can configure up to 8 HTTP NSS feeds for each log type in the Zscaler Admin Console.

Also, a new action to copy your NSS feeds is added.

 See image. 

To learn more, see Understanding Nanolog Streaming Service (NSS) , About NSS Feeds , and Adding HTTP NSS Feeds .

#### Support for Microsoft Copilot Readiness Assessment
Organizations face a significant security risk when users inadvertently overshare or mishandle sensitive internal files. The integration of AI tools, such as Microsoft Copilot, intensifies this risk, as these tools can access information within the improperly shared files, leading to the potential exposure of sensitive data to unauthorized parties. Therefore, implementing proactive monitoring and control measures is crucial to safeguard organizational security and prevent accidental data leaks.

As part of this feature, the following enhancements are available in the Zscaler Admin Console:

# SaaS Workflows: Microsoft Copilot Readiness Assessment

SaaS Workflows is introduced to streamline data protection and compliance, which is designed to automate processes and enable bulk remediation actions. A significant current capability within these workflows is the new Microsoft Copilot Readiness Assessment page. This is crucial in helping organizations mitigate risks and guarantee a secure and prepared onboarding experience for Microsoft applications.

You can access the dashboard from Analytics > Internet & SaaS > Analytics > SaaS Workflows > Microsoft Copilot Readiness Assessment.

 See image. 

To learn more, see About SaaS Workflows , About Microsoft Copilot Readiness Assessment , and Viewing Drill Down of All Assets .

# SaaS Security Insights Logs and SaaS Security Assets Logs

Filters and columns, Accessibility Flags and Label, are added to the SaaS Security Insights Logs page and SaaS Security Assets with Incidents page (Analytics > Internet & SaaS > Analytics > SaaS Security > Assets) for collaboration applications, email applications, and file sharing applications.

 See image. 

To learn more, see About SaaS Security Insights Logs and Understanding the Assets Report: Assets with Incidents .

# NSS Feeds

You can add the following fields for the Microsoft Copilot Readiness Assessment when configuring SaaS Security NSS or Cloud NSS Feed Output Format. These fields apply to collaboration, email, and file applications:
 
- %s{labelname}
- %s{accessibility_flags}
- %s{copilot_accessible} 
To learn more, see NSS Feed Output Format: SaaS Security Logs .


### March 11, 2026

#### Support for Workday Tenant RaaS-based API Access
Workday tenants now support RaaS-based API access which enables secure, programmatic retrieval of data and management through web services. Existing Workday tenants need to be reauthenticated by editing the tenant and revalidating.

To learn more, see Adding SaaS Application Tenants and About SaaS Application Tenants .

#### Support in SaaS Security Data at Rest DLP Policy for Quarantine of Sensitive Content in Microsoft Teams
The SaaS Security Data at Rest Scanning policy supports a new option to quarantine sensitive content in Microsoft Teams. You can specify a tombstone message that end users see when messages or files in Microsoft Teams are quarantined.

 See image. 

After a message or file has been quarantined in Microsoft Teams, admins can use the SaaS Assets Report to review and remove the quarantined content.

 See image. 

To learn more, see Configuring the SaaS Security API DLP Policy , About Quarantine Tombstone File Templates , and SaaS Assets Report: Assets with Incidents .

#### Cloud Custom IPS Enhancements
Custom IPS is supported on Zscaler's public cloud, allowing you to create and deploy custom IPS signature rules without requiring any additional infrastructure (previously required a Private Service Edge deployment). You can inspect traffic transiting the Zscaler cloud against your custom signatures, irrespective of whether it is forwarded to a Public, Private, or Virtual Service Edge.

To enable Custom IPS with your Advanced Firewall subscription, contact your Zscaler Account team.

With this upgrade, the following enhancements are also made to Custom IPS:
 
- Applicable to decrypted web traffic (decrypted via SSL Inspection) in addition to non-web traffic.
- Extended support for HTTP protocol-aware signatures, so signature rules can include HTTP-specific options.
- Signature rule validation occurs in two stages before deployment: static validation (currently supported) that checks rules for syntax errors, duplication, and based on other predefined conditions; dynamic validation (newly added) that runs signatures against designated packet captures to ensure efficient resource usage and optimal performance. The signature is enabled after both validations are completed. These transitions are indicated by new statuses.

View the newly added actions to initiate dynamic validation of signature rules.
- Logs showing custom signature matches for better visibility and easier troubleshooting.
- Increased the custom signature rule limit to 1,000 (previously 500). 
To learn more, see About Custom IPS Signature Rules , Configuring Custom IPS Signature Rules , and Specifications & Limitations for Custom IPS Signature Rules .
 
- In the Add Signature Rule (and Edit Signature Rule) window, a Save & Promote button is added to trigger dynamic validation of the rule.

Save image.

The Enable Signature Rule toggle button is not accessible until the rule moves to the Enable Ready state with the successful completion of dynamic validation. There is no change to the existing Save option, which continues to save the rule after successful static validation.
- On the Custom Signature Rules page, a Promote All button is added to initiate dynamic validation of all rules at once.

See image.


### March 06, 2026

#### Advanced SaaS Security Posture Management Support for Oracle Financials Cloud
You can configure Advanced SaaS Security Posture Management (SSPM) for Oracle Financials Cloud tenants. Select the SSPM Scan checkbox when onboarding a tenant to enable the Advanced SSPM scan capability for the specific tenant.

 See image. 

The SSPM Scan checkbox is enabled only when you have Advanced SSPM enabled for your tenant.

To learn more, see What Is Advanced Posture Management? and Adding SaaS Application Tenants .

#### Application Investigation in Endpoint Data Scan
Zscaler's Application Investigation is a solution that provides comprehensive visibility and automated risk management for an organization's application ecosystem by delivering a clear view of all software in use, including unauthorized AI tools and unapproved browsers. By automatically identifying vulnerable or suspicious applications, Application Investigation enables administrators to prioritize security efforts and focus on the highest-threat categories and vulnerabilities across the organization.

The Application Investigation page (Analytics > Endpoint Data Scan > Application Investigation) provides insights into executable files and applications stored on endpoints, gathering data on installed software, running processes, and libraries. This is crucial not only for compliance, but also for monitoring, auditing, and identifying vulnerabilities or unauthorized software.

As part of this change, the Inventory > Applications tab is now moved to Application Investigation > Inventory tab.

 See image. 

To learn more, see About the Application Investigation Overview , About the Application Investigation Inventory , Analyzing Applications Details , and Accessing and Navigating the Endpoint Data Scan Report .

#### DLP Operational in Endpoint Data Scan
The Zscaler DLP Operational page (Analytics > Endpoint Data Scan > DLP Operational) provides insights into the endpoint's status, thereby ensuring that the system functions properly and as designed to avoid sensitive data leakage.

 See image. 

To learn more, see About DLP Operational Dashboard .

#### Filtering by User Group in Endpoint Data Scan
Administrators can filter data on the Endpoint Data Scan page (Analytics > Endpoint Data Scan > Endpoint Data Scan) by a specific user group.

 See image. 

To learn more, see About Endpoint Data Scan .

#### New Bandwidth Control Fields for Transactions
Web Insights are enhanced to allow users to view the latency caused by bandwidth control on transactions in the ZIA Admin Portal.

# Web Insights Logs

The following new columns and filters are available in the Web Insights Logs:
 
- Request Latency Due to Bandwidth Control (ms)
- Response Latency Due to Bandwidth Control (ms)
- Total Latency Due to Bandwidth Control (ms) 
 See image. 

To learn more, see Web Insights Logs: Columns and Web Insights Logs: Filters .

# NSS Feeds

The fields %d{txn_delay_req} and %d{txn_delay_resp} can be added to the Feed Output Format when configuring an NSS or Cloud NSS feed for web logs. These fields display the bandwidth transaction request delay and the bandwidth transaction response delay in milliseconds, respectively.

To learn more, see NSS Feed Output Format: Web Logs .

#### Share Files Externally in Endpoint Data Scan
Share Files Externally provides a capability for Endpoint DLP that allows authorized users to securely share sensitive files with external partners by encrypting the data into a secure HTML format, ensuring that only verified recipients can access the content.

You can access the Share Files Externally page from Analytics > Endpoint Data Scan > Sensitive Information.

 See image. 

To learn more, see About Endpoint Data Scan Sensitive Information: Share Files Externally , Configuring Share File Externally Settings , and Understanding Share Files Externally .

#### Support for CIDR and Regex on Network Share DLP Resources
The Zscaler service supports using Classless Inter-Domain Routing (CIDR) ranges and regular expressions for advanced matching when creating or editing network shares for Endpoint Data Loss Prevention (DLP) resources. The following image shows a regular expression that matches all network servers that start with "srv" and the match is case insensitive:

 See Image. 

To learn more, see Adding DLP Resources and Editing DLP Resources .

#### Support for Network Type on Endpoint DLP Policy Rules
The Zscaler service supports specifying a network type (e.g., Trusted, Off-Trusted, VPN) for the Network Share, Printing, and Device Control channels when creating policy rules for Endpoint Data Loss Prevention (DLP).
 
- Endpoints must be running Zscaler Client Connector version 4.8.600 or later (Windows) or version 4.7.1 or later (macOS) for policy rules to enforce the network type.
- To enable this feature, contact your Zscaler Account team. 
 See Image. 

To learn more, see Configuring Endpoint DLP Policy Rules and About Trusted Networks .

#### Exact Data Matching in Endpoint Data Scan
Zscaler has introduced Exact Data Matching (EDM) for Endpoint Data Loss Prevention (DLP) which provides protection for structured sensitive data. This feature utilizes a unique hybrid architecture where the endpoint performs local prefiltering to identify candidate files for cloud inspection, ensuring maximum accuracy without compromising device performance or bandwidth.

You can access Exact Data Matching (EDM) page from Analytics > Endpoint Data Scan > Sensitive Information.

To enable this feature, contact your Zscaler Account team.

 See image. 

To learn more, see Understanding Exact Data Matching (EDM) and About Endpoint Data Scan Sensitive Information: Exact Data Matching .


### February 27, 2026

#### Enhancement to Firewall Policies Endpoints
A new query parameter, ruleLabelId , is available for the GET /firewallFilteringRules and GET /firewallFilteringRules/count endpoints. The ruleLabelId query parameter allows you to filter Firewall Filtering rules based on the rule label ID. To learn more, go to GET /firewallFilteringRules and GET /firewallFilteringRules/count from Firewall Policies .

To learn more about each endpoint, see the API Reference and API Rate Limit Summary .

#### Enhancements to Admin Role Management
On the Internet & SaaS > Role Management page, in the Policy & Components > Access Control tab, the URL Filtering and Cloud App Control policy permissions are separated to provide admins more granular control over those features.

 See image. 

To learn more, see Adding Admin Roles .

#### Expanded SSPM Controls for Salesforce
Advanced SaaS Security Posture Management (SSPM) expands its coverage for Salesforce with three new SSPM controls, providing deeper visibility and stronger security posture assessment.

#### SSL Inspection and SSL Policy Renamed to SSL/TLS Inspection and SSL/TLS Policy
The labels SSL Inspection and SSL policy are renamed to SSL/TLS Inspection and SSL/TLS policy.

 See image. 
 
Refer to the following table for a list of updated labels:
 Old UI Labels New UI Labels SSL Inspection (Policy > SSL Inspection) SSL/TLS Inspection (Policy > SSL/TLS Inspection) SSL Inspection Policy (Policy > SSL Inspection > SSL Inspection Policy) SSL/TLS Inspection Policy (Policy > SSL/TLS Inspection > SSL/TLS Inspection Policy) Configure SSL Inspection Policy (Policy > SSL Inspection > Configure SSL Inspection Policy) Configure SSL/TLS Inspection Policy (Policy > SSL/TLS Inspection > Configure SSL/TLS Inspection Policy) Add SSL Inspection Rule (Policy > SSL Inspection > Add SSL Inspection Rule) Add SSL/TLS Inspection Rule (Policy > SSL/TLS Inspection > Add SSL/TLS Inspection Rule) Edit SSL Inspection Rule (Policy > SSL Inspection > Edit SSL Inspection Rule) Edit SSL/TLS Inspection Rule (Policy > SSL/TLS Inspection > Edit SSL/TLS Inspection Rule)

#### Support for Certificate-based Authentication with Microsoft Applications for a Custom Zscaler Connector
When you create a custom Zscaler connector for a Microsoft application, you have the option to choose whether you want to provide a client secret or a private key in the Zscaler Admin Console so that the Zscaler service can access the application. SharePoint, Copilot, and Microsoft 365 require a private key for onboarding, but all other supported Microsoft applications support both options.

 See image. 

To learn more, see Adding SaaS Application Tenants and Authorizing a Custom Zscaler Connector for Microsoft Applications .

#### Updates to Recipient Email Profile Endpoints
You can create, update, and delete recipient email profiles, retrieve a list of all recipient email profiles, and obtain the count of recipient email profiles for an organization using the following endpoints:
 
- GET /emailRecipientProfile
- POST /emailRecipientProfile
- GET /emailRecipientProfile/{profileId}
- PUT /emailRecipientProfile/{profileId}
- DELETE /emailRecipientProfile/{profileId}
- GET /emailRecipientProfile/count 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### February 23, 2026

#### Updates to Firewall Policies Endpoints
You can create, update, and delete DNS application groups, and retrieve a list of all DNS application groups using the following endpoints:
 
- GET /dnsApplicationGroups
- POST /dnsApplicationGroups
- GET /dnsApplicationGroups/{groupId}
- PUT /dnsApplicationGroups/{groupId}
- DELETE /dnsApplicationGroups/{groupId}
- GET /dnsApplicationGroups/lite 
To learn more about each endpoint, see the API Reference and API Rate Limit Summary .


### February 17, 2026

#### Introducing Flexible Permission Selection for SSPM Connectors
The SaaS application tenants GitHub, Jira, Okta, Confluence, Trello, Webex Teams, and Google Workspace now have the option to onboard for SaaS Security Posture Management (SSPM) scan by choosing Read-only or Read/Write (full access) for the connector role. The Read/Write connector role is the default option.

This enhancement removes the friction caused by shared DLP and SSPM connectors that previously required elevated permissions for posture-only use cases. Administrators can onboard applications with minimal, least-privilege access for SSPM posture assessments and later upgrade to full permissions only if they choose to enable DLP content scanning or posture remediation. This provides a more secure, flexible, and customer-friendly onboarding experience.

 See image. 

To learn more, see Adding SaaS Application Tenants and Permissions for Onboarding SaaS Apps for SSPM .


### February 16, 2026

#### Enhancements to Endpoint DLP for macOS
The following enhancements are available in Zscaler Endpoint Data Loss Prevention (DLP) for macOS:
 
# Support for Endpoint DLP Block Action for Printing on macOS

The Zscaler service supports the Block action for printing from macOS devices in Endpoint DLP rules with content inspection.

 See Image. 

To learn more, see Configuring Endpoint DLP Policy Rules .

# Endpoint DLP Support for Clipboard and Application File Access

To access this feature, contact your Zscaler Account team.

Endpoint DLP supports monitoring and blocking sensitive information when specific applications access files, as well as when content is pasted into those applications.

To get started, configure the relevant applications to prevent sensitive data loss on the DLP Resources page (Policies > Data Protection > Policy > Endpoint Controls > Endpoint DLP Resources):

 See Image. 

After applications are defined, you can create Endpoint DLP policy rules that:
 
- Protect file access: Use Application File Access as the channel to detect and block sensitive data exposed when applications read files.
- Protect clipboard activity: Use Clipboard as the channel to detect and block sensitive data pasted into applications. 
 See Image. 

To learn more, see About DLP Resources , Adding DLP Resources and Configuring Endpoint DLP Policy Rules .

# Removable Storage Rule: Device Per User Pair

Streamline management of the Device Control Removable Storage rules by defining multiple removable storage devices and mapping them to specific users or endpoints within a single rule. This rule also supports CSV file import for bulk operations.

 See Image. 

To learn more, see Managing a Removable Storage Rule .

# Endpoint Data Scan: End User Report

This feature introduces configurable reports to increase transparency for end users. These reports aim at providing users with best practices and show them where sensitive data is stored locally on their endpoints. This feature aims at making endpoint data scanning more efficient, transparent, and collaborative, improving how administrators and end users work together to manage sensitive data.

To learn more, see Understanding End User Reports , About Endpoint Data Scan , and Analyzing Endpoint DLP Scan for a User .

# Endpoint DLP Configurations

This feature introduces the following expanded configuration options across Endpoint Data Scan, Classification, and DLP inspection to improve performance, control, and flexibility:
 
- Endpoint Data ScanGranular controls for End User report visibility, scheduling, sensitive data exposure, and custom messages.
- Ability to exclude specific file systems, folders, and entities. 
- Classification SettingsConfigurable maximum file size and timeout strategies with Allow or Block fallback actions. 
- Other EnhancementsOption to hide the Protect action for end users.
- Controls for Application Inventory Scan. 
 See image. 

To learn more, see Configuring Endpoint Data Scan and Endpoint Settings and Activating Device Control Policy Rules and Configuration Changes .

# Sensitive Information Index Document Match

To access this feature, contact your Zscaler Account team.

This new capability allows for the detection of data exfiltration on Endpoint DLP channels by matching full or partial content against indexed documents. A secure, endpoint-based workflow has been introduced in this release, enabling authorized users to index sensitive documents directly from their endpoints using the Endpoint DLP context menu. The Endpoint Index Document Match (IDM) operates in parallel to the Inline DLP IDM. Enforcement and detection are independent and require reindexing of IDM files using the Endpoint DLP. This feature is currently in limited availability. You can access the Sensitive Information page from Analytics > Data Security > Endpoint.

 See image. 

To learn more, see About Sensitive Information and Configuring Sensitive Information Settings .

# Additional Support for Predefined DLP Dictionaries in Endpoint DLP

The following predefined DLP dictionaries are supported for use in Endpoint DLP policy rules:
 
- CNPJ Number (Brazil)
- International Bank Account Number (IBAN)
- National Economic Registry Number (Poland)
- Passport Number (Asia) 
To learn more, see Understanding Predefined DLP Dictionaries .

# Added Context for Endpoint DLP Triggers

You can see an additional 15-byte prefix and suffix to the left and right of the Endpoint DLP trigger that provides more information about the Endpoint DLP incident. The additional context can be seen in the Incident Receiver, Zscaler Workflow Automation, and Email Notifications.

The following image shows an example of trigger context in Zscaler Workflow Automation:

 See image. 

To learn more, see Configuring DLP Notification Templates , Configuring the Zscaler Incident Receiver for On-Premises VMs , Configuring the Zscaler Incident Receiver for Amazon Web Services EC2 VMs , and Configuring the Zscaler Incident Receiver for Azure VMs .

# Endpoint DLP Support for Proximity Length in Predefined Dictionaries

The Zscaler service supports the Proximity Length field on applicable predefined DLP dictionaries when used in engines associated with Endpoint DLP rules. The proximity length defines how close a high confidence phrase must be to an instance of the pattern (that the dictionary detects) to count as a match. For certain predefined DLP dictionaries, the Proximity Length field appears when the dictionary's Confidence Score Threshold is High.

 See Image. 

To learn more, see Understanding Predefined DLP Dictionaries .


### February 12, 2026

#### Security Fixes
Proper neutralization of user input in specific input fields in the ZIA Admin Portal no longer allows an authenticated administrator to access unauthorized internal information in rare conditions (CVE-2026-22568).


### February 06, 2026

#### Advanced SaaS Security Posture Management Support for JumpCloud
You can configure Advanced SaaS Security Posture Management (SSPM) for JumpCloud tenants. Select the SSPM Scan checkbox when onboarding a JumpCloud tenant to enable the Advanced SSPM scan capability for the specific tenant.

 See image. 

The SSPM Scan checkbox is enabled only when you have Advanced SSPM enabled for your tenant.

To learn more, see What Is Advanced Posture Management? and Adding SaaS Application Tenants .

#### Insights Logs Improvements & Enhancements
The Insights Logs pages now feature asynchronous log retrieval. This enhancement allows users to continue working without interruption while queries are executed in the background, significantly improving their user experience.

The following enhancements are available for Insights Logs in the ZIA Admin Portal:
 
- You can initiate log queries or move active searches to the background with Export in Background option, so you can continue other administrative tasks without interruption. The query is not terminated while running in the background, and a progress bar is displayed. During this process, you can choose to keep the query active, move it to the background, or stop the execution entirely.
- The Apply Filters button is renamed to Run Query to better reflect the action.
- You can export up to 1 million records to a CSV file and view up to 25,000 records directly in the portal.
- You can specify a custom name for the downloaded CSV file for better organization.
- Each admin can only run one asynchronous query at a time.
- Only the user who initiated the query can view the results on-screen or access the downloaded file. 
 See image. 

To learn more, see About Insights Logs .


### February 02, 2026

#### Advanced SSPM Support for Airtable
Advanced SSPM supports a new platform, Airtable. You can onboard an Airtable tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with Airtable and Connecting Your Platforms to Advanced SSPM .

#### Advanced SSPM Support for Bitwarden
Advanced SSPM supports a new platform, Bitwarden. You can onboard a Bitwarden tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with Bitwarden and Connecting Your Platforms to Advanced SSPM .

#### Advanced SSPM Support for Sentry
Advanced SSPM supports a new platform, Sentry. You can onboard a Sentry tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with Sentry and Connecting Your Platforms to Advanced SSPM .

#### New Cloud Applications
New cloud applications are added to the cloud application categories. You can download the list of newly added cloud applications to the respective categories: Download 

The risk index and risk attribute values for these new applications are visible only after they are available on all the clouds.

#### Support for OneLogin as an API-Based Platform in Advanced SSPM
Advanced SSPM supports OneLogin as an API-based platform. You can onboard a OneLogin tenant from the 3rd-Party App Governance Admin Portal.

 See image. 

To learn more, see Integrating with OneLogin and Connecting Your Platforms to Advanced SSPM .


### January 21, 2026

#### Logs for MCP Transactions
The application activity MCP is added to the Web Insights Logs to log Model Context Protocol (MCP) transactions in the ZIA Admin Portal.

 See image. 

To learn more, see Web Insights Logs: Filters .


### January 15, 2026

#### Expanded File Type Support for Sandbox
The Zscaler Sandbox now supports the Optical Disc Image (iso) file type.

 See image. 

To learn more, see About Sandbox and Configuring the Sandbox Policy .


### January 13, 2026

#### DLP and File Type Support for MSIX Files
The File Type Control and Data Loss Prevention (DLP) policies now support MSIX files in the Executable category.
 
- File Type Control
- DLP - Rule without Content Matching 
To learn more, see About File Type Control and About Data Loss Prevention .

#### Sandbox Verdict Logging
Zscaler supports comprehensive logging of Sandbox analysis activities through Insights Logs and the Nanolog Streaming Service (NSS). You can log and view details of all files that went through behavioral analysis regardless of the verdict (e.g., Suspicious Content, Benign). With the following enhancements in the ZIA Admin Portal, you can find the relevant details quickly in order to triage and address the event appropriately:
 
# Sandbox Verdict Insights Logs

With the new Sandbox Verdict Insights page (Analytics > Sandbox Verdict Insights), you can view recent sandbox analysis activity logs.

 See image. 

To learn more, see About Insights , About Insights Logs , Sandbox Verdict Insights Logs: Filters , and Sandbox Verdict Insights Logs: Columns .

# NSS Feeds

A new log type, Sandbox Verdict, is available for NSS. You can configure an NSS feed or Cloud NSS feed to stream Sandbox analysis data from Zscaler to your security information and event management (SIEM) system.

 See image. 

To learn more, see Adding NSS Feeds for Sandbox Verdict Logs , Adding Cloud NSS Feeds for Sandbox Verdict Logs , and NSS Feed Output Format: Sandbox Verdict Logs .

#### Enhancement to Extranet Application Support
Extranet Application Support can be configured bidirectionally, allowing partners to access your organization's resources securely.

Extranet Application Support is a feature in limited availability. To access Extranet Application Support, contact your Zscaler Account team.

As part of this enhancement:
 
- Custom IP pools can be configured for Extranet Application Support.

See image.
- Static IP addresses, GRE tunnels, and sublocations are configurable for extranet locations.
- Firewall Control is automatically enabled for extranet locations.
- IPS Control is available for extranet locations.
- Three default policy rules are added to the Forwarding Control policy when Extranet Application Support is enabled.

See image.
- One predefined policy rule is added to the DNS Control policy when Extranet Application Support is enabled.

See image. 
To learn more, see Understanding Extranet Application Support .

# Insights Logs

A filter and column, Extranet Resource, is added to DNS Insights Logs, Firewall Insights Logs, and Web Insights Logs.

 See image. 

To learn more, see DNS Insights Logs: Columns , DNS Insights Logs: Filters , Firewall Insights Logs: Columns , Firewall Insights Logs: Filters , Web Insights Logs: Columns , and Web Insights Logs: Filters . 

# NSS Logs
 
- The field %s{extranet_name} is available when adding an NSS feed or Cloud NSS feed for Web, Firewall, and DNS logs.

To learn more, see NSS Feed Output Format: Web Logs, NSS Feed Output Format: Firewall Logs, and NSS Feed Output Format: DNS Logs.
- For NSS or Cloud NSS feed Tunnel logs, when configuring the Tunnel Type filter, you can select EAS Client Tunnel to limit the logs based on this tunnel type.

See image.

To learn more, see Adding NSS Feeds for Tunnel Logs and Adding Cloud NSS Feeds for Tunnel Logs.


### January 12, 2026

#### Authentication Service Integration for Management Portal for Partners & Other Enhancements
The Zscaler service supports Authentication Service Single Sign-On (SSO) for partner logins to the Zscaler Management Portal for Partners. Following the migration, all partner logins route through the Authentication Service SSO framework, offering a secure and unified authentication experience.
 
For partners migrated to Authentication Service, the following features move under Authentication Service:
 
- Role and Scope Assignments: To assign a role or scope to admins, go to Authentication Service Admin Portal > Administration > Entitlements.
- Password Resets: To reset a password, go to Authentication Service Admin Portal > Administration. 
 See image. 

Further, we are also introducing a new way to manage tenants and admins: scopes. Scopes are multi-tenant, multi-cloud setups that you can assign to one or more admins, as required.

To learn more, see About Scopes , Adding a New Scope , and Assigning Entitlements to Users and User Groups .


### January 09, 2026

#### Enhanced Flexibility in the URL Filtering Policy Rule Creation
You can apply either OR or AND logical operator between the Users, Groups, and Departments criteria in the URL Filtering Policy rules. This allows you to create granular policy rules using a combination of logical operators (i.e., OR or AND ) between these criteria. As part of this update, up and down arrows are added to the logical operators between these criteria in the Add/Edit URL Filtering Rule window.

To enable this feature, contact Zscaler Support.

You can also add up to three Groups fields by clicking the Add icon next to the Groups field, and they are connected with a logical AND operator. This allows you to create rules that are triggered when they match the selected groups in all the Groups fields.

 See image. 

To learn more, see Configuring the URL Filtering Policy .

# Enhancement to URL Filtering Policy Endpoints

New fields, usersAndGroupsSet , groupsAndDepartmentsSet , groups2 , and groups3 are available for the UrlFilteringRule model in the /urlFilteringRules APIs.

To learn more, go to the UrlFilteringRule model from URL Filtering Policy .

#### Enhancement to Zscaler Cloud Performance Test Tool
The Zscaler Cloud Performance Test Tool allows you to view only the domain part of the traffic or email, and the user name is hidden. For example, johndoe@zscaler.com is visible as xxxxxxx@zscaler.com.

 See image. 

To learn more, see Using the Zscaler Cloud Performance Test Tool .

#### Increased AWS Account IDs in Tenant Profiles
You can add up to 512 account IDs per tenant profile for AWS and there can be a maximum of 4,096 account IDs across all profiles.

To learn more, see Adding Tenant Profiles and Ranges & Limitations .

#### NSS Support for Hyper-V
Zscaler's Nanolog Streaming Service (NSS) supports the configuration and deployment of an NSS virtual machine (VM) on Hyper-V.

After deploying an NSS VM, you can stream your organization's web or firewall logs from the Zscaler cloud to your security information and event management (SIEM) system.

 See image. 

To learn more, see NSS Deployment Guide for Hyper-V .

#### NSS Support for Nutanix
Zscaler's Nanolog Streaming Service (NSS) supports the configuration and deployment of an NSS virtual machine (VM) on Nutanix.

After deploying an NSS VM, you can stream your organization's Web or Firewall logs from the Zscaler cloud to your security information and event management system.

 See image. 

To learn more, see NSS Deployment Guide for Nutanix .

#### Update to Admin Audit Logs and Event Logs API Endpoints
When you request report generation using POST /auditlogEntryReport or POST /eventlogEntryReport , it returns an HTTP 200 OK status code with the statusId in the response (previously returned 204 status code). This statusId must be captured and sent as a query parameter in the following requests that are subsequently made to check the report status, download the report, or cancel the report request:
 
- GET /auditlogEntryReport
- GET /auditlogEntryReport/download
- DELETE /auditlogEntryReport
- GET /eventlogEntryReport
- GET /eventlogEntryReport/download
- DELETE /eventlogEntryReport 
This API workflow change requires you to update your existing scripts immediately to ensure that your automated integrations for downloading audit and event logs continue to function correctly. Modify your scripts to parse the statusId from the initial report generation response and ensure that your API requests to check status, download, or cancel are updated to pass the statusId parameter.

To learn more, see the API Reference and Downloading Audit Logs and Event Logs Using API .


### January 07, 2026

#### Enhancements to 3rd-Party App Governance and Advanced SSPM
The following enhancements are available in 3rd-Party App Governance and Advanced SSPM:

## Settings

The SaaS Tenants and Notifications tabs are added to the Settings page. These tabs allow you to view and manage the onboarded SaaS tenants and also configure Slack and email notifications.

 See image. 

To learn more, see About Settings in 3rd-Party App Governance .

## Connect Drop-Down Menu

A drop-down menu is added under the Connect button on the App Dashboard. From this drop-down menu, you can select the platform you want to connect to 3rd-Party App Governance or Advanced SSPM.

 See image. 

 To learn more, see Connecting Your Platforms to 3rd-Party App Governance and Connecting Your Platforms to Advanced SSPM .

#### Sandboxing Password-Protected PDF Files for Isolation
Zscaler Isolation now supports password-protected PDF files to be sandboxed for Zscaler Internet Access (ZIA) . If ZIA Sandbox determines that the file is safe, users can download the original PDF. If ZIA Sandbox determines that the file is malicious, users cannot download the original PDF to their local device, and Zscaler stores the password for the duration of the isolated session. If the PDF can be rendered within the isolated browser, users can download the sanitized version of the PDF.

After the PDF is downloaded into the Isolation container, it opens on the user's device automatically, and they are prompted for the file password. Users are allowed unlimited incorrect password attempts.

To learn more, see About Sandbox Integration with Isolation and Transferring and Viewing Files in Isolation .
