%define		plugin	cycle2
%define		build	20131003
%define		rel		1
Summary:	Cycle2 - 2nd Generation Cycling!
Name:		jquery-%{plugin}
Version:	1.0.0
Release:	0.%{build}.%{rel}
License:	MIT/GPL
Group:		Applications/WWW
Source0:	http://malsup.github.com/jquery.cycle2.js
# Source0-md5:	06d0d62d126920d684b14c564ba77b56
Source1:	http://malsup.github.com/min/jquery.cycle2.min.js
# Source1-md5:	3af89962e7aef2b9b7d2af7d4a0462e6
URL:		http://jquery.malsup.com/cycle2/
Requires:	jquery >= 1.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Cycle2 is a versatile slideshow plugin for jQuery built around
ease-of-use. It supports a declarative initialization style that
allows full customization without any scripting. Simply include the
plugin, declare your markup, and Cycle2 does the rest.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
