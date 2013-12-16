Summary: EC2 support for Clustered Database based on Samba Trivial Database
Name: ctdb-ec2
Version: 1.1
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Daemons
URL: https://github.com/harshavardhana/ctdb-ec2
Source0: %{name}-%{version}.tar.gz
Requires: ctdb >= 1.0.114.6
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
EC2 support for Clustered Database based on Samba Trivial Database

%prep
%setup -q -n %{name}-%{version}

%build
make all

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ctdb

%{__install} -p -m 0644 ec2.rc %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0644 ec2-eni-functions %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0644 ec2-config %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0755 interface_modify_ec2.sh %{buildroot}%{_sysconfdir}/ctdb/interface_modify_ec2.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%config(noreplace) /etc/ctdb/ec2.rc
%config(noreplace) /etc/ctdb/ec2-eni-functions
%config(noreplace) /etc/ctdb/ec2-config
/etc/ctdb/interface_modify_ec2.sh

%post
if [ -f /etc/ctdb/interface_modify.sh ]; then
    %{__cp} -af /etc/ctdb/interface_modify.sh /etc/ctdb/interface_modify.sh.orig
    %{__cp} -af /etc/ctdb/interface_modify_ec2.sh /etc/ctdb/interface_modify.sh
fi

%postun
if [ -f /etc/ctdb/interface_modify.sh.orig ]; then
    %{__cp} -af /etc/ctdb/interface_modify.sh.orig /etc/ctdb/interface_modify.sh
    %{__rm} -f /etc/ctdb/interface_modify.sh.orig
fi

%changelog
* Mon Dec 09 2013 Harshavardhana <fharshav@redhat.com> - 1.0-1
- First import build
