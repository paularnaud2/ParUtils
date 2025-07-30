venv\Scripts\Activate.ps1

if (Test-Path "dist") {
  Remove-Item "dist" -Recurse
}
if (Test-Path "build") {
  Remove-Item "build" -Recurse
}
python -m build --wheel
twine check dist/*
twine upload dist/*
