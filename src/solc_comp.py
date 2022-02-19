import solcx

versions = solcx.get_installable_solc_versions()

# print(versions)

solcx.install_solc("0.8.9")

installed = solcx.get_solc_version()

print(installed)
