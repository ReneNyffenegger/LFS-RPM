Summary:	The Gettext package contains utilities for internationalization and localization	
Name:		tools-gettext
Version:	0.19.8.1
Release:	1
License:	GPL
URL:		http://ftp.gnu.org/gnu/gettext
Group:		LFS/Tools
Vendor:		Octothorpe
Distribution:	LFS-8.1
ExclusiveArch:	x86_64
Source0:	http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
%description
%prep
%setup -q -n gettext-%{version}
%build
	cd gettext-tools
	EMACS="no" ./configure \
		--prefix=%{_prefix} \
		--disable-shared
	make %{?_smp_mflags} -C gnulib-lib
	make %{?_smp_mflags} -C intl pluralx.c
	make %{?_smp_mflags} -C src msgfmt
	make %{?_smp_mflags} -C src msgmerge
	make %{?_smp_mflags} -C src xgettext
%install
	cd gettext-tools
	install -vdm 755 %{buildroot}/tools/bin
	cp -v src/{msgfmt,msgmerge,xgettext} %{buildroot}/tools/bin
	cd -
	#	Create file list
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
%files -f filelist.rpm
   %defattr(-,lfs,lfs)
%changelog
*	Mon Jan 01 2018 baho-utot <baho-utot@columbus.rr.com> 0.19.8.1-1
-	LFS-8.1