#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tgt
Version  : 1.0.75
Release  : 38
URL      : https://github.com/fujita/tgt/archive/v1.0.75.tar.gz
Source0  : https://github.com/fujita/tgt/archive/v1.0.75.tar.gz
Source1  : tgtd.service
Summary  : iSCSI Target STGT for Arch Linux
Group    : Development/Tools
License  : GPL-2.0
Requires: tgt-bin = %{version}-%{release}
Requires: tgt-data = %{version}-%{release}
Requires: tgt-license = %{version}-%{release}
Requires: tgt-man = %{version}-%{release}
Requires: tgt-services = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : libxslt-bin
BuildRequires : systemd-dev
Patch1: build.patch
Patch2: 0001-Stateless.patch
Patch3: 0002-Default-config.patch

%description
The SCSI target package contains the daemon and tools to setup a SCSI targets.
Currently, software iSCSI targets are supported.

%package bin
Summary: bin components for the tgt package.
Group: Binaries
Requires: tgt-data = %{version}-%{release}
Requires: tgt-license = %{version}-%{release}
Requires: tgt-services = %{version}-%{release}

%description bin
bin components for the tgt package.


%package data
Summary: data components for the tgt package.
Group: Data

%description data
data components for the tgt package.


%package doc
Summary: doc components for the tgt package.
Group: Documentation
Requires: tgt-man = %{version}-%{release}

%description doc
doc components for the tgt package.


%package license
Summary: license components for the tgt package.
Group: Default

%description license
license components for the tgt package.


%package man
Summary: man components for the tgt package.
Group: Default

%description man
man components for the tgt package.


%package services
Summary: services components for the tgt package.
Group: Systemd services

%description services
services components for the tgt package.


%prep
%setup -q -n tgt-1.0.75
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552575414
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags} SD_NOTIFY=1


%install
export SOURCE_DATE_EPOCH=1552575414
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tgt
cp scripts/deb/copyright %{buildroot}/usr/share/package-licenses/tgt/scripts_deb_copyright
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/tgtd.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tgt-admin
/usr/bin/tgt-setup-lun
/usr/bin/tgtadm
/usr/bin/tgtd
/usr/bin/tgtimg

%files data
%defattr(-,root,root,-)
%exclude /usr/share/defaults/tgt/examples/targets.conf.example
%exclude /usr/share/defaults/tgt/examples/targets.conf.vtl.L700
%exclude /usr/share/defaults/tgt/examples/targets.conf.vtl.MSL2024
/usr/share/defaults/tgt/targets.conf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/tgt/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tgt/scripts_deb_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/targets.conf.5
/usr/share/man/man8/tgt-admin.8
/usr/share/man/man8/tgt-setup-lun.8
/usr/share/man/man8/tgtadm.8
/usr/share/man/man8/tgtd.8
/usr/share/man/man8/tgtimg.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/tgtd.service
