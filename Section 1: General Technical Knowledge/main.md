1. What are the key security concerns when it comes to DevOps?

   > Secrets and secrets management, up to date systems( avoid vulnerabilities), public facing resources, RBAC, traffic, logs, human error, backups.

2. How do you design a self-healing distributed service?
   
   > Automatic failure handling, every component in the service should have atleats a pair. 
   Be able to auto drop from the customer traffic failed components.
   Automatically restart failed components(self-healing).   

3. Describe a centralized logging solution and you can implement logging for a  microservice architecture
   >The setup depends on the load. For simple configurations, it typically consists of a set of Loki instances or even Grafana Cloud. In heavy envs, it involves an ES or OS cluster. This cluster often includes a dedicated ingest node, with Kafka placed in front to handle future log spikes and enable maintenance without losing messages. Additionally, the setup includes backups, monitoring, and alerting mechanisms, and the documentation(!)
   
4. What are some of the reasons for choosing Terraform for DevOps?
   > Popular, in active developent, keep states in the remote(s3), lock feature(dynamoDB), types and structures based on GO, support clouds, declarative lang for IaC

5. How would you design and implement a secure CI/CD architecture for microservice deployment using GitOps? Take a scenario of 20 microservices developed using different languages and deploying to an orchestrated environment like Kubernetes.(You can add a low-level architectural diagram)
   
6. You notice React Native builds are failing intermittently. What’s your debugging process?
   >Read logs in failed builds, find the root cause. Unstable network, rate limit for external libs, free space on Cthe build machine.