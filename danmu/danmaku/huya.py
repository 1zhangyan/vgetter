import re
import aiohttp
from enum import IntEnum
from .tars import tarscore


class Huya:
    wss_url = 'wss://cdnws.api.huya.com/'
    heartbeat = b'\x00\x03\x1d\x00\x00\x69\x00\x00\x00\x69\x10\x03\x2c\x3c\x4c\x56\x08\x6f\x6e\x6c\x69\x6e\x65\x75' \
                b'\x69\x66\x0f\x4f\x6e\x55\x73\x65\x72\x48\x65\x61\x72\x74\x42\x65\x61\x74\x7d\x00\x00\x3c\x08\x00' \
                b'\x01\x06\x04\x74\x52\x65\x71\x1d\x00\x00\x2f\x0a\x0a\x0c\x16\x00\x26\x00\x36\x07\x61\x64\x72\x5f' \
                b'\x77\x61\x70\x46\x00\x0b\x12\x03\xae\xf0\x0f\x22\x03\xae\xf0\x0f\x3c\x42\x6d\x52\x02\x60\x5c\x60' \
                b'\x01\x7c\x82\x00\x0b\xb0\x1f\x9c\xac\x0b\x8c\x98\x0c\xa8\x0c '
    heartbeatInterval = 60

    @staticmethod
    async def get_ws_info(url):
        reg_datas = []
        url = 'https://m.huya.com/' + url.split('/')[-1]
        headers = {
            'user-agent': 'Mozilla/6.0 (Linux Android 6.0 Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                room_page = await resp.text()
                m = re.search(r"lYyid\":([0-9]+)", room_page, re.MULTILINE)
                ayyuid = m.group(1)
                m = re.search(r"lChannelId\":([0-9]+)", room_page, re.MULTILINE)
                tid = m.group(1)
                m = re.search(r"lSubChannelId\":([0-9]+)", room_page, re.MULTILINE)
                sid = m.group(1)
                print(ayyuid+'\t'+tid+'\t'+sid)
                #979008	1629021815	1629021815
                
        oos = tarscore.TarsOutputStream()
        oos.write(tarscore.int64, 0, int(ayyuid))
        oos.write(tarscore.boolean, 1, True)  # Anonymous
        oos.write(tarscore.string, 2, "")  # sGuid
        oos.write(tarscore.string, 3, "")
        oos.write(tarscore.int64, 4, int(tid))
        oos.write(tarscore.int64, 5, int(sid))
        oos.write(tarscore.int64, 6, 0)
        oos.write(tarscore.int64, 7, 0)

        wscmd = tarscore.TarsOutputStream()
        wscmd.write(tarscore.int32, 0, 1)
        wscmd.write(tarscore.bytes, 1, oos.getBuffer())

        reg_datas.append(wscmd.getBuffer())
        return Huya.wss_url, reg_datas

    @staticmethod
    def decode_msg(data):
        """
        class user(tarscore.struct):
            def readFrom(ios):
                return ios.read(tarscore.string, 2, False).decode('utf8')
"""
        name = ''
        content = ''
        msgs = []
        ios = tarscore.TarsInputStream(data)
        
        command = WebSocketCommand()
        command.readFrom(ios)
        if command.iCmdType == EWebSocketCommandType.EWSCmdS2C_MsgPushReq:
            stream = tarscore.TarsInputStream(command.vData)
            msg = WSPushMessage()
            msg.readFrom(stream)
            if msg.iUri == 1400:
                stream = tarscore.TarsInputStream(msg.sMsg)
                msg = MessageNotice()
                msg.readFrom(stream)
                #print(msg.tUserInfo.sNickName + ":" + msg.sContent)
            elif msg.iUri == 6501:
                stream = tarscore.TarsInputStream(msg.sMsg)
                msg = MessageSendItemSub()
                msg.readFrom(stream)
                msgs.append({"type":msg.iItemType,"name":msg.sPropsName})
                if(msg.iItemType != 4):
                    print(msg.sSenderNick + " 送出 " + str(msg.iItemCount) + "个" + msg.sPropsName  + "    礼物类型:" + str(msg.iItemType))
            elif msg.iUri == 6502 :
                stream = tarscore.TarsInputStream(msg.sMsg)
                msg = SendItemNoticeWordBroadcastPacket()
                msg.readFrom(stream)
                #print("SendItemNoticeWordBroadcastPacket:")
                #print(msg.__dict__)
            elif msg.iUri == 6507 :
                stream = tarscore.TarsInputStream(msg.sMsg)
                msg = SendItemNoticeGameBroadcastPacket()
                msg.readFrom(stream)
                #print("SendItemNoticeGameBroadcastPacket:")
                #print(msg.__dict__)
        return msgs
        """
        if ios.read(tarscore.int32, 0, False) == 7:
            ios = tarscore.TarsInputStream(ios.read(tarscore.bytes, 1, False))
            if ios.read(tarscore.int64, 1, False) == 1400:
                ios = tarscore.TarsInputStream(ios.read(tarscore.bytes, 2, False))
                name = ios.read(user, 0, False)  # username
                content = ios.read(tarscore.string, 3, False).decode('utf8')  # content

        if name != '':
            msg = {'name': name, 'content': content, 'msg_type': 'danmaku'}
        else:
            msg = {'name': '', 'content': '', 'msg_type': 'other'}
        msgs.append(msg)
        return msgs
"""

class WSUserInfo:
    def __init__(self):
        self.lUid = 0
        self.bAnonymous = True
        self.sGuid = ""
        self.sToken = ""
        self.lTid = 0
        self.lSid = 0
        self.lGroupId = 0
        self.lGroupType = 0

    def writeTo(self, t: tarscore.TarsOutputStream):
        t.write(tarscore.int64, 0, self.lUid)
        t.write(tarscore.boolean, 1, self.bAnonymous)
        t.write(tarscore.string, 2, self.sGuid)
        t.write(tarscore.string, 3, self.sToken)
        t.write(tarscore.int64, 4, self.lTid)
        t.write(tarscore.int64, 5, self.lSid)
        t.write(tarscore.int64, 6, self.lGroupId)
        t.write(tarscore.int64, 7, self.lGroupType)


class WebSocketCommand:
    def __init__(self):
        self.iCmdType = 0
        self.vData = b''

    def writeTo(self, t: tarscore.TarsOutputStream):
        t.write(tarscore.int32, 0, self.iCmdType),
        t.write(tarscore.bytes, 1, self.vData)

    def readFrom(self, t: tarscore.TarsInputStream):
        self.iCmdType = t.read(tarscore.int32, 0, False, self.iCmdType)
        self.vData = t.read(tarscore.bytes, 1, False, self.vData)


class UserHeartBeatReq:
    def __init__(self):
        self.tId = None
        self.lTid = 0
        self.lSid = 0
        self.lShortTid = 0
        self.lPid = 0
        self.bWatchVideo = True
        self.eLineType = EStreamLineType.STREAM_LINE_OLD_YY
        self.iFps = 0
        self.iAttendee = 0
        self.iBandwidth = 0
        self.iLastHeartElapseTime = 0


class WSPushMessage:
    def __init__(self):
        self.ePushType = 0,
        self.iUri = 0,
        self.sMsg = b''
        self.iProtocolType = 0

    def readFrom(self, t: tarscore.TarsInputStream):
        self.ePushType = t.read(tarscore.int32, 0, False, self.ePushType)
        self.iUri = t.read(tarscore.int64, 1, False, self.iUri)
        self.sMsg = t.read(tarscore.bytes, 2, False, self.sMsg)
        self.iProtocolType = t.read(tarscore.int32, 3, False, self.iProtocolType)
        
    def showInfo(self):
        print(str(self.ePushType) + "\t" + str(self.iUri) + "\t" + str(self.sMsg) + "\t" + str(self.iProtocolType))
        


class SenderInfo(tarscore.struct):
    def __init__(self):
        self.lUid = 0
        self.lImid = 0
        self.sNickName = ""
        self.iGender = 0

    @staticmethod
    def readFrom(t: tarscore.TarsInputStream):
        var = SenderInfo()
        var.lUid = t.read(tarscore.int64, 0, False, var.lUid)
        var.lImid = t.read(tarscore.int64, 1, False, var.lImid)
        var.sNickName = t.read(tarscore.string, 2, False, var.sNickName).decode("utf-8")
        var.iGender = t.read(tarscore.int32, 3, False, var.iGender)
        return var


class MessageNotice:
    def __init__(self):
        self.tUserInfo = None,
        self.lTid = 0,
        self.lSid = 0,
        self.sContent = "",
        self.iShowMode = 0,
        self.tFormat = None
        self.tBulletFormat = None
        self.iTermType = 0,
        self.vDecorationPrefix = None
        self.vDecorationSuffix = None
        self.vAtSomeone = None
        self.lPid = 0

    def readFrom(self, t: tarscore.TarsInputStream):
        self.tUserInfo = t.read(SenderInfo, 0, False, self.tUserInfo)
        self.lTid = t.read(tarscore.int64, 1, False, self.lTid)
        self.lSid = t.read(tarscore.int64, 2, False, self.lSid)
        self.sContent = t.read(tarscore.string, 3, False, self.sContent).decode("utf-8")
        self.iShowMode = t.read(tarscore.int32, 4, False, self.iShowMode)
        # self.tFormat = t.read(tarscore.struct, 5, False, self.tFormat)
        # self.tBulletFormat = t.read(tarscore.struct, 6, False, self.tBulletFormat)
        self.iTermType = t.read(tarscore.int32, 7, False, self.iTermType)
        # self.vDecorationPrefix = t.read(tarscore.vctclass, 8, False, self.vDecorationPrefix)
        # self.vDecorationSuffix = t.read(tarscore.vctclass, 9, False, self.vDecorationSuffix)
        # self.vAtSomeone = t.read(tarscore.vctclass, 10, False, self.vAtSomeone)
        self.lPid = t.read(tarscore.int64, 11, False, self.lPid)

class StreamerNode(tarscore.struct):
    def __init__(self):
        self.iGiftLevel = 0
        self.iStreamerLevel = 0
        self.iMaterialType = 0
    
    @staticmethod
    def readFrom(t: tarscore.TarsInputStream):
        var = StreamerNode()
        var.iGiftLevel = t.read(tarscore.int16, 0, False, var.iGiftLevel)
        var.iStreamerLevel = t.read(tarscore.int16, 1, False, var.iStreamerLevel)
        var.iMaterialType = t.read(tarscore.int16, 2, False, var.iMaterialType)
        return var



class DecorationInfo(tarscore.struct): 
    def __init__(self):
        self.iAppId = 0
        self.iViewType = 0
        self.vData = b''
    
    @staticmethod
    def readFrom(t: tarscore.TarsInputStream):
        var = DecorationInfo()
        var.iAppId = t.read(tarscore.int32, 0, False, var.iAppId)
        var.iViewType = t.read(tarscore.int32, 1, False, var.iViewType)
        var.vData = t.read(tarscore.bytes, 2, False, var.vData)
        return var

    


class UserIdentityInfo(tarscore.struct):
    def __init__(self):
        self.vDecorationPrefix = []
        self.vDecorationSuffix = []
        
    @staticmethod
    def readFrom(t: tarscore.TarsInputStream):
        var = UserIdentityInfo()
        var.vDecorationPrefix = t.read(tarscore.vctclass, 0, False, var.vDecorationPrefix)
        var.vDecorationSuffix = t.read(tarscore.vctclass, 1, False, var.vDecorationSuffix)
        return var

class MessageSendItemSub:
    def __init__(self):
        self.iItemType = 0
        self.strPayId = ""
        self.iItemCount = 0
        self.lPresenterUid = 0
        self.lSenderUid = 0
        self.sPresenterNick = ""
        self.sSenderNick = ""
        self.sSendContent = ""
        self.iItemCountByGroup = 0
        self.iItemGroup = 0
        self.iSuperPupleLevel = 0
        self.iComboScore = 0
        self.iDisplayInfo = 0
        self.iEffectType = 0
        self.iSenderIcon = ""
        self.iPresenterIcon = ""
        self.iTemplateType = 0
        self.sExpand = ""
        self.bBusi = False
        self.iColorEffectType = 0
        self.sPropsName = ""
        self.iAccpet = 0
        self.iEventType = 0
        self.tUserInfo = None
        self.lRoomId = 0
        self.lHomeOwnerUid = 0
        self.streamerInfo = None
        
    def readFrom(self, t: tarscore.TarsInputStream):
        self.iItemType = t.read(tarscore.int32,0, False, self.iItemType)
        # self.strPayId = t.read(tarscore.string,1, False, self.strPayId).decode("utf-8")
        self.iItemCount = t.read(tarscore.int32,2, False, self.iItemCount)
        # self.lPresenterUid = t.read(tarscore.int64,3, False, self.lPresenterUid)
        # self.lSenderUid = t.read(tarscore.int64,4, False, self.lSenderUid)
        # self.sPresenterNick = t.read(tarscore.string,5, False, self.sPresenterNick).decode("utf-8")
        self.sSenderNick = t.read(tarscore.string,6, False, self.sSenderNick).decode("utf-8")
        # self.sSendContent = t.read(tarscore.string,7, False, self.sSendContent).decode("utf-8")
        # self.iItemCountByGroup = t.read(tarscore.int32,8, False, self.iItemCountByGroup)
        # self.iItemGroup = t.read(tarscore.int32,9, False, self.iItemGroup)
        # self.iSuperPupleLevel = t.read(tarscore.int32,10, False, self.iSuperPupleLevel)
        # self.iComboScore = t.read(tarscore.int32,11, False, self.iComboScore)
        # self.iDisplayInfo = t.read(tarscore.int32,12, False, self.iDisplayInfo)
        # self.iEffectType = t.read(tarscore.int32,13, False, self.iEffectType)
        # self.iSenderIcon = t.read(tarscore.string,14, False, self.iSenderIcon).decode("utf-8")
        # self.iPresenterIcon = t.read(tarscore.string,15, False, self.iPresenterIcon).decode("utf-8")
        # self.iTemplateType = t.read(tarscore.int32,16, False, self.iTemplateType)
        # self.sExpand = t.read(tarscore.string,17, False, self.sExpand).decode("utf-8")
        # self.bBusi = t.read(tarscore.boolean,18, False, self.bBusi)
        # self.iColorEffectType = t.read(tarscore.int32,19, False, self.iColorEffectType)
        self.sPropsName = t.read(tarscore.string,20, False, self.sPropsName).decode("utf-8")
        # self.iAccpet = t.read(tarscore.int16,21, False, self.iAccpet)
        # self.iEventType = t.read(tarscore.int16,22, False, self.iEventType)
        # self.tUserInfo = t.read(UserIdentityInfo, 23, False, self.tUserInfo)
        # self.lRoomId = t.read(tarscore.int64,24, False, self.lRoomId)
        # self.lHomeOwnerUid = t.read(tarscore.int64,25, False, self.lHomeOwnerUid)
        # self.streamerInfo = t.read(tarscore.int64,26, False, self.streamerInfo)
        

class SendItemNoticeWordBroadcastPacket:
    def __init__(self):
        self.iItemType = 0
        self.iItemCount = 0
        self.lSenderSid = 0
        self.lSenderUid = 0
        self.sSenderNick = ""
        self.lPresenterUid = 0
        self.sPresenterNick = ""
        self.lNoticeChannelCount = 0
        self.iItemCountByGroup = 0
        self.iItemGroup = 0
        self.iDisplayInfo = 0
        self.iSuperPupleLevel = 0
        self.iTemplateType = 0
        self.sExpand = ""
        self.bBusi = False
        self.iShowTime = 0
        self.lPresenterYY = 0
        self.lSid = 0
        self.lSubSid = 0
        self.lRoomId = 0
    def readFrom(self, t: tarscore.TarsInputStream):
        self.iItemType = t.read(tarscore.int32,0, False, self.iItemType)
        self.iItemCount = t.read(tarscore.int32,1, False, self.iItemCount)
        self.lSenderSid = t.read(tarscore.int64,2, False, self.lSenderSid)
        self.lSenderUid = t.read(tarscore.int64,3, False, self.lSenderUid)
        self.sSenderNick = t.read(tarscore.string,4, False, self.sSenderNick).decode("utf-8")
        self.lPresenterUid = t.read(tarscore.int64,5, False, self.lPresenterUid)
        self.sPresenterNick = t.read(tarscore.string,6, False, self.sPresenterNick).decode("utf-8")
        self.lNoticeChannelCount = t.read(tarscore.int64,7, False, self.lNoticeChannelCount)
        self.iItemCountByGroup = t.read(tarscore.int32,8, False, self.iItemCountByGroup)
        self.iItemGroup = t.read(tarscore.int32,9, False, self.iItemGroup)
        self.iDisplayInfo = t.read(tarscore.int32,10, False, self.iDisplayInfo)
        self.iSuperPupleLevel = t.read(tarscore.int32,11, False, self.iSuperPupleLevel)
        self.iTemplateType = t.read(tarscore.int32,12, False, self.iTemplateType)
        self.sExpand = t.read(tarscore.string,13, False, self.sExpand)
        self.bBusi = t.read(tarscore.boolean,14, False, self.bBusi)
        self.iShowTime = t.read(tarscore.int32,15, False, self.iShowTime)
        self.lPresenterYY = t.read(tarscore.int64,16, False, self.lPresenterYY)
        self.lSid = t.read(tarscore.int64,17, False, self.lSid)
        self.lSubSid = t.read(tarscore.int64,18, False, self.lSubSid)
        self.lRoomId = t.read(tarscore.int64,19, False, self.lRoomId)
        


class SendItemNoticeGameBroadcastPacket:
    def __init__(self):
        self.iItemType = 0
        self.iItemCount = 0
        self.lSenderUid = 0
        self.sSenderNick = ""
        self.lPresenterUid = 0
        self.sPresenterNick = ""
        self.lSid = 0
        self.lSubSid = 0
        self.lRoomId = 0
        self.iTemplateType = 0
          
    def readFrom(self, t: tarscore.TarsInputStream):
        self.iItemType = t.read(tarscore.int32,0, False, self.iItemType)
        self.iItemCount = t.read(tarscore.int32,1, False, self.iItemCount)
        self.lSenderUid = t.read(tarscore.int64,3, False, self.lSenderUid)
        self.sSenderNick = t.read(tarscore.string,4, False, self.sSenderNick)
        self.lPresenterUid = t.read(tarscore.int64,5, False, self.lPresenterUid)
        self.sPresenterNick = t.read(tarscore.string,6, False, self.sPresenterNick).decode("utf-8")
        self.lSid = t.read(tarscore.int64,7, False, self.lSid)
        self.lSubSid = t.read(tarscore.int64,8, False, self.lSubSid)
        self.lRoomId = t.read(tarscore.int64,9, False, self.lRoomId)
        self.iTemplateType = t.read(tarscore.int32,10, False, self.iTemplateType)
    
                  

class EWebSocketCommandType(IntEnum):
    EWSCmd_NULL = 0
    EWSCmd_RegisterReq = 1
    EWSCmd_RegisterRsp = 2
    EWSCmd_WupReq = 3
    EWSCmd_WupRsp = 4
    EWSCmdC2S_HeartBeat = 5
    EWSCmdS2C_HeartBeatAck = 6
    EWSCmdS2C_MsgPushReq = 7
    EWSCmdC2S_DeregisterReq = 8
    EWSCmdS2C_DeRegisterRsp = 9
    EWSCmdC2S_VerifyCookieReq = 10
    EWSCmdS2C_VerifyCookieRsp = 11
    EWSCmdC2S_VerifyHuyaTokenReq = 12
    EWSCmdS2C_VerifyHuyaTokenRsp = 13


class EStreamLineType(IntEnum):
    STREAM_LINE_OLD_YY = 0
    STREAM_LINE_WS = 1
    STREAM_LINE_NEW_YY = 2
    STREAM_LINE_AL = 3
    STREAM_LINE_HUYA = 4
