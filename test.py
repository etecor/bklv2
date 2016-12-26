# coding: UTF-8

from datetime import datetime
import bklv2
import unittest
import json
import inspect



class Test(unittest.TestCase):
    testuser_id = "testuser"
    testuser_password = "1234567890"
    testuser_name = "tester"
    testuser_mailaddress = "test333424435@t54263465est.com"
    testproject_name = "test"
    testproject_key = "TEST"

    bkl = None
    checked_api = []

    def _gettestuser(self):
        users = self.check_api( "getUsers", self.bkl.getUsers() )
        for u in users:
            if u["userId"]==self.testuser_id:
                return u
        return self.check_api(
            "addUser",
            self.bkl.addUser(userId=self.testuser_id,
                            password=self.testuser_password,
                            name=self.testuser_name,
                            mailAddress=self.testuser_mailaddress,
                            roleType=2) )

    def _gettestproject(self):
        ps = self.check_api( "getProjects", self.bkl.getProjects() )
        if len(ps) == 1:
            # Free plan space can only have one project.
            return ps[0]
        p = self.check_api(
                "addProject",
                self.bkl.addProject(name=self.testproject_name,
                                    key=self.testproject_key,
                                    chartEnabled=False,
                                    subtaskingEnabled=False,
                                    textFormattingRule="markdown") )
        u = self._gettestuser()
        self.check_api( "addProjectUser", self.bkl.addProjectUser( projectIdOrKey=p["id"], userId=u["id"] ) )
        issues = self.check_api( "getIssueTypes", self.bkl.getIssueTypes( projectIdOrKey=p["id"] ) )
        pris = self.check_api( "getPriorities", self.bkl.getPriorities() )
        self.check_api( "addIssue", self.bkl.addIssue( projectId=p["id"], summary="課題テスト1", issueTypeId=issues[0]["id"], priorityId=pris[0]["id"] ) )
        return p

    def setUp(self):
        if self.bkl == None:
            try:
                f = open( "apikey.json", "r" )
                cfg = json.load(f)
            except Exception as e:
                sample = \
