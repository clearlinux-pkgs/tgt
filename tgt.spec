#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: 5424026
#
Name     : tgt
Version  : 1.0.94
Release  : 57
URL      : https://github.com/fujita/tgt/archive/v1.0.94/tgt-1.0.94.tar.gz
Source0  : https://github.com/fujita/tgt/archive/v1.0.94/tgt-1.0.94.tar.gz
Source1  : tgtd.service
Summary  : The SCSI target daemon and utility programs
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
Requires: systemd

%description services
services components for the tgt package.


%prep
%setup -q -n tgt-1.0.94
cd %{_builddir}/tgt-1.0.94
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a tgt-1.0.94 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1733238690
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  SD_NOTIFY=1

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}  SD_NOTIFY=1
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1733238690
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tgt
cp %{_builddir}/tgt-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/tgt/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/tgt-%{version}/scripts/deb/copyright %{buildroot}/usr/share/package-licenses/tgt/0017da1fb3304b439bdc64f2a6a7801c41790384 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/tgtd.service
## Remove excluded files
rm -f %{buildroot}*/usr/share/defaults/tgt/examples/targets.conf.example
rm -f %{buildroot}*/usr/share/defaults/tgt/examples/targets.conf.vtl.L700
rm -f %{buildroot}*/usr/share/defaults/tgt/examples/targets.conf.vtl.MSL2024
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/tgtadm
/V3/usr/bin/tgtd
/V3/usr/bin/tgtimg
/usr/bin/tgt-admin
/usr/bin/tgt-setup-lun
/usr/bin/tgtadm
/usr/bin/tgtd
/usr/bin/tgtimg

%files data
%defattr(-,root,root,-)
/usr/share/defaults/tgt/targets.conf

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/tgt/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tgt/0017da1fb3304b439bdc64f2a6a7801c41790384
/usr/share/package-licenses/tgt/4cc77b90af91e615a64ae04893fdffa7939db84c

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
