# ZDX リリースノート

> 最終更新: 2026-07-15 23:29 UTC  
> ソース: https://help.zscaler.com/zdx/release-notes

---

# ZDX Release Notes Index


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


# ZDX 2026 Release Upgrade Summary

This article provides a summary of all new features and enhancements per Zscaler cloud for Zscaler Digital Experience (ZDX). Zscaler will email a notification to your organization's registered support contacts approximately one week before your cloud is upgraded. To see scheduled maintenance updates for your cloud, visit the [Trust Portal](https://trust.zscaler.com).

## June 29, 2026

### Feature Available

#### OS Selection for Probing Criteria
Configure a probe for selected OSs in the Probing Criteria.

[See image.](#img_OS_criteria)

OS selection is supported for end user probe configurations and end user collection configurations.

To learn more, see [Configuring a Probe](/zdx/configuring-probe), [Managing Collections](/zdx/managing-collections), and [Understanding Probing Criteria Logic](/zdx/understanding-probing-criteria-logic).

![During a probe configuration, select OSs to receive monitoring metrics for end users](/sites/default/files/downloads/zdx/configuration/probes/configuring-probe/zdx-release_note-configuration-probe-OS.png "Configure Web Probe - Select OSs")

![OS Selection](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-probe-configuration-os-selection.png "OS Selection")

## June 18, 2026

### Feature Available

#### Rerun Job
Rerun the job for selected devices and schedule the job at a better time period when the devices are available. You can rerun the job from the Job Details page or from the Device Remediation page.

[See image.](#rerun)

To learn more, see [Viewing and Managing Device Remediation](/zdx/viewing-and-managing-device-remediation).

![Job Details Page - Rerun Job](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-remediation-rerun_0.png "Job Details Page - Rerun Job")![Device Remediation Page - Rerun Job](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-remediation-rerun-device-remediation.png "Device Remediation Page - Rerun Job")

## June 16, 2026

### Feature Available

#### Browser Extension Version 0.1.36 of Real User Monitoring
Zscaler released Browser Extension version 0.1.36 of Real User Monitoring (RUM), which includes:

* Enhances and extends log limitations.
* Fixes an issue where the geolocation is incorrect.

To update to the latest version, refer to:

* [Chrome Web Store - Zscaler Real User Monitoring (RUM)](https://chromewebstore.google.com/detail/zscaler-real-user-monitor/eojpolfgdcogokpbcgejpgeblcjellak?utm_source=item-share-cb)
* [Microsoft Edge Add-ons - Zscaler Real Time User Monitoring](https://microsoftedge.microsoft.com/addons/detail/realtimeusermonitoring/dggndchpbpgadddajngjekkkegacfaea)

## June 12, 2026

### Feature Available

#### Location of Stored ZDX Data 
ZDX logs and data are now stored in India in addition to the United States, the European Union (Western Europe, Netherlands), Canada, Australia East (New South Wales), or Singapore. Contact your Zscaler Account team for details.

To learn more about Zscaler's retention of logs and data, see [ZDX Logs](/customer-logs-fair-use/zdx-customer-logs-and-data).

## May 08, 2026

### Feature Available

#### Decline Button for Scripts
When you configure a script with an End-User Confirmation, you can opt to configure a Decline button for the end users.

[See image.](#img_decline)

Ensure the impacted devices, based on their OS, meet the minimum required or later [versions](/zdx/supported-versions-feature-compatibility) of ZDX Module and Zscaler Client Connector.

To learn more, see [Managing Scripts](/zdx/managing-scripts).

![Decline Button](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-remediation-decline.png "Decline Button")

### Feature Available

#### Managed Monitoring
Hosted Monitoring was renamed to Managed Monitoring for clarification and better representation.

[See image.](#img_managed_monitoring)

To learn more, see [Understanding Managed Monitoring](/zdx/understanding-managed-monitoring).

![Managed Monitoring](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-managed-monitoring.png "Managed Monitoring")

### Feature Available

#### Network Intelligence Dashboard Enhancements
The Network Intelligence dashboard has the following enhancements:

* Alternative views for User Experience & Network Insights: Configure your views to display the metrics for User Experience & Network Insights based on the top 5 ISPs with the highest number of probes.

  [See image.](#img_alternative)

  You can also view the historical comparison between different times or view geographical comparison between different locations.

  [See image.](#img_historical_geographical)
* ISP or ASN View: Display which pathways to view based on probe count. Use the Probe Count criteria to filter which pathways appear.

  [See image.](#img_ISP_ASN)
* High and Medium Severe Latency: Updated high and medium latency to better represent severities.

To learn more, see [Monitoring the Network Intelligence Dashboard](/zdx/monitoring-network-intelligence-dashboard).

![P50 Latency](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-releasenote-networkinsights-overview-compare-1.png "P50 Latency")

![Compare using the Historical or Geographical views](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-releasenote-networkinsights-overview-compare-2.png "Historical or Geographical Comparison Views")

![Use the probe count tool to display pathways](/sites/default/files/downloads/zdx/analytics/monitoring-network-intelligence-dashboard/zdx-releasenote-network-intelligence-isp-asn-default.png "ISP or ASN View - Probe Count")

## April 08, 2026

### Feature Available

#### ZDX in Zscaler Experience Center
Zscaler Experience Center simplifies Zero Trust adoption and operations through an intuitive, unified admin experience in the Zscaler Admin Console. Zscaler Digital Experience (ZDX) is available in the Experience Center and delivers a horizontal platform experience across multiple tenants.

[See image.](#zdx-xc-rn)

To learn more, see [What is Zscaler Experience Center](/unified/what-zscaler-experience-center) and [Upgrading to Zscaler Experience Center](/unified/upgrading-zscaler-experience-center).

![ZDX in Zscaler Experience Center](/sites/default/files/downloads/tech-pubs-drafts/release-notes-XC-zdx/zdx-experience-center-landing-view_0.jpg "ZDX in Zscaler Experience Center")

## March 06, 2026

### Feature Available

#### Real User Monitoring
Real User Monitoring captures and analyzes user interactions with applications through their web browsers to create a comprehensive visibility into the application's digital experience. You can use Real User Monitoring to identify bottlenecks a user might encounter while they are accessing configured applications through their web browsers.

[See image.](#RUM)

To learn more, see [Understanding Real User Monitoring](/zdx/understanding-real-user-monitoring) and [Evaluating Application Details](/zdx/evaluating-application-details).

![View application details with Real User Monitoring enabled](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/zdx-application-real-user-performance-release-note-1_0.png "View Real-User Performance with Real User Monitoring")

## February 27, 2026

## February 20, 2026

### Feature Available

#### User Location Report
The system-generated report for User Location is available in the ZDX Admin Portal.

[See image.](#userlocationreport)

To learn more, see [Viewing System-Generated Reports](/zdx/viewing-system-generated-reports).

![View the User Location Report to understand where your users are located](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/ZDX-System-Generated-Reports-user-location-report-1.png "User Location Report")

## February 06, 2026

### Feature Available

#### Session Timeout Duration
Configure the Session Timeout Duration to determine how long a user can access the ZDX Admin Portal in a session while being inactive.

[See image.](#timeout)

To learn more, see [Configuring Administrator Management Settings](/zdx/configuring-administrator-management-settings).

![Configure the Session Timeout Duration](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/ZDX-AdministratorManagement-releasenote.png "ZDX Portal Session Timeout")

### Feature Available

#### Zoom Call Quality Monitoring Exclusion Criteria
Call Quality Monitoring for Zoom now supports exclusion criteria during tenant onboarding, allowing the collection of call quality data for all users except specified users or groups.

New fields in the Monitoring Criteria section:

* **User groups**: Select one or more groups to exclude from monitoring.
* **Users**: Add individual users to exclude.
* **Departments**: Exclude entire departments to streamline administration.

These options make it easy to apply broad monitoring while exempting specific users or teams as needed.

[See image.](#zoomexclusionquality1826)

To learn more, see [Configuring Zoom Call Quality for Digital Experience Monitoring](/unified/configuring-zoom-call-quality-zdx).

![Add Tenant - Review Tenant window displaying Exclusion Criteria options](/sites/default/files/downloads/tech-pubs-drafts/zdx-draft-articles/Zoom%20Call%20Quality%20Monitoring%20Exclusion%20Criteria/placeholderforzoomcallqualityexclusion1826.png "Call Quality Monitoring Add Tenant Window")

## January 16, 2026

### Feature Available

#### Location of Stored ZDX Data
ZDX logs and data are now stored in Canada in addition to the United States, the European Union (Western Europe, Netherlands), Singapore or Australia East (New South Wales). Contact your Zscaler Account team for details.

To learn more about Zscaler's retention of logs and data, see [ZDX Logs](/customer-logs-fair-use/zdx-customer-logs-and-data).

### Feature Available

#### Support for IPv6 in ZDX
ZDX now supports IPv6 to include dual-stack (IPv4 and IPv6) or IPv6-only configurations.

ZDX IPv6 visibility requires Zscaler Internet Access (ZIA) IPv6 to be enabled, as ZDX relies on ZIA to route and inspect IPv6 traffic for telemetry collection. To learn more, see [Understanding IPv6 Support](/zia/understanding-ipv6-support).

You can view IPv6 configurations across the ZDX Admin Portal (e.g., Cloud Path, Device Details).

[See image.](#cloud-path-device-details)

To learn more, see [Viewing IPv6 Configurations](/zdx/viewing-ipv6-configurations).

![Viewing IPv6 device details in ZDX Admin Portal ](/sites/default/files/downloads/zdx/release-notes/release-upgrade-summary-2026/ZDX-IPv6-User-Details_blur_releasenote_0.png "Cloud Path and Device Details Views")