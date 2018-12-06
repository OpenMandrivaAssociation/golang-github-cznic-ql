# https://github.com/cznic/ql
%global goipath github.com/cznic/ql
Version:        1.2.0

%gometa

Name:           golang-github-cznic-ql
Summary:        Embedded SQL database written in Go
Release:        4%{?dist}
# This package is BSD licensed, but the vendored go4.org/lock library is ASLv2.0
License:        BSD and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

# Upstream patch to fix issue 208 (IN {empty set})
# https://github.com/cznic/ql/commit/d287cb6
Patch0:         00-fix-issue-208.patch

# Upstream patch to fix a nil dereference
# https://github.com/cznic/ql/commit/8e18b65
Patch1:         01-fix-nil-dereference.patch

BuildRequires:  golang(github.com/cznic/lldb)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/cznic/b)
BuildRequires:  golang(github.com/cznic/strutil)
BuildRequires:  golang(github.com/cznic/golex/lex)
Provides:       ql%{?_isa} = %{version}-%{release}


%description
%{summary}

%package        devel
Summary:        %{summary}

BuildRequires:  golang(github.com/cznic/b)
BuildRequires:  golang(github.com/cznic/golex/lex)
BuildRequires:  golang(github.com/cznic/lldb)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/cznic/strutil)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%build
%gobuildroot
%gobuild -o _bin/ql %{goipath}/ql


%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 _bin/ql %{buildroot}%{_bindir}
%goinstall


%check
%gochecks


%files
%license LICENSE
%doc README.md CONTRIBUTORS AUTHORS
%{_bindir}/ql


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTORS AUTHORS


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-4
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.2.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-2
- Fix some bugs (nil dereference, etc.) by including upstream patches.

* Mon Aug 13 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Update to version 1.2.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4.20171122.git3f53e14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3.20171122.git3f53e14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-2.20171122.git3f53e14
- Bump to commit 3f53e14.

* Wed Sep 06 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1.20170905.git8c32ff1
- Bump to commit 8c32ff1.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1.20170522.gitba9eea9
- Bump to commit ba9eea9.

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1.20170517.gitf39e59d
- First package for Fedora

