
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


### Tested on

- Debian 10
- Debian 11
- Debian 12
- Ubuntu 20.04
- Ubuntu 22.04
- Ubuntu 23.04

## usage

```
snapd_purge: true

snapd_state: stopped
snapd_enabled: false

snapd_block_later_installation: true

snapd_services:
  - snapd.service

snapd_files:
  - /etc/apt/apt.conf.d/20snapd.conf

snapd_block_packages: []
```

---

## Author and License

- Bodo Schulz

## License

[BSD](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
