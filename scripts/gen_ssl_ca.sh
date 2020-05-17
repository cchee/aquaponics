#!/bin/bash
# Copyright 2016 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
# This script take a name and create CA root certificate under the directory for the given name

# Check number of args and return usage if error
if [ $# -ne 1 ]; then
  echo "Usage: $0 <company directory name>"
  exit 0
fi

COMPANY=${1}

echo "Generate CA key for ${COMPANY}..."
openssl genrsa -aes256 -out $COMPANY/ca/private/ca.key.pem 4096
chmod 400 $COMPANY/ca/private/ca.key.pem

echo "Generate CA root certificate for ${COMPANY}..."
openssl req -config $COMPANY/ca/openssl.cnf -key $COMPANY/ca/private/ca.key.pem -new -x509 -days 7300 -sha256 -extensions v3_ca -out $COMPANY/ca/certs/ca.cert.pem
chmod 444 $COMPANY/ca/certs/ca.cert.pem

echo "Verifying CA root certificate for ${COMPANY}..."
openssl x509 -noout -text -in $COMPANY/ca/certs/ca.cert.pem

echo "Generate Diffie-Hellman params for ${COMPANY}..."
openssl dhparam -out $COMPANY/ca/certs/dhparams.pem 4096
