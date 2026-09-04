# O-RAN ALLIANCE Test and Integration Focus Group

# Criteria and Guidelines of Open Testing and Integration Centre

Copyright $\circledcirc$ 2025 by the O-RAN ALLIANCE e.V.

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material of this specification for your personal use, or copy the material of this specification for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

O-RAN ALLIANCE e.V., Buschkauler Weg 27, 53347 Alfter, Germany

# Contents

Foreword.. ..2   
Modal verbs terminology ... .2   
1 Scope ..... ..3   
2 References .... ....3   
2.1 Normative references.... ..... 3   
2.2 Informative references . ..... 4   
3 Definition of terms, symbols and abbreviations.. ...4   
3.1 Terms ..... ................................................................... ..... 4   
3.2 Symbols ... ..................................................................... .... 5   
3.3 Abbreviations.......   
4 Overview of OTIC .. ..........6   
5 General Requirements of OTIC . ................ .....7   
5.1 Participants and roles in OTIC... ........................... ...... 7   
5.1.1 Host ....... ........................................................................................................................ 7   
5.1.2 Partner ..... ..................................................................................................................... ..................... 8   
5.1.3 Client ...........   
5.1.4 Observer .....   
5.2 OTIC Physical Lab Architecture and Layout .................................................................................................... 9   
5.3 Basic Guidelines for OTIC Agreements .....   
6 Application and Qualification Processes....... ........................................................................................10   
6.1 Application for OTIC Qualification.. ................................................................................ ..... 10   
6.2 OTIC Application Reviewing and Evaluation .. ..................................................................................... ..... 11   
6.3 OTIC Application Approval . .................................................................................... ..... 11   
6.4 OTIC Catalogue.. ...................................................................................................... ..... 12   
6.5 Complaints and Disqualification.... ................................................................ ....... 12   
Annex A (normative): OTIC application form. ...14   
Annex B (informative): Guidelines on OTIC application form . ...20   
Annex C (normative): Hosting agreement.. ...21   
Revision history....... .....25   
History ..... Error! Bookmark not defined.

# Foreword

This Process Document has been produced by O-RAN ALLIANCE.

# Modal verbs terminology

In the present document "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"must" and "must not" are NOT allowed in O-RAN deliverables except when used in direct citation.

# 1 Scope

The contents of the present document are subject to continuing work within O-RAN and may change following formal O-RAN approval. Should the O-RAN Alliance modify the contents of the present document, it will be re-released by O-RAN with an identifying change of version date and an increase in version number as follows:

version xx.yy.zz

where:

xx: the first digit-group is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have $\tt x x { = } 0 1$ ). Always 2 digits with leading zero if needed.

yy: the second digit-group is incremented when editorial only changes have been incorporated in the document. Always 2 digits with leading zero if needed.

zz: the third digit-group included only in working versions of the document indicating incremental changes during the editing process. External versions never include the third digit-group. Always 2 digits with leading zero if needed.

The present document describes the essential criteria and guidelines (guiding principles) from process, organization, space and technical perspective on the qualified Open Testing and Integration Centre (OTIC).

The conformance and interoperability certification/validation/badging processes will be described in a separate set of documents (e.g. [1]), incl. the definition on who can and how to issue O-RAN certificate or badge.

# 2 References

# 2.1 Normative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are necessary for the application of the present document.

[1] O-RAN.TIFG.Cert-Badge.0-v05.00: O-RAN ALLIANCE Test and Integration Focus Group, Certification and Badging Processes and Procedures, Version 05.00, October 2022”

[2] O-RAN.WG1.O-RAN-Architecture-Description-v07.00: O-RAN ALLIANCE WG1, O-RAN Architecture Description, Version 7.0, October 2022

[3] O-RAN.TSC.WORKPROC-v03.00: “O-RAN Working Procedures”

[4] O-RAN ALLIANCE Constitution, version 27-06-2018 , available at www.o-ran.org/membership-info

# 2.2 Informative references

