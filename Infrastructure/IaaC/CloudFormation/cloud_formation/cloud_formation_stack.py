import os
from aws_cdk import Stack, aws_ec2
from constructs import Construct
from dotenv import load_dotenv

# load our env file
print("Loading env file")
load_dotenv()


class CloudFormationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.instance_name = "ServiceNow-simulator"
        self.instance_type = "t2.small"
        self.ami_name = "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20211129"
        self.vpc_name = os.getenv("VPC_NAME")

        print(f"Looking up AMI: {self.ami_name}")
        ami_image = aws_ec2.MachineImage().lookup(name=self.ami_name)
        if not ami_image:
            print("Failed finding AMI image")
            return

        print(f"Looking up instance type: {self.instance_type}")
        instance_type = aws_ec2.InstanceType(self.instance_type)
        if not instance_type:
            print("Failed finding instance")
            return

        print(f"Using VPC: {self.vpc_name}")
        vpc = aws_ec2.Vpc.from_lookup(self, "first_vpc", vpc_id=self.vpc_name)
        if not vpc:
            print("Failed finding VPC")
            return

        print("Creating security group")
        sec_grp = aws_ec2.SecurityGroup(
            self, "ec2-sec-grp", vpc=vpc, allow_all_outbound=True
        )
        if not sec_grp:
            print("Failed finding security group")
            return

        print("Creating inbound firewall rule")
        sec_grp.add_ingress_rule(
            peer=aws_ec2.Peer.ipv4("0.0.0.0/24"),
            description="inbound SSH",
            connection=aws_ec2.Port.tcp(22),
        )

        if not sec_grp:
            print("Failed creating security group")
            return

        print(
            f"Creating EC2 Instance: {self.instance_name} using {self.instance_type} with ami: {self.ami_name}"
        )
        ec2_inst = aws_ec2.Instance(
            self,
            "ec2_inst",
            instance_name=self.instance_name,
            instance_type=instance_type,
            machine_image=ami_image,
            vpc=vpc,
            security_group=sec_grp,
        )
        if not ec2_inst:
            print("Failed creating ec2 instance")
            return
