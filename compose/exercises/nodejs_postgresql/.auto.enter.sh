site="postgres"
env_db_user="postgres"
env_db_password=$(pass show "${site}/${env_db_user}")
export env_db_user
export env_db_password
