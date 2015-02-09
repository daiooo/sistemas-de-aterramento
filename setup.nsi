!define PRODUCT_NAME "Aterramento"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "LAMOTRIZ"
 
;SetCompressor lzma

!include "MUI2.nsh"
;!include "MUI.nsh"
 
; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\classic-install.ico"
 
; Welcome page
!insertmacro MUI_PAGE_WELCOME
; Components page
!insertmacro MUI_PAGE_COMPONENTS
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!insertmacro MUI_PAGE_FINISH
 
; Language files
!insertmacro MUI_LANGUAGE "Portuguese"
 
; Reserve files
;!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
 
; MUI end ------
 
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "setup.exe"
InstallDir "$PROGRAMFILES\aterramento"
ShowInstDetails show
 
Section -SETTINGS
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
SectionEnd

Section "ATERRAMENTO"

	File  src\acoes_interface.py
	File  src\aterramento.bat
	File  src\agilent_u2531a.py
	File  src\dataToTrainRfModel.mat
	File  src\demo_read_and_store_data.py
	
	CreateShortCut "$desktop\aterramento.lnk" "$INSTDIR\aterramento.bat"
	
	File  src\gera_py.bat
	File  src\load_data_mat_and_apply_rf.py
	File  src\projATT_functions.py
	File  src\projATT_getNumberofRods.py
	File  src\projATT_scaler_win.pckl
	File  src\projATT_strfore.pckl
	File  src\projATT_strfore_win.pckl
	File  src\setup_2.py
	File  src\setup.py
	File  src\sistemaAquisicao_python.py
	File  src\sistemaAquisicao.ui
	File  src\visa_linux_emulation.py
	
	SetOutPath $INSTDIR\figuras
	
	File  src\figuras\concema.png
	File  src\figuras\esquema_ligacao.dia
	File  src\figuras\esquema_ligacao.png
	File  src\figuras\esquema_ligacao.svg
	File  src\figuras\labterra.png
	File  src\figuras\LAMOTRIZ.png
	File  src\figuras\logo2.png
	File "src\figuras\Logo coelce endesa brasil12.jpg"
	File "src\figuras\LOGO P&D ANEEL (horizontal).jpg"	
	
	
	
SectionEnd

Section "ANACONDA" SEC02

	SetOutPath $INSTDIR\instaladores

  File "..\instaladores\Anaconda-2.1.0-Windows-x86_64.exe"
  ExecWait '"Anaconda-2.1.0-Windows-x86_64.exe"'
SectionEnd

;Section "PYVISA" SEC04
;	File "instala_pyvisa.bat"
;	ExecWait '"instala_pyvisa.bat"'
;SectionEnd

Section "PYQT4" SEC03

	SetOutPath $INSTDIR\instaladores
	
  File "..\instaladores\PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x64.exe"
  ExecWait '"PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x64.exe"'
SectionEnd


