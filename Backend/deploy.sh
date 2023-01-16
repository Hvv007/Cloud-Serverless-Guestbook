#!/bin/bash

echo "`(cat version.json) | jq '.version = .version + 1'`"  > version.json;

backend_version=$(jq -r '.version' version.json);

docker build -t ${GUESTBOOK_API_REPOSITORY_NAME}:0.0.$backend_version . ;

docker push ${GUESTBOOK_API_REPOSITORY_NAME}:0.0.$backend_version;

yc sls container revisions deploy \
	--folder-id ${FOLDER_ID} \
	--container-id ${GUESTBOOK_API_CONTAINER_ID} \
	--memory 512M \
	--cores 1 \
	--execution-timeout 5s \
	--concurrency 8 \
	--environment	AWS_KEY_ID=${AWS_KEY_ID},AWS_SECRET_KEY=${AWS_SECRET_KEY},DOCUMENT_API_ENDPOINT=${DOCUMENT_API_ENDPOINT},BACKEND_VERSION=$backend_version \
	--service-account-id ${APP_SERVICE_ACCOUNT_ID} \
	--image "${GUESTBOOK_API_REPOSITORY_NAME}:0.0.$backend_version";
