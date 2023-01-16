module "aws_vpc" {
    source = "./modules/three-tier"
    vpc_name = "kpmg-vpc"
    app_subnets_cidr_blocks = ["10.0.1.0/24", "10.0.2.0/24"]
    web_subnets_cidr_blocks = ["10.0.3.0/24", "10.0.4.0/24"]
    public_subnets_cidr_blocks = ["10.0.5.0/24", "10.0.6.0/24"]
    db_subnets_cidr_blocks = ["10.0.7.0/24", "10.0.8.0/24"]
    rds_subnet_name = "rds-subnet-group"
    rds_storage = "30"
    rds_engine = "mysql"
    rds_instance_class = "db.t2.micro"
    rds_name = "mysql_rds"
    rds_username = "admin"
    rds_password = "admin@123"
    websg_name = "web-sg"
    web_ami = "ami-0b5eea76982371e91"
    web_instance = "t2.micro"
    webserver_name = ["web1", "web2"]
    lb_name = "applb"
    tg_name = "apptg"
    tg_port = "80"
    listener_port = "443"
    listener_protocol = "HTTPs"
}
