%define upstream_version 20.0.1
Name:           python3-hyperlink
Version:        %{upstream_version}
Release:        0
Summary:        Pure-Python implementation of the URL
License:        MIT
URL:            https://github.com/sailfishos/python-hyperlink
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Hyperlink is a featureful, pure-Python implementation of the URL, with an
emphasis on correctness.

%prep
%autosetup -n %{name}-%{version}/upstream
# Remove bundled egg-info
rm -rf hyperlink.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/hyperlink
%{python3_sitelib}/hyperlink-%{upstream_version}-py%{python3_version}.egg-info/
