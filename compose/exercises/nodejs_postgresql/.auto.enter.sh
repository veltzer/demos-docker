site="postgres"
export env_db_user=$(jq -r ".[\"${site}\"][\"user\"]" ~/.passwords.json)
export env_db_password=$(jq -r ".[\"${site}\"][\"password\"]" ~/.passwords.json)
