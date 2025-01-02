# Infrastructure as Code (IaC) with Ansible

## Table of Contents
- [What is Infrastructure as Code (IaC)?](#what-is-infrastructure-as-code-iac)
  - [Why is IaC Important?](#why-is-iac-important)
- [What is Ansible?](#what-is-ansible)
  - [Key Features of Ansible](#key-features-of-ansible)
- [Navigate to the Exercise Directory](#navigate-to-the-exercise-directory)
- [Step 1: Install pipx](#step-1-install-pipx)
- [Step 2: Install Ansible with pipx](#step-2-install-ansible-with-pipx)
- [Step 3: Setting Up an Inventory File](#step-3-setting-up-an-inventory-file)
- [Step 4: Running an Ansible Playbook](#step-4-running-an-ansible-playbook)
  - [Verify the Output](#verify-the-output)
- [Final Objective](#final-objective)

---

## What is Infrastructure as Code (IaC)?

Infrastructure as Code (IaC) is a modern approach to managing and provisioning computing infrastructure through code, rather than manual processes. With IaC, infrastructure configuration and deployment are defined in machine-readable scripts, allowing infrastructure to be versioned, tested, and reproduced just like software code.

### Why is IaC Important?

- **Consistency**: IaC helps eliminate configuration drift and ensures that environments are consistent across development, testing, and production.
- **Efficiency**: Manual infrastructure management is time-consuming. IaC automates repetitive tasks, making setup faster and reducing human error.
- **Scalability**: With IaC, scaling infrastructure up or down is much easier, especially in environments like cloud computing where resources can be dynamically adjusted.
- **Version Control**: Since infrastructure is managed as code, all changes can be tracked through version control, enabling rollback if an issue arises.

---

## What is Ansible?

Ansible is an open-source automation tool primarily used for configuration management, application deployment, and task automation. With its simple YAML syntax, Ansible allows developers and operators to describe the desired state of systems without needing to write complex code.

### Key Features of Ansible

- **Agentless**: No need to install additional software on the target machines.
- **Idempotency**: Ensures that applying the same configuration multiple times yields the same result.
- **Flexibility**: Supports a wide range of modules for different environments.

---

## Navigate to the Exercise Directory

To begin, navigate to the directory for Exercise 4.1:

```bash
cd sre-abc-training/exercises/exercise4.1
```

This directory contains the necessary files for the exercise.

---

## Step 1: Install pipx

`pipx` is a tool to install and run Python applications in isolated environments. To install `pipx` on macOS:

```bash
brew install pipx
pipx ensurepath
```

---

## Step 2: Install Ansible with pipx

Once `pipx` is installed, use it to install Ansible. This approach ensures Ansible and its dependencies are managed in a virtual environment.

```bash
pipx install --include-deps ansible
pipx upgrade --include-injected ansible
pipx inject --include-apps ansible argcomplete
```

Verify the installation:
```bash
ansible --version
```

---

## Step 3: Setting Up an Inventory File

The required files for this exercise, including `inventory.ini` and `playbook.yaml`, are already provided in the `ansible_quickstart` directory. You do not need to create them manually. Here's the content for reference:

### Inventory File: `inventory.ini`

```ini
[allhosts]
127.0.0.1 ansible_connection=local
```

This file tells Ansible to connect to the localhost (`127.0.0.1`) using the local connection method.

---

## Step 4: Running an Ansible Playbook

To run the provided playbook, execute the following command:

```bash
ansible-playbook -i inventory.ini playbook.yaml --ask-become-pass
```

> **Note**: When prompted, enter your system password. This is required to elevate privileges for certain tasks.

### Verify the Output

The output should look like this if everything worked as expected:

```bash
BECOME password:

PLAY [My first play] *************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************
[WARNING]: Platform darwin on host 127.0.0.1 is using the discovered Python interpreter at /opt/homebrew/bin/python3.13, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [127.0.0.1]

TASK [Ping my hosts] *************************************************************************************************************
ok: [127.0.0.1]

TASK [Print message] *************************************************************************************************************
ok: [127.0.0.1] => {
    "msg": "Hello world"
}

PLAY RECAP ***********************************************************************************************************************
127.0.0.1                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Breakdown of the Output

1. **Gathering Facts**:
   - Ansible collects system information about the target host (`127.0.0.1`) for use in playbooks.

2. **Ping my hosts**:
   - This task sends a ping to the target host and confirms connectivity.

3. **Print message**:
   - Outputs the message "Hello world" using the `debug` module.

4. **Play Recap**:
   - Summarizes the outcome of all tasks:
     - `ok`: The task ran successfully.
     - `changed`: Tasks that modified the system.
     - `failed`: Tasks that encountered errors.

---

## Final Objective

At the end of this exercise, you should accomplish the following:

> **Important**  
> Use Ansible to execute tasks defined in the playbook. Ensure you run the playbook (`playbook.yaml`) with the provided inventory file (`inventory.ini`) and observe the successful execution of all tasks.  
> 
> Example:
> ```bash
> ansible-playbook -i inventory.ini playbook.yaml --ask-become-pass
> ```
> When prompted, enter your system password. This allows privilege elevation for the required tasks. Confirm the results by reviewing the output in the terminal.

---