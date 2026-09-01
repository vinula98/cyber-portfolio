---
title: "Cybersecurity Improvement Program — National Railway Museum"
description: "Ongoing cybersecurity improvement program translating assessment findings into practical controls across network segmentation, firewall validation, IAM, incident response, software governance, and vendor coordination."
---

# Cybersecurity Improvement Program — National Railway Museum

## Project Overview

**Organisation:** National Railway Museum (NRM)

**Location:** Port Adelaide, South Australia

**Role:** Cyber Security Volunteer — Infrastructure Security, IAM & Governance

**Project Duration:** March 2026 – Present

**Earlier Engagement:** Cybersecurity Risk Analyst, university capstone team, 2025

**Last Updated:** August 2026

---

## Project Highlights

- Progressed the museum from cybersecurity assessment and planning toward practical implementation across network segmentation, MFA, access governance, software control, incident response, and asset visibility
- Designed a practical segmented network model for user, server/archive, and CCTV environments
- Coordinated with the external managed service provider on Sophos firewall requirements, then validated newly configured isolated interfaces before production migration
- Developed current-state, CCTV, and proposed segmented architecture diagrams using sanitised, stakeholder-friendly documentation
- Built an asset and software governance foundation including inventories, audit planning, and a 10-worksheet software audit workbook
- Authored practical governance artefacts covering access privilege management, joiner-mover-leaver access, acceptable use, third-party software restriction, MFA rollout, and incident response
- Created a cyber incident response playbook supported by seven workflow diagrams for non-technical and operational users

---

## Challenge

The National Railway Museum manages operational systems, member and volunteer information, financial platforms, a public website, CCTV infrastructure, and a significant historical archive. Its environment must remain usable for volunteers with varied levels of technical confidence.

The initial environment included a largely flat network, an unmanaged network switch, limited MFA coverage, incomplete software and access visibility, shared or operationally sensitive systems, and legacy technology considerations. The core challenge was not to propose enterprise-scale tooling, but to identify and support controls that reduced risk without disrupting museum operations.

The public portfolio story spans two connected phases. In 2025, I contributed as part of a four-person university capstone team that assessed the museum's cybersecurity posture and developed a practical improvement framework and roadmap. In 2026, I returned independently as a Cyber Security Volunteer to help translate those recommendations into technical validation, operational procedures, governance documentation, and implementation preparation.

---

## Approach

The engagement followed a practical improvement flow:

**Assess → Design → Validate → Formalise → Sustain**

**Assess:** Document assets, software, operational dependencies, current network design, risks, and control gaps.

**Design:** Create segmentation models, access rules, MFA priorities, governance controls, and migration planning artefacts.

**Validate:** Test newly configured firewall interfaces, addressing, gateway reachability, connectivity behaviour, and migration prerequisites.

**Formalise:** Develop procedures, playbooks, inventories, rule matrices, audit workbooks, and user-friendly security guidance.

**Sustain:** Support ownership, periodic review, access lifecycle practices, software maintenance, stakeholder decisions, and continuous improvement.

---

## Key Deliverables

### Network Segmentation and Firewall Validation

The project progressed from documenting flat-network risk to preparing a practical segmented network model. I designed the target security zones, translated operational dependencies into communication logic, and coordinated requirements with the external provider.

The provider performed the authorised Sophos firewall configuration. My contribution focused on requirements, coordination, review, controlled testing, and validation.

Status:

* Current network diagram — completed
* CCTV architecture diagram — completed
* Proposed segmented architecture — completed
* Inter-zone communication/rules matrix — completed
* Infrastructure and switch validation — completed
* Sophos segmented-interface testing — successfully validated
* CCTV/server production migration — prepared as a controlled pending/follow-on activity

![Proposed Network Segmentation Architecture](/images/nrm/proposed-network-segmented-design.png)

### Asset and Software Governance

I developed structured records to improve visibility of technology assets, applications, operational dependencies, ownership questions, and software risk.

Status:

* Asset inventory — completed and designed to remain a living record
* Software & Application Audit Plan — completed
* Software Audit Workbook — completed with 10 structured worksheets
* Software & Application Inventory — draft/living inventory
* Third-Party Software Restriction Procedure — draft completed

### MFA and Access Governance

I reviewed authentication and access practices, then developed governance artefacts suited to a volunteer-heavy organisation.

Status:

* MFA readiness and rollout plan — completed, with implementation phased
* Access Privilege Management Procedure — draft completed
* Joiner-Mover-Leaver Access Management Procedure — in development/draft
* Administrative, privileged, and internet-facing account review — completed as part of the assessment and planning work

