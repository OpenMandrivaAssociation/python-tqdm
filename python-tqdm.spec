%global modname tqdm

Name:           python-%{modname}
Version:        4.41.0
Release:        1
Summary:        A Fast, Extensible Progress Meter
Group:          Development/Python
# see PACKAGE-LICENSING for more info
License:        MPLv2.0 and MIT
URL:            https://tqdm.github.io/
Source0:        https://github.com/tqdm/tqdm/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)

Recommends:     python3dist(pandas)
Recommends:     python3dist(numpy)

%global _description \
tqdm (read taqadum, تقدّم) means "progress" in Arabic.\
\
Instantly make your loops show a smart progress meter - just wrap any iterable\
with "tqdm(iterable)", and you are done!

%description %{_description}

%prep
%autosetup -p1 -n %{modname}-%{version}

# remove pre-built egg-info
rm -rf %{modname}.egg-info

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_mandir}/man1
mv -v %{buildroot}%{python_sitelib}/%{modname}/%{modname}.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENCE
%doc README.rst examples
%{_bindir}/%{modname}
%{_mandir}/man1/%{modname}.1*
%{python_sitelib}/%{modname}-*.egg-info/
%{python_sitelib}/%{modname}/
