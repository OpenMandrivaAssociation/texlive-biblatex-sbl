Name:		texlive-biblatex-sbl
Version:	71470
Release:	1
Summary:	Society of Biblical Literature (SBL) style files for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-sbl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-sbl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-sbl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides BibLaTeX support for citations in the
format specified by the second edition of the Society of
Biblical Literature (SBL) Handbook of Style. All example notes
and bibliography entries from the handbook are supported and
shown in an example file. A style file for writing SBL student
papers is also included.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-sbl
%{_texmfdistdir}/makeindex/biblatex-sbl
%doc %{_texmfdistdir}/doc/latex/biblatex-sbl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
