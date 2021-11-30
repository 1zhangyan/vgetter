package utils

import (
	"container/list"
	"encoding/csv"
	"io"
	"os"
	"path"
	"strings"
)

const FileName = "userMids.csv"

func GetCurrentDir()(string, error) {
	dir, err := os.Executable()
	if err != nil {
		return "",err
	}
	curDir,_ := path.Split(dir)
	return curDir,nil
}

func GetUserMids()(*list.List, error){
	dir,err := GetCurrentDir()
	if err != nil {
		return nil,err
	}
	csvFile, err := os.Open(dir + "/" + FileName)
	if err != nil {
		return nil,err
	}

	defer csvFile.Close()
	midList := list.New()
	reader := csv.NewReader(csvFile)
	for {
		row, err := reader.Read()
		if err != nil && err != io.EOF{
			return nil,err
		}
		if err == io.EOF {
			break
		}
		mid := strings.Trim(row[0]," ")
		if mid != ""{
			midList.PushBack(strings.Trim(row[0]," "))
		}
	}
	return midList,nil
}
