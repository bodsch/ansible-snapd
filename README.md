
# Ansible Role:  `snapd`

Disable and removes (purges) snapd and related services/packages.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-snapd/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-snapd)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-snapd)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-snapd/actions
[issues]: https://github.com/bodsch/ansible-snapd/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-snapd/releases
[quality]: https://galaxy.ansible.com/bodsch/snapd


## Requirements & Dependencies

- None

### Operating systems

Tested on

* Debian based
    - Debian 10 / 11
    - Ubuntu 20.04 / 22.04

## usage

```
snapd_purge: true

snapd_state: stopped
snapd_enabled: false

snapd_block_later_installation: true

snapd_services:
  - snapd.apparmor.service
  - snapd.autoimport.service
  - snapd.core-fixup.service
  - snapd.recovery-chooser-trigger.service
  - snapd.seeded.service
  - snapd.service
  - snapd.snap-repair.timer
  - snapd.socket
  - snapd.system-shutdown.service

snapd_files:
  - /snap
  - /var/snap
  - /var/lib/snapd
  - /var/cache/snapd
  - /run/snapd-snap.socket
  - /run/snapd.socket
  - /etc/apt/apt.conf.d/20snapd.conf

snapd_block_packages:
  - snapd
  - snap-confine
  - ubuntu-core-snapd-units
  - ubuntu-core-launcher
  - libsnapd-glib1
  - gir1.2-snapd-1
  - libsnapd-qt1
  - snapd-xdg-open
  - qml-module-snapd
```

### local Tests

With a locally installed and running dockerd, the role can be tested with different Ansible versions and operating system distributions:

```
make [-e TOX_ANSIBLE=ansible_${ansible_version}] [-e DISTRIBUTION=ubuntu:20.04]
```

---

## Author and License

- Bodo Schulz

## License

[BSD](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
