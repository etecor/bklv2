# bklv2
bklv2 is a python library for [Backlog API version 2](http://developer.nulab-inc.com/ja/docs/backlog).

## Install
~~~~
$ pip install bklv2
~~~~

## How to use
~~~~python
import bklv2

# make object.
bklv2api = bklv2.api( hostname="https://<spacename>.backlog.jp", apikey="apikey" )

# API method
# return : dict
prj = bklv2api.addProject( name = "testproject",
                           key = "TESTPROJECT",
                           chartEnabled = False,
                           subtaskingEnabled = False,
                           textFormattingRule = "markdown" )

print( type(prj) )          # >> <class 'dict'>
print( prj["projectKey"] )  # >> TESTPROJECT

# API method ( file-downloader )
# return : output file path
fp = bklv2api.getProjectIcon( projectIdOrKey=prj["id"]) )

print( type(fp) )           # >> <class 'str'>
print( fp )                 # >> ./space_img.png
~~~~

## API methods
| method | description |
|:------:|:------------|
| [addAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/add-attachment) | Posts an attachment file for issue or wiki. Returns id of the attachment file.|
| [addCategory](https://developer.nulab-inc.com/docs/backlog/api/2/add-category) | Adds new Category to the project.|
| [addComment](https://developer.nulab-inc.com/docs/backlog/api/2/add-comment) | Adds a comment to the issue.|
| [addCommentNotification](https://developer.nulab-inc.com/docs/backlog/api/2/add-comment-notification) | Adds notifications to the comment.|
| [addCustomfeild](https://developer.nulab-inc.com/docs/backlog/api/2/add-customfield) | Adds new Custom Field to the project.|
| [addCustomfieldItem](https://developer.nulab-inc.com/docs/backlog/api/2/add-customfield-item) | Adds new list item for list type custom field.|
| [addGroup](https://developer.nulab-inc.com/docs/backlog/api/2/add-group) | Adds new group.|
| [addIssue](https://developer.nulab-inc.com/docs/backlog/api/2/add-issue) | Adds new issue.|
| [addIssueSharedfile](https://developer.nulab-inc.com/docs/backlog/api/2/add-comment-notification) | Adds notifications to the comment.|
| [addIssueType](https://developer.nulab-inc.com/docs/backlog/api/2/add-issuetype) | Adds new Issue Type to the project.|
| [addProject](https://developer.nulab-inc.com/docs/backlog/api/2/add-project) | Adds new project.|
| [addProjectAdministrator](https://developer.nulab-inc.com/docs/backlog/api/2/add-project-administrator) | Adds "Project Administrator" role to user|
| [addProjectUser](https://developer.nulab-inc.com/docs/backlog/api/2/add-project-user) | Adds user to list of project members.|
| [addPullRequest](https://developer.nulab-inc.com/docs/backlog/api/2/add-pull-request) | Adds pull requests.|
| [addPullRequestComment](https://developer.nulab-inc.com/docs/backlog/api/2/add-pull-request-comment) | Adds comments on pull requests.|
| [addStar](https://developer.nulab-inc.com/docs/backlog/api/2/add-star) | Adds star.|
| [addUser](https://developer.nulab-inc.com/docs/backlog/api/2/add-user) | Adds new user to the space.|
| [addVersion](https://developer.nulab-inc.com/docs/backlog/api/2/add-version) | Adds new Version/Milestone to the project.|
| [addWatching](https://developer.nulab-inc.com/docs/backlog/api/2/get-watching) | Returns the information about a watching.|
| [addWebhook](https://developer.nulab-inc.com/docs/backlog/api/2/add-webhook) | Adds new webhook.|
| [addWiki](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-tags) | Returns list of tags that are used in the project.|
| [addWikiAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/add-wiki-attachment) | Attaches file to Wiki|
| [addWikiSharedfile](https://developer.nulab-inc.com/docs/backlog/api/2/add-wiki-sharedfile) | Links Shared Files to Wiki.|
| [checkedWatchings](https://developer.nulab-inc.com/docs/backlog/api/2/checked-watchings) | Mark watching list status as checked.|
| [countWatching](https://developer.nulab-inc.com/docs/backlog/api/2/count-watching) | Returns the number of your watching issues.|
| [deleteCategory](https://developer.nulab-inc.com/docs/backlog/api/2/delete-category) | Deletes Category.|
| [deleteCustomfeild](https://developer.nulab-inc.com/docs/backlog/api/2/delete-customfield) | Deletes Custom Field.|
| [deleteCustomfieldItem](https://developer.nulab-inc.com/docs/backlog/api/2/delete-customfield-item) | Deletes list item for list type custom field.|
| [deleteGroup](https://developer.nulab-inc.com/docs/backlog/api/2/delete-group) | Deletes group.|
| [deleteIssue](https://developer.nulab-inc.com/docs/backlog/api/2/delete-issue) | Deletes issue.|
| [deleteIssueAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/delete-issue-attachment) | Deletes an attachment of issue.|
| [deleteIssueSharedfile](https://developer.nulab-inc.com/docs/backlog/api/2/delete-issue-sharedfile) | Removes link to shared file from issue.|
| [deleteIssueType](https://developer.nulab-inc.com/docs/backlog/api/2/delete-issuetype) | Deletes Issue Type.|
| [deleteProject](https://developer.nulab-inc.com/docs/backlog/api/2/delete-project) | Deletes project.|
| [deleteProjectAdministrator](https://developer.nulab-inc.com/docs/backlog/api/2/delete-project-administrator) | Removes Project Administrator role from user|
| [deleteProjectUser](https://developer.nulab-inc.com/docs/backlog/api/2/delete-project-user) | Removes user from list project members.|
| [deletePullRequestAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/delete-pull-request-attachment) | Deletes attached files on pull requests.|
| [deleteUser](https://developer.nulab-inc.com/docs/backlog/api/2/delete-user) | Deletes user from the space.|
| [deleteVersion](https://developer.nulab-inc.com/docs/backlog/api/2/delete-version) | Deletes Version.|
| [deleteWatching](https://developer.nulab-inc.com/docs/backlog/api/2/delete-watching) | Deletes a own watching.|
| [deleteWebhook](https://developer.nulab-inc.com/docs/backlog/api/2/delete-webhook) | Deletes webhook.|
| [deleteWiki](https://developer.nulab-inc.com/docs/backlog/api/2/delete-wiki) | Deletes Wiki page.|
| [deleteWikiAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/delete-wiki-attachment) | Removes files attached to Wiki.|
| [deleteWikiSharedfile](https://developer.nulab-inc.com/docs/backlog/api/2/delete-wiki-sharedfile) | Removes link to shared file from Wiki.|
| [getActivities](https://developer.nulab-inc.com/docs/backlog/api/2/get-activities) | Returns recent updates in your space.|
| [getCategories](https://developer.nulab-inc.com/docs/backlog/api/2/get-categories) | Returns list of Categories in the project.|
| [getComment](https://developer.nulab-inc.com/docs/backlog/api/2/get-comment) | Returns information about comment.|
| [getCommentNotifications](https://developer.nulab-inc.com/docs/backlog/api/2/get-comment-notifications) | Returns the list of comment notifications.|
| [getComments](https://developer.nulab-inc.com/docs/backlog/api/2/get-comments) | Returns list of comments in issue.|
| [getCommentsCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-comments-count) | Returns number of comments in issue.|
| [getCustomfeilds](https://developer.nulab-inc.com/docs/backlog/api/2/get-customfields) | Returns list of Custom Fields in the project.|
| [getGitRepositories](https://developer.nulab-inc.com/docs/backlog/api/2/get-git-repositories) | Returns list of Git repositories.|
| [getGitRepository](https://developer.nulab-inc.com/docs/backlog/api/2/get-git-repository) | Returns Git repository.|
| [getGroup](https://developer.nulab-inc.com/docs/backlog/api/2/get-group) | Returns information about group.|
| [getGroups](https://developer.nulab-inc.com/docs/backlog/api/2/get-groups) | Returns list of groups.|
| [getIssue](https://developer.nulab-inc.com/docs/backlog/api/2/get-issue) | Returns information about issue.|
| [getIssueAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/get-issue-attachment) | Downloads issue's attachment file.|
| [getIssueAttachments](https://developer.nulab-inc.com/docs/backlog/api/2/get-issue-attachments) | Returns the list of issue attachments.|
| [getIssueSharedfiles](https://developer.nulab-inc.com/docs/backlog/api/2/get-issue-sharedfiles) | Returns the list of linked Shared Files to issues.|
| [getIssueTypes](https://developer.nulab-inc.com/docs/backlog/api/2/get-issuetypes) | Returns list of Issue Types in the project.|
| [getIssues](https://developer.nulab-inc.com/docs/backlog/api/2/get-issues) | Returns list of issues.|
| [getIssuesCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-issues-count) | Returns number of issues.|
| [getMyselfUser](https://developer.nulab-inc.com/docs/backlog/api/2/get-myself-user) | Returns own information about user.|
| [getNotification](https://developer.nulab-inc.com/docs/backlog/api/2/get-notifications) | Returns own notifications.|
| [getNotificationCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-notifications-count) | Returns number of Notifications.|
| [getPriorities](https://developer.nulab-inc.com/docs/backlog/api/2/get-priorities) | Returns list of priorities.|
| [getProject](https://developer.nulab-inc.com/docs/backlog/api/2/get-project) | Returns information about project.|
| [getProjectActivities](https://developer.nulab-inc.com/docs/backlog/api/2/get-project-activities) | Returns recent update in the project.|
| [getProjectAdministrators](https://developer.nulab-inc.com/docs/backlog/api/2/get-project-adminnistrators) | Returns list of users who has Project Administrator role|
| [getProjectDiskUsage](https://developer.nulab-inc.com/docs/backlog/api/2/get-project-diskusage) | Returns information about project disk usage.|
| [getProjectIcon](https://developer.nulab-inc.com/docs/backlog/api/2/get-project-icon) | Downloads project icon.|
| [getProjectUsers](https://developer.nulab-inc.com/docs/backlog/api/2/get-project-users) | Returns list of project members.|
| [getProjects](https://developer.nulab-inc.com/docs/backlog/api/2/get-projects) | Returns list of projects.|
| [getPullRequest](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-request) | Returns pull reuqest.|
| [getPullRequestAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-request-attachment) | Downloads attached files on pull requests.|
| [getPullRequestAttachments](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-request-attachments) | Returns list of attached files on pull requests.|
| [getPullRequestComment](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-request-comment) | Returns list of pull request comments.|
| [getPullRequestCommentsCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-request-comments-count) | Returns number of comments on pull requests.|
| [getPullRequests](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-requests) | Returns list of pull requests.|
| [getPullRequestsCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-requests-count) | Returns number of pull requests.|
| [getResolutions](https://developer.nulab-inc.com/docs/backlog/api/2/get-resolutions) | Returns list of resolutions.|
| [getSharedfile](https://developer.nulab-inc.com/docs/backlog/api/2/get-sharedfile) | Downloads the file.|
| [getSharedfiles](https://developer.nulab-inc.com/docs/backlog/api/2/get-sharedfiles) | Gets list of Shared Files.|
| [getSpace](https://developer.nulab-inc.com/docs/backlog/api/2/get-space) | Returns information about your space.|
| [getSpaceDiskUsage](https://developer.nulab-inc.com/docs/backlog/api/2/get-space-diskusage) | Returns information about space disk usage.|
| [getSpaceImage](https://developer.nulab-inc.com/docs/backlog/api/2/get-space-image) | Returns logo image of your space.|
| [getSpaceNotification](https://developer.nulab-inc.com/docs/backlog/api/2/get-space-notification) | Returns space notification.|
| [getStatus](https://developer.nulab-inc.com/docs/backlog/api/2/get-status) | Returns list of statuses.|
| [getUser](https://developer.nulab-inc.com/docs/backlog/api/2/get-user) | Returns information about user.|
| [getUserActivities](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-activities) | Returns user's recent updates|
| [getUserIcon](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-icon) | Downloads user icon.|
| [getUserRecentlyViewedIssues](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-recentlyviewedissues) | Returns list of issues which the user viewed recently.|
| [getUserRecentlyViewedProjects](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-recentlyviewedprojects) | Returns list of projects which the user viewed recently.|
| [getUserRecentlyViewedWikis](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-recentlyviewedwikis) | Returns list of Wikis which the user viewed recently.|
| [getUserStars](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-stars) | Returns the list of stars that user received.|
| [getUserStarsCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-user-stars-count) | Returns number of stars that user received.|
| [getUsers](https://developer.nulab-inc.com/docs/backlog/api/2/get-users) | Returns list of users in your space.|
| [getVersions](https://developer.nulab-inc.com/docs/backlog/api/2/get-versions) | Returns list of Versions/Milestones in the project.|
| [getWatching](https://developer.nulab-inc.com/docs/backlog/api/2/get-watching) | Returns the information about a watching.|
| [getWatchingList](https://developer.nulab-inc.com/docs/backlog/api/2/get-watching-list) | Returns list of your watching issues.|
| [getWebhook](https://developer.nulab-inc.com/docs/backlog/api/2/get-webhook) | Returns information about webhook.|
| [getWebhooks](https://developer.nulab-inc.com/docs/backlog/api/2/get-webhooks) | Returns list of webhooks.|
| [getWiki](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki) | Returns information about Wiki page.|
| [getWikiAttachment](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-attachment) | Downloads Wiki page's attachment file.|
| [getWikiAttachments](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-attachments) | Gets list of files attached to Wiki.|
| [getWikiHistory](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-history) | Returns history of Wiki page.|
| [getWikiSharedfiles](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-sharedfiles) | Returns the list of Shared Files on Wiki.|
| [getWikiStars](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-stars) | Returns list of stars received on the Wiki page.|
| [getWikiTags](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-tags) | Returns list of tags that are used in the project.|
| [getWikis](https://developer.nulab-inc.com/docs/backlog/api/2/get-wikis) | Returns list of Wiki pages.|
| [getWikisCount](https://developer.nulab-inc.com/docs/backlog/api/2/get-wikis-count) | Returns number of Wiki pages.|
| [markAsreadNotification](https://developer.nulab-inc.com/docs/backlog/api/2/markasread-notification) | Changes notifications read.|
| [markAsreadNotifications](https://developer.nulab-inc.com/docs/backlog/api/2/get-wiki-stars) | Returns list of stars received on the Wiki page.|
| [readWatching](https://developer.nulab-inc.com/docs/backlog/api/2/read-watching) | Mark a watching as read.|
| [updateCategory](https://developer.nulab-inc.com/docs/backlog/api/2/update-category) | Updates information about Category.|
| [updateComment](https://developer.nulab-inc.com/docs/backlog/api/2/update-comment) | Updates content of comment.|
| [updateCustomfeild](https://developer.nulab-inc.com/docs/backlog/api/2/update-customfield) | Updates Custom Field.|
| [updateCustomfieldItem](https://developer.nulab-inc.com/docs/backlog/api/2/update-customfield-item) | Updates list item for list type custom field.|
| [updateGroup](https://developer.nulab-inc.com/docs/backlog/api/2/update-group) | Updates information about group.|
| [updateIssue](https://developer.nulab-inc.com/docs/backlog/api/2/update-issue) | Updates information about issue.|
| [updateIssueType](https://developer.nulab-inc.com/docs/backlog/api/2/update-issuetype) | Updates information about Issue Type.|
| [updateProject](https://developer.nulab-inc.com/docs/backlog/api/2/update-project) | Updates information about project.|
| [updatePullRequest](https://developer.nulab-inc.com/docs/backlog/api/2/update-pull-request) | Updates pull requests.|
| [updatePullRequestComment](https://developer.nulab-inc.com/docs/backlog/api/2/get-pull-request-comment) | Returns list of pull request comments.|
| [updateSpaceNotification](https://developer.nulab-inc.com/docs/backlog/api/2/update-space-notification) | Updates space notification.|
| [updateUser](https://developer.nulab-inc.com/docs/backlog/api/2/update-user) | Updates information about user.|
| [updateVersion](https://developer.nulab-inc.com/docs/backlog/api/2/update-version) | Updates information about Version/Milestone.|
| [updateWatching](https://developer.nulab-inc.com/docs/backlog/api/2/update-watching) | Updates a watching. User can update own note.|
| [updateWebhook](https://developer.nulab-inc.com/docs/backlog/api/2/update-webhook) | Updates information about webhook.|
| [updateWiki](https://developer.nulab-inc.com/docs/backlog/api/2/update-wiki) | Updates information about Wiki page.|
