provider "aws" {
  access_key = "AKIAQMNBOBOR2W76GH6X"
  secret_key = "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"
  region     = "us-east-1"
}


# ---------------------------------------<Production>--------------------------------------#
resource "aws_instance" "ServiceNow-simulator-production" {
  ami             = "ami-04505e74c0741db8d"
  instance_type   = "t2.small"
  key_name        = aws_key_pair.key.key_name
  security_groups = ["security_group_servicenow"]
}
# ---------------------------------------</Production>-------------------------------------#

# ---------------------------------------<Monitoring>--------------------------------------#
resource "aws_instance" "ServiceNow-simulator-mon" {
  ami             = "ami-04505e74c0741db8d"
  instance_type   = "t2.small"
  key_name        = aws_key_pair.key.key_name
  security_groups = ["security_group_servicenow"]
}
# ---------------------------------------</Monitoring>-------------------------------------#

resource "aws_key_pair" "key" {
  key_name   = "servicenow-simulator"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZkn/ncB5YVQMSCLjMcpgfpTVCNTkdFAAz5oPSpXDkQLJzN+mFIroOchoNnul7BFFqwaOUirJu6rma7oIc1hH+4472HqdqpM01zhv329LsSXx2B70tQ7b1hCTg9eljVzVowmO8w+442e1wzeWktqzXp6BxPgoBYPkjKRKKUoKBwhIeCzV+tlECE3Ijt7p7Y6CQp3RTvnxJsM0meS8VchvB1daEpvxPJ7s2pgr+Vuhlj0y4wK6xMbEJJspU8Zf4qDb9q+A7mhPbuBih0NsLcqd6KXQLgbKxLpu8rT5NduQyeepIN9sD4Y9eDo7/ko3SaTU3MhZoxq+CR985w1Vddsqx rsa-key-20220715"
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


  egress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

}
