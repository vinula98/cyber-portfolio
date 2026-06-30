from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


OUTPUT = Path(__file__).resolve().parents[1] / "public" / "Vinula_Kasthuriarachchi_Resume.pdf"


EXPERIENCE = [
    (
        "Cyber Security Volunteer",
        "National Railway Museum",
        "Adelaide, Australia",
        "March 2026 - Present",
        [
            "Conducting cybersecurity assessments across operational IT environments, identifying risks related to network architecture, access control, infrastructure exposure, and operational dependencies.",
            "Developed asset inventories, software application inventories, network topology documentation, and stakeholder-friendly infrastructure diagrams across servers, NAS systems, CCTV infrastructure, workstations, and networking equipment.",
            "Designed a proposed segmented network architecture separating User, Server, and CCTV environments, including conceptual traffic restriction and access control logic.",
            "Collaborated with stakeholders and external service providers to support VLAN-based segmentation planning, Sophos firewall architecture review, infrastructure validation, and implementation preparation.",
            "Assessed identity and access management practices, reviewed MFA adoption opportunities, and developed recommendations aligned with operational requirements.",
            "Developed cybersecurity governance documentation including access management procedures, acceptable use standards, software governance controls, awareness material, validation documentation, and cybersecurity improvement roadmaps.",
        ],
    ),
    (
        "Team Member / Acting Assistant Department Manager Secondment",
        "Woolworths Group",
        "Adelaide, Australia",
        "October 2023 - Present",
        [
            "Trusted to perform Acting Assistant Department Manager responsibilities during a 5-week secondment, supporting team coordination, task allocation, and operational decision-making.",
            "Supported customer service, daily store operations, stock replenishment, and inventory management in a fast-paced retail environment.",
            "Helped maintain operational standards, team communication, and customer service quality.",
        ],
    ),
    (
        "Software Engineering Consultant (Front-End Technologies)",
        "Evolza",
        "Colombo, Sri Lanka",
        "March 2023 - July 2023",
        [
            "Delivered technical solutions and supported front-end development activities.",
            "Facilitated client training sessions on system functionality and best practices.",
            "Collaborated with stakeholders to translate business requirements into structured technical implementations.",
            "Provided post-deployment support and process guidance to support operational stability.",
        ],
    ),
    (
        "Software Engineer Intern",
        "Kavithi Group",
        "Colombo, Sri Lanka",
        "July 2022 - January 2023",
        [
            "Worked primarily as a Front-End Developer on company projects including ERPNext and the Blynxx Quiz App.",
            "Supported front-end development, testing, and application improvement activities.",
            "Collaborated with technical teams to deliver software features and improvements.",
        ],
    ),
    (
        "Software Engineer Intern",
        "iiH Solutions (Pvt) Ltd",
        "Colombo, Sri Lanka",
        "July 2020 - July 2021",
        [
            "Worked in the Front-End Development team on the company project Infirma.",
            "Developed front-end features using ReactJS.",
            "Collaborated with development teams on software maintenance, testing, and feature implementation.",
        ],
    ),
    (
        "Customer Service Associate",
        "Dialog Axiata PLC",
        "Colombo, Sri Lanka",
        "October 2017 - February 2018",
        [
            "Managed high-volume customer interactions in a regulated telecommunications environment.",
            "Supported customers with service enquiries and issue resolution.",
            "Developed communication, problem-solving, and customer support skills.",
        ],
    ),
]


def para(text, style):
    return Paragraph(text.replace("&", "&amp;"), style)


def bullet_list(items, style):
    return ListFlowable(
        [ListItem(para(item, style), leftIndent=8) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=14,
        bulletFontSize=5,
    )


def section(title, styles):
    return [
        Spacer(1, 5),
        para(title, styles["Section"]),
        Spacer(1, 4),
    ]


def build_pdf():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=25,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Contact",
            parent=styles["Normal"],
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#334155"),
            alignment=1,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=14,
            textColor=colors.HexColor("#0369a1"),
            borderPadding=(0, 0, 2, 0),
            spaceBefore=4,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Role",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=5,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            parent=styles["Normal"],
            fontSize=8.5,
            leading=10.5,
            textColor=colors.HexColor("#475569"),
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodySmall",
            parent=styles["Normal"],
            fontSize=8.4,
            leading=10.4,
            textColor=colors.HexColor("#1e293b"),
        )
    )

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=14 * mm,
        leftMargin=14 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
    )

    story = [
        para("Vinula Kasthuriarachchi", styles["Name"]),
        para(
            "Adelaide, South Australia | 0404781574 | vinulakas.98@gmail.com | www.linkedin.com/in/vinula-kasthuriarachchi-7b3130154 | github.com/vinula98",
            styles["Contact"],
        ),
    ]

    story += section("Professional Summary", styles)
    story.append(
        para(
            "Cybersecurity graduate with a Master of Information Technology (Cyber Security) from the University of South Australia and a background in Software Engineering. Experience supporting cybersecurity assessment, infrastructure analysis, network segmentation planning, governance development, identity security improvements, and cyber risk reduction initiatives.",
            styles["BodySmall"],
        )
    )

    story += section("Experience", styles)
    for title, company, location, dates, bullets in EXPERIENCE:
        story.append(para(title, styles["Role"]))
        story.append(para(f"{company} | {location} | {dates}", styles["Meta"]))
        story.append(bullet_list(bullets, styles["BodySmall"]))

    story += section("Education", styles)
    story.append(para("<b>Master of Information Technology (Cyber Security)</b> - University of South Australia - Completed 2025", styles["BodySmall"]))
    story.append(para("<b>BEng (Hons) Software Engineering</b> - University of Westminster - Upper Second Class Honours (2:1)", styles["BodySmall"]))

    story += section("Certifications & Learning", styles)
    story.append(
        bullet_list(
            [
                "CompTIA Security+ (In Progress)",
                "Google Security Operations Certificate",
                "TryHackMe SOC Level 1 Path",
                "LetsDefend SOC Training",
            ],
            styles["BodySmall"],
        )
    )

    story += section("Technical Skills", styles)
    story.append(
        para(
            "Network Security | Identity & Access Management | Cyber Risk Assessment | Governance & Compliance | NIST Cybersecurity Framework | Microsoft Windows | Active Directory | Python | Java | SQL",
            styles["BodySmall"],
        )
    )

    doc.build(story)


if __name__ == "__main__":
    build_pdf()
