Summary:	The Binutils package contains a linker, an assembler, and other tools for handling object files
Name:		binutils
Version:	2.29
Release:	1
License:	Any
URL:		Any
Group:		LFS/Base
Vendor:		Octothorpe
Distribution:	LFS-8.1
ExclusiveArch:	x86_64
Requires:	filesystem
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
%description
	The Binutils package contains a linker, an assembler, and other tools for handling object files
%prep
%setup -q -n %{NAME}-%{VERSION}
%build
	mkdir build
	cd build
	../configure \
		--prefix=%{_prefix} \
		--enable-gold \
		--enable-ld=default \
		--enable-plugins \
		--enable-shared \
		--disable-werror \
		--with-system-zlib
	make %{?_smp_mflags} tooldir=/usr
%install
	cd build
	make DESTDIR=%{buildroot} tooldir=/usr install
	cd -
	#	Copy license/copying file 
	#install -D -m644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
	#	Create file list
	rm  %{buildroot}/usr/share/info/dir
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
%files -f filelist.rpm
	%defattr(-,root,root)
%changelog
*	Tue Jan 09 2018 baho-utot <baho-utot@columbus.rr.com> -1
-	Initial build.	First version