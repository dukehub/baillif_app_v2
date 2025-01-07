[Setup]
AppName=BailiffApp
AppVersion=1.0
DefaultDirName={pf}\BailiffApp
DefaultGroupName=BailiffApp
OutputDir=installer
OutputBaseFilename=BailiffApp_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\BailiffApp\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\BailiffApp"; Filename: "{app}\BailiffApp.exe"
Name: "{commondesktop}\BailiffApp"; Filename: "{app}\BailiffApp.exe"

[Run]
Filename: "{app}\BaillifApp.exe"; Description: "Lancer BaillifApp"; Flags: nowait postinstall skipifsilent 