References are either specific (identified by date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies.

NOTE: While any hyperlinks included in this clause were valid at the time of publication, O-RAN cannot guarantee their long-term validity.

The following referenced documents are not necessary for the application of the present document, but they assist the user with regard to a particular subject area.

# 3 Definition of terms, symbols and abbreviations

# 3.1 Terms

For the purposes of the present document, the following terms apply:

Affiliate: the definition is given in [4].

Blueprint: is the set of inputs which is used to describe a specific O-RAN deployment from several aspects. These aspects include the specification of the O-RAN deployment at the system level (e.g. architecture, performance metrics) as well as subsystem level and the interfaces between the specified subsystems. This would then allow definition and documentation of the testing methodology and the test cases using the blueprint specification.

Client: is a participant in OTIC who provides its O-RAN equipment, components and/or services for the testing in OTIC.

Host: is a founder and main sponsor of Open Testing and Integration Centre (OTIC). Only O-RAN Member (including the affiliates [4]) or non-vendor O-RAN Participants (including the affiliates [4]) may become a host. Host is mandatory entity in OTIC.

IOT profile: specifies a specific selection of parameters, optional features, default values and ranges of configurable attributes and mechanisms from O-RAN subsystem interface specification(s) that shall be supported and used in order to guarantee interoperability between implementations from different vendors.

Observer: is a participant in OTIC who is allowed to observe the testing activities in OTIC for a limited period and/or a limited purpose.

OTIC: is a qualified Open Testing and Integration Centre meeting the relevant subset of criteria and guidelines mentioned in the present document.

O-RAN Academic Contributor: the definition is given in [3].

O-RAN Contributor: the definition is given in [3].

O-RAN Entity: the definition is given in [3].

O-RAN Member: the definition is given in [3].

2 O-RAN Participant: the definition is given in [3].

Partner: is a participant in OTIC who can provide, maintain and/or operate test and measurement equipment and tools, can provide space and services, can design, set-up, conduct and evaluate the testing activities on behalf of host.

Testing: any activity involving testing of O-RAN equipment, e.g. plugfest, demo, lab trial, field trial.

# 3.2 Symbols

For the purposes of the present document, the following symbols apply:

# 3.3 Abbreviations

For the purposes of the present document, the following abbreviations apply:

IOT Interoperability   
IUT Interface under Test   
O-CU-CP O-RAN Central Unit – Control Plane   
O-CU-UP O-RAN Central Unit – User Plane   
O-DU O-RAN Distributed Unit   
O-RU O-RAN Radio Unit   
OTIC Open Testing and Integration Centre   
PoC Proof of Concept   
RIC RAN Intelligent Controller   
TIFG O-RAN ALLIANCE Test and Integration Focus Group   
TSC O-RAN ALLIANCE Technical Steering Committee

# 4 Overview of OTIC

The Open Testing and Integration Centre (OTIC) provides a collaborative, open, and impartial working environment; however, the intellectual property of participants in OTIC must be protected in this environment as well.

The environment meeting all of the criteria and guidelines from this document may be qualified as OTIC and may be named as “Open Testing and Integration Centre (OTIC)”. OTIC may or may not have its own legal incorporation. OTIC is an activity outside O-RAN ALLIANCE.

8 Multiple OTICs may exist in different regions around the world. Each OTIC may focus on different O-RAN   
9 functions [2] (such as Near-RT RIC, O-CU-CP and O-CU-UP, O-DU, O-RU), interfaces [2] (such as Open   
10 Fronthaul, E2, O1, O2, A1), blueprints, IOT profiles, etc. The testing results, experiences, best practices,   
11 knowledge, lesson-learned, adopted processes, etc. are assumed to be shared among the OTICs in order to   
12 reduce the overall costs and resources and coordinate the efforts. The learning and experiences may also be published and shared outside the O-RAN community with specified level of confidentiality. The Open Testing and Integration Centre is proposed as vendor-independent1 , open and qualified physical space in order to, among others (not everything must be included in the scope of work of a particular OTIC):   
a) Support of wide adoption of O-RAN specifications and promote the openness of O-RAN ecosystem via demos, community events (e.g. speaker sessions, workshops, tutorials), lab and field trials, etc.   
b) Demonstrate implementations and solutions based on O-RAN specifications via plugfests and proofs of concept “PoCs”.   
c) Test and verify the conformity of RAN equipment with O-RAN interface specifications, based on O-RAN conformance test specifications.   
d) Test and verify the interoperability of RAN equipment from different vendors (or the same vendor) using O-RAN interface specifications, based on O-RAN interoperability test specifications.   
e) Foster and develop the integrator’s technical capabilities via workshops, tutorials, etc.   
f) Conduct functional as well as performance (load, capacity) tests of both end-to-end systems as well as sub-systems.   
g) Give O-RAN (in particular O-RAN workgroups, O-RAN contributors) feedback about the experiences made with O-RAN specifications during the testing activities (i.e. implementation driven specification).

The coordination (in terms of considered focus areas, test scenarios, operators’ specific requirements, plugfests) among worldwide OTICs is required to avoid fragmentation and repeating the same functional as well as performance tests (with the same vendors) multiple times. The services offered by OTICs should be complementary rather than competitive.

The O-RAN ALLIANCE in cooperation with TIFG (O-RAN ALLIANCE Test and Integration Focus Group) is the governing body to resolve any un-clarity, inconsistency and ambiguity in the present document, as well as any conflict and complaint which cannot be resolved internally inside OTIC.

# 5 General Requirements of OTIC

# 5.1 Participants and roles in OTIC

The following roles with relations and responsibilities are defined in Open Testing and Integration Centre (OTIC):

a) Host b) Partner c) Client d) Observer

# 9 5.1.1 Host

