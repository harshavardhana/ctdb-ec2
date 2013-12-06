Summary: A Clustered Database based on Samba's Trivial Database (TDB) - EC2 support
Name: ctdb-ec2
Version: 1.0
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Daemons

Source0: %{name}-%{version}.tar.gz

Requires: ctdb >= 1.0.114.6

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: autoconf net-tools popt-devel

%description
CTDB ec2 support
