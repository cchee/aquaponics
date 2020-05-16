#!/bin/bash
# Copyright 2016 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
# This scripts generates keystore file for SSL certificate validation based on private key and PEM file.

# Check number of args and return usage if error
if [ $# -lt 1 ]; then
  echo "Usage: $0 <company directory name> <keystore password> [keystore private key pem] [client bundle certs pem] [alias]"
  echo "WARNING: This removes intermediate CA file for in company directory."
  exit 0
fi

COMPANY=${1}
ALIAS=${2:-client}
KEY=${3:-client.key.pem}
BUNDLE=${4:-bundle.cert.pem}

echo "Converting the certificates and private key to PKCS 12 for ${COMPANY}..."
openssl pkcs12 -export -in $COMPANY/ca/intermediate/certs/$BUNDLE -inkey $COMPANY/ca/intermediate/private/$KEY -name $ALIAS -out $COMPANY/ca/intermediate/certs/$COMPANY.p12

echo "Import the certificates into keystore for ${COMPANY}..."
mkdir -p $COMPANY/ca/intermediate/ks
keytool -importkeystore -destkeystore $COMPANY/ca/intermediate/ks/$COMPANY.jks -srckeystore $COMPANY/ca/intermediate/certs/$COMPANY.p12 -srcstoretype PKCS12
