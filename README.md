# awmsc2022
Wednesday Assignment M.Sc. Group 2021-2022

## Table of Contents

  * [Table of Contents](#table-of-contents)
  * [Preamble](#preamble)
    + [Scrum Master](#scrum-master)
    + [Product Owner](#product-owner)
  * [Project Deadline](#project-deadline)
  * [Project Specification](#project-specification)
  * [Considerations](#considerations)
  * [Useful Links](#useful-links)
  * [Risk Register](#risk-register)
  * [Tenants of Design](#tenants-of-design)
  * [Social Contract](#social-contract)
  * [Branching Strategy](#branching-strategy)

## Preamble

This is the online repository for the "Wicked Adventures". Summary of project requirements should go here.


Our product will be delivered using an Agile methodology that embraces the DevOps culture. Please note that our culture embraces change and these documents are treated as living, breathing artefacts that will be continuously updated.

### Scrum Master
Member Name							Date
-----------							----
Sreejith Jayasree Purushothaman				13/12/2021 to 19/12/2021
Varnit Rohilla						20/12/2021 to 26/12/2021
Snehal Shirsath						27/12/2021 to 02/01/2022
Anup Jacob						03/01/2022 to 09/01/2022
Muhammed Shafeeq					10/01/2022 to 16/01/2022
Snehal Khairnar						17/01/2022 to 23/01/2022
Sreejith Jayasree Purushothaman				24/01/2022 to 30/01/2022
Snehal Shirsath						31/01/2022 to 06/02/2022
Anup Jacob						07/02/2022 to 13/02/2022
Snehal Khairnar						14/02/2022 to 20/02/2022
Varnit Rohilla						21/02/2022 to 27/02/2022
Sreejith Jayasree Purushothaman				28/02/2022 to 06/03/2022
Snehal Shirsath						07/03/2022 to 13/03/2022
Muhammed Shafeeq					14/03/2022 to 20/03/2022
Snehal Khairnar						21/03/2021 to 27/03/2021
Snehal Shirsath						28/03/2022 to 03/04/2022

### Product Owner
Member Name							Date
-----------							----
Anup Jacob						13/12/2021 to 19/12/2021
Snehal Khairnar						20/12/2021 to 26/12/2021
Muhammed Shafeeq					27/12/2021 to 02/01/2022
Sreejith Jayasree Purushothaman				03/01/2022 to 09/01/2022
Varnit Rohilla						10/01/2022 to 16/01/2022
Snehal Shirsath						17/01/2022 to 23/01/2022
Muhammed Shafeeq					24/01/2022 to 30/01/2022
Anup Jacob						31/01/2022 to 06/02/2022
Snehal Khairnar						07/02/2022 to 13/02/2022
Sreejith Jayasree Purushothaman				14/02/2022 to 20/02/2022
Snehal Shirsath						21/02/2022 to 27/02/2022
Varnit Rohilla						28/02/2022 to 06/03/2022
Muhammed Shafeeq					07/03/2022 to 13/03/2022
Varnit Rohilla						14/03/2022 to 20/03/2022
Anup Jacob						21/03/2021 to 27/03/2021
Sreejith Jayasree Purushothaman				28/03/2022 to 03/04/2022

### Team Members
Snehal Shirsath
Snehal Khairnar
Muhammed Shafeeq Thottathil
Varnit Rohilla
Anup Jacob
Sreejith Jayasree Purushothaman

Lecturer: Paul Greaney

  
### Project Deadline
08/04/2022 23:59
Refer to Blackboard for the most up to date information on deadlines.
  
## Project Specification  
<!-- <team must agree specifications here - below are samples for discussion purposes>     -->
    Clean and simple design
    User access levels (client, administrator)
    Includes at least one self developed api and one webservice
    To be run over Amazon AWS

    Frameworks
    Database
    Database persistence technology
    Define the buisness Requirements
    Named queries and database triggers for security
    Regex for cleansing and validation of data before sending to the database.

## Useful Links

    DC Slack: https://app.slack.com/client/T84LE6L6R/C02PELNHHD4
    Jira: https://weekendadventure.atlassian.net/jira/software/projects/WA/boards/1
    GitHub: https://github.com/devopslecturer/awmsc2022.git
    Project close out presentation: 

### More Information
For more information visit our other sections
| Section  | Description  |
| --- | --- |
| Process  | Describes the companies process  |
| Project Log  | Log of project activities  |
| Costings  | Overview of the project cost  |
|  Architecture | Outlines the architecture  |
| Environments  | Overview of the environment set-up  |
| DR Plan  | Disaster Recovery Plan and procedures  |
| Requirements  | Overview of the requirements for the project  |
| SLAs  | Service level agreements  |
| Risk Management  | How we manage risk  |
| Security  | Overview of security  |
| Project Log  | Team log for the project  |

## Risk Register

These are the current Risks on the project, re-aligned on a weekly basis

    Infrastructure proving to be a real problem, may block being able to release software
    Team is finding itself to be running short on time due to other work and study commitments
    No PO feedback on software
    Unknown technology choices has led to a lot of upskilling required
    Changing / ambiguous requirements
    Talk of the company being bought out has raised concerns
    Lack of rights for toolsets chosen has hindered progress and ability to deliver

## Tenants of Design
<pick from the sample sections below and add your own>
    Dedication to clean, secure, performant and self documented code
        code Frameworks used
        code coverage tool used
        Secure code: Regex for cleansing and validation, Named queries and database triggers
        performance testing tool to be used
    Documentation / code commenting (javadoc)/separate branch
    Datastore for persistance
    Testing:
        Unit testing
        integretation testing
        UA
    Environments:
        staging and production
        tight configuration management for consistency and reproducibility
        automated creation and deployments
        integrated and automated pipeline (commit -> test -> deploy)
    Github version control:
        branches used
        version/release management
    Agile project management methods/principles (jira)

## Social Contract

### Meetings

    Stand-ups will occur on Wednesday at 10.30 AM and Thursday at 2.30 PM.
    The order that people give their updates will be based on <<define the order>> of those present at the meeting.
    Updates will be in the form: What I've done, What I plan to do, Impediments
    Sprint planning will occur every other Wednesday at 11.00 AM.
    Please add and update items within Jira prior to the sprint planning session.
    Sprint retro will occur once a month, <<Date and time>>.
    The order that people present their sprint retro updates will be based on alphabetical order of those present at the meeting.
    Points raised in the sprint retro will be noted and posted on the slack channel by the Scrum Master.
    Backlog refinement?
    Task estimation will be done using <<what method>>. 
    Come prepared to meetings.
    Be on time for Stand Ups and meetings.
    Mobile phones on silent.
    Everyone has equal voice and valuable contribution.
    Keep your language and tone professional at all times.
    Be honest.

### Communication

    Slack is the preferred method of communication.
    If a demonstration is required use Slack, record the session and upload to the Slack channel.
    No Slack communications between "8 PM to 8 AM ".
    Raise a problem as soon as you see it.
    Respect each other and understand differences in knowledge.
    All team documents are to be created using Markdown language and shared on GitHub.
    There are no silly questions, if you don’t understand, ask.
    Share success stories.
    Focus on the positives.
    Don’t make assumptions.
    Don’t interrupt and cut another person off while they are talking.
    Listen when someone is talking, don’t interject.
    Zero tolerance for bullying.
    Communication in this order: 
	Paul Greaney > Ruth Lennon > [Team Members] 
    Agile way of working.
    If are assigned a job, take ownership of it and keep it up to date.
    Stick to your agreed working patterns. Let the team know when you are late or going early.
    Keep JIRA board updated at all times.
    Update the Scrum Board as you progress the story i.e. don’t update at standup.
    Don't be afraid to ask for help.
    Don't be afraid to give constructive critism, as long as it is constructive.
    Solve roadblocks within the team. If the impediment can’t be solved within the team then give it to the Scrum Master.

## Other

    Sprints will start <<check with lecturer>>.
    The Scrum Master role rotates each week, the schedule is available on the on the process section
    The Product Owner role rotates each week, the schedule is available on the on the process section
    Jira will be used for task management and planning.
    Each member of the team will work one or two per week, unless they are on vacation.

## Branching Strategy
Master Branch
	
	-Develop branch
	
		-Login-Register branch
	
		-Database branch
	
	
	-Flask_Initial_Setup
	
		-...
	
	-Test Branch
	
	-Prod Branch

### Estimating Story Points Within Jira

The teams team's velocity is calculated by dividing the the number of points burned each sprint divided by no of sprints. The Velocity chart from Jira (below) is used for this calculation.

The teams current story point velocity is "<Choose the number!>".
