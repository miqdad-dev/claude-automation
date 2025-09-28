# Docker Compose Infrastructure

This project uses Ansible to provision a Docker Compose infrastructure on a host.

## What it does
This Ansible playbook will ensure that Docker and Docker Compose are installed on the host, copy a Docker Compose file to the host, and execute `docker-compose up -d`.

## How it works
The playbook is divided into several tasks:

- **Ensure docker is installed.**
- **Ensure docker-compose is installed.**
- **Ensure directory exists for docker-compose file.**
- **Copy docker-compose file to remote.**
- **Run docker-compose up -d.**

The Docker Compose file runs an Nginx container and exposes port 80.

## How to run
1. Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).
2. Clone this repository and navigate to the `devops-infrastructure` directory.
3. Run the playbook with the `ansible-playbook ansible/playbook.yml` command.

## Example usage
After running the playbook, you should be able to access the Nginx welcome page by navigating to `http://localhost` in your web browser.

## Notes on architecture & tradeoffs
This project is a simple example of how to use Ansible to manage Docker Compose infrastructures. For more complex scenarios, you might want to consider using Ansible roles and include more error checking in your tasks.