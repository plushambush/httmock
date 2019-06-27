%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%if 0%{?fedora} > 12 || 0%{?rhel} && 0%{?dist_raw} >= 75
%bcond_without python3
%else
%bcond_with python3
%endif

# centos 7.2 and lower versions don't have %py2_* macros, so define it manually
%if 0%{?rhel} && 0%{?dist_raw} <= 72
%{!?py2_build: %global py2_build %py_build}
%{!?py2_install: %global py2_install %py_install}
%endif

%define pkgname httmock
%global sum A mocking library for requests
%global descr A mocking library for `requests` for Python 2.6, 2.7 and 3.2, 3.3.

%define nose_version %nil
%if 0%{?rhel} <= 6
%define nose_version 1.1
%endif

Name: python-%{pkgname}
Summary: %{sum}
Version: 1.2.3
Release: 3%{?dist}
License: Apache License, Version 2.0

Group: Development/Testing
URL: https://github.com/patrys/httmock
Source0: %{pkgname}-%{version}.tar.gz


BuildArch: noarch

%description
%{descr}


%package -n python2-%{pkgname}
Summary:       %{sum}
Requires:      python-requests >= 1.0.0
BuildRequires: python2-devel
BuildRequires: python-requests >= 1.0.0
BuildRequires: python-nose%{nose_version}
Obsoletes:     python-httmock < 1.2.3-3%{?dist}

%description -n python2-%{pkgname}
%{descr}


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:       %{sum}
Requires:      python%{python3_pkgversion}-requests >= 1.0.0
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-requests >= 1.0.0
BuildRequires: python%{python3_pkgversion}-nose%{nose_version}

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}
%endif


%prep
%setup -q -n %{pkgname}-%{version}


%build
%py2_build

%if %{with python3}
%py3_build
%endif


%check
nosetests%{nose_version} -v

%if %{with python3}
nosetests%{nose_version}-%{python3_version} -v
%endif


%install
[ %buildroot = "/" ] || rm -rf %buildroot

%py2_install

%if %{with python3}
%py3_install
%endif


%clean
rm -rf %{buildroot}


%files -n python2-%{pkgname}
%defattr(-,root,root,-)
%{python2_sitelib}/*

%doc README.md LICENSE

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%{python3_sitelib}/*

%doc README.md LICENSE
%endif

%changelog
* Thu Jun 27 2019 Vladislav Odintsov <odivlad@gmail.com> 1.2.3-3
- Add support for py2/py3.x build

* Fri Jun 03 2016 Vladislav Odintsov <odivlad@gmail.com> 1.2.3-2
- Fix build for el7 distros

* Mon Mar 16 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.2.3-1
- Update version.

* Fri Feb 06 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.2.2-1
- Initial build.
