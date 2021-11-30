package utils

import (
	"container/list"
	"errors"
	"fmt"
	"github.com/buger/jsonparser"
	"github.com/schollz/progressbar/v3"
	"io"
	"io/ioutil"
	"math"
	"net/http"
	"os"
	"reflect"
	"strconv"
)

const TotalNumUrl = "http://api.bilibili.com/x/space/navnum?"
const VideoInfoPageURL = "http://api.bilibili.com/x/space/arc/search?ps=30&tid=0&pn=1"
const CidUrl = "http://api.bilibili.com/x/player/pagelist"
const DownloadInfoUrl = "http://api.bilibili.com/x/player/playurl?qn=64&fnval=0&fnver=0&fourk=1"


const ORIGIN = "https://www.bilibili.com"
const REFERER = "https://www.bilibili.com/"
const USERAGENT = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"

const PageSize = 30.0


const test = "{\"code\":0,\"message\":\"0\",\"ttl\":1,\"data\":[{\"cid\":409687852,\"page\":1,\"from\":\"vupload\",\"part\":\"02.第一章类型1与概率有关的概念_高清 720P\",\"duration\":2780,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i0.hdslb.com/bfs/storyff/n21091716112ci5ov4hwqn1e5n9ek82n_firsti.jpg\"},{\"cid\":409688850,\"page\":2,\"from\":\"vupload\",\"part\":\"003—2022考研数学-基础概率-第一章-概率（一）[余丙森]__高清 720P\",\"duration\":2206,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i2.hdslb.com/bfs/storyff/n21091715370mvmd2abavy1sut0yqy5y_firsti.jpg\"},{\"cid\":409690183,\"page\":3,\"from\":\"vupload\",\"part\":\"004—2022考研数学-基础概率-第一章-概率（二）[余丙森]__高清 720P\",\"duration\":1647,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n210917131pxamicf21ef63ffz9s3lvi_firsti.jpg\"},{\"cid\":409693267,\"page\":4,\"from\":\"vupload\",\"part\":\"04.第一章类型2-5_高清 720P\",\"duration\":3476,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i0.hdslb.com/bfs/storyff/n210917161gvpdn4ckgb3n2th6c33984_firsti.jpg\"},{\"cid\":409690031,\"page\":5,\"from\":\"vupload\",\"part\":\"005—2022考研数学-基础概率-第一章-概率（三）[余丙森]__高清 720P\",\"duration\":2564,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n210917153dqin1zueeruzdw0iq6coxr_firsti.jpg\"},{\"cid\":409692365,\"page\":6,\"from\":\"vupload\",\"part\":\"006—2022考研数学-基础概率-第一章-概率（四）[余丙森]__高清 720P\",\"duration\":2706,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i2.hdslb.com/bfs/storyff/n21091715405tb9pnv6a61tgrz6ddvab_firsti.jpg\"},{\"cid\":409691908,\"page\":7,\"from\":\"vupload\",\"part\":\"007—2022考研数学-基础概率-第一章-事件的独立性（一）[余丙森]__高清 720P\",\"duration\":1924,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n210917162jinklm9a9tpxqphsa3b8t0_firsti.jpg\"},{\"cid\":409692201,\"page\":8,\"from\":\"vupload\",\"part\":\"008—2022考研数学-基础概率-第一章-事件的独立性（二）[余丙森]__高清 720P\",\"duration\":1859,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n210917161vs5nr7tn45sc24ed9z0rgc_firsti.jpg\"},{\"cid\":409695954,\"page\":9,\"from\":\"vupload\",\"part\":\"09.第九讲_20072_高清 720P\",\"duration\":3007,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":1280,\"height\":720,\"rotate\":0},\"first_frame\":\"http://i2.hdslb.com/bfs/storyff/n21091714wgly1gp5ixfk3bjyatgg1v2_firsti.jpg\"},{\"cid\":409692999,\"page\":10,\"from\":\"vupload\",\"part\":\"012—2022考研数学-基础概率-第二章连续型随机变量及其概率分布（二）[余丙森]_流畅 360P\",\"duration\":2436,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":640,\"height\":360,\"rotate\":0},\"first_frame\":\"http://i2.hdslb.com/bfs/storyff/n21091715i0x8hellz3393hoakuuyn64_firsti.jpg\"},{\"cid\":409693785,\"page\":11,\"from\":\"vupload\",\"part\":\"013—2022考研数学-基础概率-第二章连续型随机变量及其概率分布（三）[余丙森]_流畅 360P\",\"duration\":2031,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":640,\"height\":360,\"rotate\":0},\"first_frame\":\"http://i0.hdslb.com/bfs/storyff/n21091714nkmjfnuol1wwibuncwmubhb_firsti.jpg\"},{\"cid\":409693986,\"page\":12,\"from\":\"vupload\",\"part\":\"014—2022考研数学-基础概率-第二章随机变量函数的分布（一）[余丙森]_流畅 360P\",\"duration\":1980,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":640,\"height\":360,\"rotate\":0},\"first_frame\":\"http://i2.hdslb.com/bfs/storyff/n210917131bt97a3j0dxzv2d20o2uhxp_firsti.jpg\"},{\"cid\":409693515,\"page\":13,\"from\":\"vupload\",\"part\":\"015—2022考研数学-基础概率-第二章随机变量函数的分布（二）[余丙森]_流畅 360P\",\"duration\":1860,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":640,\"height\":360,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n210917152z4y2ag3aolli2dh440bbrr_firsti.jpg\"},{\"cid\":409694169,\"page\":14,\"from\":\"vupload\",\"part\":\"016—2022考研数学-基础概率-第三章多维随机变量及其分布[余丙森]_流畅 360P\",\"duration\":2194,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":640,\"height\":360,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n2109171348855gmlpifcrf2routua5x_firsti.jpg\"},{\"cid\":409695901,\"page\":15,\"from\":\"vupload\",\"part\":\"017—2022考研数学-基础概率-第三章二维随机变量（一）[余丙森]_流畅 360P\",\"duration\":2282,\"vid\":\"\",\"weblink\":\"\",\"dimension\":{\"width\":640,\"height\":360,\"rotate\":0},\"first_frame\":\"http://i1.hdslb.com/bfs/storyff/n21091715e71k5l6e139j3j4t9pusc9s_firsti.jpg\"}]}"

