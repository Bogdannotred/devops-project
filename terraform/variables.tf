variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "ecr_repository_name" {
  type    = string
  default = "devops-health-api"
}

variable "app_name" {
  type    = string
  default = "devops-health-api"
}

variable "container_port" {
  type    = number
  default = 8000
}
