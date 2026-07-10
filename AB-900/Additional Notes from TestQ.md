Additional Notes from Test Questions

1. Role of M365 Copilot orchestration service
    > Managing how prompts, data sources and LLMs interact to produce secure, relevant responses.
  
2.  Data Loss Prevention (DLP) is designed to prevent unauthorized sharing or exfiltration of sensitive information

3. Function of Copilot Control System in M365 admin center
    > Primarily responsible for managing aagent availabilty, assignments, data access and related policies across entire tenant.

    > Helps administrators efficiently control and monitor the activities of agents within the organization

4. Grounding during prompt processing means enriching a user's prompt with contextual data from sources like Microsoft Graph and apps before sending it to LLMs.

5. Purview is to provide a unified data governance, protection and compliance management across M365

6. Data Security Posture Management (DSPM) for AI in Microsoft Purview focus on monitoring and controlling sensitive data used by AI systems.
   
    Helps organizations discover, classify and secure data flows in AI workloads to ensure compliance and promote responsible AI use.

7. Deep briefing pack is to run multi step research across internal content and the web to produce a sourced breifting

    Allows for the analysis of internaal slide decks, notes, email and other sources to create a structured report that can be resued in future updates

8. Microsoft Defender provides advannced threat protection capabilities, including URL rewriting for click time verification and attachment detonation in an isolated environment.

9. Microsoft Defender XDR can provide real time insights, indicators of compromise and behavioral analytics that can be used to enhance detection capabilities and automate response actions

10. SharePoint admin can restrict access to a specific subset of files without altering permissions on the entire site by creating a folder with unique permissions

11. Zero Trust security model have the concept of "never trust, always verify" which applies to all connections, even internal networks.

12. Microsoft 365 admin center Copilot reports and the Agent page is the best approach to track adoption and status of custom agents built with Copilot Studio.

    This method provides a tenant level view that shows which custom agents are being used, how often they are used and if any are currently blocked or disabled

13. Explorer in Mircosoft Purview provides at a glance snapshot view across labeled and classified items.
    
    It allows users to filter and drill into the data to gain insights into the location and classification of items within the organization data sources.

14. Data access governance reports in SharePoint admin center provides a tenant level view of sites that might be overshared or contain sensitive content.

15. Power Platform admin center is primarily used to manage environments, connectors and usage analytics for agents built with a Copilot Studio.

16. Copilot Prompt Gallery lets users and teams save and share prompts so that a carefully runed instruction can be resused consistently.

17. Purview retention policies <b>ARE NOT A COMPLETE REPLACEMENT</b> for backup and recovery strategies

    They do not offer the same level of data protection and recovery capabilities as dedicated backup solutions

18. Copilot admins can scope individual agents to specific groups or users.

19. DLP mainly looks at preventing sensitive daata from leaving the organization (content aaaand actions in the moment)

20. Insider Risk management analyzes user behavior patterns over time to detect potenntial insider risks (user behavior over time)

21. Microsoft Defender XDR helps security teams by correlating related alerts into a single incident view.

22. Risky sign ins & Risk Users reports in Entra ID is an effective approach for troubleshooting MFA, Conditional Access and risky sign ins.

23. Global admins have the ability to add custom domains and set the default domain for new users email address

    Once subscription is created, they do not have the capability to change the tenant original country / region.

24. Data access governance report in SharePoint can generate tenant wide snapshots that list sites with potentially overshared or sensitive content for further analysis and remediation actions

25. Purview Information Protection primarily focused on classifying and protecting sensitive data within organization.

26. Purview Data Loss Prevention is designed to detect and prevent unauthorized disclosure of sensitive information.

27. App registration are used to define the global blueprint of an application which includes :
    - Redirect Urls
    - Supported account types
    - Exposed API scopes

28. Enterprise application is the primary object to configure when integrating a 3rd party SaaS application for SSO and access control

29. Turning off meeting recording for specific users or teams in the Teams admin will affect all users in that team.

    Meeting policies are used to control meeting settings and permissions at a more ranular level, allowing for specific teams or users to have different settings.

30. M365 Copilot agents usage report is specifically designed to show active users and usage for each agent in the M365 admin center.

31. App registration create the global definition of an app while enterprise applications represent the local service principal instance in each tenant where the app is used.

32. We can edit the distribution group in Exchange admin center and configure its delivery management and address list options to prevent external senders from emailing the internal announcement list.

33. Process of using Microsoft Graph to anchor prompts in your organizations data is called grounding.
    
    Grounding involves retrieving relevant, premission trimmed content and context from Graph to provide a well informed response to the user

34. Improvement actions page is to provide prioritized list of concrete tasks that will raise compliance score if tasks are completed.

    Also allows for assignment of owners, storage of evidence and tracking of taks status

35. Integrated Apps in M365 admin center is for centrally managing and disabling built in Copilot agents in the Copilot app.

    This section allows admins to control the availability and settings for integrated apps within M365 environment

36. Microsoft Defender Threat Intelligence is designed to be a central source of curated threat intelligence that can enrich investigations across Microsoft Defender XDR and Sentinel.

37. Microsoft Copilot Dashboard and M365 admin center Copilot usage reports are built on the same underlying usage dataset but are tailored for different audiences and perspectives on Copilot adoption and impact.

    - M365 admin center usage reports provide IT admins with SKU level usage reports and license details to track user adoption

    - Copilot Analytics offer insights into how Copilot is changing work patterns and measure business impact over time for executives

 - App registration define how an application integrates with Microsoft Entra ID, such as API permissions and authentication settings

- Enterprise apps represent the specific instances of those applications and manage access withing a particular tenant

- Power Automate is a tool that allows users to automate workflows and integrate different applications and services.

- Scheduled prompts in Copilot is to view, run, edit and delete their scheduled prompts.

- Purview Audit is a central audit solution that can capture and provide detailed insights into user interactions across M365 apps including Copilot.

- Label encryption to a group allows specific users, such as auditors, to access the encrypted files without using Copilot to summarize them.

- Entra ID Protection can detect high risk sign ins and provide risk assessment

    It still requires Conditional Access policies to be configured to enforce actions such as requiring multifactor authentication or blocking access based on risk level

- Defender for Office is the core M365 security feature that specifically focuses on protecting email and collaboration tools like Exchange Online and MIcrosoft Teams from phishing, malware and unsafe URLs.

- Administrative units are used for organizing users and resources for administrative purposes such as delegating administrative tasks

- Data loss prevention alerts page in Purview is specifically designed for security analysts to view, filter and triage DLP incidents.

- Advanced hunting in Defender XDR allows the threat hunting team to proactively search across raw telemetry using Kusto Query Language (KQL).
  
    Provides a hunting surface that exposes events and entities over a specified time frame, enabling the team to test hypotheses and discover new attack patterns without waiting for alerts.

- Incidents queue in Defender XDR allows analysts to view and manage security incidents that are automatically generated by correlating alerts from various Defender XDR workloads.

- Purview unified audit log does not cover Entra ID specific activities such as changes to Entra roles or creation of enterprise applications

- Defender Threat Intelligence is primarily used for understanding attacker infrastructure, campaigns and emerging vulnerabilities while blocking malicious attachments and real time URL rewriting in email that come from other Defender components.