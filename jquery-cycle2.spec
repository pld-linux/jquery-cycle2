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
Source2:	http://malsup.github.io/min/jquery.cycle2.carousel.min.js
# Source2-md5:	9cf68537eddd6a13f0f3429f99280a9f
Source3:	http://malsup.github.io/jquery.cycle2.carousel.js
# Source3-md5:	0ffe6e4b3a891a48e6bb978aa27afa86
Source4:	http://malsup.github.io/min/jquery.cycle2.flip.min.js
# Source4-md5:	d02e61e0d0199495ee0cb10f7da6a9c6
Source5:	http://malsup.github.io/jquery.cycle2.flip.js
# Source5-md5:	d330eb0285d3c19637663fa997f3bc9f
Source6:	http://malsup.github.io/min/jquery.cycle2.ie-fade.min.js
# Source6-md5:	dcfa4748d817d5caf0be589c78aedb1c
Source7:	http://malsup.github.io/jquery.cycle2.ie-fade.js
# Source7-md5:	7dde0761c751193ce76d70357d8bf57c
Source8:	http://malsup.github.io/min/jquery.cycle2.scrollVert.min.js
# Source8-md5:	eb217b6fbaf72793d84d937ddd97c69f
Source9:	http://malsup.github.io/jquery.cycle2.scrollVert.js
# Source9-md5:	78bf38a27e80f6a43fb0022474e8b8e9
Source10:	http://malsup.github.io/min/jquery.cycle2.shuffle.min.js
# Source10-md5:	7f0289d36f833f7576397918c2b17751
Source11:	http://malsup.github.io/jquery.cycle2.shuffle.js
# Source11-md5:	0065a47df1136ff1caceaf45263cc95b
Source12:	http://malsup.github.io/min/jquery.cycle2.tile.min.js
# Source12-md5:	aafe171bb8361751f385dcaa21edcf2d
Source13:	http://malsup.github.io/jquery.cycle2.tile.js
# Source13-md5:	a08b821412c3806d846c5133ff3e65ba
Source14:	http://malsup.github.io/min/jquery.cycle2.caption2.min.js
# Source14-md5:	fb931d675f1acb203a115b0312c7abad
Source15:	http://malsup.github.io/jquery.cycle2.caption2.js
# Source15-md5:	65c15d15fe72c35999fc25541b66980a
Source16:	http://malsup.github.io/min/jquery.cycle2.center.min.js
# Source16-md5:	ba58576292312d950b5fd9d079ad80a3
Source17:	http://malsup.github.io/jquery.cycle2.center.js
# Source17-md5:	c0e71d8bdbd4858202901767d56ba1e8
Source18:	http://malsup.github.io/min/jquery.cycle2.swipe.min.js
# Source18-md5:	a1310de18f5cbbf2c91cfd2fad7e19a0
Source19:	http://malsup.github.io/jquery.cycle2.swipe.js
# Source19-md5:	dada8bc5d4fbc6372ac0ab13282fba65
Source20:	http://malsup.github.io/min/jquery.cycle2.video.min.js
# Source20-md5:	95583506229e3f723e2c61080ed0e5a5
Source21:	http://malsup.github.io/jquery.cycle2.video.js
# Source21-md5:	a10789fb1dac19e6a66fd503c18b9400
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

install -d p

cp -p %{SOURCE2} p
cp -p %{SOURCE3} p
cp -p %{SOURCE4} p
cp -p %{SOURCE5} p
cp -p %{SOURCE6} p
cp -p %{SOURCE7} p
cp -p %{SOURCE8} p
cp -p %{SOURCE9} p
cp -p %{SOURCE10} p
cp -p %{SOURCE11} p
cp -p %{SOURCE12} p
cp -p %{SOURCE13} p
cp -p %{SOURCE14} p
cp -p %{SOURCE15} p
cp -p %{SOURCE16} p
cp -p %{SOURCE17} p
cp -p %{SOURCE18} p
cp -p %{SOURCE19} p
cp -p %{SOURCE20} p
cp -p %{SOURCE21} p

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

# plugins
for a in p/*; do
	sn=${a#*/jquery.%{plugin}.*}
	case "$sn" in
	*.min.js)
		cp -p $a $RPM_BUILD_ROOT%{_appdir}/$sn
		bn=${sn%.min.js}.js
		ln -s $sn $RPM_BUILD_ROOT%{_appdir}/$bn
		;;
	*.js)
		sn=${sn%.js}.src.js
		cp -p $a $RPM_BUILD_ROOT%{_appdir}/$sn
		;;
	esac
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
