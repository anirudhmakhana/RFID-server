#!/bin/bash
# SCRIPT WILL START THE ADAPTER SERVER
python app.py & \ # will run flask server that runs RFID interface
lt --port 1337 --subdomain p2plib-adapter && fg # localtunnel to expose flask server
