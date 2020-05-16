#!/bin/bash
# Copyright 2016 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
# This script generates the company SSL direcotry.

# Check number of args and return usage if error
if [ $# -ne 2 ]; then
  echo "Usage: $0 <company directory name> <company name>"
  exit 0
fi

COMP_DIR=${1}
COMPANY=${2}
CURR_DIR=`pwd`

mkdir -p $CURR_DIR/$COMP_DIR/ca/private
mkdir -p $CURR_DIR/$COMP_DIR/ca/certs
mkdir -p $CURR_DIR/$COMP_DIR/ca/newcerts
mkdir -p $CURR_DIR/$COMP_DIR/ca/intermediate/private
mkdir -p $CURR_DIR/$COMP_DIR/ca/intermediate/certs
mkdir -p $CURR_DIR/$COMP_DIR/ca/intermediate/csr

echo "sed -e 's?_CURRENT_DIR_?${CURR_DIR}?g' -e 's?_COMPANY_?${COMP_DIR}?g' -e 's?_ORGANIZATION_NAME_?${COMPANY}?g' ssl_template/ca/openssl.cnf > ${CURR_DIR}/${COMP_DIR}/ca/openssl.cnf" | sh
echo "sed -e 's?_CURRENT_DIR_?${CURR_DIR}?g' -e 's?_COMPANY_?${COMP_DIR}?g' -e 's?_ORGANIZATION_NAME_?${COMPANY}?g' ssl_template/ca/intermediate/openssl.cnf > ${CURR_DIR}/${COMP_DIR}/ca/intermediate/openssl.cnf" | sh
