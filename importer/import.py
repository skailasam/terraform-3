#!/usr/bin/env python3

import os 
import argparse
import subprocess
from subprocess import Popen

parser = argparse.ArgumentParser(description='Create a shell script for importing TF resources.')
parser.add_argument('tf_state_dir', help='Full path to Terraform dir under Amygdala/terraform/')
parser.add_argument('aws_profile',  help='Name of the appropriate AWS Profile (prod/hub/dev/login/demo)')
# Update this to version 1.0.0
parser.add_argument("--tf14", default='terraform-0.11.14', help="Executable name for your terraform version 0.11.14 binary")
args = parser.parse_args()

tf_import_cmd = f'awsudo -- {args.aws_profile} terraform import'
tf_state_cmd = f'awsudo -- {args.aws_profile} terraform state list'

terraform_reader = args.tf14  # the arg takes the default value if the argument is omitted.

def generate_resource_list():
  # Read in resource_list from file
  # Improvement: run terraform state list and generate file automagically
  with open('resources','w') as file:
    proc = Popen([terraform_reader, "state", "list"], stdout=file, stderr=subprocess.PIPE, universal_newlines=True)
    output, errors = proc.communicate()
  if errors:
    print("  Error running 'terraform state show list': ", errors)
    exit(1)
  resource_list = open("resources.txt", "r").readlines()
  return resource_list

def fetch_resource_attributes(resource):
  attributes = []
  return attributes
  

def match_resources(resource_list):
  with open('resources.map', 'w') as resources_map:
    for resource in resource_list:
      print(resource)
  return

def main():

  # Check for AWS environment credentials
  aws_env = os.environ.get('AWS_PROFILE')
  if aws_env is None:
    print('AWS credentials not found. Run export AWS_PROFILE=<profile_name>')

  
      
  exit(0) #testing
  
  resources = generate_resource_list()
  match_resources(resources)
  return 

main()
