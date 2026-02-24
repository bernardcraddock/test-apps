import toml

programatic_config = {
    'title': 'TOML Example',
    'owner': {
        'name': 'John Doe',
        'dob': '1981-05-12T07:32:00-08:00'
    }
}

with open('programatic-config.toml', 'w') as fh:
    toml.dump(programatic_config, fh)
