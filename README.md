# My Labs Challenge

## API Docs (for routes not documented in challenge)

|Route|Method|Data|Return|
|---|---|---|---|
|`/scrape`|GET|N/A|Sucess if scrape was successful|
|`/api/clubs`|POST|JSON list (parameter `data`) with maps containing `name :: string`,`description :: string`, `tags :: string list`|Success if addition was successful|
|`/ascii`|GET|String (parameter `image-url`) containing a HTTP-only url of an image|That image in ASCII art|

## Info on my setup

This is all hosted at [https://labs.walthome.duckdns.org/](https://labs.walthome.duckdns.org/)

### Django

This Django boilerplate is taken from the [template-django](https://github.com/pennlabs/template-django/) repository and modified appropriately.

### Docker

I then used the [django-base](https://github.com/pennlabs/) repo to build a docker image. There was just one problem. Armaan only half-finished the repo. I made a few pull requests and now the thing's finished(ish). It has some problems with serving static files in prod, but I'm working on it. In the words of Armaan, "I have no idea why this isn't working." Same.

### Kubernetes

I then made [a deployment file](k8s/labs-challenge.yaml) and deployed it to my Kubernetes cluster. This cluster is in my homelab created using some [automated deployment files](https://pwpon500.github.io/posts/2019/07/automating-k3s-deployment-on-proxmox/) I created. Because the whole deploy process is automated, I could kill the entire cluster and recreate it in minutes with no repercussions.

### Database

I then used KubeDB to create a [mysql manifest](k8s/labs-mysql.yaml) and applied it. Then, I pulled out the credentials from the secret KubeDB created and created a DATABASE_URL secret. I attached the DATABASE_URL secret to the main deployment, and we're all done!

## Why

You may be asking "Why are you deploying this on Kubernetes? That seems way too complicated." If you only consider this project, you're absolutely right. It would be foolish to create a cluster only to host this project. However, the value from Kubernetes comes as I create more and more projects like this. Each new project is just a simmple deploy file. With that one deploy file, I get replication, automatic SSL, and easy orchestration.

Also, you might be wondering why I'm using KubeDB rather than a DB hosted on a VM. The reasoning is basically the same as why I'm doing the deploy on Kubernetes. I hate making new VMs and spinning up new databases. I'd much rather just make a KubeDB manifest.
