#!/bin/bash
# Copyright 2016 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
# This script generates the intermediate SSL certificate. Intermediate SSL certificate makes revoking client and server certificate easy without
# the hassle to re-generating the root CA certificate. 

# Check number of args and return usage if error
if [ $# -ne 1 ]; then
  echo "Usage: $0 <company directory name>"
  exit 0
fi

COMPANY=${1}

echo "Generate Intermediate Key for ${COMPANY}..."
openssl genrsa -aes256 -out $COMPANY/ca/intermediate/private/intermediate.key.pem 4096
chmod 400 $COMPANY/ca/intermediate/private/intermediate.key.pem

echo "Generate Intermediate Certificate Signing Request (CSR) for ${COMPANY}..."
openssl req -config $COMPANY/ca/intermediate/openssl.cnf -new -sha256 -key $COMPANY/ca/intermediate/private/intermediate.key.pem -out $COMPANY/ca/intermediate/csr/intermediate.csr.pem
chmod 400 $COMPANY/ca/intermediate/csr/intermediate.csr.pem

echo "Generate Intermediate Certificate for ${COMPANY}..."
openssl ca -config $COMPANY/ca/openssl.cnf -extensions v3_intermediate_ca -days 3650 -notext -md sha256 -in $COMPANY/ca/intermediate/csr/intermediate.csr.pem -out $COMPANY/ca/intermediate/certs/intermediate.cert.pem
chmod 400 $COMPANY/ca/intermediate/certs/intermediate.cert.pem

echo "Verify Intermediate Certificate for ${COMPANY}..."
openssl x509 -noout -text -in $COMPANY/ca/intermediate/certs/intermediate.cert.pem

echo "Verify Intermediate Certificate against root certificate for ${COMPANY}..."
openssl verify -CAfile $COMPANY/ca/certs/ca.cert.pem $COMPANY/ca/intermediate/certs/intermediate.cert.pem

cat $COMPANY/ca/intermediate/certs/intermediate.cert.pem $COMPANY/ca/certs/ca.cert.pem > $COMPANY/ca/intermediate/certs/ca-chain.cert.pem
chmod 400 $COMPANY/ca/intermediate/certs/ca-chain.cert.pem

echo "Verify CA Chain Certificate for ${COMPANY}..."
openssl verify -CAfile $COMPANY/ca/certs/ca.cert.pem $COMPANY/ca/intermediate/certs/ca-chain.cert.pem

echo "Generate Diffie-Hellman params and DSA Certificate for ${COMPANY}..."
openssl dhparam -outform PEM -out $COMPANY/ca/intermediate/certs/dhparams.pem 4096
openssl dsaparam -out $COMPANY/ca/intermediate/certs/dsaparams.pem 4096
openssl req -config $COMPANY/ca/intermediate/openssl.cnf -out $COMPANY/ca/intermediate/csr/dsa.csr.pem -keyout $COMPANY/ca/intermediate/private/dsa.key.pem -newkey dsa:$COMPANY/ca/intermediate/certs/dsaparams.pem
openssl ca -config $COMPANY/ca/intermediate/openssl.cnf -in $COMPANY/ca/intermediate/csr/dsa.csr.pem -out $COMPANY/ca/intermediate/certs/dsa.cert.pem