a) Host is a founder, main contact (designated multi-host representative in case of co-hosted OTIC) and main sponsor of OTIC. The financial flows inside the OTIC are controlled and managed by the host itself. Host is also an entity which coordinates and is fully responsible for all the activities in OTIC.   
b) Host shall be an O-RAN Member [3] (i.e. mobile operator, including the affiliates [4]) or an O-RAN Participants [3] (i.e. O-RAN Contributor or O-RAN Academic Contributor, including the affiliates [4]); in order to ensure a high level of credibility, confidentiality, the O-RAN Participant shall demonstrate vendor-independence2 . For example, a third-party authorized test laboratory (an open lab) may also host OTIC, but it shall become O-RAN Participant first. Note that only O-RAN Entities may present the results, proposals, etc. at O-RAN ALLIANCE meetings, and upload the results and reports to O-RAN ALLIANCE wiki and other shared folders.   
c) OTIC may be hosted by one or more hosts (co-hosted OTIC). In this case a designated multi-host representative will be designated as main OTIC contact among the involved hosts.   
d) Host provides the space (test rooms, server rooms) for conducting of the tests and hosting the events (incl. IOT and conformance testing, plugfest, PoC, demo), network connectivity, and test/measurement equipment, tools and services. These can be fully or partially provided by the host itself or by the contracted partner(s), but the host assumes responsibility for meeting the required criteria, conditions, and guidelines.   
e) Host guarantees the openness and fairness to any client who has interest in testing its equipment in OTIC. It means OTIC is available and open for all clients, and any client may not be disqualified from testing in OTIC without cause. All clients shall be handled equally.   
f) Host guarantees the credibility, confidentiality, openness and vendor-independence2 of OTIC. Host also guarantees that the agreed test procedures are properly followed, and the results are produced in agreed format and with certain level of quality and confidentiality.   
g) Host enters into agreements (e.g. participant agreement, testing agreement) with all other participants in OTIC. The agreement shall be in compliance with the criteria and requirements stated in the present document.   
h) Host shall take all necessary steps (e.g. participant’s agreement, testing agreement, isolated space) to work towards protecting the intellectual property each participant in OTIC in a mutually collaborative environment; however, OTIC participants shall recognize that it may not be possible to safeguard intellectual property in all situations, e.g. outdoor equipment.   
i) Host shall take necessary steps to ensure that the used test and measurement equipment and tools are properly calibrated and ready to use.   
j) Host allows the detailed results, blueprints, interface profiles, experiences, best practices, knowledges, lesson-learned, adopted processes, etc. to be shared following the confidentiality levels from the agreements.   
k) Host regularly presents the summary of testing results, experiences, best practices, knowledges, lesson-learned and adopted processes at TIFG meetings (and optionally on request to any other ORAN meeting).   
l) Host or multi-host designated representative responds to the request for information or testing results from TIFG in a timely manner.   
m) Host acts as a mediator trying to resolve any complaint inside OTIC. The complaint resolution processes (incl. documentation of resolution of complaint) shall be set up in each OTIC. O-RAN ALLIANCE in cooperation with TIFG acts as the governing body in case the complaint might not be resolved by the host(s) inside OTIC.   
n) In the multi-host scenario, O-RAN ALLIANCE and TIFG will only communicate officially with the multi-host designated representative.

# 5.1.2 Partner

a) Partner is any company/organization with or without O-RAN ALLIANCE membership in good standing.   
b) Partner can provide maintain, and/or operate test and measurement equipment and tools (e.g. emulators, log tools, analysers, generators) on behalf of the host on permanent basis or temporary basis per test.   
c) Partner can provide, maintain space (rooms, servers) and services in OTIC on behalf of the host.   
d) Partner can design, set-up, conduct and evaluate the testing activities on behalf of the host, but the host always guarantees that the test procedures are properly followed with certain level of quality and confidentiality (e.g. using a confidentiality agreement signed between host and partner).   
e) All the aforementioned items can be also provided by the host itself, i.e. OTIC can have no contracted partner.

# 5.1.3 Client

a) Client (or customer) is any company/organization with or without O-RAN ALLIANCE membership in good standing producing O-RAN equipment and components which are subsequently provided for the testing in OTIC.   
b) Client can choose any OTIC for the testing of its RAN equipment and components.   
c) The host or delegated partner should sign a testing agreement with the client.   
d) Client is encouraged to leave at least one representative product in the OTIC for a reasonable time period. Leaving more than one product is encouraged, as is replacing outdated products with newer models.

# 5.1.4 Observer

a) Observer (or Visitor) is any company/organization with or without O-RAN ALLIANCE membership in good standing which is allowed to observe the testing activities in OTIC for a limited period and/or a limited purpose. The period and purpose shall be clearly specified and known in advance to all participants in OTIC involved in testing activity. The role is expected to be more related to the O-RAN PlugFest.

1 b) The host guarantees that the confidentiality in OTIC is not violated by the observer (e.g. using a   
2 confidentiality agreement signed between host/delegated partner and observer).

# 5.2 OTIC Physical Lab Architecture and Layout

The OTIC physical lab is designed to create an open and collaborative environment, but at the same time satisfy IPR protection concerns of all OTIC participants. OTIC is a place where different participating companies are onsite collaborating, and where multiple different testing activities can be hosted at the same time. Therefore, the space layout, architecture and network setups shall be flexible and ensure restricted access to specific components only to specific participants engaged in specific testing activity.

A logical and physical separation between OTIC and the rest of facilities (e.g. host’s own internal lab(s)) shall be provided and ensured in order to minimize any security risk. The OTIC environment should be presented as an OTIC resource.

Every testing activity shall be assigned a separated work area with restricted access (e.g. a badging access) only to participants engaged in that testing activity. The work area shall be equipped with working desks and secure connections to the server room(s) with server racks. The size of specified work area is related to the number of engaged participants and complexity of the testing activity.

