provider "aws" {
  access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  region     = "us-east-1"
}

# ---------------------------------------<MAIN>----------------------------------------#
resource "aws_instance" "ServiceNow-simulator" {
  ami             = "ami-04505e74c0741db8d" #Amazon Machine Image
  instance_type   = "t2.small"              #Instance type describing CPU, Architecture, Memory, Storage, Pricing
  key_name        = aws_key_pair.key.key_name
  security_groups = ["security_group_servicenow"]
}
# ---------------------------------------</MAIN>----------------------------------------#

resource "aws_key_pair" "key" {
  key_name   = "servicenow-simulator"
  public_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

resource "aws_security_group" "security_group_servicenow" {
  name = "security_group_servicenow"

  #Incoming traffic
  ingress {
    from_port   = 3000
    to_port     = 9116
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  #Outgoing traffic
  egress {
    from_port   = 3000
    protocol    = "tcp"
    to_port     = 9116
    cidr_blocks = ["0.0.0.0/0"]
  }
}
