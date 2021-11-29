# USING API LIST
## Get total num Information
- api: https://api.bilibili.com/x/space/navnum
- parameter : mid
- example : https://api.bilibili.com/x/space/navnum?mid=3845290
```json
{
	"code": 0,
	"message": "0",
	"ttl": 1,
	"data": {
		"video": 2,
		"bangumi": 0,
		"cinema": 1,
		"channel": {
			"master": 0,
			"guest": 0
		},
		"favourite": {
			"master": 5,
			"guest": 5
		},
		"tag": 0,
		"article": 0,
		"playlist": 0,
		"album": 0,
		"audio": 0,
		"pugv": 0
	}
}
```
## Page Get Personal Video Information
- api: https://api.bilibili.com/x/space/arc/search
- parameter : mid, ps, tid, pn
- example : https://api.bilibili.com/x/space/arc/search?mid=3845290&ps=30&tid=0&pn=1
```json
{
	"code": 0,
	"message": "0",
	"ttl": 1,
	"data": {
		"list": {
			"tlist": {
				"4": {
					"tid": 4,
					"count": 10,
					"name": "游戏"
				}
			},
			"vlist": [{
				"comment": 26,
				"typeid": 65,
				"play": 2181,
				"pic": "http://i2.hdslb.com/bfs/archive/f985766462701a99f22d070a3d7e7dac7a99ca05.jpg",
				"subtitle": "",
				"description": "投完稿切回游戏发现有人开出来弓箭手没打过，想着上去打一波把这仨都录了，结果没发现时间不够。后面技能不全开怪随便录一个，笑死，根本死不了。bd同应邀发布2",
				"copyright": "1",
				"title": "【GW2元素】应邀发布3--笑死，根本死不了",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1624509736,
				"length": "02:18",
				"video_review": 0,
				"aid": 418784781,
				"bvid": "BV1cV411x7fj",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 16,
				"typeid": 65,
				"play": 854,
				"pic": "http://i2.hdslb.com/bfs/archive/38a00acfefe36b656bc5e24e0ec1370aae3f7d5d.jpg",
				"subtitle": "",
				"description": "RT，新版本火焰纹章削弱，因此把火焰纹章换成了岩石共振，元素能量雕文换成了扭转命运，装备上把超级元素使换成了超级神佑，法印从【渴求+洁净】换成了【迅敏+洁净】，其他与上一稿相同",
				"copyright": "1",
				"title": "【GW2元素】应邀发布2",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1624509164,
				"length": "01:14",
				"video_review": 0,
				"aid": 503834356,
				"bvid": "BV1ng41137ix",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 6,
				"typeid": 65,
				"play": 527,
				"pic": "http://i0.hdslb.com/bfs/archive/2b1bacb0fcdc8c8b14b4bb91e3566f669321ed12.jpg",
				"subtitle": "",
				"description": "应评论区朋友邀请发布",
				"copyright": "1",
				"title": "【GW2元素】应邀发布",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1624508901,
				"length": "01:16",
				"video_review": 0,
				"aid": 758760588,
				"bvid": "BV1u64y197Nc",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 105,
				"typeid": 65,
				"play": 9562,
				"pic": "http://i1.hdslb.com/bfs/archive/a44c18e9d88e138eb11715d35f46aae29e0d3c56.jpg",
				"subtitle": "",
				"description": "全身天界（视频录制的时候有一个戒指是毒蛇，因为马上出凝心所以就懒得搞了）\r\n超级元素使，超级渴求+洁净\r\n火112，秘法121，编织313，bd之后还会再调整\r\n目前来看还是很猛的。",
				"copyright": "1",
				"title": "【激战2】新版天界编织野外测试",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1621131571,
				"length": "03:31",
				"video_review": 2,
				"aid": 888124043,
				"bvid": "BV1wK4y1P7Cq",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 127,
				"typeid": 65,
				"play": 20158,
				"pic": "http://i0.hdslb.com/bfs/archive/d3c05fb002ab7c6d2a1157e49e08c83494012eee.png",
				"subtitle": "",
				"description": "原创BD，up野外自用\nP1:\n00:08-00:52:如何通过光环获得生存能力\n00:53-02:10:如何获得光环\n02:23-02:45:使用组合技打出爆发性回血\n02:46-03:14:其他回血清症和解除昏迷手段（补充：所有的过载都可以解除昏迷）\n03:17-03:52:破蔑视技能\n03:54-04:23:核心特性“岩石力量”提供的伤害制造能力\n04:26-04:38:装备配置\n04:42-05:32:实战细节讲解\n05:33-06:56:输出循环演示\n06:57-07:05:总结",
				"copyright": "1",
				"title": "【激战2原创bd】野外最强元素",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1613608154,
				"length": "27:39",
				"video_review": 28,
				"aid": 886655564,
				"bvid": "BV18K4y1n7o2",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 10,
				"typeid": 65,
				"play": 2626,
				"pic": "http://i2.hdslb.com/bfs/archive/a625dd1cc898c67dc795a19b44fa73cff7420fe8.png",
				"subtitle": "",
				"description": "回血：\r\n回血纹章：每次释放技能回血\r\n水2+土4\r\n水2+土2\r\n水协调下翻滚\r\n精英水元素雕文\r\n水3\r\n脉冲护盾+稳固：\r\n火土3\r\n双重攻击获得护盾\r\n清症状：\r\n土4\r\n无敌：\r\n土5\r\n闪避：\r\n水2\r\n土2\r\n阻挡投掷物：\r\n电4\r\n\r\nbd：\r\n防具天界\r\n武器统帅\r\n首饰毒蛇\r\n超级巴萨泽\r\n超级渴求+恶毒",
				"copyright": "1",
				"title": "【激战2】编织生存向技巧",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1606184613,
				"length": "04:37",
				"video_review": 0,
				"aid": 585458153,
				"bvid": "BV18z4y1k79m",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 13,
				"typeid": 65,
				"play": 1643,
				"pic": "http://i2.hdslb.com/bfs/archive/7607a0b910bebc10c1edca8ae0c76efe4734358e.png",
				"subtitle": "",
				"description": "没\r\n有\r\n简\r\n介",
				"copyright": "1",
				"title": "【激战2】十人本工具人元素的自我修养",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1603618905,
				"length": "06:57",
				"video_review": 5,
				"aid": 245107691,
				"bvid": "BV1rv41167qS",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 12,
				"typeid": 65,
				"play": 6495,
				"pic": "http://i2.hdslb.com/bfs/archive/a2377bf4a2b23589d75695c3962b63f9568416da.jpg",
				"subtitle": "",
				"description": "周末如果能做完实验就更新这套bd的使用教程！TAT\r\n装备：全身帕花\r\n武器：匕首/号角\r\n符文：超级亡灵符文\r\n法印：超级渴求+超级恶毒",
				"copyright": "1",
				"title": "【激战2】元素野外该怎么玩？——野外症状暴风使",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1602951559,
				"length": "08:03",
				"video_review": 2,
				"aid": 287408467,
				"bvid": "BV1Wf4y1B7XK",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 46,
				"typeid": 65,
				"play": 10595,
				"pic": "http://i2.hdslb.com/bfs/archive/7d0ff23232b6bd40a9287be46b26794ab92ce579.jpg",
				"subtitle": "",
				"description": "",
				"copyright": "1",
				"title": "【激战2】“我就是元素！”——症状编织",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1602516579,
				"length": "02:35",
				"video_review": 1,
				"aid": 839964684,
				"bvid": "BV1b54y1R7cB",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}, {
				"comment": 9,
				"typeid": 65,
				"play": 1018,
				"pic": "http://i0.hdslb.com/bfs/archive/7c07fc3f3c9bdc59a4c0154523c735cf14939b21.jpg",
				"subtitle": "",
				"description": "相关游戏: 地下城与勇士\n简介补充: 这个地板过得可以说是很刺激了",
				"copyright": "1",
				"title": "【皮皮】起源版本女机械1分50秒单人火山",
				"review": 0,
				"author": "吉安娜拉格纳罗斯",
				"mid": 3845290,
				"created": 1518845444,
				"length": "02:37",
				"video_review": 1,
				"aid": 19698990,
				"bvid": "BV1QW411j7PH",
				"hide_click": false,
				"is_pay": 0,
				"is_union_video": 0,
				"is_steins_gate": 0,
				"is_live_playback": 0
			}]
		},
		"page": {
			"pn": 1,
			"ps": 30,
			"count": 10
		},
		"episodic_button": {
			"text": "播放全部",
			"uri": "//www.bilibili.com/medialist/play/3845290?from=space"
		}
	}
}
```
## Get Video cid by bvid
- api: https://api.bilibili.com/x/player/pagelist
- parameter : bvid
- example : https://api.bilibili.com/x/player/pagelist?bvid=BV1cV411x7fj
```json
{
	"code": 0,
	"message": "0",
	"ttl": 1,
	"data": [{
		"cid": 358888885,
		"page": 1,
		"from": "vupload",
		"part": "Guild Wars 2 2021.06.24 - 12.16.33.03",
		"duration": 138,
		"vid": "",
		"weblink": "",
		"dimension": {
			"width": 1920,
			"height": 1080,
			"rotate": 0
		}
	}]
}
```

