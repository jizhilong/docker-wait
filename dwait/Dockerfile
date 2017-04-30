FROM golang:1.6

ENV SOURCE /go/src/github.com/jizhilong/docker-wait/dwait

ADD . $SOURCE
WORKDIR $SOURCE
ENV CGO_ENABLED=0
RUN go build -v -ldflags '-extldflags "-static"' -o bin/dwait
WORKDIR $SOURCE/bin
RUN ln -sf dwait init && ln -sf dwait reboot