### Incident Response Capability

I authored a practical Cyber Incident Response Playbook to help the museum respond consistently during security events.

The playbook covers incident identification, reporting, triage, escalation, containment, recovery, evidence handling, stakeholder notification, vendor escalation, and post-incident review. It includes seven workflow diagrams to make the process easier for non-technical users to follow under pressure.

Status:

* Cyber Incident Response Playbook — draft completed
* Supporting workflow diagrams — completed as part of the draft playbook

### Stakeholder and Vendor Coordination

Throughout the volunteer engagement, I acted as a bridge between cybersecurity planning, museum operations, and external technical support.

Activities included:

* Confirming priorities, constraints, and acceptable implementation windows
* Translating findings into diagrams, checklists, procedures, and decision points
* Preparing focused questions and evidence for the managed service provider
* Following up on firewall changes, implementation dependencies, hardware limitations, and migration readiness
* Scheduling technical work to minimise disruption to museum systems and CCTV operations

---

## Outcomes

The project has strengthened the museum's cybersecurity foundation by improving visibility, documenting dependencies, validating technical changes, and establishing practical governance artefacts.

Concrete outcomes include:

* Progressed the museum from a documented flat-network risk toward three separated security zones for user, server/archive, and CCTV environments
* Successfully validated two newly configured isolated firewall interfaces before production migration
* Produced at least three architecture/dependency views: current network, CCTV environment, and proposed segmented design
* Developed a 10-page incident response playbook supported by seven workflow diagrams
* Created a software-audit workbook with 10 structured worksheets
* Established operational governance artefacts covering access, user lifecycle, acceptable use, software restriction, software inventory, MFA, and incident response
* Converted vendor discussions into testable technical requirements and controlled migration checks
* Balanced recognised security frameworks with the real constraints of a small not-for-profit and volunteer workforce

Production migration of CCTV/server systems is prepared as a controlled follow-on activity and should not be described as complete until confirmed.

---

## Framework and Control Alignment

The work was informed by recognised cybersecurity frameworks and privacy obligations, without claiming formal certification or full compliance.

* **ASD Essential Eight:** MFA, software governance, patching and unsupported software considerations, administrative privilege restriction, backup validation, and practical maturity improvement
* **NIST Cybersecurity Framework:** Asset Management; Identity Management, Authentication and Access Control; Platform Security; Incident Management; Incident Analysis; Incident Recovery; continuous improvement
* **ISO/IEC 27001 principles:** Asset management, access control, acceptable use, operational security, supplier/third-party considerations, incident management, and continual improvement
* **Australian privacy context:** Privacy Act 1988, Australian Privacy Principle 11, and consideration of Notifiable Data Breaches obligations

---

## Supporting Evidence

The following public-facing evidence categories can be referenced without exposing sensitive configuration details:

* Sanitised current-state, CCTV, and proposed segmentation diagrams
* Asset and software inventory structures
* Software audit workbook structure
* Access privilege, acceptable use, third-party software, and joiner-mover-leaver procedure drafts
* Cyber incident response playbook structure and workflow diagrams
* MFA readiness and rollout planning notes
* Migration readiness and validation checklists
* Stakeholder and vendor coordination records

Sensitive details such as internal IP ranges, gateway/DNS/DHCP addresses, firewall ports, usernames, remote-access methods, and detailed firewall rules should remain unpublished.

---

## Skills Demonstrated

### Governance, Risk and Compliance

* Cybersecurity assessment
* Risk-based control prioritisation
* Governance and procedure development
* Framework-aligned documentation
* Security awareness for non-technical audiences

### Infrastructure Security

* Infrastructure analysis
* Dependency mapping
* Network architecture review
* Segmentation design
* Firewall-interface and connectivity validation

### Identity and Access Management

* MFA readiness assessment
* Access lifecycle governance
* Administrative and privileged access review
* Practical access-control documentation

### Stakeholder Communication

* Vendor coordination
* Requirements translation
* Status reporting
* Implementation planning
* Technical writing for mixed audiences

---

## Reflection

This project strengthened my ability to balance technical security objectives with operational reality. The most effective recommendation was not always the most complex one; it was the control the museum could afford, understand, maintain, and verify.

I gained practical experience translating risk and framework requirements into network designs, validation steps, procedures, playbooks, inventories, and stakeholder decisions suited to a small, volunteer-led organisation.
