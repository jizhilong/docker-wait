package main

import (
	"fmt"
	dwait "github.com/jizhilong/docker-wait/dwait/d"
	"os"
	"path/filepath"
	"time"
)

func init_() {
	pid := os.Getpid()
	if pid != 1 {
		fmt.Fprintf(os.Stderr, "dwait init should run as the init process!\n")
		os.Exit(1)
	}
	container, err := dwait.GetContainerId()
	if err != nil {
		panic(err)
	}
	var execinfo dwait.ExecInfo
	for {
		execinfo, err = container.GetExecInfo()
		if err == nil {
			break
		}
		fmt.Printf("error requesting dresponse: %s\n", err)
		time.Sleep(time.Duration(2) * time.Second)
	}

	dwait.SetAuthToken(execinfo.AuthToken)

	execinfo.Execute()
}

func reboot() (err error) {
	container, err := dwait.GetContainerId()
	if err != nil {
		fmt.Fprintf(os.Stderr, "can'd find id of this container\n")
		return
	}
	fmt.Printf("rebooting container: %s\n", container.ID)
	container.RequestDresponse("/reboot")
	return
}

func main() {
	_, progName := filepath.Split(os.Args[0])
	if progName == "dwait" || progName == "init" {
		init_()
	} else if progName == "reboot" {
		reboot()
	} else {
		fmt.Fprintf(os.Stderr, "unknown command %s\n", progName)
		os.Exit(127)
	}
}
