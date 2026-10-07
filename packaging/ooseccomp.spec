Name:           ooseccomp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Applies BPF seccomp filters restricting dangerous syscalls like ptrace and unshare.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooseccomp
Source0:        ooseccomp-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooseccomp is a sovereign, capability-bounded SYSCALL FILTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooseccomp
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooseccomp-uninstall

%files
/usr/bin/ooseccomp
/usr/bin/ooseccomp-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
