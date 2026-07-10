%global tl_name b1encoding
%global tl_revision 21271

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX encoding tools for Bookhands fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/b1encoding
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package characterises and defines the author's B1 encoding for use
with LaTeX when typesetting things using his Bookhands fonts.