The server room(s) shall be separated from the work area. The restricted access to server room is granted only to participants engaged in the testing activity(ies). The server room might be shared for multiple testing activities but the physical and/or logical separation between servers shall be ensured (e.g. physical servers separated in locked racks, virtual servers logically separated).

The access to the network and sharing of the resources and equipment should be secured (e.g. using subnets, access lists).

The host of OTIC is responsible (also, where appropriate, by engaging into specific agreements with any contracted partners) for the security, configuration and maintenance of network (e.g. assignment of subnets, VPNs to each testing activity and participants) as well as for identification and provision of the proper test and measurement equipment and tools within hosted testing activities and supported services and focus areas. The additional equipment and tools, which are not available in OTIC, might be needed for the period of the testing activity.

Each OTIC is encouraged to have the capability to easily and securely connect to the other OTICs in case different HW or SW components from each individual OTIC need to communicate with each other.

The vendors may remotely connect their O-RAN functions to the OTIC and run the specified remote testing (e.g. remote testing of A1 interface between Non-RT RIC and Near-RT RIC, or O1 interface between Service Management and Orchestration system and O-RAN functions). This will allow vendors to scale logistic issues.

The OTIC support of remote connectivity is optional.

# 5.3 Basic Guidelines for OTIC Agreements

O-RAN ALLIANCE foresees the following two types of agreements that OTIC will adopt

Legal agreement between host and its potential partners, clients or observers

• Legally binding Hosting agreement between the underlying OTIC (OTIC host(s)) and O-RAN ALLIANCE

(see Annex C)

3 In general, the host or hosts have the full flexibility and authorization to negotiate and sign legal agreements   
4 with its partners, clients and observers. O-RAN ALLIANCE will not interfere in such processes. However, O  
5 RAN ALLIANCE recommends the following main common items to be included in the agreement:

Confidentiality

• Openness and fairness

Rights to share the testing/validation results and other outcomes

9 It is required for the underlying OTIC and its host(s) to sign the Hosting agreement with O-RAN ALLIANCE to   
10 be qualified as Open Testing and Integration Centre (OTIC), which may cover the following processes and   
11 main considerations:

Qualification and disqualification process Reporting and results sharing process Complaint resolution process

# 6 Application and Qualification Processes

# 6.1 Application for OTIC Qualification

This section describes OTIC qualification process. The OTIC applicant (i.e. host or designated multi-host representative in case of co-hosted OTIC) needs to send the complete application to otic@groups.o-ran.org in order to start OTIC qualification process. The OTIC application can be submitted at any time. The submitted application is received by the O-RAN Office and sent to TIFG for handling the review. The approval process is handled by O-RAN Office. The OTIC application form is defined in Annex A (with the guidelines on how to fill OTIC application form in Annex B), and it contains among others the following information:

• General information about OTIC, incl. name of OTIC, location (address) and main contacts

Information about the host(s) and potential partners, if any

Information about the lab(s), incl. space layout and architecture • Information about the supported focus area and work scope – supported services and test cases • OTIC applicant self-declaration confirming that the requirements for qualification have been fulfilled.

The name of OTIC shall be unique and English name including word “OTIC”. The proposed OTIC name may be revised and harmonized with other OTIC names during the review meeting. It would be also recommended (optional) to use the naming convention (scheme) based on geographic location of OTIC lab(s) and/or hosting company/organization name(s) whenever possible. Please visit https://www.o-ran.org/ for already approved OTIC names.

1

2 The following changes are subject to O-RAN approval. The OTIC needs to send a request for such approval to   
3 otic@groups.o-ran.org.

• Changing of name of OTIC • Changing of host(s) of the OTIC

# 6.2 OTIC Application Reviewing and Evaluation

Once the O-RAN Office sends the application to the TIFG, TIFG co-chairs assign each application to a reviewer who is the next in line and who has no relation to the OTIC applicant or OTIC host(s). The applications should be equally distributed to the reviewers.

0 The reviewer is selected from the list of reviewers which is maintained by TIFG. The reviewer list is accessible   
11 to all O-RAN Entities [3], and it contains information about the reviewers such as name, e-mail address, phone   
12 number, company affiliation, and assigned OTIC applications. Any representative of O-RAN Entity can be   
3 registered in or deregister from the list of reviewers at his or her own request at any time. The TIFG co-chairs   
4 can re-select the assigned reviewer if needed.

The assigned reviewer checks the application to ensure it is complete and in compliance with the requirements. If needed, the reviewer may request OTIC applicant to provide additional information for any missing or unclear information in the application. The reviewer is designated as the point of contact for all communications with OTIC applicant. The reviewer helps OTIC applicant to complete the application. The reviewer guarantees completeness and compliance of the application. The reviewer does not approve or evaluate the application.

Once the application is completed, the assigned reviewer needs to inform TIFG co-chairs to schedule a review meeting where OTIC applicant will present and defend the application. If needed, TIFG can also try to coordinate the application with other OTICs in order to avoid fragmentation, overlap, etc.

If the review meeting does not take place within 2 months of the date when application was submitted, the application may be withdrawn from review process. The applicant can still submit new OTIC application later on.

