module "aws_vpc" {
    source = "./modules/vpc"
    vpc_name = "kpmg-vpc"
    app_subnets_cidr_blocks = ["10.0.1.0/24", "10.0.2.0/24"]
    web_subnets_cidr_blocks = ["10.0.3.0/24", "10.0.4.0/24"]
    public_subnets_cidr_blocks = ["10.0.5.0/24", "10.0.6.0/24"]
    db_subnets_cidr_blocks = ["10.0.7.0/24", "10.0.8.0/24"]


}
