Name:		texlive-b1encoding
Version:	1.0
Release:	1
Summary:	LaTeX encoding tools for Bookhands fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/b1encoding
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/b1encoding.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package characterises and defines the author's B1 encoding
for use with LaTeX when typesetting things using his Bookhands
fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/b1encoding/TeXB1.enc
%{_texmfdistdir}/tex/latex/b1encoding/b1cmr.fd
%{_texmfdistdir}/tex/latex/b1encoding/b1enc.def
%doc %{_texmfdistdir}/doc/latex/b1encoding/README
%doc %{_texmfdistdir}/doc/latex/b1encoding/b1encoding.pdf
#- source
%doc %{_texmfdistdir}/source/latex/b1encoding/b1encoding.dtx
%doc %{_texmfdistdir}/source/latex/b1encoding/b1encoding.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
