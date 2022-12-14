#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-types_toml
Version  : 0.10.8.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/c6/8b/a8544990966e9b475c1767f21272cbbdc2b470d4e690e04b5510b129b311/types-toml-0.10.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c6/8b/a8544990966e9b475c1767f21272cbbdc2b470d4e690e04b5510b129b311/types-toml-0.10.8.1.tar.gz
Summary  : Typing stubs for toml
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_toml-python = %{version}-%{release}
Requires: pypi-types_toml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the pypi-types_toml package.
Group: Default
Requires: pypi-types_toml-python3 = %{version}-%{release}

%description python
python components for the pypi-types_toml package.


%package python3
Summary: python3 components for the pypi-types_toml package.
Group: Default
Requires: python3-core
Provides: pypi(types_toml)

%description python3
python3 components for the pypi-types_toml package.


%prep
%setup -q -n types-toml-0.10.8.1
cd %{_builddir}/types-toml-0.10.8.1
pushd ..
cp -a types-toml-0.10.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668451133
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
