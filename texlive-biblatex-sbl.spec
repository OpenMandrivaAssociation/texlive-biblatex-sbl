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
BuildSystem:	texlive
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

