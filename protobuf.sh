#!/bin/bash

VERSION=3.5.1

if [ -z "$1" ]; then
    echo "-v args not set, use default ${VERSION}"
else
    VERSION=$1
fi


FILE=proto3.zip
DIR=proto3

# Make sure you grab the latest version
curl -L -o ${FILE} https://github.com/google/protobuf/releases/download/v${VERSION}/protoc-${VERSION}-linux-x86_64.zip

if [ -d ${DIR} ]; then
    rm -rf ${DIR}
fi

# Unzip
unzip ${FILE} -d ${DIR}
rm -f ${FILE}

# Move protoc to /usr/local/bin/
sudo \mv -f ${DIR}/bin/* /usr/local/bin/

# Move protoc3/include to /usr/local/include/
if [[ ! (-d /usr/local/include/google) ]]; then
    sudo mkdir -p /usr/local/include/google
fi

sudo \mv -f ${DIR}/include/google/protobuf /usr/local/include/google/protobuf

sudo chmod 755 /usr/local/bin/protoc
sudo chmod -R 755 /usr/local/include/google

rm -rf ${DIR}
