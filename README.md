
# Ansible Role:  `snapd`

disable and remove snapd

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-snapd/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-snapd)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-snapd)][releases]

[ci]: https://github.com/bodsch/ansible-snapd/actions
[issues]: https://github.com/bodsch/ansible-snapd/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-snapd/releases


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

---

## Author and License

- Bodo Schulz

## License

[BSD](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
