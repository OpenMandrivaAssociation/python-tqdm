%global modname tqdm

%bcond_with tests

Name:           python-%{modname}
Version:        4.41.0
Release:        %mkrel 1
Summary:        A Fast, Extensible Progress Meter
Group:          Development/Python
# see PACKAGE-LICENSING for more info
License:        MPLv2.0 and MIT
URL:            https://tqdm.github.io/
Source0:        https://github.com/tqdm/tqdm/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
tqdm (read taqadum, تقدّم) means "progress" in Arabic.\
\
Instantly make your loops show a smart progress meter - just wrap any iterable\
with "tqdm(iterable)", and you are done!

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%if %{with tests}
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
%endif
Recommends:     python3dist(pandas)
Recommends:     python3dist(numpy)

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -p1 -n %{modname}-%{version}

# remove pre-built egg-info
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man1
mv -v %{buildroot}%{python3_sitelib}/%{modname}/%{modname}.1 %{buildroot}%{_mandir}/man1/

%if %{with tests}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{modname}
%license LICENCE
%doc README.rst examples
%{_bindir}/%{modname}
%{_mandir}/man1/%{modname}.1*
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/
