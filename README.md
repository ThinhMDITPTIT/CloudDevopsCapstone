[![CircleCI](https://circleci.com/gh/ThinhMDITPTIT/CloudDevopsCapstone/tree/main.svg?style=svg)](https://circleci.com/gh/ThinhMDITPTIT/CloudDevopsCapstone/tree/main)

# CloudDevopsCapstone
AWS Cloud Devops Engineer program

The project has followed the instruction from tutorials and examples for the cloud DevOps capstone:
https://medium.com/@andresaaap/capstone-cloud-devops-nanodegree-4493ab439d48

In this Capstone project, I've applied the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program to build the application. The project could be devide into steps by steps:
- Setup AWS configure
- Use CircleCI to implement CICD for application
- Build Application pipeline
- Build k8s cluster
- Build Docker image and upload to Docker Hub repository
- Deploy Docker container to Kubernetes cluster
- Build Ansible roles, CloudFormation stacks to create network, nodegroup as well as deploy eks cluster

The pipeline follow CircleCI my_workflow:
- build:
	+ This job used to prepare the working environment for project and check lint syntax,...
- docker_upload:
	+ This job used to build the docker image with tag, then push/upload the image to Docker Hub repository
- deployment_infra:
	+ This job used to create the cloudformation stack to build and prepare everything like: EKS network, EKS cluster, EKS Nodegroup and host management,...
- configure_infra:
	+ This job used to authentication AWS, set up AWS congfigure options as well as config Kubernetes cluster
- cluster_configure:
	+ This job used to setup service and prepare deployment, it also get and store Elastic Load Balancer DNS to local file
- docker_deployment:
	+ This last job used to deploy docker image (from Docker Hub repository) to Kubernetes cluster

Screenshots results:
- CircleCI pipeline workflow successfully:
![circle_ci_pipe_success](https://user-images.githubusercontent.com/56442337/174252236-1cc092aa-dfd4-48b6-ba1e-277214eea34b.png)
- CloudFormation stacks:
![image](https://user-images.githubusercontent.com/56442337/174250594-6c350b9c-5ccb-46ee-9b6a-03e1504202a5.png)
- EC2 instances
![elc2_instances](https://user-images.githubusercontent.com/56442337/174251220-3cf98202-b807-4a07-8086-efeb84e7d795.png)
- Run lint failure
![lint_failed](https://user-images.githubusercontent.com/56442337/174251298-4b935aa7-7557-42fa-9d01-45ec3fff4cf4.png)
- Run lint successfully
![lint_success](https://user-images.githubusercontent.com/56442337/174251393-facf6d2e-9224-4e0f-8554-789eebd6d3a4.png)
- Load Balancer IP
![lb_dns_configure](https://user-images.githubusercontent.com/56442337/174251609-e4a6ada0-70e4-4e1c-b2d0-84c8422e0623.png)
- Docker image application deployment
![docker_image_deploy](https://user-images.githubusercontent.com/56442337/174251750-fe467c49-b66e-4662-a381-1c0eb99cb7db.png)
- Web application result:
- URL: http://af05d85cc147443c283ef4ce49eccdfe-105490069.us-east-1.elb.amazonaws.com/
![elb_dns_web_app](https://user-images.githubusercontent.com/56442337/174251897-b29a46ad-4de3-4947-abba-2c3eefc67fb0.png)