type VideoInfo struct {
	bvid string
	title string
	description string
	createdTime int64
}

type VideoDownloadInfo struct {
	bvid string
	cid string
	order int64
	durl string
	size int64
	length int64
}

func getFromUrl(url string) ([]byte , error) {
	request, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil,err
	}
	request.Header.Set("origin", ORIGIN)
	request.Header.Set("referer", REFERER)
	request.Header.Set("User-Agent",USERAGENT)
	respon, err := (&http.Client{}).Do(request)
	if err != nil {
		return make([]byte, 0, 0), err
	}
	requestBody, err := ioutil.ReadAll(respon.Body)
	if err != nil {
		return make([]byte, 0, 0), err
	}
	return requestBody, err
}

func getTotalVideoNum(mid string) (int64 , error) {
	requestBody, err :=  getFromUrl(TotalNumUrl + "mid="+ mid)
	if err != nil{
		return 0, err
	}
	num,err := jsonparser.GetInt(requestBody,"data","video")
	if err != nil {
		return 0, err
	}
	return num, nil
}

func getCidByBvid(bvid string) (*list.List, error) {
	requestBody, err := getFromUrl(CidUrl + "?bvid=" + bvid)
	if err != nil{
		return nil, err
	}

	cidList := list.New()
	_, err = jsonparser.ArrayEach(requestBody, func(value []byte, dataType jsonparser.ValueType, offset int, err error) {
		cid, _, _, _ := jsonparser.Get(value, "cid")
		cidList.PushBack(string(cid))
	}, "data")
	if err != nil{
		return nil, err
	}

	return cidList,nil
}

func GetVideoDownloadInfos(bvid string, cid string) (*list.List, error){
	requestBody, err := getFromUrl(DownloadInfoUrl + "&bvid=" + bvid + "&cid=" + cid)
	if err != nil{
		return nil,err
	}
	videoDownloadInfos := list.New()

	_, err = jsonparser.ArrayEach(requestBody,
		func(value []byte, dataType jsonparser.ValueType, offset int, err error) {
		url,_ := jsonparser.GetString(value, "url")
		length,_ := jsonparser.GetInt(value, "length")
		size,_  := jsonparser.GetInt(value, "size")
		order,_ := jsonparser.GetInt(value, "order")
		videoDownloadInfo := new(VideoDownloadInfo)
		videoDownloadInfo.cid = cid
		videoDownloadInfo.bvid = bvid
		videoDownloadInfo.order = order
		videoDownloadInfo.size = size
		videoDownloadInfo.length = length
		videoDownloadInfo.durl = url
		videoDownloadInfos.PushBack(videoDownloadInfo)
	},
	"data", "durl")
	if err != nil{
		return nil,err
	}
	return videoDownloadInfos,nil
}


func PageGetVideoInfo(pageSize int, pageNum int, mid string) (*list.List, error) {
	requestBody, err := getFromUrl(VideoInfoPageURL + "&ps=" + strconv.Itoa(pageSize) + "&pn=" + strconv.Itoa(pageNum) + "&mid=" + mid)
	if err != nil{
		return nil,err
	}
	videoInfos := list.New()

	_, err = jsonparser.ArrayEach(requestBody,
		func(value []byte, dataType jsonparser.ValueType, offset int, err error) {
			title,_ := jsonparser.GetString(value, "title")
			created,_ := jsonparser.GetInt(value, "created")
			bvid,_  := jsonparser.GetString(value, "bvid")
			description,_ := jsonparser.GetString(value, "description")
			videoInfo := new(VideoInfo)
			videoInfo.title = title
			videoInfo.createdTime = created
			videoInfo.bvid = bvid
			videoInfo.description = description
			videoInfos.PushBack(videoInfo)
		},
		"data", "list","vlist")
	if err != nil{
		return nil,err
	}
	return videoInfos, nil
}

