%global tl_name biblatex-sbl
%global tl_revision 78850

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Society of Biblical Literature (SBL) style files for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-sbl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-sbl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-sbl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX support for citations in the format
specified by the second edition of the Society of Biblical Literature
Handbook of Style, the SBLHS Student Supplement and updates published in
the SBLHS blog. Highlights include: Full support for every example in
the SBL Handbook of Style 2nd ed., SBLHS Student Supplement and SBLHS
blog. Documentation showing how to set up and cite bib entries for every
supported example. Advanced handling of first and subsequent citations
in running text and footnotes. Support for a variety of types of
reprints. Comprehensive support for abbreviations, including citing
reference works, ancient works and general abbreviations. Support for
citing ancient works by both source division and text collection page,
including indicating the translator if needed. German translation
strings.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-sbl
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-sbl
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-blog-examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-blog-examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-examples-preamble.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-handbook-examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-handbook-examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-studentsupplement-examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl-studentsupplement-examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-sbl/biblatex-sbl.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/american-sbl.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/biblatex-sbl.def
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/english-sbl.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/german-sbl.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/sbl.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/sbl.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/sbl.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-sbl/spanish-sbl.lbx
