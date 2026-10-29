
# SWYNEX - Final Cloud Deployment Case Study

## 1. Project Overview

This case study combines cloud architecture design, static website deployment, monitoring concepts, cost awareness, and security best practices as part of the SWYNEX Technologies Cloud Computing Internship.

**Project:** Final Cloud Deployment  
**Cloud Platform:** GitHub Pages  
**Technology:** HTML, CSS, GitHub  
**Project Type:** Static website hosting  
**Internship Task:** Task 4

## 2. Cloud Architecture

The conceptual architecture includes the following components:

- **Compute:** Amazon EC2 is a possible option for hosting applications that require a server.
- **Storage:** Amazon S3 can store files and static website assets.
- **Networking:** HTTPS provides encrypted communication between users and the website.
- **Identity and Access Management:** IAM controls access to AWS resources.
- **Monitoring:** Amazon CloudWatch can collect supported metrics and logs from AWS resources.

For this project, the static website is hosted using GitHub Pages rather than deployed on AWS.

## 3. Deployment Process

The website was prepared using HTML and CSS and stored in a GitHub repository.

Deployment steps:

1. Create the HTML website.
2. Upload the website files to GitHub.
3. Enable GitHub Pages in repository settings.
4. Select the `main` branch and root folder as the publishing source.
5. Wait for GitHub Pages to build and publish the site.
6. Open the published URL to verify the website.

### Live Website

https://syedabubakar01.github.io/SWYNEX-Cloud-Architecture-Outline/

### Source Repository

https://github.com/syedabubakar01/SWYNEX-Cloud-Architecture-Outline

## 4. Monitoring and Status Checks

Basic monitoring activities include:

- Checking whether the published website opens successfully.
- Reviewing GitHub Pages deployment and build status.
- Inspecting available workflow logs when a deployment fails.
- Checking the website after changes are committed.

### Proposed Alert

If a deployment fails or the website becomes unavailable, investigate the build status, configuration, and available error information.

This is a proposed monitoring approach. An automated uptime alert has not been configured for this project.

## 5. Cost Awareness

The project uses GitHub Pages for static website hosting.

Cost-management practices:

- Prefer free hosting for small educational projects.
- Review pricing before creating paid cloud resources.
- Avoid unused compute instances and storage.
- Monitor usage and data transfer when using paid cloud services.
- Review logging and monitoring costs before enabling additional services.

## 6. Security Checklist

- [ ] Use HTTPS for website access.
- [ ] Never upload passwords, API keys, or access tokens.
- [ ] Use least-privilege access for cloud resources.
- [ ] Enable multi-factor authentication on cloud accounts where available.
- [ ] Review repository permissions and visibility.
- [ ] Keep software and dependencies updated where applicable.

## 7. Lessons Learned

This project helped develop an understanding of:

- Basic cloud architecture components.
- Static website hosting and repository-based deployment.
- GitHub Pages configuration and deployment verification.
- Monitoring concepts and deployment troubleshooting.
- Cloud cost awareness and access-control practices.
- The differences between conceptual AWS architecture and an actual AWS deployment.

## 8. Limitations

This project uses GitHub Pages to host a static website. It does not demonstrate a deployed AWS EC2 application, AWS S3 integration, or an active CloudWatch alert. Those components are described as cloud architecture concepts rather than implemented services.

## 9. Conclusion

The project demonstrates the basic process of preparing, publishing, and verifying a static website. It also documents monitoring approaches, cost-management practices, security considerations, and potential improvements for a future cloud deployment.

**Project:** SWYNEX Cloud Computing Internship - Task 4
