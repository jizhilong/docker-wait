package dwait

import (
	"bufio"
	"bytes"
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"os"
	"os/exec"
	"regexp"
	"syscall"
)

const (
	authTokenPath = "/.dwaitauthtoken"
)

type ContainerId struct {
	ID string `json:"container_id"`
}

type ExecInfo struct {
	Entrypoint []string `json:"entrypoint"`
	Command    []string `json:"command"`
	AuthToken  string   `json:"token"`
}

func unixDial(proto, addr string) (conn net.Conn, err error) {
	return net.Dial("unix", "/.dwait/dwait.sock")
}

func GetContainerId() (container ContainerId, err error) {
	ubuntuPattern := regexp.MustCompile(`docker/(?P<Id>[a-z0-9]{64})`)
	centosPattern := regexp.MustCompile(`docker-(?P<Id>[a-z0-9]{64})`)
	file, err := os.Open("/proc/self/cgroup")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var ret [][]byte
	for scanner.Scan() {
		line := scanner.Text()
		ret = ubuntuPattern.FindSubmatch([]byte(line))
		if ret != nil {
			break
		}
		ret = centosPattern.FindSubmatch([]byte(line))
		if ret != nil {
			break
		}
	}

	if ret == nil {
		panic(errors.New("can't find container id from /proc/self/cgroup"))
	}

	return ContainerId{ID: string(ret[1])}, nil
}

func (execinfo *ExecInfo) Execute() (err error) {
	var argv []string
	argv = append(execinfo.Entrypoint, execinfo.Command...)
	path, err := exec.LookPath(argv[0])
	if err != nil {
		return
	}
	fmt.Printf("entrypoint: %s\n", execinfo.Entrypoint)
	fmt.Printf("command: %s\n", execinfo.Command)
	fmt.Printf("argv: %s\n", argv)
	fmt.Printf("path: %s\n", path)
	return syscall.Exec(path, argv, syscall.Environ())
}

func GetAuthToken() (token string, err error) {
	content, err := ioutil.ReadFile(authTokenPath)
	if err != nil {
		return
	}
	return string(content), nil
}

func SetAuthToken(token string) (err error) {
	return ioutil.WriteFile(authTokenPath, []byte(token), 0600)
}

func (container *ContainerId) RequestDresponse(path string) (resp *http.Response, err error) {
	tr := &http.Transport{
		Dial: unixDial,
	}
	client := &http.Client{Transport: tr}

	container_str, err := json.Marshal(container)
	if err != nil {
		return
	}

	req, err := http.NewRequest("POST", "http://d"+path,
		bytes.NewBuffer(container_str))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")
	authToken, err := GetAuthToken()
	if err == nil {
		req.Header.Add("Auth-Token", authToken)
	}

	return client.Do(req)
}

func (container *ContainerId) GetExecInfo() (execinfo ExecInfo, err error) {
	resp, err := container.RequestDresponse("/dwait")
	if err != nil {
		return
	}
	defer resp.Body.Close()

	content, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return
	}
	err = json.Unmarshal(content, &execinfo)
	if err != nil {
		return
	}
	return execinfo, nil
}
