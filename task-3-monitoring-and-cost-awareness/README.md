
# SWYNEX - Monitoring and Cost Awareness

## 1. Project Overview
This document describes basic monitoring, status checks, alerting ideas, cost awareness, and security controls for the conceptual cloud deployment created during Task 2.

## 2. Monitoring and Status Checks
For a cloud-hosted application, monitor:
- Website availability using periodic HTTP status checks.
- Application logs for errors and failed requests.
- CPU and memory usage when supported by the hosting platform.
- Deployment status and build failures.

For AWS-based deployments, Amazon CloudWatch can collect supported logs and metrics. For this project hosted on GitHub Pages, use the deployment workflow status and browser checks to verify that the site is available.

## 3. Simple Alert Idea
**Condition:** The website returns an HTTP error or the deployment workflow fails.

**Action:** Review the deployment status, inspect available error logs, and investigate the failed build or incorrect configuration. A monitoring service could send an email notification when a supported alert condition is detected.

This is a proposed alert design, not an active monitoring alert.

## 4. Cost Awareness Checklist
- [ ] Prefer free hosting options for a small static website.
- [ ] Check pricing before creating paid cloud resources.
- [ ] Set a budget and review usage regularly when using a cloud provider.
- [ ] Remove unused compute resources and storage.
- [ ] Review data transfer and logging costs.
- [ ] Avoid enabling unnecessary paid services.

## 5. Security and Access-Control Checklist
- [ ] Use HTTPS for public website access.
- [ ] Give users and services only the permissions they need.
- [ ] Enable multi-factor authentication on cloud accounts where available.
- [ ] Never commit passwords, access keys, or API tokens to GitHub.
- [ ] Review repository visibility and access permissions.
- [ ] Keep software and dependencies updated where applicable.

## 6. Results and Limitations
The website is hosted through GitHub Pages. Repository and deployment status can be checked through GitHub. No active third-party uptime monitor, email alert, or paid cloud monitoring service has been configured as part of this documentation.

## 7. Conclusion
Monitoring helps identify availability and deployment problems. Cost reviews help avoid unnecessary expenses, while access controls and HTTPS improve security.

**Project:** SWYNEX Cloud Computing Internship - Task 3
