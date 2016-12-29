# VolunteerCoordinator
Management of volunteer scheduling


<b>Core Functionality<\b>

Store information about each volunteer
<p>Allow for creation of assignments/jobs
<p>Allow coordinators and/or volunteers to assign volunteers to assignments/jobs
<p>Allow volunteers to log in to see schedules and commit to “shifts”

<b>Key Features

Track minimum/maximum number of volunteers per assignment
<p>Allow recurring schedules, both in terms of creation on calendar and in terms of volunteer assignment
<p>Track training/certifications volunteers may have or assignments/jobs may need
<p>Send notifications if an assignment/job is understaffed.
<p>Allow creation of reports
<p>Track when volunteers’ trainings or certifications were obtained and if/when they will need renewal
<p>Track each volunteer’s service history based on log in/log out functions after confirmation/editing by administrator.
<p>Provide simple graphic such that volunteers can see appropriate open assignments at a glance; clicking the graphic takes volunteer to schedule page for that day.
<p>Allow volunteers to cancel a shift up to a user-defined amount of time prior to the shift.
<p>After that time, allow the software to warn the volunteer that the volunteer is still expected to show up, but offer to look for a replacement (email coordinators and/or volunteers who could fill the slot).
<p>By default, calendar view should show all jobs that the logged-in user is qualified for.
<p>Dropdown menu or checkboxes should allow user to show all jobs (qualified or not) or to show only a subset of jobs the user is qualified for.


<b> Roles/Access Levels

<p>Owner: has complete access to all functions of a particular organization’s information.
<p>Administrator: has complete access to all information but may not be able to add other administrators and may not be able to change certain information. All administrators should have the same level of access.
<p>Coordinator: has limited access to information. There may be different categories of coordinators with different levels of access. Can place volunteers on the schedule (perhaps only a limited group which are assigned to the coordinator). May be able to create/change/delete assignments/jobs within a certain category.
<p>Volunteer: has access only to the volunteer’s own schedule information. May be able to see which volunteers are scheduled at which times, but will not be able to change any information relating to any other individual. May only be able to see how many open slots there are.

<b>Nice-to-have Features

<p>Set up automatic reports, such as “volunteers who have been inactive for X days”
<p>Similar to above; ability to create alerts based on “parameter x” is “>, =, <” “trigger level’
<p>User proposed log-in edits confirmed by coordinator
<p>Filter on calendar page for only showing category eg zoo, aquarium, scion
<p>Monthly cumulative service (month to date) on cal page
<p>Integrate with school system API for honors hours
<p>Coordinator and Administrator have ability to push simple messages to users; maybe to display when they open the site rather than email; maybe either/or/both?
<p>Allow users to offer swap; “I would like to get out of this commitment, can anyone cover my scheduled shift?”

<b>Licensing
<p>Probably GPL. Maybe LGPL, but I (CAM) don’t really see any reason to prefer LGPL.

<b>Documentation
<p>Find a free wiki service to host documentation?
<p>Resources
<p>https://www.smashingmagazine.com/2013/01/starting-an-open-source-project/
<p>https://www.airpair.com/python/posts/django-flask-pyramid


<b>Code/DB Structure

<p>DB Structure
<p>User table, from django, for login
<p>Userprofile table, custom-created
<p>Role field: serialized dictionary with key:value pairs of organization:role (eg, [Science Center pk]:”Coordinator”
<p>Organization table
<p>Some method of holding organization’s preferences?
<p>Jobs table
<p>Foreign key to point to the organization which the job is for (cannot be null)
<p>Foreign key to point to the user scheduled for the job (null = unfilled)
<p>StartTime = DateTimeField
<p>EndTime = DateTimeField
<p>TBD method of tracking training requirements


<b>possible names
VolunSharing
VolCharley
VolGroup.org
volGroups.com or Volgroups.org

