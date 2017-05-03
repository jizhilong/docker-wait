# what does this example project do?
this example shows how to run an arbitary bash script before a container's entrypoint starts with `docker-wait`.

# how to run this example project?
run `docker-compose up --build --force-recreate --abort-on-container-exit`

# what you will see?
you will see the output of both two containers and the output of `docker-compose`, on my Mac Book Pro, it looks the content of
[output.txt](output.txt)

# how this example works?
1. 2 scirpts are added to the customized dresponse image, which will be executed by the dresponse app before each container's 
image entrypoint/cmd starts.What the scripts do is printing out the container's and its images' attributes.
2. both the dresponse and the dwait container are managed by the `docker-compose.yml`.