func GetUserAllVideos(mid string) (*list.List , error){
	num,_ := getTotalVideoNum(mid)
	page := int(math.Ceil(float64(num)/PageSize))
	var i = 1
	var videoInfos = list.New()
	for i = 1; i <= page; i++ {
		tmpList,err := PageGetVideoInfo(int(PageSize), i, mid)
		if err != nil {
			return nil,err
		}
		if tmpList!= nil {
			videoInfos.PushBackList(tmpList)
		}
	}
	return videoInfos,nil
}

func DownloadVideo(durl string, name string)(error){
	curDir, err := GetCurrentDir()
	if err != nil {
		return err
	}
	filePath := curDir + "/" + name + ".flv"
	file,err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	request, err := http.NewRequest("GET", durl, nil)
	if err != nil {
		return err
	}
	request.Header.Set("origin", ORIGIN)
	request.Header.Set("referer", REFERER)
	request.Header.Set("User-Agent",USERAGENT)
	respon, err := (&http.Client{}).Do(request)
	if err != nil{
		return err
	}

	defer respon.Body.Close()
	bar:= progressbar.DefaultBytes(respon.ContentLength,"正在下载" , name)
	bar.Clear()
	_,err = io.Copy(io.MultiWriter(file,bar), respon.Body)
	if err != nil{
		return err
	}
	return nil
	/*
	buf := make([]byte, FileChunkSize)
	for{
		index,err := respon.Body.Read(buf)
		if err != nil {
			return err
		}
		file.Write(buf[:index])
	}*/
}

func DownloadUserAllVideos(mid string) error{
	videoInfos,err :=GetUserAllVideos(mid)
	if err != nil {
		return err
	}
	for rawVideoInfo:= videoInfos.Front(); rawVideoInfo!= nil; rawVideoInfo = rawVideoInfo.Next() {
		videoInfo,ok := (rawVideoInfo.Value).(*VideoInfo)
		if (!ok) {
			return errors.New("can not convert " + reflect.TypeOf(rawVideoInfo.Value).String())
		}
		cids,err := getCidByBvid(videoInfo.bvid)
		if err != nil {
			fmt.Println(mid + "Get CID WRONG: bvid is " + videoInfo.bvid )
			fmt.Println(err.Error())
			return nil
		}
		for cid:= cids.Front(); cid!= nil; cid = cid.Next(){
			videoDownloadInfos,err := GetVideoDownloadInfos(videoInfo.bvid, cid.Value.(string))
			if err != nil {
				fmt.Println(mid + "GetVideoDownloadInfos WRONG: bvid is " + videoInfo.bvid + " cid is "+  cid.Value.(string) )
				fmt.Println(err.Error())
				return nil
			}
			for rawVideoDownloadInfo:= videoDownloadInfos.Front(); rawVideoDownloadInfo!= nil; rawVideoDownloadInfo = rawVideoDownloadInfo.Next() {
				videoDownloadInfo := (rawVideoDownloadInfo.Value).(*VideoDownloadInfo)
				if (!ok) {
					return errors.New("can not convert " + reflect.TypeOf(rawVideoDownloadInfo.Value).String())
				}
				err:= DownloadVideo(videoDownloadInfo.durl, videoDownloadInfo.bvid+videoDownloadInfo.cid+ strconv.Itoa(int(videoDownloadInfo.order)))
				if err != nil {
					fmt.Println(mid + "DownloadVideo WRONG: dur is " + videoDownloadInfo.durl )
					fmt.Println(err.Error())
					return nil
				}
			}
		}
	}
	return nil
}

func Filter(videoInfoList *list.List)(*list.List , error){
	//TODO
	return videoInfoList,nil
}

func Test(){
	req, _ := http.NewRequest("GET", "https://dl.google.com/go/go1.14.2.src.tar.gz", nil)
	resp, _ := http.DefaultClient.Do(req)
	defer resp.Body.Close()

	f, _ := os.OpenFile("go1.14.2.src.tar.gz", os.O_CREATE|os.O_WRONLY, 0644)
	defer f.Close()

	bar := progressbar.DefaultBytes(
		resp.ContentLength,
		"downloading",
	)
	_, _ = io.Copy(io.MultiWriter(f, bar), resp.Body)
}

/*

for rawVideoInfo:= videoInfos.Front(); rawVideoInfo!= nil; rawVideoInfo = rawVideoInfo.Next() {
		videoInfo,ok := (rawVideoInfo.Value).(*VideoInfo)
		if (!ok) {
			return nil,errors.New("can not convert " + reflect.TypeOf(rawVideoInfo.Value).String())
		}
		fmt.Printf(videoInfo.title)
		fmt.Printf("\n")
	}
 */