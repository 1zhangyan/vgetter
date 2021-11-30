package main

import (
	"fmt"
	"vgetter/utils"

	"os"
	"strings"
)

func main() {

	fmt.Println("***********OPEN SOURCE CODE SOFTWARE**********")
	fmt.Println("*        FOR LEANING OR COMMUNICATION        *")
	fmt.Println("*        FORBIDDEN COMMERCIAL PURPOSE        *")
	fmt.Println("*               VERSION 1.0                  *")
	fmt.Println("**********************************************")
	fmt.Println("默认下载路径： 当前文件所在路径")
	fmt.Println("默认UP主mid信息：当前文件所在路径下csv文件")
	fmt.Println("按任意键继续下载 ")
	fmt.Println("按q键退出程序")
	fmt.Println("开始下载后不要关闭黑框 最小化运行即可")
	var command string
	fmt.Scanln(&command)
	if strings.Compare(command,"q") == 0 {
		os.Exit(0)
	}
	mids,err := utils.GetUserMids()
	if err != nil {
		fmt.Println(err.Error())
		return
	}
	for rawMid := mids.Front(); rawMid!=nil; rawMid = rawMid.Next(){
		utils.DownloadUserAllVideos(rawMid.Value.(string))
	}
	return
}


