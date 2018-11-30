# -*- coding: utf-8 -*-
import os
from datetime import datetime
import bklv2
import unittest
import json
import inspect


class bklv2_api_d( bklv2.api ):
    checked_api = []
    error_api = []

    def check_api( self, api, response ):
        print( "[" + api + "]" )
        print( response )
        if "errors" in response:
            if not api in self.error_api:
                self.error_api.append( api )
            print( "" )
        else:
            if not api in self.checked_api:
                self.checked_api.append( api )
            print( "" )
        return response

    def _api_return( self, response, **kwargs ):
        res = super()._api_return( response, **kwargs )
        self.check_api( inspect.stack()[1][3], res )
        return res


class Test(unittest.TestCase):
    testuser_id = "testuser"
    testuser_password = "1234567890"
    testuser_name = "tester"
    testuser_mailaddress = "test333424435@t54263465est.com"
    testproject_name = "test"
    testproject_key = "TEST"

    bkl = None

    @classmethod
    def _gettestuser(cls):
        users = cls.bkl.getUserList()
        for u in users:
            if u["userId"]==cls.testuser_id:
                return u
        return cls.bkl.addUser(userId=self.testuser_id,
                            password=self.testuser_password,
                            name=self.testuser_name,
                            mailAddress=self.testuser_mailaddress,
                            roleType=2)

    @classmethod
    def _gettestproject(cls):
        ps = cls.bkl.getProjectList()
        if len(ps) == 1:
            # Free plan space can only have one project.
            return ps[0]
        p = cls.bkl.addProject( name=cls.testproject_name,
                                key=cls.testproject_key,
                                chartEnabled=False,
                                subtaskingEnabled=False,
                                textFormattingRule="markdown" )
        u = cls._gettestuser()
        cls.bkl.addProjectUser( projectIdOrKey=p["id"], userId=u["id"] )
        issues = cls.bkl.getIssueTypeList( projectIdOrKey=p["id"] )
        pris = cls.bkl.getPriorityList()
        cls.bkl.addIssue( projectId=p["id"], summary="issue test 1", issueTypeId=issues[0]["id"], priorityId=pris[0]["id"] )
        return p

    @classmethod
    def setUpClass(cls):
        if cls.bkl == None:
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
            cls.bkl = bklv2_api_d( hostname=cfg["hostname"], apikey=cfg["apikey"] )
            cls._gettestproject()

    @classmethod
    def tearDownClass(cls):
        print( "" )
        print( cls.bkl.checked_api )
        print( "# checked api count = " + str( len(cls.bkl.checked_api) ) )
        print( "" )
        print( cls.bkl.error_api )
        print( "# error api count = " + str( len(cls.bkl.error_api) ) )
        print( "" )
        mbrs = inspect.getmembers( bklv2.api, inspect.isfunction )
        rests = []
        for m in mbrs:
            if m[0] not in cls.bkl.checked_api and m[0] not in cls.bkl.error_api and m[0][0]!="_":
                rests.append( m[0] )
                print( m[0] )
        print( "# no-check api count = " + str( len(rests) ) )


    #@unittest.skip("")
    def testSpace(self):
        self.bkl.getSpace()
        self.bkl.getSpaceLogo()
        self.bkl.getSpaceDiskUsage()
        self.bkl.updateSpaceNotification( "## test of updateSpaceNotification.\r\n" + datetime.now().isoformat() )
        self.bkl.getSpaceNotification()
        self.bkl.getStatusList()
        self.bkl.getResolutionList()
        self.bkl.getPriorityList()
        self.bkl.getListOfRecentlyViewedWikis()
        self.bkl.getListOfRecentlyViewedIssues()
        self.bkl.getListOfRecentlyViewedProjects()
        self.bkl.getNotification()
        self.bkl.countNotification( alreadyRead=True )
        self.bkl.getRecentUpdates( activityTypeIds=[2,3,4], count=5 )
        self.bkl.getLicence()
        pass

    #@unittest.skip("")
    def testUser(self):
        uid = self._gettestuser()["id"]
        self.bkl.updateUser(userId=uid,name="T_E_S_T")
        self.bkl.getUser(userId=uid)
        self.bkl.getUserIcon(userId=uid)
        self.bkl.updateUser(userId=uid,name=self.testuser_name)
        self.bkl.getReceivedStarList(userId=uid)
        self.bkl.countUserReceivedStars(userId=uid)
        self.bkl.getUserRecentUpdates(userId=uid)
        self.bkl.getOwnUser()
        self.bkl.getWatchingList(userId=uid)
        self.bkl.countWatching(userId=uid)
        adduser = self.bkl.addUser(userId="adduser",password="12345678",name="new_user",mailAddress=self.testuser_mailaddress,roleType=2)
        self.bkl.deleteUser(userId=adduser["id"])
        pass

    #@unittest.skip("")
    def testGroup(self):
        res = self.bkl.getUserList()
        uid_0 = res[0]["id"]
        uid_1 = res[1]["id"]
        gs = self.bkl.getListOfGroups()
        for g in gs:
            if g["name"]=="testgroup":
                self.bkl.deleteGroup(groupId=g["id"])
        res = self.bkl.addGroup(name="testgroup",members=[uid_0])
        gid = res["id"]
        self.bkl.updateGroup(groupId=gid,members=[uid_0,uid_1])
        self.bkl.getGroup(groupId=gid)
        self.bkl.getGroupIcon(groupId=gid)
        pass

    #@unittest.skip("")
    def testProject(self):
        prjs = self.bkl.getProjectList()
        for p in prjs:
            if p["name"]==self.testproject_name:
                pid = p["id"]
                self.bkl.updateProject(projectIdOrKey=pid,textFormattingRule="backlog")
            #    self.bkl.deleteProject(projectIdOrKey=pid)

        pid = self._gettestproject()["id"]
        icon_path = self.bkl.getProjectIcon(projectIdOrKey=pid)
        afile = self.bkl.postAttachmentFile(icon_path)
        self.bkl.getProjectRecentUpdates(projectIdOrKey=pid)
        self.bkl.getUserList()

        testuser = self._gettestuser()
        gs = self.bkl.getListOfGroups()
        gid=0
        for g in gs:
            gid=g["id"]
        self.bkl.addProjectGroup(projectIdOrKey=pid, groupId=gid)
        self.bkl.getProjectGroupList(projectIdOrKey=pid)
        self.bkl.deleteProjectGroup(projectIdOrKey=pid, groupId=gid)
        self.bkl.getProjectUserList(projectIdOrKey=pid)
        self.bkl.addProjectAdministrator(projectIdOrKey=pid,userId=testuser["id"])
        self.bkl.getListOfProjectAdministrators(projectIdOrKey=pid)
        self.bkl.deleteProjectAdministrator(projectIdOrKey=pid,userId=testuser["id"])
        self.bkl.deleteProjectUser(projectIdOrKey=pid,userId=testuser["id"])
        self.bkl.addProjectUser(projectIdOrKey=pid,userId=testuser["id"])
        self.bkl.getProject(projectIdOrKey=pid)
        self.bkl.getProjectDiskUsage(projectIdOrKey=pid)

        cid = self.bkl.addCategory(projectIdOrKey=pid,name="test1")["id"]
        self.bkl.updateCategory(projectIdOrKey=pid,id=cid,name="test2")
        self.bkl.getCategoryList(projectIdOrKey=pid)
        self.bkl.deleteCategory(projectIdOrKey=pid,id=cid)

        iid = self.bkl.addIssueType(projectIdOrKey=pid,name="test",color="#2779ca")["id"]
        self.bkl.updateIssueType(projectIdOrKey=pid,id=iid,name="test2")
        iids = self.bkl.getIssueTypeList(projectIdOrKey=pid)
        for id0 in iids:
            if iid != id0["id"]:
                self.bkl.deleteIssueType(projectIdOrKey=pid,id=iid,substituteIssueTypeId=id0["id"])
                break

        res = self.bkl.addVersionMilestone(
            projectIdOrKey=pid,name="testversion",description="add version test.",
            startDate="2019-01-03",releaseDueDate="2020-01-03" )
        vid = res["id"]
        self.bkl.updateVersionMilestone(projectIdOrKey=pid,id=vid,name="test2-2",releaseDueDate="2019-02-05")
        self.bkl.getVersionMilestoneList(projectIdOrKey=pid)
        self.bkl.deleteVersion(projectIdOrKey=pid,id=vid)

        self.bkl.getListOfSharedFiles(projectIdOrKey=pid,path="")
        self.bkl.getListOfWebhooks(projectIdOrKey=pid)

        rep = self.bkl.getListOfGitRepositories( projectIdOrKey=pid )
        if len(rep) > 0:
            self.bkl.getGitRepository( projectIdOrKey=pid, repoIdOrName=rep[0]["id"] )
            self.bkl.getPullRequestList( projectIdOrKey=pid, repoIdOrName=rep[0]["id"] )
            self.bkl.getPullRequestsCount( projectIdOrKey=pid, repoIdOrName=rep[0]["id"] )

        wiki = self.bkl.addWikiPage(projectId=pid, name="wikiテスト", content="test 1234567890")
        self.bkl.getWikiPageList(projectIdOrKey=pid)
        self.bkl.countWikiPage(projectIdOrKey=pid)
        cfid=0

        # dead on free plan.
        cf = self.bkl.addCustomField(projectIdOrKey=pid, typeId=1, name="customfield_test", description="DESCRIPTION")
        if "errors" not in cf:
            cfid = cf["id"]
        # dead on free plan.
        self.bkl.updateCustomField(projectIdOrKey=pid, customFieldId=cfid, name="customfield_test_test" )
        # dead on free plan.
        self.bkl.deleteCustomField(projectIdOrKey=pid, customFieldId=cfid)

        self.bkl.updateWikiPage(wikiId=wiki["id"], content="abcd")
        self.bkl.getListOfWikiAttachments( wikiId=wiki["id"] )
        # dead on free plan.
        self.bkl.attachFileToWiki(wikiId=wiki["id"], attachmentIds = [ afile["id"] ])
        # dead on free plan.
        self.bkl.removeWikiAttachment(wikiId=wiki["id"], attachmentId = afile["id"])
        self.bkl.getWikiPage(wikiId=wiki["id"])
        self.bkl.getWikiPageHistory(wikiId=wiki["id"])
        self.bkl.getWikiPageStar(wikiId=wiki["id"])
        self.bkl.getWikiPageTagList(projectIdOrKey=pid)
        self.bkl.deleteWikiPage(wikiId=wiki["id"])
        pass

    #@unittest.skip("")
    def testIssue(self):
        p = self._gettestproject()
        img = self.bkl.getSpaceLogo()
        pus = self.bkl.getProjectUserList(projectIdOrKey=p["id"])
        issuestype = self.bkl.getIssueTypeList(projectIdOrKey=p["id"])
        pris = self.bkl.getPriorityList()
        issue = self.bkl.addIssue(
                            projectId=p["id"],
                            summary="issuetest",
                            issueTypeId=issuestype[0]["id"],
                            priorityId=pris[0]["id"] )
        islist = self.bkl.getIssueList(projectIds=[p["id"]])
        self.bkl.countIssue(projectIds=[p["id"]])
        self.bkl.getIssue(issueIdOrKey=issue["id"])
        afile = self.bkl.postAttachmentFile( img )
        sfile = self.bkl.getListOfSharedFiles(projectIdOrKey=p["id"])
        self.bkl.linkSharedFilesToIssue(issueIdOrKey=issue["id"], fileIds=[sfile[0]["id"]])
        self.bkl.removeLinkToSharedFileFromIssue(issueIdOrKey=issue["id"], fileId=sfile[0]["id"])
        self.bkl.updateIssue(
                            issueIdOrKey=issue["id"],
                            description="DESCRIPTION",
                            attachmentIds=[ afile["id"] ],
                            summary="SUMMARY")
        comment = self.bkl.addComment(issueIdOrKey=issue["id"],content="comment...")
        self.bkl.addCommentNotification(issueIdOrKey=issue["id"], commentId=comment["id"], notifiedUserIds = [ pus[1]["id"] ])
        self.bkl.updateComment(issueIdOrKey=issue["id"], commentId=comment["id"], content="comment 123.")
        self.bkl.getComment(issueIdOrKey=issue["id"], commentId=comment["id"] )
        self.bkl.getCommentList(issueIdOrKey=issue["id"])
        self.bkl.countComment(issueIdOrKey=issue["id"])
        self.bkl.addStar( commentId=comment["id"] )
        self.bkl.addStar( issueId=issue["id"] )
        ats = self.bkl.getListOfIssueAttachments( issueIdOrKey=issue["id"] )
        self.bkl.getIssueAttachment( issueIdOrKey=issue["id"], attachmentId=ats[0]["id"] )
        self.bkl.deleteIssueAttachment( issueIdOrKey=issue["id"], attachmentId=ats[0]["id"] )
        watch = self.bkl.addWatching( issueIdOrKey=issue["id"], note = "note1" )
        self.bkl.updateWatching( watchingId=watch["id"], note = "note2" )
        self.bkl.deleteWatching( watchingId=watch["id"] )
        self.bkl.deleteComment( issueIdOrKey=issue["id"], commentId=comment["id"] )
        for i in islist:
            self.bkl.deleteIssue( issueIdOrKey=i["id"] )
        pass


if __name__ == "__main__":
    p = os.path.dirname(__file__)
    if len(p) > 0:
        os.chdir( p )
    unittest.main()
