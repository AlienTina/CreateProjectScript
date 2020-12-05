@echo off
SET mypath=%~dp0
SET pyscript=create.py
SET pydir=%mypath%%pyscript%
py %pydir% %1 %2