The preliminary favourable or unfavourable recommendations should be collected by TIFG co-chairs during the review meeting, and provided to OTIC applicant after the review meeting. The TIFG co-chairs also add the recommendations and summary of the review meeting to OTIC application. OTIC applicant has the rights to provide their statements and any necessary information or correction if the unfavourable recommendation is made. The OTIC applicant statements and corrections are also added to OTIC application.

It needs to be noted that the OTIC application cannot be approved or rejected by TIFG.

# 6.3 OTIC Application Approval

The completed application with TIFG recommendations and with OTIC applicant statements, if provided, shall be sent back to the O-RAN Office for further approvals. The OTIC application is handled as a process document and not as a technical specification. OTIC applicant needs to address any question or inquiry raised during this official approval process.

1 After passing O-RAN ALLIANCE approval process, OTIC applicant will be required to sign the Hosting   
2 agreement with O-RAN ALLIANCE, which is defined in Annex C. The OTIC qualification process is considered   
3 completed after the Hosting agreement is signed.

It needs to be noted that O-RAN ALLIANCE can terminate the Hosting agreement without cause at any time with prior written notice.

It needs to be also noted that the additional criteria and requirements on conformance and interoperability validation processes (certification, badging, etc.) can be added and described in a separate set of documents (e.g. [1]).

There may be a future requirement to make a contribution or to pay a license fee to the O-RAN ALLIANCE for the use of their logos (e.g., “O-RAN”, “OTIC”) or fees for O-RAN qualification services in the event that an OTIC collects a fee.

# 6.4 OTIC Catalogue

The assigned reviewer will create new record (page) with the information about approved OTIC in the list of OTICs (OTIC catalogue) at O-RAN ALLIANCE wiki and at O-RAN ALLIANCE web site. The reviewer will be also assigned as the initial page administrator in the OTIC catalogue. The list of OTICs is maintained by TIFG (via assigned page administrator), and each OTIC needs to keep all published information up to date – any relevant change, which does not require approval (see chapter 6.1 for changes requiring approval), shall be reported to assigned page administrator as soon as possible. The page administrator ensures changes at all relevant places. TIFG co-chairs can re-select the assigned page administrator if needed.

# 6.5 Complaints and Disqualification

O-RAN ALLIANCE encourages each underlying OTIC to resolve internally the complaints and disagreements raised by its partners, clients or observers. O-RAN ALLIANCE has no intent and will not involve in the daily operations of OTIC and resulting normal business operation issues, which could be arbitrated or resolved by legal challenges among the involved parties.

However, when O-RAN ALLIANCE receives the official request with convincing evidence that this guideline has been violated or the following situations have happened, O-RAN ALLIANCE will launch the formal investigation and may request the further information from all underlying parties

• The behaviour of OTIC has seriously undermined the healthy operation of global OTICs. • The OTIC is not following the testing process. For example, OTIC releases detailed test results without the written consent of participant (vendor). • OTIC unable to fulfil its obligations and responsibilities with O-RAN ALLIANCE.

The O-RAN Entity [3] can submit the complaint directly to O-RAN ALLIANCE, while the others can use the contact form at www.o-ran.org for this purpose (as they have no access to O-RAN internal documents and procedures).

The OTIC host(s) has/have the obligation to provide the information requested, as well as full rights to appeal and defend its/their position by providing evidence and supporting materials.

O-RAN ALLIANCE will review the materials submitted by all parties, collect and verify all necessary information, and present the findings and preliminary recommendation to O-RAN ALLIANCE TSC/EC/Board,

1 and follow the legal process defined in the Hosting agreement between the OTIC host and O-RAN ALLIANCE   
2 for the disqualification process.   
3 All participants in OTIC should be acquainted with the complaint rights and procedures (e.g. via OTIC charter,   
4 testing agreements).

# 1 Annex A (normative): OTIC application form

The following application form is used during OTIC qualification process as described in Chapter 6.

# Open Testing and Integration Centre – Application form

# 2 A. GENERAL INFORMATION

<table><tr><td rowspan=1 colspan=1>A1 Full name of OTIC</td><td rowspan=1 colspan=1>A1-1 Proposed O-RAN ALLIANCE designator of OTIC (3-4 letters)</td></tr><tr><td rowspan=1 colspan=1>A2 Link to OTIC web site</td><td rowspan=1 colspan=1>A3 E-mail address</td></tr><tr><td rowspan=1 colspan=2>A4 Correspondence address: street– city– country – postal code</td></tr><tr><td rowspan=1 colspan=2>A5 Description and introduction of OTIC (max 100 words)</td></tr><tr><td rowspan=1 colspan=2>Contact 1</td></tr><tr><td rowspan=1 colspan=1>A7 First name</td><td rowspan=1 colspan=1>A8 Surname</td></tr><tr><td rowspan=1 colspan=1>A9 Telephone number (incl. country code)</td><td rowspan=1 colspan=1>A10 E-mail address</td></tr><tr><td rowspan=1 colspan=2>A11 Responsibilities/duties</td></tr><tr><td rowspan=1 colspan=2>Contact 2</td></tr><tr><td rowspan=1 colspan=1>A12 First name</td><td rowspan=1 colspan=1>A13 Surname</td></tr><tr><td rowspan=1 colspan=1>A14 Telephone number (incl. country code)</td><td rowspan=1 colspan=1>A15 E-mail address</td></tr><tr><td rowspan=1 colspan=2>A16 Responsibilities/duties</td></tr></table>

