#!/bin/bash -eux

docker run -it --rm --name run_http_server_container \
            -v "$(pwd)/served_assets:/usr/local/run" \
            -p 8000:8000 \
            bgoldstone/http_server:latest \
	          bash /usr/local/run/run_http_server.sh

