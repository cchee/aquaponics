#!/bin/bash
# Copyright 2016 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
# This script generates the server side SSL key and self-signed certificate files based on the intermediate CA file. It also generate the bundled PEM file.

# Check number of args and return usage if error
if [ $# -ne 2 ]; then
  echo "Usage: $0 <company directory name> <server name>"
  echo "Note: Make sure the server name matches FQDN of the web server."
  exit 0
fi
COMPANY=${1}
HOSTNAME=${2}

echo "Genearate SSL key for ${HOSTNAME} for ${COMPANY}..."
openssl genrsa -aes256 -out $COMPANY/ca/intermediate/private/$HOSTNAME.key.pem 2048
chmod 400 $COMPANY/ca/intermediate/private/$HOSTNAME.key.pem

echo "Generate SSL certificate signing request (CSR) for ${COMPANY}..."
openssl req -config $COMPANY/ca/intermediate/openssl.cnf -key $COMPANY/ca/intermediate/private/$HOSTNAME.key.pem -new -sha256 -out $COMPANY/ca/intermediate/csr/$HOSTNAME.csr.pem

echo "Generate SSL certificate using intermediate CA for ${COMPANY}..."
openssl ca -config $COMPANY/ca/intermediate/openssl.cnf -extensions server_cert -days 375 -notext -md sha256 -in $COMPANY/ca/intermediate/csr/$HOSTNAME.csr.pem -out $COMPANY/ca/intermediate/certs/$HOSTNAME.cert.pem
chmod 400 $COMPANY/ca/intermediate/certs/$HOSTNAME.cert.pem

echo "Verify the server SSL certificate for ${COMPANY}..."
openssl x509 -noout -text -in $COMPANY/ca/intermediate/certs/$HOSTNAME.cert.pem

echo "Verify the server SSL certificate against CA chain certificate for ${COMPANY}..."
openssl verify -CAfile $COMPANY/ca/intermediate/certs/ca-chain.cert.pem $COMPANY/ca/intermediate/certs/$HOSTNAME.cert.pem