Note A1: Name of OTIC is unique and English name including word “OTIC”. The proposed OTIC name can be revised and harmonized during the review meeting.

Note A1-1: Proposed O-RAN ALLIANCE designator of OTIC needs to be a unique identifier within O-RAN ALLIANCE and is subject to harmonization.   
The assigned O-RAN ALLIANCE designator will be mentioned in item F4.

# The designed single point of contact for all communication between OTIC and O-RAN ALLIANCE

<table><tr><td>A17 First name</td><td>A18 Surname</td></tr><tr><td>A19 Telephone number (incl. country code)</td><td>A20 E-mail address</td></tr></table>

# 2 OTIC Applicant

<table><tr><td rowspan=1 colspan=2>A21 Full legal name of company</td></tr><tr><td rowspan=1 colspan=2>A22 Correspondence address: street – city– country – postal code</td></tr><tr><td rowspan=1 colspan=2>The point of contact for all communication between applicant and O-RAN ALLIANCE during qualification process</td></tr><tr><td rowspan=1 colspan=1>A23 First name</td><td rowspan=1 colspan=1>A24 Surname</td></tr><tr><td rowspan=1 colspan=1>A25 Telephone number (incl. country code)</td><td rowspan=1 colspan=1>A26 E-mail address</td></tr></table>

3

# 4 B. HOSTS AND PARTNERS

5 The OTIC has at least one host, and no or more partners.

<table><tr><td>B1 Total number of hosts</td><td>B2 Total number of partners</td></tr></table>

6

# 7 Host 1#

<table><tr><td rowspan=1 colspan=2>B3 Full legal name of company</td></tr><tr><td rowspan=1 colspan=2>B4 Correspondence address: street – city– country– postal code</td></tr><tr><td rowspan=1 colspan=2>Contact</td></tr><tr><td rowspan=1 colspan=1>B5 First name</td><td rowspan=1 colspan=1>B6 Surname</td></tr><tr><td rowspan=1 colspan=1>B7 Telephone number (incl. country code)</td><td rowspan=1 colspan=1>B8 E-mail address</td></tr><tr><td rowspan=1 colspan=2>B9 O-RAN membership Member (i.e. mobile network operator)  Contributor □ Academic Contributor</td></tr></table>

Note #: The OTIC has at least one host. The other host(s) is optional. Please copy the table if OTIC has more than one host.

# 1 Partner 1#

<table><tr><td rowspan=1 colspan=2>B10 Full legal name of company</td></tr><tr><td rowspan=1 colspan=2>B11 Correspondence address: street – city– country – postal code</td></tr><tr><td rowspan=1 colspan=2>Contact</td></tr><tr><td rowspan=1 colspan=1>B12 First name</td><td rowspan=1 colspan=1>B13 Surname</td></tr><tr><td rowspan=1 colspan=1>B14 Telephone number (incl. country code)</td><td rowspan=1 colspan=1>B15 E-mail address</td></tr><tr><td rowspan=1 colspan=2>B16 O-RAN membership Member (i.e. mobile network operator) □ Contributor  Academic ContributorNo O-RAN membership</td></tr></table>

Note #: The OTIC has no or more partners. Please leave the table empty if OTIC has no partner, and copy the table if OTIC has more than one partner.

# C. PHYSICAL LAYOUT AND ARCHITECTURE OF LAB(S)

The OTIC has at least one physical lab. An additional information about the lab(s) can be asked during O-RAN ALLIANCE review meeting.

<table><tr><td>C1 Total number of physical labs</td></tr><tr><td>C2 Description of OTiC architecture (max 100 words) - the pictures/photos can be including</td></tr></table>

# 9 Lab 1#

<table><tr><td>C3 Name of lab</td></tr><tr><td>C4 Correspondence address: street – city – country– postal code</td></tr><tr><td></td></tr><tr><td>Pleaseiluritptecticniss  as saif t ftacilf, capability of quickly setting up a separate work area with restricted access based on projects, etc.</td></tr><tr><td></td></tr><tr><td></td></tr></table>

Note #: If OTIC has more than one lab, please copy the table.

# D. SUPPORTED WORK SCOPE AND SERVICES

Please tick the relevant box(es) based on the current OTIC testing capabilities (e.g. based on the available test and measurement equipment in the OTIC today).

<table><tr><td colspan="2">D1 Brief description of testing and other services curretly supported by TiC that can be ofered to cliets text max 1word)</td></tr><tr><td>D2 Is anechoic chamber available in the OTic?</td><td>D3 Is RF shielded chamber/room available in the OTIC?</td></tr><tr><td>Yes, FR1 Yes, FR2 □No Yes, FR1</td><td>□ Yes, FR2 □No</td></tr></table>

6

D4 O-RAN Certificates and Badges that can be awarded by OTIC, as defined in Clause 5.3 [1]   

<table><tr><td rowspan=1 colspan=1>Type of award</td><td rowspan=1 colspan=1>Interface under test</td><td rowspan=1 colspan=1>Device under test</td><td rowspan=1 colspan=1>RAT under test</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# E. SELF-DECLARATION

