provider "aws" {
  access_key = "XXXXXXXXXXXXXX"
  secret_key = "XXXXXXXXXXXXXX"
  region     = "us-east-1"
}


# ---------------------------------------<Jenkins>-----------------------------------------#
resource "aws_instance" "Jenkins-ServiceNow-simulator" {
  ami             = "ami-04505e74c0741db8d"
  instance_type   = "t2.micro"
  key_name        = aws_key_pair.key.key_name
  security_groups = ["security_group_servicenow"]
}
# ---------------------------------------</Jenkins>----------------------------------------#


# ---------------------------------------<Production>--------------------------------------#
resource "aws_instance" "Prod-ServiceNow-simulator" {
  ami             = "ami-04505e74c0741db8d"
  instance_type   = "t2.small"
  key_name        = aws_key_pair.key.key_name
  security_groups = ["security_group_servicenow"]
}
# ---------------------------------------</Production>-------------------------------------#


resource "aws_key_pair" "key" {
  key_name   = "servicenow-simulator"
  public_key = "XXXXXXX"
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

  ingress {
    from_port   = 22
    to_port     = 22
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
