[![tests](https://github.com/boutetnico/ansible-role-percona-xtrabackup/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-percona-xtrabackup/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.percona_xtrabackup-blue.svg)](https://galaxy.ansible.com/boutetnico/percona_xtrabackup)

ansible-role-percona-xtrabackup
============================

This role installs [Percona XtraBackup](https://docs.percona.com/percona-xtrabackup/innovation-release/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable                           | Required | Default       | Choices   | Comments                                          |
|------------------------------------|----------|---------------|-----------|---------------------------------------------------|
| percona_xtrabackup_packages        | true     |               | list      | See `defaults/main.yml`.                          |
| percona_xtrabackup_package_version | true     | `present`     | string    | Use `latest` to update.                           |

Dependencies
------------

- [percona-release role](https://github.com/boutetnico/ansible-role-percona-release/)

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-percona-xtrabackup


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