OTIC applicant declares fulfilment of the requirements for qualification as an OTIC HOST as defined in the Criteria and Guidelines of Open Testing and Integration Centre, dated … …., Version …… .... OTIC applicant also hereby confirms the accuracy of data provided in this application form.

# F. PROCESSING INFORMATION

Please do not fill the following items. The following items will be filled by O-RAN ALLIANCE.

<table><tr><td>F1 Date of application received</td><td>F2 Assigned reviewer</td></tr><tr><td>F3 O-RAN ALLIANCE unique reference ID for this application</td><td>F4 O-RAN ALLANCE designator asigned to OTIC (3-4 letters)</td></tr><tr><td colspan="2">F5 Recommendations and summary from the review meeting, and OTIC applicant statements</td></tr></table>

# 1 Annex B (informative): Guidelines on OTIC application form 2 VOID 3

# 1 Annex C (normative): Hosting agreement

After passing O-RAN ALLIANCE approval process, OTIC applicant will be required to sign the legally binding Hosting agreement with O-RAN ALLIANCE.

2 HOSTING AGREEMENT

3

Between

6 <Company Name>

(“OTIC Host”)

8 <Address>

9 <Address>

10

11 And

O-RAN ALLIANCE e.V.

(“O-RAN ALLIANCE”)

Buschkauler Weg 27

1. O-RAN ALLIANCE has accepted <Company> as OTIC HOST on <DATE>.

2. O-RAN ALLIANCE confirms that OTIC HOST fulfills the requirements for qualification as an OTIC HOST as defined in the Criteria and Guidelines of Open Testing and Integration Centre, dated Version (“Criteria and Guidelines”) and as declared by OTIC Host in its self-declaration (OTIC application form).

3. OTIC HOST as the founder, main contact and main sponsor of OTIC will take full responsibility for all OTIC activities, including the organization as well as all budget and financial flows inside the OTIC.

4. OTIC HOST will in particular:

a. Provide the space (test rooms, server rooms) for conducting of tests and hosting events (incl. IOT and conformance testing, PlugFest, PoC, demo), network connectivity, and test/measurement equipment, tools and services; these services may also be provided by partner(s) contracted by the OTIC HOST;   
b. Guarantee the openness and fairness to any client who has interest in testing its equipment in OTIC;   
c. Guarantee the credibility, confidentiality, openness and vendor-independence of OTIC;   
d. Guarantee that the agreed O-RAN ALLIANCE test procedures (e.g. for certification and badging) are properly followed, and the results are produced in agreed format and with certain level of quality and confidentiality;   
e. Enter into agreements (e.g. participant agreement, testing agreement) with all other participants in OTIC; all agreements shall be in compliance with the criteria and requirements stated in the “Criteria and Guidelines”;   
f. Take all necessary steps (e.g. participation agreement, testing agreement, isolated space) to work towards protecting the intellectual property of each participant in OTIC; to safeguard intellectual property in all situations, e.g., outdoor equipment;   
g. Take all necessary steps to ensure that the used test and measurement equipment and tools are properly calibrated and ready to use;   
h. Allow the detailed results, blueprints, interface profiles, experiences, best practices, knowledges, lesson-learned, adopted processes, etc. to be shared following the confidentiality levels from the agreements;   
i. Regularly present the summary of testing results, experiences, best practices, knowledges, lesson-learned and adopted processes at O-RAN ALLIANCE TIFG meetings (and optionally on request to any other O-RAN ALLIANCE meeting);   
j. Host or multi-host designated representative responds to the request for information or testing results from O-RAN ALLIANCE in a timely manner;   
k. Acts as a mediator trying to resolve any complaint and disagreements inside OTIC raised by its partners, clients or observers; and   
l. Set-up a complaint resolution processes (incl. documentation of resolution of complaint) as described in the “Criteria and Guidelines”.

5. OTIC HOST has flexibility and authorization to negotiate and sign bilateral legal agreements with its partners, clients and observers. At minimum these agreements should include confidentiality, openness and fairness, and rights to share the testing/validation results according to the “Criteria and Guidelines”.

6. OTIC HOST must notify the O-RAN ALLIANCE immediately if any of the requirements for qualification as an OTIC Host as defined in the “Criteria and Guidelines” are not fulfilled any longer.

7. O-RAN ALLIANCE must notify OTIC HOST immediately if any of the requirements for qualification as OTIC HOST as defined in the “Criteria and Guidelines”, are changed.

8. There is no obligation to pay fees to O-RAN ALLIANCE. In case that OTIC HOST collects fees from OTIC participants O-RAN ALLIANCE reserves the right to charge fees for the use of its logos (e.g. “ORAN”, “OTIC” ) and/or fees for O-RAN ALLIANCE qualification services.

9. Having regard to the considerable commercial value of confidential information, OTIC HOST shall keep confidential and secret and not disclose to any third party confidential information. "Confidential Information" means all financial, commercial, technical, operational, staff, management and other information, data and know-how relating to Specifications or Contributions, which may be supplied to or may otherwise come into the possession of the OTIC HOST, whether orally or in writing or in any other form, and which is confidential or proprietary in nature or otherwise expressed by the disclosing party to be confidential.

