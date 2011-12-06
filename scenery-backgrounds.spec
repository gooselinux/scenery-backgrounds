Name:           scenery-backgrounds
Version:        6.0.0
Release:        1%{?dist}
Summary:        Scenery desktop backgrounds

Group:          Applications/Multimedia
License:        CC-BY
URL:            http://www.redhat.com/

# This package has no upstream.
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
This package contains a collection of Creative Commons photos taken by Jenny
Downing and Luis Argerich of various peices of scenery.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/scenery/
install -m 644 backgrounds/scenery/*.jpg $RPM_BUILD_ROOT/%{_datadir}/backgrounds/scenery/
install -m 644 backgrounds/scenery/*.xml $RPM_BUILD_ROOT/%{_datadir}/backgrounds/scenery/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
install -m 644 gnome-background-properties/*.xml $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/gnome-background-properties/scenery.xml
%{_datadir}/backgrounds/scenery/*.xml
%{_datadir}/backgrounds/scenery/*.jpg

%changelog
* Wed Jun 02 2010 Ray Strode <rstrode@redhat.com> 6.0.0-1
- Initial import
