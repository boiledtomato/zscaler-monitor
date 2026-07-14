# ZDX リリースノート

> 最終更新: 2026-07-14 23:20 UTC
> ソース: https://help.zscaler.com/zdx/release-notes

---

## Release Upgrade Summary (2026)

This article provides a summary of all new features and enhancements per Zscaler cloud for Zscaler Digital Experience (ZDX). Zscaler will email a notification to your organization's registered support contacts approximately one week before your cloud is upgraded. To see scheduled maintenance updates for your cloud, visit the Trust Portal .

### 関連記事（他年度）
- [Release Upgrade Summary (2026)](https://help.zscaler.com/zdx/release-upgrade-summary-2026)
- [Release Upgrade Summary (2025)](https://help.zscaler.com/zdx/release-upgrade-summary-2025)
- [Release Upgrade Summary (2024)](https://help.zscaler.com/zdx/release-upgrade-summary-2024)
- [Release Upgrade Summary (2023)](https://help.zscaler.com/zdx/release-upgrade-summary-2023)
- [Release Upgrade Summary (2022)](https://help.zscaler.com/zdx/release-upgrade-summary-2022)
- [Release Upgrade Summary (2021)](https://help.zscaler.com/zdx/release-upgrade-summary-2021)
- [Release Upgrade Summary (2020)](https://help.zscaler.com/zdx/release-upgrade-summary-2020)

## 2026年 リリースノート一覧

Zscalerクラウド: zdxcloud.net


### June 29, 2026

#### OS Selection for Probing Criteria
Configure a probe for selected OSs in the Probing Criteria.

 See image. 

OS selection is supported for end user probe configurations and end user collection configurations.

To learn more, see Configuring a Probe , Managing Collections , and Understanding Probing Criteria Logic .


### June 18, 2026

#### Rerun Job
Rerun the job for selected devices and schedule the job at a better time period when the devices are available. You can rerun the job from the Job Details page or from the Device Remediation page.

 See image. 

To learn more, see Viewing and Managing Device Remediation .


### June 16, 2026

#### Browser Extension Version 0.1.36 of Real User Monitoring
Zscaler released Browser Extension version 0.1.36 of Real User Monitoring (RUM), which includes:
 
- Enhances and extends log limitations.
- Fixes an issue where the geolocation is incorrect. 
To update to the latest version, refer to:
 
- Chrome Web Store - Zscaler Real User Monitoring (RUM)
- Microsoft Edge Add-ons - Zscaler Real Time User Monitoring


### June 12, 2026

#### Location of Stored ZDX Data 
ZDX logs and data are now stored in India in addition to the United States, the European Union (Western Europe, Netherlands), Canada, Australia East (New South Wales), or Singapore. Contact your Zscaler Account team for details.

To learn more about Zscaler's retention of logs and data, see ZDX Logs .


### May 08, 2026

#### Decline Button for Scripts
When you configure a script with an End-User Confirmation, you can opt to configure a Decline button for the end users.

 See image. 

Ensure the impacted devices, based on their OS, meet the minimum required or later versions of ZDX Module and Zscaler Client Connector.

To learn more, see Managing Scripts .

#### Managed Monitoring
Hosted Monitoring was renamed to Managed Monitoring for clarification and better representation.

 See image. 

To learn more, see Understanding Managed Monitoring .

#### Network Intelligence Dashboard Enhancements
The Network Intelligence dashboard has the following enhancements:
 
- Alternative views for User Experience & Network Insights: Configure your views to display the metrics for User Experience & Network Insights based on the top 5 ISPs with the highest number of probes.

See image.

You can also view the historical comparison between different times or view geographical comparison between different locations.

See image.
- ISP or ASN View: Display which pathways to view based on probe count. Use the Probe Count criteria to filter which pathways appear.

See image.
- High and Medium Severe Latency: Updated high and medium latency to better represent severities. 
To learn more, see Monitoring the Network Intelligence Dashboard .


### April 08, 2026

#### ZDX in Zscaler Experience Center
Zscaler Experience Center simplifies Zero Trust adoption and operations through an intuitive, unified admin experience in the Zscaler Admin Console. Zscaler Digital Experience (ZDX) is available in the Experience Center and delivers a horizontal platform experience across multiple tenants.

 See image. 

To learn more, see What is Zscaler Experience Center and Upgrading to Zscaler Experience Center .


### March 06, 2026

#### Real User Monitoring
Real User Monitoring captures and analyzes user interactions with applications through their web browsers to create a comprehensive visibility into the application's digital experience. You can use Real User Monitoring to identify bottlenecks a user might encounter while they are accessing configured applications through their web browsers.

 See image. 

To learn more, see Understanding Real User Monitoring and Evaluating Application Details .


### February 27, 2026

#### ZDX API Enhancements
The ZDX API includes the following endpoints:
 
- /snapshot/alert: Share a ZDX Snapshot for a given alert ID to evaluate alert details.
- /snapshot/user: Share a ZDX Snapshot for a given user ID to monitor user details about device and application use. 
To learn more, see ZDX Snapshots .


### February 20, 2026

#### User Location Report
The system-generated report for User Location is available in the ZDX Admin Portal.

 See image. 

To learn more, see Viewing System-Generated Reports .


### February 06, 2026

#### Session Timeout Duration
Configure the Session Timeout Duration to determine how long a user can access the ZDX Admin Portal in a session while being inactive.

 See image. 

To learn more, see Configuring Administrator Management Settings .

#### Zoom Call Quality Monitoring Exclusion Criteria
Call Quality Monitoring for Zoom now supports exclusion criteria during tenant onboarding, allowing the collection of call quality data for all users except specified users or groups.

New fields in the Monitoring Criteria section:
 
- User groups: Select one or more groups to exclude from monitoring.
- Users: Add individual users to exclude.
- Departments: Exclude entire departments to streamline administration. 
These options make it easy to apply broad monitoring while exempting specific users or teams as needed.

 See image. 

To learn more, see Configuring Zoom Call Quality for Digital Experience Monitoring .


### January 16, 2026

#### Location of Stored ZDX Data
ZDX logs and data are now stored in Canada in addition to the United States, the European Union (Western Europe, Netherlands), Singapore or Australia East (New South Wales). Contact your Zscaler Account team for details.

To learn more about Zscaler's retention of logs and data, see ZDX Logs .

#### Support for IPv6 in ZDX
ZDX now supports IPv6 to include dual-stack (IPv4 and IPv6) or IPv6-only configurations.

ZDX IPv6 visibility requires Zscaler Internet Access (ZIA) IPv6 to be enabled, as ZDX relies on ZIA to route and inspect IPv6 traffic for telemetry collection. To learn more, see Understanding IPv6 Support .

You can view IPv6 configurations across the ZDX Admin Portal (e.g., Cloud Path, Device Details).

 See image. 

To learn more, see Viewing IPv6 Configurations .