10. The restrictions on use and disclosure of Confidential Information as described above shall not apply to any information which:

a) is already in the possession of the receiving party prior to its disclosure; b) is or comes into the public domain or otherwise ceases to be of a confidential nature other than as a result of wrongful disclosure hereunder by the receiving party;

c) becomes available to the receiving party on a non-confidential basis from a source other than the Disclosing Party or any of its Associates;   
d) is separately generated by the receiving party who are not privy to the Confidential Information; or   
e) is required to be disclosed by any law or order of a court of competent jurisdiction, recognised stock exchange, governmental department or agency provided that the receiving party (where legally permitted to do so) promptly notifies the OTIC HOST of any such requirement.

11. O-RAN ALLIANCE grants OTIC HOST a royalty-free, non-exclusive, non-transferable, nonsublicensable license to use the registered O-RAN logos (“O-RAN”, “OTIC”) solely for the purpose of this Hosting Agreement. In the event of termination of this Hosting Agreement, OTIC HOST must immediately cease all use of the Logo.

12. OTIC HOST will comply with the rules on data protection as provided by the European General Data Protection Regulation (GDPR) in effect since May 25, 2018.

13. O-RAN ALLIANCE reserves the right to suspend or withdraw OTIC HOST its status as OTIC HOST if it reasonably believes that OTIC is not in compliance with the terms of this Hosting Agreement by following the procedure described in the “Criteria and Guidelines”. The OTIC HOST shall reasonably cooperate with O-RAN ALLIANCE and provide all the requested necessary information and data during investigation of received complaints.

14. O-RAN ALLIANCE and OTIC HOST can terminate this Hosting Agreement without cause at any time with prior written notice of ninety (90) days.

15. Upon termination of this Hosting Agreement OTIC HOST shall on demand promptly return to or destroy all originals of Confidential Information, whether in paper or in electronic form, supplied to it and promptly destroy all copies made of the Confidential Information and all notes, memoranda and other documents or computer files or records prepared by it to the extent of the Confidential Information contained in them, provided that the Receiving Party may keep one copy of Confidential Information for archiving purposes.

16. OTIC HOST agrees and acknowledges that the obligations contained in this Hosting Agreement are legally binding upon it and that they will be construed and interpreted in accordance with German law.

17. The OTIC HOST agrees that any disputes which may rise out of or in connection with this Hosting Agreement or otherwise in connection with its involvement in or with the O-RAN ALLIANCE shall be finally settled under the Rules of Conciliation and Arbitration of the International Chamber of Commerce by one or more arbitrators appointed in accordance with these Rules. The OTIC HOST further agrees that the place of arbitration shall be Geneva/Switzerland and all proceedings in the arbitration shall be in English.

18. The obligations in this Hosting Agreement in respect of confidentiality shall survive termination of this Hosting Agreement howsoever arising.

Signatures:

Company Name (“OTIC Host”): . (Name and Date)

O-RAN ALLIANCE e.V.: … . (Name and Date)

# 1 Annex:

# 2 Change history/Change request (history)

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>2020.07.02</td><td rowspan=1 colspan=1>01.00</td><td rowspan=1 colspan=1>First published version</td></tr><tr><td rowspan=1 colspan=1>2020.11.07</td><td rowspan=1 colspan=1>02.00</td><td rowspan=1 colspan=1>The details of OTIC qualification process have been added in Chapter 4. The OTICapplication form has been added in Annex A.</td></tr><tr><td rowspan=1 colspan=1>2021.05.07</td><td rowspan=1 colspan=1>03.00</td><td rowspan=1 colspan=1>The format of document has been changed from technical specification to processdocument. The OTIC application approval process has been updated in Chapter 4. TheHosting agreement has been added in Annex C. The OTIC application form in Annex Ahas been extended by Self-declaration.</td></tr><tr><td rowspan=1 colspan=1>2022.06.01</td><td rowspan=1 colspan=1>04.00</td><td rowspan=1 colspan=1>Legal review of the document. The guidelines on mapping of OTIC testing capabilitiesand services to OTIC application form have been added to Annex B. The OTICapplication form in Annex A has been updated. The format and structure of document hasbeen updated according to the latest O-RAN templates.</td></tr><tr><td rowspan=1 colspan=1>2023.03.01</td><td rowspan=1 colspan=1>05.00</td><td rowspan=1 colspan=1>Harmonization of OTIC names – adding requirements on OTIC names and recommendednaming convention (scheme) in chapter 6.1. The changes which require additional O-RAN approval have been listed in chapter 6.1. Limitation of 2 months on duration of OTICreview process has been added to chapter 6.2. The OTIC application form (Annex A) hasbeen updated accordingly, and new item for O-RAN ALLIANCE designator has beenadded.</td></tr><tr><td rowspan=1 colspan=1>2025.01.15</td><td rowspan=1 colspan=1>06.00</td><td rowspan=1 colspan=1>Updated and simplified OTIC application form in Annex A. Alignment of terminology withO-RAN Working procedures and O-RAN Constitution. Clarification of who can be OTIChost, including O-RAN Contributors as well as O-RAN Academic Contributors.</td></tr></table>