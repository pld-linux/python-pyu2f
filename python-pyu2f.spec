#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	U2F host library for interacting with a U2F device over USB
Summary(pl.UTF-8):	Biblioteka hosta U2F do współpracy z urządzeniami U2F po USB
Name:		python-pyu2f
Version:	0.1.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://github.com/google/pyu2f/releases
Source0:	https://github.com/google/pyu2f/archive/%{version}/pyu2f-%{version}.tar.gz
# Source0-md5:	5b10b5a1619466504b31f81b3945519c
Patch0:		%{name}-deps.patch
Patch1:		%{name}-mock.patch
URL:		https://github.com/google/pyu2f
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock >= 1.0.1
BuildRequires:	python-pyfakefs >= 2.4
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pyfakefs >= 2.4
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
%endif
Requires:	python-modules
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyu2f is a Python based U2F host library for Linux, Windows, and
MacOS. It provides functionality for interacting with a U2F device
over USB.

%description -l pl.UTF-8
pyu2f to pythonowa biblioteka hosta U2F dla Linuksa, Windows i
MacOS-a. Zapewnia funkcjonalność potrzebną do współpracy z
urządzeniami U2F po USB.

%package -n python3-pyu2f
Summary:	U2F host library for interacting with a U2F device over USB
Summary(pl.UTF-8):	Biblioteka hosta U2F do współpracy z urządzeniami U2F po USB
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-six

%description -n python3-pyu2f
pyu2f is a Python based U2F host library for Linux, Windows, and
MacOS. It provides functionality for interacting with a U2F device
over USB.

%description -n python3-pyu2f -l pl.UTF-8
pyu2f to pythonowa biblioteka hosta U2F dla Linuksa, Windows i
MacOS-a. Zapewnia funkcjonalność potrzebną do współpracy z
urządzeniami U2F po USB.

%prep
%setup -q -n pyu2f-%{version}
%patch0 -p1
%patch1 -p1

%build
%if %{with python2}
%py_build

%{?with_tests:py.test-2 pyu2f/tests}
%endif

%if %{with python3}
%py3_build

%{?with_tests:py.test-3 pyu2f/tests}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/pyu2f
%{py_sitescriptdir}/pyu2f-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyu2f
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/pyu2f
%{py3_sitescriptdir}/pyu2f-%{version}-py*.egg-info
%endif
