%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%define pkgname httmock
%global sum A mocking library for requests
%global descr A mocking library for `requests` for Python.

Name: python-%{pkgname}
Summary: %{sum}
Version: 1.3.0
Release: 2.CROC3%{?dist}
License: Apache License, Version 2.0

Group: Development/Testing
URL: https://github.com/patrys/httmock
Source0: %{pkgname}-%{version}.tar.gz

BuildArch: noarch

%description
%{descr}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:       %{sum}
%if 0%{?rhel} && 0%{?rhel} >=8
Requires:      python3-requests >= 1.0.0
%else
Requires:      python36-requests >= 1.0.0
%endif
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-requests >= 1.0.0
%if 0%{?rhel} && 0%{?rhel} >=8
BuildRequires: python3-nose
%else
BuildRequires: python36-nose
%endif

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}

%prep
%setup -q -n %{pkgname}-%{version}

%build
%py3_build

%check
nosetests-%{python3_version} -v

%install
[ %buildroot = "/" ] || rm -rf %buildroot

%py3_install

%clean
rm -rf %{buildroot}

%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%{python3_sitelib}/*

%doc README.md LICENSE

%changelog
* Mon Jan 16 2023 Ivan Konov <ikonov@croc.ru> 1.3.0-2.CROC3
- Fix package names for py3 builds
- Remove py2 support

* Thu Aug 1  2019 Vladislav Odintsov <odivlad@gmail.com> 1.3.0-2
- Update with upstream patches #58

* Thu Jul 18 2019 Vladislav Odintsov <odivlad@gmail.com> 1.3.0-1
- Update with upstream version 1.3.0

* Thu Jun 27 2019 Vladislav Odintsov <odivlad@gmail.com> 1.2.3-3
- Add support for py2/py3.x build

* Fri Jun 03 2016 Vladislav Odintsov <odivlad@gmail.com> 1.2.3-2
- Fix build for el7 distros

* Mon Mar 16 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.2.3-1
- Update version.

* Fri Feb 06 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.2.2-1
- Initial build.
