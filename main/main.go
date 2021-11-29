package main

import (
	"fmt"
	"vgetter/httputils"
)

func main() {

/*
	for li := lis.Front(); li!= nil; li = li.Next() {
		fmt.Printf("\n")
		fmt.Printf(li.Value.(string))
	}
*/
	err := httputils.Test()
	if err != nil {
		fmt.Printf(err.Error())
	}
	return
}

