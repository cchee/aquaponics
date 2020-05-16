#!/bin/bash
# Copyright 2016 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
# This script generates client side SSL key and self-signed certificates file based on intermediate CA. It also creates bundled PEM file.

# Check number of args and return usage if error
if [ $# -ne 1 ]; then
  echo "Usage: $0 <company directory name>"
  exit 0
fi

COMPANY=${1}

echo "Genearate SSL key for ${EMAIL} for ${COMPANY}..."
openssl genrsa -aes256 -out $COMPANY/ca/intermediate/private/client.key.pem 2048
chmod 400 $COMPANY/ca/intermediate/private/client.key.pem

echo "Generate SSL certificate signing request (CSR) for ${COMPANY}..."
openssl req -config $COMPANY/ca/intermediate/openssl.cnf -key $COMPANY/ca/intermediate/private/client.key.pem -new -sha256 -out $COMPANY/ca/intermediate/csr/client.csr.pem

echo "Generate SSL certificate using intermediate CA for ${COMPANY}..."
openssl ca -config $COMPANY/ca/intermediate/openssl.cnf -extensions usr_cert -days 375 -notext -md sha256 -in $COMPANY/ca/intermediate/csr/client.csr.pem -out $COMPANY/ca/intermediate/certs/client.cert.pem
chmod 400 $COMPANY/ca/intermediate/certs/client.cert.pem

echo "Verify the client SSL certificate for ${COMPANY}..."
openssl x509 -noout -text -in $COMPANY/ca/intermediate/certs/client.cert.pem

echo "Verify the client SSL certificate against CA chain certificate for ${COMPANY}..."
openssl verify -CAfile $COMPANY/ca/intermediate/certs/ca-chain.cert.pem $COMPANY/ca/intermediate/certs/client.cert.pem

echo "Create bundle cert pem for ${COMPANY}..."
cat $COMPANY/ca/intermediate/certs/client.cert.pem $COMPANY/ca/intermediate/certs/ca-chain.cert.pem $COMPANY/ca/intermediate/private/client.key.pem > $COMPANY/ca/intermediate/certs/bundle.cert.pem
