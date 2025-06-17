if (Test-Path "dist") {
  Remove-Item "dist" -Recurse
}
python -m build --wheel
twine check dist/*
twine upload dist/*
