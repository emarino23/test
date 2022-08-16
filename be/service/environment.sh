#!/bin/bash

echo 'TABLAS'
#TABLAS 
export LOG='LOG@WEB'
export PARAM='PARAM@WEB'
export USER='USER@CRS'
export CLIENT='CLIENT@CRS'
export QUOTE='QUOTE@CRS'
export QUOTE_DAY='QUOTE_DAY@CRS'
export QUOTE_DAY_DETAIL='QUOTE_DAY_DETAIL@CRS'

echo 'REGION'

#REGION
export MYCULTURE='es-EC'
export MYDECIMALSEPARATOR=','
export MYGROUPSEPARATOR='.'
export MYDATESEPARATOR='/'
export MYSHORTDATE='DD/MM/YY'
export MYLONGDATE='DD/MM/YYYY'
export MYDECIMALDIGITS='2'

#BASES DE DATOS
export CRS='postgresql://postgres:postgres@172.16.0.129:5432/CRS'
export WEB='postgresql://postgres:postgres@172.16.0.129:5432/WEB'

#CORREO
export MAIL_USER='jose.cuevas.cv@gmail.com'
export MAIL_PASS='vrttwujaqezajqos'
export MAIL_SERVER='smtp.gmail.com'
export MAIL_SERVER_PORT='587'

#CRYPTO
export PKSALT='1qazxsw23edcvfr45tgbnhy67ujm,ki8'

#WEB
export SERVER_PORT='9999'
export SERVER_HOST='127.0.0.1'