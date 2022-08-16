#!/bin/bash

sudo docker build -t fxnaranjom/crs_be:1.0 --file Dockerfile .
sudo docker tag fxnaranjom/crs_be:1.0 us-east1-docker.pkg.dev/crs-hotel-352722/hotelrepo/crs-be:1
gcloud auth print-access-token | sudo docker login -u oauth2accesstoken --password-stdin us-east1-docker.pkg.dev
sudo docker push us-east1-docker.pkg.dev/crs-hotel-352722/hotelrepo/crs-be:1
