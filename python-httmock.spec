%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%define pkgname httmock

%define nose_version %nil
%if 0%{?rhel} <= 6
%define nose_version 1.1
%endif

Name: python-%{pkgname}
Summary: A mocking library for requests
Version: 1.2.3
Release: 2%{?dist}
License: Apache License, Version 2.0

Group: Development/Testing
URL: https://github.com/patrys/httmock
Source0: %{pkgname}-%{version}.tar.gz

Requires: python-requests >= 1.0.0
BuildRequires: python-requests >= 1.0.0
BuildRequires: python-nose%{nose_version}, python2-devel

BuildArch: noarch

%description
A mocking library for `requests` for Python 2.6, 2.7 and 3.2, 3.3.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__python2} setup.py build
nosetests%{nose_version} -v

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python2_sitelib}/httmock.py*
%{python2_sitelib}/httmock-*.egg-info

%doc README.md LICENSE

%changelog
* Fri Jun 03 2016 Vladislav Odintsov <odivlad@gmail.com> 1.2.3-2
- Fix build for el7 distros

* Mon Mar 16 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.2.3-1
- Update version.

* Fri Feb 06 2015 Mikhail Ushanov <gm.mephisto@gmail.com> 1.2.2-1
- Initial build.