## Get Video Download info by cid and bvid
- api: http://api.bilibili.com/x/player/playurl?qn=64&fnval=0&fnver=0&fourk=1& + bvid_info + "&"+cid_info
- parameter : qn, fnval, fnver, fourk, bvid, cid
- note: headers['SESSDATA'] = 'xxx' for vip if needed
- example : http://api.bilibili.com/x/player/playurl?qn=64&fnval=0&fnver=0&fourk=1&bvid=BV1cV411x7fj&cid=358888885
```json
{
	"code": 0,
	"message": "0",
	"ttl": 1,
	"data": {
		"from": "local",
		"result": "suee",
		"message": "",
		"quality": 64,
		"format": "flv720_p60",
		"timelength": 137100,
		"accept_format": "flv_p60,flv,flv720_p60,flv480,mp4",
		"accept_description": ["高清 1080P60", "高清 1080P", "高清 720P60", "清晰 480P", "流畅 360P"],
		"accept_quality": [116, 80, 64, 32, 16],
		"video_codecid": 7,
		"seek_param": "start",
		"seek_type": "offset",
		"durl": [{
			"order": 1,
			"length": 137100,
			"size": 33665716,
			"ahead": "",
			"vhead": "",
			"url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/85/88/358888885/358888885-1-74.flv?e=ig8euxZM2rNcNbNM7WdVhwdlhbKBhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1637832921\u0026gen=playurlv2\u0026os=cosbv\u0026oi=822547397\u0026trid=8f5f84c49c79406c90ef0039b2d77e45u\u0026platform=pc\u0026upsig=a9bd3e27edfa408dab0a0b5c33982e4a\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform\u0026mid=62397974\u0026bvc=vod\u0026nettype=0\u0026orderid=0,3\u0026agrr=1\u0026bw=245735\u0026logo=80000000",
			"backup_url": ["https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/85/88/358888885/358888885-1-74.flv?e=ig8euxZM2rNcNbNM7WdVhwdlhbKBhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1637832921\u0026gen=playurlv2\u0026os=cosbv\u0026oi=822547397\u0026trid=8f5f84c49c79406c90ef0039b2d77e45u\u0026platform=pc\u0026upsig=a9bd3e27edfa408dab0a0b5c33982e4a\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform\u0026mid=62397974\u0026bvc=vod\u0026nettype=0\u0026orderid=1,3\u0026agrr=1\u0026bw=245735\u0026logo=40000000", "https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/85/88/358888885/358888885-1-74.flv?e=ig8euxZM2rNcNbNM7WdVhwdlhbKBhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=\u0026uipk=5\u0026nbs=1\u0026deadline=1637832921\u0026gen=playurlv2\u0026os=cosbbv\u0026oi=822547397\u0026trid=8f5f84c49c79406c90ef0039b2d77e45u\u0026platform=pc\u0026upsig=dad9e03ee76c41c7c82c5e49bb525c7b\u0026uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform\u0026mid=62397974\u0026bvc=vod\u0026nettype=0\u0026orderid=2,3\u0026agrr=1\u0026bw=245735\u0026logo=40000000"]
		}],
		"support_formats": [{
			"quality": 116,
			"format": "flv_p60",
			"new_description": "1080P 60帧",
			"display_desc": "1080P",
			"superscript": "60帧"
		}, {
			"quality": 80,
			"format": "flv",
			"new_description": "1080P 高清",
			"display_desc": "1080P",
			"superscript": ""
		}, {
			"quality": 64,
			"format": "flv720_p60",
			"new_description": "720P 60帧",
			"display_desc": "720P",
			"superscript": "60帧"
		}, {
			"quality": 32,
			"format": "flv480",
			"new_description": "480P 清晰",
			"display_desc": "480P",
			"superscript": ""
		}, {
			"quality": 16,
			"format": "mp4",
			"new_description": "360P 流畅",
			"display_desc": "360P",
			"superscript": ""
		}],
		"high_format": null
	}
}
```

## Download video by cid_bvid_order
- api: get from durl
- parameter : none
- note: headers = get_http_header()