"""{
    "hostname": "https://<spacename>.backlog.jp",
    "apikey": "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12"
}
"""
                fsample = open( "apikey.json", "w" )
                fsample.write( sample )
                fsample.close()
            finally:
                f.close()
            self.bkl = bklv2.api( hostname=cfg["hostname"], apikey=cfg["apikey"] )
            self._gettestproject()

    @classmethod
    def tearDownClass(cls):
        print( "" )
        print( "# checked api count = " + str( len(cls.checked_api) ) )
        print( cls.checked_api )
        print( "" )
        mbrs = inspect.getmembers( bklv2.api, inspect.isfunction )
        rests = []
        for m in mbrs:
            if not m[0] in cls.checked_api and m[0][0]!="_":
                rests.append( m[0] )
        print( "# no-check api count = " + str( len(rests) ) )
        print( rests )

    def check_api( self, api, response ):
        print( "[" + api + "]" )
        print( self.bkl.response.url )
        print( ">>" )
        print( response )
        self.assertFalse( "errors" in response )
        if not api in self.checked_api:
            self.checked_api.append( api )
        print( "" )
        return response

    #@unittest.skip("")
    def testSpace(self):
        self.check_api( "getSpace", self.bkl.getSpace() )
        self.check_api( "getSpaceImage", self.bkl.getSpaceImage() )
        self.check_api( "getSpaceDiskUsage", self.bkl.getSpaceDiskUsage() )
        self.check_api( "updateSpaceNotification", self.bkl.updateSpaceNotification( "## test of updateSpaceNotification.\r\n" + datetime.now().isoformat() ) )
        self.check_api( "getSpaceNotification", self.bkl.getSpaceNotification() )
        self.check_api( "getStatus",self.bkl.getStatus() )
        self.check_api( "getResolutions",self.bkl.getResolutions() )
        self.check_api( "getPriorities",self.bkl.getPriorities() )
        self.check_api( "getUserRecentlyViewedIssues", self.bkl.getUserRecentlyViewedIssues() )
        self.check_api( "getUserRecentlyViewedProjects", self.bkl.getUserRecentlyViewedProjects() )
        self.check_api( "getUserRecentlyViewedWikis", self.bkl.getUserRecentlyViewedWikis() )
        self.check_api( "getNotification", self.bkl.getNotification() )
        self.check_api( "getNotificationCount", self.bkl.getNotificationCount( alreadyRead=True ) )
        self.check_api( "getActivities", self.bkl.getActivities( activityTypeIds=[2,3,4], count=5 ) )
        pass

    #@unittest.skip("")
    def testUser(self):
        uid = self._gettestuser()["id"]
        self.check_api( "updateUser", self.bkl.updateUser(userId=uid,name="てすと") )
        self.check_api( "getUser", self.bkl.getUser(userId=uid) )
        self.check_api( "getUserIcon", self.bkl.getUserIcon(userId=uid) )
        self.check_api( "updateUser", self.bkl.updateUser(userId=uid,name=self.testuser_name) )
        self.check_api( "getUserStars", self.bkl.getUserStars(userId=uid) )
        self.check_api( "getUserStarsCount", self.bkl.getUserStarsCount(userId=uid) )
        self.check_api( "getUserActivities", self.bkl.getUserActivities(userId=uid) )
        self.check_api( "getMyselfUser", self.bkl.getMyselfUser() )
        self.check_api( "getWatchingList", self.bkl.getWatchingList(userId=uid) )
        self.check_api( "countWatching", self.bkl.countWatching(userId=uid) )
        adduser = self.check_api( "addUser", self.bkl.addUser(userId="adduser",password="12345678",name="追加ゆーざ",mailAddress=self.testuser_mailaddress,roleType=2) )
        self.check_api( "deleteUser", self.bkl.deleteUser(userId=adduser["id"]) )
        pass

    #@unittest.skip("")
    def testGroup(self):
        res = self.check_api( "getUsers", self.bkl.getUsers() )
        uid_0 = res[0]["id"]
        uid_1 = res[1]["id"]
        gs = self.check_api( "getGroups", self.bkl.getGroups() )
        for g in gs:
            if g["name"]=="testgroup":
                self.check_api( "deleteGroup", self.bkl.deleteGroup(groupId=g["id"]) )
        res = self.check_api( "addGroup", self.bkl.addGroup(name="testgroup",members=[uid_0]) )
        gid = res["id"]
        self.check_api( "updateGroup", self.bkl.updateGroup(groupId=gid,members=[uid_0,uid_1]) )
        self.check_api( "getGroup", self.bkl.getGroup(groupId=gid) )
        pass

    #@unittest.skip("")
    def testProject(self):
        prjs = self.check_api( "getProjects", self.bkl.getProjects() )
        for p in prjs:
            if p["name"]==self.testproject_name:
                pid = p["id"]
                self.check_api( "updateProject", self.bkl.updateProject(projectIdOrKey=pid,textFormattingRule="backlog") )
                self.check_api( "deleteProject", self.bkl.deleteProject(projectIdOrKey=pid) )

        pid = self._gettestproject()["id"]
        icon_path = self.check_api( "getProjectIcon", self.bkl.getProjectIcon(projectIdOrKey=pid) )
        afile = self.check_api( "addAttachment", self.bkl.addAttachment(icon_path) )
        self.check_api( "getProjectActivities", self.bkl.getProjectActivities(projectIdOrKey=pid) )
        self.check_api( "getUsers", self.bkl.getUsers() )

        testuser = self._gettestuser()
        self.check_api( "getProjectUsers",self.bkl.getProjectUsers(projectIdOrKey=pid) )
        self.check_api( "addProjectAdministrator",self.bkl.addProjectAdministrator(projectIdOrKey=pid,userId=testuser["id"]) )
        self.check_api( "getProjectAdministrators",self.bkl.getProjectAdministrators(projectIdOrKey=pid) )
        self.check_api( "deleteProjectAdministrator",self.bkl.deleteProjectAdministrator(projectIdOrKey=pid,userId=testuser["id"]) )
        self.check_api( "deleteProjectUser",self.bkl.deleteProjectUser(projectIdOrKey=pid,userId=testuser["id"]) )
        self.check_api( "addProjectUser",self.bkl.addProjectUser(projectIdOrKey=pid,userId=testuser["id"]) )
        self.check_api( "getProject",self.bkl.getProject(projectIdOrKey=pid) )
        self.check_api( "getProjectDiskUsage", self.bkl.getProjectDiskUsage(projectIdOrKey=pid) )

        cid = self.check_api( "addCategory",self.bkl.addCategory(projectIdOrKey=pid,name="test1") )["id"]
        self.check_api( "updateCategory", self.bkl.updateCategory(projectIdOrKey=pid,id=cid,name="test2") )
        self.check_api( "getCategories", self.bkl.getCategories(projectIdOrKey=pid) )
        self.check_api( "deleteCategory", self.bkl.deleteCategory(projectIdOrKey=pid,id=cid) )

        iid = self.check_api( "addIssueType", self.bkl.addIssueType(projectIdOrKey=pid,name="test",color="#2779ca") )["id"]
        self.check_api( "updateIssueType", self.bkl.updateIssueType(projectIdOrKey=pid,id=iid,name="test2") )
        iids = self.check_api( "getIssueTypes", self.bkl.getIssueTypes(projectIdOrKey=pid) )
        for id0 in iids:
            if iid != id0["id"]:
                self.check_api( "deleteIssueType", self.bkl.deleteIssueType(projectIdOrKey=pid,id=iid,substituteIssueTypeId=id0["id"]) )
                break

        vid = self.check_api( "addVersion", self.bkl.addVersion(
            projectIdOrKey=pid,name="testversion",description="add version test.",
            startDate="2000-01-03",releaseDueDate="2020-01-03" ))["id"]
        self.check_api( "updateVersion", self.bkl.updateVersion(projectIdOrKey=pid,id=vid,name="test2-2",releaseDueDate="2020-02-03") )
        self.check_api( "getVersions", self.bkl.getVersions(projectIdOrKey=pid) )
        self.check_api( "deleteVersion", self.bkl.deleteVersion(projectIdOrKey=pid,id=vid) )

        self.check_api( "getSharedfiles", self.bkl.getSharedfiles(projectIdOrKey=pid,path="") )
        self.check_api( "getWebhooks", self.bkl.getWebhooks(projectIdOrKey=pid) )

        rep = self.check_api( "getGitRepositories", self.bkl.getGitRepositories( projectIdOrKey=pid ) )
        if( len(rep) > 0 ):
            self.check_api( "getGitRepository",self.bkl.getGitRepository( projectIdOrKey=pid, repoIdOrName=rep[0]["id"] ) )
            self.check_api( "getPullRequests", self.bkl.getPullRequests( projectIdOrKey=pid, repoIdOrName=rep[0]["id"] ) )
            self.check_api( "getPullRequestsCount", self.bkl.getPullRequestsCount( projectIdOrKey=pid, repoIdOrName=rep[0]["id"] ) )

        wiki = self.check_api( "addWiki", self.bkl.addWiki(projectId=pid, name="wikiテスト", content="test 1234567890") )
        self.check_api( "getWikis", self.bkl.getWikis(projectIdOrKey=pid) )
        self.check_api( "getWikisCount", self.bkl.getWikisCount(projectIdOrKey=pid) )
        self.check_api( "updateWiki", self.bkl.updateWiki(wikiId=wiki["id"], content="abcd") )
        self.check_api( "getWikiAttachments", self.bkl.getWikiAttachments( wikiId=wiki["id"] ) )
        """
        # WikiAttachment is dead on free plan.
        self.check_api( "addWikiAttachment", self.bkl.addWikiAttachment(wikiId=wiki["id"], attachmentIds = [ afile["id"] ]) )
        self.check_api( "deleteWikiAttachment", self.bkl.deleteWikiAttachment(wikiId=wiki["id"], attachmentId = afile["id"]) )
        """
        self.check_api( "getWiki", self.bkl.getWiki(wikiId=wiki["id"]) )
        self.check_api( "getWikiHistory", self.bkl.getWikiHistory(wikiId=wiki["id"]) )
        self.check_api( "getWikiStars", self.bkl.getWikiStars(wikiId=wiki["id"]) )
        self.check_api( "getWikiTags", self.bkl.getWikiTags(projectIdOrKey=pid) )
        self.check_api( "deleteWiki", self.bkl.deleteWiki(wikiId=wiki["id"]) )
        pass

    #@unittest.skip("")
    def testIssue(self):
        p = self._gettestproject()
        img = self.check_api( "getSpaceImage", self.bkl.getSpaceImage() )
        pus = self.check_api( "getProjectUsers",self.bkl.getProjectUsers(projectIdOrKey=p["id"]) )
        issuestype = self.check_api( "getIssueTypes", self.bkl.getIssueTypes(projectIdOrKey=p["id"]) )
        pris = self.check_api( "getPriorities", self.bkl.getPriorities() )
        issue = self.check_api( "addIssue", self.bkl.addIssue(
                            projectId=p["id"],
                            summary="issuetest",
                            issueTypeId=issuestype[0]["id"],
                            priorityId=pris[0]["id"] ) )
        self.check_api( "getIssues", self.bkl.getIssues(projectIds=[p["id"]]) )
        self.check_api( "getIssuesCount", self.bkl.getIssuesCount(projectIds=[p["id"]]) )
        self.check_api( "getIssue", self.bkl.getIssue(issueIdOrKey=issue["id"]) )
        afile = self.check_api( "addAttachment", self.bkl.addAttachment( img ) )
        self.check_api( "updateIssue", self.bkl.updateIssue(
                            issueIdOrKey=issue["id"],
                            description="詳細",
                            attachmentIds=[ afile["id"] ],
                            summary="サマリー") )
        comment = self.check_api( "addComment", self.bkl.addComment(issueIdOrKey=issue["id"],content="コメントの本文") )
        self.check_api( "addCommentNotification", self.bkl.addCommentNotification(issueIdOrKey=issue["id"], commentId=comment["id"], notifiedUserIds = [ pus[1]["id"] ]) )
        self.check_api( "updateComment", self.bkl.updateComment(issueIdOrKey=issue["id"], commentId=comment["id"], content="comment 123.") )
        self.check_api( "getComment", self.bkl.getComment(issueIdOrKey=issue["id"], commentId=comment["id"] ) )
        self.check_api( "getComments", self.bkl.getComments(issueIdOrKey=issue["id"]) )
        self.check_api( "getCommentsCount", self.bkl.getCommentsCount(issueIdOrKey=issue["id"]) )
        self.check_api( "addStar", self.bkl.addStar( commentId=comment["id"] ) )
        self.check_api( "addStar", self.bkl.addStar( issueId=issue["id"] ) )
        ats = self.check_api( "getIssueAttachments", self.bkl.getIssueAttachments( issueIdOrKey=issue["id"] ) )
        self.check_api( "getIssueAttachment", self.bkl.getIssueAttachment( issueIdOrKey=issue["id"], attachmentId=ats[0]["id"] ) )
        self.check_api( "deleteIssueAttachment", self.bkl.deleteIssueAttachment( issueIdOrKey=issue["id"], attachmentId=ats[0]["id"] ) )
        watch = self.check_api( "addWatching", self.bkl.addWatching( issueIdOrKey=issue["id"], note = "note1" ) )
        self.check_api( "updateWatching", self.bkl.updateWatching( watchingId=watch["id"], note = "note2" ) )
        self.check_api( "deleteWatching", self.bkl.deleteWatching( watchingId=watch["id"] ) )
        self.check_api( "deleteIssue", self.bkl.deleteIssue( issueIdOrKey=issue["id"] ) )
        pass

if __name__ == "__main__":

    unittest.main()
