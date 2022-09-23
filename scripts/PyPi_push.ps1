Remove-Item "dist" -Recurse
python setup.py bdist_wheel
twine check dist/*
twine upload dist/*
