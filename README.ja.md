# bklv2
bklv2 is a python library for [Backlog API version 2](https://developer.nulab-inc.com/docs/backlog/)
[(JP)](http://developer.nulab-inc.com/ja/docs/backlog).

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
| [getSpace](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-space) | スペースの情報を取得します。 |
| [getRecentUpdates](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-recent-updates) | スペース上で行われた最近の更新の一覧を取得します。 |
| [getSpaceLogo](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-space-logo) | スペースのアイコン画像を取得します。 |
| [getSpaceNotification](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-space-notification) | スペースのお知らせの情報を取得します。 |
| [updateSpaceNotification](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-space-notification) | スペースのお知らせの情報を更新します。 |
| [getSpaceDiskUsage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-space-disk-usage) | スペースの容量使用状況の情報を取得します。 |
| [postAttachmentFile](https://developer.nulab-inc.com/ja/docs/backlog/api/2/post-attachment-file) | 課題、コメントまたはWikiに添付するファイルを送信し、添付ファイルに発行されたIDを取得します。送信されたファイルは添付された後に削除されます。また添付されなかった場合は1時間後に削除されます。 |
| [getUserList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-user-list) | スペースのユーザーの一覧を取得します。“lang” はユーザが言語設定をしていない場合は、null になります。 |
| [getUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-user) | ユーザー情報を取得します。“lang” はユーザが言語設定をしていない場合は、null になります。 |
| [addUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-user) | スペースに新しいユーザーを追加します。プロジェクト管理者は管理者権限のユーザを追加することは出来ません。backlog.com のスペースではこのAPIを利用できません。 |
| [updateUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-user) | ユーザーの情報を更新します。backlog.com のスペースではこのAPIを利用できません。 |
| [deleteUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-user) | ユーザーをスペースから削除します。backlog.com のスペースではこのAPIを利用できません。 |
| [getOwnUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-own-user) | APIとの認証に使用しているユーザーの情報を取得します。 |
| [getUserIcon](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-user-icon) | ユーザーのアイコン画像を取得します。 |
| [getUserRecentUpdates](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-user-recent-updates) | ユーザーの最近の活動の一覧を取得します。 |
| [getReceivedStarList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-received-star-list) | ユーザーの受け取ったスターの一覧を取得します。 |
| [countUserReceivedStars](https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-user-received-stars) | ユーザーの受け取ったスターの数を取得します。 |
| [getListOfRecentlyViewedIssues](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-recently-viewed-issues) | APIとの認証に使用しているユーザーが最近見た課題の一覧を取得します。 |
| [getListOfRecentlyViewedProjects](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-recently-viewed-projects) | APIとの認証に使用しているユーザーが最近見たプロジェクトの一覧を取得します。 |
| [getListOfRecentlyViewedWikis](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-recently-viewed-wikis) | APIとの認証に使用しているユーザーが最近見たWikiの一覧を取得します。 |
| [getListOfGroups](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-groups) | グループの一覧を取得します。 |
| [addGroup](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-group) | グループを追加します。backlog.com のスペースではこのAPIを利用できません。 |
| [getGroup](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-group) | グループの情報を取得します。 |
| [updateGroup](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-group) | グループの情報を更新します。backlog.com のスペースではこのAPIを利用できません。 |
| [deleteGroup](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-group) | グループを削除します。backlog.com のスペースではこのAPIを利用できません。 |
| [getStatusList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-status-list) | 課題に設定できる状態の一覧を取得します。 |
| [getResolutionList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-resolution-list) | 課題に設定できる完了理由の一覧を取得します。 |
| [getPriorityList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-priority-list) | 課題に設定できる優先度の一覧を取得します。 |
| [getProjectList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-list) | プロジェクトの一覧を取得します。 |
| [addProject](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-project) | 新しいプロジェクトを追加します。 |
| [getProject](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project) | プロジェクトの情報を取得します。 |
| [updateProject](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-project) | プロジェクトの情報を更新します。 |
| [deleteProject](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-project) | プロジェクトを削除します。 |
| [getProjectIcon](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-icon) | プロジェクトのアイコン画像を取得します。 |
| [getProjectRecentUpdates](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-recent-updates) | プロジェクト上の最近の活動の一覧を取得します。 |
| [addProjectUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-project-user) | プロジェクトにユーザーを追加します。 |
| [getProjectUserList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-user-list) | プロジェクトのユーザーの一覧を取得します。 |
| [deleteProjectUser](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-project-user) | プロジェクトからユーザーを削除します。 |
| [addProjectAdministrator](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-project-administrator) | プロジェクトユーザーにプロジェクト管理者権限を追加します。 |
| [getListOfProjectAdministrators](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-project-administrators) | プロジェクト管理者に設定されているユーザーの一覧を取得します。 |
| [deleteProjectAdministrator](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-project-administrator) | プロジェクトユーザーからプロジェクト管理者権限を削除します。 |
| [getIssueTypeList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-type-list) | プロジェクトに登録されている種別の一覧を返します。 |
| [addIssueType](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-issue-type) | プロジェクトに種別を追加します。 |
| [updateIssueType](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-issue-type) | 種別の情報を更新します。 |
| [deleteIssueType](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-issue-type) | プロジェクトから種別を削除します。 |
| [getCategoryList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-category-list) | プロジェクトに登録されているカテゴリーの一覧を返します。 |
| [addCategory](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-category) | プロジェクトにカテゴリーを追加します。 |
| [updateCategory](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-category) | カテゴリーの情報を更新します。 |
| [deleteCategory](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-category) | カテゴリーを削除します。 |
| [getVersionMilestoneList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-version-milestone-list) | プロジェクトに登録されているバージョン(マイルストーン)の一覧を返します。 |
| [addVersionMilestone](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-version-milestone) | プロジェクトにバージョン(マイルストーン)を追加します。 |
| [updateVersionMilestone](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-version-milestone) | バージョン(マイルストーン)の情報を更新します。 |
| [deleteVersion](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-version) | バージョン(マイルストーン)を削除します。 |
| [getCustomFieldList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-custom-field-list) | プロジェクトに登録されているカスタム属性の一覧を取得します。 |
| [addCustomField](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-custom-field) | プロジェクトに新しいカスタム属性を追加します。 |
| [updateCustomField](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-custom-field) | カスタム属性を更新します。 |
| [deleteCustomField](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-custom-field) | カスタム属性を削除します。 |
| [addListItemForListTypeCustomField](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-list-item-for-list-type-custom-field) | 選択リスト形式のカスタム属性のリスト項目を追加します。「課題の追加/編集時に選択肢を追加できる」の設定が無効な場合は管理者権限のユーザーのみ呼び出せます。指定されたカスタム属性が選択リスト形式でない場合はエラーになります。 |
| [updateListItemForListTypeCustomField](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-list-item-for-list-type-custom-field) | 選択リスト形式のカスタム属性のリスト項目を更新します。指定されたカスタム属性が選択リスト形式でない場合はエラーになります。 |
| [deleteListItemForListTypeCustomField](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-list-item-for-list-type-custom-field) | 選択リスト形式のカスタム属性のリスト項目を削除します。指定されたカスタム属性が選択リスト形式でない場合はエラーになります。 |
| [getListOfSharedFiles](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-shared-files) | 共有ファイルの一覧を取得します。 |
| [getFile](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-file) | 共有ファイルを取得します。 |
| [getProjectDiskUsage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-disk-usage) | プロジェクトの容量使用状況の情報を取得します。 |
| [getListOfWebhooks](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-webhooks) | Webhookの一覧を取得します。 |
| [addWebhook](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-webhook) | Webhookを追加します。 |
| [getWebhook](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-webhook) | Webhookの情報を取得します。 |
| [updateWebhook](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-webhook) | Webhookの情報を更新します。 |
| [deleteWebhook](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-webhook) | Webhookを削除します。 |
| [getIssueList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-list) | 課題の一覧を取得します。 |
| [countIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-issue) | 課題の数を取得します。 |
| [addIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-issue) | 新しい課題を追加します。 |
| [getIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue) | 課題の情報を取得します。 |
| [updateIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-issue) | 課題の情報を更新します。 |
| [deleteIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-issue) | 課題を削除します。 |
| [getCommentList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-comment-list) | 課題に登録されているコメントの一覧を取得します。 |
| [addComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-comment) | 課題に新しいコメントを追加します。 |
| [countComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-comment) | 課題に登録されているコメントの数を取得します。 |
| [getComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-comment) | 課題コメントの詳細を取得します。 |
| [deleteComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-comment) | 課題コメントを削除します。 |
| [updateComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-comment) | 課題コメントの情報を更新します。認証ユーザー自身が登録したコメントのみ更新することが出来ます。 |
| [getListOfCommentNotifications](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-comment-notifications) | 課題コメントのお知らせ一覧を取得します。 |
| [addCommentNotification](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-comment-notification) | コメントにお知らせを追加します認証ユーザー自身が登録したコメントのみお知らせを追加することが出来ます。 |
| [getListOfIssueAttachments](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-issue-attachments) | 課題の添付ファイルの一覧を取得します。 |
| [getIssueAttachment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-attachment) | 課題の添付ファイルをダウンロードします。 |
| [deleteIssueAttachment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-issue-attachment) | 課題の添付ファイルを削除します。 |
| [getListOfLinkedSharedFiles](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-linked-shared-files) | 課題にリンクされた共有ファイルの一覧を取得します。 |
| [linkSharedFilesToIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/link-shared-files-to-issue) | 課題に共有ファイルをリンクします。 |
| [removeLinkToSharedFileFromIssue](https://developer.nulab-inc.com/ja/docs/backlog/api/2/remove-link-to-shared-file-from-issue) | 課題にリンクされた共有ファイルのリンクを解除します。 |
| [getWikiPageList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-list) | Wikiページの一覧を取得します。 |
| [countWikiPage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-wiki-page) | Wikiページの数を取得します。 |
| [getWikiPageTagList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-tag-list) | プロジェクト内のWikiページで使用されているタグの一覧を取得します。 |
| [addWikiPage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-wiki-page) | WIkiの新しいページを追加します。 |
| [getWikiPage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page) | Wikiページの情報を取得します。 |
| [updateWikiPage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-wiki-page) | Wikiページの情報を更新します。 |
| [deleteWikiPage](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-wiki-page) | WIkiページを削除します。 |
| [getListOfWikiAttachments](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-wiki-attachments) | Wikiの添付ファイルの一覧を取得します。 |
| [attachFileToWiki](https://developer.nulab-inc.com/ja/docs/backlog/api/2/attach-file-to-wiki) | Wikiに添付ファイルを追加します。 |
| [getWikiPageAttachment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-attachment) | Wikiの添付ファイルをダウンロードします。 |
| [removeWikiAttachment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/remove-wiki-attachment) | Wikiの添付ファイルを削除します。 |
| [getListOfSharedFilesOnWiki](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-shared-files-on-wiki) | Wikiの共有ファイルの一覧を取得します。 |
| [linkSharedFilesToWiki](https://developer.nulab-inc.com/ja/docs/backlog/api/2/link-shared-files-to-wiki) | Wikiに共有ファイルをリンクします。 |
| [removeLinkToSharedFileFromWiki](https://developer.nulab-inc.com/ja/docs/backlog/api/2/remove-link-to-shared-file-from-wiki) | Wikiにリンクされた共有ファイルのリンクを解除します。 |
| [getWikiPageHistory](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-history) | Wikiページの更新履歴の一覧を取得します。 |
| [getWikiPageStar](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-star) | Wikiページが受け取ったスターの一覧を取得します。 |
| [addStar](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-star) | 課題、コメント、Wikiページにスターを一つ追加します。 |
| [getNotification](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-notification) | 自分の受け取ったお知らせの一覧を取得します。 |
| [countNotification](https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-notification) | 自分の受け取ったお知らせの数を取得します。 |
| [resetUnreadNotificationCount](https://developer.nulab-inc.com/ja/docs/backlog/api/2/reset-unread-notification-count) | 自分の受け取ったお知らせの未読数をリセットします。 |
| [readNotification](https://developer.nulab-inc.com/ja/docs/backlog/api/2/read-notification) | お知らせを既読にします。 |
| [getListOfGitRepositories](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-git-repositories) | Gitリポジトリの一覧を取得します。 |
| [getGitRepository](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-git-repository) | Gitリポジトリを取得します。 |
| [getPullRequestList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-pull-request-list) | プルリクエストの一覧を取得します。 |
| [getNumberOfPullRequests](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-number-of-pull-requests) | プルリクエストの数を取得します。 |
| [addPullRequest](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-pull-request) | プルリクエストを追加します。 |
| [getPullRequest](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-pull-request) | プルリクエストを取得します。 |
| [updatePullRequest](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-pull-request) | プルリクエストを更新します。 |
| [getPullRequestComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-pull-request-comment) | プルリクエストのコメントの一覧を取得します。 |
| [addPullRequestComment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-pull-request-comment) | プルリクエストにコメントを追加します。 |
| [getNumberOfPullRequestComments](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-number-of-pull-request-comments) | プルリクエストに登録されているコメントの数を取得します。 |
| [updatePullRequestCommentInformation](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-pull-request-comment-information) | プルリクエストコメントの情報を更新します。認証ユーザー自身が登録したコメントのみ更新することが出来ます。 |
| [getListOfPullRequestAttachment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-list-of-pull-request-attachment) | プルリクエストの添付ファイルの一覧を取得します。 |
| [downloadPullRequestAttachment](https://developer.nulab-inc.com/ja/docs/backlog/api/2/download-pull-request-attachment) | プルリクエストの添付ファイルをダウンロードします。 |
| [deletePullRequestAttachments](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-pull-request-attachments) | プルリクエストの添付ファイルを削除します。 |
| [getWatchingList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-watching-list) | ウォッチの一覧を取得します。 |
| [countWatching](https://developer.nulab-inc.com/ja/docs/backlog/api/2/count-watching) | ウォッチの数を取得します。 |
| [getWatching](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-watching) | ウォッチの情報を追加します。 |
| [addWatching](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-watching) | ウォッチを追加します。 |
| [updateWatching](https://developer.nulab-inc.com/ja/docs/backlog/api/2/update-watching) | ウォッチを更新します。 |
| [deleteWatching](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-watching) | ウォッチを削除します。 |
| [markWatchingAsRead](https://developer.nulab-inc.com/ja/docs/backlog/api/2/mark-watching-as-read) | ウォッチを既読にします。 |
| [getProjectGroupList](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-group-list) | プロジェクトのグループの一覧を取得します。 |
| [addProjectGroup](https://developer.nulab-inc.com/ja/docs/backlog/api/2/add-project-group) | プロジェクトにグループを追加します。 |
| [deleteProjectGroup](https://developer.nulab-inc.com/ja/docs/backlog/api/2/delete-project-group) | プロジェクトからグループを削除します。 |
| [getGroupIcon](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-group-icon) | グループのアイコン画像を取得します。 |
| [getLicence](https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-licence) | ライセンスの情報を取得します。 |
