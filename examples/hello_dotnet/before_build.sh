#!/bin/bash -e

dotnet build
# dotnet publish -c Release -r linux-x64 --self-contained true
dotnet publish -c Release -r linux-x64 --self-contained true /p:PublishSingleFile=true
