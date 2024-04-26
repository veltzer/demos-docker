site="postgres"
env_db_user="postgres"
env_db_password=$(pass show "passwords/${site}/${env_db_user}")
export env_db_user
export env_db_password
